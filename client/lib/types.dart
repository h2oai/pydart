// ignore_for_file: deprecated_member_use
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
  final String? name = uNull<String>(uString)(__m['name']);
  final Object? arguments = uNull<Object>(uClass)(__m['arguments']);
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
  final Key? key = uNull<Key>(uClass)(__m['key']);
  final List<Page<dynamic>> pages = uConst(<Page<dynamic>>[], uList<Page<dynamic>>(uClass))(__m['pages']);
  final bool Function(Route<dynamic>, dynamic)? onPopPage = uNull<bool Function(Route<dynamic>, dynamic)>(uFunc)(__m['onPopPage']);
  final String? initialRoute = uNull<String>(uString)(__m['initialRoute']);
  final List<Route<dynamic>> Function(NavigatorState, String) onGenerateInitialRoutes = uConst(Navigator.defaultGenerateInitialRoutes, uFunc)(__m['onGenerateInitialRoutes']);
  final Route<dynamic>? Function(RouteSettings)? onGenerateRoute = uNull<Route<dynamic>? Function(RouteSettings)>(uFunc)(__m['onGenerateRoute']);
  final Route<dynamic>? Function(RouteSettings)? onUnknownRoute = uNull<Route<dynamic>? Function(RouteSettings)>(uFunc)(__m['onUnknownRoute']);
  final TransitionDelegate<dynamic> transitionDelegate = uClass(__m['transitionDelegate']);
  final bool reportsRouteUpdateToEngine = uConst<bool>(false, uBool)(__m['reportsRouteUpdateToEngine']);
  final List<NavigatorObserver> observers = uConst(<NavigatorObserver>[], uList<NavigatorObserver>(uClass))(__m['observers']);
  final String? restorationScopeId = uNull<String>(uString)(__m['restorationScopeId']);
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
  final Key? key = uNull<Key>(uClass)(__m['key']);
  final Widget child = uClass(__m['child']);
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
  final K key = (__m['key']);
  final V value = (__m['value']);
  return MapEntry(
    key,
    value,
  );
}

Color _uColor(Map<String, dynamic> __m) {
  final int value = uInt(__m['value']);
  return Color(
    value,
  );
}

Color _uColorFromARGB(Map<String, dynamic> __m) {
  final int a = uInt(__m['a']);
  final int r = uInt(__m['r']);
  final int g = uInt(__m['g']);
  final int b = uInt(__m['b']);
  return Color.fromARGB(
    a,
    r,
    g,
    b,
  );
}

Color _uColorFromRGBO(Map<String, dynamic> __m) {
  final int r = uInt(__m['r']);
  final int g = uInt(__m['g']);
  final int b = uInt(__m['b']);
  final double opacity = uDouble(__m['opacity']);
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
  final double horizontal = uConst<double>(0.0, uDouble)(__m['horizontal']);
  final double vertical = uConst<double>(0.0, uDouble)(__m['vertical']);
  return VisualDensity(
    horizontal: horizontal,
    vertical: vertical,
  );
}

ColorSwatch _uColorSwatch<T>(Map<String, dynamic> __m) {
  final int primary = uInt(__m['primary']);
  final Map<T, Color> _swatch = uClass(__m['_swatch']);
  return ColorSwatch(
    primary,
    _swatch,
  );
}

MaterialColor _uMaterialColor(Map<String, dynamic> __m) {
  final int primary = uInt(__m['primary']);
  final Map<int, Color> swatch = uClass(__m['swatch']);
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
  final Color primary = uClass(__m['primary']);
  final Color primaryVariant = uClass(__m['primaryVariant']);
  final Color secondary = uClass(__m['secondary']);
  final Color secondaryVariant = uClass(__m['secondaryVariant']);
  final Color surface = uClass(__m['surface']);
  final Color background = uClass(__m['background']);
  final Color error = uClass(__m['error']);
  final Color onPrimary = uClass(__m['onPrimary']);
  final Color onSecondary = uClass(__m['onSecondary']);
  final Color onSurface = uClass(__m['onSurface']);
  final Color onBackground = uClass(__m['onBackground']);
  final Color onError = uClass(__m['onError']);
  final Brightness brightness = _uBrightness(__m['brightness']);
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
  final Color primary = uClass(__m['primary']);
  final Color primaryVariant = uClass(__m['primaryVariant']);
  final Color secondary = uClass(__m['secondary']);
  final Color secondaryVariant = uClass(__m['secondaryVariant']);
  final Color surface = uClass(__m['surface']);
  final Color background = uClass(__m['background']);
  final Color error = uClass(__m['error']);
  final Color onPrimary = uClass(__m['onPrimary']);
  final Color onSecondary = uClass(__m['onSecondary']);
  final Color onSurface = uClass(__m['onSurface']);
  final Color onBackground = uClass(__m['onBackground']);
  final Color onError = uClass(__m['onError']);
  final Brightness brightness = uConst(Brightness.light, _uBrightness)(__m['brightness']);
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
  final Color primary = uClass(__m['primary']);
  final Color primaryVariant = uClass(__m['primaryVariant']);
  final Color secondary = uClass(__m['secondary']);
  final Color secondaryVariant = uClass(__m['secondaryVariant']);
  final Color surface = uClass(__m['surface']);
  final Color background = uClass(__m['background']);
  final Color error = uClass(__m['error']);
  final Color onPrimary = uClass(__m['onPrimary']);
  final Color onSecondary = uClass(__m['onSecondary']);
  final Color onSurface = uClass(__m['onSurface']);
  final Color onBackground = uClass(__m['onBackground']);
  final Color onError = uClass(__m['onError']);
  final Brightness brightness = uConst(Brightness.dark, _uBrightness)(__m['brightness']);
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
  final Color primary = uClass(__m['primary']);
  final Color primaryVariant = uClass(__m['primaryVariant']);
  final Color secondary = uClass(__m['secondary']);
  final Color secondaryVariant = uClass(__m['secondaryVariant']);
  final Color surface = uClass(__m['surface']);
  final Color background = uClass(__m['background']);
  final Color error = uClass(__m['error']);
  final Color onPrimary = uClass(__m['onPrimary']);
  final Color onSecondary = uClass(__m['onSecondary']);
  final Color onSurface = uClass(__m['onSurface']);
  final Color onBackground = uClass(__m['onBackground']);
  final Color onError = uClass(__m['onError']);
  final Brightness brightness = uConst(Brightness.light, _uBrightness)(__m['brightness']);
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
  final Color primary = uClass(__m['primary']);
  final Color primaryVariant = uClass(__m['primaryVariant']);
  final Color secondary = uClass(__m['secondary']);
  final Color secondaryVariant = uClass(__m['secondaryVariant']);
  final Color surface = uClass(__m['surface']);
  final Color background = uClass(__m['background']);
  final Color error = uClass(__m['error']);
  final Color onPrimary = uClass(__m['onPrimary']);
  final Color onSecondary = uClass(__m['onSecondary']);
  final Color onSurface = uClass(__m['onSurface']);
  final Color onBackground = uClass(__m['onBackground']);
  final Color onError = uClass(__m['onError']);
  final Brightness brightness = uConst(Brightness.dark, _uBrightness)(__m['brightness']);
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
  final MaterialColor primarySwatch = uClass(__m['primarySwatch']);
  final Color? primaryColorDark = uNull<Color>(uClass)(__m['primaryColorDark']);
  final Color? accentColor = uNull<Color>(uClass)(__m['accentColor']);
  final Color? cardColor = uNull<Color>(uClass)(__m['cardColor']);
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final Color? errorColor = uNull<Color>(uClass)(__m['errorColor']);
  final Brightness brightness = uConst(Brightness.light, _uBrightness)(__m['brightness']);
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
  final ButtonTextTheme textTheme = uConst(ButtonTextTheme.normal, _uButtonTextTheme)(__m['textTheme']);
  final double minWidth = uConst<double>(88.0, uDouble)(__m['minWidth']);
  final double height = uConst<double>(36.0, uDouble)(__m['height']);
  final EdgeInsetsGeometry? padding = uNull<EdgeInsetsGeometry>(uClass)(__m['padding']);
  final ShapeBorder? shape = uNull<ShapeBorder>(uClass)(__m['shape']);
  final ButtonBarLayoutBehavior layoutBehavior = uConst(ButtonBarLayoutBehavior.padded, _uButtonBarLayoutBehavior)(__m['layoutBehavior']);
  final bool alignedDropdown = uConst<bool>(false, uBool)(__m['alignedDropdown']);
  final Color? buttonColor = uNull<Color>(uClass)(__m['buttonColor']);
  final Color? disabledColor = uNull<Color>(uClass)(__m['disabledColor']);
  final Color? focusColor = uNull<Color>(uClass)(__m['focusColor']);
  final Color? hoverColor = uNull<Color>(uClass)(__m['hoverColor']);
  final Color? highlightColor = uNull<Color>(uClass)(__m['highlightColor']);
  final Color? splashColor = uNull<Color>(uClass)(__m['splashColor']);
  final ColorScheme? colorScheme = uNull<ColorScheme>(uClass)(__m['colorScheme']);
  final MaterialTapTargetSize? materialTapTargetSize = uNull<MaterialTapTargetSize>(_uMaterialTapTargetSize)(__m['materialTapTargetSize']);
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
  final String _languageCode = uString(__m['_languageCode']);
  final String? _countryCode = uNull<String>(uString)(__m['_countryCode']);
  return Locale(
    _languageCode,
    _countryCode,
  );
}

Locale _uLocaleFromSubtags(Map<String, dynamic> __m) {
  final String languageCode = uConst<String>('und', uString)(__m['languageCode']);
  final String? scriptCode = uNull<String>(uString)(__m['scriptCode']);
  final String? countryCode = uNull<String>(uString)(__m['countryCode']);
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
  final double dx = uDouble(__m['dx']);
  final double dy = uDouble(__m['dy']);
  return Offset(
    dx,
    dy,
  );
}

Offset _uOffsetFromDirection(Map<String, dynamic> __m) {
  final double direction = uDouble(__m['direction']);
  final double distance = uConst<double>(1.0, uDouble)(__m['distance']);
  return Offset.fromDirection(
    direction,
    distance,
  );
}

Shadow _uShadow(Map<String, dynamic> __m) {
  final Color color = uClass(__m['color']);
  final Offset offset = uClass(__m['offset']);
  final double blurRadius = uConst<double>(0.0, uDouble)(__m['blurRadius']);
  return Shadow(
    color: color,
    offset: offset,
    blurRadius: blurRadius,
  );
}

FontFeature _uFontFeature(Map<String, dynamic> __m) {
  final String feature = uString(__m['feature']);
  final int value = uConst<int>(1, uInt)(__m['value']);
  return FontFeature(
    feature,
    value,
  );
}

