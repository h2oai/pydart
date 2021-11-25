typedef Unmarshal = dynamic Function(Map<String, dynamic> state);

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

dynamic unmarshal(Map<String, Unmarshal> loaders, dynamic state) {
  if (state == null) throw 'cannot unmarshal null';
  if (state is Map<String, dynamic>) {
    final t = _typeOf(state);
    if (t != null) {
      final unmarshal = loaders[t];
      if (unmarshal != null) return unmarshal(state);
      throw 'unmarshal failed: no loader found for $t';
    }
  }
  return state;
}

bool uBool(dynamic v) {
  if (v is bool) return v;
  throw 'unmarshal failed: not a bool';
}

bool? unBool(dynamic v) => v == null ? v : uBool(v);

int uInt(dynamic v) {
  if (v is int) return v;
  throw 'unmarshal failed: not a int';
}

int? unInt(dynamic v) => v == null ? v : uInt(v);

double uDouble(dynamic v) {
  if (v is double) return v;
  throw 'unmarshal failed: not a double';
}

double? unDouble(dynamic v) => v == null ? v : uDouble(v);

String uString(dynamic v) {
  if (v is String) return v;
  throw 'unmarshal failed: not a string';
}

String? unString(dynamic v) => v == null ? v : uString(v);
