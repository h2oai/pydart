import 'dart:io';

import 'package:analyzer/dart/analysis/analysis_context_collection.dart';
import 'package:analyzer/dart/analysis/results.dart';
import 'package:analyzer/dart/constant/value.dart';
import 'package:analyzer/dart/element/element.dart';
import 'package:analyzer/dart/element/nullability_suffix.dart';
import 'package:analyzer/dart/element/type.dart';
import 'package:analyzer/src/dart/element/element.dart'
    show ConstFieldElementImpl;
import 'package:path/path.dart' as path;
import 'ir.dart';
import 'emit.dart';

class PythonUnit {
  final String path;
  final String name;

  PythonUnit(this.path, this.name);

  static final placeholder = PythonUnit('NA', 'NA');
}

class PythonEnum extends PythonUnit {
  final List<PythonEnumEntry> entries;

  PythonEnum(String path, String name, this.entries) : super(path, name);
}

class PythonEnumEntry {
  final String name;
  final String value;

  PythonEnumEntry(this.name, this.value);
}

List<PythonField> sortNonDefaultFields(List<PythonField> fields) {
  return [
    ...fields.where((f) => !f.isOptional),
    ...fields.where((f) => f.isOptional),
  ];
}

class PythonClass extends PythonUnit {
  final List<PythonClass> supertypes;
  final List<PythonClass> interfaces;
  final List<PythonField> fields;
  final List<PythonStaticField> staticFields;
  final List<PythonVariant> variants;
  late List<PythonField> sortedFields;
  final List<String> typeParameters;

  PythonClass(String path, String name,
      {required this.supertypes,
      required this.interfaces,
      required this.fields,
      required this.variants,
      required this.staticFields,
      required this.typeParameters})
      : super(path, name) {
    // Non-default params must precede default params in Python
    sortedFields = sortNonDefaultFields(fields);
  }

  Iterable<PythonField> get requiredFields {
    return sortedFields.where((f) => !f.isOptional);
  }
}

class PythonVariant {
  final String name;
  final String dartName;
  final List<PythonField> fields;
  late List<PythonField> sortedFields;

  PythonVariant(this.name, this.dartName, this.fields) {
    // Non-default params must precede default params in Python
    sortedFields = sortNonDefaultFields(fields);
  }
}

class PythonStaticField {
  final String name;
  final String dartName;
  final PythonType type;
  final String value;
  final bool isEnumLike;

  PythonStaticField(
      this.name, this.dartName, this.type, this.value, this.isEnumLike);
}

class PythonField {
  final String name;
  final String dartName;
  final PythonType type;
  final bool isOptional;

  PythonField(this.name, this.dartName, this.type, this.isOptional);
}

class PythonType {
  final String name;
  final List<PythonType>? types;
  final PythonUnit? unit;

  PythonType(this.name, {this.types, this.unit});

  static final bool = PythonType('bool');
  static final int = PythonType('int');
  static final float = PythonType('float');
  static final str = PythonType('str');
  static final any = PythonType('Any');
  static final callable = PythonType('Callable');
}

String snakeCase(String name) => name
    .replaceAllMapped(
        RegExp(r'([a-z0-9])([A-Z])'), (m) => '${m[1]}_${m[2]}'.toLowerCase())
    .toLowerCase();

String _titleCase(String name) =>
    name.replaceFirstMapped(RegExp(r'^[a-z]'), (m) => '${m[0]}'.toUpperCase());

// TODO is there a simpler way to determine this?
bool _hasInterface(DartType t, List<String> names) {
  if (t is InterfaceType) {
    final location = t.element.location;
    if (location != null) {
      final components = location.components;
      for (final name in names) {
        if (!components.contains(name)) return false;
      }
      return true;
    }
  }
  return false;
}

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

String _unreserved(String name) =>
    _reservedWords.contains(name) ? '${name}_' : name;

bool _isPrivateSymbol(String name) {
  return name.startsWith(r'_');
}

class PythonTranslator {
  final p = Printer('    ');
  final _units = <PythonUnit>[];
  final _unitCache = <Element, PythonUnit>{};
  final _declaredNames = <String>{
    'bool',
    'int',
    'float',
    'str',
    'Any',
    'Callable',
    'Optional',
    'Iterable',
    'List',
    'Dict',
  };
  final _knownTypeParameters = <String>{};
  String _traceDepth = '';

  String quote(String name) => _declaredNames.contains(name) ? name : "'$name'";

  void trace(Object? o) {
    print('$_traceDepth$o');
  }

  String stringifyField(PythonField f) {
    return '${f.name}: ${stringifyType(f.type)}';
  }

