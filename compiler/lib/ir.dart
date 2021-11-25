import 'package:analyzer/dart/constant/value.dart';
import 'package:analyzer/dart/element/element.dart';
import 'package:analyzer/dart/element/nullability_suffix.dart';
import 'package:analyzer/dart/element/type.dart';
import 'package:analyzer/src/dart/element/element.dart'
    show ConstFieldElementImpl;
import 'package:quiver/core.dart';

import 'emit.dart';

abstract class IRConst {}

class IRUndefined extends IRConst {
  @override
  String toString() => 'undefined';
}

final undefined = IRUndefined();

class IRBool extends IRConst {
  final bool value;

  IRBool(this.value);

  @override
  String toString() => '$value';
}

class IRInt extends IRConst {
  final int value;

  IRInt(this.value);

  @override
  String toString() => '$value';
}

class IRDouble extends IRConst {
  final double value;

  IRDouble(this.value);

  @override
  String toString() => '$value';
}

class IRString extends IRConst {
  final String value;

  IRString(this.value);

  @override
  String toString() => "'$value'";
}

class IRType {
  final String name;

  IRType(this.name);

  static final unknown = IRType('unknown');
  static final nothing = IRType('void');
  static final bool = IRType('bool');
  static final int = IRType('int');
  static final double = IRType('double');
  static final string = IRType('String');
  static final any = IRType('dynamic');

  get isPrimitive =>
      this == IRType.bool ||
      this == IRType.int ||
      this == IRType.double ||
      this == IRType.string;
}

class IRTypeParameter extends IRType {
  final IRType? bound;

  IRTypeParameter(String name, this.bound) : super(name);
}

class IRParameterizedType extends IRType {
  final IRElement element;
  final List<IRType> parameters;

  IRParameterizedType(
    this.element,
    this.parameters,
  ) : super(element.name);
}

class IRElement {
  final String path;
  final String name;

  IRElement(this.path, this.name);

  static final optional = IRElement('', 'opt');
  static final func = IRElement('', 'Function');

  @override
  bool operator ==(Object other) =>
      other is IRElement && path == other.path && name == other.name;

  @override
  int get hashCode => hash2(path, name);
}

class IRPlaceholder extends IRElement {
  final ClassElement dartElement;

  IRPlaceholder(this.dartElement) : super('', '__PLACEHOLDER__');
}

class IREnum extends IRElement {
  final List<String> values;
  final ClassElement dartElement;

  IREnum(String path, String name,
      {required this.values, required this.dartElement})
      : super(path, name);
}

class IRField {
  final String name;
  final IRType type;
  final IRConst value;
  final bool isPositional;
  final bool isRequired;
  final bool isOptional;

  IRField({
    required this.name,
    required this.type,
    required this.value,
    required this.isPositional,
    required this.isRequired,
    required this.isOptional,
  });
}

class IRConstructor {
  final String name;
  final List<IRField> fields;

  IRConstructor(this.name, this.fields);
}

class IRClass extends IRElement {
  final bool isAbstract;
  final List<IRTypeParameter> parameters;
  final List<IRType> supertypes;
  final List<IRType> interfaces;
  final List<IRConstructor> constructors;
  final List<IRField> fields;
  final ClassElement dartElement;

  IRClass(
    String path,
    String name, {
    required this.isAbstract,
    required this.parameters,
    required this.supertypes,
    required this.interfaces,
    required this.constructors,
    required this.fields,
    required this.dartElement,
  }) : super(path, name);
}

bool _isPrivateSymbol(String name) {
  return name.startsWith(r'_');
}

String _getRelativeSourcePath(ClassElement e) {
  final absPath = e.source.fullName;
  final libPath = 'flutter';
  // TODO assumes SDK path doesn't contain ../flutter/../flutter/..
  final pos = absPath.indexOf(libPath);
  return pos < 0 ? "" : absPath.substring(pos + libPath.length + 1);
}

// TODO is there a simpler way to determine this?
bool _hasInterface(DartType t, List<String> names) {
  if (t is InterfaceType) {
    final location = t.element.location;
    if (location != null) {
      final components = location.components;
      for (final name in names) {
        if (!components.contains(name)) return false;
      }
      return true;
    }
  }
  return false;
}

