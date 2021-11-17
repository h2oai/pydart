String comma(Iterable<String> items) => items.join(', ');

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

class Emitter {
  final _lines = <String>[];

  void call(String s) => _lines.add(s);

  @override
  String toString() => _lines.join();
}
