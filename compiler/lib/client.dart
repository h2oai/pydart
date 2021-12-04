import 'emit.dart';
import 'ir.dart';

class Expr {}

class IdExpr extends Expr {
  final String name;

  IdExpr(this.name);

  @override
  String toString() => name;
}

class ConstExpr extends Expr {
  final IRConst value;

  ConstExpr(this.value);

  @override
  String toString() => value.toString();
}

class CallExpr extends Expr {
  final Expr subject;
  final List<IRType> parameters;
  final List<Expr> arguments;

  CallExpr(this.subject, this.parameters, this.arguments);

  @override
  String toString() {
    final args = arguments.join(', ');
    final params = parameters.map((p) => dumpType(p)).join(', ');
    return parameters.isNotEmpty
        ? '$subject<$params>($args)'
        : '$subject($args)';
  }
}

final nullExpr = IdExpr('null');

class LiteralExpr extends Expr {
  final String literal;

  LiteralExpr(this.literal);

  @override
  String toString() => literal;
}

class StringLiteralExpr extends Expr {
  final String literal;

  StringLiteralExpr(this.literal);

  @override
  String toString() => "'$literal'";
}

class AttrExpr extends Expr {
  final Expr subject;
  final Expr attribute;

  AttrExpr(this.subject, this.attribute);

  @override
  String toString() => '$subject.$attribute';
}

class BinaryExpr extends Expr {
  final Expr left;
  final String operator;
  final Expr right;

  BinaryExpr(this.left, this.operator, this.right);

  @override
  String toString() => '$left $operator $right';
}

class TernaryExpr extends Expr {
  final Expr cond;
  final Expr whenTrue;
  final Expr whenFalse;

  TernaryExpr(this.cond, this.whenTrue, this.whenFalse);

  @override
  String toString() => '($cond ? $whenTrue : $whenFalse)';
}

class LambdaExpr extends Expr {
  final List<Expr> parameters;
  final Expr body;

  LambdaExpr(this.parameters, this.body);

  @override
  String toString() => "(${parameters.join(', ')}) => $body";
}

Expr Function() _gensym(String prefix) {
  var i = 0;
  return () => IdExpr('$prefix${++i}');
}

String capitalize(String s) =>
    (s.isEmpty) ? s : s.substring(0, 1).toUpperCase() + s.substring(1);

String _toConstructorSymbol(IRClass e, IRConstructor c) =>
    e.name + capitalize(c.name);

Expr _die(String message) =>
    CallExpr(IdExpr('die'), [], [StringLiteralExpr(message)]);

Expr _unmarshal(IRType t, Expr x) {
  if (t.isPrimitive) {
    return CallExpr(IdExpr('u' + capitalize(t.name)), [], [x]);
  }
  if (t is IRParameterizedType) {
    final e = t.element;
    if (e == IRElement.nullable) {
      final p = t.parameters.first;
      return TernaryExpr(
          BinaryExpr(x, '!=', nullExpr), _unmarshal(p, x), nullExpr);
    }
    if (e.name == 'List') {
      final p = t.parameters.first;
      return TernaryExpr(
          BinaryExpr(x, 'is', LiteralExpr('List<dynamic>')),
          CallExpr(
              AttrExpr(
                  CallExpr(AttrExpr(x, IdExpr('map')), [], [
                    LambdaExpr([IdExpr('v')], _unmarshal(p, IdExpr('v')))
                  ]),
                  IdExpr('toList')),
              [],
              []),
          _die('not a list'));
    }
    if (e.name == 'Set') {
      final p = t.parameters.first;
      return TernaryExpr(
          BinaryExpr(x, 'is', LiteralExpr('List<dynamic>')),
          CallExpr(
              AttrExpr(
                  CallExpr(AttrExpr(x, IdExpr('map')), [], [
                    LambdaExpr([IdExpr('v')], _unmarshal(p, IdExpr('v')))
                  ]),
                  IdExpr('toSet')),
              [],
              []),
          _die('not a list'));
    }
    if (e.name == 'Map') {
      final pk = t.parameters[0];
      final pv = t.parameters[1];
      return TernaryExpr(
          BinaryExpr(x, 'is', LiteralExpr('Map<dynamic, dynamic>')),
          CallExpr(AttrExpr(x, IdExpr('map')), [], [
            LambdaExpr(
                [IdExpr('k'), IdExpr('v')],
                CallExpr(IdExpr('MapEntry'), [],
                    [_unmarshal(pk, IdExpr('k')), _unmarshal(pv, IdExpr('v'))]))
          ]),
          _die('not a map'));
    }

    if (e == IRElement.func) return CallExpr(IdExpr('uFunc'), [t], [x]);

    if (e is IREnum) return CallExpr(IdExpr('_u${e.name}'), [], [x]);

    // TODO constructor-tearoffs
    // Ideally this would be passed as uClass<T>, but causes the compiler to
    //  complain with "This requires the 'constructor-tearoffs' language
    //  feature to be enabled."
    // https://github.com/dart-lang/language/blob/master/accepted/future-releases/constructor-tearoffs/feature-specification.md
    if (e is IRClass) return CallExpr(IdExpr('uClass'), [t], [x]);
  }

  if (t is IRTypeParameter) return CallExpr(IdExpr('uClass'), [t], [x]);

  throw 'could not determine unmarshaler for ${t.name}';
}