FontFeature _uFontFeatureEnable(Map<String, dynamic> __m) {
  final String feature = uString(__m['feature']);
  return FontFeature.enable(
    feature,
  );
}

FontFeature _uFontFeatureDisable(Map<String, dynamic> __m) {
  final String feature = uString(__m['feature']);
  return FontFeature.disable(
    feature,
  );
}

FontFeature _uFontFeatureAlternative(Map<String, dynamic> __m) {
  final int value = uInt(__m['value']);
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
  final int value = uInt(__m['value']);
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
  final bool enable = uConst<bool>(true, uBool)(__m['enable']);
  return FontFeature.localeAware(
    enable: enable,
  );
}

FontFeature _uFontFeatureNotationalForms(Map<String, dynamic> __m) {
  final int value = uConst<int>(1, uInt)(__m['value']);
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
  final int value = uInt(__m['value']);
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
  final int value = uConst<int>(1, uInt)(__m['value']);
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
  final List<TextDecoration> decorations = uList<TextDecoration>(uClass)(__m['decorations']);
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
  final bool inherit = uConst<bool>(true, uBool)(__m['inherit']);
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final double? fontSize = uNull<double>(uDouble)(__m['fontSize']);
  final FontWeight? fontWeight = uNull<FontWeight>(uClass)(__m['fontWeight']);
  final FontStyle? fontStyle = uNull<FontStyle>(_uFontStyle)(__m['fontStyle']);
  final double? letterSpacing = uNull<double>(uDouble)(__m['letterSpacing']);
  final double? wordSpacing = uNull<double>(uDouble)(__m['wordSpacing']);
  final TextBaseline? textBaseline = uNull<TextBaseline>(_uTextBaseline)(__m['textBaseline']);
  final double? height = uNull<double>(uDouble)(__m['height']);
  final TextLeadingDistribution? leadingDistribution = uNull<TextLeadingDistribution>(_uTextLeadingDistribution)(__m['leadingDistribution']);
  final Locale? locale = uNull<Locale>(uClass)(__m['locale']);
  final Paint? foreground = uNull<Paint>(uClass)(__m['foreground']);
  final Paint? background = uNull<Paint>(uClass)(__m['background']);
  final List<Shadow>? shadows = uNull<List<Shadow>>(uList<Shadow>(uClass))(__m['shadows']);
  final List<FontFeature>? fontFeatures = uNull<List<FontFeature>>(uList<FontFeature>(uClass))(__m['fontFeatures']);
  final TextDecoration? decoration = uNull<TextDecoration>(uClass)(__m['decoration']);
  final Color? decorationColor = uNull<Color>(uClass)(__m['decorationColor']);
  final TextDecorationStyle? decorationStyle = uNull<TextDecorationStyle>(_uTextDecorationStyle)(__m['decorationStyle']);
  final double? decorationThickness = uNull<double>(uDouble)(__m['decorationThickness']);
  final String? debugLabel = uNull<String>(uString)(__m['debugLabel']);
  final String? fontFamily = uNull<String>(uString)(__m['fontFamily']);
  final List<String>? fontFamilyFallback = uNull<List<String>>(uList<String>(uString))(__m['fontFamilyFallback']);
  final String? package = uNull<String>(uString)(__m['package']);
  final TextOverflow? overflow = uNull<TextOverflow>(_uTextOverflow)(__m['overflow']);
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
  final double width = uDouble(__m['width']);
  final double height = uDouble(__m['height']);
  return Size(
    width,
    height,
  );
}

Size _uSizeCopy(Map<String, dynamic> __m) {
  final Size source = uClass(__m['source']);
  return Size.copy(
    source,
  );
}

Size _uSizeSquare(Map<String, dynamic> __m) {
  final double dimension = uDouble(__m['dimension']);
  return Size.square(
    dimension,
  );
}

Size _uSizeFromWidth(Map<String, dynamic> __m) {
  final double width = uDouble(__m['width']);
  return Size.fromWidth(
    width,
  );
}

Size _uSizeFromHeight(Map<String, dynamic> __m) {
  final double height = uDouble(__m['height']);
  return Size.fromHeight(
    height,
  );
}

Size _uSizeFromRadius(Map<String, dynamic> __m) {
  final double radius = uDouble(__m['radius']);
  return Size.fromRadius(
    radius,
  );
}

BoxConstraints _uBoxConstraints(Map<String, dynamic> __m) {
  final double minWidth = uConst<double>(0.0, uDouble)(__m['minWidth']);
  final double maxWidth = uConst<double>(double.infinity, uDouble)(__m['maxWidth']);
  final double minHeight = uConst<double>(0.0, uDouble)(__m['minHeight']);
  final double maxHeight = uConst<double>(double.infinity, uDouble)(__m['maxHeight']);
  return BoxConstraints(
    minWidth: minWidth,
    maxWidth: maxWidth,
    minHeight: minHeight,
    maxHeight: maxHeight,
  );
}

BoxConstraints _uBoxConstraintsTight(Map<String, dynamic> __m) {
  final Size size = uClass(__m['size']);
  return BoxConstraints.tight(
    size,
  );
}

BoxConstraints _uBoxConstraintsTightFor(Map<String, dynamic> __m) {
  final double? width = uNull<double>(uDouble)(__m['width']);
  final double? height = uNull<double>(uDouble)(__m['height']);
  return BoxConstraints.tightFor(
    width: width,
    height: height,
  );
}

BoxConstraints _uBoxConstraintsTightForFinite(Map<String, dynamic> __m) {
  final double width = uConst<double>(double.infinity, uDouble)(__m['width']);
  final double height = uConst<double>(double.infinity, uDouble)(__m['height']);
  return BoxConstraints.tightForFinite(
    width: width,
    height: height,
  );
}

BoxConstraints _uBoxConstraintsLoose(Map<String, dynamic> __m) {
  final Size size = uClass(__m['size']);
  return BoxConstraints.loose(
    size,
  );
}

BoxConstraints _uBoxConstraintsExpand(Map<String, dynamic> __m) {
  final double? width = uNull<double>(uDouble)(__m['width']);
  final double? height = uNull<double>(uDouble)(__m['height']);
  return BoxConstraints.expand(
    width: width,
    height: height,
  );
}

Radius _uRadiusCircular(Map<String, dynamic> __m) {
  final double radius = uDouble(__m['radius']);
  return Radius.circular(
    radius,
  );
}

Radius _uRadiusElliptical(Map<String, dynamic> __m) {
  final double x = uDouble(__m['x']);
  final double y = uDouble(__m['y']);
  return Radius.elliptical(
    x,
    y,
  );
}

BorderRadius _uBorderRadiusAll(Map<String, dynamic> __m) {
  final Radius radius = uClass(__m['radius']);
  return BorderRadius.all(
    radius,
  );
}

BorderRadius _uBorderRadiusCircular(Map<String, dynamic> __m) {
  final double radius = uDouble(__m['radius']);
  return BorderRadius.circular(
    radius,
  );
}

BorderRadius _uBorderRadiusVertical(Map<String, dynamic> __m) {
  final Radius top = uClass(__m['top']);
  final Radius bottom = uClass(__m['bottom']);
  return BorderRadius.vertical(
    top: top,
    bottom: bottom,
  );
}

BorderRadius _uBorderRadiusHorizontal(Map<String, dynamic> __m) {
  final Radius left = uClass(__m['left']);
  final Radius right = uClass(__m['right']);
  return BorderRadius.horizontal(
    left: left,
    right: right,
  );
}

BorderRadius _uBorderRadiusOnly(Map<String, dynamic> __m) {
  final Radius topLeft = uClass(__m['topLeft']);
  final Radius topRight = uClass(__m['topRight']);
  final Radius bottomLeft = uClass(__m['bottomLeft']);
  final Radius bottomRight = uClass(__m['bottomRight']);
  return BorderRadius.only(
    topLeft: topLeft,
    topRight: topRight,
    bottomLeft: bottomLeft,
    bottomRight: bottomRight,
  );
}

ToggleButtonsThemeData _uToggleButtonsThemeData(Map<String, dynamic> __m) {
  final TextStyle? textStyle = uNull<TextStyle>(uClass)(__m['textStyle']);
  final BoxConstraints? constraints = uNull<BoxConstraints>(uClass)(__m['constraints']);
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final Color? selectedColor = uNull<Color>(uClass)(__m['selectedColor']);
  final Color? disabledColor = uNull<Color>(uClass)(__m['disabledColor']);
  final Color? fillColor = uNull<Color>(uClass)(__m['fillColor']);
  final Color? focusColor = uNull<Color>(uClass)(__m['focusColor']);
  final Color? highlightColor = uNull<Color>(uClass)(__m['highlightColor']);
  final Color? hoverColor = uNull<Color>(uClass)(__m['hoverColor']);
  final Color? splashColor = uNull<Color>(uClass)(__m['splashColor']);
  final Color? borderColor = uNull<Color>(uClass)(__m['borderColor']);
  final Color? selectedBorderColor = uNull<Color>(uClass)(__m['selectedBorderColor']);
  final Color? disabledBorderColor = uNull<Color>(uClass)(__m['disabledBorderColor']);
  final BorderRadius? borderRadius = uNull<BorderRadius>(uClass)(__m['borderRadius']);
  final double? borderWidth = uNull<double>(uDouble)(__m['borderWidth']);
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
  final TextStyle? headline1 = uNull<TextStyle>(uClass)(__m['headline1']);
  final TextStyle? headline2 = uNull<TextStyle>(uClass)(__m['headline2']);
  final TextStyle? headline3 = uNull<TextStyle>(uClass)(__m['headline3']);
  final TextStyle? headline4 = uNull<TextStyle>(uClass)(__m['headline4']);
  final TextStyle? headline5 = uNull<TextStyle>(uClass)(__m['headline5']);
  final TextStyle? headline6 = uNull<TextStyle>(uClass)(__m['headline6']);
  final TextStyle? subtitle1 = uNull<TextStyle>(uClass)(__m['subtitle1']);
  final TextStyle? subtitle2 = uNull<TextStyle>(uClass)(__m['subtitle2']);
  final TextStyle? bodyText1 = uNull<TextStyle>(uClass)(__m['bodyText1']);
  final TextStyle? bodyText2 = uNull<TextStyle>(uClass)(__m['bodyText2']);
  final TextStyle? caption = uNull<TextStyle>(uClass)(__m['caption']);
  final TextStyle? button = uNull<TextStyle>(uClass)(__m['button']);
  final TextStyle? overline = uNull<TextStyle>(uClass)(__m['overline']);
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
  final Color color = uClass(__m['color']);
  final double width = uConst<double>(1.0, uDouble)(__m['width']);
  final BorderStyle style = uConst(BorderStyle.solid, _uBorderStyle)(__m['style']);
  return BorderSide(
    color: color,
    width: width,
    style: style,
  );
}