String dumpType(IRType t) {
  if (t is IRParameterizedType) {
    if (t.parameters.isNotEmpty) {
      final types = t.parameters.map(dumpType).toList();
      if (t.element == IRElement.func) {
        final params = types.sublist(0, types.length - 1).join(', ');
        final returnType = types.last;
        return '$returnType Function($params)';
      }
      final params = types.join(', ');
      if (t.element == IRElement.optional) {
        return '$params?';
      }
      return '${t.name}<$params>';
    }
  } else if (t is IRTypeParameter) {
    final b = t.bound;
    return t.name + (b != null ? ' extends ${dumpType(b)}' : '');
  }
  return t.name;
}

class IRBuilder {
  final _elements = <IRElement>[];
  final _cache = <Element, IRElement>{};

  IREnum _toEnum(ClassElement e) {
    assert(e.isEnum);
    final path = _getRelativeSourcePath(e);
    final values =
        e.fields.where((f) => f.isEnumConstant).map((f) => f.name).toList();
    return IREnum(path, e.name, values: values, dartElement: e);
  }

  IRTypeParameter _toParameterType(TypeParameterElement p) {
    final bound = p.bound;
    return IRTypeParameter(p.name, bound != null ? _toType(bound) : null);
  }

  IRType _toType(DartType t) {
    if (t.isVoid) return IRType.nothing;
    if (t.isDartCoreBool) return IRType.bool;
    if (t.isDartCoreInt) return IRType.int;
    if (t.isDartCoreDouble) return IRType.double;
    if (t.isDartCoreString) return IRType.string;
    if (t.isDynamic) return IRType.any;

    if (t is InterfaceType) {
      final pt = IRParameterizedType(
          _toElement(t.element), t.typeArguments.map(_toType).toList());
      return t.nullabilitySuffix == NullabilitySuffix.question
          ? _toOptional(pt)
          : pt;
    }

    if (t is FunctionType) {
      final parameterTypes = t.parameters.map((p) {
        return _toType(p.type);
      }).toList();
      final returnType = _toType(t.returnType);
      return IRParameterizedType(
          IRElement.func, [...parameterTypes, returnType]);
    }

    if (t is TypeParameterType) {
      return _toParameterType(t.element);
    }

    return IRType.unknown;
  }

  IRField _toStaticField(ClassElement e, ConstFieldElementImpl f) {
    return IRField(
      name: f.name,
      type: _toType(f.type),
      value: _toConst(f.computeConstantValue()),
      isPositional: false,
      isRequired: true,
      isOptional: false,
    );
  }

  IRConst _toConst(DartObject? o) {
    if (o == null) return undefined;

    final t = o.type;
    if (t == null) return undefined;

    if (t.isDartCoreBool) {
      final v = o.toBoolValue();
      if (v != null) return IRBool(v);
    } else if (t.isDartCoreInt) {
      final v = o.toIntValue();
      if (v != null) return IRInt(v);
    } else if (t.isDartCoreDouble) {
      final v = o.toDoubleValue();
      if (v != null) return IRDouble(v);
    } else if (t.isDartCoreString) {
      final v = o.toStringValue();
      if (v != null) return IRString(v);
    }

    return undefined;
  }

  IRType _toOptional(IRType t) {
    return IRParameterizedType(IRElement.optional, [t]);
  }

  IRField _toField(ParameterElement e) {
    return IRField(
      name: e.name,
      type: _toType(e.type),
      value: undefined,
      isPositional: e.isPositional,
      isRequired: e.isNotOptional,
      isOptional: e.isOptional,
    );
  }

  List<IRField> _toFields(List<ParameterElement> params) =>
      params.map(_toField).toList();

  IRClass _toClass(ClassElement e) {
    assert(!e.isEnum);
    final path = _getRelativeSourcePath(e);

    final supertype = e.supertype;
    final supertypes = supertype != null ? [_toType(supertype)] : <IRType>[];
    final interfaces = e.interfaces.map(_toType).toList();

    final fields = e.fields
        .where((f) => f.isStatic)
        .whereType<ConstFieldElementImpl>()
        .where((f) => !_isPrivateSymbol(f.name))
        // Ignore FontWeight.values, etc.
        .where((f) => !_hasInterface(f.type, ['dart:core', 'List']))
        .map((f) => _toStaticField(e, f))
        .toList();

    final constructors = e.constructors
        .where((c) => !_isPrivateSymbol(c.name))
        .map((c) => IRConstructor(c.name, _toFields(c.parameters)))
        .toList();

    final parameters = e.typeParameters.map(_toParameterType).toList();

    return IRClass(
      path, e.name,
      // TODO handle e.isMixin
      isAbstract: e.isAbstract,
      parameters: parameters,
      supertypes: supertypes,
      interfaces: interfaces,
      constructors: constructors,
      fields: fields,
      dartElement: e,
    );
  }

