// ignore_for_file: deprecated_member_use
// ignore_for_file: use_full_hex_values_for_flutter_colors
// ignore_for_file: unnecessary_const
import 'dart:ui';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/services.dart';
import 'unmarshal.dart';

Object _uObject(Map<String, dynamic> __m) {
  return const Object(
  );
}

RouteSettings _uRouteSettings(Map<String, dynamic> __m) {
  final __m1 = __m['name'];
  final String? name = (__m1 != null ? uString(__m1) : null);
  final __m2 = __m['arguments'];
  final Object? arguments = (__m2 != null ? uClass<Object>(__m2) : null);
  return RouteSettings(
    name: name,
    arguments: arguments,
  );
}

NavigatorObserver _uNavigatorObserver(Map<String, dynamic> __m) {
  return NavigatorObserver(
  );
}

Navigator _uNavigator(Map<String, dynamic> __m) {
  final __m1 = __m['key'];
  final Key? key = (__m1 != null ? uClass<Key>(__m1) : null);
  final __m2 = __m['pages'];
  final List<Page<dynamic>> pages = (__m2 != null ? (__m2 is List<dynamic> ? __m2.map((v) => uClass<Page<dynamic>>(v)).toList() : die('not a list')) : <Page<dynamic>>[]);
  final __m3 = __m['onPopPage'];
  final bool Function(Route<dynamic>, dynamic)? onPopPage = (__m3 != null ? uFunc<bool Function(Route<dynamic>, dynamic)>(__m3) : null);
  final __m4 = __m['initialRoute'];
  final String? initialRoute = (__m4 != null ? uString(__m4) : null);
  final __m5 = __m['onGenerateInitialRoutes'];
  final List<Route<dynamic>> Function(NavigatorState, String) onGenerateInitialRoutes = (__m5 != null ? uFunc<List<Route<dynamic>> Function(NavigatorState, String)>(__m5) : Navigator.defaultGenerateInitialRoutes);
  final __m6 = __m['onGenerateRoute'];
  final Route<dynamic>? Function(RouteSettings)? onGenerateRoute = (__m6 != null ? uFunc<Route<dynamic>? Function(RouteSettings)>(__m6) : null);
  final __m7 = __m['onUnknownRoute'];
  final Route<dynamic>? Function(RouteSettings)? onUnknownRoute = (__m7 != null ? uFunc<Route<dynamic>? Function(RouteSettings)>(__m7) : null);
  final __m8 = __m['transitionDelegate'];
  final TransitionDelegate<dynamic> transitionDelegate = (__m8 != null ? uClass<TransitionDelegate<dynamic>>(__m8) : const DefaultTransitionDelegate());
  final __m9 = __m['reportsRouteUpdateToEngine'];
  final bool reportsRouteUpdateToEngine = (__m9 != null ? uBool(__m9) : false);
  final __m10 = __m['observers'];
  final List<NavigatorObserver> observers = (__m10 != null ? (__m10 is List<dynamic> ? __m10.map((v) => uClass<NavigatorObserver>(v)).toList() : die('not a list')) : <NavigatorObserver>[]);
  final __m11 = __m['restorationScopeId'];
  final String? restorationScopeId = (__m11 != null ? uString(__m11) : null);
  return Navigator(
    key: key,
    pages: pages,
    onPopPage: onPopPage,
    initialRoute: initialRoute,
    onGenerateInitialRoutes: onGenerateInitialRoutes,
    onGenerateRoute: onGenerateRoute,
    onUnknownRoute: onUnknownRoute,
    transitionDelegate: transitionDelegate,
    reportsRouteUpdateToEngine: reportsRouteUpdateToEngine,
    observers: observers,
    restorationScopeId: restorationScopeId,
  );
}

NavigatorState _uNavigatorState(Map<String, dynamic> __m) {
  return NavigatorState(
  );
}

ScaffoldMessenger _uScaffoldMessenger(Map<String, dynamic> __m) {
  final __m1 = __m['key'];
  final Key? key = (__m1 != null ? uClass<Key>(__m1) : null);
  final __m2 = __m['child'];
  final Widget child = uClass<Widget>(__m2);
  return ScaffoldMessenger(
    key: key,
    child: child,
  );
}

ScaffoldMessengerState _uScaffoldMessengerState(Map<String, dynamic> __m) {
  return ScaffoldMessengerState(
  );
}

MapEntry _uMapEntry<K, V>(Map<String, dynamic> __m) {
  final __m1 = __m['key'];
  final K key = uClass<K>(__m1);
  final __m2 = __m['value'];
  final V value = uClass<V>(__m2);
  return MapEntry(
    key,
    value,
  );
}

Color _uColor(Map<String, dynamic> __m) {
  final __m1 = __m['value'];
  final int value = uInt(__m1);
  return Color(
    value,
  );
}

Color _uColorFromARGB(Map<String, dynamic> __m) {
  final __m1 = __m['a'];
  final int a = uInt(__m1);
  final __m2 = __m['r'];
  final int r = uInt(__m2);
  final __m3 = __m['g'];
  final int g = uInt(__m3);
  final __m4 = __m['b'];
  final int b = uInt(__m4);
  return Color.fromARGB(
    a,
    r,
    g,
    b,
  );
}

Color _uColorFromRGBO(Map<String, dynamic> __m) {
  final __m1 = __m['r'];
  final int r = uInt(__m1);
  final __m2 = __m['g'];
  final int g = uInt(__m2);
  final __m3 = __m['b'];
  final int b = uInt(__m3);
  final __m4 = __m['opacity'];
  final double opacity = uDouble(__m4);
  return Color.fromRGBO(
    r,
    g,
    b,
    opacity,
  );
}

Brightness _uBrightness(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'dark':
        return Brightness.dark;
      case 'light':
        return Brightness.light;
    }
  }
  throw 'illegal enum value $v';
}

VisualDensity _uVisualDensity(Map<String, dynamic> __m) {
  final __m1 = __m['horizontal'];
  final double horizontal = (__m1 != null ? uDouble(__m1) : 0.0);
  final __m2 = __m['vertical'];
  final double vertical = (__m2 != null ? uDouble(__m2) : 0.0);
  return VisualDensity(
    horizontal: horizontal,
    vertical: vertical,
  );
}

ColorSwatch _uColorSwatch<T>(Map<String, dynamic> __m) {
  final __m1 = __m['primary'];
  final int primary = uInt(__m1);
  final __m2 = __m['_swatch'];
  final Map<T, Color> _swatch = (__m2 is Map<dynamic, dynamic> ? __m2.map((k, v) => MapEntry(uClass<T>(k), uClass<Color>(v))) : die('not a map'));
  return ColorSwatch(
    primary,
    _swatch,
  );
}

MaterialColor _uMaterialColor(Map<String, dynamic> __m) {
  final __m1 = __m['primary'];
  final int primary = uInt(__m1);
  final __m2 = __m['swatch'];
  final Map<int, Color> swatch = (__m2 is Map<dynamic, dynamic> ? __m2.map((k, v) => MapEntry(uInt(k), uClass<Color>(v))) : die('not a map'));
  return MaterialColor(
    primary,
    swatch,
  );
}

ButtonTextTheme _uButtonTextTheme(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'normal':
        return ButtonTextTheme.normal;
      case 'accent':
        return ButtonTextTheme.accent;
      case 'primary':
        return ButtonTextTheme.primary;
    }
  }
  throw 'illegal enum value $v';
}

ButtonBarLayoutBehavior _uButtonBarLayoutBehavior(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'constrained':
        return ButtonBarLayoutBehavior.constrained;
      case 'padded':
        return ButtonBarLayoutBehavior.padded;
    }
  }
  throw 'illegal enum value $v';
}

ColorScheme _uColorScheme(Map<String, dynamic> __m) {
  final __m1 = __m['primary'];
  final Color primary = uClass<Color>(__m1);
  final __m2 = __m['primaryVariant'];
  final Color primaryVariant = uClass<Color>(__m2);
  final __m3 = __m['secondary'];
  final Color secondary = uClass<Color>(__m3);
  final __m4 = __m['secondaryVariant'];
  final Color secondaryVariant = uClass<Color>(__m4);
  final __m5 = __m['surface'];
  final Color surface = uClass<Color>(__m5);
  final __m6 = __m['background'];
  final Color background = uClass<Color>(__m6);
  final __m7 = __m['error'];
  final Color error = uClass<Color>(__m7);
  final __m8 = __m['onPrimary'];
  final Color onPrimary = uClass<Color>(__m8);
  final __m9 = __m['onSecondary'];
  final Color onSecondary = uClass<Color>(__m9);
  final __m10 = __m['onSurface'];
  final Color onSurface = uClass<Color>(__m10);
  final __m11 = __m['onBackground'];
  final Color onBackground = uClass<Color>(__m11);
  final __m12 = __m['onError'];
  final Color onError = uClass<Color>(__m12);
  final __m13 = __m['brightness'];
  final Brightness brightness = _uBrightness(__m13);
  return ColorScheme(
    primary: primary,
    primaryVariant: primaryVariant,
    secondary: secondary,
    secondaryVariant: secondaryVariant,
    surface: surface,
    background: background,
    error: error,
    onPrimary: onPrimary,
    onSecondary: onSecondary,
    onSurface: onSurface,
    onBackground: onBackground,
    onError: onError,
    brightness: brightness,
  );
}

ColorScheme _uColorSchemeLight(Map<String, dynamic> __m) {
  final __m1 = __m['primary'];
  final Color primary = (__m1 != null ? uClass<Color>(__m1) : const Color(4284612846));
  final __m2 = __m['primaryVariant'];
  final Color primaryVariant = (__m2 != null ? uClass<Color>(__m2) : const Color(4281794739));
  final __m3 = __m['secondary'];
  final Color secondary = (__m3 != null ? uClass<Color>(__m3) : const Color(4278442694));
  final __m4 = __m['secondaryVariant'];
  final Color secondaryVariant = (__m4 != null ? uClass<Color>(__m4) : const Color(4278290310));
  final __m5 = __m['surface'];
  final Color surface = (__m5 != null ? uClass<Color>(__m5) : const Color(4294967295));
  final __m6 = __m['background'];
  final Color background = (__m6 != null ? uClass<Color>(__m6) : const Color(4294967295));
  final __m7 = __m['error'];
  final Color error = (__m7 != null ? uClass<Color>(__m7) : const Color(4289724448));
  final __m8 = __m['onPrimary'];
  final Color onPrimary = (__m8 != null ? uClass<Color>(__m8) : const Color(4294967295));
  final __m9 = __m['onSecondary'];
  final Color onSecondary = (__m9 != null ? uClass<Color>(__m9) : const Color(4278190080));
  final __m10 = __m['onSurface'];
  final Color onSurface = (__m10 != null ? uClass<Color>(__m10) : const Color(4278190080));
  final __m11 = __m['onBackground'];
  final Color onBackground = (__m11 != null ? uClass<Color>(__m11) : const Color(4278190080));
  final __m12 = __m['onError'];
  final Color onError = (__m12 != null ? uClass<Color>(__m12) : const Color(4294967295));
  final __m13 = __m['brightness'];
  final Brightness brightness = (__m13 != null ? _uBrightness(__m13) : Brightness.light);
  return ColorScheme.light(
    primary: primary,
    primaryVariant: primaryVariant,
    secondary: secondary,
    secondaryVariant: secondaryVariant,
    surface: surface,
    background: background,
    error: error,
    onPrimary: onPrimary,
    onSecondary: onSecondary,
    onSurface: onSurface,
    onBackground: onBackground,
    onError: onError,
    brightness: brightness,
  );
}

ColorScheme _uColorSchemeDark(Map<String, dynamic> __m) {
  final __m1 = __m['primary'];
  final Color primary = (__m1 != null ? uClass<Color>(__m1) : const Color(4290479868));
  final __m2 = __m['primaryVariant'];
  final Color primaryVariant = (__m2 != null ? uClass<Color>(__m2) : const Color(4281794739));
  final __m3 = __m['secondary'];
  final Color secondary = (__m3 != null ? uClass<Color>(__m3) : const Color(4278442694));
  final __m4 = __m['secondaryVariant'];
  final Color secondaryVariant = (__m4 != null ? uClass<Color>(__m4) : const Color(4278442694));
  final __m5 = __m['surface'];
  final Color surface = (__m5 != null ? uClass<Color>(__m5) : const Color(4279374354));
  final __m6 = __m['background'];
  final Color background = (__m6 != null ? uClass<Color>(__m6) : const Color(4279374354));
  final __m7 = __m['error'];
  final Color error = (__m7 != null ? uClass<Color>(__m7) : const Color(4291782265));
  final __m8 = __m['onPrimary'];
  final Color onPrimary = (__m8 != null ? uClass<Color>(__m8) : const Color(4278190080));
  final __m9 = __m['onSecondary'];
  final Color onSecondary = (__m9 != null ? uClass<Color>(__m9) : const Color(4278190080));
  final __m10 = __m['onSurface'];
  final Color onSurface = (__m10 != null ? uClass<Color>(__m10) : const Color(4294967295));
  final __m11 = __m['onBackground'];
  final Color onBackground = (__m11 != null ? uClass<Color>(__m11) : const Color(4294967295));
  final __m12 = __m['onError'];
  final Color onError = (__m12 != null ? uClass<Color>(__m12) : const Color(4278190080));
  final __m13 = __m['brightness'];
  final Brightness brightness = (__m13 != null ? _uBrightness(__m13) : Brightness.dark);
  return ColorScheme.dark(
    primary: primary,
    primaryVariant: primaryVariant,
    secondary: secondary,
    secondaryVariant: secondaryVariant,
    surface: surface,
    background: background,
    error: error,
    onPrimary: onPrimary,
    onSecondary: onSecondary,
    onSurface: onSurface,
    onBackground: onBackground,
    onError: onError,
    brightness: brightness,
  );
}

ColorScheme _uColorSchemeHighContrastLight(Map<String, dynamic> __m) {
  final __m1 = __m['primary'];
  final Color primary = (__m1 != null ? uClass<Color>(__m1) : const Color(4278190266));
  final __m2 = __m['primaryVariant'];
  final Color primaryVariant = (__m2 != null ? uClass<Color>(__m2) : const Color(4278190216));
  final __m3 = __m['secondary'];
  final Color secondary = (__m3 != null ? uClass<Color>(__m3) : const Color(4284940281));
  final __m4 = __m['secondaryVariant'];
  final Color secondaryVariant = (__m4 != null ? uClass<Color>(__m4) : const Color(4278290310));
  final __m5 = __m['surface'];
  final Color surface = (__m5 != null ? uClass<Color>(__m5) : const Color(4294967295));
  final __m6 = __m['background'];
  final Color background = (__m6 != null ? uClass<Color>(__m6) : const Color(4294967295));
  final __m7 = __m['error'];
  final Color error = (__m7 != null ? uClass<Color>(__m7) : const Color(4286119936));
  final __m8 = __m['onPrimary'];
  final Color onPrimary = (__m8 != null ? uClass<Color>(__m8) : const Color(4294967295));
  final __m9 = __m['onSecondary'];
  final Color onSecondary = (__m9 != null ? uClass<Color>(__m9) : const Color(4278190080));
  final __m10 = __m['onSurface'];
  final Color onSurface = (__m10 != null ? uClass<Color>(__m10) : const Color(4278190080));
  final __m11 = __m['onBackground'];
  final Color onBackground = (__m11 != null ? uClass<Color>(__m11) : const Color(4278190080));
  final __m12 = __m['onError'];
  final Color onError = (__m12 != null ? uClass<Color>(__m12) : const Color(4294967295));
  final __m13 = __m['brightness'];
  final Brightness brightness = (__m13 != null ? _uBrightness(__m13) : Brightness.light);
  return ColorScheme.highContrastLight(
    primary: primary,
    primaryVariant: primaryVariant,
    secondary: secondary,
    secondaryVariant: secondaryVariant,
    surface: surface,
    background: background,
    error: error,
    onPrimary: onPrimary,
    onSecondary: onSecondary,
    onSurface: onSurface,
    onBackground: onBackground,
    onError: onError,
    brightness: brightness,
  );
}

ColorScheme _uColorSchemeHighContrastDark(Map<String, dynamic> __m) {
  final __m1 = __m['primary'];
  final Color primary = (__m1 != null ? uClass<Color>(__m1) : const Color(4293900287));
  final __m2 = __m['primaryVariant'];
  final Color primaryVariant = (__m2 != null ? uClass<Color>(__m2) : const Color(4290682623));
  final __m3 = __m['secondary'];
  final Color secondary = (__m3 != null ? uClass<Color>(__m3) : const Color(4284940281));
  final __m4 = __m['secondaryVariant'];
  final Color secondaryVariant = (__m4 != null ? uClass<Color>(__m4) : const Color(4284940281));
  final __m5 = __m['surface'];
  final Color surface = (__m5 != null ? uClass<Color>(__m5) : const Color(4279374354));
  final __m6 = __m['background'];
  final Color background = (__m6 != null ? uClass<Color>(__m6) : const Color(4279374354));
  final __m7 = __m['error'];
  final Color error = (__m7 != null ? uClass<Color>(__m7) : const Color(4288362317));
  final __m8 = __m['onPrimary'];
  final Color onPrimary = (__m8 != null ? uClass<Color>(__m8) : const Color(4278190080));
  final __m9 = __m['onSecondary'];
  final Color onSecondary = (__m9 != null ? uClass<Color>(__m9) : const Color(4278190080));
  final __m10 = __m['onSurface'];
  final Color onSurface = (__m10 != null ? uClass<Color>(__m10) : const Color(4294967295));
  final __m11 = __m['onBackground'];
  final Color onBackground = (__m11 != null ? uClass<Color>(__m11) : const Color(4294967295));
  final __m12 = __m['onError'];
  final Color onError = (__m12 != null ? uClass<Color>(__m12) : const Color(4278190080));
  final __m13 = __m['brightness'];
  final Brightness brightness = (__m13 != null ? _uBrightness(__m13) : Brightness.dark);
  return ColorScheme.highContrastDark(
    primary: primary,
    primaryVariant: primaryVariant,
    secondary: secondary,
    secondaryVariant: secondaryVariant,
    surface: surface,
    background: background,
    error: error,
    onPrimary: onPrimary,
    onSecondary: onSecondary,
    onSurface: onSurface,
    onBackground: onBackground,
    onError: onError,
    brightness: brightness,
  );
}

ColorScheme _uColorSchemeFromSwatch(Map<String, dynamic> __m) {
  final __m1 = __m['primarySwatch'];
  final MaterialColor primarySwatch = (__m1 != null ? uClass<MaterialColor>(__m1) : const MaterialColor(4280391411, <int, Color>{50: const Color(4293128957), 100: const Color(4290502395), 200: const Color(4287679225), 300: const Color(4284790262), 400: const Color(4282557941), 500: const Color(4280391411), 600: const Color(4280191205), 700: const Color(4279858898), 800: const Color(4279592384), 900: const Color(4279060385)}));
  final __m2 = __m['primaryColorDark'];
  final Color? primaryColorDark = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['accentColor'];
  final Color? accentColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['cardColor'];
  final Color? cardColor = (__m4 != null ? uClass<Color>(__m4) : null);
  final __m5 = __m['backgroundColor'];
  final Color? backgroundColor = (__m5 != null ? uClass<Color>(__m5) : null);
  final __m6 = __m['errorColor'];
  final Color? errorColor = (__m6 != null ? uClass<Color>(__m6) : null);
  final __m7 = __m['brightness'];
  final Brightness brightness = (__m7 != null ? _uBrightness(__m7) : Brightness.light);
  return ColorScheme.fromSwatch(
    primarySwatch: primarySwatch,
    primaryColorDark: primaryColorDark,
    accentColor: accentColor,
    cardColor: cardColor,
    backgroundColor: backgroundColor,
    errorColor: errorColor,
    brightness: brightness,
  );
}

MaterialTapTargetSize _uMaterialTapTargetSize(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'padded':
        return MaterialTapTargetSize.padded;
      case 'shrinkWrap':
        return MaterialTapTargetSize.shrinkWrap;
    }
  }
  throw 'illegal enum value $v';
}

ButtonThemeData _uButtonThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['textTheme'];
  final ButtonTextTheme textTheme = (__m1 != null ? _uButtonTextTheme(__m1) : ButtonTextTheme.normal);
  final __m2 = __m['minWidth'];
  final double minWidth = (__m2 != null ? uDouble(__m2) : 88.0);
  final __m3 = __m['height'];
  final double height = (__m3 != null ? uDouble(__m3) : 36.0);
  final __m4 = __m['padding'];
  final EdgeInsetsGeometry? padding = (__m4 != null ? uClass<EdgeInsetsGeometry>(__m4) : null);
  final __m5 = __m['shape'];
  final ShapeBorder? shape = (__m5 != null ? uClass<ShapeBorder>(__m5) : null);
  final __m6 = __m['layoutBehavior'];
  final ButtonBarLayoutBehavior layoutBehavior = (__m6 != null ? _uButtonBarLayoutBehavior(__m6) : ButtonBarLayoutBehavior.padded);
  final __m7 = __m['alignedDropdown'];
  final bool alignedDropdown = (__m7 != null ? uBool(__m7) : false);
  final __m8 = __m['buttonColor'];
  final Color? buttonColor = (__m8 != null ? uClass<Color>(__m8) : null);
  final __m9 = __m['disabledColor'];
  final Color? disabledColor = (__m9 != null ? uClass<Color>(__m9) : null);
  final __m10 = __m['focusColor'];
  final Color? focusColor = (__m10 != null ? uClass<Color>(__m10) : null);
  final __m11 = __m['hoverColor'];
  final Color? hoverColor = (__m11 != null ? uClass<Color>(__m11) : null);
  final __m12 = __m['highlightColor'];
  final Color? highlightColor = (__m12 != null ? uClass<Color>(__m12) : null);
  final __m13 = __m['splashColor'];
  final Color? splashColor = (__m13 != null ? uClass<Color>(__m13) : null);
  final __m14 = __m['colorScheme'];
  final ColorScheme? colorScheme = (__m14 != null ? uClass<ColorScheme>(__m14) : null);
  final __m15 = __m['materialTapTargetSize'];
  final MaterialTapTargetSize? materialTapTargetSize = (__m15 != null ? _uMaterialTapTargetSize(__m15) : null);
  return ButtonThemeData(
    textTheme: textTheme,
    minWidth: minWidth,
    height: height,
    padding: padding,
    shape: shape,
    layoutBehavior: layoutBehavior,
    alignedDropdown: alignedDropdown,
    buttonColor: buttonColor,
    disabledColor: disabledColor,
    focusColor: focusColor,
    hoverColor: hoverColor,
    highlightColor: highlightColor,
    splashColor: splashColor,
    colorScheme: colorScheme,
    materialTapTargetSize: materialTapTargetSize,
  );
}

