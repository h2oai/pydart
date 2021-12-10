import 'emit.dart';
import 'ir.dart';

// From Python 3.9.5
// >>> import keyword
// >>> keyword.kwlist
final _reservedWords = {
  'False',
  'None',
  'True',
  '__peg_parser__',
  'and',
  'as',
  'assert',
  'async',
  'await',
  'break',
  'class',
  'continue',
  'def',
  'del',
  'elif',
  'else',
  'except',
  'finally',
  'for',
  'from',
  'global',
  'if',
  'import',
  'in',
  'is',
  'lambda',
  'nonlocal',
  'not',
  'or',
  'pass',
  'raise',
  'return',
  'try',
  'while',
  'with',
  'yield'
};

final _builtins = {
  'void': 'None',
  'bool': 'bool',
  'int': 'int',
  'double': 'float',
  'String': 'str',
  'dynamic': 'Any',
  'Nullable': 'Optional',
  'Function': 'Callable',
  'Map': 'Dict',
};

class Pair<T1, T2> {
  final T1 a;
  final T2 b;

  Pair(this.a, this.b);
}

// Symbols already available via Python's typing.*:
// FIXME don't emit elements referenced only by blacklisted types
// e.g. EfficientLengthIterable
final _blacklist = {
  'Iterable',
  'List',
  'Map',
  'MapEntry',
  'DoNothingIntent',
  '_StringStackTrace'
};

// Recursive references like this confuse Python:
// |
// | class DoNothingIntent(Intent):
// |     pass
// |
// | class Intent(Object):
// |     do_nothing: DoNothingIntent = DoNothingIntent(...)
// |
// Fix: Blacklist class DoNothingIntent and change type of doNothing to Intent.
final _refactorings = [
  Pair('Intent', 'doNothing'),
  Pair('StackTrace', 'empty')
];

String _snakeCase(String s) => s
    .replaceAllMapped(
        RegExp(r'([a-z0-9])([A-Z])'), (m) => '${m[1]}_${m[2]}'.toLowerCase())
    .toLowerCase();

String _n(String s) {
  final b = _builtins[s];
  if (b != null) return b;
  return _reservedWords.contains(s) ? '${s}_' : s;
}

String _sc(String s) => _n(_snakeCase(s));

bool _isOptional(IRField f) =>
    f.isOptional || (f.isRequired && isNullable(f.type));

Iterable<IRField> _getDefaultConstructorFields(IRClass e) {
  final cs = e.constructors.where((c) => c.name.isEmpty);
  return cs.isNotEmpty ? cs.first.fields : [];
}

class PythonTranslator {
  final p = Printer('    ');
  final _declaredNames = {..._builtins.values, ..._blacklist};

  String _toConst(IRConst c) {
    if (c is IRInt) {
      return '${c.value}';
    } else if (c is IRDouble) {
      return '${c.value}';
    } else if (c is IRBool) {
      return c.value ? 'True' : 'False';
    } else if (c is IRString) {
      return "'${c.value}'"; // TODO escape properly
    }
    return 'UNDEFINED';
  }

  String _toType(IRType t, {failIfNotDeclared = false}) {
    if (t is IRParameterizedType) {
      final ps = t.parameters.map(_toType).toList();
      final params = t.parameters.isNotEmpty
          ? (t.element == IRElement.func)
              // 'Callable' must be used as 'Callable[[arg, ...], result]'
              ? '[[${comma(ps.sublist(0, ps.length - 1))}], ${ps.last}]'
              : '[${comma(ps)}]'
          : '';
      final name = _n(t.name);
      final sig = '$name$params';
      if (_declaredNames.contains(name)) return sig;
      if (failIfNotDeclared) throw 'undeclared symbol $sig';
      return "'$sig'";
    }
    if (t is IRTypeParameter) {
      // TODO handle bound?
      return t.name;
    }

    final builtin = _builtins[t.name];
    if (builtin != null) return builtin;

    throw 'unknown type ${t.name}';
  }

  String _toDeclaredType(IRType t) => _toType(t, failIfNotDeclared: true);