void _collectTypeParameters(
    List<IRTypeParameter> params, Iterable<IRType> types) {
  for (final t in types) {
    if (t is IRTypeParameter) {
      params.add(t);
    } else if (t is IRParameterizedType) {
      _collectTypeParameters(params, t.parameters);
    }
  }
}

class ClientTranslator {
  final p = Printer('  ');

  void _emitClass(IRClass e) {
    final m = '__m';
    for (final c in e.constructors) {
      final params = <IRTypeParameter>[];
      _collectTypeParameters(params, c.fields.map((f) => f.type));

      final typeParams =
          params.isNotEmpty ? "<${params.map((p) => p.name).join(', ')}>" : '';

      final gensym = _gensym('__m');

      p('');
      p('${e.name} _u${_toConstructorSymbol(e, c)}$typeParams(Map<String, dynamic> $m) {');
      p.t(() {
        for (final f in c.fields) {
          final x = gensym();
          p("final $x = $m['${f.name}'];");
          final u = _unmarshal(f.type, x);
          final unmarshal = f.value == undefined
              ? u
              : TernaryExpr(
                  BinaryExpr(x, '!=', nullExpr), u, ConstExpr(f.value));
          p("final ${dumpType(f.type)} ${f.name} = $unmarshal;");
        }
        final ctor = c.name.isNotEmpty ? '.${c.name}' : '';
        final constPrefix = c.isConst && c.fields.isEmpty ? 'const ' : '';
        p('return $constPrefix${e.name}$ctor(');
        p.t(() {
          for (final f in c.fields) {
            p(f.isPositional ? '${f.name},' : '${f.name}: ${f.name},');
          }
        });
        p(');');
      });
      p('}');
    }
  }

  void _emitEnum(IREnum e) {
    p('');
    p('${e.name} _u${e.name}(dynamic v) {');
    p('  if (v is String) {');
    p('    switch(v) {');
    for (final v in e.values) {
      p("      case '$v':");
      p('        return ${e.name}.$v;');
    }
    p('    }');
    p('  }');
    p("  throw 'illegal enum value \$v';");
    p('}');
  }

  String _emit(List<IRElement> elements) {
    // TODO generate imports automatically
    p('// ignore_for_file: deprecated_member_use');
    p('// ignore_for_file: use_full_hex_values_for_flutter_colors');
    p('// ignore_for_file: unnecessary_const');
    p("import 'dart:ui';");
    p("import 'package:flutter/cupertino.dart';");
    p("import 'package:flutter/material.dart';");
    p("import 'package:flutter/gestures.dart';");
    p("import 'package:flutter/services.dart';");
    p("import 'unmarshal.dart';");
    for (final e in elements) {
      if (e is IRClass && !e.isAbstract && !e.isInternal) {
        _emitClass(e);
      } else if (e is IREnum) {
        _emitEnum(e);
      }
    }

    p('');
    p('final unmarshalers = <String, Unmarshal>{');
    for (final e in elements.whereType<IRClass>()) {
      if (!e.isAbstract && !e.isInternal) {
        for (final c in e.constructors) {
          p("  '${e.name}.${c.name}': _u${_toConstructorSymbol(e, c)},");
        }
      }
    }
    p('};');
    return p.lines.join();
  }

  static String emit(List<IRElement> elements) =>
      ClientTranslator()._emit(elements);
}