InputDecorationTheme _uInputDecorationTheme(Map<String, dynamic> __m) {
  final TextStyle? labelStyle = uNull<TextStyle>(uClass)(__m['labelStyle']);
  final TextStyle? floatingLabelStyle = uNull<TextStyle>(uClass)(__m['floatingLabelStyle']);
  final TextStyle? helperStyle = uNull<TextStyle>(uClass)(__m['helperStyle']);
  final int? helperMaxLines = uNull<int>(uInt)(__m['helperMaxLines']);
  final TextStyle? hintStyle = uNull<TextStyle>(uClass)(__m['hintStyle']);
  final TextStyle? errorStyle = uNull<TextStyle>(uClass)(__m['errorStyle']);
  final int? errorMaxLines = uNull<int>(uInt)(__m['errorMaxLines']);
  final FloatingLabelBehavior floatingLabelBehavior = uConst(FloatingLabelBehavior.auto, _uFloatingLabelBehavior)(__m['floatingLabelBehavior']);
  final bool isDense = uConst<bool>(false, uBool)(__m['isDense']);
  final EdgeInsetsGeometry? contentPadding = uNull<EdgeInsetsGeometry>(uClass)(__m['contentPadding']);
  final bool isCollapsed = uConst<bool>(false, uBool)(__m['isCollapsed']);
  final TextStyle? prefixStyle = uNull<TextStyle>(uClass)(__m['prefixStyle']);
  final TextStyle? suffixStyle = uNull<TextStyle>(uClass)(__m['suffixStyle']);
  final TextStyle? counterStyle = uNull<TextStyle>(uClass)(__m['counterStyle']);
  final bool filled = uConst<bool>(false, uBool)(__m['filled']);
  final Color? fillColor = uNull<Color>(uClass)(__m['fillColor']);
  final Color? focusColor = uNull<Color>(uClass)(__m['focusColor']);
  final Color? hoverColor = uNull<Color>(uClass)(__m['hoverColor']);
  final InputBorder? errorBorder = uNull<InputBorder>(uClass)(__m['errorBorder']);
  final InputBorder? focusedBorder = uNull<InputBorder>(uClass)(__m['focusedBorder']);
  final InputBorder? focusedErrorBorder = uNull<InputBorder>(uClass)(__m['focusedErrorBorder']);
  final InputBorder? disabledBorder = uNull<InputBorder>(uClass)(__m['disabledBorder']);
  final InputBorder? enabledBorder = uNull<InputBorder>(uClass)(__m['enabledBorder']);
  final InputBorder? border = uNull<InputBorder>(uClass)(__m['border']);
  final bool alignLabelWithHint = uConst<bool>(false, uBool)(__m['alignLabelWithHint']);
  final BoxConstraints? constraints = uNull<BoxConstraints>(uClass)(__m['constraints']);
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
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final double? opacity = uNull<double>(uDouble)(__m['opacity']);
  final double? size = uNull<double>(uDouble)(__m['size']);
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
  final double start = uDouble(__m['start']);
  final double end = uDouble(__m['end']);
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
  final double? trackHeight = uNull<double>(uDouble)(__m['trackHeight']);
  final Color? activeTrackColor = uNull<Color>(uClass)(__m['activeTrackColor']);
  final Color? inactiveTrackColor = uNull<Color>(uClass)(__m['inactiveTrackColor']);
  final Color? disabledActiveTrackColor = uNull<Color>(uClass)(__m['disabledActiveTrackColor']);
  final Color? disabledInactiveTrackColor = uNull<Color>(uClass)(__m['disabledInactiveTrackColor']);
  final Color? activeTickMarkColor = uNull<Color>(uClass)(__m['activeTickMarkColor']);
  final Color? inactiveTickMarkColor = uNull<Color>(uClass)(__m['inactiveTickMarkColor']);
  final Color? disabledActiveTickMarkColor = uNull<Color>(uClass)(__m['disabledActiveTickMarkColor']);
  final Color? disabledInactiveTickMarkColor = uNull<Color>(uClass)(__m['disabledInactiveTickMarkColor']);
  final Color? thumbColor = uNull<Color>(uClass)(__m['thumbColor']);
  final Color? overlappingShapeStrokeColor = uNull<Color>(uClass)(__m['overlappingShapeStrokeColor']);
  final Color? disabledThumbColor = uNull<Color>(uClass)(__m['disabledThumbColor']);
  final Color? overlayColor = uNull<Color>(uClass)(__m['overlayColor']);
  final Color? valueIndicatorColor = uNull<Color>(uClass)(__m['valueIndicatorColor']);
  final SliderComponentShape? overlayShape = uNull<SliderComponentShape>(uClass)(__m['overlayShape']);
  final SliderTickMarkShape? tickMarkShape = uNull<SliderTickMarkShape>(uClass)(__m['tickMarkShape']);
  final SliderComponentShape? thumbShape = uNull<SliderComponentShape>(uClass)(__m['thumbShape']);
  final SliderTrackShape? trackShape = uNull<SliderTrackShape>(uClass)(__m['trackShape']);
  final SliderComponentShape? valueIndicatorShape = uNull<SliderComponentShape>(uClass)(__m['valueIndicatorShape']);
  final RangeSliderTickMarkShape? rangeTickMarkShape = uNull<RangeSliderTickMarkShape>(uClass)(__m['rangeTickMarkShape']);
  final RangeSliderThumbShape? rangeThumbShape = uNull<RangeSliderThumbShape>(uClass)(__m['rangeThumbShape']);
  final RangeSliderTrackShape? rangeTrackShape = uNull<RangeSliderTrackShape>(uClass)(__m['rangeTrackShape']);
  final RangeSliderValueIndicatorShape? rangeValueIndicatorShape = uNull<RangeSliderValueIndicatorShape>(uClass)(__m['rangeValueIndicatorShape']);
  final ShowValueIndicator? showValueIndicator = uNull<ShowValueIndicator>(_uShowValueIndicator)(__m['showValueIndicator']);
  final TextStyle? valueIndicatorTextStyle = uNull<TextStyle>(uClass)(__m['valueIndicatorTextStyle']);
  final double? minThumbSeparation = uNull<double>(uDouble)(__m['minThumbSeparation']);
  final Thumb? Function(TextDirection, RangeValues, double, Size, Size, double)? thumbSelector = uNull<Thumb? Function(TextDirection, RangeValues, double, Size, Size, double)>(uFunc)(__m['thumbSelector']);
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
  final Color primaryColor = uClass(__m['primaryColor']);
  final Color primaryColorDark = uClass(__m['primaryColorDark']);
  final Color primaryColorLight = uClass(__m['primaryColorLight']);
  final TextStyle valueIndicatorTextStyle = uClass(__m['valueIndicatorTextStyle']);
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
  final Decoration? indicator = uNull<Decoration>(uClass)(__m['indicator']);
  final TabBarIndicatorSize? indicatorSize = uNull<TabBarIndicatorSize>(_uTabBarIndicatorSize)(__m['indicatorSize']);
  final Color? labelColor = uNull<Color>(uClass)(__m['labelColor']);
  final EdgeInsetsGeometry? labelPadding = uNull<EdgeInsetsGeometry>(uClass)(__m['labelPadding']);
  final TextStyle? labelStyle = uNull<TextStyle>(uClass)(__m['labelStyle']);
  final Color? unselectedLabelColor = uNull<Color>(uClass)(__m['unselectedLabelColor']);
  final TextStyle? unselectedLabelStyle = uNull<TextStyle>(uClass)(__m['unselectedLabelStyle']);
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
  final int days = uConst<int>(0, uInt)(__m['days']);
  final int hours = uConst<int>(0, uInt)(__m['hours']);
  final int minutes = uConst<int>(0, uInt)(__m['minutes']);
  final int seconds = uConst<int>(0, uInt)(__m['seconds']);
  final int milliseconds = uConst<int>(0, uInt)(__m['milliseconds']);
  final int microseconds = uConst<int>(0, uInt)(__m['microseconds']);
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
  final double? height = uNull<double>(uDouble)(__m['height']);
  final EdgeInsetsGeometry? padding = uNull<EdgeInsetsGeometry>(uClass)(__m['padding']);
  final EdgeInsetsGeometry? margin = uNull<EdgeInsetsGeometry>(uClass)(__m['margin']);
  final double? verticalOffset = uNull<double>(uDouble)(__m['verticalOffset']);
  final bool? preferBelow = uNull<bool>(uBool)(__m['preferBelow']);
  final bool? excludeFromSemantics = uNull<bool>(uBool)(__m['excludeFromSemantics']);
  final Decoration? decoration = uNull<Decoration>(uClass)(__m['decoration']);
  final TextStyle? textStyle = uNull<TextStyle>(uClass)(__m['textStyle']);
  final Duration? waitDuration = uNull<Duration>(uClass)(__m['waitDuration']);
  final Duration? showDuration = uNull<Duration>(uClass)(__m['showDuration']);
  final TooltipTriggerMode? triggerMode = uNull<TooltipTriggerMode>(_uTooltipTriggerMode)(__m['triggerMode']);
  final bool? enableFeedback = uNull<bool>(uBool)(__m['enableFeedback']);
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
  final Clip? clipBehavior = uNull<Clip>(_uClip)(__m['clipBehavior']);
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final Color? shadowColor = uNull<Color>(uClass)(__m['shadowColor']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final EdgeInsetsGeometry? margin = uNull<EdgeInsetsGeometry>(uClass)(__m['margin']);
  final ShapeBorder? shape = uNull<ShapeBorder>(uClass)(__m['shape']);
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
  final Color backgroundColor = uClass(__m['backgroundColor']);
  final Color? deleteIconColor = uNull<Color>(uClass)(__m['deleteIconColor']);
  final Color disabledColor = uClass(__m['disabledColor']);
  final Color selectedColor = uClass(__m['selectedColor']);
  final Color secondarySelectedColor = uClass(__m['secondarySelectedColor']);
  final Color? shadowColor = uNull<Color>(uClass)(__m['shadowColor']);
  final Color? selectedShadowColor = uNull<Color>(uClass)(__m['selectedShadowColor']);
  final bool? showCheckmark = uNull<bool>(uBool)(__m['showCheckmark']);
  final Color? checkmarkColor = uNull<Color>(uClass)(__m['checkmarkColor']);
  final EdgeInsetsGeometry? labelPadding = uNull<EdgeInsetsGeometry>(uClass)(__m['labelPadding']);
  final EdgeInsetsGeometry padding = uClass(__m['padding']);
  final BorderSide? side = uNull<BorderSide>(uClass)(__m['side']);
  final OutlinedBorder? shape = uNull<OutlinedBorder>(uClass)(__m['shape']);
  final TextStyle labelStyle = uClass(__m['labelStyle']);
  final TextStyle secondaryLabelStyle = uClass(__m['secondaryLabelStyle']);
  final Brightness brightness = _uBrightness(__m['brightness']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final double? pressElevation = uNull<double>(uDouble)(__m['pressElevation']);
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
  final Brightness? brightness = uNull<Brightness>(_uBrightness)(__m['brightness']);
  final Color? primaryColor = uNull<Color>(uClass)(__m['primaryColor']);
  final Color secondaryColor = uClass(__m['secondaryColor']);
  final TextStyle labelStyle = uClass(__m['labelStyle']);
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
  final Map<TargetPlatform, PageTransitionsBuilder> builders = uClass(__m['builders']);
  return PageTransitionsTheme(
    builders: builders,
  );
}

SystemUiOverlayStyle _uSystemUiOverlayStyle(Map<String, dynamic> __m) {
  final Color? systemNavigationBarColor = uNull<Color>(uClass)(__m['systemNavigationBarColor']);
  final Color? systemNavigationBarDividerColor = uNull<Color>(uClass)(__m['systemNavigationBarDividerColor']);
  final Brightness? systemNavigationBarIconBrightness = uNull<Brightness>(_uBrightness)(__m['systemNavigationBarIconBrightness']);
  final bool? systemNavigationBarContrastEnforced = uNull<bool>(uBool)(__m['systemNavigationBarContrastEnforced']);
  final Color? statusBarColor = uNull<Color>(uClass)(__m['statusBarColor']);
  final Brightness? statusBarBrightness = uNull<Brightness>(_uBrightness)(__m['statusBarBrightness']);
  final Brightness? statusBarIconBrightness = uNull<Brightness>(_uBrightness)(__m['statusBarIconBrightness']);
  final bool? systemStatusBarContrastEnforced = uNull<bool>(uBool)(__m['systemStatusBarContrastEnforced']);
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
  final Brightness? brightness = uNull<Brightness>(_uBrightness)(__m['brightness']);
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final Color? foregroundColor = uNull<Color>(uClass)(__m['foregroundColor']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final Color? shadowColor = uNull<Color>(uClass)(__m['shadowColor']);
  final ShapeBorder? shape = uNull<ShapeBorder>(uClass)(__m['shape']);
  final IconThemeData? iconTheme = uNull<IconThemeData>(uClass)(__m['iconTheme']);
  final IconThemeData? actionsIconTheme = uNull<IconThemeData>(uClass)(__m['actionsIconTheme']);
  final TextTheme? textTheme = uNull<TextTheme>(uClass)(__m['textTheme']);
  final bool? centerTitle = uNull<bool>(uBool)(__m['centerTitle']);
  final double? titleSpacing = uNull<double>(uDouble)(__m['titleSpacing']);
  final double? toolbarHeight = uNull<double>(uDouble)(__m['toolbarHeight']);
  final TextStyle? toolbarTextStyle = uNull<TextStyle>(uClass)(__m['toolbarTextStyle']);
  final TextStyle? titleTextStyle = uNull<TextStyle>(uClass)(__m['titleTextStyle']);
  final SystemUiOverlayStyle? systemOverlayStyle = uNull<SystemUiOverlayStyle>(uClass)(__m['systemOverlayStyle']);
  final bool? backwardsCompatibility = uNull<bool>(uBool)(__m['backwardsCompatibility']);
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
  final MaterialStateProperty<double?>? thickness = uNull<MaterialStateProperty<double?>>(uClass)(__m['thickness']);
  final bool? showTrackOnHover = uNull<bool>(uBool)(__m['showTrackOnHover']);
  final bool? isAlwaysShown = uNull<bool>(uBool)(__m['isAlwaysShown']);
  final Radius? radius = uNull<Radius>(uClass)(__m['radius']);
  final MaterialStateProperty<Color?>? thumbColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['thumbColor']);
  final MaterialStateProperty<Color?>? trackColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['trackColor']);
  final MaterialStateProperty<Color?>? trackBorderColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['trackBorderColor']);
  final double? crossAxisMargin = uNull<double>(uDouble)(__m['crossAxisMargin']);
  final double? mainAxisMargin = uNull<double>(uDouble)(__m['mainAxisMargin']);
  final double? minThumbLength = uNull<double>(uDouble)(__m['minThumbLength']);
  final bool? interactive = uNull<bool>(uBool)(__m['interactive']);
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
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final NotchedShape? shape = uNull<NotchedShape>(uClass)(__m['shape']);
  return BottomAppBarTheme(
    color: color,
    elevation: elevation,
    shape: shape,
  );
}

