import 'package:compiler/compiler.dart' as compiler;

void main(List<String> arguments) {
  compiler.compile('../loader/lib/main.dart', '../python/package/h2o_nitro');
}
