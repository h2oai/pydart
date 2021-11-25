import 'package:analyzer/dart/element/element.dart';
import 'package:analyzer/dart/element/type.dart';

import 'emit.dart';
import 'ir.dart';

bool _isOptional(IRType t) =>
    t is IRParameterizedType && t.element == IRElement.optional;

String capitalize(String s) {
  if (s.isEmpty) return s;
  return s.substring(0, 1).toUpperCase() + s.substring(1);
}

String _unmarshalerNameOf(String className, String ctorName) =>
    '_u$className' + capitalize(ctorName);

String _unmarshalerOf(IRType t) {
  if (t.isPrimitive) return 'u' + capitalize(t.name);

  // uNull(uList(uBool))(v)

  if (t is IRParameterizedType) {
    final e = t.element;
    if (e == IRElement.optional) {
      final p = t.parameters.first;
      return 'uNull<${dumpType(p)}>(${_unmarshalerOf(p)})';
    }
    if (e.name == 'List') {
      final p = t.parameters.first;
      return 'uList<${dumpType(p)}>(${_unmarshalerOf(p)})';
    }

    // FIXME Handle Map<K, V>

    if (e is IREnum) return "_u${e.name}";

    // TODO constructor-tearoffs
    // Ideally this would be passed as uClass<T>, but causes the compiler to
    //  complain with "This requires the 'constructor-tearoffs' language
    //  feature to be enabled."
    // https://github.com/dart-lang/language/blob/master/accepted/future-releases/constructor-tearoffs/feature-specification.md
    if (e is IRClass) return 'uClass';
  }
  return '';
}

class ClientTranslator {
  final p = Printer('  ');

  void _emitClass(IRClass e) {
    final m = '__m';
    for (final c in e.constructors) {
      p('');
      p('${e.name} ${_unmarshalerNameOf(e.name, c.name)}(Map<String, dynamic> $m) {');
      p.t(() {
        for (final f in c.fields) {
          final lookup = "$m['${f.name}']";
          final unmarshal = _unmarshalerOf(f.type);
          p("final ${dumpType(f.type)} ${f.name} = $unmarshal($lookup);");
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
    p('');
    p('${e.name}? _un${e.name}(dynamic v) => v == null ? v : _u${e.name}(v);');
  }

  String _emit(List<IRElement> elements) {
    // TODO generate imports automatically
    p("import 'dart:ui';");
    p("import 'package:flutter/cupertino.dart';");
    p("import 'package:flutter/material.dart';");
    p("import 'package:flutter/gestures.dart';");
    p("import 'package:flutter/services.dart';");
    p("import 'load.dart';");
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
    p('registerLoaders(<String, Unmarshal>{');
    for (final e in elements.whereType<IRClass>()) {
      if (!e.isAbstract) {
        for (final c in e.constructors) {
          p("  '${e.name}.${c.name}': ${_unmarshalerNameOf(e.name, c.name)},");
        }
      }
    }
    p('});');
    return p.lines.join();
  }

  static String emit(List<IRElement> elements) =>
      ClientTranslator()._emit(elements);
}
