import 'dart:convert';
import 'dart:io';

import 'package:path/path.dart' as path;

import 'ir.dart';
import 'load.dart';
import 'client.dart';
import 'python.dart';

const libNames = <String>[];

void compile({
  required String loaderPath,
  required String clientOutputDir,
  required String pythonOutputDir,
  required Set<String> libraryWhitelist,
  required Set<String> elementWhitelist,
}) {
  load(
          sourcePath: path.normalize(File(loaderPath).absolute.path),
          libraryWhitelist: libraryWhitelist)
      .then((elements) {
    final ir = IRBuilder.load(elements, elementWhitelist);
    _write(path.join(clientOutputDir, 'types.dart'), ClientTranslator.emit(ir));
    _write(path.join(pythonOutputDir, 'types.ir'), IRBuilder.dump(ir));
    _write(path.join(pythonOutputDir, 'types.py'), PythonTranslator.emit(ir));
  });
}

void _write(String path, String text) => File(path).writeAsStringSync(text);

String _read(String path) => File(path).readAsStringSync();

void _mkdirp(String path) => Directory(path).createSync(recursive: true);