  String stringifyType(PythonType t) {
    final args = (t.types ?? []).map((e) => stringifyType(e)).join(', ');
    return args.isEmpty ? quote(t.name) : '${t.name}[$args]';
  }

  void pushTrace() => _traceDepth += '\t';

  void popTrace() => _traceDepth = _traceDepth.substring(1);

  PythonType _toType(DartType t) {
    if (t.isDartCoreBool) return PythonType.bool;
    if (t.isDartCoreInt) return PythonType.int;
    if (t.isDartCoreDouble) return PythonType.float;
    if (t.isDartCoreString) return PythonType.str;
    if (t.isDynamic) return PythonType.any;

    if (t is FunctionType) {
      return PythonType.callable; // XXX handle delegates
    }

    if (t is InterfaceType) {
      final typeArgs = t.typeArguments;
      if (typeArgs.isEmpty) {
        // recurse: Python requires forward declaration
        pushTrace();
        final unit = _toUnit(t.element);
        popTrace();
        return PythonType(t.element.name, unit: unit);
      } else {
        final types = typeArgs.map(_toType).toList(); // recurse
        if (_hasInterface(t, ['dart:core', 'Iterable'])) {
          return PythonType('Iterable', types: types);
        } else if (_hasInterface(t, ['dart:core', 'List'])) {
          return PythonType('List', types: types);
        } else if (_hasInterface(t, ['dart:core', 'Map'])) {
          return PythonType('Dict', types: types);
        }
        // recurse: Python requires forward declaration
        pushTrace();
        final unit = _toUnit(t.element);
        popTrace();
        return PythonType(t.element.name, types: types, unit: unit);
      }
    }

    if (t is TypeParameterType) {
      // Treat X<T extends Y> as X<Y>
      // .isDynamic is false if the type parameter has bounds.
      final type =
          t.bound.isDynamic ? PythonType(t.element.name) : _toType(t.bound);
      return t.nullabilitySuffix == NullabilitySuffix.question
          ? _toOptional(type)
          : type;
    }

    throw 'cannot translate $t';
  }

  PythonType _toOptional(PythonType t) => PythonType('Optional', types: [t]);

  PythonField _toField(ParameterElement param) {
    trace('\t$param');
    final type = _toType(param.type);
    final required = param.isRequiredNamed || param.isRequiredPositional;
    return PythonField(_unreserved(snakeCase(param.name)), param.name,
        required ? type : _toOptional(type), !required);
  }

  static const unknown = 'UNKNOWN';

  String _toConst(DartObject? o) {
    if (o == null) return unknown;

    final t = o.type;
    if (t == null) return unknown;

    if (t.isDartCoreBool) {
      final v = o.toBoolValue();
      if (v != null) return v ? 'True' : 'False';
    } else if (t.isDartCoreInt) {
      final v = o.toIntValue();
      if (v != null) return '$v';
    } else if (t.isDartCoreDouble) {
      final v = o.toDoubleValue();
      if (v != null) return '$v';
    } else if (t.isDartCoreString) {
      final v = o.toStringValue();
      if (v != null) return "'$v'"; // XXX quote string
    } else if (t.isDartCoreList) {
      final l = o.toListValue();
      if (l != null) {
        final vs = l.map(_toConst).join(', ');
        return '[$vs]';
      }
    }

    return unknown;
  }

  PythonStaticField _toStaticField(ClassElement e, ConstFieldElementImpl f) {
    trace('\t$f');
    final type = _toType(f.type);
    final value = _toConst(f.computeConstantValue());
    final isEnumLike = f.type.element == e;
    // XXX handle !isEnumLike && value == unknown
    return PythonStaticField(
        snakeCase(f.name), f.name, type, value, isEnumLike);
  }

  List<PythonField> _toFields(List<ParameterElement> params) =>
      params.map(_toField).toList();

  PythonEnum _toEnum(ClassElement e) {
    assert(e.isEnum);
    final sourcePath = _getRelativeSourcePath(e);
    trace('$e\t$sourcePath');

    return PythonEnum(
        sourcePath,
        e.name,
        e.fields
            .map((f) => PythonEnumEntry(snakeCase(f.name), f.name))
            .toList());
  }

