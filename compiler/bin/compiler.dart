import 'package:compiler/compiler.dart' as compiler;

void main(List<String> arguments) {
  compiler.compile('../client/lib/main.dart', '../python/h2o_nitro');
}