DialogTheme _uDialogTheme(Map<String, dynamic> __m) {
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final ShapeBorder? shape = uNull<ShapeBorder>(uClass)(__m['shape']);
  final TextStyle? titleTextStyle = uNull<TextStyle>(uClass)(__m['titleTextStyle']);
  final TextStyle? contentTextStyle = uNull<TextStyle>(uClass)(__m['contentTextStyle']);
  return DialogTheme(
    backgroundColor: backgroundColor,
    elevation: elevation,
    shape: shape,
    titleTextStyle: titleTextStyle,
    contentTextStyle: contentTextStyle,
  );
}

FloatingActionButtonThemeData _uFloatingActionButtonThemeData(Map<String, dynamic> __m) {
  final Color? foregroundColor = uNull<Color>(uClass)(__m['foregroundColor']);
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final Color? focusColor = uNull<Color>(uClass)(__m['focusColor']);
  final Color? hoverColor = uNull<Color>(uClass)(__m['hoverColor']);
  final Color? splashColor = uNull<Color>(uClass)(__m['splashColor']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final double? focusElevation = uNull<double>(uDouble)(__m['focusElevation']);
  final double? hoverElevation = uNull<double>(uDouble)(__m['hoverElevation']);
  final double? disabledElevation = uNull<double>(uDouble)(__m['disabledElevation']);
  final double? highlightElevation = uNull<double>(uDouble)(__m['highlightElevation']);
  final ShapeBorder? shape = uNull<ShapeBorder>(uClass)(__m['shape']);
  final bool? enableFeedback = uNull<bool>(uBool)(__m['enableFeedback']);
  final BoxConstraints? sizeConstraints = uNull<BoxConstraints>(uClass)(__m['sizeConstraints']);
  final BoxConstraints? smallSizeConstraints = uNull<BoxConstraints>(uClass)(__m['smallSizeConstraints']);
  final BoxConstraints? largeSizeConstraints = uNull<BoxConstraints>(uClass)(__m['largeSizeConstraints']);
  final BoxConstraints? extendedSizeConstraints = uNull<BoxConstraints>(uClass)(__m['extendedSizeConstraints']);
  final double? extendedIconLabelSpacing = uNull<double>(uDouble)(__m['extendedIconLabelSpacing']);
  final EdgeInsetsGeometry? extendedPadding = uNull<EdgeInsetsGeometry>(uClass)(__m['extendedPadding']);
  final TextStyle? extendedTextStyle = uNull<TextStyle>(uClass)(__m['extendedTextStyle']);
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
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final TextStyle? unselectedLabelTextStyle = uNull<TextStyle>(uClass)(__m['unselectedLabelTextStyle']);
  final TextStyle? selectedLabelTextStyle = uNull<TextStyle>(uClass)(__m['selectedLabelTextStyle']);
  final IconThemeData? unselectedIconTheme = uNull<IconThemeData>(uClass)(__m['unselectedIconTheme']);
  final IconThemeData? selectedIconTheme = uNull<IconThemeData>(uClass)(__m['selectedIconTheme']);
  final double? groupAlignment = uNull<double>(uDouble)(__m['groupAlignment']);
  final NavigationRailLabelType? labelType = uNull<NavigationRailLabelType>(_uNavigationRailLabelType)(__m['labelType']);
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
  final TargetPlatform? platform = uNull<TargetPlatform>(_uTargetPlatform)(__m['platform']);
  final TextTheme? black = uNull<TextTheme>(uClass)(__m['black']);
  final TextTheme? white = uNull<TextTheme>(uClass)(__m['white']);
  final TextTheme? englishLike = uNull<TextTheme>(uClass)(__m['englishLike']);
  final TextTheme? dense = uNull<TextTheme>(uClass)(__m['dense']);
  final TextTheme? tall = uNull<TextTheme>(uClass)(__m['tall']);
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
  final TargetPlatform? platform = uNull<TargetPlatform>(_uTargetPlatform)(__m['platform']);
  final TextTheme? black = uNull<TextTheme>(uClass)(__m['black']);
  final TextTheme? white = uNull<TextTheme>(uClass)(__m['white']);
  final TextTheme? englishLike = uNull<TextTheme>(uClass)(__m['englishLike']);
  final TextTheme? dense = uNull<TextTheme>(uClass)(__m['dense']);
  final TextTheme? tall = uNull<TextTheme>(uClass)(__m['tall']);
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
  final TargetPlatform? platform = uNull<TargetPlatform>(_uTargetPlatform)(__m['platform']);
  final TextTheme? black = uNull<TextTheme>(uClass)(__m['black']);
  final TextTheme? white = uNull<TextTheme>(uClass)(__m['white']);
  final TextTheme? englishLike = uNull<TextTheme>(uClass)(__m['englishLike']);
  final TextTheme? dense = uNull<TextTheme>(uClass)(__m['dense']);
  final TextTheme? tall = uNull<TextTheme>(uClass)(__m['tall']);
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
  final Color primaryColor = uClass(__m['primaryColor']);
  final TextStyle? textStyle = uNull<TextStyle>(uClass)(__m['textStyle']);
  final TextStyle? actionTextStyle = uNull<TextStyle>(uClass)(__m['actionTextStyle']);
  final TextStyle? tabLabelTextStyle = uNull<TextStyle>(uClass)(__m['tabLabelTextStyle']);
  final TextStyle? navTitleTextStyle = uNull<TextStyle>(uClass)(__m['navTitleTextStyle']);
  final TextStyle? navLargeTitleTextStyle = uNull<TextStyle>(uClass)(__m['navLargeTitleTextStyle']);
  final TextStyle? navActionTextStyle = uNull<TextStyle>(uClass)(__m['navActionTextStyle']);
  final TextStyle? pickerTextStyle = uNull<TextStyle>(uClass)(__m['pickerTextStyle']);
  final TextStyle? dateTimePickerTextStyle = uNull<TextStyle>(uClass)(__m['dateTimePickerTextStyle']);
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
  final Brightness? brightness = uNull<Brightness>(_uBrightness)(__m['brightness']);
  final Color? primaryColor = uNull<Color>(uClass)(__m['primaryColor']);
  final Color? primaryContrastingColor = uNull<Color>(uClass)(__m['primaryContrastingColor']);
  final CupertinoTextThemeData? textTheme = uNull<CupertinoTextThemeData>(uClass)(__m['textTheme']);
  final Color? barBackgroundColor = uNull<Color>(uClass)(__m['barBackgroundColor']);
  final Color? scaffoldBackgroundColor = uNull<Color>(uClass)(__m['scaffoldBackgroundColor']);
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
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final Color? actionTextColor = uNull<Color>(uClass)(__m['actionTextColor']);
  final Color? disabledActionTextColor = uNull<Color>(uClass)(__m['disabledActionTextColor']);
  final TextStyle? contentTextStyle = uNull<TextStyle>(uClass)(__m['contentTextStyle']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final ShapeBorder? shape = uNull<ShapeBorder>(uClass)(__m['shape']);
  final SnackBarBehavior? behavior = uNull<SnackBarBehavior>(_uSnackBarBehavior)(__m['behavior']);
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
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final Color? modalBackgroundColor = uNull<Color>(uClass)(__m['modalBackgroundColor']);
  final double? modalElevation = uNull<double>(uDouble)(__m['modalElevation']);
  final ShapeBorder? shape = uNull<ShapeBorder>(uClass)(__m['shape']);
  final Clip? clipBehavior = uNull<Clip>(_uClip)(__m['clipBehavior']);
  final BoxConstraints? constraints = uNull<BoxConstraints>(uClass)(__m['constraints']);
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
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final ShapeBorder? shape = uNull<ShapeBorder>(uClass)(__m['shape']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final TextStyle? textStyle = uNull<TextStyle>(uClass)(__m['textStyle']);
  final bool? enableFeedback = uNull<bool>(uBool)(__m['enableFeedback']);
  return PopupMenuThemeData(
    color: color,
    shape: shape,
    elevation: elevation,
    textStyle: textStyle,
    enableFeedback: enableFeedback,
  );
}

MaterialBannerThemeData _uMaterialBannerThemeData(Map<String, dynamic> __m) {
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final TextStyle? contentTextStyle = uNull<TextStyle>(uClass)(__m['contentTextStyle']);
  final EdgeInsetsGeometry? padding = uNull<EdgeInsetsGeometry>(uClass)(__m['padding']);
  final EdgeInsetsGeometry? leadingPadding = uNull<EdgeInsetsGeometry>(uClass)(__m['leadingPadding']);
  return MaterialBannerThemeData(
    backgroundColor: backgroundColor,
    contentTextStyle: contentTextStyle,
    padding: padding,
    leadingPadding: leadingPadding,
  );
}

DividerThemeData _uDividerThemeData(Map<String, dynamic> __m) {
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final double? space = uNull<double>(uDouble)(__m['space']);
  final double? thickness = uNull<double>(uDouble)(__m['thickness']);
  final double? indent = uNull<double>(uDouble)(__m['indent']);
  final double? endIndent = uNull<double>(uDouble)(__m['endIndent']);
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
  final MainAxisAlignment? alignment = uNull<MainAxisAlignment>(_uMainAxisAlignment)(__m['alignment']);
  final MainAxisSize? mainAxisSize = uNull<MainAxisSize>(_uMainAxisSize)(__m['mainAxisSize']);
  final ButtonTextTheme? buttonTextTheme = uNull<ButtonTextTheme>(_uButtonTextTheme)(__m['buttonTextTheme']);
  final double? buttonMinWidth = uNull<double>(uDouble)(__m['buttonMinWidth']);
  final double? buttonHeight = uNull<double>(uDouble)(__m['buttonHeight']);
  final EdgeInsetsGeometry? buttonPadding = uNull<EdgeInsetsGeometry>(uClass)(__m['buttonPadding']);
  final bool? buttonAlignedDropdown = uNull<bool>(uBool)(__m['buttonAlignedDropdown']);
  final ButtonBarLayoutBehavior? layoutBehavior = uNull<ButtonBarLayoutBehavior>(_uButtonBarLayoutBehavior)(__m['layoutBehavior']);
  final VerticalDirection? overflowDirection = uNull<VerticalDirection>(_uVerticalDirection)(__m['overflowDirection']);
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
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final double? elevation = uNull<double>(uDouble)(__m['elevation']);
  final IconThemeData? selectedIconTheme = uNull<IconThemeData>(uClass)(__m['selectedIconTheme']);
  final IconThemeData? unselectedIconTheme = uNull<IconThemeData>(uClass)(__m['unselectedIconTheme']);
  final Color? selectedItemColor = uNull<Color>(uClass)(__m['selectedItemColor']);
  final Color? unselectedItemColor = uNull<Color>(uClass)(__m['unselectedItemColor']);
  final TextStyle? selectedLabelStyle = uNull<TextStyle>(uClass)(__m['selectedLabelStyle']);
  final TextStyle? unselectedLabelStyle = uNull<TextStyle>(uClass)(__m['unselectedLabelStyle']);
  final bool? showSelectedLabels = uNull<bool>(uBool)(__m['showSelectedLabels']);
  final bool? showUnselectedLabels = uNull<bool>(uBool)(__m['showUnselectedLabels']);
  final BottomNavigationBarType? type = uNull<BottomNavigationBarType>(_uBottomNavigationBarType)(__m['type']);
  final bool? enableFeedback = uNull<bool>(uBool)(__m['enableFeedback']);
  final BottomNavigationBarLandscapeLayout? landscapeLayout = uNull<BottomNavigationBarLandscapeLayout>(_uBottomNavigationBarLandscapeLayout)(__m['landscapeLayout']);
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
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final Color? hourMinuteTextColor = uNull<Color>(uClass)(__m['hourMinuteTextColor']);
  final Color? hourMinuteColor = uNull<Color>(uClass)(__m['hourMinuteColor']);
  final Color? dayPeriodTextColor = uNull<Color>(uClass)(__m['dayPeriodTextColor']);
  final Color? dayPeriodColor = uNull<Color>(uClass)(__m['dayPeriodColor']);
  final Color? dialHandColor = uNull<Color>(uClass)(__m['dialHandColor']);
  final Color? dialBackgroundColor = uNull<Color>(uClass)(__m['dialBackgroundColor']);
  final Color? dialTextColor = uNull<Color>(uClass)(__m['dialTextColor']);
  final Color? entryModeIconColor = uNull<Color>(uClass)(__m['entryModeIconColor']);
  final TextStyle? hourMinuteTextStyle = uNull<TextStyle>(uClass)(__m['hourMinuteTextStyle']);
  final TextStyle? dayPeriodTextStyle = uNull<TextStyle>(uClass)(__m['dayPeriodTextStyle']);
  final TextStyle? helpTextStyle = uNull<TextStyle>(uClass)(__m['helpTextStyle']);
  final ShapeBorder? shape = uNull<ShapeBorder>(uClass)(__m['shape']);
  final ShapeBorder? hourMinuteShape = uNull<ShapeBorder>(uClass)(__m['hourMinuteShape']);
  final OutlinedBorder? dayPeriodShape = uNull<OutlinedBorder>(uClass)(__m['dayPeriodShape']);
  final BorderSide? dayPeriodBorderSide = uNull<BorderSide>(uClass)(__m['dayPeriodBorderSide']);
  final InputDecorationTheme? inputDecorationTheme = uNull<InputDecorationTheme>(uClass)(__m['inputDecorationTheme']);
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
  final MaterialStateProperty<TextStyle?>? textStyle = uNull<MaterialStateProperty<TextStyle?>>(uClass)(__m['textStyle']);
  final MaterialStateProperty<Color?>? backgroundColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['backgroundColor']);
  final MaterialStateProperty<Color?>? foregroundColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['foregroundColor']);
  final MaterialStateProperty<Color?>? overlayColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['overlayColor']);
  final MaterialStateProperty<Color?>? shadowColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['shadowColor']);
  final MaterialStateProperty<double?>? elevation = uNull<MaterialStateProperty<double?>>(uClass)(__m['elevation']);
  final MaterialStateProperty<EdgeInsetsGeometry?>? padding = uNull<MaterialStateProperty<EdgeInsetsGeometry?>>(uClass)(__m['padding']);
  final MaterialStateProperty<Size?>? minimumSize = uNull<MaterialStateProperty<Size?>>(uClass)(__m['minimumSize']);
  final MaterialStateProperty<Size?>? fixedSize = uNull<MaterialStateProperty<Size?>>(uClass)(__m['fixedSize']);
  final MaterialStateProperty<Size?>? maximumSize = uNull<MaterialStateProperty<Size?>>(uClass)(__m['maximumSize']);
  final MaterialStateProperty<BorderSide?>? side = uNull<MaterialStateProperty<BorderSide?>>(uClass)(__m['side']);
  final MaterialStateProperty<OutlinedBorder?>? shape = uNull<MaterialStateProperty<OutlinedBorder?>>(uClass)(__m['shape']);
  final MaterialStateProperty<MouseCursor?>? mouseCursor = uNull<MaterialStateProperty<MouseCursor?>>(uClass)(__m['mouseCursor']);
  final VisualDensity? visualDensity = uNull<VisualDensity>(uClass)(__m['visualDensity']);
  final MaterialTapTargetSize? tapTargetSize = uNull<MaterialTapTargetSize>(_uMaterialTapTargetSize)(__m['tapTargetSize']);
  final Duration? animationDuration = uNull<Duration>(uClass)(__m['animationDuration']);
  final bool? enableFeedback = uNull<bool>(uBool)(__m['enableFeedback']);
  final AlignmentGeometry? alignment = uNull<AlignmentGeometry>(uClass)(__m['alignment']);
  final InteractiveInkFeatureFactory? splashFactory = uNull<InteractiveInkFeatureFactory>(uClass)(__m['splashFactory']);
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
  final ButtonStyle? style = uNull<ButtonStyle>(uClass)(__m['style']);
  return TextButtonThemeData(
    style: style,
  );
}