FontStyle _uFontStyle(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'normal':
        return FontStyle.normal;
      case 'italic':
        return FontStyle.italic;
    }
  }
  throw 'illegal enum value $v';
}

TextBaseline _uTextBaseline(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'alphabetic':
        return TextBaseline.alphabetic;
      case 'ideographic':
        return TextBaseline.ideographic;
    }
  }
  throw 'illegal enum value $v';
}

TextLeadingDistribution _uTextLeadingDistribution(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'proportional':
        return TextLeadingDistribution.proportional;
      case 'even':
        return TextLeadingDistribution.even;
    }
  }
  throw 'illegal enum value $v';
}

Locale _uLocale(Map<String, dynamic> __m) {
  final __m1 = __m['_languageCode'];
  final String _languageCode = uString(__m1);
  final __m2 = __m['_countryCode'];
  final String? _countryCode = (__m2 != null ? uString(__m2) : null);
  return Locale(
    _languageCode,
    _countryCode,
  );
}

Locale _uLocaleFromSubtags(Map<String, dynamic> __m) {
  final __m1 = __m['languageCode'];
  final String languageCode = (__m1 != null ? uString(__m1) : 'und');
  final __m2 = __m['scriptCode'];
  final String? scriptCode = (__m2 != null ? uString(__m2) : null);
  final __m3 = __m['countryCode'];
  final String? countryCode = (__m3 != null ? uString(__m3) : null);
  return Locale.fromSubtags(
    languageCode: languageCode,
    scriptCode: scriptCode,
    countryCode: countryCode,
  );
}

Paint _uPaint(Map<String, dynamic> __m) {
  return Paint(
  );
}

Offset _uOffset(Map<String, dynamic> __m) {
  final __m1 = __m['dx'];
  final double dx = uDouble(__m1);
  final __m2 = __m['dy'];
  final double dy = uDouble(__m2);
  return Offset(
    dx,
    dy,
  );
}

Offset _uOffsetFromDirection(Map<String, dynamic> __m) {
  final __m1 = __m['direction'];
  final double direction = uDouble(__m1);
  final __m2 = __m['distance'];
  final double distance = (__m2 != null ? uDouble(__m2) : 1.0);
  return Offset.fromDirection(
    direction,
    distance,
  );
}

Shadow _uShadow(Map<String, dynamic> __m) {
  final __m1 = __m['color'];
  final Color color = (__m1 != null ? uClass<Color>(__m1) : const Color(4278190080));
  final __m2 = __m['offset'];
  final Offset offset = (__m2 != null ? uClass<Offset>(__m2) : const Offset(0.0, 0.0));
  final __m3 = __m['blurRadius'];
  final double blurRadius = (__m3 != null ? uDouble(__m3) : 0.0);
  return Shadow(
    color: color,
    offset: offset,
    blurRadius: blurRadius,
  );
}

FontFeature _uFontFeature(Map<String, dynamic> __m) {
  final __m1 = __m['feature'];
  final String feature = uString(__m1);
  final __m2 = __m['value'];
  final int value = (__m2 != null ? uInt(__m2) : 1);
  return FontFeature(
    feature,
    value,
  );
}

FontFeature _uFontFeatureEnable(Map<String, dynamic> __m) {
  final __m1 = __m['feature'];
  final String feature = uString(__m1);
  return FontFeature.enable(
    feature,
  );
}

FontFeature _uFontFeatureDisable(Map<String, dynamic> __m) {
  final __m1 = __m['feature'];
  final String feature = uString(__m1);
  return FontFeature.disable(
    feature,
  );
}

FontFeature _uFontFeatureAlternative(Map<String, dynamic> __m) {
  final __m1 = __m['value'];
  final int value = uInt(__m1);
  return FontFeature.alternative(
    value,
  );
}

FontFeature _uFontFeatureAlternativeFractions(Map<String, dynamic> __m) {
  return const FontFeature.alternativeFractions(
  );
}

FontFeature _uFontFeatureContextualAlternates(Map<String, dynamic> __m) {
  return const FontFeature.contextualAlternates(
  );
}

FontFeature _uFontFeatureCaseSensitiveForms(Map<String, dynamic> __m) {
  return const FontFeature.caseSensitiveForms(
  );
}

FontFeature _uFontFeatureCharacterVariant(Map<String, dynamic> __m) {
  final __m1 = __m['value'];
  final int value = uInt(__m1);
  return FontFeature.characterVariant(
    value,
  );
}

FontFeature _uFontFeatureDenominator(Map<String, dynamic> __m) {
  return const FontFeature.denominator(
  );
}

FontFeature _uFontFeatureFractions(Map<String, dynamic> __m) {
  return const FontFeature.fractions(
  );
}

FontFeature _uFontFeatureHistoricalForms(Map<String, dynamic> __m) {
  return const FontFeature.historicalForms(
  );
}

FontFeature _uFontFeatureHistoricalLigatures(Map<String, dynamic> __m) {
  return const FontFeature.historicalLigatures(
  );
}

FontFeature _uFontFeatureLiningFigures(Map<String, dynamic> __m) {
  return const FontFeature.liningFigures(
  );
}

FontFeature _uFontFeatureLocaleAware(Map<String, dynamic> __m) {
  final __m1 = __m['enable'];
  final bool enable = (__m1 != null ? uBool(__m1) : true);
  return FontFeature.localeAware(
    enable: enable,
  );
}

FontFeature _uFontFeatureNotationalForms(Map<String, dynamic> __m) {
  final __m1 = __m['value'];
  final int value = (__m1 != null ? uInt(__m1) : 1);
  return FontFeature.notationalForms(
    value,
  );
}

FontFeature _uFontFeatureNumerators(Map<String, dynamic> __m) {
  return const FontFeature.numerators(
  );
}

FontFeature _uFontFeatureOldstyleFigures(Map<String, dynamic> __m) {
  return const FontFeature.oldstyleFigures(
  );
}

FontFeature _uFontFeatureOrdinalForms(Map<String, dynamic> __m) {
  return const FontFeature.ordinalForms(
  );
}

FontFeature _uFontFeatureProportionalFigures(Map<String, dynamic> __m) {
  return const FontFeature.proportionalFigures(
  );
}

FontFeature _uFontFeatureRandomize(Map<String, dynamic> __m) {
  return const FontFeature.randomize(
  );
}

FontFeature _uFontFeatureStylisticAlternates(Map<String, dynamic> __m) {
  return const FontFeature.stylisticAlternates(
  );
}

FontFeature _uFontFeatureScientificInferiors(Map<String, dynamic> __m) {
  return const FontFeature.scientificInferiors(
  );
}

FontFeature _uFontFeatureStylisticSet(Map<String, dynamic> __m) {
  final __m1 = __m['value'];
  final int value = uInt(__m1);
  return FontFeature.stylisticSet(
    value,
  );
}

FontFeature _uFontFeatureSubscripts(Map<String, dynamic> __m) {
  return const FontFeature.subscripts(
  );
}

FontFeature _uFontFeatureSuperscripts(Map<String, dynamic> __m) {
  return const FontFeature.superscripts(
  );
}

FontFeature _uFontFeatureSwash(Map<String, dynamic> __m) {
  final __m1 = __m['value'];
  final int value = (__m1 != null ? uInt(__m1) : 1);
  return FontFeature.swash(
    value,
  );
}

FontFeature _uFontFeatureTabularFigures(Map<String, dynamic> __m) {
  return const FontFeature.tabularFigures(
  );
}

FontFeature _uFontFeatureSlashedZero(Map<String, dynamic> __m) {
  return const FontFeature.slashedZero(
  );
}

TextDecoration _uTextDecorationCombine(Map<String, dynamic> __m) {
  final __m1 = __m['decorations'];
  final List<TextDecoration> decorations = (__m1 is List<dynamic> ? __m1.map((v) => uClass<TextDecoration>(v)).toList() : die('not a list'));
  return TextDecoration.combine(
    decorations,
  );
}

TextDecorationStyle _uTextDecorationStyle(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'solid':
        return TextDecorationStyle.solid;
      case 'double':
        return TextDecorationStyle.double;
      case 'dotted':
        return TextDecorationStyle.dotted;
      case 'dashed':
        return TextDecorationStyle.dashed;
      case 'wavy':
        return TextDecorationStyle.wavy;
    }
  }
  throw 'illegal enum value $v';
}

TextOverflow _uTextOverflow(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'clip':
        return TextOverflow.clip;
      case 'fade':
        return TextOverflow.fade;
      case 'ellipsis':
        return TextOverflow.ellipsis;
      case 'visible':
        return TextOverflow.visible;
    }
  }
  throw 'illegal enum value $v';
}

TextStyle _uTextStyle(Map<String, dynamic> __m) {
  final __m1 = __m['inherit'];
  final bool inherit = (__m1 != null ? uBool(__m1) : true);
  final __m2 = __m['color'];
  final Color? color = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['backgroundColor'];
  final Color? backgroundColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['fontSize'];
  final double? fontSize = (__m4 != null ? uDouble(__m4) : null);
  final __m5 = __m['fontWeight'];
  final FontWeight? fontWeight = (__m5 != null ? uClass<FontWeight>(__m5) : null);
  final __m6 = __m['fontStyle'];
  final FontStyle? fontStyle = (__m6 != null ? _uFontStyle(__m6) : null);
  final __m7 = __m['letterSpacing'];
  final double? letterSpacing = (__m7 != null ? uDouble(__m7) : null);
  final __m8 = __m['wordSpacing'];
  final double? wordSpacing = (__m8 != null ? uDouble(__m8) : null);
  final __m9 = __m['textBaseline'];
  final TextBaseline? textBaseline = (__m9 != null ? _uTextBaseline(__m9) : null);
  final __m10 = __m['height'];
  final double? height = (__m10 != null ? uDouble(__m10) : null);
  final __m11 = __m['leadingDistribution'];
  final TextLeadingDistribution? leadingDistribution = (__m11 != null ? _uTextLeadingDistribution(__m11) : null);
  final __m12 = __m['locale'];
  final Locale? locale = (__m12 != null ? uClass<Locale>(__m12) : null);
  final __m13 = __m['foreground'];
  final Paint? foreground = (__m13 != null ? uClass<Paint>(__m13) : null);
  final __m14 = __m['background'];
  final Paint? background = (__m14 != null ? uClass<Paint>(__m14) : null);
  final __m15 = __m['shadows'];
  final List<Shadow>? shadows = (__m15 != null ? (__m15 is List<dynamic> ? __m15.map((v) => uClass<Shadow>(v)).toList() : die('not a list')) : null);
  final __m16 = __m['fontFeatures'];
  final List<FontFeature>? fontFeatures = (__m16 != null ? (__m16 is List<dynamic> ? __m16.map((v) => uClass<FontFeature>(v)).toList() : die('not a list')) : null);
  final __m17 = __m['decoration'];
  final TextDecoration? decoration = (__m17 != null ? uClass<TextDecoration>(__m17) : null);
  final __m18 = __m['decorationColor'];
  final Color? decorationColor = (__m18 != null ? uClass<Color>(__m18) : null);
  final __m19 = __m['decorationStyle'];
  final TextDecorationStyle? decorationStyle = (__m19 != null ? _uTextDecorationStyle(__m19) : null);
  final __m20 = __m['decorationThickness'];
  final double? decorationThickness = (__m20 != null ? uDouble(__m20) : null);
  final __m21 = __m['debugLabel'];
  final String? debugLabel = (__m21 != null ? uString(__m21) : null);
  final __m22 = __m['fontFamily'];
  final String? fontFamily = (__m22 != null ? uString(__m22) : null);
  final __m23 = __m['fontFamilyFallback'];
  final List<String>? fontFamilyFallback = (__m23 != null ? (__m23 is List<dynamic> ? __m23.map((v) => uString(v)).toList() : die('not a list')) : null);
  final __m24 = __m['package'];
  final String? package = (__m24 != null ? uString(__m24) : null);
  final __m25 = __m['overflow'];
  final TextOverflow? overflow = (__m25 != null ? _uTextOverflow(__m25) : null);
  return TextStyle(
    inherit: inherit,
    color: color,
    backgroundColor: backgroundColor,
    fontSize: fontSize,
    fontWeight: fontWeight,
    fontStyle: fontStyle,
    letterSpacing: letterSpacing,
    wordSpacing: wordSpacing,
    textBaseline: textBaseline,
    height: height,
    leadingDistribution: leadingDistribution,
    locale: locale,
    foreground: foreground,
    background: background,
    shadows: shadows,
    fontFeatures: fontFeatures,
    decoration: decoration,
    decorationColor: decorationColor,
    decorationStyle: decorationStyle,
    decorationThickness: decorationThickness,
    debugLabel: debugLabel,
    fontFamily: fontFamily,
    fontFamilyFallback: fontFamilyFallback,
    package: package,
    overflow: overflow,
  );
}

Size _uSize(Map<String, dynamic> __m) {
  final __m1 = __m['width'];
  final double width = uDouble(__m1);
  final __m2 = __m['height'];
  final double height = uDouble(__m2);
  return Size(
    width,
    height,
  );
}

Size _uSizeCopy(Map<String, dynamic> __m) {
  final __m1 = __m['source'];
  final Size source = uClass<Size>(__m1);
  return Size.copy(
    source,
  );
}

Size _uSizeSquare(Map<String, dynamic> __m) {
  final __m1 = __m['dimension'];
  final double dimension = uDouble(__m1);
  return Size.square(
    dimension,
  );
}

Size _uSizeFromWidth(Map<String, dynamic> __m) {
  final __m1 = __m['width'];
  final double width = uDouble(__m1);
  return Size.fromWidth(
    width,
  );
}

Size _uSizeFromHeight(Map<String, dynamic> __m) {
  final __m1 = __m['height'];
  final double height = uDouble(__m1);
  return Size.fromHeight(
    height,
  );
}

Size _uSizeFromRadius(Map<String, dynamic> __m) {
  final __m1 = __m['radius'];
  final double radius = uDouble(__m1);
  return Size.fromRadius(
    radius,
  );
}

BoxConstraints _uBoxConstraints(Map<String, dynamic> __m) {
  final __m1 = __m['minWidth'];
  final double minWidth = (__m1 != null ? uDouble(__m1) : 0.0);
  final __m2 = __m['maxWidth'];
  final double maxWidth = (__m2 != null ? uDouble(__m2) : double.infinity);
  final __m3 = __m['minHeight'];
  final double minHeight = (__m3 != null ? uDouble(__m3) : 0.0);
  final __m4 = __m['maxHeight'];
  final double maxHeight = (__m4 != null ? uDouble(__m4) : double.infinity);
  return BoxConstraints(
    minWidth: minWidth,
    maxWidth: maxWidth,
    minHeight: minHeight,
    maxHeight: maxHeight,
  );
}

BoxConstraints _uBoxConstraintsTight(Map<String, dynamic> __m) {
  final __m1 = __m['size'];
  final Size size = uClass<Size>(__m1);
  return BoxConstraints.tight(
    size,
  );
}

BoxConstraints _uBoxConstraintsTightFor(Map<String, dynamic> __m) {
  final __m1 = __m['width'];
  final double? width = (__m1 != null ? uDouble(__m1) : null);
  final __m2 = __m['height'];
  final double? height = (__m2 != null ? uDouble(__m2) : null);
  return BoxConstraints.tightFor(
    width: width,
    height: height,
  );
}

BoxConstraints _uBoxConstraintsTightForFinite(Map<String, dynamic> __m) {
  final __m1 = __m['width'];
  final double width = (__m1 != null ? uDouble(__m1) : double.infinity);
  final __m2 = __m['height'];
  final double height = (__m2 != null ? uDouble(__m2) : double.infinity);
  return BoxConstraints.tightForFinite(
    width: width,
    height: height,
  );
}

BoxConstraints _uBoxConstraintsLoose(Map<String, dynamic> __m) {
  final __m1 = __m['size'];
  final Size size = uClass<Size>(__m1);
  return BoxConstraints.loose(
    size,
  );
}

BoxConstraints _uBoxConstraintsExpand(Map<String, dynamic> __m) {
  final __m1 = __m['width'];
  final double? width = (__m1 != null ? uDouble(__m1) : null);
  final __m2 = __m['height'];
  final double? height = (__m2 != null ? uDouble(__m2) : null);
  return BoxConstraints.expand(
    width: width,
    height: height,
  );
}

Radius _uRadiusCircular(Map<String, dynamic> __m) {
  final __m1 = __m['radius'];
  final double radius = uDouble(__m1);
  return Radius.circular(
    radius,
  );
}

Radius _uRadiusElliptical(Map<String, dynamic> __m) {
  final __m1 = __m['x'];
  final double x = uDouble(__m1);
  final __m2 = __m['y'];
  final double y = uDouble(__m2);
  return Radius.elliptical(
    x,
    y,
  );
}

BorderRadius _uBorderRadiusAll(Map<String, dynamic> __m) {
  final __m1 = __m['radius'];
  final Radius radius = uClass<Radius>(__m1);
  return BorderRadius.all(
    radius,
  );
}

BorderRadius _uBorderRadiusCircular(Map<String, dynamic> __m) {
  final __m1 = __m['radius'];
  final double radius = uDouble(__m1);
  return BorderRadius.circular(
    radius,
  );
}

BorderRadius _uBorderRadiusVertical(Map<String, dynamic> __m) {
  final __m1 = __m['top'];
  final Radius top = (__m1 != null ? uClass<Radius>(__m1) : const Radius.circular(0.0));
  final __m2 = __m['bottom'];
  final Radius bottom = (__m2 != null ? uClass<Radius>(__m2) : const Radius.circular(0.0));
  return BorderRadius.vertical(
    top: top,
    bottom: bottom,
  );
}

BorderRadius _uBorderRadiusHorizontal(Map<String, dynamic> __m) {
  final __m1 = __m['left'];
  final Radius left = (__m1 != null ? uClass<Radius>(__m1) : const Radius.circular(0.0));
  final __m2 = __m['right'];
  final Radius right = (__m2 != null ? uClass<Radius>(__m2) : const Radius.circular(0.0));
  return BorderRadius.horizontal(
    left: left,
    right: right,
  );
}

BorderRadius _uBorderRadiusOnly(Map<String, dynamic> __m) {
  final __m1 = __m['topLeft'];
  final Radius topLeft = (__m1 != null ? uClass<Radius>(__m1) : const Radius.circular(0.0));
  final __m2 = __m['topRight'];
  final Radius topRight = (__m2 != null ? uClass<Radius>(__m2) : const Radius.circular(0.0));
  final __m3 = __m['bottomLeft'];
  final Radius bottomLeft = (__m3 != null ? uClass<Radius>(__m3) : const Radius.circular(0.0));
  final __m4 = __m['bottomRight'];
  final Radius bottomRight = (__m4 != null ? uClass<Radius>(__m4) : const Radius.circular(0.0));
  return BorderRadius.only(
    topLeft: topLeft,
    topRight: topRight,
    bottomLeft: bottomLeft,
    bottomRight: bottomRight,
  );
}

ToggleButtonsThemeData _uToggleButtonsThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['textStyle'];
  final TextStyle? textStyle = (__m1 != null ? uClass<TextStyle>(__m1) : null);
  final __m2 = __m['constraints'];
  final BoxConstraints? constraints = (__m2 != null ? uClass<BoxConstraints>(__m2) : null);
  final __m3 = __m['color'];
  final Color? color = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['selectedColor'];
  final Color? selectedColor = (__m4 != null ? uClass<Color>(__m4) : null);
  final __m5 = __m['disabledColor'];
  final Color? disabledColor = (__m5 != null ? uClass<Color>(__m5) : null);
  final __m6 = __m['fillColor'];
  final Color? fillColor = (__m6 != null ? uClass<Color>(__m6) : null);
  final __m7 = __m['focusColor'];
  final Color? focusColor = (__m7 != null ? uClass<Color>(__m7) : null);
  final __m8 = __m['highlightColor'];
  final Color? highlightColor = (__m8 != null ? uClass<Color>(__m8) : null);
  final __m9 = __m['hoverColor'];
  final Color? hoverColor = (__m9 != null ? uClass<Color>(__m9) : null);
  final __m10 = __m['splashColor'];
  final Color? splashColor = (__m10 != null ? uClass<Color>(__m10) : null);
  final __m11 = __m['borderColor'];
  final Color? borderColor = (__m11 != null ? uClass<Color>(__m11) : null);
  final __m12 = __m['selectedBorderColor'];
  final Color? selectedBorderColor = (__m12 != null ? uClass<Color>(__m12) : null);
  final __m13 = __m['disabledBorderColor'];
  final Color? disabledBorderColor = (__m13 != null ? uClass<Color>(__m13) : null);
  final __m14 = __m['borderRadius'];
  final BorderRadius? borderRadius = (__m14 != null ? uClass<BorderRadius>(__m14) : null);
  final __m15 = __m['borderWidth'];
  final double? borderWidth = (__m15 != null ? uDouble(__m15) : null);
  return ToggleButtonsThemeData(
    textStyle: textStyle,
    constraints: constraints,
    color: color,
    selectedColor: selectedColor,
    disabledColor: disabledColor,
    fillColor: fillColor,
    focusColor: focusColor,
    highlightColor: highlightColor,
    hoverColor: hoverColor,
    splashColor: splashColor,
    borderColor: borderColor,
    selectedBorderColor: selectedBorderColor,
    disabledBorderColor: disabledBorderColor,
    borderRadius: borderRadius,
    borderWidth: borderWidth,
  );
}

