import 'dart:io';
import 'package:analyzer/dart/element/type.dart';
import 'package:path/path.dart' as path;
import 'package:analyzer/dart/analysis/analysis_context_collection.dart';
import 'package:analyzer/dart/analysis/results.dart';
import 'package:analyzer/dart/element/element.dart';
import 'package:analyzer/src/dart/element/element.dart'
    show ConstFieldElementImpl;

void compile(String loaderPath, String outputDir) {
  _analyze(path.normalize(File(loaderPath).absolute.path))
      .then((es) => _postProcess(es, outputDir));
}

const libraryWhitelist = {
  'material',
};

const widgetWhitelist = {
  'MaterialApp',
  'ElevatedButton',
};

const libNames = <String>[];

class Printer {
  final String _tab;
  String _indent = '';
  final lines = <String>[];

  Printer(this._tab);

  void call(String line) {
    if (_indent.isNotEmpty && line.isNotEmpty) {
      lines.add(_indent);
    }
    if (line.isNotEmpty) {
      lines.add(line);
    }
    lines.add('\n');
  }

  void t(void Function() f) {
    _indent += _tab;
    f();
    _indent = _indent.isNotEmpty
        ? _indent.substring(0, _indent.length - _tab.length)
        : _indent;
  }
}

class PythonUnit {
  final String path;

  PythonUnit(this.path);
}

class PythonEnum extends PythonUnit {
  final String name;
  final List<PythonEnumEntry> entries;

  PythonEnum(String path, this.name, this.entries) : super(path);
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
  final String name;
  final List<PythonField> fields;
  final List<PythonStaticField> staticFields;
  final List<PythonVariant> variants;
  late List<PythonField> sortedFields;
  final List<String> typeParameters;