ElevatedButtonThemeData _uElevatedButtonThemeData(Map<String, dynamic> __m) {
  final ButtonStyle? style = uNull<ButtonStyle>(uClass)(__m['style']);
  return ElevatedButtonThemeData(
    style: style,
  );
}

OutlinedButtonThemeData _uOutlinedButtonThemeData(Map<String, dynamic> __m) {
  final ButtonStyle? style = uNull<ButtonStyle>(uClass)(__m['style']);
  return OutlinedButtonThemeData(
    style: style,
  );
}

TextSelectionThemeData _uTextSelectionThemeData(Map<String, dynamic> __m) {
  final Color? cursorColor = uNull<Color>(uClass)(__m['cursorColor']);
  final Color? selectionColor = uNull<Color>(uClass)(__m['selectionColor']);
  final Color? selectionHandleColor = uNull<Color>(uClass)(__m['selectionHandleColor']);
  return TextSelectionThemeData(
    cursorColor: cursorColor,
    selectionColor: selectionColor,
    selectionHandleColor: selectionHandleColor,
  );
}

DataTableThemeData _uDataTableThemeData(Map<String, dynamic> __m) {
  final Decoration? decoration = uNull<Decoration>(uClass)(__m['decoration']);
  final MaterialStateProperty<Color?>? dataRowColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['dataRowColor']);
  final double? dataRowHeight = uNull<double>(uDouble)(__m['dataRowHeight']);
  final TextStyle? dataTextStyle = uNull<TextStyle>(uClass)(__m['dataTextStyle']);
  final MaterialStateProperty<Color?>? headingRowColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['headingRowColor']);
  final double? headingRowHeight = uNull<double>(uDouble)(__m['headingRowHeight']);
  final TextStyle? headingTextStyle = uNull<TextStyle>(uClass)(__m['headingTextStyle']);
  final double? horizontalMargin = uNull<double>(uDouble)(__m['horizontalMargin']);
  final double? columnSpacing = uNull<double>(uDouble)(__m['columnSpacing']);
  final double? dividerThickness = uNull<double>(uDouble)(__m['dividerThickness']);
  final double? checkboxHorizontalMargin = uNull<double>(uDouble)(__m['checkboxHorizontalMargin']);
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
  final MaterialStateProperty<MouseCursor?>? mouseCursor = uNull<MaterialStateProperty<MouseCursor?>>(uClass)(__m['mouseCursor']);
  final MaterialStateProperty<Color?>? fillColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['fillColor']);
  final MaterialStateProperty<Color?>? checkColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['checkColor']);
  final MaterialStateProperty<Color?>? overlayColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['overlayColor']);
  final double? splashRadius = uNull<double>(uDouble)(__m['splashRadius']);
  final MaterialTapTargetSize? materialTapTargetSize = uNull<MaterialTapTargetSize>(_uMaterialTapTargetSize)(__m['materialTapTargetSize']);
  final VisualDensity? visualDensity = uNull<VisualDensity>(uClass)(__m['visualDensity']);
  final OutlinedBorder? shape = uNull<OutlinedBorder>(uClass)(__m['shape']);
  final BorderSide? side = uNull<BorderSide>(uClass)(__m['side']);
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
  final MaterialStateProperty<MouseCursor?>? mouseCursor = uNull<MaterialStateProperty<MouseCursor?>>(uClass)(__m['mouseCursor']);
  final MaterialStateProperty<Color?>? fillColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['fillColor']);
  final MaterialStateProperty<Color?>? overlayColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['overlayColor']);
  final double? splashRadius = uNull<double>(uDouble)(__m['splashRadius']);
  final MaterialTapTargetSize? materialTapTargetSize = uNull<MaterialTapTargetSize>(_uMaterialTapTargetSize)(__m['materialTapTargetSize']);
  final VisualDensity? visualDensity = uNull<VisualDensity>(uClass)(__m['visualDensity']);
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
  final MaterialStateProperty<Color?>? thumbColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['thumbColor']);
  final MaterialStateProperty<Color?>? trackColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['trackColor']);
  final MaterialTapTargetSize? materialTapTargetSize = uNull<MaterialTapTargetSize>(_uMaterialTapTargetSize)(__m['materialTapTargetSize']);
  final MaterialStateProperty<MouseCursor?>? mouseCursor = uNull<MaterialStateProperty<MouseCursor?>>(uClass)(__m['mouseCursor']);
  final MaterialStateProperty<Color?>? overlayColor = uNull<MaterialStateProperty<Color?>>(uClass)(__m['overlayColor']);
  final double? splashRadius = uNull<double>(uDouble)(__m['splashRadius']);
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
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final Color? linearTrackColor = uNull<Color>(uClass)(__m['linearTrackColor']);
  final double? linearMinHeight = uNull<double>(uDouble)(__m['linearMinHeight']);
  final Color? circularTrackColor = uNull<Color>(uClass)(__m['circularTrackColor']);
  final Color? refreshBackgroundColor = uNull<Color>(uClass)(__m['refreshBackgroundColor']);
  return ProgressIndicatorThemeData(
    color: color,
    linearTrackColor: linearTrackColor,
    linearMinHeight: linearMinHeight,
    circularTrackColor: circularTrackColor,
    refreshBackgroundColor: refreshBackgroundColor,
  );
}