TextTheme _uTextTheme(Map<String, dynamic> __m) {
  final __m1 = __m['headline1'];
  final TextStyle? headline1 = (__m1 != null ? uClass<TextStyle>(__m1) : null);
  final __m2 = __m['headline2'];
  final TextStyle? headline2 = (__m2 != null ? uClass<TextStyle>(__m2) : null);
  final __m3 = __m['headline3'];
  final TextStyle? headline3 = (__m3 != null ? uClass<TextStyle>(__m3) : null);
  final __m4 = __m['headline4'];
  final TextStyle? headline4 = (__m4 != null ? uClass<TextStyle>(__m4) : null);
  final __m5 = __m['headline5'];
  final TextStyle? headline5 = (__m5 != null ? uClass<TextStyle>(__m5) : null);
  final __m6 = __m['headline6'];
  final TextStyle? headline6 = (__m6 != null ? uClass<TextStyle>(__m6) : null);
  final __m7 = __m['subtitle1'];
  final TextStyle? subtitle1 = (__m7 != null ? uClass<TextStyle>(__m7) : null);
  final __m8 = __m['subtitle2'];
  final TextStyle? subtitle2 = (__m8 != null ? uClass<TextStyle>(__m8) : null);
  final __m9 = __m['bodyText1'];
  final TextStyle? bodyText1 = (__m9 != null ? uClass<TextStyle>(__m9) : null);
  final __m10 = __m['bodyText2'];
  final TextStyle? bodyText2 = (__m10 != null ? uClass<TextStyle>(__m10) : null);
  final __m11 = __m['caption'];
  final TextStyle? caption = (__m11 != null ? uClass<TextStyle>(__m11) : null);
  final __m12 = __m['button'];
  final TextStyle? button = (__m12 != null ? uClass<TextStyle>(__m12) : null);
  final __m13 = __m['overline'];
  final TextStyle? overline = (__m13 != null ? uClass<TextStyle>(__m13) : null);
  return TextTheme(
    headline1: headline1,
    headline2: headline2,
    headline3: headline3,
    headline4: headline4,
    headline5: headline5,
    headline6: headline6,
    subtitle1: subtitle1,
    subtitle2: subtitle2,
    bodyText1: bodyText1,
    bodyText2: bodyText2,
    caption: caption,
    button: button,
    overline: overline,
  );
}

FloatingLabelBehavior _uFloatingLabelBehavior(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'never':
        return FloatingLabelBehavior.never;
      case 'auto':
        return FloatingLabelBehavior.auto;
      case 'always':
        return FloatingLabelBehavior.always;
    }
  }
  throw 'illegal enum value $v';
}

BorderStyle _uBorderStyle(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'none':
        return BorderStyle.none;
      case 'solid':
        return BorderStyle.solid;
    }
  }
  throw 'illegal enum value $v';
}

BorderSide _uBorderSide(Map<String, dynamic> __m) {
  final __m1 = __m['color'];
  final Color color = (__m1 != null ? uClass<Color>(__m1) : const Color(4278190080));
  final __m2 = __m['width'];
  final double width = (__m2 != null ? uDouble(__m2) : 1.0);
  final __m3 = __m['style'];
  final BorderStyle style = (__m3 != null ? _uBorderStyle(__m3) : BorderStyle.solid);
  return BorderSide(
    color: color,
    width: width,
    style: style,
  );
}

InputDecorationTheme _uInputDecorationTheme(Map<String, dynamic> __m) {
  final __m1 = __m['labelStyle'];
  final TextStyle? labelStyle = (__m1 != null ? uClass<TextStyle>(__m1) : null);
  final __m2 = __m['floatingLabelStyle'];
  final TextStyle? floatingLabelStyle = (__m2 != null ? uClass<TextStyle>(__m2) : null);
  final __m3 = __m['helperStyle'];
  final TextStyle? helperStyle = (__m3 != null ? uClass<TextStyle>(__m3) : null);
  final __m4 = __m['helperMaxLines'];
  final int? helperMaxLines = (__m4 != null ? uInt(__m4) : null);
  final __m5 = __m['hintStyle'];
  final TextStyle? hintStyle = (__m5 != null ? uClass<TextStyle>(__m5) : null);
  final __m6 = __m['errorStyle'];
  final TextStyle? errorStyle = (__m6 != null ? uClass<TextStyle>(__m6) : null);
  final __m7 = __m['errorMaxLines'];
  final int? errorMaxLines = (__m7 != null ? uInt(__m7) : null);
  final __m8 = __m['floatingLabelBehavior'];
  final FloatingLabelBehavior floatingLabelBehavior = (__m8 != null ? _uFloatingLabelBehavior(__m8) : FloatingLabelBehavior.auto);
  final __m9 = __m['isDense'];
  final bool isDense = (__m9 != null ? uBool(__m9) : false);
  final __m10 = __m['contentPadding'];
  final EdgeInsetsGeometry? contentPadding = (__m10 != null ? uClass<EdgeInsetsGeometry>(__m10) : null);
  final __m11 = __m['isCollapsed'];
  final bool isCollapsed = (__m11 != null ? uBool(__m11) : false);
  final __m12 = __m['prefixStyle'];
  final TextStyle? prefixStyle = (__m12 != null ? uClass<TextStyle>(__m12) : null);
  final __m13 = __m['suffixStyle'];
  final TextStyle? suffixStyle = (__m13 != null ? uClass<TextStyle>(__m13) : null);
  final __m14 = __m['counterStyle'];
  final TextStyle? counterStyle = (__m14 != null ? uClass<TextStyle>(__m14) : null);
  final __m15 = __m['filled'];
  final bool filled = (__m15 != null ? uBool(__m15) : false);
  final __m16 = __m['fillColor'];
  final Color? fillColor = (__m16 != null ? uClass<Color>(__m16) : null);
  final __m17 = __m['focusColor'];
  final Color? focusColor = (__m17 != null ? uClass<Color>(__m17) : null);
  final __m18 = __m['hoverColor'];
  final Color? hoverColor = (__m18 != null ? uClass<Color>(__m18) : null);
  final __m19 = __m['errorBorder'];
  final InputBorder? errorBorder = (__m19 != null ? uClass<InputBorder>(__m19) : null);
  final __m20 = __m['focusedBorder'];
  final InputBorder? focusedBorder = (__m20 != null ? uClass<InputBorder>(__m20) : null);
  final __m21 = __m['focusedErrorBorder'];
  final InputBorder? focusedErrorBorder = (__m21 != null ? uClass<InputBorder>(__m21) : null);
  final __m22 = __m['disabledBorder'];
  final InputBorder? disabledBorder = (__m22 != null ? uClass<InputBorder>(__m22) : null);
  final __m23 = __m['enabledBorder'];
  final InputBorder? enabledBorder = (__m23 != null ? uClass<InputBorder>(__m23) : null);
  final __m24 = __m['border'];
  final InputBorder? border = (__m24 != null ? uClass<InputBorder>(__m24) : null);
  final __m25 = __m['alignLabelWithHint'];
  final bool alignLabelWithHint = (__m25 != null ? uBool(__m25) : false);
  final __m26 = __m['constraints'];
  final BoxConstraints? constraints = (__m26 != null ? uClass<BoxConstraints>(__m26) : null);
  return InputDecorationTheme(
    labelStyle: labelStyle,
    floatingLabelStyle: floatingLabelStyle,
    helperStyle: helperStyle,
    helperMaxLines: helperMaxLines,
    hintStyle: hintStyle,
    errorStyle: errorStyle,
    errorMaxLines: errorMaxLines,
    floatingLabelBehavior: floatingLabelBehavior,
    isDense: isDense,
    contentPadding: contentPadding,
    isCollapsed: isCollapsed,
    prefixStyle: prefixStyle,
    suffixStyle: suffixStyle,
    counterStyle: counterStyle,
    filled: filled,
    fillColor: fillColor,
    focusColor: focusColor,
    hoverColor: hoverColor,
    errorBorder: errorBorder,
    focusedBorder: focusedBorder,
    focusedErrorBorder: focusedErrorBorder,
    disabledBorder: disabledBorder,
    enabledBorder: enabledBorder,
    border: border,
    alignLabelWithHint: alignLabelWithHint,
    constraints: constraints,
  );
}

IconThemeData _uIconThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['color'];
  final Color? color = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['opacity'];
  final double? opacity = (__m2 != null ? uDouble(__m2) : null);
  final __m3 = __m['size'];
  final double? size = (__m3 != null ? uDouble(__m3) : null);
  return IconThemeData(
    color: color,
    opacity: opacity,
    size: size,
  );
}

IconThemeData _uIconThemeDataFallback(Map<String, dynamic> __m) {
  return const IconThemeData.fallback(
  );
}

ShowValueIndicator _uShowValueIndicator(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'onlyForDiscrete':
        return ShowValueIndicator.onlyForDiscrete;
      case 'onlyForContinuous':
        return ShowValueIndicator.onlyForContinuous;
      case 'always':
        return ShowValueIndicator.always;
      case 'never':
        return ShowValueIndicator.never;
    }
  }
  throw 'illegal enum value $v';
}

TextDirection _uTextDirection(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'rtl':
        return TextDirection.rtl;
      case 'ltr':
        return TextDirection.ltr;
    }
  }
  throw 'illegal enum value $v';
}

RangeValues _uRangeValues(Map<String, dynamic> __m) {
  final __m1 = __m['start'];
  final double start = uDouble(__m1);
  final __m2 = __m['end'];
  final double end = uDouble(__m2);
  return RangeValues(
    start,
    end,
  );
}

Thumb _uThumb(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'start':
        return Thumb.start;
      case 'end':
        return Thumb.end;
    }
  }
  throw 'illegal enum value $v';
}

SliderThemeData _uSliderThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['trackHeight'];
  final double? trackHeight = (__m1 != null ? uDouble(__m1) : null);
  final __m2 = __m['activeTrackColor'];
  final Color? activeTrackColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['inactiveTrackColor'];
  final Color? inactiveTrackColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['disabledActiveTrackColor'];
  final Color? disabledActiveTrackColor = (__m4 != null ? uClass<Color>(__m4) : null);
  final __m5 = __m['disabledInactiveTrackColor'];
  final Color? disabledInactiveTrackColor = (__m5 != null ? uClass<Color>(__m5) : null);
  final __m6 = __m['activeTickMarkColor'];
  final Color? activeTickMarkColor = (__m6 != null ? uClass<Color>(__m6) : null);
  final __m7 = __m['inactiveTickMarkColor'];
  final Color? inactiveTickMarkColor = (__m7 != null ? uClass<Color>(__m7) : null);
  final __m8 = __m['disabledActiveTickMarkColor'];
  final Color? disabledActiveTickMarkColor = (__m8 != null ? uClass<Color>(__m8) : null);
  final __m9 = __m['disabledInactiveTickMarkColor'];
  final Color? disabledInactiveTickMarkColor = (__m9 != null ? uClass<Color>(__m9) : null);
  final __m10 = __m['thumbColor'];
  final Color? thumbColor = (__m10 != null ? uClass<Color>(__m10) : null);
  final __m11 = __m['overlappingShapeStrokeColor'];
  final Color? overlappingShapeStrokeColor = (__m11 != null ? uClass<Color>(__m11) : null);
  final __m12 = __m['disabledThumbColor'];
  final Color? disabledThumbColor = (__m12 != null ? uClass<Color>(__m12) : null);
  final __m13 = __m['overlayColor'];
  final Color? overlayColor = (__m13 != null ? uClass<Color>(__m13) : null);
  final __m14 = __m['valueIndicatorColor'];
  final Color? valueIndicatorColor = (__m14 != null ? uClass<Color>(__m14) : null);
  final __m15 = __m['overlayShape'];
  final SliderComponentShape? overlayShape = (__m15 != null ? uClass<SliderComponentShape>(__m15) : null);
  final __m16 = __m['tickMarkShape'];
  final SliderTickMarkShape? tickMarkShape = (__m16 != null ? uClass<SliderTickMarkShape>(__m16) : null);
  final __m17 = __m['thumbShape'];
  final SliderComponentShape? thumbShape = (__m17 != null ? uClass<SliderComponentShape>(__m17) : null);
  final __m18 = __m['trackShape'];
  final SliderTrackShape? trackShape = (__m18 != null ? uClass<SliderTrackShape>(__m18) : null);
  final __m19 = __m['valueIndicatorShape'];
  final SliderComponentShape? valueIndicatorShape = (__m19 != null ? uClass<SliderComponentShape>(__m19) : null);
  final __m20 = __m['rangeTickMarkShape'];
  final RangeSliderTickMarkShape? rangeTickMarkShape = (__m20 != null ? uClass<RangeSliderTickMarkShape>(__m20) : null);
  final __m21 = __m['rangeThumbShape'];
  final RangeSliderThumbShape? rangeThumbShape = (__m21 != null ? uClass<RangeSliderThumbShape>(__m21) : null);
  final __m22 = __m['rangeTrackShape'];
  final RangeSliderTrackShape? rangeTrackShape = (__m22 != null ? uClass<RangeSliderTrackShape>(__m22) : null);
  final __m23 = __m['rangeValueIndicatorShape'];
  final RangeSliderValueIndicatorShape? rangeValueIndicatorShape = (__m23 != null ? uClass<RangeSliderValueIndicatorShape>(__m23) : null);
  final __m24 = __m['showValueIndicator'];
  final ShowValueIndicator? showValueIndicator = (__m24 != null ? _uShowValueIndicator(__m24) : null);
  final __m25 = __m['valueIndicatorTextStyle'];
  final TextStyle? valueIndicatorTextStyle = (__m25 != null ? uClass<TextStyle>(__m25) : null);
  final __m26 = __m['minThumbSeparation'];
  final double? minThumbSeparation = (__m26 != null ? uDouble(__m26) : null);
  final __m27 = __m['thumbSelector'];
  final Thumb? Function(TextDirection, RangeValues, double, Size, Size, double)? thumbSelector = (__m27 != null ? uFunc<Thumb? Function(TextDirection, RangeValues, double, Size, Size, double)>(__m27) : null);
  return SliderThemeData(
    trackHeight: trackHeight,
    activeTrackColor: activeTrackColor,
    inactiveTrackColor: inactiveTrackColor,
    disabledActiveTrackColor: disabledActiveTrackColor,
    disabledInactiveTrackColor: disabledInactiveTrackColor,
    activeTickMarkColor: activeTickMarkColor,
    inactiveTickMarkColor: inactiveTickMarkColor,
    disabledActiveTickMarkColor: disabledActiveTickMarkColor,
    disabledInactiveTickMarkColor: disabledInactiveTickMarkColor,
    thumbColor: thumbColor,
    overlappingShapeStrokeColor: overlappingShapeStrokeColor,
    disabledThumbColor: disabledThumbColor,
    overlayColor: overlayColor,
    valueIndicatorColor: valueIndicatorColor,
    overlayShape: overlayShape,
    tickMarkShape: tickMarkShape,
    thumbShape: thumbShape,
    trackShape: trackShape,
    valueIndicatorShape: valueIndicatorShape,
    rangeTickMarkShape: rangeTickMarkShape,
    rangeThumbShape: rangeThumbShape,
    rangeTrackShape: rangeTrackShape,
    rangeValueIndicatorShape: rangeValueIndicatorShape,
    showValueIndicator: showValueIndicator,
    valueIndicatorTextStyle: valueIndicatorTextStyle,
    minThumbSeparation: minThumbSeparation,
    thumbSelector: thumbSelector,
  );
}

SliderThemeData _uSliderThemeDataFromPrimaryColors(Map<String, dynamic> __m) {
  final __m1 = __m['primaryColor'];
  final Color primaryColor = uClass<Color>(__m1);
  final __m2 = __m['primaryColorDark'];
  final Color primaryColorDark = uClass<Color>(__m2);
  final __m3 = __m['primaryColorLight'];
  final Color primaryColorLight = uClass<Color>(__m3);
  final __m4 = __m['valueIndicatorTextStyle'];
  final TextStyle valueIndicatorTextStyle = uClass<TextStyle>(__m4);
  return SliderThemeData.fromPrimaryColors(
    primaryColor: primaryColor,
    primaryColorDark: primaryColorDark,
    primaryColorLight: primaryColorLight,
    valueIndicatorTextStyle: valueIndicatorTextStyle,
  );
}

TabBarIndicatorSize _uTabBarIndicatorSize(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'tab':
        return TabBarIndicatorSize.tab;
      case 'label':
        return TabBarIndicatorSize.label;
    }
  }
  throw 'illegal enum value $v';
}

TabBarTheme _uTabBarTheme(Map<String, dynamic> __m) {
  final __m1 = __m['indicator'];
  final Decoration? indicator = (__m1 != null ? uClass<Decoration>(__m1) : null);
  final __m2 = __m['indicatorSize'];
  final TabBarIndicatorSize? indicatorSize = (__m2 != null ? _uTabBarIndicatorSize(__m2) : null);
  final __m3 = __m['labelColor'];
  final Color? labelColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['labelPadding'];
  final EdgeInsetsGeometry? labelPadding = (__m4 != null ? uClass<EdgeInsetsGeometry>(__m4) : null);
  final __m5 = __m['labelStyle'];
  final TextStyle? labelStyle = (__m5 != null ? uClass<TextStyle>(__m5) : null);
  final __m6 = __m['unselectedLabelColor'];
  final Color? unselectedLabelColor = (__m6 != null ? uClass<Color>(__m6) : null);
  final __m7 = __m['unselectedLabelStyle'];
  final TextStyle? unselectedLabelStyle = (__m7 != null ? uClass<TextStyle>(__m7) : null);
  return TabBarTheme(
    indicator: indicator,
    indicatorSize: indicatorSize,
    labelColor: labelColor,
    labelPadding: labelPadding,
    labelStyle: labelStyle,
    unselectedLabelColor: unselectedLabelColor,
    unselectedLabelStyle: unselectedLabelStyle,
  );
}

Duration _uDuration(Map<String, dynamic> __m) {
  final __m1 = __m['days'];
  final int days = (__m1 != null ? uInt(__m1) : 0);
  final __m2 = __m['hours'];
  final int hours = (__m2 != null ? uInt(__m2) : 0);
  final __m3 = __m['minutes'];
  final int minutes = (__m3 != null ? uInt(__m3) : 0);
  final __m4 = __m['seconds'];
  final int seconds = (__m4 != null ? uInt(__m4) : 0);
  final __m5 = __m['milliseconds'];
  final int milliseconds = (__m5 != null ? uInt(__m5) : 0);
  final __m6 = __m['microseconds'];
  final int microseconds = (__m6 != null ? uInt(__m6) : 0);
  return Duration(
    days: days,
    hours: hours,
    minutes: minutes,
    seconds: seconds,
    milliseconds: milliseconds,
    microseconds: microseconds,
  );
}

TooltipTriggerMode _uTooltipTriggerMode(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'manual':
        return TooltipTriggerMode.manual;
      case 'longPress':
        return TooltipTriggerMode.longPress;
      case 'tap':
        return TooltipTriggerMode.tap;
    }
  }
  throw 'illegal enum value $v';
}

TooltipThemeData _uTooltipThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['height'];
  final double? height = (__m1 != null ? uDouble(__m1) : null);
  final __m2 = __m['padding'];
  final EdgeInsetsGeometry? padding = (__m2 != null ? uClass<EdgeInsetsGeometry>(__m2) : null);
  final __m3 = __m['margin'];
  final EdgeInsetsGeometry? margin = (__m3 != null ? uClass<EdgeInsetsGeometry>(__m3) : null);
  final __m4 = __m['verticalOffset'];
  final double? verticalOffset = (__m4 != null ? uDouble(__m4) : null);
  final __m5 = __m['preferBelow'];
  final bool? preferBelow = (__m5 != null ? uBool(__m5) : null);
  final __m6 = __m['excludeFromSemantics'];
  final bool? excludeFromSemantics = (__m6 != null ? uBool(__m6) : null);
  final __m7 = __m['decoration'];
  final Decoration? decoration = (__m7 != null ? uClass<Decoration>(__m7) : null);
  final __m8 = __m['textStyle'];
  final TextStyle? textStyle = (__m8 != null ? uClass<TextStyle>(__m8) : null);
  final __m9 = __m['waitDuration'];
  final Duration? waitDuration = (__m9 != null ? uClass<Duration>(__m9) : null);
  final __m10 = __m['showDuration'];
  final Duration? showDuration = (__m10 != null ? uClass<Duration>(__m10) : null);
  final __m11 = __m['triggerMode'];
  final TooltipTriggerMode? triggerMode = (__m11 != null ? _uTooltipTriggerMode(__m11) : null);
  final __m12 = __m['enableFeedback'];
  final bool? enableFeedback = (__m12 != null ? uBool(__m12) : null);
  return TooltipThemeData(
    height: height,
    padding: padding,
    margin: margin,
    verticalOffset: verticalOffset,
    preferBelow: preferBelow,
    excludeFromSemantics: excludeFromSemantics,
    decoration: decoration,
    textStyle: textStyle,
    waitDuration: waitDuration,
    showDuration: showDuration,
    triggerMode: triggerMode,
    enableFeedback: enableFeedback,
  );
}

Clip _uClip(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'none':
        return Clip.none;
      case 'hardEdge':
        return Clip.hardEdge;
      case 'antiAlias':
        return Clip.antiAlias;
      case 'antiAliasWithSaveLayer':
        return Clip.antiAliasWithSaveLayer;
    }
  }
  throw 'illegal enum value $v';
}

CardTheme _uCardTheme(Map<String, dynamic> __m) {
  final __m1 = __m['clipBehavior'];
  final Clip? clipBehavior = (__m1 != null ? _uClip(__m1) : null);
  final __m2 = __m['color'];
  final Color? color = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['shadowColor'];
  final Color? shadowColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['elevation'];
  final double? elevation = (__m4 != null ? uDouble(__m4) : null);
  final __m5 = __m['margin'];
  final EdgeInsetsGeometry? margin = (__m5 != null ? uClass<EdgeInsetsGeometry>(__m5) : null);
  final __m6 = __m['shape'];
  final ShapeBorder? shape = (__m6 != null ? uClass<ShapeBorder>(__m6) : null);
  return CardTheme(
    clipBehavior: clipBehavior,
    color: color,
    shadowColor: shadowColor,
    elevation: elevation,
    margin: margin,
    shape: shape,
  );
}

