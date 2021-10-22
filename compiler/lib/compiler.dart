import 'dart:io';
import 'package:analyzer/dart/element/type.dart';
import 'package:path/path.dart' as path;
import 'package:analyzer/dart/analysis/analysis_context_collection.dart';
import 'package:analyzer/dart/analysis/results.dart';
import 'package:analyzer/dart/element/element.dart';

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
  final List<String> values;

  PythonEnum(String path, this.name, this.values) : super(path);
}

class PythonClass extends PythonUnit {
  final String name;
  final List<PythonField> fields;
  late List<PythonField> sortedFields;
  final List<PythonVariant>? variants;

  PythonClass(String path, this.name, this.fields, {this.variants})
      : super(path) {
    // Non-default params must precede default params in Python
    sortedFields = [
      ...fields.where((f) => !f.type.isOptional),
      ...fields.where((f) => f.type.isOptional),
    ];
  }
}

class PythonVariant {
  final String name;
  final PythonClass klass;

  PythonVariant(this.name, this.klass);
}

class PythonField {
  final String name;
  final PythonType type;

  PythonField(this.name, this.type);

  String get code => '$name: ${type.code}';
}

class PythonType {
  final String name;
  final List<PythonType>? types;
  final bool isOptional;

  PythonType(this.name, {this.types, this.isOptional = false});

  String get code {
    final args = (types ?? []).map((e) => e.code).join(', ');
    return args.isEmpty ? name : '$name[$args]';
  }
}

String snakeCase(String name) => name.replaceAllMapped(
    RegExp(r'([a-z0-9])([A-Z])'), (m) => '${m[1]}_${m[2]}'.toLowerCase());

String titleCase(String name) =>
    name.replaceFirstMapped(RegExp(r'^[a-z]'), (m) => '${m[0]}'.toUpperCase());

class PythonTranslator {
  final p = Printer('    ');
  final classes = <PythonClass>[];
  final enums = <PythonEnum>[];
  final processedClasses = <Element>{};
  String traceDepth = '';

  void trace(Object? o) {
    print('$traceDepth$o');
  }

  PythonType toType(DartType t) {
    if (t.isDartCoreBool) return PythonType('bool');
    if (t.isDartCoreInt) return PythonType('int');
    if (t.isDartCoreDouble) return PythonType('float');
    if (t.isDartCoreString) return PythonType('str');
    if (t.isDynamic) return PythonType('any');

    if (t is FunctionType) {
      return PythonType('Callable'); // TODO
    }

    if (t is InterfaceType) {
      final typeArgs = t.typeArguments;
      if (typeArgs.isEmpty) {
        traceDepth+='\t';
        processElement(t.element); // recurse: Python requires forward declaration
        traceDepth=traceDepth.substring(1);
        return PythonType(t.element.name);
      } else {
        final types = typeArgs.map(toType).toList(); // recurse
        String typeName = t.element.name;
        final location = t.element.location;
        if (location != null) {
          final components = location.components;
          if (components.contains('dart:core')) {
            if (components.contains('Iterable')) {
              typeName = 'Iterable';
            } else if (components.contains('List')) {
              typeName = 'List';
            } else if (components.contains('Map')) {
              typeName = 'Dict';
            }
          }
        }
        return PythonType(typeName, types: types);
      }
    }

    throw 'cannot translate $t';
  }

  PythonType toOptional(PythonType t) {
    return PythonType('Optional', types: [t], isOptional: true);
  }

  PythonField toField(ParameterElement param) {
    trace('\t$param');
    final type = toType(param.type);
    final required = param.isRequiredNamed || param.isRequiredPositional;
    return PythonField(
        snakeCase(param.name), required ? type : toOptional(type));
  }

  List<PythonField> toFields(List<ParameterElement> params) =>
      params.map(toField).toList();

  void printParameters(List<PythonField> fields, {isMethod = true}) {
    p.t(() {
      p.t(() {
        if (isMethod) {
          p('self,');
        }
        // Non-default params must precede default params
        fields.where((f) => !f.type.isOptional).forEach((f) => p('${f.code},'));
        fields
            .where((f) => f.type.isOptional)
            .forEach((f) => p('${f.code} = None,'));
      });
    });
  }

  void printInitialization(List<PythonField> fields) {
    if (fields.isEmpty) {
      p('pass');
    }
    for (final f in fields) {
      p('self.${f.name} = ${f.name}');
    }
  }

  void printClass(PythonClass klass) {
    p('');
    p('');
    p('# ${klass.path}');
    p('class ${klass.name}:');
    p.t(() {
      // TODO class doc
      // TODO ctor doc
      p('def __init__(');
      printParameters(klass.sortedFields);
      p('):');
      p.t(() {
        printInitialization(klass.sortedFields);
      });
    });
    for (final variant in klass.variants ?? []) {
      p.t(() {
        p('');
        p('@staticmethod');
        p('def with_${variant.name}(');
        printParameters(variant.klass.sortedFields, isMethod: false);
        p(') -> ${variant.klass.name}:');
        p.t(() {
          p('return ${variant.klass.name}(');
          p.t(() {
            for (final f in variant.klass.sortedFields) {
              p('${f.name},');
            }
          });
          p(')');
        });
      });
    }
  }

  void printEnum(PythonEnum e) {
    p('');
    p('');
    p('# ${e.path}');
    p('class ${e.name}(Enum):');
    p.t(() {
      for (final v in e.values) {
        p('${snakeCase(v).toUpperCase()} = \'$v\'');
      }
    });
  }

  String getRelativeSourcePath(ClassElement e) {
    final absPath = e.source.fullName;
    final libPath = 'flutter';
    // FIXME assumes SDK path doesn't contain ../flutter/../flutter/..
    final pos = absPath.indexOf(libPath);
    return pos < 0 ? "" : absPath.substring(pos + libPath.length + 1);
  }

  void processElement(ClassElement e) {
    if (processedClasses.contains(e)) return;
    processedClasses.add(e);

    final sourcePath = getRelativeSourcePath(e);
    trace('$e@$sourcePath');
    if (e.isEnum) {
      enums.add(
          PythonEnum(sourcePath, e.name, e.fields.map((f) => f.name).toList()));
    } else if (e.isMixin) {
      throw 'cannot translate mixins';
    } else {
      final ctors = e.constructors;
      final ctor0 = ctors.where((c) => c.name.isEmpty);
      if (ctor0.isNotEmpty) {
      final variants = ctors.where((c) => c.name.isNotEmpty).map((c) {
        final name = '${e.name}With${titleCase(c.name)}';
        final variantClass =
            PythonClass(sourcePath, name, toFields(c.parameters));
        return PythonVariant(c.name, variantClass);
      }).toList();
      classes.addAll(variants.map((v) => v.klass).toList());
      classes.add(PythonClass(sourcePath, e.name, toFields(ctor0.first.parameters),
          variants: variants));
      } else {
        // TODO handle enum-like classes (e.g. FontWeight)
      }
    }
  }

  String translate(Set<Element> elements) {
    p('from enum import Enum');
    p('from typing import Callable, Optional, Iterable, List, Dict');
    for (final e in elements) {
      if (e is! ClassElement) continue;
      if (!widgetWhitelist.contains(e.name)) continue;
      processElement(e);
    }

    for (final e in enums) {
      printEnum(e);
    }

    for (final klass in classes) {
      printClass(klass);
    }

    return p.lines.join();
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