ThemeData _uThemeData(Map<String, dynamic> __m) {
  final Brightness? brightness = uNull<Brightness>(_uBrightness)(__m['brightness']);
  final VisualDensity? visualDensity = uNull<VisualDensity>(uClass)(__m['visualDensity']);
  final MaterialColor? primarySwatch = uNull<MaterialColor>(uClass)(__m['primarySwatch']);
  final Color? primaryColor = uNull<Color>(uClass)(__m['primaryColor']);
  final Brightness? primaryColorBrightness = uNull<Brightness>(_uBrightness)(__m['primaryColorBrightness']);
  final Color? primaryColorLight = uNull<Color>(uClass)(__m['primaryColorLight']);
  final Color? primaryColorDark = uNull<Color>(uClass)(__m['primaryColorDark']);
  final Color? accentColor = uNull<Color>(uClass)(__m['accentColor']);
  final Brightness? accentColorBrightness = uNull<Brightness>(_uBrightness)(__m['accentColorBrightness']);
  final Color? canvasColor = uNull<Color>(uClass)(__m['canvasColor']);
  final Color? shadowColor = uNull<Color>(uClass)(__m['shadowColor']);
  final Color? scaffoldBackgroundColor = uNull<Color>(uClass)(__m['scaffoldBackgroundColor']);
  final Color? bottomAppBarColor = uNull<Color>(uClass)(__m['bottomAppBarColor']);
  final Color? cardColor = uNull<Color>(uClass)(__m['cardColor']);
  final Color? dividerColor = uNull<Color>(uClass)(__m['dividerColor']);
  final Color? focusColor = uNull<Color>(uClass)(__m['focusColor']);
  final Color? hoverColor = uNull<Color>(uClass)(__m['hoverColor']);
  final Color? highlightColor = uNull<Color>(uClass)(__m['highlightColor']);
  final Color? splashColor = uNull<Color>(uClass)(__m['splashColor']);
  final InteractiveInkFeatureFactory? splashFactory = uNull<InteractiveInkFeatureFactory>(uClass)(__m['splashFactory']);
  final Color? selectedRowColor = uNull<Color>(uClass)(__m['selectedRowColor']);
  final Color? unselectedWidgetColor = uNull<Color>(uClass)(__m['unselectedWidgetColor']);
  final Color? disabledColor = uNull<Color>(uClass)(__m['disabledColor']);
  final Color? buttonColor = uNull<Color>(uClass)(__m['buttonColor']);
  final ButtonThemeData? buttonTheme = uNull<ButtonThemeData>(uClass)(__m['buttonTheme']);
  final ToggleButtonsThemeData? toggleButtonsTheme = uNull<ToggleButtonsThemeData>(uClass)(__m['toggleButtonsTheme']);
  final Color? secondaryHeaderColor = uNull<Color>(uClass)(__m['secondaryHeaderColor']);
  final Color? textSelectionColor = uNull<Color>(uClass)(__m['textSelectionColor']);
  final Color? cursorColor = uNull<Color>(uClass)(__m['cursorColor']);
  final Color? textSelectionHandleColor = uNull<Color>(uClass)(__m['textSelectionHandleColor']);
  final Color? backgroundColor = uNull<Color>(uClass)(__m['backgroundColor']);
  final Color? dialogBackgroundColor = uNull<Color>(uClass)(__m['dialogBackgroundColor']);
  final Color? indicatorColor = uNull<Color>(uClass)(__m['indicatorColor']);
  final Color? hintColor = uNull<Color>(uClass)(__m['hintColor']);
  final Color? errorColor = uNull<Color>(uClass)(__m['errorColor']);
  final Color? toggleableActiveColor = uNull<Color>(uClass)(__m['toggleableActiveColor']);
  final String? fontFamily = uNull<String>(uString)(__m['fontFamily']);
  final TextTheme? textTheme = uNull<TextTheme>(uClass)(__m['textTheme']);
  final TextTheme? primaryTextTheme = uNull<TextTheme>(uClass)(__m['primaryTextTheme']);
  final TextTheme? accentTextTheme = uNull<TextTheme>(uClass)(__m['accentTextTheme']);
  final InputDecorationTheme? inputDecorationTheme = uNull<InputDecorationTheme>(uClass)(__m['inputDecorationTheme']);
  final IconThemeData? iconTheme = uNull<IconThemeData>(uClass)(__m['iconTheme']);
  final IconThemeData? primaryIconTheme = uNull<IconThemeData>(uClass)(__m['primaryIconTheme']);
  final IconThemeData? accentIconTheme = uNull<IconThemeData>(uClass)(__m['accentIconTheme']);
  final SliderThemeData? sliderTheme = uNull<SliderThemeData>(uClass)(__m['sliderTheme']);
  final TabBarTheme? tabBarTheme = uNull<TabBarTheme>(uClass)(__m['tabBarTheme']);
  final TooltipThemeData? tooltipTheme = uNull<TooltipThemeData>(uClass)(__m['tooltipTheme']);
  final CardTheme? cardTheme = uNull<CardTheme>(uClass)(__m['cardTheme']);
  final ChipThemeData? chipTheme = uNull<ChipThemeData>(uClass)(__m['chipTheme']);
  final TargetPlatform? platform = uNull<TargetPlatform>(_uTargetPlatform)(__m['platform']);
  final MaterialTapTargetSize? materialTapTargetSize = uNull<MaterialTapTargetSize>(_uMaterialTapTargetSize)(__m['materialTapTargetSize']);
  final bool? applyElevationOverlayColor = uNull<bool>(uBool)(__m['applyElevationOverlayColor']);
  final PageTransitionsTheme? pageTransitionsTheme = uNull<PageTransitionsTheme>(uClass)(__m['pageTransitionsTheme']);
  final AppBarTheme? appBarTheme = uNull<AppBarTheme>(uClass)(__m['appBarTheme']);
  final ScrollbarThemeData? scrollbarTheme = uNull<ScrollbarThemeData>(uClass)(__m['scrollbarTheme']);
  final BottomAppBarTheme? bottomAppBarTheme = uNull<BottomAppBarTheme>(uClass)(__m['bottomAppBarTheme']);
  final ColorScheme? colorScheme = uNull<ColorScheme>(uClass)(__m['colorScheme']);
  final DialogTheme? dialogTheme = uNull<DialogTheme>(uClass)(__m['dialogTheme']);
  final FloatingActionButtonThemeData? floatingActionButtonTheme = uNull<FloatingActionButtonThemeData>(uClass)(__m['floatingActionButtonTheme']);
  final NavigationRailThemeData? navigationRailTheme = uNull<NavigationRailThemeData>(uClass)(__m['navigationRailTheme']);
  final Typography? typography = uNull<Typography>(uClass)(__m['typography']);
  final NoDefaultCupertinoThemeData? cupertinoOverrideTheme = uNull<NoDefaultCupertinoThemeData>(uClass)(__m['cupertinoOverrideTheme']);
  final SnackBarThemeData? snackBarTheme = uNull<SnackBarThemeData>(uClass)(__m['snackBarTheme']);
  final BottomSheetThemeData? bottomSheetTheme = uNull<BottomSheetThemeData>(uClass)(__m['bottomSheetTheme']);
  final PopupMenuThemeData? popupMenuTheme = uNull<PopupMenuThemeData>(uClass)(__m['popupMenuTheme']);
  final MaterialBannerThemeData? bannerTheme = uNull<MaterialBannerThemeData>(uClass)(__m['bannerTheme']);
  final DividerThemeData? dividerTheme = uNull<DividerThemeData>(uClass)(__m['dividerTheme']);
  final ButtonBarThemeData? buttonBarTheme = uNull<ButtonBarThemeData>(uClass)(__m['buttonBarTheme']);
  final BottomNavigationBarThemeData? bottomNavigationBarTheme = uNull<BottomNavigationBarThemeData>(uClass)(__m['bottomNavigationBarTheme']);
  final TimePickerThemeData? timePickerTheme = uNull<TimePickerThemeData>(uClass)(__m['timePickerTheme']);
  final TextButtonThemeData? textButtonTheme = uNull<TextButtonThemeData>(uClass)(__m['textButtonTheme']);
  final ElevatedButtonThemeData? elevatedButtonTheme = uNull<ElevatedButtonThemeData>(uClass)(__m['elevatedButtonTheme']);
  final OutlinedButtonThemeData? outlinedButtonTheme = uNull<OutlinedButtonThemeData>(uClass)(__m['outlinedButtonTheme']);
  final TextSelectionThemeData? textSelectionTheme = uNull<TextSelectionThemeData>(uClass)(__m['textSelectionTheme']);
  final DataTableThemeData? dataTableTheme = uNull<DataTableThemeData>(uClass)(__m['dataTableTheme']);
  final CheckboxThemeData? checkboxTheme = uNull<CheckboxThemeData>(uClass)(__m['checkboxTheme']);
  final RadioThemeData? radioTheme = uNull<RadioThemeData>(uClass)(__m['radioTheme']);
  final SwitchThemeData? switchTheme = uNull<SwitchThemeData>(uClass)(__m['switchTheme']);
  final ProgressIndicatorThemeData? progressIndicatorTheme = uNull<ProgressIndicatorThemeData>(uClass)(__m['progressIndicatorTheme']);
  final bool? fixTextFieldOutlineLabel = uNull<bool>(uBool)(__m['fixTextFieldOutlineLabel']);
  final bool? useTextSelectionTheme = uNull<bool>(uBool)(__m['useTextSelectionTheme']);
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
  final VisualDensity visualDensity = uClass(__m['visualDensity']);
  final Color primaryColor = uClass(__m['primaryColor']);
  final Brightness primaryColorBrightness = _uBrightness(__m['primaryColorBrightness']);
  final Color primaryColorLight = uClass(__m['primaryColorLight']);
  final Color primaryColorDark = uClass(__m['primaryColorDark']);
  final Color canvasColor = uClass(__m['canvasColor']);
  final Color shadowColor = uClass(__m['shadowColor']);
  final Color accentColor = uClass(__m['accentColor']);
  final Brightness accentColorBrightness = _uBrightness(__m['accentColorBrightness']);
  final Color scaffoldBackgroundColor = uClass(__m['scaffoldBackgroundColor']);
  final Color bottomAppBarColor = uClass(__m['bottomAppBarColor']);
  final Color cardColor = uClass(__m['cardColor']);
  final Color dividerColor = uClass(__m['dividerColor']);
  final Color focusColor = uClass(__m['focusColor']);
  final Color hoverColor = uClass(__m['hoverColor']);
  final Color highlightColor = uClass(__m['highlightColor']);
  final Color splashColor = uClass(__m['splashColor']);
  final InteractiveInkFeatureFactory splashFactory = uClass(__m['splashFactory']);
  final Color selectedRowColor = uClass(__m['selectedRowColor']);
  final Color unselectedWidgetColor = uClass(__m['unselectedWidgetColor']);
  final Color disabledColor = uClass(__m['disabledColor']);
  final ButtonThemeData buttonTheme = uClass(__m['buttonTheme']);
  final Color buttonColor = uClass(__m['buttonColor']);
  final ToggleButtonsThemeData toggleButtonsTheme = uClass(__m['toggleButtonsTheme']);
  final Color secondaryHeaderColor = uClass(__m['secondaryHeaderColor']);
  final Color textSelectionColor = uClass(__m['textSelectionColor']);
  final Color cursorColor = uClass(__m['cursorColor']);
  final Color textSelectionHandleColor = uClass(__m['textSelectionHandleColor']);
  final Color backgroundColor = uClass(__m['backgroundColor']);
  final Color dialogBackgroundColor = uClass(__m['dialogBackgroundColor']);
  final Color indicatorColor = uClass(__m['indicatorColor']);
  final Color hintColor = uClass(__m['hintColor']);
  final Color errorColor = uClass(__m['errorColor']);
  final Color toggleableActiveColor = uClass(__m['toggleableActiveColor']);
  final TextTheme textTheme = uClass(__m['textTheme']);
  final TextTheme primaryTextTheme = uClass(__m['primaryTextTheme']);
  final TextTheme accentTextTheme = uClass(__m['accentTextTheme']);
  final InputDecorationTheme inputDecorationTheme = uClass(__m['inputDecorationTheme']);
  final IconThemeData iconTheme = uClass(__m['iconTheme']);
  final IconThemeData primaryIconTheme = uClass(__m['primaryIconTheme']);
  final IconThemeData accentIconTheme = uClass(__m['accentIconTheme']);
  final SliderThemeData sliderTheme = uClass(__m['sliderTheme']);
  final TabBarTheme tabBarTheme = uClass(__m['tabBarTheme']);
  final TooltipThemeData tooltipTheme = uClass(__m['tooltipTheme']);
  final CardTheme cardTheme = uClass(__m['cardTheme']);
  final ChipThemeData chipTheme = uClass(__m['chipTheme']);
  final TargetPlatform platform = _uTargetPlatform(__m['platform']);
  final MaterialTapTargetSize materialTapTargetSize = _uMaterialTapTargetSize(__m['materialTapTargetSize']);
  final bool applyElevationOverlayColor = uBool(__m['applyElevationOverlayColor']);
  final PageTransitionsTheme pageTransitionsTheme = uClass(__m['pageTransitionsTheme']);
  final AppBarTheme appBarTheme = uClass(__m['appBarTheme']);
  final ScrollbarThemeData scrollbarTheme = uClass(__m['scrollbarTheme']);
  final BottomAppBarTheme bottomAppBarTheme = uClass(__m['bottomAppBarTheme']);
  final ColorScheme colorScheme = uClass(__m['colorScheme']);
  final DialogTheme dialogTheme = uClass(__m['dialogTheme']);
  final FloatingActionButtonThemeData floatingActionButtonTheme = uClass(__m['floatingActionButtonTheme']);
  final NavigationRailThemeData navigationRailTheme = uClass(__m['navigationRailTheme']);
  final Typography typography = uClass(__m['typography']);
  final NoDefaultCupertinoThemeData? cupertinoOverrideTheme = uNull<NoDefaultCupertinoThemeData>(uClass)(__m['cupertinoOverrideTheme']);
  final SnackBarThemeData snackBarTheme = uClass(__m['snackBarTheme']);
  final BottomSheetThemeData bottomSheetTheme = uClass(__m['bottomSheetTheme']);
  final PopupMenuThemeData popupMenuTheme = uClass(__m['popupMenuTheme']);
  final MaterialBannerThemeData bannerTheme = uClass(__m['bannerTheme']);
  final DividerThemeData dividerTheme = uClass(__m['dividerTheme']);
  final ButtonBarThemeData buttonBarTheme = uClass(__m['buttonBarTheme']);
  final BottomNavigationBarThemeData bottomNavigationBarTheme = uClass(__m['bottomNavigationBarTheme']);
  final TimePickerThemeData timePickerTheme = uClass(__m['timePickerTheme']);
  final TextButtonThemeData textButtonTheme = uClass(__m['textButtonTheme']);
  final ElevatedButtonThemeData elevatedButtonTheme = uClass(__m['elevatedButtonTheme']);
  final OutlinedButtonThemeData outlinedButtonTheme = uClass(__m['outlinedButtonTheme']);
  final TextSelectionThemeData textSelectionTheme = uClass(__m['textSelectionTheme']);
  final DataTableThemeData dataTableTheme = uClass(__m['dataTableTheme']);
  final CheckboxThemeData checkboxTheme = uClass(__m['checkboxTheme']);
  final RadioThemeData radioTheme = uClass(__m['radioTheme']);
  final SwitchThemeData switchTheme = uClass(__m['switchTheme']);
  final ProgressIndicatorThemeData progressIndicatorTheme = uClass(__m['progressIndicatorTheme']);
  final bool fixTextFieldOutlineLabel = uBool(__m['fixTextFieldOutlineLabel']);
  final bool useTextSelectionTheme = uBool(__m['useTextSelectionTheme']);
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
  final ColorScheme colorScheme = uClass(__m['colorScheme']);
  final TextTheme? textTheme = uNull<TextTheme>(uClass)(__m['textTheme']);
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
  final String? location = uNull<String>(uString)(__m['location']);
  final Object? state = uNull<Object>(uClass)(__m['state']);
  return RouteInformation(
    location: location,
    state: state,
  );
}

