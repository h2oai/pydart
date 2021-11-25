typedef Unmarshal = dynamic Function(Map<String, dynamic> state);

Map<String, Unmarshal> _loaders = {};

void registerLoaders(Map<String, Unmarshal> loaders) =>
    _loaders.addAll(loaders);

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
      final u = _loaders[t];
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

T? Function(dynamic) uNull<T>(T Function(dynamic) u) =>
    (dynamic v) => v == null ? v : u(v);

List<T> Function(dynamic) uList<T>(T Function(dynamic) u) {
  return (dynamic v) {
    if (v is List<dynamic>) return v.map(u).toList(growable: false);
    throw 'unmarshal failed: not a list';
  };
}
