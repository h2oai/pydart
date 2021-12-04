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
      throw 'unmarshal failed: no loader found for $t';
    }
    throw 'unmarshal failed: no type name found on object';
  }
  throw 'unmarshal failed: not an object';
}

bool uBool(dynamic v) {
  if (v is bool) return v;
  throw 'unmarshal failed: not a bool';
}

int uInt(dynamic v) {
  if (v is int) return v;
  throw 'unmarshal failed: not a int';
}

double uDouble(dynamic v) {
  if (v is double) return v;
  throw 'unmarshal failed: not a double';
}

String uString(dynamic v) {
  if (v is String) return v;
  throw 'unmarshal failed: not a string';
}

T uClass<T>(dynamic v) => unmarshal(v);

T uFunc<T>(dynamic v) {
  throw 'unmarshal function: not implemented';
}

T die<T>(String message) {
  throw message;
}
