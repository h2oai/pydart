import 'package:analyzer/dart/element/element.dart';

import 'emit.dart';
import 'ir.dart';

bool _isOptional(IRType t) =>
    t is IRParameterizedType && t.element == IRElement.optional;

class ClientTranslator {
  final p = Printer('  ');

  void _emitClass(IRClass e) {
    final m = '__m';
    for (final c in e.constructors) {
      p('');
      p('${e.name} _u${c.name}${e.name}(Map<String, dynamic> $m) {');
      p.t(() {
        for (final f in c.fields) {
          final t = f.type;
          p("final ${dumpType(f.type)} ${f.name} = $m['${f.name}'];");
        }
        final ctor = c.name.isNotEmpty ? '.${c.name}' : '';
        p('return ${e.name}$ctor(');
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
    p("import 'dart:ui';");
    p("import 'package:flutter/cupertino.dart';");
    p("import 'package:flutter/material.dart';");
    p("import 'package:flutter/gestures.dart';");
    p("import 'package:flutter/services.dart';");
    for (final e in elements) {
      if (e is IRClass && !e.isAbstract) {
        _emitClass(e);
      } else if (e is IREnum) {
        _emitEnum(e);
      }
    }

    p('');
    p('typedef Unmarshal = dynamic Function(Map<String, dynamic> state);');
    p('');
    p('final loaders = <String, Unmarshal>{');
    for (final e in elements.whereType<IRClass>()) {
      if (!e.isAbstract) {
        for (final c in e.constructors) {
          p("  '${e.name}.${c.name}': _u${c.name}${e.name},");
        }
      }
    }
    p('};');
    return p.lines.join();
  }

  static String emit(List<IRElement> elements) =>
      ClientTranslator()._emit(elements);
}