ChipThemeData _uChipThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['backgroundColor'];
  final Color backgroundColor = uClass<Color>(__m1);
  final __m2 = __m['deleteIconColor'];
  final Color? deleteIconColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['disabledColor'];
  final Color disabledColor = uClass<Color>(__m3);
  final __m4 = __m['selectedColor'];
  final Color selectedColor = uClass<Color>(__m4);
  final __m5 = __m['secondarySelectedColor'];
  final Color secondarySelectedColor = uClass<Color>(__m5);
  final __m6 = __m['shadowColor'];
  final Color? shadowColor = (__m6 != null ? uClass<Color>(__m6) : null);
  final __m7 = __m['selectedShadowColor'];
  final Color? selectedShadowColor = (__m7 != null ? uClass<Color>(__m7) : null);
  final __m8 = __m['showCheckmark'];
  final bool? showCheckmark = (__m8 != null ? uBool(__m8) : null);
  final __m9 = __m['checkmarkColor'];
  final Color? checkmarkColor = (__m9 != null ? uClass<Color>(__m9) : null);
  final __m10 = __m['labelPadding'];
  final EdgeInsetsGeometry? labelPadding = (__m10 != null ? uClass<EdgeInsetsGeometry>(__m10) : null);
  final __m11 = __m['padding'];
  final EdgeInsetsGeometry padding = uClass<EdgeInsetsGeometry>(__m11);
  final __m12 = __m['side'];
  final BorderSide? side = (__m12 != null ? uClass<BorderSide>(__m12) : null);
  final __m13 = __m['shape'];
  final OutlinedBorder? shape = (__m13 != null ? uClass<OutlinedBorder>(__m13) : null);
  final __m14 = __m['labelStyle'];
  final TextStyle labelStyle = uClass<TextStyle>(__m14);
  final __m15 = __m['secondaryLabelStyle'];
  final TextStyle secondaryLabelStyle = uClass<TextStyle>(__m15);
  final __m16 = __m['brightness'];
  final Brightness brightness = _uBrightness(__m16);
  final __m17 = __m['elevation'];
  final double? elevation = (__m17 != null ? uDouble(__m17) : null);
  final __m18 = __m['pressElevation'];
  final double? pressElevation = (__m18 != null ? uDouble(__m18) : null);
  return ChipThemeData(
    backgroundColor: backgroundColor,
    deleteIconColor: deleteIconColor,
    disabledColor: disabledColor,
    selectedColor: selectedColor,
    secondarySelectedColor: secondarySelectedColor,
    shadowColor: shadowColor,
    selectedShadowColor: selectedShadowColor,
    showCheckmark: showCheckmark,
    checkmarkColor: checkmarkColor,
    labelPadding: labelPadding,
    padding: padding,
    side: side,
    shape: shape,
    labelStyle: labelStyle,
    secondaryLabelStyle: secondaryLabelStyle,
    brightness: brightness,
    elevation: elevation,
    pressElevation: pressElevation,
  );
}

ChipThemeData _uChipThemeDataFromDefaults(Map<String, dynamic> __m) {
  final __m1 = __m['brightness'];
  final Brightness? brightness = (__m1 != null ? _uBrightness(__m1) : null);
  final __m2 = __m['primaryColor'];
  final Color? primaryColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['secondaryColor'];
  final Color secondaryColor = uClass<Color>(__m3);
  final __m4 = __m['labelStyle'];
  final TextStyle labelStyle = uClass<TextStyle>(__m4);
  return ChipThemeData.fromDefaults(
    brightness: brightness,
    primaryColor: primaryColor,
    secondaryColor: secondaryColor,
    labelStyle: labelStyle,
  );
}

TargetPlatform _uTargetPlatform(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'android':
        return TargetPlatform.android;
      case 'fuchsia':
        return TargetPlatform.fuchsia;
      case 'iOS':
        return TargetPlatform.iOS;
      case 'linux':
        return TargetPlatform.linux;
      case 'macOS':
        return TargetPlatform.macOS;
      case 'windows':
        return TargetPlatform.windows;
    }
  }
  throw 'illegal enum value $v';
}

PageTransitionsTheme _uPageTransitionsTheme(Map<String, dynamic> __m) {
  final __m1 = __m['builders'];
  final Map<TargetPlatform, PageTransitionsBuilder> builders = (__m1 != null ? (__m1 is Map<dynamic, dynamic> ? __m1.map((k, v) => MapEntry(_uTargetPlatform(k), uClass<PageTransitionsBuilder>(v))) : die('not a map')) : <TargetPlatform, PageTransitionsBuilder>{TargetPlatform.android: const FadeUpwardsPageTransitionsBuilder(), TargetPlatform.iOS: const CupertinoPageTransitionsBuilder(), TargetPlatform.linux: const FadeUpwardsPageTransitionsBuilder(), TargetPlatform.macOS: const CupertinoPageTransitionsBuilder(), TargetPlatform.windows: const FadeUpwardsPageTransitionsBuilder()});
  return PageTransitionsTheme(
    builders: builders,
  );
}

SystemUiOverlayStyle _uSystemUiOverlayStyle(Map<String, dynamic> __m) {
  final __m1 = __m['systemNavigationBarColor'];
  final Color? systemNavigationBarColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['systemNavigationBarDividerColor'];
  final Color? systemNavigationBarDividerColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['systemNavigationBarIconBrightness'];
  final Brightness? systemNavigationBarIconBrightness = (__m3 != null ? _uBrightness(__m3) : null);
  final __m4 = __m['systemNavigationBarContrastEnforced'];
  final bool? systemNavigationBarContrastEnforced = (__m4 != null ? uBool(__m4) : null);
  final __m5 = __m['statusBarColor'];
  final Color? statusBarColor = (__m5 != null ? uClass<Color>(__m5) : null);
  final __m6 = __m['statusBarBrightness'];
  final Brightness? statusBarBrightness = (__m6 != null ? _uBrightness(__m6) : null);
  final __m7 = __m['statusBarIconBrightness'];
  final Brightness? statusBarIconBrightness = (__m7 != null ? _uBrightness(__m7) : null);
  final __m8 = __m['systemStatusBarContrastEnforced'];
  final bool? systemStatusBarContrastEnforced = (__m8 != null ? uBool(__m8) : null);
  return SystemUiOverlayStyle(
    systemNavigationBarColor: systemNavigationBarColor,
    systemNavigationBarDividerColor: systemNavigationBarDividerColor,
    systemNavigationBarIconBrightness: systemNavigationBarIconBrightness,
    systemNavigationBarContrastEnforced: systemNavigationBarContrastEnforced,
    statusBarColor: statusBarColor,
    statusBarBrightness: statusBarBrightness,
    statusBarIconBrightness: statusBarIconBrightness,
    systemStatusBarContrastEnforced: systemStatusBarContrastEnforced,
  );
}

AppBarTheme _uAppBarTheme(Map<String, dynamic> __m) {
  final __m1 = __m['brightness'];
  final Brightness? brightness = (__m1 != null ? _uBrightness(__m1) : null);
  final __m2 = __m['color'];
  final Color? color = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['backgroundColor'];
  final Color? backgroundColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['foregroundColor'];
  final Color? foregroundColor = (__m4 != null ? uClass<Color>(__m4) : null);
  final __m5 = __m['elevation'];
  final double? elevation = (__m5 != null ? uDouble(__m5) : null);
  final __m6 = __m['shadowColor'];
  final Color? shadowColor = (__m6 != null ? uClass<Color>(__m6) : null);
  final __m7 = __m['shape'];
  final ShapeBorder? shape = (__m7 != null ? uClass<ShapeBorder>(__m7) : null);
  final __m8 = __m['iconTheme'];
  final IconThemeData? iconTheme = (__m8 != null ? uClass<IconThemeData>(__m8) : null);
  final __m9 = __m['actionsIconTheme'];
  final IconThemeData? actionsIconTheme = (__m9 != null ? uClass<IconThemeData>(__m9) : null);
  final __m10 = __m['textTheme'];
  final TextTheme? textTheme = (__m10 != null ? uClass<TextTheme>(__m10) : null);
  final __m11 = __m['centerTitle'];
  final bool? centerTitle = (__m11 != null ? uBool(__m11) : null);
  final __m12 = __m['titleSpacing'];
  final double? titleSpacing = (__m12 != null ? uDouble(__m12) : null);
  final __m13 = __m['toolbarHeight'];
  final double? toolbarHeight = (__m13 != null ? uDouble(__m13) : null);
  final __m14 = __m['toolbarTextStyle'];
  final TextStyle? toolbarTextStyle = (__m14 != null ? uClass<TextStyle>(__m14) : null);
  final __m15 = __m['titleTextStyle'];
  final TextStyle? titleTextStyle = (__m15 != null ? uClass<TextStyle>(__m15) : null);
  final __m16 = __m['systemOverlayStyle'];
  final SystemUiOverlayStyle? systemOverlayStyle = (__m16 != null ? uClass<SystemUiOverlayStyle>(__m16) : null);
  final __m17 = __m['backwardsCompatibility'];
  final bool? backwardsCompatibility = (__m17 != null ? uBool(__m17) : null);
  return AppBarTheme(
    brightness: brightness,
    color: color,
    backgroundColor: backgroundColor,
    foregroundColor: foregroundColor,
    elevation: elevation,
    shadowColor: shadowColor,
    shape: shape,
    iconTheme: iconTheme,
    actionsIconTheme: actionsIconTheme,
    textTheme: textTheme,
    centerTitle: centerTitle,
    titleSpacing: titleSpacing,
    toolbarHeight: toolbarHeight,
    toolbarTextStyle: toolbarTextStyle,
    titleTextStyle: titleTextStyle,
    systemOverlayStyle: systemOverlayStyle,
    backwardsCompatibility: backwardsCompatibility,
  );
}

ScrollbarThemeData _uScrollbarThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['thickness'];
  final MaterialStateProperty<double?>? thickness = (__m1 != null ? uClass<MaterialStateProperty<double?>>(__m1) : null);
  final __m2 = __m['showTrackOnHover'];
  final bool? showTrackOnHover = (__m2 != null ? uBool(__m2) : null);
  final __m3 = __m['isAlwaysShown'];
  final bool? isAlwaysShown = (__m3 != null ? uBool(__m3) : null);
  final __m4 = __m['radius'];
  final Radius? radius = (__m4 != null ? uClass<Radius>(__m4) : null);
  final __m5 = __m['thumbColor'];
  final MaterialStateProperty<Color?>? thumbColor = (__m5 != null ? uClass<MaterialStateProperty<Color?>>(__m5) : null);
  final __m6 = __m['trackColor'];
  final MaterialStateProperty<Color?>? trackColor = (__m6 != null ? uClass<MaterialStateProperty<Color?>>(__m6) : null);
  final __m7 = __m['trackBorderColor'];
  final MaterialStateProperty<Color?>? trackBorderColor = (__m7 != null ? uClass<MaterialStateProperty<Color?>>(__m7) : null);
  final __m8 = __m['crossAxisMargin'];
  final double? crossAxisMargin = (__m8 != null ? uDouble(__m8) : null);
  final __m9 = __m['mainAxisMargin'];
  final double? mainAxisMargin = (__m9 != null ? uDouble(__m9) : null);
  final __m10 = __m['minThumbLength'];
  final double? minThumbLength = (__m10 != null ? uDouble(__m10) : null);
  final __m11 = __m['interactive'];
  final bool? interactive = (__m11 != null ? uBool(__m11) : null);
  return ScrollbarThemeData(
    thickness: thickness,
    showTrackOnHover: showTrackOnHover,
    isAlwaysShown: isAlwaysShown,
    radius: radius,
    thumbColor: thumbColor,
    trackColor: trackColor,
    trackBorderColor: trackBorderColor,
    crossAxisMargin: crossAxisMargin,
    mainAxisMargin: mainAxisMargin,
    minThumbLength: minThumbLength,
    interactive: interactive,
  );
}

BottomAppBarTheme _uBottomAppBarTheme(Map<String, dynamic> __m) {
  final __m1 = __m['color'];
  final Color? color = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['elevation'];
  final double? elevation = (__m2 != null ? uDouble(__m2) : null);
  final __m3 = __m['shape'];
  final NotchedShape? shape = (__m3 != null ? uClass<NotchedShape>(__m3) : null);
  return BottomAppBarTheme(
    color: color,
    elevation: elevation,
    shape: shape,
  );
}

DialogTheme _uDialogTheme(Map<String, dynamic> __m) {
  final __m1 = __m['backgroundColor'];
  final Color? backgroundColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['elevation'];
  final double? elevation = (__m2 != null ? uDouble(__m2) : null);
  final __m3 = __m['shape'];
  final ShapeBorder? shape = (__m3 != null ? uClass<ShapeBorder>(__m3) : null);
  final __m4 = __m['titleTextStyle'];
  final TextStyle? titleTextStyle = (__m4 != null ? uClass<TextStyle>(__m4) : null);
  final __m5 = __m['contentTextStyle'];
  final TextStyle? contentTextStyle = (__m5 != null ? uClass<TextStyle>(__m5) : null);
  return DialogTheme(
    backgroundColor: backgroundColor,
    elevation: elevation,
    shape: shape,
    titleTextStyle: titleTextStyle,
    contentTextStyle: contentTextStyle,
  );
}

FloatingActionButtonThemeData _uFloatingActionButtonThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['foregroundColor'];
  final Color? foregroundColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['backgroundColor'];
  final Color? backgroundColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['focusColor'];
  final Color? focusColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['hoverColor'];
  final Color? hoverColor = (__m4 != null ? uClass<Color>(__m4) : null);
  final __m5 = __m['splashColor'];
  final Color? splashColor = (__m5 != null ? uClass<Color>(__m5) : null);
  final __m6 = __m['elevation'];
  final double? elevation = (__m6 != null ? uDouble(__m6) : null);
  final __m7 = __m['focusElevation'];
  final double? focusElevation = (__m7 != null ? uDouble(__m7) : null);
  final __m8 = __m['hoverElevation'];
  final double? hoverElevation = (__m8 != null ? uDouble(__m8) : null);
  final __m9 = __m['disabledElevation'];
  final double? disabledElevation = (__m9 != null ? uDouble(__m9) : null);
  final __m10 = __m['highlightElevation'];
  final double? highlightElevation = (__m10 != null ? uDouble(__m10) : null);
  final __m11 = __m['shape'];
  final ShapeBorder? shape = (__m11 != null ? uClass<ShapeBorder>(__m11) : null);
  final __m12 = __m['enableFeedback'];
  final bool? enableFeedback = (__m12 != null ? uBool(__m12) : null);
  final __m13 = __m['sizeConstraints'];
  final BoxConstraints? sizeConstraints = (__m13 != null ? uClass<BoxConstraints>(__m13) : null);
  final __m14 = __m['smallSizeConstraints'];
  final BoxConstraints? smallSizeConstraints = (__m14 != null ? uClass<BoxConstraints>(__m14) : null);
  final __m15 = __m['largeSizeConstraints'];
  final BoxConstraints? largeSizeConstraints = (__m15 != null ? uClass<BoxConstraints>(__m15) : null);
  final __m16 = __m['extendedSizeConstraints'];
  final BoxConstraints? extendedSizeConstraints = (__m16 != null ? uClass<BoxConstraints>(__m16) : null);
  final __m17 = __m['extendedIconLabelSpacing'];
  final double? extendedIconLabelSpacing = (__m17 != null ? uDouble(__m17) : null);
  final __m18 = __m['extendedPadding'];
  final EdgeInsetsGeometry? extendedPadding = (__m18 != null ? uClass<EdgeInsetsGeometry>(__m18) : null);
  final __m19 = __m['extendedTextStyle'];
  final TextStyle? extendedTextStyle = (__m19 != null ? uClass<TextStyle>(__m19) : null);
  return FloatingActionButtonThemeData(
    foregroundColor: foregroundColor,
    backgroundColor: backgroundColor,
    focusColor: focusColor,
    hoverColor: hoverColor,
    splashColor: splashColor,
    elevation: elevation,
    focusElevation: focusElevation,
    hoverElevation: hoverElevation,
    disabledElevation: disabledElevation,
    highlightElevation: highlightElevation,
    shape: shape,
    enableFeedback: enableFeedback,
    sizeConstraints: sizeConstraints,
    smallSizeConstraints: smallSizeConstraints,
    largeSizeConstraints: largeSizeConstraints,
    extendedSizeConstraints: extendedSizeConstraints,
    extendedIconLabelSpacing: extendedIconLabelSpacing,
    extendedPadding: extendedPadding,
    extendedTextStyle: extendedTextStyle,
  );
}

NavigationRailLabelType _uNavigationRailLabelType(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'none':
        return NavigationRailLabelType.none;
      case 'selected':
        return NavigationRailLabelType.selected;
      case 'all':
        return NavigationRailLabelType.all;
    }
  }
  throw 'illegal enum value $v';
}

NavigationRailThemeData _uNavigationRailThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['backgroundColor'];
  final Color? backgroundColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['elevation'];
  final double? elevation = (__m2 != null ? uDouble(__m2) : null);
  final __m3 = __m['unselectedLabelTextStyle'];
  final TextStyle? unselectedLabelTextStyle = (__m3 != null ? uClass<TextStyle>(__m3) : null);
  final __m4 = __m['selectedLabelTextStyle'];
  final TextStyle? selectedLabelTextStyle = (__m4 != null ? uClass<TextStyle>(__m4) : null);
  final __m5 = __m['unselectedIconTheme'];
  final IconThemeData? unselectedIconTheme = (__m5 != null ? uClass<IconThemeData>(__m5) : null);
  final __m6 = __m['selectedIconTheme'];
  final IconThemeData? selectedIconTheme = (__m6 != null ? uClass<IconThemeData>(__m6) : null);
  final __m7 = __m['groupAlignment'];
  final double? groupAlignment = (__m7 != null ? uDouble(__m7) : null);
  final __m8 = __m['labelType'];
  final NavigationRailLabelType? labelType = (__m8 != null ? _uNavigationRailLabelType(__m8) : null);
  return NavigationRailThemeData(
    backgroundColor: backgroundColor,
    elevation: elevation,
    unselectedLabelTextStyle: unselectedLabelTextStyle,
    selectedLabelTextStyle: selectedLabelTextStyle,
    unselectedIconTheme: unselectedIconTheme,
    selectedIconTheme: selectedIconTheme,
    groupAlignment: groupAlignment,
    labelType: labelType,
  );
}

Typography _uTypography(Map<String, dynamic> __m) {
  final __m1 = __m['platform'];
  final TargetPlatform? platform = (__m1 != null ? _uTargetPlatform(__m1) : null);
  final __m2 = __m['black'];
  final TextTheme? black = (__m2 != null ? uClass<TextTheme>(__m2) : null);
  final __m3 = __m['white'];
  final TextTheme? white = (__m3 != null ? uClass<TextTheme>(__m3) : null);
  final __m4 = __m['englishLike'];
  final TextTheme? englishLike = (__m4 != null ? uClass<TextTheme>(__m4) : null);
  final __m5 = __m['dense'];
  final TextTheme? dense = (__m5 != null ? uClass<TextTheme>(__m5) : null);
  final __m6 = __m['tall'];
  final TextTheme? tall = (__m6 != null ? uClass<TextTheme>(__m6) : null);
  return Typography(
    platform: platform,
    black: black,
    white: white,
    englishLike: englishLike,
    dense: dense,
    tall: tall,
  );
}

Typography _uTypographyMaterial2014(Map<String, dynamic> __m) {
  final __m1 = __m['platform'];
  final TargetPlatform? platform = (__m1 != null ? (__m1 != null ? _uTargetPlatform(__m1) : null) : TargetPlatform.android);
  final __m2 = __m['black'];
  final TextTheme? black = (__m2 != null ? uClass<TextTheme>(__m2) : null);
  final __m3 = __m['white'];
  final TextTheme? white = (__m3 != null ? uClass<TextTheme>(__m3) : null);
  final __m4 = __m['englishLike'];
  final TextTheme? englishLike = (__m4 != null ? uClass<TextTheme>(__m4) : null);
  final __m5 = __m['dense'];
  final TextTheme? dense = (__m5 != null ? uClass<TextTheme>(__m5) : null);
  final __m6 = __m['tall'];
  final TextTheme? tall = (__m6 != null ? uClass<TextTheme>(__m6) : null);
  return Typography.material2014(
    platform: platform,
    black: black,
    white: white,
    englishLike: englishLike,
    dense: dense,
    tall: tall,
  );
}

Typography _uTypographyMaterial2018(Map<String, dynamic> __m) {
  final __m1 = __m['platform'];
  final TargetPlatform? platform = (__m1 != null ? (__m1 != null ? _uTargetPlatform(__m1) : null) : TargetPlatform.android);
  final __m2 = __m['black'];
  final TextTheme? black = (__m2 != null ? uClass<TextTheme>(__m2) : null);
  final __m3 = __m['white'];
  final TextTheme? white = (__m3 != null ? uClass<TextTheme>(__m3) : null);
  final __m4 = __m['englishLike'];
  final TextTheme? englishLike = (__m4 != null ? uClass<TextTheme>(__m4) : null);
  final __m5 = __m['dense'];
  final TextTheme? dense = (__m5 != null ? uClass<TextTheme>(__m5) : null);
  final __m6 = __m['tall'];
  final TextTheme? tall = (__m6 != null ? uClass<TextTheme>(__m6) : null);
  return Typography.material2018(
    platform: platform,
    black: black,
    white: white,
    englishLike: englishLike,
    dense: dense,
    tall: tall,
  );
}

CupertinoTextThemeData _uCupertinoTextThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['primaryColor'];
  final Color primaryColor = (__m1 != null ? uClass<Color>(__m1) : const CupertinoDynamicColor.withBrightnessAndContrast(debugLabel: 'systemBlue', color: const Color.fromARGB(255, 0, 122, 255), darkColor: const Color.fromARGB(255, 10, 132, 255), highContrastColor: const Color.fromARGB(255, 0, 64, 221), darkHighContrastColor: const Color.fromARGB(255, 64, 156, 255)));
  final __m2 = __m['textStyle'];
  final TextStyle? textStyle = (__m2 != null ? uClass<TextStyle>(__m2) : null);
  final __m3 = __m['actionTextStyle'];
  final TextStyle? actionTextStyle = (__m3 != null ? uClass<TextStyle>(__m3) : null);
  final __m4 = __m['tabLabelTextStyle'];
  final TextStyle? tabLabelTextStyle = (__m4 != null ? uClass<TextStyle>(__m4) : null);
  final __m5 = __m['navTitleTextStyle'];
  final TextStyle? navTitleTextStyle = (__m5 != null ? uClass<TextStyle>(__m5) : null);
  final __m6 = __m['navLargeTitleTextStyle'];
  final TextStyle? navLargeTitleTextStyle = (__m6 != null ? uClass<TextStyle>(__m6) : null);
  final __m7 = __m['navActionTextStyle'];
  final TextStyle? navActionTextStyle = (__m7 != null ? uClass<TextStyle>(__m7) : null);
  final __m8 = __m['pickerTextStyle'];
  final TextStyle? pickerTextStyle = (__m8 != null ? uClass<TextStyle>(__m8) : null);
  final __m9 = __m['dateTimePickerTextStyle'];
  final TextStyle? dateTimePickerTextStyle = (__m9 != null ? uClass<TextStyle>(__m9) : null);
  return CupertinoTextThemeData(
    primaryColor: primaryColor,
    textStyle: textStyle,
    actionTextStyle: actionTextStyle,
    tabLabelTextStyle: tabLabelTextStyle,
    navTitleTextStyle: navTitleTextStyle,
    navLargeTitleTextStyle: navLargeTitleTextStyle,
    navActionTextStyle: navActionTextStyle,
    pickerTextStyle: pickerTextStyle,
    dateTimePickerTextStyle: dateTimePickerTextStyle,
  );
}

