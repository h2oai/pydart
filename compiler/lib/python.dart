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
  'opt': 'Optional',
  'func': 'Callable',
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
      switch (e.name) {
        case 'opt':
          return 'None';
        case 'List':
          return '[]';
        case 'Set':
          return 'set()';
        case 'Map':
          return '{}';
        case 'func':
          return '_noop';
      }

      if (e is IRClass) {
        final args = _getDefaultConstructorFields(e)
            .where((f) => !_isOptional(f.type))
            .map((f) => _defaultValueOf(f.type))
            .join(', ');
        return '${_n(e.name)}($args)';
      } else if (e is IREnum) {
        return '${_n(e.name)}.${_sc(e.values.first)}';
      }
    }

    throw 'cannot compute default value of ${t.name}';
  }

  bool _isOptional(IRType t) =>
      t is IRParameterizedType && t.element == IRElement.optional;

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
          if (fs.isNotEmpty) {
            p('super().__init__(');
            _emitDefaultArgs(e);
            p(')');
            return;
          }
        }
      }
    }
  }

  Iterable<IRField> _getDefaultConstructorFields(IRClass e) {
    final cs = e.constructors.where((c) => c.name.isEmpty);
    return cs.isNotEmpty ? cs.first.fields : [];
  }

  void _emitDefaultArgs(IRClass e) {
    p.t(() {
      final req =
          _getDefaultConstructorFields(e).where((f) => !_isOptional(f.type));
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
        if (isDefault && c.fields.isEmpty) continue;

        p('');
        if (!isDefault) {
          p('@staticmethod');
        }
        final name = isDefault ? '__init__' : _sc(c.name);
        p('def $name(');
        // Non-default params must precede default params, so separate them.
        final req = c.fields.where((f) => !_isOptional(f.type));
        final opt = c.fields.where((f) => _isOptional(f.type));
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
            p('${_sc(f.name)}: ${_toType(f.type)} = None,');
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

      // No fields/constructors or default param-less constructor only
      if (internalFields.isEmpty &&
          (e.constructors.isEmpty ||
              e.constructors.length == 1 &&
                  e.constructors.first.fields.isEmpty)) {
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

  static IRElement _refactor(IRElement e) {
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
            );
          }
          return f;
        }).toList();

        return IRClass(
          e.path,
          e.name,
          isAbstract: e.isAbstract,
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

  static String emit(List<IRElement> elements) => PythonTranslator()._emit(
      elements.where((e) => !_blacklist.contains(e.name)).map(_refactor));
}