  IRElement _toElement(ClassElement e) {
    final ir0 = _cache[e];
    if (ir0 != null) return ir0;

    // prevent stack overflow caused by recursive type references.
    _cache[e] = IRPlaceholder(e);

    final ir = e.isEnum ? _toEnum(e) : _toClass(e);
    _cache[e] = ir;
    _elements.add(ir);
    return ir;
  }

  IRType _resolveType(IRType t) => (t is IRTypeParameter)
      ? _resolveTypeParameter(t)
      : (t is IRParameterizedType)
          ? IRParameterizedType(_resolveElement(t.element),
              t.parameters.map(_resolveType).toList())
          : t;

  IRTypeParameter _resolveTypeParameter(IRTypeParameter p) {
    final b = p.bound;
    return b != null ? IRTypeParameter(p.name, _resolveType(b)) : p;
  }

  IRField _resolveField(IRField f) => IRField(
        name: f.name,
        type: _resolveType(f.type),
        value: f.value,
        isPositional: f.isPositional,
        isRequired: f.isRequired,
        isOptional: f.isOptional,
      );

  IRConstructor _resolveConstructor(IRConstructor c) =>
      IRConstructor(c.name, c.fields.map(_resolveField).toList());

  IRElement _resolveElement(IRElement e) {
    if (e is IRPlaceholder) {
      final ir = _cache[e.dartElement];
      if (ir != null) return ir;
      throw 'could not resolve ${e.dartElement.name}';
    }
    if (e is IRClass) {
      final c = IRClass(
        e.path,
        e.name,
        isAbstract: e.isAbstract,
        parameters: e.parameters.map(_resolveTypeParameter).toList(),
        supertypes: e.supertypes.map(_resolveType).toList(),
        interfaces: e.interfaces.map(_resolveType).toList(),
        constructors: e.constructors.map(_resolveConstructor).toList(),
        fields: e.fields.map(_resolveField).toList(),
        dartElement: e.dartElement,
      );
      _cache[c.dartElement] = c;
      return c;
    }
    return e;
  }

  List<IRElement> _load(Set<Element> elements, Set<String> widgetWhitelist) {
    for (final e in elements) {
      if (e is ClassElement && widgetWhitelist.contains(e.name)) {
        _toElement(e);
      }
    }

    for (var i = 0; i < _elements.length; i++) {
      _elements[i] = _resolveElement(_elements[i]);
    }

    return _elements;
  }

  static List<IRElement> load(
          Set<Element> elements, Set<String> widgetWhitelist) =>
      IRBuilder()._load(elements, widgetWhitelist);

  static String dump(List<IRElement> elements) {
    final p = Printer('\t');
    for (final e in elements) {
      p('# ${e.path}');
      if (e is IREnum) {
        p('enum ${e.name}:');
        p.t(() {
          for (final v in e.values) {
            p(v);
          }
        });
      } else if (e is IRClass) {
        final abs = e.isAbstract ? 'abstract ' : '';
        final params = e.parameters.isNotEmpty
            ? '<${comma(e.parameters.map(dumpType))}>'
            : '';
        final ext = e.supertypes.isNotEmpty
            ? ' extends ' + comma(e.supertypes.map(dumpType))
            : '';
        final impl = e.interfaces.isNotEmpty
            ? ' implements ' + comma(e.interfaces.map(dumpType))
            : '';
        p('${abs}class ${e.name}$params$ext$impl:');
        p.t(() {
          if (e.fields.isNotEmpty) {
            p('static:');
            p.t(() {
              for (final f in e.fields) {
                final v = f.value is! IRUndefined ? ' = ${f.value}' : '';
                p('${f.name}: ${dumpType(f.type)}$v');
              }
            });
          }
          for (final c in e.constructors) {
            p(c.name.isNotEmpty ? '${c.name}:' : 'default:');
            p.t(() {
              for (final f in c.fields) {
                p('${f.name}: ${dumpType(f.type)}');
              }
            });
          }
        });
      }
      p('');
    }
    return p.lines.join();
  }
}