NoDefaultCupertinoThemeData _uNoDefaultCupertinoThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['brightness'];
  final Brightness? brightness = (__m1 != null ? _uBrightness(__m1) : null);
  final __m2 = __m['primaryColor'];
  final Color? primaryColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['primaryContrastingColor'];
  final Color? primaryContrastingColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['textTheme'];
  final CupertinoTextThemeData? textTheme = (__m4 != null ? uClass<CupertinoTextThemeData>(__m4) : null);
  final __m5 = __m['barBackgroundColor'];
  final Color? barBackgroundColor = (__m5 != null ? uClass<Color>(__m5) : null);
  final __m6 = __m['scaffoldBackgroundColor'];
  final Color? scaffoldBackgroundColor = (__m6 != null ? uClass<Color>(__m6) : null);
  return NoDefaultCupertinoThemeData(
    brightness: brightness,
    primaryColor: primaryColor,
    primaryContrastingColor: primaryContrastingColor,
    textTheme: textTheme,
    barBackgroundColor: barBackgroundColor,
    scaffoldBackgroundColor: scaffoldBackgroundColor,
  );
}

SnackBarBehavior _uSnackBarBehavior(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'fixed':
        return SnackBarBehavior.fixed;
      case 'floating':
        return SnackBarBehavior.floating;
    }
  }
  throw 'illegal enum value $v';
}

SnackBarThemeData _uSnackBarThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['backgroundColor'];
  final Color? backgroundColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['actionTextColor'];
  final Color? actionTextColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['disabledActionTextColor'];
  final Color? disabledActionTextColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['contentTextStyle'];
  final TextStyle? contentTextStyle = (__m4 != null ? uClass<TextStyle>(__m4) : null);
  final __m5 = __m['elevation'];
  final double? elevation = (__m5 != null ? uDouble(__m5) : null);
  final __m6 = __m['shape'];
  final ShapeBorder? shape = (__m6 != null ? uClass<ShapeBorder>(__m6) : null);
  final __m7 = __m['behavior'];
  final SnackBarBehavior? behavior = (__m7 != null ? _uSnackBarBehavior(__m7) : null);
  return SnackBarThemeData(
    backgroundColor: backgroundColor,
    actionTextColor: actionTextColor,
    disabledActionTextColor: disabledActionTextColor,
    contentTextStyle: contentTextStyle,
    elevation: elevation,
    shape: shape,
    behavior: behavior,
  );
}

BottomSheetThemeData _uBottomSheetThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['backgroundColor'];
  final Color? backgroundColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['elevation'];
  final double? elevation = (__m2 != null ? uDouble(__m2) : null);
  final __m3 = __m['modalBackgroundColor'];
  final Color? modalBackgroundColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['modalElevation'];
  final double? modalElevation = (__m4 != null ? uDouble(__m4) : null);
  final __m5 = __m['shape'];
  final ShapeBorder? shape = (__m5 != null ? uClass<ShapeBorder>(__m5) : null);
  final __m6 = __m['clipBehavior'];
  final Clip? clipBehavior = (__m6 != null ? _uClip(__m6) : null);
  final __m7 = __m['constraints'];
  final BoxConstraints? constraints = (__m7 != null ? uClass<BoxConstraints>(__m7) : null);
  return BottomSheetThemeData(
    backgroundColor: backgroundColor,
    elevation: elevation,
    modalBackgroundColor: modalBackgroundColor,
    modalElevation: modalElevation,
    shape: shape,
    clipBehavior: clipBehavior,
    constraints: constraints,
  );
}

PopupMenuThemeData _uPopupMenuThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['color'];
  final Color? color = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['shape'];
  final ShapeBorder? shape = (__m2 != null ? uClass<ShapeBorder>(__m2) : null);
  final __m3 = __m['elevation'];
  final double? elevation = (__m3 != null ? uDouble(__m3) : null);
  final __m4 = __m['textStyle'];
  final TextStyle? textStyle = (__m4 != null ? uClass<TextStyle>(__m4) : null);
  final __m5 = __m['enableFeedback'];
  final bool? enableFeedback = (__m5 != null ? uBool(__m5) : null);
  return PopupMenuThemeData(
    color: color,
    shape: shape,
    elevation: elevation,
    textStyle: textStyle,
    enableFeedback: enableFeedback,
  );
}

MaterialBannerThemeData _uMaterialBannerThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['backgroundColor'];
  final Color? backgroundColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['contentTextStyle'];
  final TextStyle? contentTextStyle = (__m2 != null ? uClass<TextStyle>(__m2) : null);
  final __m3 = __m['padding'];
  final EdgeInsetsGeometry? padding = (__m3 != null ? uClass<EdgeInsetsGeometry>(__m3) : null);
  final __m4 = __m['leadingPadding'];
  final EdgeInsetsGeometry? leadingPadding = (__m4 != null ? uClass<EdgeInsetsGeometry>(__m4) : null);
  return MaterialBannerThemeData(
    backgroundColor: backgroundColor,
    contentTextStyle: contentTextStyle,
    padding: padding,
    leadingPadding: leadingPadding,
  );
}

DividerThemeData _uDividerThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['color'];
  final Color? color = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['space'];
  final double? space = (__m2 != null ? uDouble(__m2) : null);
  final __m3 = __m['thickness'];
  final double? thickness = (__m3 != null ? uDouble(__m3) : null);
  final __m4 = __m['indent'];
  final double? indent = (__m4 != null ? uDouble(__m4) : null);
  final __m5 = __m['endIndent'];
  final double? endIndent = (__m5 != null ? uDouble(__m5) : null);
  return DividerThemeData(
    color: color,
    space: space,
    thickness: thickness,
    indent: indent,
    endIndent: endIndent,
  );
}

MainAxisAlignment _uMainAxisAlignment(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'start':
        return MainAxisAlignment.start;
      case 'end':
        return MainAxisAlignment.end;
      case 'center':
        return MainAxisAlignment.center;
      case 'spaceBetween':
        return MainAxisAlignment.spaceBetween;
      case 'spaceAround':
        return MainAxisAlignment.spaceAround;
      case 'spaceEvenly':
        return MainAxisAlignment.spaceEvenly;
    }
  }
  throw 'illegal enum value $v';
}

MainAxisSize _uMainAxisSize(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'min':
        return MainAxisSize.min;
      case 'max':
        return MainAxisSize.max;
    }
  }
  throw 'illegal enum value $v';
}

VerticalDirection _uVerticalDirection(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'up':
        return VerticalDirection.up;
      case 'down':
        return VerticalDirection.down;
    }
  }
  throw 'illegal enum value $v';
}

ButtonBarThemeData _uButtonBarThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['alignment'];
  final MainAxisAlignment? alignment = (__m1 != null ? _uMainAxisAlignment(__m1) : null);
  final __m2 = __m['mainAxisSize'];
  final MainAxisSize? mainAxisSize = (__m2 != null ? _uMainAxisSize(__m2) : null);
  final __m3 = __m['buttonTextTheme'];
  final ButtonTextTheme? buttonTextTheme = (__m3 != null ? _uButtonTextTheme(__m3) : null);
  final __m4 = __m['buttonMinWidth'];
  final double? buttonMinWidth = (__m4 != null ? uDouble(__m4) : null);
  final __m5 = __m['buttonHeight'];
  final double? buttonHeight = (__m5 != null ? uDouble(__m5) : null);
  final __m6 = __m['buttonPadding'];
  final EdgeInsetsGeometry? buttonPadding = (__m6 != null ? uClass<EdgeInsetsGeometry>(__m6) : null);
  final __m7 = __m['buttonAlignedDropdown'];
  final bool? buttonAlignedDropdown = (__m7 != null ? uBool(__m7) : null);
  final __m8 = __m['layoutBehavior'];
  final ButtonBarLayoutBehavior? layoutBehavior = (__m8 != null ? _uButtonBarLayoutBehavior(__m8) : null);
  final __m9 = __m['overflowDirection'];
  final VerticalDirection? overflowDirection = (__m9 != null ? _uVerticalDirection(__m9) : null);
  return ButtonBarThemeData(
    alignment: alignment,
    mainAxisSize: mainAxisSize,
    buttonTextTheme: buttonTextTheme,
    buttonMinWidth: buttonMinWidth,
    buttonHeight: buttonHeight,
    buttonPadding: buttonPadding,
    buttonAlignedDropdown: buttonAlignedDropdown,
    layoutBehavior: layoutBehavior,
    overflowDirection: overflowDirection,
  );
}

BottomNavigationBarType _uBottomNavigationBarType(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'fixed':
        return BottomNavigationBarType.fixed;
      case 'shifting':
        return BottomNavigationBarType.shifting;
    }
  }
  throw 'illegal enum value $v';
}

BottomNavigationBarLandscapeLayout _uBottomNavigationBarLandscapeLayout(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'spread':
        return BottomNavigationBarLandscapeLayout.spread;
      case 'centered':
        return BottomNavigationBarLandscapeLayout.centered;
      case 'linear':
        return BottomNavigationBarLandscapeLayout.linear;
    }
  }
  throw 'illegal enum value $v';
}

BottomNavigationBarThemeData _uBottomNavigationBarThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['backgroundColor'];
  final Color? backgroundColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['elevation'];
  final double? elevation = (__m2 != null ? uDouble(__m2) : null);
  final __m3 = __m['selectedIconTheme'];
  final IconThemeData? selectedIconTheme = (__m3 != null ? uClass<IconThemeData>(__m3) : null);
  final __m4 = __m['unselectedIconTheme'];
  final IconThemeData? unselectedIconTheme = (__m4 != null ? uClass<IconThemeData>(__m4) : null);
  final __m5 = __m['selectedItemColor'];
  final Color? selectedItemColor = (__m5 != null ? uClass<Color>(__m5) : null);
  final __m6 = __m['unselectedItemColor'];
  final Color? unselectedItemColor = (__m6 != null ? uClass<Color>(__m6) : null);
  final __m7 = __m['selectedLabelStyle'];
  final TextStyle? selectedLabelStyle = (__m7 != null ? uClass<TextStyle>(__m7) : null);
  final __m8 = __m['unselectedLabelStyle'];
  final TextStyle? unselectedLabelStyle = (__m8 != null ? uClass<TextStyle>(__m8) : null);
  final __m9 = __m['showSelectedLabels'];
  final bool? showSelectedLabels = (__m9 != null ? uBool(__m9) : null);
  final __m10 = __m['showUnselectedLabels'];
  final bool? showUnselectedLabels = (__m10 != null ? uBool(__m10) : null);
  final __m11 = __m['type'];
  final BottomNavigationBarType? type = (__m11 != null ? _uBottomNavigationBarType(__m11) : null);
  final __m12 = __m['enableFeedback'];
  final bool? enableFeedback = (__m12 != null ? uBool(__m12) : null);
  final __m13 = __m['landscapeLayout'];
  final BottomNavigationBarLandscapeLayout? landscapeLayout = (__m13 != null ? _uBottomNavigationBarLandscapeLayout(__m13) : null);
  return BottomNavigationBarThemeData(
    backgroundColor: backgroundColor,
    elevation: elevation,
    selectedIconTheme: selectedIconTheme,
    unselectedIconTheme: unselectedIconTheme,
    selectedItemColor: selectedItemColor,
    unselectedItemColor: unselectedItemColor,
    selectedLabelStyle: selectedLabelStyle,
    unselectedLabelStyle: unselectedLabelStyle,
    showSelectedLabels: showSelectedLabels,
    showUnselectedLabels: showUnselectedLabels,
    type: type,
    enableFeedback: enableFeedback,
    landscapeLayout: landscapeLayout,
  );
}

TimePickerThemeData _uTimePickerThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['backgroundColor'];
  final Color? backgroundColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['hourMinuteTextColor'];
  final Color? hourMinuteTextColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['hourMinuteColor'];
  final Color? hourMinuteColor = (__m3 != null ? uClass<Color>(__m3) : null);
  final __m4 = __m['dayPeriodTextColor'];
  final Color? dayPeriodTextColor = (__m4 != null ? uClass<Color>(__m4) : null);
  final __m5 = __m['dayPeriodColor'];
  final Color? dayPeriodColor = (__m5 != null ? uClass<Color>(__m5) : null);
  final __m6 = __m['dialHandColor'];
  final Color? dialHandColor = (__m6 != null ? uClass<Color>(__m6) : null);
  final __m7 = __m['dialBackgroundColor'];
  final Color? dialBackgroundColor = (__m7 != null ? uClass<Color>(__m7) : null);
  final __m8 = __m['dialTextColor'];
  final Color? dialTextColor = (__m8 != null ? uClass<Color>(__m8) : null);
  final __m9 = __m['entryModeIconColor'];
  final Color? entryModeIconColor = (__m9 != null ? uClass<Color>(__m9) : null);
  final __m10 = __m['hourMinuteTextStyle'];
  final TextStyle? hourMinuteTextStyle = (__m10 != null ? uClass<TextStyle>(__m10) : null);
  final __m11 = __m['dayPeriodTextStyle'];
  final TextStyle? dayPeriodTextStyle = (__m11 != null ? uClass<TextStyle>(__m11) : null);
  final __m12 = __m['helpTextStyle'];
  final TextStyle? helpTextStyle = (__m12 != null ? uClass<TextStyle>(__m12) : null);
  final __m13 = __m['shape'];
  final ShapeBorder? shape = (__m13 != null ? uClass<ShapeBorder>(__m13) : null);
  final __m14 = __m['hourMinuteShape'];
  final ShapeBorder? hourMinuteShape = (__m14 != null ? uClass<ShapeBorder>(__m14) : null);
  final __m15 = __m['dayPeriodShape'];
  final OutlinedBorder? dayPeriodShape = (__m15 != null ? uClass<OutlinedBorder>(__m15) : null);
  final __m16 = __m['dayPeriodBorderSide'];
  final BorderSide? dayPeriodBorderSide = (__m16 != null ? uClass<BorderSide>(__m16) : null);
  final __m17 = __m['inputDecorationTheme'];
  final InputDecorationTheme? inputDecorationTheme = (__m17 != null ? uClass<InputDecorationTheme>(__m17) : null);
  return TimePickerThemeData(
    backgroundColor: backgroundColor,
    hourMinuteTextColor: hourMinuteTextColor,
    hourMinuteColor: hourMinuteColor,
    dayPeriodTextColor: dayPeriodTextColor,
    dayPeriodColor: dayPeriodColor,
    dialHandColor: dialHandColor,
    dialBackgroundColor: dialBackgroundColor,
    dialTextColor: dialTextColor,
    entryModeIconColor: entryModeIconColor,
    hourMinuteTextStyle: hourMinuteTextStyle,
    dayPeriodTextStyle: dayPeriodTextStyle,
    helpTextStyle: helpTextStyle,
    shape: shape,
    hourMinuteShape: hourMinuteShape,
    dayPeriodShape: dayPeriodShape,
    dayPeriodBorderSide: dayPeriodBorderSide,
    inputDecorationTheme: inputDecorationTheme,
  );
}

ButtonStyle _uButtonStyle(Map<String, dynamic> __m) {
  final __m1 = __m['textStyle'];
  final MaterialStateProperty<TextStyle?>? textStyle = (__m1 != null ? uClass<MaterialStateProperty<TextStyle?>>(__m1) : null);
  final __m2 = __m['backgroundColor'];
  final MaterialStateProperty<Color?>? backgroundColor = (__m2 != null ? uClass<MaterialStateProperty<Color?>>(__m2) : null);
  final __m3 = __m['foregroundColor'];
  final MaterialStateProperty<Color?>? foregroundColor = (__m3 != null ? uClass<MaterialStateProperty<Color?>>(__m3) : null);
  final __m4 = __m['overlayColor'];
  final MaterialStateProperty<Color?>? overlayColor = (__m4 != null ? uClass<MaterialStateProperty<Color?>>(__m4) : null);
  final __m5 = __m['shadowColor'];
  final MaterialStateProperty<Color?>? shadowColor = (__m5 != null ? uClass<MaterialStateProperty<Color?>>(__m5) : null);
  final __m6 = __m['elevation'];
  final MaterialStateProperty<double?>? elevation = (__m6 != null ? uClass<MaterialStateProperty<double?>>(__m6) : null);
  final __m7 = __m['padding'];
  final MaterialStateProperty<EdgeInsetsGeometry?>? padding = (__m7 != null ? uClass<MaterialStateProperty<EdgeInsetsGeometry?>>(__m7) : null);
  final __m8 = __m['minimumSize'];
  final MaterialStateProperty<Size?>? minimumSize = (__m8 != null ? uClass<MaterialStateProperty<Size?>>(__m8) : null);
  final __m9 = __m['fixedSize'];
  final MaterialStateProperty<Size?>? fixedSize = (__m9 != null ? uClass<MaterialStateProperty<Size?>>(__m9) : null);
  final __m10 = __m['maximumSize'];
  final MaterialStateProperty<Size?>? maximumSize = (__m10 != null ? uClass<MaterialStateProperty<Size?>>(__m10) : null);
  final __m11 = __m['side'];
  final MaterialStateProperty<BorderSide?>? side = (__m11 != null ? uClass<MaterialStateProperty<BorderSide?>>(__m11) : null);
  final __m12 = __m['shape'];
  final MaterialStateProperty<OutlinedBorder?>? shape = (__m12 != null ? uClass<MaterialStateProperty<OutlinedBorder?>>(__m12) : null);
  final __m13 = __m['mouseCursor'];
  final MaterialStateProperty<MouseCursor?>? mouseCursor = (__m13 != null ? uClass<MaterialStateProperty<MouseCursor?>>(__m13) : null);
  final __m14 = __m['visualDensity'];
  final VisualDensity? visualDensity = (__m14 != null ? uClass<VisualDensity>(__m14) : null);
  final __m15 = __m['tapTargetSize'];
  final MaterialTapTargetSize? tapTargetSize = (__m15 != null ? _uMaterialTapTargetSize(__m15) : null);
  final __m16 = __m['animationDuration'];
  final Duration? animationDuration = (__m16 != null ? uClass<Duration>(__m16) : null);
  final __m17 = __m['enableFeedback'];
  final bool? enableFeedback = (__m17 != null ? uBool(__m17) : null);
  final __m18 = __m['alignment'];
  final AlignmentGeometry? alignment = (__m18 != null ? uClass<AlignmentGeometry>(__m18) : null);
  final __m19 = __m['splashFactory'];
  final InteractiveInkFeatureFactory? splashFactory = (__m19 != null ? uClass<InteractiveInkFeatureFactory>(__m19) : null);
  return ButtonStyle(
    textStyle: textStyle,
    backgroundColor: backgroundColor,
    foregroundColor: foregroundColor,
    overlayColor: overlayColor,
    shadowColor: shadowColor,
    elevation: elevation,
    padding: padding,
    minimumSize: minimumSize,
    fixedSize: fixedSize,
    maximumSize: maximumSize,
    side: side,
    shape: shape,
    mouseCursor: mouseCursor,
    visualDensity: visualDensity,
    tapTargetSize: tapTargetSize,
    animationDuration: animationDuration,
    enableFeedback: enableFeedback,
    alignment: alignment,
    splashFactory: splashFactory,
  );
}

TextButtonThemeData _uTextButtonThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['style'];
  final ButtonStyle? style = (__m1 != null ? uClass<ButtonStyle>(__m1) : null);
  return TextButtonThemeData(
    style: style,
  );
}

ElevatedButtonThemeData _uElevatedButtonThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['style'];
  final ButtonStyle? style = (__m1 != null ? uClass<ButtonStyle>(__m1) : null);
  return ElevatedButtonThemeData(
    style: style,
  );
}

OutlinedButtonThemeData _uOutlinedButtonThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['style'];
  final ButtonStyle? style = (__m1 != null ? uClass<ButtonStyle>(__m1) : null);
  return OutlinedButtonThemeData(
    style: style,
  );
}

TextSelectionThemeData _uTextSelectionThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['cursorColor'];
  final Color? cursorColor = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['selectionColor'];
  final Color? selectionColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['selectionHandleColor'];
  final Color? selectionHandleColor = (__m3 != null ? uClass<Color>(__m3) : null);
  return TextSelectionThemeData(
    cursorColor: cursorColor,
    selectionColor: selectionColor,
    selectionHandleColor: selectionHandleColor,
  );
}

DataTableThemeData _uDataTableThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['decoration'];
  final Decoration? decoration = (__m1 != null ? uClass<Decoration>(__m1) : null);
  final __m2 = __m['dataRowColor'];
  final MaterialStateProperty<Color?>? dataRowColor = (__m2 != null ? uClass<MaterialStateProperty<Color?>>(__m2) : null);
  final __m3 = __m['dataRowHeight'];
  final double? dataRowHeight = (__m3 != null ? uDouble(__m3) : null);
  final __m4 = __m['dataTextStyle'];
  final TextStyle? dataTextStyle = (__m4 != null ? uClass<TextStyle>(__m4) : null);
  final __m5 = __m['headingRowColor'];
  final MaterialStateProperty<Color?>? headingRowColor = (__m5 != null ? uClass<MaterialStateProperty<Color?>>(__m5) : null);
  final __m6 = __m['headingRowHeight'];
  final double? headingRowHeight = (__m6 != null ? uDouble(__m6) : null);
  final __m7 = __m['headingTextStyle'];
  final TextStyle? headingTextStyle = (__m7 != null ? uClass<TextStyle>(__m7) : null);
  final __m8 = __m['horizontalMargin'];
  final double? horizontalMargin = (__m8 != null ? uDouble(__m8) : null);
  final __m9 = __m['columnSpacing'];
  final double? columnSpacing = (__m9 != null ? uDouble(__m9) : null);
  final __m10 = __m['dividerThickness'];
  final double? dividerThickness = (__m10 != null ? uDouble(__m10) : null);
  final __m11 = __m['checkboxHorizontalMargin'];
  final double? checkboxHorizontalMargin = (__m11 != null ? uDouble(__m11) : null);
  return DataTableThemeData(
    decoration: decoration,
    dataRowColor: dataRowColor,
    dataRowHeight: dataRowHeight,
    dataTextStyle: dataTextStyle,
    headingRowColor: headingRowColor,
    headingRowHeight: headingRowHeight,
    headingTextStyle: headingTextStyle,
    horizontalMargin: horizontalMargin,
    columnSpacing: columnSpacing,
    dividerThickness: dividerThickness,
    checkboxHorizontalMargin: checkboxHorizontalMargin,
  );
}

