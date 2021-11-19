import 'package:compiler/compiler.dart' as compiler;

void main(List<String> arguments) {
  compiler.compile(
    loaderPath: '../client/lib/main.dart',
    clientOutputDir: '../client/lib',
    pythonOutputDir: '../python/h2o_nitro',
  );
}
