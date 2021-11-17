
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
  'str': 'str',
  'any': 'Any',
  'opt': 'Optional',
  'func': 'Callable',
};

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

  String _toType(IRType t) {
    if (t is IRParameterizedType) {
      final ps = t.parameters.map(_toType).toList();
      final params = t.parameters.isNotEmpty
          ? (t.element == IRElement.func)
              // 'Callable' must be used as 'Callable[[arg, ...], result]'
              ? '[[${comma(ps.sublist(0, ps.length - 1))}], ${ps.last}]'
              : '[${comma(ps)}]'
          : '';
      return '${_n(t.name)}$params';
    }
    if (t is IRTypeParameter) {
      // XXX handle bound
      return t.name;
    }

    final builtin = _builtins[t.name];
    if (builtin != null) return builtin;

    throw 'unknown type ${t.name}';
  }

  bool _isOptional(IRType t) =>
      t is IRParameterizedType && t.element == IRElement.optional;

  bool _typeRefersTo(IRType t, IRElement e) =>
      t is IRParameterizedType && t.element == e;

  void _emitClass(IRClass e) {
    final abstracts = e.isAbstract ? ['ABC'] : <String>[];
    final parameters = e.parameters.isNotEmpty
        ? ['Generic[${comma(e.parameters.map(_toType))}]']
        : <String>[];
    final superTypes = e.supertypes.map(_toType);
    final interfaces = e.interfaces.map(_toType);
    final inherits = [
      ...abstracts,
      ...parameters,
      ...superTypes,
      ...interfaces
    ];
    final base = inherits.isNotEmpty ? '(${comma(inherits)})' : '';

    // Python doesn't handle recursive type definitions: static fields of the
    // same type as the containing class need to be assigned after the class
    // definition.
    final internalFields = e.fields.where((f) => !_typeRefersTo(f.type, e));
    final primitiveInternalFields =
        internalFields.where((f) => f.type.isPrimitive);
    final complexInternalFields =
        internalFields.where((f) => !f.type.isPrimitive);
    final externalFields = e.fields.where((f) => _typeRefersTo(f.type, e));

    if (complexInternalFields.isNotEmpty) {
      final ctors = Set.from(complexInternalFields.map((f) => _toType(f.type)));
      for (final t in ctors) {
        p('');
        p('');
        p('def _${_sc(e.name)}__${_sc(t)}(_k: str) -> $t:');
        p.t(() {
          p('_o = $t(');
          p(')');
          p("_o.__ctor = (('${e.name}', _k),)");
          p('return _o');
        });
      }
    }

    p('');
    p('');
    p('class ${_n(e.name)}$base:');
    p.t(() {
      // foo: float = 42.0
      for (final f in primitiveInternalFields) {
        p('${_sc(f.name)}: ${_toType(f.type)} = ${_toConst(f.value)}');
      }
      // a_foo_bar: FooBar = _container__foo_bar('aFooBar')
      for (final f in complexInternalFields) {
        final t = _toType(f.type);
        p("${_sc(f.name)}: $t = _${_sc(e.name)}__${_sc(t)}('${f.name}')");
      }
      if (internalFields.isNotEmpty) {
        p('');
      }

      for (final c in [e.constructor, ...e.constructors]) {
        if (c.name.isNotEmpty) {
          p('');
          p('@staticmethod');
        }
        final name = c.name.isEmpty ? '__init__' : _sc(c.name);
        p('def $name(');
        // Non-default params must precede default params, so separate them.
        final req = c.fields.where((f) => !_isOptional(f.type));
        final opt = c.fields.where((f) => _isOptional(f.type));
        p.t(() {
          p('self,');
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
          p("self.__ctor = (('${c.name}',), (");
          p.t(() {
            for (final f in [...req, ...opt]) {
              p("'${f.name}', ${_sc(f.name)},");
            }
          });
          p('))');
        });
      }
    });
  }

  void _emitEnum(IREnum e) {
    p('');
    p('');
    p('class ${_n(e.name)}(Enum):');
    p.t(() {
      for (final v in e.values) {
        p("${_sc(v)} = '$v'");
      }
    });
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

  void _emitTypeVars(List<IRElement> elements) {
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

  String _emit(List<IRElement> elements) {
    p('from abc import ABC');
    p('from enum import Enum');
    p('from typing import Generic, TypeVar, Callable, Any, Optional, Iterable, List, Dict');
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

  static String emit(List<IRElement> elements) =>
      PythonTranslator()._emit(elements);
}