  PythonClass _toClass(ClassElement e) {
    assert(!e.isEnum);
    final sourcePath = _getRelativeSourcePath(e);
    trace('$e\t$sourcePath');
    // TODO special handling for mixins?
    // XXX turn abstract classes into Union[] (e.g. SliderComponentShape)
    // XXX find and include implementers; recurse before adding abstract class

    final supertype = e.supertype;
    final supertypeUnit = supertype != null ? _toUnit(supertype.element) : null;

    final interfaces = e.interfaces.map((i) => _toUnit(i.element));

    final staticFields = e.fields
        .where((f) => f.isStatic)
        .whereType<ConstFieldElementImpl>()
        .where((f) => !_isPrivateSymbol(f.name))
        // Ignore FontWeight.values, etc.
        .where((f) => !_hasInterface(f.type, ['dart:core', 'List']))
        .map((f) => _toStaticField(e, f))
        .toList();

    final defaultConstructor = e.constructors.where((c) => c.name.isEmpty);

    final variants = e.constructors
        .where((c) => c.name.isNotEmpty && !_isPrivateSymbol(c.name))
        .map((c) => PythonVariant(
            _unreserved(snakeCase(c.name)), c.name, _toFields(c.parameters)))
        .toList();

    final fields = _toFields(defaultConstructor.isNotEmpty
        ? defaultConstructor.first.parameters
        : []);

    final typeParameters = e.typeParameters.map((t) => t.name).toList();
    _knownTypeParameters.addAll(typeParameters);

    return PythonClass(sourcePath, e.name,
        supertypes: supertypeUnit is PythonClass ? [supertypeUnit] : [],
        interfaces: interfaces.whereType<PythonClass>().toList(),
        fields: fields,
        variants: variants,
        staticFields: staticFields,
        typeParameters: typeParameters);
  }

  void emitParameters(List<PythonField> fields, {isMethod = true}) {
    p.t(() {
      p.t(() {
        if (isMethod) {
          p('self,');
        }
        // Non-default params must precede default params
        fields
            .where((f) => !f.isOptional)
            .forEach((f) => p('${stringifyField(f)},'));
        fields
            .where((f) => f.isOptional)
            .forEach((f) => p('${stringifyField(f)} = None,'));
      });
    });
  }

  void emitInitialization(List<PythonField> fields) {
    if (fields.isEmpty) {
      return p('pass');
    }
    for (final f in fields) {
      p('self.${f.name} = ${f.name}');
    }
  }

  String _defaultValueOf(PythonType t) {
    switch (t.name) {
      case 'bool':
        return 'False';
      case 'int':
        return '0';
      case 'float':
        return '0.0';
      case 'str':
        return "''";
      case 'List':
        return '[]';
      case 'Dict':
        return '{}';
      case 'Optional':
        return 'None';
      case 'Callable':
        return 'None'; // XXX pass noop
    }
    final u = t.unit;
    if (u != null) {
      if (u is PythonClass) {
        final args =
            u.requiredFields.map((f) => _defaultValueOf(f.type)).join(', ');
        return '${u.name}($args)';
      } else if (u is PythonEnum) {
        return '${u.name}.${u.entries.first.name}';
      }
    }

    throw 'could not determine default value for ${t.name}';
  }

  String _toStaticFieldInitializerName(String className, String type) {
    final ctorExtn = type
        .replaceAll(RegExp(r'[\]]'), '')
        .replaceAll(RegExp(r'[\[]'), '_of_');
    return snakeCase("_${className}__$ctorExtn");
  }

