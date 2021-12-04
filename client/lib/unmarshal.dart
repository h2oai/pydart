typedef Unmarshal = dynamic Function(Map<String, dynamic> state);

Map<String, Unmarshal> _unmarshalers = {};

void registerUnmarshalers(Map<String, Unmarshal> unmarshalers) =>
    _unmarshalers.addAll(unmarshalers);

String? _typeOf(Map<String, dynamic> state) {
  final t = state['#t'];
  if (t != null && t is List<dynamic> && t.length == 2) {
    final klass = t[0];
    final constructor = t[1];
    if (klass is String && constructor is String) {
      return '$klass.$constructor';
    }
  }
  return null;
}

dynamic unmarshal(dynamic v) {
  if (v is Map<String, dynamic>) {
    final t = _typeOf(v);
    if (t != null) {
      final u = _unmarshalers[t];
      if (u != null) return u(v);
      throw 'no loader found for $t';
    }
    throw 'no type name found on object';
  }
  throw 'not an object';
}

T uClass<T>(dynamic v) => unmarshal(v);

T uFunc<T>(dynamic v) {
  throw 'unmarshal function: not implemented';
}

T die<T>(String message) {
  throw message;
}
