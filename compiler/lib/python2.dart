import 'package:analyzer/dart/element/type.dart';

import 'ir.dart';
import 'emit.dart';

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
  'float': 'float',
  'str': 'str',
  'any': 'Any',
  'opt': 'Optional',
  'func': 'Callable',
};

String _snakeCase(String s) => s
    .replaceAllMapped(
        RegExp(r'([a-z0-9])([A-Z])'), (m) => '${m[1]}_${m[2]}'.toLowerCase())
    .toLowerCase();

String _n(String s) => _reservedWords.contains(s) ? '${s}_' : s;

String _sc(String s) => _n(_snakeCase(s));

class PythonTranslator {
  final p = Printer('    ');

  String _toType(IRType t) {
    if (t is IRParameterizedType) {
      final params = t.parameters.isNotEmpty
          ? '[${comma(t.parameters.map(_toType))}]'
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

  void _emitClass(IRClass e) {
    final parameters = e.parameters.isNotEmpty
        ? ['Generic[${comma(e.parameters.map(_toType))}]']
        : <String>[];
    final superTypes = e.supertypes.map(_toType);
    final interfaces = e.interfaces.map(_toType);
    final inherits = [...parameters, ...superTypes, ...interfaces];
    final base = inherits.isNotEmpty ? '(${comma(inherits)})' : '';

    p('');
    p('');
    p('class ${_n(e.name)}$base:');
    p.t(() {
      p('pass');
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

  void _collectTypeVars(IRType t, Set<String> vars) {
    if (t is IRParameterizedType) {
      for (final p in t.parameters) {
        _collectTypeVars(p, vars);
      }
    } else if (t is IRTypeParameter) {
      vars.add(t.name);
    }
  }

  String _emit(List<IRElement> elements) {
    p('from enum import Enum');
    p('from typing import Generic, TypeVar, Callable, Any, Optional, Iterable, List, Dict');
    p('');

    final vars = <String>{};
    for (final e in elements) {
      if (e is IRClass) {
        for (final t in [...e.parameters, ...e.supertypes, ...e.interfaces]) {
          _collectTypeVars(t, vars);
        }
      }
    }

    for (final v in vars) {
      p("$v = TypeVar('$v')");
    }

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