MaterialApp _uMaterialApp(Map<String, dynamic> __m) {
  final Key? key = uNull<Key>(uClass)(__m['key']);
  final GlobalKey<NavigatorState>? navigatorKey = uNull<GlobalKey<NavigatorState>>(uClass)(__m['navigatorKey']);
  final GlobalKey<ScaffoldMessengerState>? scaffoldMessengerKey = uNull<GlobalKey<ScaffoldMessengerState>>(uClass)(__m['scaffoldMessengerKey']);
  final Widget? home = uNull<Widget>(uClass)(__m['home']);
  final Map<String, Widget Function(BuildContext)> routes = uConst(<String, Widget Function(BuildContext)>{}, uClass)(__m['routes']);
  final String? initialRoute = uNull<String>(uString)(__m['initialRoute']);
  final Route<dynamic>? Function(RouteSettings)? onGenerateRoute = uNull<Route<dynamic>? Function(RouteSettings)>(uFunc)(__m['onGenerateRoute']);
  final List<Route<dynamic>> Function(String)? onGenerateInitialRoutes = uNull<List<Route<dynamic>> Function(String)>(uFunc)(__m['onGenerateInitialRoutes']);
  final Route<dynamic>? Function(RouteSettings)? onUnknownRoute = uNull<Route<dynamic>? Function(RouteSettings)>(uFunc)(__m['onUnknownRoute']);
  final List<NavigatorObserver> navigatorObservers = uConst(<NavigatorObserver>[], uList<NavigatorObserver>(uClass))(__m['navigatorObservers']);
  final Widget Function(BuildContext, Widget?)? builder = uNull<Widget Function(BuildContext, Widget?)>(uFunc)(__m['builder']);
  final String title = uConst<String>('', uString)(__m['title']);
  final String Function(BuildContext)? onGenerateTitle = uNull<String Function(BuildContext)>(uFunc)(__m['onGenerateTitle']);
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final ThemeData? theme = uNull<ThemeData>(uClass)(__m['theme']);
  final ThemeData? darkTheme = uNull<ThemeData>(uClass)(__m['darkTheme']);
  final ThemeData? highContrastTheme = uNull<ThemeData>(uClass)(__m['highContrastTheme']);
  final ThemeData? highContrastDarkTheme = uNull<ThemeData>(uClass)(__m['highContrastDarkTheme']);
  final ThemeMode? themeMode = uNull<ThemeMode>(_uThemeMode)(__m['themeMode']);
  final Locale? locale = uNull<Locale>(uClass)(__m['locale']);
  final Iterable<LocalizationsDelegate<dynamic>>? localizationsDelegates = uNull<Iterable<LocalizationsDelegate<dynamic>>>(uClass)(__m['localizationsDelegates']);
  final Locale? Function(List<Locale>?, Iterable<Locale>)? localeListResolutionCallback = uNull<Locale? Function(List<Locale>?, Iterable<Locale>)>(uFunc)(__m['localeListResolutionCallback']);
  final Locale? Function(Locale?, Iterable<Locale>)? localeResolutionCallback = uNull<Locale? Function(Locale?, Iterable<Locale>)>(uFunc)(__m['localeResolutionCallback']);
  final Iterable<Locale> supportedLocales = uClass(__m['supportedLocales']);
  final bool debugShowMaterialGrid = uConst<bool>(false, uBool)(__m['debugShowMaterialGrid']);
  final bool showPerformanceOverlay = uConst<bool>(false, uBool)(__m['showPerformanceOverlay']);
  final bool checkerboardRasterCacheImages = uConst<bool>(false, uBool)(__m['checkerboardRasterCacheImages']);
  final bool checkerboardOffscreenLayers = uConst<bool>(false, uBool)(__m['checkerboardOffscreenLayers']);
  final bool showSemanticsDebugger = uConst<bool>(false, uBool)(__m['showSemanticsDebugger']);
  final bool debugShowCheckedModeBanner = uConst<bool>(true, uBool)(__m['debugShowCheckedModeBanner']);
  final Map<ShortcutActivator, Intent>? shortcuts = uNull<Map<ShortcutActivator, Intent>>(uClass)(__m['shortcuts']);
  final Map<Type, Action<Intent>>? actions = uNull<Map<Type, Action<Intent>>>(uClass)(__m['actions']);
  final String? restorationScopeId = uNull<String>(uString)(__m['restorationScopeId']);
  final ScrollBehavior? scrollBehavior = uNull<ScrollBehavior>(uClass)(__m['scrollBehavior']);
  final bool useInheritedMediaQuery = uConst<bool>(false, uBool)(__m['useInheritedMediaQuery']);
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
  final Key? key = uNull<Key>(uClass)(__m['key']);
  final GlobalKey<ScaffoldMessengerState>? scaffoldMessengerKey = uNull<GlobalKey<ScaffoldMessengerState>>(uClass)(__m['scaffoldMessengerKey']);
  final RouteInformationProvider? routeInformationProvider = uNull<RouteInformationProvider>(uClass)(__m['routeInformationProvider']);
  final RouteInformationParser<Object> routeInformationParser = uClass(__m['routeInformationParser']);
  final RouterDelegate<Object> routerDelegate = uClass(__m['routerDelegate']);
  final BackButtonDispatcher? backButtonDispatcher = uNull<BackButtonDispatcher>(uClass)(__m['backButtonDispatcher']);
  final Widget Function(BuildContext, Widget?)? builder = uNull<Widget Function(BuildContext, Widget?)>(uFunc)(__m['builder']);
  final String title = uConst<String>('', uString)(__m['title']);
  final String Function(BuildContext)? onGenerateTitle = uNull<String Function(BuildContext)>(uFunc)(__m['onGenerateTitle']);
  final Color? color = uNull<Color>(uClass)(__m['color']);
  final ThemeData? theme = uNull<ThemeData>(uClass)(__m['theme']);
  final ThemeData? darkTheme = uNull<ThemeData>(uClass)(__m['darkTheme']);
  final ThemeData? highContrastTheme = uNull<ThemeData>(uClass)(__m['highContrastTheme']);
  final ThemeData? highContrastDarkTheme = uNull<ThemeData>(uClass)(__m['highContrastDarkTheme']);
  final ThemeMode? themeMode = uNull<ThemeMode>(_uThemeMode)(__m['themeMode']);
  final Locale? locale = uNull<Locale>(uClass)(__m['locale']);
  final Iterable<LocalizationsDelegate<dynamic>>? localizationsDelegates = uNull<Iterable<LocalizationsDelegate<dynamic>>>(uClass)(__m['localizationsDelegates']);
  final Locale? Function(List<Locale>?, Iterable<Locale>)? localeListResolutionCallback = uNull<Locale? Function(List<Locale>?, Iterable<Locale>)>(uFunc)(__m['localeListResolutionCallback']);
  final Locale? Function(Locale?, Iterable<Locale>)? localeResolutionCallback = uNull<Locale? Function(Locale?, Iterable<Locale>)>(uFunc)(__m['localeResolutionCallback']);
  final Iterable<Locale> supportedLocales = uClass(__m['supportedLocales']);
  final bool debugShowMaterialGrid = uConst<bool>(false, uBool)(__m['debugShowMaterialGrid']);
  final bool showPerformanceOverlay = uConst<bool>(false, uBool)(__m['showPerformanceOverlay']);
  final bool checkerboardRasterCacheImages = uConst<bool>(false, uBool)(__m['checkerboardRasterCacheImages']);
  final bool checkerboardOffscreenLayers = uConst<bool>(false, uBool)(__m['checkerboardOffscreenLayers']);
  final bool showSemanticsDebugger = uConst<bool>(false, uBool)(__m['showSemanticsDebugger']);
  final bool debugShowCheckedModeBanner = uConst<bool>(true, uBool)(__m['debugShowCheckedModeBanner']);
  final Map<ShortcutActivator, Intent>? shortcuts = uNull<Map<ShortcutActivator, Intent>>(uClass)(__m['shortcuts']);
  final Map<Type, Action<Intent>>? actions = uNull<Map<Type, Action<Intent>>>(uClass)(__m['actions']);
  final String? restorationScopeId = uNull<String>(uString)(__m['restorationScopeId']);
  final ScrollBehavior? scrollBehavior = uNull<ScrollBehavior>(uClass)(__m['scrollBehavior']);
  final bool useInheritedMediaQuery = uConst<bool>(false, uBool)(__m['useInheritedMediaQuery']);
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
  final int usbHidUsage = uInt(__m['usbHidUsage']);
  return PhysicalKeyboardKey(
    usbHidUsage,
  );
}