  String _defaultValueOf(IRType t) {
    if (t == IRType.bool) return 'False';
    if (t == IRType.int) return '0';
    if (t == IRType.double) return '0.0';
    if (t == IRType.string) return "''";

    if (t is IRParameterizedType) {
      final e = t.element;
      if (e == IRElement.func) return '_noop';
      if (e == IRElement.nullable) return 'None';
      switch (e.name) {
        case 'List':
          return '[]';
        case 'Set':
          return 'set()';
        case 'Map':
          return '{}';
      }

      if (e is IRClass) {
        final args = _getDefaultConstructorFields(e)
            .where((f) => !_isOptional(f))
            .map((f) => _defaultValueOf(f.type))
            .join(', ');
        return '${_n(e.name)}($args)';
      } else if (e is IREnum) {
        return '${_n(e.name)}.${_sc(e.values.first)}';
      }
    }

    throw 'cannot compute default value of ${t.name}';
  }

  bool _typeRefersTo(IRType t, IRElement e) =>
      t is IRParameterizedType && t.element == e;

  void _emitSuperCall(IRClass c) {
    for (final s in c.supertypes) {
      if (s is IRParameterizedType) {
        final e = s.element;
        // Emit a super() call even if the base class constructor has only
        // optional args, otherwise PyCharm's type checker will complain.
        if (e is IRClass) {
          final fs = _getDefaultConstructorFields(e);
          p('super().__init__(');
          _emitDefaultArgs(e);
          p(')');
          return; // bail out after printing first available super() call
        }
      }
    }
  }

  void _emitDefaultArgs(IRClass e) {
    p.t(() {
      final req = _getDefaultConstructorFields(e).where((f) => !_isOptional(f));
      for (final f in req) {
        p('${_sc(f.name)}=${_defaultValueOf(f.type)},');
      }
    });
  }

  void _emitClass(IRClass e) {
    final abstracts = e.isAbstract ? ['ABC'] : <String>[];
    final parameters = e.parameters.isNotEmpty
        ? ['Generic[${comma(e.parameters.map(_toType))}]']
        : <String>[];
    final superTypes = e.supertypes.map(_toDeclaredType);
    final interfaces = e.interfaces.map(_toDeclaredType);
    final inherits = [
      ...interfaces,
      ...superTypes,
      ...abstracts,
      ...parameters,
    ];
    final klass = _n(e.name);
    final base = inherits.isNotEmpty ? '(${comma(inherits)})' : '';

    // Python doesn't handle recursive type definitions: static fields of the
    // same type as the containing class need to be assigned after the class
    // definition.
    final internalFields = e.fields.where((f) => !_typeRefersTo(f.type, e));
    final constFields = internalFields.where((f) => f.type.isPrimitive);
    final nonConstFields = internalFields.where((f) => !f.type.isPrimitive);
    final externalFields = e.fields.where((f) => _typeRefersTo(f.type, e));

    if (nonConstFields.isNotEmpty) {
      final types = <String, IRType>{};
      for (final f in nonConstFields) {
        types[_toType(f.type)] = f.type;
      }
      types.forEach((t, v) {
        if (v is IRParameterizedType) {
          final element = v.element;
          if (element is IRClass) {
            p('');
            p('');
            p('def _${_sc(klass)}__${_sc(t)}(_k: str) -> $t:');
            p.t(() {
              p('_o = $t(');
              _emitDefaultArgs(element);
              p(')');
              p("_o._nx_ = {'#t': ('${e.name}', _k)}");
              p('return _o');
            });
          }
        }
      });
    }

    p('');
    p('');
    p('# ${e.path}');
    p('class $klass$base:');
    p.t(() {
      // foo: float = 42.0
      for (final f in constFields) {
        p('${_sc(f.name)}: ${_toType(f.type)} = ${_toConst(f.value)}');
      }
      // a_foo_bar: FooBar = _container__foo_bar('aFooBar')
      for (final f in nonConstFields) {
        final t = _toType(f.type);
        p("${_sc(f.name)}: $t = _${_sc(e.name)}__${_sc(t)}('${f.name}')");
      }

      for (final c in e.constructors) {
        final isDefault = c.name.isEmpty;
        // Don't emit default constructor if empty

        p('');
        if (!isDefault) {
          p('@staticmethod');
        }
        final name = isDefault ? '__init__' : _sc(c.name);
        p('def $name(');
        // Non-default params must precede default params, so separate them.
        final req = c.fields.where((f) => !_isOptional(f));
        final opt = c.fields.where(_isOptional);
        p.t(() {
          if (isDefault) {
            p('self,');
          }
          // foo: Foo,
          for (final f in req) {
            p('${_sc(f.name)}: ${_toType(f.type)},');
          }
          // foo: Optional[Foo] = None,
          for (final f in opt) {
            final t = isNullable(f.type) ? f.type : toNullable(f.type);
            p('${_sc(f.name)}: ${_toType(t)} = None,');
          }
        });
        p('):');
        p.t(() {
          final self = isDefault ? 'self' : '_o';
          if (isDefault) {
            _emitSuperCall(e);
          } else {
            p('$self = $klass(');
            _emitDefaultArgs(e);
            p(')');
          }

          p("$self._nx_ = {");
          p.t(() {
            p("'#t': ('${e.name}', '${c.name}'),");
            for (final f in [...req, ...opt]) {
              p("'${f.name}': ${_sc(f.name)},");
            }
          });
          p('}');

          if (!isDefault) {
            p('return $self');
          }
        });
      }

      // No fields/constructors
      if (internalFields.isEmpty && e.constructors.isEmpty) {
        p('pass');
      }
    });

    if (externalFields.isNotEmpty) {
      p('');
      p('');
      for (final f in externalFields) {
        // Foo.bar = Foo(
        // )
        // Foo.bar._nx_ = {'#t': ('Foo', 'bar')}
        //
        final attr = _sc(f.name);
        p('$klass.$attr = $klass(');
        _emitDefaultArgs(e);
        p(')');
        p("$klass.$attr._nx_ = {'#t': ('${e.name}', '${f.name}')}");
      }
    }

    _declaredNames.add(klass);
  }