CheckboxThemeData _uCheckboxThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['mouseCursor'];
  final MaterialStateProperty<MouseCursor?>? mouseCursor = (__m1 != null ? uClass<MaterialStateProperty<MouseCursor?>>(__m1) : null);
  final __m2 = __m['fillColor'];
  final MaterialStateProperty<Color?>? fillColor = (__m2 != null ? uClass<MaterialStateProperty<Color?>>(__m2) : null);
  final __m3 = __m['checkColor'];
  final MaterialStateProperty<Color?>? checkColor = (__m3 != null ? uClass<MaterialStateProperty<Color?>>(__m3) : null);
  final __m4 = __m['overlayColor'];
  final MaterialStateProperty<Color?>? overlayColor = (__m4 != null ? uClass<MaterialStateProperty<Color?>>(__m4) : null);
  final __m5 = __m['splashRadius'];
  final double? splashRadius = (__m5 != null ? uDouble(__m5) : null);
  final __m6 = __m['materialTapTargetSize'];
  final MaterialTapTargetSize? materialTapTargetSize = (__m6 != null ? _uMaterialTapTargetSize(__m6) : null);
  final __m7 = __m['visualDensity'];
  final VisualDensity? visualDensity = (__m7 != null ? uClass<VisualDensity>(__m7) : null);
  final __m8 = __m['shape'];
  final OutlinedBorder? shape = (__m8 != null ? uClass<OutlinedBorder>(__m8) : null);
  final __m9 = __m['side'];
  final BorderSide? side = (__m9 != null ? uClass<BorderSide>(__m9) : null);
  return CheckboxThemeData(
    mouseCursor: mouseCursor,
    fillColor: fillColor,
    checkColor: checkColor,
    overlayColor: overlayColor,
    splashRadius: splashRadius,
    materialTapTargetSize: materialTapTargetSize,
    visualDensity: visualDensity,
    shape: shape,
    side: side,
  );
}

RadioThemeData _uRadioThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['mouseCursor'];
  final MaterialStateProperty<MouseCursor?>? mouseCursor = (__m1 != null ? uClass<MaterialStateProperty<MouseCursor?>>(__m1) : null);
  final __m2 = __m['fillColor'];
  final MaterialStateProperty<Color?>? fillColor = (__m2 != null ? uClass<MaterialStateProperty<Color?>>(__m2) : null);
  final __m3 = __m['overlayColor'];
  final MaterialStateProperty<Color?>? overlayColor = (__m3 != null ? uClass<MaterialStateProperty<Color?>>(__m3) : null);
  final __m4 = __m['splashRadius'];
  final double? splashRadius = (__m4 != null ? uDouble(__m4) : null);
  final __m5 = __m['materialTapTargetSize'];
  final MaterialTapTargetSize? materialTapTargetSize = (__m5 != null ? _uMaterialTapTargetSize(__m5) : null);
  final __m6 = __m['visualDensity'];
  final VisualDensity? visualDensity = (__m6 != null ? uClass<VisualDensity>(__m6) : null);
  return RadioThemeData(
    mouseCursor: mouseCursor,
    fillColor: fillColor,
    overlayColor: overlayColor,
    splashRadius: splashRadius,
    materialTapTargetSize: materialTapTargetSize,
    visualDensity: visualDensity,
  );
}

SwitchThemeData _uSwitchThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['thumbColor'];
  final MaterialStateProperty<Color?>? thumbColor = (__m1 != null ? uClass<MaterialStateProperty<Color?>>(__m1) : null);
  final __m2 = __m['trackColor'];
  final MaterialStateProperty<Color?>? trackColor = (__m2 != null ? uClass<MaterialStateProperty<Color?>>(__m2) : null);
  final __m3 = __m['materialTapTargetSize'];
  final MaterialTapTargetSize? materialTapTargetSize = (__m3 != null ? _uMaterialTapTargetSize(__m3) : null);
  final __m4 = __m['mouseCursor'];
  final MaterialStateProperty<MouseCursor?>? mouseCursor = (__m4 != null ? uClass<MaterialStateProperty<MouseCursor?>>(__m4) : null);
  final __m5 = __m['overlayColor'];
  final MaterialStateProperty<Color?>? overlayColor = (__m5 != null ? uClass<MaterialStateProperty<Color?>>(__m5) : null);
  final __m6 = __m['splashRadius'];
  final double? splashRadius = (__m6 != null ? uDouble(__m6) : null);
  return SwitchThemeData(
    thumbColor: thumbColor,
    trackColor: trackColor,
    materialTapTargetSize: materialTapTargetSize,
    mouseCursor: mouseCursor,
    overlayColor: overlayColor,
    splashRadius: splashRadius,
  );
}

ProgressIndicatorThemeData _uProgressIndicatorThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['color'];
  final Color? color = (__m1 != null ? uClass<Color>(__m1) : null);
  final __m2 = __m['linearTrackColor'];
  final Color? linearTrackColor = (__m2 != null ? uClass<Color>(__m2) : null);
  final __m3 = __m['linearMinHeight'];
  final double? linearMinHeight = (__m3 != null ? uDouble(__m3) : null);
  final __m4 = __m['circularTrackColor'];
  final Color? circularTrackColor = (__m4 != null ? uClass<Color>(__m4) : null);
  final __m5 = __m['refreshBackgroundColor'];
  final Color? refreshBackgroundColor = (__m5 != null ? uClass<Color>(__m5) : null);
  return ProgressIndicatorThemeData(
    color: color,
    linearTrackColor: linearTrackColor,
    linearMinHeight: linearMinHeight,
    circularTrackColor: circularTrackColor,
    refreshBackgroundColor: refreshBackgroundColor,
  );
}

ThemeData _uThemeData(Map<String, dynamic> __m) {
  final __m1 = __m['brightness'];
  final Brightness? brightness = (__m1 != null ? _uBrightness(__m1) : null);
  final __m2 = __m['visualDensity'];
  final VisualDensity? visualDensity = (__m2 != null ? uClass<VisualDensity>(__m2) : null);
  final __m3 = __m['primarySwatch'];
  final MaterialColor? primarySwatch = (__m3 != null ? uClass<MaterialColor>(__m3) : null);
  final __m4 = __m['primaryColor'];
  final Color? primaryColor = (__m4 != null ? uClass<Color>(__m4) : null);
  final __m5 = __m['primaryColorBrightness'];
  final Brightness? primaryColorBrightness = (__m5 != null ? _uBrightness(__m5) : null);
  final __m6 = __m['primaryColorLight'];
  final Color? primaryColorLight = (__m6 != null ? uClass<Color>(__m6) : null);
  final __m7 = __m['primaryColorDark'];
  final Color? primaryColorDark = (__m7 != null ? uClass<Color>(__m7) : null);
  final __m8 = __m['accentColor'];
  final Color? accentColor = (__m8 != null ? uClass<Color>(__m8) : null);
  final __m9 = __m['accentColorBrightness'];
  final Brightness? accentColorBrightness = (__m9 != null ? _uBrightness(__m9) : null);
  final __m10 = __m['canvasColor'];
  final Color? canvasColor = (__m10 != null ? uClass<Color>(__m10) : null);
  final __m11 = __m['shadowColor'];
  final Color? shadowColor = (__m11 != null ? uClass<Color>(__m11) : null);
  final __m12 = __m['scaffoldBackgroundColor'];
  final Color? scaffoldBackgroundColor = (__m12 != null ? uClass<Color>(__m12) : null);
  final __m13 = __m['bottomAppBarColor'];
  final Color? bottomAppBarColor = (__m13 != null ? uClass<Color>(__m13) : null);
  final __m14 = __m['cardColor'];
  final Color? cardColor = (__m14 != null ? uClass<Color>(__m14) : null);
  final __m15 = __m['dividerColor'];
  final Color? dividerColor = (__m15 != null ? uClass<Color>(__m15) : null);
  final __m16 = __m['focusColor'];
  final Color? focusColor = (__m16 != null ? uClass<Color>(__m16) : null);
  final __m17 = __m['hoverColor'];
  final Color? hoverColor = (__m17 != null ? uClass<Color>(__m17) : null);
  final __m18 = __m['highlightColor'];
  final Color? highlightColor = (__m18 != null ? uClass<Color>(__m18) : null);
  final __m19 = __m['splashColor'];
  final Color? splashColor = (__m19 != null ? uClass<Color>(__m19) : null);
  final __m20 = __m['splashFactory'];
  final InteractiveInkFeatureFactory? splashFactory = (__m20 != null ? uClass<InteractiveInkFeatureFactory>(__m20) : null);
  final __m21 = __m['selectedRowColor'];
  final Color? selectedRowColor = (__m21 != null ? uClass<Color>(__m21) : null);
  final __m22 = __m['unselectedWidgetColor'];
  final Color? unselectedWidgetColor = (__m22 != null ? uClass<Color>(__m22) : null);
  final __m23 = __m['disabledColor'];
  final Color? disabledColor = (__m23 != null ? uClass<Color>(__m23) : null);
  final __m24 = __m['buttonColor'];
  final Color? buttonColor = (__m24 != null ? uClass<Color>(__m24) : null);
  final __m25 = __m['buttonTheme'];
  final ButtonThemeData? buttonTheme = (__m25 != null ? uClass<ButtonThemeData>(__m25) : null);
  final __m26 = __m['toggleButtonsTheme'];
  final ToggleButtonsThemeData? toggleButtonsTheme = (__m26 != null ? uClass<ToggleButtonsThemeData>(__m26) : null);
  final __m27 = __m['secondaryHeaderColor'];
  final Color? secondaryHeaderColor = (__m27 != null ? uClass<Color>(__m27) : null);
  final __m28 = __m['textSelectionColor'];
  final Color? textSelectionColor = (__m28 != null ? uClass<Color>(__m28) : null);
  final __m29 = __m['cursorColor'];
  final Color? cursorColor = (__m29 != null ? uClass<Color>(__m29) : null);
  final __m30 = __m['textSelectionHandleColor'];
  final Color? textSelectionHandleColor = (__m30 != null ? uClass<Color>(__m30) : null);
  final __m31 = __m['backgroundColor'];
  final Color? backgroundColor = (__m31 != null ? uClass<Color>(__m31) : null);
  final __m32 = __m['dialogBackgroundColor'];
  final Color? dialogBackgroundColor = (__m32 != null ? uClass<Color>(__m32) : null);
  final __m33 = __m['indicatorColor'];
  final Color? indicatorColor = (__m33 != null ? uClass<Color>(__m33) : null);
  final __m34 = __m['hintColor'];
  final Color? hintColor = (__m34 != null ? uClass<Color>(__m34) : null);
  final __m35 = __m['errorColor'];
  final Color? errorColor = (__m35 != null ? uClass<Color>(__m35) : null);
  final __m36 = __m['toggleableActiveColor'];
  final Color? toggleableActiveColor = (__m36 != null ? uClass<Color>(__m36) : null);
  final __m37 = __m['fontFamily'];
  final String? fontFamily = (__m37 != null ? uString(__m37) : null);
  final __m38 = __m['textTheme'];
  final TextTheme? textTheme = (__m38 != null ? uClass<TextTheme>(__m38) : null);
  final __m39 = __m['primaryTextTheme'];
  final TextTheme? primaryTextTheme = (__m39 != null ? uClass<TextTheme>(__m39) : null);
  final __m40 = __m['accentTextTheme'];
  final TextTheme? accentTextTheme = (__m40 != null ? uClass<TextTheme>(__m40) : null);
  final __m41 = __m['inputDecorationTheme'];
  final InputDecorationTheme? inputDecorationTheme = (__m41 != null ? uClass<InputDecorationTheme>(__m41) : null);
  final __m42 = __m['iconTheme'];
  final IconThemeData? iconTheme = (__m42 != null ? uClass<IconThemeData>(__m42) : null);
  final __m43 = __m['primaryIconTheme'];
  final IconThemeData? primaryIconTheme = (__m43 != null ? uClass<IconThemeData>(__m43) : null);
  final __m44 = __m['accentIconTheme'];
  final IconThemeData? accentIconTheme = (__m44 != null ? uClass<IconThemeData>(__m44) : null);
  final __m45 = __m['sliderTheme'];
  final SliderThemeData? sliderTheme = (__m45 != null ? uClass<SliderThemeData>(__m45) : null);
  final __m46 = __m['tabBarTheme'];
  final TabBarTheme? tabBarTheme = (__m46 != null ? uClass<TabBarTheme>(__m46) : null);
  final __m47 = __m['tooltipTheme'];
  final TooltipThemeData? tooltipTheme = (__m47 != null ? uClass<TooltipThemeData>(__m47) : null);
  final __m48 = __m['cardTheme'];
  final CardTheme? cardTheme = (__m48 != null ? uClass<CardTheme>(__m48) : null);
  final __m49 = __m['chipTheme'];
  final ChipThemeData? chipTheme = (__m49 != null ? uClass<ChipThemeData>(__m49) : null);
  final __m50 = __m['platform'];
  final TargetPlatform? platform = (__m50 != null ? _uTargetPlatform(__m50) : null);
  final __m51 = __m['materialTapTargetSize'];
  final MaterialTapTargetSize? materialTapTargetSize = (__m51 != null ? _uMaterialTapTargetSize(__m51) : null);
  final __m52 = __m['applyElevationOverlayColor'];
  final bool? applyElevationOverlayColor = (__m52 != null ? uBool(__m52) : null);
  final __m53 = __m['pageTransitionsTheme'];
  final PageTransitionsTheme? pageTransitionsTheme = (__m53 != null ? uClass<PageTransitionsTheme>(__m53) : null);
  final __m54 = __m['appBarTheme'];
  final AppBarTheme? appBarTheme = (__m54 != null ? uClass<AppBarTheme>(__m54) : null);
  final __m55 = __m['scrollbarTheme'];
  final ScrollbarThemeData? scrollbarTheme = (__m55 != null ? uClass<ScrollbarThemeData>(__m55) : null);
  final __m56 = __m['bottomAppBarTheme'];
  final BottomAppBarTheme? bottomAppBarTheme = (__m56 != null ? uClass<BottomAppBarTheme>(__m56) : null);
  final __m57 = __m['colorScheme'];
  final ColorScheme? colorScheme = (__m57 != null ? uClass<ColorScheme>(__m57) : null);
  final __m58 = __m['dialogTheme'];
  final DialogTheme? dialogTheme = (__m58 != null ? uClass<DialogTheme>(__m58) : null);
  final __m59 = __m['floatingActionButtonTheme'];
  final FloatingActionButtonThemeData? floatingActionButtonTheme = (__m59 != null ? uClass<FloatingActionButtonThemeData>(__m59) : null);
  final __m60 = __m['navigationRailTheme'];
  final NavigationRailThemeData? navigationRailTheme = (__m60 != null ? uClass<NavigationRailThemeData>(__m60) : null);
  final __m61 = __m['typography'];
  final Typography? typography = (__m61 != null ? uClass<Typography>(__m61) : null);
  final __m62 = __m['cupertinoOverrideTheme'];
  final NoDefaultCupertinoThemeData? cupertinoOverrideTheme = (__m62 != null ? uClass<NoDefaultCupertinoThemeData>(__m62) : null);
  final __m63 = __m['snackBarTheme'];
  final SnackBarThemeData? snackBarTheme = (__m63 != null ? uClass<SnackBarThemeData>(__m63) : null);
  final __m64 = __m['bottomSheetTheme'];
  final BottomSheetThemeData? bottomSheetTheme = (__m64 != null ? uClass<BottomSheetThemeData>(__m64) : null);
  final __m65 = __m['popupMenuTheme'];
  final PopupMenuThemeData? popupMenuTheme = (__m65 != null ? uClass<PopupMenuThemeData>(__m65) : null);
  final __m66 = __m['bannerTheme'];
  final MaterialBannerThemeData? bannerTheme = (__m66 != null ? uClass<MaterialBannerThemeData>(__m66) : null);
  final __m67 = __m['dividerTheme'];
  final DividerThemeData? dividerTheme = (__m67 != null ? uClass<DividerThemeData>(__m67) : null);
  final __m68 = __m['buttonBarTheme'];
  final ButtonBarThemeData? buttonBarTheme = (__m68 != null ? uClass<ButtonBarThemeData>(__m68) : null);
  final __m69 = __m['bottomNavigationBarTheme'];
  final BottomNavigationBarThemeData? bottomNavigationBarTheme = (__m69 != null ? uClass<BottomNavigationBarThemeData>(__m69) : null);
  final __m70 = __m['timePickerTheme'];
  final TimePickerThemeData? timePickerTheme = (__m70 != null ? uClass<TimePickerThemeData>(__m70) : null);
  final __m71 = __m['textButtonTheme'];
  final TextButtonThemeData? textButtonTheme = (__m71 != null ? uClass<TextButtonThemeData>(__m71) : null);
  final __m72 = __m['elevatedButtonTheme'];
  final ElevatedButtonThemeData? elevatedButtonTheme = (__m72 != null ? uClass<ElevatedButtonThemeData>(__m72) : null);
  final __m73 = __m['outlinedButtonTheme'];
  final OutlinedButtonThemeData? outlinedButtonTheme = (__m73 != null ? uClass<OutlinedButtonThemeData>(__m73) : null);
  final __m74 = __m['textSelectionTheme'];
  final TextSelectionThemeData? textSelectionTheme = (__m74 != null ? uClass<TextSelectionThemeData>(__m74) : null);
  final __m75 = __m['dataTableTheme'];
  final DataTableThemeData? dataTableTheme = (__m75 != null ? uClass<DataTableThemeData>(__m75) : null);
  final __m76 = __m['checkboxTheme'];
  final CheckboxThemeData? checkboxTheme = (__m76 != null ? uClass<CheckboxThemeData>(__m76) : null);
  final __m77 = __m['radioTheme'];
  final RadioThemeData? radioTheme = (__m77 != null ? uClass<RadioThemeData>(__m77) : null);
  final __m78 = __m['switchTheme'];
  final SwitchThemeData? switchTheme = (__m78 != null ? uClass<SwitchThemeData>(__m78) : null);
  final __m79 = __m['progressIndicatorTheme'];
  final ProgressIndicatorThemeData? progressIndicatorTheme = (__m79 != null ? uClass<ProgressIndicatorThemeData>(__m79) : null);
  final __m80 = __m['fixTextFieldOutlineLabel'];
  final bool? fixTextFieldOutlineLabel = (__m80 != null ? uBool(__m80) : null);
  final __m81 = __m['useTextSelectionTheme'];
  final bool? useTextSelectionTheme = (__m81 != null ? uBool(__m81) : null);
  return ThemeData(
    brightness: brightness,
    visualDensity: visualDensity,
    primarySwatch: primarySwatch,
    primaryColor: primaryColor,
    primaryColorBrightness: primaryColorBrightness,
    primaryColorLight: primaryColorLight,
    primaryColorDark: primaryColorDark,
    accentColor: accentColor,
    accentColorBrightness: accentColorBrightness,
    canvasColor: canvasColor,
    shadowColor: shadowColor,
    scaffoldBackgroundColor: scaffoldBackgroundColor,
    bottomAppBarColor: bottomAppBarColor,
    cardColor: cardColor,
    dividerColor: dividerColor,
    focusColor: focusColor,
    hoverColor: hoverColor,
    highlightColor: highlightColor,
    splashColor: splashColor,
    splashFactory: splashFactory,
    selectedRowColor: selectedRowColor,
    unselectedWidgetColor: unselectedWidgetColor,
    disabledColor: disabledColor,
    buttonColor: buttonColor,
    buttonTheme: buttonTheme,
    toggleButtonsTheme: toggleButtonsTheme,
    secondaryHeaderColor: secondaryHeaderColor,
    textSelectionColor: textSelectionColor,
    cursorColor: cursorColor,
    textSelectionHandleColor: textSelectionHandleColor,
    backgroundColor: backgroundColor,
    dialogBackgroundColor: dialogBackgroundColor,
    indicatorColor: indicatorColor,
    hintColor: hintColor,
    errorColor: errorColor,
    toggleableActiveColor: toggleableActiveColor,
    fontFamily: fontFamily,
    textTheme: textTheme,
    primaryTextTheme: primaryTextTheme,
    accentTextTheme: accentTextTheme,
    inputDecorationTheme: inputDecorationTheme,
    iconTheme: iconTheme,
    primaryIconTheme: primaryIconTheme,
    accentIconTheme: accentIconTheme,
    sliderTheme: sliderTheme,
    tabBarTheme: tabBarTheme,
    tooltipTheme: tooltipTheme,
    cardTheme: cardTheme,
    chipTheme: chipTheme,
    platform: platform,
    materialTapTargetSize: materialTapTargetSize,
    applyElevationOverlayColor: applyElevationOverlayColor,
    pageTransitionsTheme: pageTransitionsTheme,
    appBarTheme: appBarTheme,
    scrollbarTheme: scrollbarTheme,
    bottomAppBarTheme: bottomAppBarTheme,
    colorScheme: colorScheme,
    dialogTheme: dialogTheme,
    floatingActionButtonTheme: floatingActionButtonTheme,
    navigationRailTheme: navigationRailTheme,
    typography: typography,
    cupertinoOverrideTheme: cupertinoOverrideTheme,
    snackBarTheme: snackBarTheme,
    bottomSheetTheme: bottomSheetTheme,
    popupMenuTheme: popupMenuTheme,
    bannerTheme: bannerTheme,
    dividerTheme: dividerTheme,
    buttonBarTheme: buttonBarTheme,
    bottomNavigationBarTheme: bottomNavigationBarTheme,
    timePickerTheme: timePickerTheme,
    textButtonTheme: textButtonTheme,
    elevatedButtonTheme: elevatedButtonTheme,
    outlinedButtonTheme: outlinedButtonTheme,
    textSelectionTheme: textSelectionTheme,
    dataTableTheme: dataTableTheme,
    checkboxTheme: checkboxTheme,
    radioTheme: radioTheme,
    switchTheme: switchTheme,
    progressIndicatorTheme: progressIndicatorTheme,
    fixTextFieldOutlineLabel: fixTextFieldOutlineLabel,
    useTextSelectionTheme: useTextSelectionTheme,
  );
}

