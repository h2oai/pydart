import 'package:compiler/compiler.dart' as compiler;

void main(List<String> arguments) {
  // TODO load from config file
  compiler.compile(
    loaderPath: '../client/lib/main.dart',
    clientOutputDir: '../client/lib',
    pythonOutputDir: '../python',
    libraryWhitelist: {
      'material',
    },
    elementWhitelist: {
      'MaterialApp',
      'ElevatedButton',
      // 'Scaffold',
      // 'AppBar',
      // 'Text',
      // 'ListView',
      // 'ListTile',
      // 'EdgeInsets',
    },
  );
}
