import 'dart:io';

import 'package:analyzer/dart/analysis/analysis_context_collection.dart';
import 'package:analyzer/dart/analysis/results.dart';
import 'package:analyzer/dart/constant/value.dart';
import 'package:analyzer/dart/element/element.dart';
import 'package:analyzer/dart/element/nullability_suffix.dart';
import 'package:analyzer/dart/element/type.dart';
import 'package:analyzer/src/dart/element/element.dart'
    show ConstFieldElementImpl;
import 'package:path/path.dart' as path;
import 'emit.dart';

const widgetWhitelist = {
  'MaterialApp',
  'ElevatedButton',
  // 'Scaffold',
  // 'AppBar',
  // 'Text',
  // 'ListView',
  // 'ListTile',
  // 'EdgeInsets',
};

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
  static final float = IRType('float');
  static final str = IRType('str');
  static final any = IRType('any');
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
  static final func = IRElement('', 'func');
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

  IRField({
    required this.name,
    required this.type,
    required this.value,
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
  final IRConstructor constructor;
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
    required this.constructor,
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
    if (t.isDartCoreDouble) return IRType.float;
    if (t.isDartCoreString) return IRType.str;
    if (t.isDynamic) return IRType.any;

    if (t is InterfaceType) {
      return IRParameterizedType(
          _toElement(t.element), t.typeArguments.map(_toType).toList());
    }

    if (t is FunctionType) {
      // XXX handle t.typeArguments
      final parameterTypes = t.parameters.map((p) {
        final t = _toType(p.type);
        return p.isOptional ? _toOptional(t) : t;
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
    final required = e.isRequiredNamed || e.isRequiredPositional;
    final t = _toType(e.type);
    return IRField(
      name: e.name,
      type: required ? t : _toOptional(t),
      value: undefined,
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

    final defaultConstructors = e.constructors.where((c) => c.name.isEmpty);
    final defaultFields = _toFields(defaultConstructors.isEmpty
        ? []
        : defaultConstructors.first.parameters);

    final constructors = e.constructors
        .where((c) => c.name.isNotEmpty && !_isPrivateSymbol(c.name))
        .map((c) => IRConstructor(c.name, _toFields(c.parameters)))
        .toList();

    final parameters = e.typeParameters.map(_toParameterType).toList();

    return IRClass(
      path, e.name,
      // XXX handle e.isMixin
      isAbstract: e.isAbstract,
      parameters: parameters,
      supertypes: supertypes,
      interfaces: interfaces,
      constructor: IRConstructor('', defaultFields),
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
      ? _resolveParameterType(t)
      : (t is IRParameterizedType)
          ? IRParameterizedType(_resolveElement(t.element),
              t.parameters.map(_resolveType).toList())
          : t;

  IRTypeParameter _resolveParameterType(IRTypeParameter p) {
    final b = p.bound;
    return b != null ? IRTypeParameter(p.name, _resolveType(b)) : p;
  }

  IRField _resolveField(IRField f) =>
      IRField(name: f.name, type: _resolveType(f.type), value: f.value);

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
        parameters: e.parameters.map(_resolveParameterType).toList(),
        supertypes: e.supertypes.map(_resolveType).toList(),
        interfaces: e.interfaces.map(_resolveType).toList(),
        constructor: _resolveConstructor(e.constructor),
        constructors: e.constructors.map(_resolveConstructor).toList(),
        fields: e.fields.map(_resolveField).toList(),
        dartElement: e.dartElement,
      );
      _cache[c.dartElement] = c;
      return c;
    }
    return e;
  }

  List<IRElement> _load(Set<Element> elements) {
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

  static List<IRElement> load(Set<Element> elements) =>
      IRBuilder()._load(elements);

  static String _dumpType(IRType t) {
    if (t is IRParameterizedType) {
      if (t.parameters.isNotEmpty) {
        final params = t.parameters.map(_dumpType).join(', ');
        return '${t.name}<$params>';
      }
    } else if (t is IRTypeParameter) {
      final b = t.bound;
      return t.name + (b != null ? ' extends ${_dumpType(b)}' : '');
    }
    return t.name;
  }

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
            ? '<${comma(e.parameters.map(_dumpType))}>'
            : '';
        final ext = e.supertypes.isNotEmpty
            ? ' extends ' + comma(e.supertypes.map(_dumpType))
            : '';
        final impl = e.interfaces.isNotEmpty
            ? ' implements ' + comma(e.interfaces.map(_dumpType))
            : '';
        p('${abs}class ${e.name}$params$ext$impl:');
        p.t(() {
          if (e.fields.isNotEmpty) {
            p('static:');
            p.t(() {
              for (final f in e.fields) {
                final v = f.value is! IRUndefined ? ' = ${f.value}' : '';
                p('${f.name}: ${_dumpType(f.type)}$v');
              }
            });
          }
          if (e.constructor.fields.isNotEmpty) {
            p('default:');
            p.t(() {
              for (final f in e.constructor.fields) {
                p('${f.name}: ${_dumpType(f.type)}');
              }
            });
          }
          for (final c in e.constructors) {
            p('${c.name}:');
            p.t(() {
              for (final f in c.fields) {
                p('${f.name}: ${_dumpType(f.type)}');
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