ThemeData _uThemeDataRaw(Map<String, dynamic> __m) {
  final __m1 = __m['visualDensity'];
  final VisualDensity visualDensity = uClass<VisualDensity>(__m1);
  final __m2 = __m['primaryColor'];
  final Color primaryColor = uClass<Color>(__m2);
  final __m3 = __m['primaryColorBrightness'];
  final Brightness primaryColorBrightness = _uBrightness(__m3);
  final __m4 = __m['primaryColorLight'];
  final Color primaryColorLight = uClass<Color>(__m4);
  final __m5 = __m['primaryColorDark'];
  final Color primaryColorDark = uClass<Color>(__m5);
  final __m6 = __m['canvasColor'];
  final Color canvasColor = uClass<Color>(__m6);
  final __m7 = __m['shadowColor'];
  final Color shadowColor = uClass<Color>(__m7);
  final __m8 = __m['accentColor'];
  final Color accentColor = uClass<Color>(__m8);
  final __m9 = __m['accentColorBrightness'];
  final Brightness accentColorBrightness = _uBrightness(__m9);
  final __m10 = __m['scaffoldBackgroundColor'];
  final Color scaffoldBackgroundColor = uClass<Color>(__m10);
  final __m11 = __m['bottomAppBarColor'];
  final Color bottomAppBarColor = uClass<Color>(__m11);
  final __m12 = __m['cardColor'];
  final Color cardColor = uClass<Color>(__m12);
  final __m13 = __m['dividerColor'];
  final Color dividerColor = uClass<Color>(__m13);
  final __m14 = __m['focusColor'];
  final Color focusColor = uClass<Color>(__m14);
  final __m15 = __m['hoverColor'];
  final Color hoverColor = uClass<Color>(__m15);
  final __m16 = __m['highlightColor'];
  final Color highlightColor = uClass<Color>(__m16);
  final __m17 = __m['splashColor'];
  final Color splashColor = uClass<Color>(__m17);
  final __m18 = __m['splashFactory'];
  final InteractiveInkFeatureFactory splashFactory = uClass<InteractiveInkFeatureFactory>(__m18);
  final __m19 = __m['selectedRowColor'];
  final Color selectedRowColor = uClass<Color>(__m19);
  final __m20 = __m['unselectedWidgetColor'];
  final Color unselectedWidgetColor = uClass<Color>(__m20);
  final __m21 = __m['disabledColor'];
  final Color disabledColor = uClass<Color>(__m21);
  final __m22 = __m['buttonTheme'];
  final ButtonThemeData buttonTheme = uClass<ButtonThemeData>(__m22);
  final __m23 = __m['buttonColor'];
  final Color buttonColor = uClass<Color>(__m23);
  final __m24 = __m['toggleButtonsTheme'];
  final ToggleButtonsThemeData toggleButtonsTheme = uClass<ToggleButtonsThemeData>(__m24);
  final __m25 = __m['secondaryHeaderColor'];
  final Color secondaryHeaderColor = uClass<Color>(__m25);
  final __m26 = __m['textSelectionColor'];
  final Color textSelectionColor = uClass<Color>(__m26);
  final __m27 = __m['cursorColor'];
  final Color cursorColor = uClass<Color>(__m27);
  final __m28 = __m['textSelectionHandleColor'];
  final Color textSelectionHandleColor = uClass<Color>(__m28);
  final __m29 = __m['backgroundColor'];
  final Color backgroundColor = uClass<Color>(__m29);
  final __m30 = __m['dialogBackgroundColor'];
  final Color dialogBackgroundColor = uClass<Color>(__m30);
  final __m31 = __m['indicatorColor'];
  final Color indicatorColor = uClass<Color>(__m31);
  final __m32 = __m['hintColor'];
  final Color hintColor = uClass<Color>(__m32);
  final __m33 = __m['errorColor'];
  final Color errorColor = uClass<Color>(__m33);
  final __m34 = __m['toggleableActiveColor'];
  final Color toggleableActiveColor = uClass<Color>(__m34);
  final __m35 = __m['textTheme'];
  final TextTheme textTheme = uClass<TextTheme>(__m35);
  final __m36 = __m['primaryTextTheme'];
  final TextTheme primaryTextTheme = uClass<TextTheme>(__m36);
  final __m37 = __m['accentTextTheme'];
  final TextTheme accentTextTheme = uClass<TextTheme>(__m37);
  final __m38 = __m['inputDecorationTheme'];
  final InputDecorationTheme inputDecorationTheme = uClass<InputDecorationTheme>(__m38);
  final __m39 = __m['iconTheme'];
  final IconThemeData iconTheme = uClass<IconThemeData>(__m39);
  final __m40 = __m['primaryIconTheme'];
  final IconThemeData primaryIconTheme = uClass<IconThemeData>(__m40);
  final __m41 = __m['accentIconTheme'];
  final IconThemeData accentIconTheme = uClass<IconThemeData>(__m41);
  final __m42 = __m['sliderTheme'];
  final SliderThemeData sliderTheme = uClass<SliderThemeData>(__m42);
  final __m43 = __m['tabBarTheme'];
  final TabBarTheme tabBarTheme = uClass<TabBarTheme>(__m43);
  final __m44 = __m['tooltipTheme'];
  final TooltipThemeData tooltipTheme = uClass<TooltipThemeData>(__m44);
  final __m45 = __m['cardTheme'];
  final CardTheme cardTheme = uClass<CardTheme>(__m45);
  final __m46 = __m['chipTheme'];
  final ChipThemeData chipTheme = uClass<ChipThemeData>(__m46);
  final __m47 = __m['platform'];
  final TargetPlatform platform = _uTargetPlatform(__m47);
  final __m48 = __m['materialTapTargetSize'];
  final MaterialTapTargetSize materialTapTargetSize = _uMaterialTapTargetSize(__m48);
  final __m49 = __m['applyElevationOverlayColor'];
  final bool applyElevationOverlayColor = uBool(__m49);
  final __m50 = __m['pageTransitionsTheme'];
  final PageTransitionsTheme pageTransitionsTheme = uClass<PageTransitionsTheme>(__m50);
  final __m51 = __m['appBarTheme'];
  final AppBarTheme appBarTheme = uClass<AppBarTheme>(__m51);
  final __m52 = __m['scrollbarTheme'];
  final ScrollbarThemeData scrollbarTheme = uClass<ScrollbarThemeData>(__m52);
  final __m53 = __m['bottomAppBarTheme'];
  final BottomAppBarTheme bottomAppBarTheme = uClass<BottomAppBarTheme>(__m53);
  final __m54 = __m['colorScheme'];
  final ColorScheme colorScheme = uClass<ColorScheme>(__m54);
  final __m55 = __m['dialogTheme'];
  final DialogTheme dialogTheme = uClass<DialogTheme>(__m55);
  final __m56 = __m['floatingActionButtonTheme'];
  final FloatingActionButtonThemeData floatingActionButtonTheme = uClass<FloatingActionButtonThemeData>(__m56);
  final __m57 = __m['navigationRailTheme'];
  final NavigationRailThemeData navigationRailTheme = uClass<NavigationRailThemeData>(__m57);
  final __m58 = __m['typography'];
  final Typography typography = uClass<Typography>(__m58);
  final __m59 = __m['cupertinoOverrideTheme'];
  final NoDefaultCupertinoThemeData? cupertinoOverrideTheme = (__m59 != null ? uClass<NoDefaultCupertinoThemeData>(__m59) : null);
  final __m60 = __m['snackBarTheme'];
  final SnackBarThemeData snackBarTheme = uClass<SnackBarThemeData>(__m60);
  final __m61 = __m['bottomSheetTheme'];
  final BottomSheetThemeData bottomSheetTheme = uClass<BottomSheetThemeData>(__m61);
  final __m62 = __m['popupMenuTheme'];
  final PopupMenuThemeData popupMenuTheme = uClass<PopupMenuThemeData>(__m62);
  final __m63 = __m['bannerTheme'];
  final MaterialBannerThemeData bannerTheme = uClass<MaterialBannerThemeData>(__m63);
  final __m64 = __m['dividerTheme'];
  final DividerThemeData dividerTheme = uClass<DividerThemeData>(__m64);
  final __m65 = __m['buttonBarTheme'];
  final ButtonBarThemeData buttonBarTheme = uClass<ButtonBarThemeData>(__m65);
  final __m66 = __m['bottomNavigationBarTheme'];
  final BottomNavigationBarThemeData bottomNavigationBarTheme = uClass<BottomNavigationBarThemeData>(__m66);
  final __m67 = __m['timePickerTheme'];
  final TimePickerThemeData timePickerTheme = uClass<TimePickerThemeData>(__m67);
  final __m68 = __m['textButtonTheme'];
  final TextButtonThemeData textButtonTheme = uClass<TextButtonThemeData>(__m68);
  final __m69 = __m['elevatedButtonTheme'];
  final ElevatedButtonThemeData elevatedButtonTheme = uClass<ElevatedButtonThemeData>(__m69);
  final __m70 = __m['outlinedButtonTheme'];
  final OutlinedButtonThemeData outlinedButtonTheme = uClass<OutlinedButtonThemeData>(__m70);
  final __m71 = __m['textSelectionTheme'];
  final TextSelectionThemeData textSelectionTheme = uClass<TextSelectionThemeData>(__m71);
  final __m72 = __m['dataTableTheme'];
  final DataTableThemeData dataTableTheme = uClass<DataTableThemeData>(__m72);
  final __m73 = __m['checkboxTheme'];
  final CheckboxThemeData checkboxTheme = uClass<CheckboxThemeData>(__m73);
  final __m74 = __m['radioTheme'];
  final RadioThemeData radioTheme = uClass<RadioThemeData>(__m74);
  final __m75 = __m['switchTheme'];
  final SwitchThemeData switchTheme = uClass<SwitchThemeData>(__m75);
  final __m76 = __m['progressIndicatorTheme'];
  final ProgressIndicatorThemeData progressIndicatorTheme = uClass<ProgressIndicatorThemeData>(__m76);
  final __m77 = __m['fixTextFieldOutlineLabel'];
  final bool fixTextFieldOutlineLabel = uBool(__m77);
  final __m78 = __m['useTextSelectionTheme'];
  final bool useTextSelectionTheme = uBool(__m78);
  return ThemeData.raw(
    visualDensity: visualDensity,
    primaryColor: primaryColor,
    primaryColorBrightness: primaryColorBrightness,
    primaryColorLight: primaryColorLight,
    primaryColorDark: primaryColorDark,
    canvasColor: canvasColor,
    shadowColor: shadowColor,
    accentColor: accentColor,
    accentColorBrightness: accentColorBrightness,
    scaffoldBackgroundColor: scaffoldBackgroundColor,
    bottomAppBarColor: bottomAppBarColor,
    cardColor: cardColor,
    dividerColor: dividerColor,
    focusColor: focusColor,
    hoverColor: hoverColor,
    highlightColor: highlightColor,
    splashColor: splashColor,
    splashFactory: splashFactory,
    selectedRowColor: selectedRowColor,
    unselectedWidgetColor: unselectedWidgetColor,
    disabledColor: disabledColor,
    buttonTheme: buttonTheme,
    buttonColor: buttonColor,
    toggleButtonsTheme: toggleButtonsTheme,
    secondaryHeaderColor: secondaryHeaderColor,
    textSelectionColor: textSelectionColor,
    cursorColor: cursorColor,
    textSelectionHandleColor: textSelectionHandleColor,
    backgroundColor: backgroundColor,
    dialogBackgroundColor: dialogBackgroundColor,
    indicatorColor: indicatorColor,
    hintColor: hintColor,
    errorColor: errorColor,
    toggleableActiveColor: toggleableActiveColor,
    textTheme: textTheme,
    primaryTextTheme: primaryTextTheme,
    accentTextTheme: accentTextTheme,
    inputDecorationTheme: inputDecorationTheme,
    iconTheme: iconTheme,
    primaryIconTheme: primaryIconTheme,
    accentIconTheme: accentIconTheme,
    sliderTheme: sliderTheme,
    tabBarTheme: tabBarTheme,
    tooltipTheme: tooltipTheme,
    cardTheme: cardTheme,
    chipTheme: chipTheme,
    platform: platform,
    materialTapTargetSize: materialTapTargetSize,
    applyElevationOverlayColor: applyElevationOverlayColor,
    pageTransitionsTheme: pageTransitionsTheme,
    appBarTheme: appBarTheme,
    scrollbarTheme: scrollbarTheme,
    bottomAppBarTheme: bottomAppBarTheme,
    colorScheme: colorScheme,
    dialogTheme: dialogTheme,
    floatingActionButtonTheme: floatingActionButtonTheme,
    navigationRailTheme: navigationRailTheme,
    typography: typography,
    cupertinoOverrideTheme: cupertinoOverrideTheme,
    snackBarTheme: snackBarTheme,
    bottomSheetTheme: bottomSheetTheme,
    popupMenuTheme: popupMenuTheme,
    bannerTheme: bannerTheme,
    dividerTheme: dividerTheme,
    buttonBarTheme: buttonBarTheme,
    bottomNavigationBarTheme: bottomNavigationBarTheme,
    timePickerTheme: timePickerTheme,
    textButtonTheme: textButtonTheme,
    elevatedButtonTheme: elevatedButtonTheme,
    outlinedButtonTheme: outlinedButtonTheme,
    textSelectionTheme: textSelectionTheme,
    dataTableTheme: dataTableTheme,
    checkboxTheme: checkboxTheme,
    radioTheme: radioTheme,
    switchTheme: switchTheme,
    progressIndicatorTheme: progressIndicatorTheme,
    fixTextFieldOutlineLabel: fixTextFieldOutlineLabel,
    useTextSelectionTheme: useTextSelectionTheme,
  );
}

ThemeData _uThemeDataFrom(Map<String, dynamic> __m) {
  final __m1 = __m['colorScheme'];
  final ColorScheme colorScheme = uClass<ColorScheme>(__m1);
  final __m2 = __m['textTheme'];
  final TextTheme? textTheme = (__m2 != null ? uClass<TextTheme>(__m2) : null);
  return ThemeData.from(
    colorScheme: colorScheme,
    textTheme: textTheme,
  );
}

ThemeData _uThemeDataLight(Map<String, dynamic> __m) {
  return ThemeData.light(
  );
}

ThemeData _uThemeDataDark(Map<String, dynamic> __m) {
  return ThemeData.dark(
  );
}

ThemeData _uThemeDataFallback(Map<String, dynamic> __m) {
  return ThemeData.fallback(
  );
}

ThemeMode _uThemeMode(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'system':
        return ThemeMode.system;
      case 'light':
        return ThemeMode.light;
      case 'dark':
        return ThemeMode.dark;
    }
  }
  throw 'illegal enum value $v';
}

DoNothingIntent _uDoNothingIntent(Map<String, dynamic> __m) {
  return DoNothingIntent(
  );
}

ScrollBehavior _uScrollBehavior(Map<String, dynamic> __m) {
  return const ScrollBehavior(
  );
}

RouteInformation _uRouteInformation(Map<String, dynamic> __m) {
  final __m1 = __m['location'];
  final String? location = (__m1 != null ? uString(__m1) : null);
  final __m2 = __m['state'];
  final Object? state = (__m2 != null ? uClass<Object>(__m2) : null);
  return RouteInformation(
    location: location,
    state: state,
  );
}

MaterialApp _uMaterialApp(Map<String, dynamic> __m) {
  final __m1 = __m['key'];
  final Key? key = (__m1 != null ? uClass<Key>(__m1) : null);
  final __m2 = __m['navigatorKey'];
  final GlobalKey<NavigatorState>? navigatorKey = (__m2 != null ? uClass<GlobalKey<NavigatorState>>(__m2) : null);
  final __m3 = __m['scaffoldMessengerKey'];
  final GlobalKey<ScaffoldMessengerState>? scaffoldMessengerKey = (__m3 != null ? uClass<GlobalKey<ScaffoldMessengerState>>(__m3) : null);
  final __m4 = __m['home'];
  final Widget? home = (__m4 != null ? uClass<Widget>(__m4) : null);
  final __m5 = __m['routes'];
  final Map<String, Widget Function(BuildContext)> routes = (__m5 != null ? (__m5 is Map<dynamic, dynamic> ? __m5.map((k, v) => MapEntry(uString(k), uFunc<Widget Function(BuildContext)>(v))) : die('not a map')) : <String, Widget Function(BuildContext)>{});
  final __m6 = __m['initialRoute'];
  final String? initialRoute = (__m6 != null ? uString(__m6) : null);
  final __m7 = __m['onGenerateRoute'];
  final Route<dynamic>? Function(RouteSettings)? onGenerateRoute = (__m7 != null ? uFunc<Route<dynamic>? Function(RouteSettings)>(__m7) : null);
  final __m8 = __m['onGenerateInitialRoutes'];
  final List<Route<dynamic>> Function(String)? onGenerateInitialRoutes = (__m8 != null ? uFunc<List<Route<dynamic>> Function(String)>(__m8) : null);
  final __m9 = __m['onUnknownRoute'];
  final Route<dynamic>? Function(RouteSettings)? onUnknownRoute = (__m9 != null ? uFunc<Route<dynamic>? Function(RouteSettings)>(__m9) : null);
  final __m10 = __m['navigatorObservers'];
  final List<NavigatorObserver> navigatorObservers = (__m10 != null ? (__m10 is List<dynamic> ? __m10.map((v) => uClass<NavigatorObserver>(v)).toList() : die('not a list')) : <NavigatorObserver>[]);
  final __m11 = __m['builder'];
  final Widget Function(BuildContext, Widget?)? builder = (__m11 != null ? uFunc<Widget Function(BuildContext, Widget?)>(__m11) : null);
  final __m12 = __m['title'];
  final String title = (__m12 != null ? uString(__m12) : '');
  final __m13 = __m['onGenerateTitle'];
  final String Function(BuildContext)? onGenerateTitle = (__m13 != null ? uFunc<String Function(BuildContext)>(__m13) : null);
  final __m14 = __m['color'];
  final Color? color = (__m14 != null ? uClass<Color>(__m14) : null);
  final __m15 = __m['theme'];
  final ThemeData? theme = (__m15 != null ? uClass<ThemeData>(__m15) : null);
  final __m16 = __m['darkTheme'];
  final ThemeData? darkTheme = (__m16 != null ? uClass<ThemeData>(__m16) : null);
  final __m17 = __m['highContrastTheme'];
  final ThemeData? highContrastTheme = (__m17 != null ? uClass<ThemeData>(__m17) : null);
  final __m18 = __m['highContrastDarkTheme'];
  final ThemeData? highContrastDarkTheme = (__m18 != null ? uClass<ThemeData>(__m18) : null);
  final __m19 = __m['themeMode'];
  final ThemeMode? themeMode = (__m19 != null ? (__m19 != null ? _uThemeMode(__m19) : null) : ThemeMode.system);
  final __m20 = __m['locale'];
  final Locale? locale = (__m20 != null ? uClass<Locale>(__m20) : null);
  final __m21 = __m['localizationsDelegates'];
  final Iterable<LocalizationsDelegate<dynamic>>? localizationsDelegates = (__m21 != null ? uClass<Iterable<LocalizationsDelegate<dynamic>>>(__m21) : null);
  final __m22 = __m['localeListResolutionCallback'];
  final Locale? Function(List<Locale>?, Iterable<Locale>)? localeListResolutionCallback = (__m22 != null ? uFunc<Locale? Function(List<Locale>?, Iterable<Locale>)>(__m22) : null);
  final __m23 = __m['localeResolutionCallback'];
  final Locale? Function(Locale?, Iterable<Locale>)? localeResolutionCallback = (__m23 != null ? uFunc<Locale? Function(Locale?, Iterable<Locale>)>(__m23) : null);
  final __m24 = __m['supportedLocales'];
  final Iterable<Locale> supportedLocales = (__m24 != null ? uClass<Iterable<Locale>>(__m24) : <Locale>[const Locale('en', 'US')]);
  final __m25 = __m['debugShowMaterialGrid'];
  final bool debugShowMaterialGrid = (__m25 != null ? uBool(__m25) : false);
  final __m26 = __m['showPerformanceOverlay'];
  final bool showPerformanceOverlay = (__m26 != null ? uBool(__m26) : false);
  final __m27 = __m['checkerboardRasterCacheImages'];
  final bool checkerboardRasterCacheImages = (__m27 != null ? uBool(__m27) : false);
  final __m28 = __m['checkerboardOffscreenLayers'];
  final bool checkerboardOffscreenLayers = (__m28 != null ? uBool(__m28) : false);
  final __m29 = __m['showSemanticsDebugger'];
  final bool showSemanticsDebugger = (__m29 != null ? uBool(__m29) : false);
  final __m30 = __m['debugShowCheckedModeBanner'];
  final bool debugShowCheckedModeBanner = (__m30 != null ? uBool(__m30) : true);
  final __m31 = __m['shortcuts'];
  final Map<ShortcutActivator, Intent>? shortcuts = (__m31 != null ? (__m31 is Map<dynamic, dynamic> ? __m31.map((k, v) => MapEntry(uClass<ShortcutActivator>(k), uClass<Intent>(v))) : die('not a map')) : null);
  final __m32 = __m['actions'];
  final Map<Type, Action<Intent>>? actions = (__m32 != null ? (__m32 is Map<dynamic, dynamic> ? __m32.map((k, v) => MapEntry(uClass<Type>(k), uClass<Action<Intent>>(v))) : die('not a map')) : null);
  final __m33 = __m['restorationScopeId'];
  final String? restorationScopeId = (__m33 != null ? uString(__m33) : null);
  final __m34 = __m['scrollBehavior'];
  final ScrollBehavior? scrollBehavior = (__m34 != null ? uClass<ScrollBehavior>(__m34) : null);
  final __m35 = __m['useInheritedMediaQuery'];
  final bool useInheritedMediaQuery = (__m35 != null ? uBool(__m35) : false);
  return MaterialApp(
    key: key,
    navigatorKey: navigatorKey,
    scaffoldMessengerKey: scaffoldMessengerKey,
    home: home,
    routes: routes,
    initialRoute: initialRoute,
    onGenerateRoute: onGenerateRoute,
    onGenerateInitialRoutes: onGenerateInitialRoutes,
    onUnknownRoute: onUnknownRoute,
    navigatorObservers: navigatorObservers,
    builder: builder,
    title: title,
    onGenerateTitle: onGenerateTitle,
    color: color,
    theme: theme,
    darkTheme: darkTheme,
    highContrastTheme: highContrastTheme,
    highContrastDarkTheme: highContrastDarkTheme,
    themeMode: themeMode,
    locale: locale,
    localizationsDelegates: localizationsDelegates,
    localeListResolutionCallback: localeListResolutionCallback,
    localeResolutionCallback: localeResolutionCallback,
    supportedLocales: supportedLocales,
    debugShowMaterialGrid: debugShowMaterialGrid,
    showPerformanceOverlay: showPerformanceOverlay,
    checkerboardRasterCacheImages: checkerboardRasterCacheImages,
    checkerboardOffscreenLayers: checkerboardOffscreenLayers,
    showSemanticsDebugger: showSemanticsDebugger,
    debugShowCheckedModeBanner: debugShowCheckedModeBanner,
    shortcuts: shortcuts,
    actions: actions,
    restorationScopeId: restorationScopeId,
    scrollBehavior: scrollBehavior,
    useInheritedMediaQuery: useInheritedMediaQuery,
  );
}

