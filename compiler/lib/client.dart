import 'package:analyzer/dart/element/element.dart';

import 'emit.dart';
import 'ir.dart';

class ClientTranslator {
  final p = Printer('  ');

  void _emitClass(IRClass e) {
    for (final c in [e.constructor, ...e.constructors]) {
      p('');
      p('${e.name} _u${c.name}${e.name}(Map<String, dynamic> __m) {');
      p("  throw 'not implemented';");
      p('}');
    }
  }

  void _emitEnum(IREnum e) {
    p('');
    p('${e.name} _u${e.name}(String v) {');
    p('  switch(v) {');
    for (final v in e.values) {
      p("    case '$v':");
      p('      return ${e.name}.$v;');
    }
    p('  }');
    p("  throw 'illegal enum value \$v';");
    p('}');
  }

  String _emit(List<IRElement> elements) {
    // TODO generate imports automatically
    p("import 'package:flutter/material.dart';");
    p("import 'package:flutter/gestures.dart';");
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
        for (final c in [e.constructor, ...e.constructors]) {
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