  PythonClass(String path, this.name,
      {required this.fields,
      required this.variants,
      required this.staticFields,
      required this.typeParameters})
      : super(path) {
    // Non-default params must precede default params in Python
    sortedFields = sortNonDefaultFields(fields);
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
  final PythonType type;
  final bool isEnumLike;

  PythonStaticField(this.name, this.type, {this.isEnumLike = false});
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

  PythonType(this.name, {this.types});
}

String snakeCase(String name) => name
    .replaceAllMapped(
        RegExp(r'([a-z0-9])([A-Z])'), (m) => '${m[1]}_${m[2]}'.toLowerCase())
    .toLowerCase();

String _titleCase(String name) =>
    name.replaceFirstMapped(RegExp(r'^[a-z]'), (m) => '${m[0]}'.toUpperCase());

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

class PythonTranslator {
  final p = Printer('    ');
  final _classes = <PythonClass>[];
  final _enums = <PythonEnum>[];
  final _processedClasses = <Element>{};
  final _declaredUnits = <String>{
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

  String quote(String name) => _declaredUnits.contains(name) ? name : "'$name'";

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

  String stringifyStaticField(PythonStaticField f) {
    // Python doesn't handle recursive type definitions: static fields of the
    // same type as the containing class need to be assigned after the class
    // definition.
    // TODO Make sure IDE static analysis does not raise false positives.
    // XXX assign static const __ctor
    // e.g. EdgeInsetsGeometry.infinity = EdgeInsetsGeometry()
    //      EdgeInsetsGeometry.infinity.__ctor = (...)
    return f.isEnumLike
        ? '${stringifyType(f.type)}.${f.name} = ${stringifyType(f.type)}(None)'
        : '${f.name}: ${stringifyType(f.type)} = None'; //XXX constant value
  }

  void pushTrace() => _traceDepth += '\t';

  void popTrace() => _traceDepth = _traceDepth.substring(1);

  PythonType toType(DartType t) {
    if (t.isDartCoreBool) return PythonType('bool');
    if (t.isDartCoreInt) return PythonType('int');
    if (t.isDartCoreDouble) return PythonType('float');
    if (t.isDartCoreString) return PythonType('str');
    if (t.isDynamic) return PythonType('Any');

    if (t is FunctionType) {
      return PythonType('Callable'); // TODO
    }

    if (t is InterfaceType) {
      final typeArgs = t.typeArguments;
      if (typeArgs.isEmpty) {
        // recurse: Python requires forward declaration
        pushTrace();
        translateElement(t.element);
        popTrace();
        return PythonType(t.element.name);
      } else {
        final types = typeArgs.map(toType).toList(); // recurse
        final location = t.element.location;
        if (location != null) {
          final components = location.components;
          if (components.contains('dart:core')) {
            if (components.contains('Iterable')) {
              return PythonType('Iterable', types: types);
            } else if (components.contains('List')) {
              return PythonType('List', types: types);
            } else if (components.contains('Map')) {
              return PythonType('Dict', types: types);
            }
          }
        }
        // recurse: Python requires forward declaration
        pushTrace();
        translateElement(t.element);
        popTrace();
        return PythonType(t.element.name, types: types);
      }
    }

    throw 'cannot translate $t';
  }

  PythonType toOptional(PythonType t) => PythonType('Optional', types: [t]);

  PythonField toField(ParameterElement param) {
    trace('\t$param');
    final type = toType(param.type);
    final required = param.isRequiredNamed || param.isRequiredPositional;
    return PythonField(snakeCase(param.name), param.name,
        required ? type : toOptional(type), !required);
  }

  PythonStaticField toStaticField(ClassElement e, ConstFieldElementImpl f) {
    trace('\t$f');
    final type = toType(f.type);
    return PythonStaticField(snakeCase(f.name), type,
        isEnumLike: f.type.element == e);
  }

  List<PythonField> toFields(List<ParameterElement> params) =>
      params.map(toField).toList();

  bool isPrivateSymbol(String name) {
    return name.startsWith(r'_');
  }

  void printParameters(List<PythonField> fields, {isMethod = true}) {
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

  void printInitialization(List<PythonField> fields) {
    if (fields.isEmpty) {
      return p('pass');
    }
    for (final f in fields) {
      p('self.${f.name} = ${f.name}');
    }
  }

  void printClass(PythonClass klass) {
    p('');
    p('');
    p('# ${klass.path}');

    final typeVars = klass.typeParameters.join(', ');
    final base = typeVars.isEmpty ? '' : '(Generic[$typeVars])';
    p('class ${klass.name}$base:');

    final internalStaticFields = klass.staticFields.where((f) => !f.isEnumLike);
    final externalStaticFields = klass.staticFields.where((f) => f.isEnumLike);

    p.t(() {
      // TODO class doc
      // TODO ctor doc
      if (internalStaticFields.isNotEmpty) {
        for (final f in internalStaticFields) {
          p(stringifyStaticField(f));
        }
        if (klass.fields.isNotEmpty) {
          p('');
        }
      }

      if (klass.fields.isNotEmpty) {
        p('def __init__(');
        printParameters(klass.sortedFields);
        p('):');
        p.t(() {
          // printInitialization(klass.sortedFields);
          p("self.__ctor = ('', (");
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
        printParameters(variant.sortedFields, isMethod: false);
        p(') -> ${quote(klass.name)}:');
        p.t(() {
          p('_o = ${klass.name}(');
          for (final f in klass.sortedFields) {}
          p(')');
          p("_o.__ctor = ('${variant.dartName}', (");
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
          klass.variants.isEmpty) {
        p('pass');
      }
    });

    _declaredUnits.add(klass.name);

    if (externalStaticFields.isNotEmpty) {
      p('');
      p('');
      for (final f in externalStaticFields) {
        p(stringifyStaticField(f));
      }
    }
  }

  void printEnum(PythonEnum e) {
    p('');
    p('');
    p('# ${e.path}');
    p('class ${e.name}(Enum):');
    p.t(() {
      for (final v in e.entries) {
        p("${v.name} = '${v.value}'");
      }
    });

    _declaredUnits.add(e.name);
  }

  String getRelativeSourcePath(ClassElement e) {
    final absPath = e.source.fullName;
    final libPath = 'flutter';
    // TODO assumes SDK path doesn't contain ../flutter/../flutter/..
    final pos = absPath.indexOf(libPath);
    return pos < 0 ? "" : absPath.substring(pos + libPath.length + 1);
  }

  void translateElement(ClassElement e) {
    // XXX ctors with _arg not handled (e.g. Locale)
    if (_processedClasses.contains(e)) return;
    _processedClasses.add(e);

    final sourcePath = getRelativeSourcePath(e);
    trace('$e\t$sourcePath');
    if (e.isEnum) {
      _enums.add(PythonEnum(
          sourcePath,
          e.name,
          e.fields
              .map((f) => PythonEnumEntry(snakeCase(f.name), f.name))
              .toList()));
    } else if (e.isMixin) {
      throw 'cannot translate mixins';
    } else {
      // XXX turn abstract classes into Union[] (e.g. SliderComponentShape)
      // XXX find and include implementers; recurse before adding abstract class
      final staticFields = e.fields
          .whereType<ConstFieldElementImpl>()
          .where((f) => !isPrivateSymbol(f.name))
          .map((f) => toStaticField(e, f))
          .toList();
      final defaultConstructor = e.constructors.where((c) => c.name.isEmpty);

      // XXX fix argument ordering
      // XXX add marker for which ctor was used
      final variants = e.constructors
          .where((c) => c.name.isNotEmpty && !isPrivateSymbol(c.name))
          .map((c) => PythonVariant(
              _unreserved(snakeCase(c.name)), c.name, toFields(c.parameters)))
          .toList();

      final fields = toFields(defaultConstructor.isNotEmpty
          ? defaultConstructor.first.parameters
          : []);

      final typeParameters = e.typeParameters.map((t) => t.name).toList();
      _knownTypeParameters.addAll(typeParameters);

      _classes.add(PythonClass(sourcePath, e.name,
          fields: fields,
          variants: variants,
          staticFields: staticFields,
          typeParameters: typeParameters));
    }
  }

  String printAll() {
    p('from enum import Enum');
    p('from typing import Generic, TypeVar, Callable, Any, Optional, Iterable, List, Dict');
    p('');
    for (final t in _knownTypeParameters) {
      p("$t = TypeVar('$t')");
    }

    for (final e in _enums) {
      printEnum(e);
    }

    for (final klass in _classes) {
      printClass(klass);
    }

    return p.lines.join();
  }

  String translate(Set<Element> elements) {
    for (final e in elements) {
      if (e is! ClassElement) continue;
      if (!widgetWhitelist.contains(e.name)) continue;
      translateElement(e);
    }

    return printAll();
  }
}

void _postProcess(Set<Element> elements, String outputDir) {
  final lines = PythonTranslator().translate(elements);
  _mkdirp(outputDir);
  _write(path.join(outputDir, 'types.py'), lines);
}

Future<Set<Element>> _analyze(String sourcePath) async {
  // Important: The analyzer resolves symbols correctly only if the file
  // .dart_tool/package_config.json is found inside the source project.

  // https://groups.google.com/a/dartlang.org/g/analyzer-discuss/c/Z8hIZDYvUxk
  // -----
  // When the analyzer needs to resolve a URI to a file location there are three
  // options:
  // - If the URI is a `dart:` URI, then the library is found in a known
  //   location in the sdk.
  // - If the URI is a `package:` URI, then the analyzer looks in each of the
  //   parent directories containing the library for a file whose relative path
  //   is `.dart_tool/package_config.json`. That file contains a JSON encoding
  //   of a map from the name of the package (`flutter` in this case) to the
  //   path of the `lib` directory for that package
  //   (`<path>/flutter/packages/flutter/lib` in this case).
  //   Everything after the first `/` in the URI is then appended to the path
  //   to form the full path to the file.
  // - If the URI is any other kind of URI, then the normal URI resolution
  //   rules are followed.
  //
  // The most likely problem here is that the analyzer is unable to locate the
  // `package_config.json` file and hence can't convert the URI into a file path.
  //
  // By the way, the process of finding the `package_config.json` file happens
  // at the time you create the `AnalysisContextCollection` so that it doesn't
  // need to be repeated for each library you analyze. That, and the locations
  // of the `analysis_options.yaml` files, is what determines how many analysis
  // contexts get created in the collection.
  // ---

  final analysis = AnalysisContextCollection(includedPaths: [sourcePath]);
  final elements = <Element>{};
  for (final ctx in analysis.contexts) {
    for (final filePath in ctx.contextRoot.analyzedFiles()) {
      final result = await ctx.currentSession.getResolvedLibrary(filePath);
      if (result is ResolvedLibraryResult) {
        final lib = result.element;
        for (final lib in lib.importedLibraries) {
          if (!libraryWhitelist.contains(lib.name)) continue;
          elements.addAll(lib.exportNamespace.definedNames.values);
          elements.addAll(_getDefinedElements(lib.definingCompilationUnit));
          for (final part in lib.parts) {
            elements.addAll(_getDefinedElements(part));
          }
        }
      }
    }
  }
  return elements;
}

void _write(String path, String text) => File(path).writeAsStringSync(text);

String _read(String path) => File(path).readAsStringSync();

void _mkdirp(String path) => Directory(path).createSync(recursive: true);

Iterable<Element> _getDefinedElements(CompilationUnitElement e) {
  return [
    e.accessors,
    e.classes,
    e.enums,
    e.extensions,
    e.functions,
    e.mixins,
    e.topLevelVariables,
    e.typeAliases,
  ].expand((e) => e);
}