  void _emitClass(PythonClass klass) {
    final supertypes = <String>[];
    if (klass.typeParameters.isNotEmpty) {
      final typeVars = klass.typeParameters.join(', ');
      supertypes.add('Generic[$typeVars]');
    }
    for (final st in klass.supertypes) {
      // TODO flag abstract/interface supertypes accordingly
      // TODO ensure supertype is already emitted
      // TODO might conflict with Generic[T] type annotation or trip type-checker
      // TODO don't emit Object if already in hierarchy (e.g. class PreferredSizeWidget(Object, Widget))
      supertypes.add(st.name);
    }
    for (final i in klass.interfaces) {
      supertypes.add(i.name);
    }
    final base = supertypes.isEmpty ? '' : "(${supertypes.join(', ')})";

    final internalStaticFields = klass.staticFields.where((f) => !f.isEnumLike);
    final externalStaticFields = klass.staticFields.where((f) => f.isEnumLike);

    final constBuilders = <String, PythonStaticField>{};
    for (final f in internalStaticFields) {
      final unit = f.type.unit;
      if (unit != null && unit is PythonClass) {
        constBuilders[stringifyType(f.type)] = f;
      }
    }

    for (final entry in constBuilders.entries) {
      final type = entry.key;
      final f = entry.value;
      final unit = f.type.unit;
      if (unit != null && unit is PythonClass) {
        p('');
        p('');
        final name = _toStaticFieldInitializerName(klass.name, type);
        p('def $name(_k: str) -> $type:');
        p.t(() {
          p('_o = $type(');
          _emitDefaultCtorArgs(unit);
          p(')');
          p("_o.__ctor = (('${klass.name}', _k),)");
          p('return _o');
        });
      }
    }

    p('');
    p('');
    p('# ${klass.path}');
    p('class ${klass.name}$base:');

    p.t(() {
      // TODO class doc
      // TODO ctor doc
      if (internalStaticFields.isNotEmpty) {
        for (final f in internalStaticFields) {
          final unit = f.type.unit;
          final type = stringifyType(f.type);
          if (unit != null) {
            final name = _toStaticFieldInitializerName(klass.name, type);
            p("${f.name}: $type = $name('${f.dartName}')");
          } else {
            p('${f.name}: $type = ${f.value}');
          }
        }
        if (klass.fields.isNotEmpty) {
          p('');
        }
      }

      if (klass.fields.isNotEmpty) {
        p('def __init__(');
        emitParameters(klass.sortedFields);
        p('):');
        p.t(() {
          // printInitialization(klass.sortedFields);
          p("self.__ctor = (('',), (");
          p.t(() {
            for (final f in klass.fields) {
              p("'${f.dartName}', ${f.name},");
            }
          });
          p('))');
        });
      }

      for (final variant in klass.variants) {
        p('');
        p('@staticmethod');
        p('def ${variant.name}(');
        emitParameters(variant.sortedFields, isMethod: false);
        p(') -> ${quote(klass.name)}:');
        p.t(() {
          p('_o = ${klass.name}(');
          _emitDefaultCtorArgs(klass);
          p(')');
          p("_o.__ctor = (('${variant.dartName}',), (");
          p.t(() {
            for (final f in variant.fields) {
              p("'${f.dartName}', ${f.name},");
            }
          });
          p('))');
          p('return _o');
        });
      }

      if (klass.fields.isEmpty &&
          klass.fields.isEmpty &&
          klass.variants.isEmpty &&
          internalStaticFields.isEmpty) {
        p('pass');
      }
    });

    _declaredNames.add(klass.name);

    // Python doesn't handle recursive type definitions: static fields of the
    // same type as the containing class need to be assigned after the class
    // definition.
    if (externalStaticFields.isNotEmpty) {
      p('');
      p('');
      for (final f in externalStaticFields) {
        if (f.isEnumLike) {
          p('${stringifyType(f.type)}.${f.name} = ${stringifyType(f.type)}(');
          _emitDefaultCtorArgs(klass);
          p(')');
          p("${stringifyType(f.type)}.${f.name}.__ctor = ('${f.name}', )");
        }
      }
    }
  }

  void _emitDefaultCtorArgs(PythonClass klass) {
    p.t(() {
      for (final f in klass.requiredFields) {
        // XXX use analyzer to eval original values?
        p('${f.name}=${_defaultValueOf(f.type)},');
      }
    });
  }

  void _emitEnum(PythonEnum e) {
    p('');
    p('');
    p('# ${e.path}');
    p('class ${e.name}(Enum):');
    p.t(() {
      for (final v in e.entries) {
        p("${v.name} = '${v.value}'");
      }
    });

    _declaredNames.add(e.name);
  }

  PythonUnit _toUnit(ClassElement e) {
    // XXX ctors with _arg not handled (e.g. Locale)
    if (_unitCache.containsKey(e)) {
      final unit = _unitCache[e];
      if (unit != null) return unit;
      throw 'type not found in cache'; // XXX ugly
    }
    _unitCache[e] = PythonUnit.placeholder;

    final unit = e.isEnum ? _toEnum(e) : _toClass(e);
    _units.add(unit);
    _unitCache[e] = unit;
    return unit;
  }

  String _emitAll() {
    p('from enum import Enum');
    p('from typing import Generic, TypeVar, Callable, Any, Optional, Iterable, List, Dict');
    p('');
    for (final t in _knownTypeParameters) {
      p("$t = TypeVar('$t')");
    }

    for (final unit in _units) {
      if (unit is PythonClass) {
        _emitClass(unit);
      } else if (unit is PythonEnum) {
        _emitEnum(unit);
      }
    }

    return p.lines.join();
  }

  String translate(Set<Element> elements) {
    for (final e in elements) {
      if (e is! ClassElement) continue;
      if (!widgetWhitelist.contains(e.name)) continue;
      _toUnit(e);
    }

    return _emitAll();
  }
}

String _getRelativeSourcePath(ClassElement e) {
  final absPath = e.source.fullName;
  final libPath = 'flutter';
  // TODO assumes SDK path doesn't contain ../flutter/../flutter/..
  final pos = absPath.indexOf(libPath);
  return pos < 0 ? "" : absPath.substring(pos + libPath.length + 1);
}