  void _emitEnum(IREnum e) {
    final name = _n(e.name);
    p('');
    p('');
    p('# ${e.path}');
    p('class $name(Enum):');
    p.t(() {
      for (final v in e.values) {
        p("${_sc(v)} = '$v'");
      }
    });

    _declaredNames.add(name);
  }

  void _collectTypeVars(IRType t, Set<String> typeVars) {
    if (t is IRParameterizedType) {
      for (final p in t.parameters) {
        _collectTypeVars(p, typeVars);
      }
    } else if (t is IRTypeParameter) {
      typeVars.add(t.name);
    }
  }

  void _emitTypeVars(Iterable<IRElement> elements) {
    final typeVars = <String>{};
    for (final e in elements) {
      if (e is IRClass) {
        for (final t in [...e.parameters, ...e.supertypes, ...e.interfaces]) {
          _collectTypeVars(t, typeVars);
        }
      }
    }

    for (final t in typeVars) {
      p("$t = TypeVar('$t')");
    }
  }

  String _emit(Iterable<IRElement> elements) {
    p('from abc import ABC');
    p('from enum import Enum');
    p('from typing import Generic, TypeVar, Callable, Any, Optional, Iterable, List, Dict');
    p('');
    p('');
    p('def _noop(*args, **kwargs) -> Any:');
    p("    raise f'_noop({args}, {kwargs})'");
    p('');
    p('');

    _emitTypeVars(elements);

    for (final e in elements) {
      if (e is IRClass) {
        _emitClass(e);
      } else if (e is IREnum) {
        _emitEnum(e);
      }
    }

    return p.lines.join();
  }

  static String emit(Iterable<IRElement> elements) =>
      PythonTranslator()._emit(elements);
}

Iterable<IRElement> refactor(Iterable<IRElement> elements) =>
    elements.where((e) => !_blacklist.contains(e.name)).map(_refactor);

IRElement _refactor(IRElement e) {
  for (final refactoring in _refactorings) {
    final targetClass = refactoring.a;
    final targetField = refactoring.b;
    if (e is IRClass && e.name == targetClass) {
      final fields = e.fields.map((f) {
        if (f.name == targetField) {
          return IRField(
            name: f.name,
            type: IRParameterizedType(e, []),
            value: f.value,
            isPositional: f.isPositional,
            isRequired: f.isRequired,
            isOptional: f.isOptional,
            hasDefaultValue: f.hasDefaultValue,
          );
        }
        return f;
      }).toList();

      return IRClass(
        e.path,
        e.name,
        isAbstract: e.isAbstract,
        isInternal: e.isInternal,
        parameters: e.parameters,
        supertypes: e.supertypes,
        interfaces: e.interfaces,
        constructors: e.constructors,
        fields: fields,
        dartElement: e.dartElement,
      );
    }
  }

  return e;
}

class Seq {
  final int start;
  int i = 0;

  Seq(this.start) {
    i = start;
  }

  int call() => i++;

  void reset() => i = start;
}