LogicalKeyboardKey _uLogicalKeyboardKey(Map<String, dynamic> __m) {
  final int keyId = uInt(__m['keyId']);
  return LogicalKeyboardKey(
    keyId,
  );
}

FocusNode _uFocusNode(Map<String, dynamic> __m) {
  final String? debugLabel = uNull<String>(uString)(__m['debugLabel']);
  final KeyEventResult Function(FocusNode, RawKeyEvent)? onKey = uNull<KeyEventResult Function(FocusNode, RawKeyEvent)>(uFunc)(__m['onKey']);
  final KeyEventResult Function(FocusNode, KeyEvent)? onKeyEvent = uNull<KeyEventResult Function(FocusNode, KeyEvent)>(uFunc)(__m['onKeyEvent']);
  final bool skipTraversal = uConst<bool>(false, uBool)(__m['skipTraversal']);
  final bool canRequestFocus = uConst<bool>(true, uBool)(__m['canRequestFocus']);
  final bool descendantsAreFocusable = uConst<bool>(true, uBool)(__m['descendantsAreFocusable']);
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
  final Key? key = uNull<Key>(uClass)(__m['key']);
  final void Function()? onPressed = uNull<void Function()>(uFunc)(__m['onPressed']);
  final void Function()? onLongPress = uNull<void Function()>(uFunc)(__m['onLongPress']);
  final ButtonStyle? style = uNull<ButtonStyle>(uClass)(__m['style']);
  final FocusNode? focusNode = uNull<FocusNode>(uClass)(__m['focusNode']);
  final bool autofocus = uConst<bool>(false, uBool)(__m['autofocus']);
  final Clip clipBehavior = uConst(Clip.none, _uClip)(__m['clipBehavior']);
  final Widget? child = uNull<Widget>(uClass)(__m['child']);
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
  final Key? key = uNull<Key>(uClass)(__m['key']);
  final void Function()? onPressed = uNull<void Function()>(uFunc)(__m['onPressed']);
  final void Function()? onLongPress = uNull<void Function()>(uFunc)(__m['onLongPress']);
  final ButtonStyle? style = uNull<ButtonStyle>(uClass)(__m['style']);
  final FocusNode? focusNode = uNull<FocusNode>(uClass)(__m['focusNode']);
  final bool? autofocus = uNull<bool>(uBool)(__m['autofocus']);
  final Clip? clipBehavior = uNull<Clip>(_uClip)(__m['clipBehavior']);
  final Widget icon = uClass(__m['icon']);
  final Widget label = uClass(__m['label']);
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