MaterialApp _uMaterialAppRouter(Map<String, dynamic> __m) {
  final __m1 = __m['key'];
  final Key? key = (__m1 != null ? uClass<Key>(__m1) : null);
  final __m2 = __m['scaffoldMessengerKey'];
  final GlobalKey<ScaffoldMessengerState>? scaffoldMessengerKey = (__m2 != null ? uClass<GlobalKey<ScaffoldMessengerState>>(__m2) : null);
  final __m3 = __m['routeInformationProvider'];
  final RouteInformationProvider? routeInformationProvider = (__m3 != null ? uClass<RouteInformationProvider>(__m3) : null);
  final __m4 = __m['routeInformationParser'];
  final RouteInformationParser<Object> routeInformationParser = uClass<RouteInformationParser<Object>>(__m4);
  final __m5 = __m['routerDelegate'];
  final RouterDelegate<Object> routerDelegate = uClass<RouterDelegate<Object>>(__m5);
  final __m6 = __m['backButtonDispatcher'];
  final BackButtonDispatcher? backButtonDispatcher = (__m6 != null ? uClass<BackButtonDispatcher>(__m6) : null);
  final __m7 = __m['builder'];
  final Widget Function(BuildContext, Widget?)? builder = (__m7 != null ? uFunc<Widget Function(BuildContext, Widget?)>(__m7) : null);
  final __m8 = __m['title'];
  final String title = (__m8 != null ? uString(__m8) : '');
  final __m9 = __m['onGenerateTitle'];
  final String Function(BuildContext)? onGenerateTitle = (__m9 != null ? uFunc<String Function(BuildContext)>(__m9) : null);
  final __m10 = __m['color'];
  final Color? color = (__m10 != null ? uClass<Color>(__m10) : null);
  final __m11 = __m['theme'];
  final ThemeData? theme = (__m11 != null ? uClass<ThemeData>(__m11) : null);
  final __m12 = __m['darkTheme'];
  final ThemeData? darkTheme = (__m12 != null ? uClass<ThemeData>(__m12) : null);
  final __m13 = __m['highContrastTheme'];
  final ThemeData? highContrastTheme = (__m13 != null ? uClass<ThemeData>(__m13) : null);
  final __m14 = __m['highContrastDarkTheme'];
  final ThemeData? highContrastDarkTheme = (__m14 != null ? uClass<ThemeData>(__m14) : null);
  final __m15 = __m['themeMode'];
  final ThemeMode? themeMode = (__m15 != null ? (__m15 != null ? _uThemeMode(__m15) : null) : ThemeMode.system);
  final __m16 = __m['locale'];
  final Locale? locale = (__m16 != null ? uClass<Locale>(__m16) : null);
  final __m17 = __m['localizationsDelegates'];
  final Iterable<LocalizationsDelegate<dynamic>>? localizationsDelegates = (__m17 != null ? uClass<Iterable<LocalizationsDelegate<dynamic>>>(__m17) : null);
  final __m18 = __m['localeListResolutionCallback'];
  final Locale? Function(List<Locale>?, Iterable<Locale>)? localeListResolutionCallback = (__m18 != null ? uFunc<Locale? Function(List<Locale>?, Iterable<Locale>)>(__m18) : null);
  final __m19 = __m['localeResolutionCallback'];
  final Locale? Function(Locale?, Iterable<Locale>)? localeResolutionCallback = (__m19 != null ? uFunc<Locale? Function(Locale?, Iterable<Locale>)>(__m19) : null);
  final __m20 = __m['supportedLocales'];
  final Iterable<Locale> supportedLocales = (__m20 != null ? uClass<Iterable<Locale>>(__m20) : <Locale>[const Locale('en', 'US')]);
  final __m21 = __m['debugShowMaterialGrid'];
  final bool debugShowMaterialGrid = (__m21 != null ? uBool(__m21) : false);
  final __m22 = __m['showPerformanceOverlay'];
  final bool showPerformanceOverlay = (__m22 != null ? uBool(__m22) : false);
  final __m23 = __m['checkerboardRasterCacheImages'];
  final bool checkerboardRasterCacheImages = (__m23 != null ? uBool(__m23) : false);
  final __m24 = __m['checkerboardOffscreenLayers'];
  final bool checkerboardOffscreenLayers = (__m24 != null ? uBool(__m24) : false);
  final __m25 = __m['showSemanticsDebugger'];
  final bool showSemanticsDebugger = (__m25 != null ? uBool(__m25) : false);
  final __m26 = __m['debugShowCheckedModeBanner'];
  final bool debugShowCheckedModeBanner = (__m26 != null ? uBool(__m26) : true);
  final __m27 = __m['shortcuts'];
  final Map<ShortcutActivator, Intent>? shortcuts = (__m27 != null ? (__m27 is Map<dynamic, dynamic> ? __m27.map((k, v) => MapEntry(uClass<ShortcutActivator>(k), uClass<Intent>(v))) : die('not a map')) : null);
  final __m28 = __m['actions'];
  final Map<Type, Action<Intent>>? actions = (__m28 != null ? (__m28 is Map<dynamic, dynamic> ? __m28.map((k, v) => MapEntry(uClass<Type>(k), uClass<Action<Intent>>(v))) : die('not a map')) : null);
  final __m29 = __m['restorationScopeId'];
  final String? restorationScopeId = (__m29 != null ? uString(__m29) : null);
  final __m30 = __m['scrollBehavior'];
  final ScrollBehavior? scrollBehavior = (__m30 != null ? uClass<ScrollBehavior>(__m30) : null);
  final __m31 = __m['useInheritedMediaQuery'];
  final bool useInheritedMediaQuery = (__m31 != null ? uBool(__m31) : false);
  return MaterialApp.router(
    key: key,
    scaffoldMessengerKey: scaffoldMessengerKey,
    routeInformationProvider: routeInformationProvider,
    routeInformationParser: routeInformationParser,
    routerDelegate: routerDelegate,
    backButtonDispatcher: backButtonDispatcher,
    builder: builder,
    title: title,
    onGenerateTitle: onGenerateTitle,
    color: color,
    theme: theme,
    darkTheme: darkTheme,
    highContrastTheme: highContrastTheme,
    highContrastDarkTheme: highContrastDarkTheme,
    themeMode: themeMode,
    locale: locale,
    localizationsDelegates: localizationsDelegates,
    localeListResolutionCallback: localeListResolutionCallback,
    localeResolutionCallback: localeResolutionCallback,
    supportedLocales: supportedLocales,
    debugShowMaterialGrid: debugShowMaterialGrid,
    showPerformanceOverlay: showPerformanceOverlay,
    checkerboardRasterCacheImages: checkerboardRasterCacheImages,
    checkerboardOffscreenLayers: checkerboardOffscreenLayers,
    showSemanticsDebugger: showSemanticsDebugger,
    debugShowCheckedModeBanner: debugShowCheckedModeBanner,
    shortcuts: shortcuts,
    actions: actions,
    restorationScopeId: restorationScopeId,
    scrollBehavior: scrollBehavior,
    useInheritedMediaQuery: useInheritedMediaQuery,
  );
}

KeyEventResult _uKeyEventResult(dynamic v) {
  if (v is String) {
    switch(v) {
      case 'handled':
        return KeyEventResult.handled;
      case 'ignored':
        return KeyEventResult.ignored;
      case 'skipRemainingHandlers':
        return KeyEventResult.skipRemainingHandlers;
    }
  }
  throw 'illegal enum value $v';
}

PhysicalKeyboardKey _uPhysicalKeyboardKey(Map<String, dynamic> __m) {
  final __m1 = __m['usbHidUsage'];
  final int usbHidUsage = uInt(__m1);
  return PhysicalKeyboardKey(
    usbHidUsage,
  );
}

LogicalKeyboardKey _uLogicalKeyboardKey(Map<String, dynamic> __m) {
  final __m1 = __m['keyId'];
  final int keyId = uInt(__m1);
  return LogicalKeyboardKey(
    keyId,
  );
}

FocusNode _uFocusNode(Map<String, dynamic> __m) {
  final __m1 = __m['debugLabel'];
  final String? debugLabel = (__m1 != null ? uString(__m1) : null);
  final __m2 = __m['onKey'];
  final KeyEventResult Function(FocusNode, RawKeyEvent)? onKey = (__m2 != null ? uFunc<KeyEventResult Function(FocusNode, RawKeyEvent)>(__m2) : null);
  final __m3 = __m['onKeyEvent'];
  final KeyEventResult Function(FocusNode, KeyEvent)? onKeyEvent = (__m3 != null ? uFunc<KeyEventResult Function(FocusNode, KeyEvent)>(__m3) : null);
  final __m4 = __m['skipTraversal'];
  final bool skipTraversal = (__m4 != null ? uBool(__m4) : false);
  final __m5 = __m['canRequestFocus'];
  final bool canRequestFocus = (__m5 != null ? uBool(__m5) : true);
  final __m6 = __m['descendantsAreFocusable'];
  final bool descendantsAreFocusable = (__m6 != null ? uBool(__m6) : true);
  return FocusNode(
    debugLabel: debugLabel,
    onKey: onKey,
    onKeyEvent: onKeyEvent,
    skipTraversal: skipTraversal,
    canRequestFocus: canRequestFocus,
    descendantsAreFocusable: descendantsAreFocusable,
  );
}

ElevatedButton _uElevatedButton(Map<String, dynamic> __m) {
  final __m1 = __m['key'];
  final Key? key = (__m1 != null ? uClass<Key>(__m1) : null);
  final __m2 = __m['onPressed'];
  final void Function()? onPressed = (__m2 != null ? uFunc<void Function()>(__m2) : null);
  final __m3 = __m['onLongPress'];
  final void Function()? onLongPress = (__m3 != null ? uFunc<void Function()>(__m3) : null);
  final __m4 = __m['style'];
  final ButtonStyle? style = (__m4 != null ? uClass<ButtonStyle>(__m4) : null);
  final __m5 = __m['focusNode'];
  final FocusNode? focusNode = (__m5 != null ? uClass<FocusNode>(__m5) : null);
  final __m6 = __m['autofocus'];
  final bool autofocus = (__m6 != null ? uBool(__m6) : false);
  final __m7 = __m['clipBehavior'];
  final Clip clipBehavior = (__m7 != null ? _uClip(__m7) : Clip.none);
  final __m8 = __m['child'];
  final Widget? child = (__m8 != null ? uClass<Widget>(__m8) : null);
  return ElevatedButton(
    key: key,
    onPressed: onPressed,
    onLongPress: onLongPress,
    style: style,
    focusNode: focusNode,
    autofocus: autofocus,
    clipBehavior: clipBehavior,
    child: child,
  );
}

ElevatedButton _uElevatedButtonIcon(Map<String, dynamic> __m) {
  final __m1 = __m['key'];
  final Key? key = (__m1 != null ? uClass<Key>(__m1) : null);
  final __m2 = __m['onPressed'];
  final void Function()? onPressed = (__m2 != null ? uFunc<void Function()>(__m2) : null);
  final __m3 = __m['onLongPress'];
  final void Function()? onLongPress = (__m3 != null ? uFunc<void Function()>(__m3) : null);
  final __m4 = __m['style'];
  final ButtonStyle? style = (__m4 != null ? uClass<ButtonStyle>(__m4) : null);
  final __m5 = __m['focusNode'];
  final FocusNode? focusNode = (__m5 != null ? uClass<FocusNode>(__m5) : null);
  final __m6 = __m['autofocus'];
  final bool? autofocus = (__m6 != null ? uBool(__m6) : null);
  final __m7 = __m['clipBehavior'];
  final Clip? clipBehavior = (__m7 != null ? _uClip(__m7) : null);
  final __m8 = __m['icon'];
  final Widget icon = uClass<Widget>(__m8);
  final __m9 = __m['label'];
  final Widget label = uClass<Widget>(__m9);
  return ElevatedButton.icon(
    key: key,
    onPressed: onPressed,
    onLongPress: onLongPress,
    style: style,
    focusNode: focusNode,
    autofocus: autofocus,
    clipBehavior: clipBehavior,
    icon: icon,
    label: label,
  );
}

final unmarshalers = <String, Unmarshal>{
  'Object.': _uObject,
  'RouteSettings.': _uRouteSettings,
  'NavigatorObserver.': _uNavigatorObserver,
  'Navigator.': _uNavigator,
  'NavigatorState.': _uNavigatorState,
  'ScaffoldMessenger.': _uScaffoldMessenger,
  'ScaffoldMessengerState.': _uScaffoldMessengerState,
  'MapEntry.': _uMapEntry,
  'Color.': _uColor,
  'Color.fromARGB': _uColorFromARGB,
  'Color.fromRGBO': _uColorFromRGBO,
  'VisualDensity.': _uVisualDensity,
  'ColorSwatch.': _uColorSwatch,
  'MaterialColor.': _uMaterialColor,
  'ColorScheme.': _uColorScheme,
  'ColorScheme.light': _uColorSchemeLight,
  'ColorScheme.dark': _uColorSchemeDark,
  'ColorScheme.highContrastLight': _uColorSchemeHighContrastLight,
  'ColorScheme.highContrastDark': _uColorSchemeHighContrastDark,
  'ColorScheme.fromSwatch': _uColorSchemeFromSwatch,
  'ButtonThemeData.': _uButtonThemeData,
  'Locale.': _uLocale,
  'Locale.fromSubtags': _uLocaleFromSubtags,
  'Paint.': _uPaint,
  'Offset.': _uOffset,
  'Offset.fromDirection': _uOffsetFromDirection,
  'Shadow.': _uShadow,
  'FontFeature.': _uFontFeature,
  'FontFeature.enable': _uFontFeatureEnable,
  'FontFeature.disable': _uFontFeatureDisable,
  'FontFeature.alternative': _uFontFeatureAlternative,
  'FontFeature.alternativeFractions': _uFontFeatureAlternativeFractions,
  'FontFeature.contextualAlternates': _uFontFeatureContextualAlternates,
  'FontFeature.caseSensitiveForms': _uFontFeatureCaseSensitiveForms,
  'FontFeature.characterVariant': _uFontFeatureCharacterVariant,
  'FontFeature.denominator': _uFontFeatureDenominator,
  'FontFeature.fractions': _uFontFeatureFractions,
  'FontFeature.historicalForms': _uFontFeatureHistoricalForms,
  'FontFeature.historicalLigatures': _uFontFeatureHistoricalLigatures,
  'FontFeature.liningFigures': _uFontFeatureLiningFigures,
  'FontFeature.localeAware': _uFontFeatureLocaleAware,
  'FontFeature.notationalForms': _uFontFeatureNotationalForms,
  'FontFeature.numerators': _uFontFeatureNumerators,
  'FontFeature.oldstyleFigures': _uFontFeatureOldstyleFigures,
  'FontFeature.ordinalForms': _uFontFeatureOrdinalForms,
  'FontFeature.proportionalFigures': _uFontFeatureProportionalFigures,
  'FontFeature.randomize': _uFontFeatureRandomize,
  'FontFeature.stylisticAlternates': _uFontFeatureStylisticAlternates,
  'FontFeature.scientificInferiors': _uFontFeatureScientificInferiors,
  'FontFeature.stylisticSet': _uFontFeatureStylisticSet,
  'FontFeature.subscripts': _uFontFeatureSubscripts,
  'FontFeature.superscripts': _uFontFeatureSuperscripts,
  'FontFeature.swash': _uFontFeatureSwash,
  'FontFeature.tabularFigures': _uFontFeatureTabularFigures,
  'FontFeature.slashedZero': _uFontFeatureSlashedZero,
  'TextDecoration.combine': _uTextDecorationCombine,
  'TextStyle.': _uTextStyle,
  'Size.': _uSize,
  'Size.copy': _uSizeCopy,
  'Size.square': _uSizeSquare,
  'Size.fromWidth': _uSizeFromWidth,
  'Size.fromHeight': _uSizeFromHeight,
  'Size.fromRadius': _uSizeFromRadius,
  'BoxConstraints.': _uBoxConstraints,
  'BoxConstraints.tight': _uBoxConstraintsTight,
  'BoxConstraints.tightFor': _uBoxConstraintsTightFor,
  'BoxConstraints.tightForFinite': _uBoxConstraintsTightForFinite,
  'BoxConstraints.loose': _uBoxConstraintsLoose,
  'BoxConstraints.expand': _uBoxConstraintsExpand,
  'Radius.circular': _uRadiusCircular,
  'Radius.elliptical': _uRadiusElliptical,
  'BorderRadius.all': _uBorderRadiusAll,
  'BorderRadius.circular': _uBorderRadiusCircular,
  'BorderRadius.vertical': _uBorderRadiusVertical,
  'BorderRadius.horizontal': _uBorderRadiusHorizontal,
  'BorderRadius.only': _uBorderRadiusOnly,
  'ToggleButtonsThemeData.': _uToggleButtonsThemeData,
  'TextTheme.': _uTextTheme,
  'BorderSide.': _uBorderSide,
  'InputDecorationTheme.': _uInputDecorationTheme,
  'IconThemeData.': _uIconThemeData,
  'IconThemeData.fallback': _uIconThemeDataFallback,
  'RangeValues.': _uRangeValues,
  'SliderThemeData.': _uSliderThemeData,
  'SliderThemeData.fromPrimaryColors': _uSliderThemeDataFromPrimaryColors,
  'TabBarTheme.': _uTabBarTheme,
  'Duration.': _uDuration,
  'TooltipThemeData.': _uTooltipThemeData,
  'CardTheme.': _uCardTheme,
  'ChipThemeData.': _uChipThemeData,
  'ChipThemeData.fromDefaults': _uChipThemeDataFromDefaults,
  'PageTransitionsTheme.': _uPageTransitionsTheme,
  'SystemUiOverlayStyle.': _uSystemUiOverlayStyle,
  'AppBarTheme.': _uAppBarTheme,
  'ScrollbarThemeData.': _uScrollbarThemeData,
  'BottomAppBarTheme.': _uBottomAppBarTheme,
  'DialogTheme.': _uDialogTheme,
  'FloatingActionButtonThemeData.': _uFloatingActionButtonThemeData,
  'NavigationRailThemeData.': _uNavigationRailThemeData,
  'Typography.': _uTypography,
  'Typography.material2014': _uTypographyMaterial2014,
  'Typography.material2018': _uTypographyMaterial2018,
  'CupertinoTextThemeData.': _uCupertinoTextThemeData,
  'NoDefaultCupertinoThemeData.': _uNoDefaultCupertinoThemeData,
  'SnackBarThemeData.': _uSnackBarThemeData,
  'BottomSheetThemeData.': _uBottomSheetThemeData,
  'PopupMenuThemeData.': _uPopupMenuThemeData,
  'MaterialBannerThemeData.': _uMaterialBannerThemeData,
  'DividerThemeData.': _uDividerThemeData,
  'ButtonBarThemeData.': _uButtonBarThemeData,
  'BottomNavigationBarThemeData.': _uBottomNavigationBarThemeData,
  'TimePickerThemeData.': _uTimePickerThemeData,
  'ButtonStyle.': _uButtonStyle,
  'TextButtonThemeData.': _uTextButtonThemeData,
  'ElevatedButtonThemeData.': _uElevatedButtonThemeData,
  'OutlinedButtonThemeData.': _uOutlinedButtonThemeData,
  'TextSelectionThemeData.': _uTextSelectionThemeData,
  'DataTableThemeData.': _uDataTableThemeData,
  'CheckboxThemeData.': _uCheckboxThemeData,
  'RadioThemeData.': _uRadioThemeData,
  'SwitchThemeData.': _uSwitchThemeData,
  'ProgressIndicatorThemeData.': _uProgressIndicatorThemeData,
  'ThemeData.': _uThemeData,
  'ThemeData.raw': _uThemeDataRaw,
  'ThemeData.from': _uThemeDataFrom,
  'ThemeData.light': _uThemeDataLight,
  'ThemeData.dark': _uThemeDataDark,
  'ThemeData.fallback': _uThemeDataFallback,
  'DoNothingIntent.': _uDoNothingIntent,
  'ScrollBehavior.': _uScrollBehavior,
  'RouteInformation.': _uRouteInformation,
  'MaterialApp.': _uMaterialApp,
  'MaterialApp.router': _uMaterialAppRouter,
  'PhysicalKeyboardKey.': _uPhysicalKeyboardKey,
  'LogicalKeyboardKey.': _uLogicalKeyboardKey,
  'FocusNode.': _uFocusNode,
  'ElevatedButton.': _uElevatedButton,
  'ElevatedButton.icon': _uElevatedButtonIcon,
};