class PythonTestGenerator {
  final _seq = Seq(42);
  late Map<String, IRClass> _subclasses;

  PythonTestGenerator(Iterable<IRElement> elements) {
    _subclasses = _identifySubclasses(elements);
    assert(_subclasses.isNotEmpty);
  }

  static String _classKey(IRClass e) => '${e.name} ${e.path}';

  static Map<String, IRClass> _identifySubclasses(
      Iterable<IRElement> elements) {
    final classes = elements.whereType<IRClass>();
    final subtypes = <String, IRClass>{};
    for (final c in classes) {
      for (final st in [...c.supertypes, ...c.interfaces]) {
        if (st is IRParameterizedType) {
          final ste = st.element;
          if (ste is IRClass) {
            final key = _classKey(ste);
            if (!subtypes.containsKey(key)) {
              subtypes[key] = c;
            }
          }
        }
      }
    }
    return subtypes;
  }

  IRClass? _findSubclass(IRClass e) {
    IRClass? sc = _subclasses[_classKey(e)];
    while (sc != null && sc.isAbstract) {
      sc = _subclasses[_classKey(sc)];
    }
    return sc;
  }

  String _make(IRType t) {
    if (t == IRType.bool) return 'True';
    if (t == IRType.int) return '${_seq()}';
    if (t == IRType.double) return '0.${_seq()}';
    if (t == IRType.string) return "'String ${_seq()}'";

    if (t is IRParameterizedType) {
      final e = t.element;
      if (e == IRElement.func) return '_noop';
      if (e == IRElement.nullable) return _make(t.parameters.first);
      switch (e.name) {
        case 'List':
          final items = _rands(t.parameters.first).join(', ');
          return '[$items]';
        case 'Set':
          final items = _rands(t.parameters.first).join(', ');
          return 'set($items)';
        case 'Map':
          final items = [1, 2, 3]
              .map((_) =>
                  '${_make(t.parameters.first)}: ${_make(t.parameters.last)}')
              .join(', ');
          return '{$items}';
      }

      if (e is IRClass) {
        final c = e.isAbstract ? _findSubclass(e) : e;
        if (c != null) {
          return '_sample_${_sc(c.name)}()';
        } else {
          return '_notfound_${_sc(e.name)}()';
        }
      } else if (e is IREnum) {
        return '${_n(e.name)}.${_sc(e.values.last)}';
      }
    }

    return 'undefined'; // reaching here is an error
  }

  Iterable<String> _rands(IRType t) => [1, 2, 3].map((_) => _make(t));

  void _emitTestFields(Printer p, Iterable<IRField> fields) {
    p.t(() {
      _seq.reset();
      for (final f in fields) {
        p('${_sc(f.name)}=${_make(f.type)},');
      }
    });
  }

  void _emitGenFunc(Printer p, Printer p2, IRElement e, IRConstructor c) {
    final req = c.fields.where((f) => !_isOptional(f));
    final opt = c.fields.where(_isOptional);
    final filename = c.name.isEmpty ? e.name : '${e.name}_${c.name}';
    final ctorName = c.name.isEmpty ? e.name : '${_n(e.name)}.${_sc(c.name)}';
    final funcName = _sc(c.name.isEmpty ? e.name : '${e.name}__${c.name}');
    final all = [...req, ...opt];
    p2("('$filename', _sample_$funcName()),");
    p('');
    p('');
    p('def _sample_$funcName():');
    p.t(() {
      p('return $ctorName(');
      _emitTestFields(p, all);
      p(')');
    });
    if (opt.isNotEmpty) {
      p2("('$filename.min', _min_sample_$funcName()),");
      p('');
      p('');
      p('def _min_sample_$funcName():');
      p.t(() {
        p('return $ctorName(');
        _emitTestFields(p, req);
        p(')');
      });
    }
  }

  String _emit(Iterable<IRElement> elements) {
    final p = Printer('    ');
    p('from h2o_nitro import *');

    final p2 = Printer('    ');
    p2('');
    p2('dump_list = [');

    p2.t(() {
      for (final e in elements) {
        if (e is IRClass && !e.isAbstract) {
          for (final c in e.constructors) {
            _emitGenFunc(p, p2, e, c);
          }
        }
      }
    });
    p2(']');

    p.lines.addAll(p2.lines);
    return p.lines.join();
  }

  static String emit(Iterable<IRElement> elements) =>
      PythonTestGenerator(elements)._emit(elements);
}
