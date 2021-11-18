import 'dart:io';

import 'package:analyzer/dart/element/element.dart';
import 'package:path/path.dart' as path;

import 'ir.dart';
import 'load.dart';
import 'python.dart';

const libraryWhitelist = {
  'material',
};

const widgetWhitelist = {
  'MaterialApp',
  'ElevatedButton',
  // 'Scaffold',
  // 'AppBar',
  // 'Text',
  // 'ListView',
  // 'ListTile',
  // 'EdgeInsets',
};

const libNames = <String>[];

void compile(String loaderPath, String outputDir) {
  load(
          sourcePath: path.normalize(File(loaderPath).absolute.path),
          libraryWhitelist: libraryWhitelist,
          widgetWhitelist: widgetWhitelist)
      .then((es) => _postProcess(es, outputDir));
}

void _postProcess(Set<Element> elements, String outputDir) {
  _mkdirp(outputDir);

  final ir = IRBuilder.load(elements);
  _write(path.join(outputDir, 'types.ir'), IRBuilder.dump(ir));

  final lines = PythonTranslator.emit(ir);
  _write(path.join(outputDir, 'types.py'), lines);
}

void _write(String path, String text) => File(path).writeAsStringSync(text);

String _read(String path) => File(path).readAsStringSync();

void _mkdirp(String path) => Directory(path).createSync(recursive: true);
