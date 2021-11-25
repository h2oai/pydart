import 'dart:ui';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/services.dart';
import 'load.dart';

Object _uObject(Map<String, dynamic> __m) {
  return Object(
  );
}

RouteSettings _uRouteSettings(Map<String, dynamic> __m) {
  final String name = uString(__m['name']);
  final Object? arguments = _unClass(__m['arguments']);
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
  final Key? key = _unClass(__m['key']);
  final List<Page<dynamic>> pages = _uClass(__m['pages']);
  final bool Function(Route<dynamic>, dynamic) onPopPage = __m['onPopPage'];
  final String initialRoute = uString(__m['initialRoute']);
  final List<Route<dynamic>> Function(NavigatorState, String) onGenerateInitialRoutes = __m['onGenerateInitialRoutes'];
  final Route<dynamic>? Function(RouteSettings) onGenerateRoute = __m['onGenerateRoute'];
  final Route<dynamic>? Function(RouteSettings) onUnknownRoute = __m['onUnknownRoute'];
  final TransitionDelegate<dynamic> transitionDelegate = _uClass(__m['transitionDelegate']);
  final bool reportsRouteUpdateToEngine = uBool(__m['reportsRouteUpdateToEngine']);
  final List<NavigatorObserver> observers = _uClass(__m['observers']);
  final String restorationScopeId = uString(__m['restorationScopeId']);
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
  final Key? key = _unClass(__m['key']);
  final Widget child = _uClass(__m['child']);
  return ScaffoldMessenger(
    key: key,
    child: child,
  );
}

ScaffoldMessengerState _uScaffoldMessengerState(Map<String, dynamic> __m) {
  return ScaffoldMessengerState(
  );
}

MapEntry _uMapEntry(Map<String, dynamic> __m) {
  final K key = __m['key'];
  final V value = __m['value'];
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

Brightness? _unBrightness(dynamic v) => v == null ? v : _uBrightness(v);

VisualDensity _uVisualDensity(Map<String, dynamic> __m) {
  final double horizontal = uDouble(__m['horizontal']);
  final double vertical = uDouble(__m['vertical']);
  return VisualDensity(
    horizontal: horizontal,
    vertical: vertical,
  );
}

ColorSwatch _uColorSwatch(Map<String, dynamic> __m) {
  final int primary = uInt(__m['primary']);
  final Map<T, Color> _swatch = _uClass(__m['_swatch']);
  return ColorSwatch(
    primary,
    _swatch,
  );
}

MaterialColor _uMaterialColor(Map<String, dynamic> __m) {
  final int primary = uInt(__m['primary']);
  final Map<int, Color> swatch = _uClass(__m['swatch']);
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

ButtonTextTheme? _unButtonTextTheme(dynamic v) => v == null ? v : _uButtonTextTheme(v);

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

ButtonBarLayoutBehavior? _unButtonBarLayoutBehavior(dynamic v) => v == null ? v : _uButtonBarLayoutBehavior(v);

ColorScheme _uColorScheme(Map<String, dynamic> __m) {
  final Color primary = _uClass(__m['primary']);
  final Color primaryVariant = _uClass(__m['primaryVariant']);
  final Color secondary = _uClass(__m['secondary']);
  final Color secondaryVariant = _uClass(__m['secondaryVariant']);
  final Color surface = _uClass(__m['surface']);
  final Color background = _uClass(__m['background']);
  final Color error = _uClass(__m['error']);
  final Color onPrimary = _uClass(__m['onPrimary']);
  final Color onSecondary = _uClass(__m['onSecondary']);
  final Color onSurface = _uClass(__m['onSurface']);
  final Color onBackground = _uClass(__m['onBackground']);
  final Color onError = _uClass(__m['onError']);
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
  final Color primary = _uClass(__m['primary']);
  final Color primaryVariant = _uClass(__m['primaryVariant']);
  final Color secondary = _uClass(__m['secondary']);
  final Color secondaryVariant = _uClass(__m['secondaryVariant']);
  final Color surface = _uClass(__m['surface']);
  final Color background = _uClass(__m['background']);
  final Color error = _uClass(__m['error']);
  final Color onPrimary = _uClass(__m['onPrimary']);
  final Color onSecondary = _uClass(__m['onSecondary']);
  final Color onSurface = _uClass(__m['onSurface']);
  final Color onBackground = _uClass(__m['onBackground']);
  final Color onError = _uClass(__m['onError']);
  final Brightness brightness = _uBrightness(__m['brightness']);
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
  final Color primary = _uClass(__m['primary']);
  final Color primaryVariant = _uClass(__m['primaryVariant']);
  final Color secondary = _uClass(__m['secondary']);
  final Color secondaryVariant = _uClass(__m['secondaryVariant']);
  final Color surface = _uClass(__m['surface']);
  final Color background = _uClass(__m['background']);
  final Color error = _uClass(__m['error']);
  final Color onPrimary = _uClass(__m['onPrimary']);
  final Color onSecondary = _uClass(__m['onSecondary']);
  final Color onSurface = _uClass(__m['onSurface']);
  final Color onBackground = _uClass(__m['onBackground']);
  final Color onError = _uClass(__m['onError']);
  final Brightness brightness = _uBrightness(__m['brightness']);
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
  final Color primary = _uClass(__m['primary']);
  final Color primaryVariant = _uClass(__m['primaryVariant']);
  final Color secondary = _uClass(__m['secondary']);
  final Color secondaryVariant = _uClass(__m['secondaryVariant']);
  final Color surface = _uClass(__m['surface']);
  final Color background = _uClass(__m['background']);
  final Color error = _uClass(__m['error']);
  final Color onPrimary = _uClass(__m['onPrimary']);
  final Color onSecondary = _uClass(__m['onSecondary']);
  final Color onSurface = _uClass(__m['onSurface']);
  final Color onBackground = _uClass(__m['onBackground']);
  final Color onError = _uClass(__m['onError']);
  final Brightness brightness = _uBrightness(__m['brightness']);
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
  final Color primary = _uClass(__m['primary']);
  final Color primaryVariant = _uClass(__m['primaryVariant']);
  final Color secondary = _uClass(__m['secondary']);
  final Color secondaryVariant = _uClass(__m['secondaryVariant']);
  final Color surface = _uClass(__m['surface']);
  final Color background = _uClass(__m['background']);
  final Color error = _uClass(__m['error']);
  final Color onPrimary = _uClass(__m['onPrimary']);
  final Color onSecondary = _uClass(__m['onSecondary']);
  final Color onSurface = _uClass(__m['onSurface']);
  final Color onBackground = _uClass(__m['onBackground']);
  final Color onError = _uClass(__m['onError']);
  final Brightness brightness = _uBrightness(__m['brightness']);
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
  final MaterialColor primarySwatch = _uClass(__m['primarySwatch']);
  final Color? primaryColorDark = _unClass(__m['primaryColorDark']);
  final Color? accentColor = _unClass(__m['accentColor']);
  final Color? cardColor = _unClass(__m['cardColor']);
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final Color? errorColor = _unClass(__m['errorColor']);
  final Brightness brightness = _uBrightness(__m['brightness']);
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

MaterialTapTargetSize? _unMaterialTapTargetSize(dynamic v) => v == null ? v : _uMaterialTapTargetSize(v);

ButtonThemeData _uButtonThemeData(Map<String, dynamic> __m) {
  final ButtonTextTheme textTheme = _uButtonTextTheme(__m['textTheme']);
  final double minWidth = uDouble(__m['minWidth']);
  final double height = uDouble(__m['height']);
  final EdgeInsetsGeometry? padding = _unClass(__m['padding']);
  final ShapeBorder? shape = _unClass(__m['shape']);
  final ButtonBarLayoutBehavior layoutBehavior = _uButtonBarLayoutBehavior(__m['layoutBehavior']);
  final bool alignedDropdown = uBool(__m['alignedDropdown']);
  final Color? buttonColor = _unClass(__m['buttonColor']);
  final Color? disabledColor = _unClass(__m['disabledColor']);
  final Color? focusColor = _unClass(__m['focusColor']);
  final Color? hoverColor = _unClass(__m['hoverColor']);
  final Color? highlightColor = _unClass(__m['highlightColor']);
  final Color? splashColor = _unClass(__m['splashColor']);
  final ColorScheme? colorScheme = _unClass(__m['colorScheme']);
  final MaterialTapTargetSize? materialTapTargetSize = _unMaterialTapTargetSize(__m['materialTapTargetSize']);
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

FontStyle? _unFontStyle(dynamic v) => v == null ? v : _uFontStyle(v);

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

TextBaseline? _unTextBaseline(dynamic v) => v == null ? v : _uTextBaseline(v);

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

TextLeadingDistribution? _unTextLeadingDistribution(dynamic v) => v == null ? v : _uTextLeadingDistribution(v);

Locale _uLocale(Map<String, dynamic> __m) {
  final String _languageCode = uString(__m['_languageCode']);
  final String _countryCode = uString(__m['_countryCode']);
  return Locale(
    _languageCode,
    _countryCode,
  );
}

Locale _uLocaleFromSubtags(Map<String, dynamic> __m) {
  final String languageCode = uString(__m['languageCode']);
  final String scriptCode = uString(__m['scriptCode']);
  final String countryCode = uString(__m['countryCode']);
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
  final double distance = uDouble(__m['distance']);
  return Offset.fromDirection(
    direction,
    distance,
  );
}

Shadow _uShadow(Map<String, dynamic> __m) {
  final Color color = _uClass(__m['color']);
  final Offset offset = _uClass(__m['offset']);
  final double blurRadius = uDouble(__m['blurRadius']);
  return Shadow(
    color: color,
    offset: offset,
    blurRadius: blurRadius,
  );
}

FontFeature _uFontFeature(Map<String, dynamic> __m) {
  final String feature = uString(__m['feature']);
  final int value = uInt(__m['value']);
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
  return FontFeature.alternativeFractions(
  );
}

FontFeature _uFontFeatureContextualAlternates(Map<String, dynamic> __m) {
  return FontFeature.contextualAlternates(
  );
}

FontFeature _uFontFeatureCaseSensitiveForms(Map<String, dynamic> __m) {
  return FontFeature.caseSensitiveForms(
  );
}

FontFeature _uFontFeatureCharacterVariant(Map<String, dynamic> __m) {
  final int value = uInt(__m['value']);
  return FontFeature.characterVariant(
    value,
  );
}

FontFeature _uFontFeatureDenominator(Map<String, dynamic> __m) {
  return FontFeature.denominator(
  );
}

FontFeature _uFontFeatureFractions(Map<String, dynamic> __m) {
  return FontFeature.fractions(
  );
}

FontFeature _uFontFeatureHistoricalForms(Map<String, dynamic> __m) {
  return FontFeature.historicalForms(
  );
}

FontFeature _uFontFeatureHistoricalLigatures(Map<String, dynamic> __m) {
  return FontFeature.historicalLigatures(
  );
}

FontFeature _uFontFeatureLiningFigures(Map<String, dynamic> __m) {
  return FontFeature.liningFigures(
  );
}

FontFeature _uFontFeatureLocaleAware(Map<String, dynamic> __m) {
  final bool enable = uBool(__m['enable']);
  return FontFeature.localeAware(
    enable: enable,
  );
}

FontFeature _uFontFeatureNotationalForms(Map<String, dynamic> __m) {
  final int value = uInt(__m['value']);
  return FontFeature.notationalForms(
    value,
  );
}

FontFeature _uFontFeatureNumerators(Map<String, dynamic> __m) {
  return FontFeature.numerators(
  );
}

FontFeature _uFontFeatureOldstyleFigures(Map<String, dynamic> __m) {
  return FontFeature.oldstyleFigures(
  );
}

FontFeature _uFontFeatureOrdinalForms(Map<String, dynamic> __m) {
  return FontFeature.ordinalForms(
  );
}

FontFeature _uFontFeatureProportionalFigures(Map<String, dynamic> __m) {
  return FontFeature.proportionalFigures(
  );
}

FontFeature _uFontFeatureRandomize(Map<String, dynamic> __m) {
  return FontFeature.randomize(
  );
}

FontFeature _uFontFeatureStylisticAlternates(Map<String, dynamic> __m) {
  return FontFeature.stylisticAlternates(
  );
}

FontFeature _uFontFeatureScientificInferiors(Map<String, dynamic> __m) {
  return FontFeature.scientificInferiors(
  );
}

FontFeature _uFontFeatureStylisticSet(Map<String, dynamic> __m) {
  final int value = uInt(__m['value']);
  return FontFeature.stylisticSet(
    value,
  );
}

FontFeature _uFontFeatureSubscripts(Map<String, dynamic> __m) {
  return FontFeature.subscripts(
  );
}

FontFeature _uFontFeatureSuperscripts(Map<String, dynamic> __m) {
  return FontFeature.superscripts(
  );
}

FontFeature _uFontFeatureSwash(Map<String, dynamic> __m) {
  final int value = uInt(__m['value']);
  return FontFeature.swash(
    value,
  );
}

FontFeature _uFontFeatureTabularFigures(Map<String, dynamic> __m) {
  return FontFeature.tabularFigures(
  );
}

FontFeature _uFontFeatureSlashedZero(Map<String, dynamic> __m) {
  return FontFeature.slashedZero(
  );
}

TextDecoration _uTextDecorationCombine(Map<String, dynamic> __m) {
  final List<TextDecoration> decorations = _uClass(__m['decorations']);
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

TextDecorationStyle? _unTextDecorationStyle(dynamic v) => v == null ? v : _uTextDecorationStyle(v);

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

TextOverflow? _unTextOverflow(dynamic v) => v == null ? v : _uTextOverflow(v);

TextStyle _uTextStyle(Map<String, dynamic> __m) {
  final bool inherit = uBool(__m['inherit']);
  final Color? color = _unClass(__m['color']);
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final double fontSize = uDouble(__m['fontSize']);
  final FontWeight? fontWeight = _unClass(__m['fontWeight']);
  final FontStyle? fontStyle = _unFontStyle(__m['fontStyle']);
  final double letterSpacing = uDouble(__m['letterSpacing']);
  final double wordSpacing = uDouble(__m['wordSpacing']);
  final TextBaseline? textBaseline = _unTextBaseline(__m['textBaseline']);
  final double height = uDouble(__m['height']);
  final TextLeadingDistribution? leadingDistribution = _unTextLeadingDistribution(__m['leadingDistribution']);
  final Locale? locale = _unClass(__m['locale']);
  final Paint? foreground = _unClass(__m['foreground']);
  final Paint? background = _unClass(__m['background']);
  final List<Shadow>? shadows = _unClass(__m['shadows']);
  final List<FontFeature>? fontFeatures = _unClass(__m['fontFeatures']);
  final TextDecoration? decoration = _unClass(__m['decoration']);
  final Color? decorationColor = _unClass(__m['decorationColor']);
  final TextDecorationStyle? decorationStyle = _unTextDecorationStyle(__m['decorationStyle']);
  final double decorationThickness = uDouble(__m['decorationThickness']);
  final String debugLabel = uString(__m['debugLabel']);
  final String fontFamily = uString(__m['fontFamily']);
  final List<String>? fontFamilyFallback = _unClass(__m['fontFamilyFallback']);
  final String package = uString(__m['package']);
  final TextOverflow? overflow = _unTextOverflow(__m['overflow']);
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
  final Size source = _uClass(__m['source']);
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
  final double minWidth = uDouble(__m['minWidth']);
  final double maxWidth = uDouble(__m['maxWidth']);
  final double minHeight = uDouble(__m['minHeight']);
  final double maxHeight = uDouble(__m['maxHeight']);
  return BoxConstraints(
    minWidth: minWidth,
    maxWidth: maxWidth,
    minHeight: minHeight,
    maxHeight: maxHeight,
  );
}

BoxConstraints _uBoxConstraintsTight(Map<String, dynamic> __m) {
  final Size size = _uClass(__m['size']);
  return BoxConstraints.tight(
    size,
  );
}

BoxConstraints _uBoxConstraintsTightFor(Map<String, dynamic> __m) {
  final double width = uDouble(__m['width']);
  final double height = uDouble(__m['height']);
  return BoxConstraints.tightFor(
    width: width,
    height: height,
  );
}

BoxConstraints _uBoxConstraintsTightForFinite(Map<String, dynamic> __m) {
  final double width = uDouble(__m['width']);
  final double height = uDouble(__m['height']);
  return BoxConstraints.tightForFinite(
    width: width,
    height: height,
  );
}

BoxConstraints _uBoxConstraintsLoose(Map<String, dynamic> __m) {
  final Size size = _uClass(__m['size']);
  return BoxConstraints.loose(
    size,
  );
}

BoxConstraints _uBoxConstraintsExpand(Map<String, dynamic> __m) {
  final double width = uDouble(__m['width']);
  final double height = uDouble(__m['height']);
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
  final Radius radius = _uClass(__m['radius']);
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
  final Radius top = _uClass(__m['top']);
  final Radius bottom = _uClass(__m['bottom']);
  return BorderRadius.vertical(
    top: top,
    bottom: bottom,
  );
}

BorderRadius _uBorderRadiusHorizontal(Map<String, dynamic> __m) {
  final Radius left = _uClass(__m['left']);
  final Radius right = _uClass(__m['right']);
  return BorderRadius.horizontal(
    left: left,
    right: right,
  );
}

BorderRadius _uBorderRadiusOnly(Map<String, dynamic> __m) {
  final Radius topLeft = _uClass(__m['topLeft']);
  final Radius topRight = _uClass(__m['topRight']);
  final Radius bottomLeft = _uClass(__m['bottomLeft']);
  final Radius bottomRight = _uClass(__m['bottomRight']);
  return BorderRadius.only(
    topLeft: topLeft,
    topRight: topRight,
    bottomLeft: bottomLeft,
    bottomRight: bottomRight,
  );
}

ToggleButtonsThemeData _uToggleButtonsThemeData(Map<String, dynamic> __m) {
  final TextStyle? textStyle = _unClass(__m['textStyle']);
  final BoxConstraints? constraints = _unClass(__m['constraints']);
  final Color? color = _unClass(__m['color']);
  final Color? selectedColor = _unClass(__m['selectedColor']);
  final Color? disabledColor = _unClass(__m['disabledColor']);
  final Color? fillColor = _unClass(__m['fillColor']);
  final Color? focusColor = _unClass(__m['focusColor']);
  final Color? highlightColor = _unClass(__m['highlightColor']);
  final Color? hoverColor = _unClass(__m['hoverColor']);
  final Color? splashColor = _unClass(__m['splashColor']);
  final Color? borderColor = _unClass(__m['borderColor']);
  final Color? selectedBorderColor = _unClass(__m['selectedBorderColor']);
  final Color? disabledBorderColor = _unClass(__m['disabledBorderColor']);
  final BorderRadius? borderRadius = _unClass(__m['borderRadius']);
  final double borderWidth = uDouble(__m['borderWidth']);
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
  final TextStyle? headline1 = _unClass(__m['headline1']);
  final TextStyle? headline2 = _unClass(__m['headline2']);
  final TextStyle? headline3 = _unClass(__m['headline3']);
  final TextStyle? headline4 = _unClass(__m['headline4']);
  final TextStyle? headline5 = _unClass(__m['headline5']);
  final TextStyle? headline6 = _unClass(__m['headline6']);
  final TextStyle? subtitle1 = _unClass(__m['subtitle1']);
  final TextStyle? subtitle2 = _unClass(__m['subtitle2']);
  final TextStyle? bodyText1 = _unClass(__m['bodyText1']);
  final TextStyle? bodyText2 = _unClass(__m['bodyText2']);
  final TextStyle? caption = _unClass(__m['caption']);
  final TextStyle? button = _unClass(__m['button']);
  final TextStyle? overline = _unClass(__m['overline']);
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

FloatingLabelBehavior? _unFloatingLabelBehavior(dynamic v) => v == null ? v : _uFloatingLabelBehavior(v);

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

BorderStyle? _unBorderStyle(dynamic v) => v == null ? v : _uBorderStyle(v);

BorderSide _uBorderSide(Map<String, dynamic> __m) {
  final Color color = _uClass(__m['color']);
  final double width = uDouble(__m['width']);
  final BorderStyle style = _uBorderStyle(__m['style']);
  return BorderSide(
    color: color,
    width: width,
    style: style,
  );
}

InputDecorationTheme _uInputDecorationTheme(Map<String, dynamic> __m) {
  final TextStyle? labelStyle = _unClass(__m['labelStyle']);
  final TextStyle? floatingLabelStyle = _unClass(__m['floatingLabelStyle']);
  final TextStyle? helperStyle = _unClass(__m['helperStyle']);
  final int helperMaxLines = uInt(__m['helperMaxLines']);
  final TextStyle? hintStyle = _unClass(__m['hintStyle']);
  final TextStyle? errorStyle = _unClass(__m['errorStyle']);
  final int errorMaxLines = uInt(__m['errorMaxLines']);
  final FloatingLabelBehavior floatingLabelBehavior = _uFloatingLabelBehavior(__m['floatingLabelBehavior']);
  final bool isDense = uBool(__m['isDense']);
  final EdgeInsetsGeometry? contentPadding = _unClass(__m['contentPadding']);
  final bool isCollapsed = uBool(__m['isCollapsed']);
  final TextStyle? prefixStyle = _unClass(__m['prefixStyle']);
  final TextStyle? suffixStyle = _unClass(__m['suffixStyle']);
  final TextStyle? counterStyle = _unClass(__m['counterStyle']);
  final bool filled = uBool(__m['filled']);
  final Color? fillColor = _unClass(__m['fillColor']);
  final Color? focusColor = _unClass(__m['focusColor']);
  final Color? hoverColor = _unClass(__m['hoverColor']);
  final InputBorder? errorBorder = _unClass(__m['errorBorder']);
  final InputBorder? focusedBorder = _unClass(__m['focusedBorder']);
  final InputBorder? focusedErrorBorder = _unClass(__m['focusedErrorBorder']);
  final InputBorder? disabledBorder = _unClass(__m['disabledBorder']);
  final InputBorder? enabledBorder = _unClass(__m['enabledBorder']);
  final InputBorder? border = _unClass(__m['border']);
  final bool alignLabelWithHint = uBool(__m['alignLabelWithHint']);
  final BoxConstraints? constraints = _unClass(__m['constraints']);
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
  final Color? color = _unClass(__m['color']);
  final double opacity = uDouble(__m['opacity']);
  final double size = uDouble(__m['size']);
  return IconThemeData(
    color: color,
    opacity: opacity,
    size: size,
  );
}

IconThemeData _uIconThemeDataFallback(Map<String, dynamic> __m) {
  return IconThemeData.fallback(
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

ShowValueIndicator? _unShowValueIndicator(dynamic v) => v == null ? v : _uShowValueIndicator(v);

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

TextDirection? _unTextDirection(dynamic v) => v == null ? v : _uTextDirection(v);

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

Thumb? _unThumb(dynamic v) => v == null ? v : _uThumb(v);

SliderThemeData _uSliderThemeData(Map<String, dynamic> __m) {
  final double trackHeight = uDouble(__m['trackHeight']);
  final Color? activeTrackColor = _unClass(__m['activeTrackColor']);
  final Color? inactiveTrackColor = _unClass(__m['inactiveTrackColor']);
  final Color? disabledActiveTrackColor = _unClass(__m['disabledActiveTrackColor']);
  final Color? disabledInactiveTrackColor = _unClass(__m['disabledInactiveTrackColor']);
  final Color? activeTickMarkColor = _unClass(__m['activeTickMarkColor']);
  final Color? inactiveTickMarkColor = _unClass(__m['inactiveTickMarkColor']);
  final Color? disabledActiveTickMarkColor = _unClass(__m['disabledActiveTickMarkColor']);
  final Color? disabledInactiveTickMarkColor = _unClass(__m['disabledInactiveTickMarkColor']);
  final Color? thumbColor = _unClass(__m['thumbColor']);
  final Color? overlappingShapeStrokeColor = _unClass(__m['overlappingShapeStrokeColor']);
  final Color? disabledThumbColor = _unClass(__m['disabledThumbColor']);
  final Color? overlayColor = _unClass(__m['overlayColor']);
  final Color? valueIndicatorColor = _unClass(__m['valueIndicatorColor']);
  final SliderComponentShape? overlayShape = _unClass(__m['overlayShape']);
  final SliderTickMarkShape? tickMarkShape = _unClass(__m['tickMarkShape']);
  final SliderComponentShape? thumbShape = _unClass(__m['thumbShape']);
  final SliderTrackShape? trackShape = _unClass(__m['trackShape']);
  final SliderComponentShape? valueIndicatorShape = _unClass(__m['valueIndicatorShape']);
  final RangeSliderTickMarkShape? rangeTickMarkShape = _unClass(__m['rangeTickMarkShape']);
  final RangeSliderThumbShape? rangeThumbShape = _unClass(__m['rangeThumbShape']);
  final RangeSliderTrackShape? rangeTrackShape = _unClass(__m['rangeTrackShape']);
  final RangeSliderValueIndicatorShape? rangeValueIndicatorShape = _unClass(__m['rangeValueIndicatorShape']);
  final ShowValueIndicator? showValueIndicator = _unShowValueIndicator(__m['showValueIndicator']);
  final TextStyle? valueIndicatorTextStyle = _unClass(__m['valueIndicatorTextStyle']);
  final double minThumbSeparation = uDouble(__m['minThumbSeparation']);
  final Thumb? Function(TextDirection, RangeValues, double, Size, Size, double) thumbSelector = __m['thumbSelector'];
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
  final Color primaryColor = _uClass(__m['primaryColor']);
  final Color primaryColorDark = _uClass(__m['primaryColorDark']);
  final Color primaryColorLight = _uClass(__m['primaryColorLight']);
  final TextStyle valueIndicatorTextStyle = _uClass(__m['valueIndicatorTextStyle']);
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

TabBarIndicatorSize? _unTabBarIndicatorSize(dynamic v) => v == null ? v : _uTabBarIndicatorSize(v);

TabBarTheme _uTabBarTheme(Map<String, dynamic> __m) {
  final Decoration? indicator = _unClass(__m['indicator']);
  final TabBarIndicatorSize? indicatorSize = _unTabBarIndicatorSize(__m['indicatorSize']);
  final Color? labelColor = _unClass(__m['labelColor']);
  final EdgeInsetsGeometry? labelPadding = _unClass(__m['labelPadding']);
  final TextStyle? labelStyle = _unClass(__m['labelStyle']);
  final Color? unselectedLabelColor = _unClass(__m['unselectedLabelColor']);
  final TextStyle? unselectedLabelStyle = _unClass(__m['unselectedLabelStyle']);
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
  final int days = uInt(__m['days']);
  final int hours = uInt(__m['hours']);
  final int minutes = uInt(__m['minutes']);
  final int seconds = uInt(__m['seconds']);
  final int milliseconds = uInt(__m['milliseconds']);
  final int microseconds = uInt(__m['microseconds']);
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

TooltipTriggerMode? _unTooltipTriggerMode(dynamic v) => v == null ? v : _uTooltipTriggerMode(v);

TooltipThemeData _uTooltipThemeData(Map<String, dynamic> __m) {
  final double height = uDouble(__m['height']);
  final EdgeInsetsGeometry? padding = _unClass(__m['padding']);
  final EdgeInsetsGeometry? margin = _unClass(__m['margin']);
  final double verticalOffset = uDouble(__m['verticalOffset']);
  final bool preferBelow = uBool(__m['preferBelow']);
  final bool excludeFromSemantics = uBool(__m['excludeFromSemantics']);
  final Decoration? decoration = _unClass(__m['decoration']);
  final TextStyle? textStyle = _unClass(__m['textStyle']);
  final Duration? waitDuration = _unClass(__m['waitDuration']);
  final Duration? showDuration = _unClass(__m['showDuration']);
  final TooltipTriggerMode? triggerMode = _unTooltipTriggerMode(__m['triggerMode']);
  final bool enableFeedback = uBool(__m['enableFeedback']);
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

Clip? _unClip(dynamic v) => v == null ? v : _uClip(v);

CardTheme _uCardTheme(Map<String, dynamic> __m) {
  final Clip? clipBehavior = _unClip(__m['clipBehavior']);
  final Color? color = _unClass(__m['color']);
  final Color? shadowColor = _unClass(__m['shadowColor']);
  final double elevation = uDouble(__m['elevation']);
  final EdgeInsetsGeometry? margin = _unClass(__m['margin']);
  final ShapeBorder? shape = _unClass(__m['shape']);
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
  final Color backgroundColor = _uClass(__m['backgroundColor']);
  final Color? deleteIconColor = _unClass(__m['deleteIconColor']);
  final Color disabledColor = _uClass(__m['disabledColor']);
  final Color selectedColor = _uClass(__m['selectedColor']);
  final Color secondarySelectedColor = _uClass(__m['secondarySelectedColor']);
  final Color? shadowColor = _unClass(__m['shadowColor']);
  final Color? selectedShadowColor = _unClass(__m['selectedShadowColor']);
  final bool showCheckmark = uBool(__m['showCheckmark']);
  final Color? checkmarkColor = _unClass(__m['checkmarkColor']);
  final EdgeInsetsGeometry? labelPadding = _unClass(__m['labelPadding']);
  final EdgeInsetsGeometry padding = _uClass(__m['padding']);
  final BorderSide? side = _unClass(__m['side']);
  final OutlinedBorder? shape = _unClass(__m['shape']);
  final TextStyle labelStyle = _uClass(__m['labelStyle']);
  final TextStyle secondaryLabelStyle = _uClass(__m['secondaryLabelStyle']);
  final Brightness brightness = _uBrightness(__m['brightness']);
  final double elevation = uDouble(__m['elevation']);
  final double pressElevation = uDouble(__m['pressElevation']);
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
  final Brightness? brightness = _unBrightness(__m['brightness']);
  final Color? primaryColor = _unClass(__m['primaryColor']);
  final Color secondaryColor = _uClass(__m['secondaryColor']);
  final TextStyle labelStyle = _uClass(__m['labelStyle']);
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

TargetPlatform? _unTargetPlatform(dynamic v) => v == null ? v : _uTargetPlatform(v);

PageTransitionsTheme _uPageTransitionsTheme(Map<String, dynamic> __m) {
  final Map<TargetPlatform, PageTransitionsBuilder> builders = _uClass(__m['builders']);
  return PageTransitionsTheme(
    builders: builders,
  );
}

SystemUiOverlayStyle _uSystemUiOverlayStyle(Map<String, dynamic> __m) {
  final Color? systemNavigationBarColor = _unClass(__m['systemNavigationBarColor']);
  final Color? systemNavigationBarDividerColor = _unClass(__m['systemNavigationBarDividerColor']);
  final Brightness? systemNavigationBarIconBrightness = _unBrightness(__m['systemNavigationBarIconBrightness']);
  final bool systemNavigationBarContrastEnforced = uBool(__m['systemNavigationBarContrastEnforced']);
  final Color? statusBarColor = _unClass(__m['statusBarColor']);
  final Brightness? statusBarBrightness = _unBrightness(__m['statusBarBrightness']);
  final Brightness? statusBarIconBrightness = _unBrightness(__m['statusBarIconBrightness']);
  final bool systemStatusBarContrastEnforced = uBool(__m['systemStatusBarContrastEnforced']);
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
  final Brightness? brightness = _unBrightness(__m['brightness']);
  final Color? color = _unClass(__m['color']);
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final Color? foregroundColor = _unClass(__m['foregroundColor']);
  final double elevation = uDouble(__m['elevation']);
  final Color? shadowColor = _unClass(__m['shadowColor']);
  final ShapeBorder? shape = _unClass(__m['shape']);
  final IconThemeData? iconTheme = _unClass(__m['iconTheme']);
  final IconThemeData? actionsIconTheme = _unClass(__m['actionsIconTheme']);
  final TextTheme? textTheme = _unClass(__m['textTheme']);
  final bool centerTitle = uBool(__m['centerTitle']);
  final double titleSpacing = uDouble(__m['titleSpacing']);
  final double toolbarHeight = uDouble(__m['toolbarHeight']);
  final TextStyle? toolbarTextStyle = _unClass(__m['toolbarTextStyle']);
  final TextStyle? titleTextStyle = _unClass(__m['titleTextStyle']);
  final SystemUiOverlayStyle? systemOverlayStyle = _unClass(__m['systemOverlayStyle']);
  final bool backwardsCompatibility = uBool(__m['backwardsCompatibility']);
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
  final MaterialStateProperty<double>? thickness = _unClass(__m['thickness']);
  final bool showTrackOnHover = uBool(__m['showTrackOnHover']);
  final bool isAlwaysShown = uBool(__m['isAlwaysShown']);
  final Radius? radius = _unClass(__m['radius']);
  final MaterialStateProperty<Color?>? thumbColor = _unClass(__m['thumbColor']);
  final MaterialStateProperty<Color?>? trackColor = _unClass(__m['trackColor']);
  final MaterialStateProperty<Color?>? trackBorderColor = _unClass(__m['trackBorderColor']);
  final double crossAxisMargin = uDouble(__m['crossAxisMargin']);
  final double mainAxisMargin = uDouble(__m['mainAxisMargin']);
  final double minThumbLength = uDouble(__m['minThumbLength']);
  final bool interactive = uBool(__m['interactive']);
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
  final Color? color = _unClass(__m['color']);
  final double elevation = uDouble(__m['elevation']);
  final NotchedShape? shape = _unClass(__m['shape']);
  return BottomAppBarTheme(
    color: color,
    elevation: elevation,
    shape: shape,
  );
}

DialogTheme _uDialogTheme(Map<String, dynamic> __m) {
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final double elevation = uDouble(__m['elevation']);
  final ShapeBorder? shape = _unClass(__m['shape']);
  final TextStyle? titleTextStyle = _unClass(__m['titleTextStyle']);
  final TextStyle? contentTextStyle = _unClass(__m['contentTextStyle']);
  return DialogTheme(
    backgroundColor: backgroundColor,
    elevation: elevation,
    shape: shape,
    titleTextStyle: titleTextStyle,
    contentTextStyle: contentTextStyle,
  );
}

FloatingActionButtonThemeData _uFloatingActionButtonThemeData(Map<String, dynamic> __m) {
  final Color? foregroundColor = _unClass(__m['foregroundColor']);
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final Color? focusColor = _unClass(__m['focusColor']);
  final Color? hoverColor = _unClass(__m['hoverColor']);
  final Color? splashColor = _unClass(__m['splashColor']);
  final double elevation = uDouble(__m['elevation']);
  final double focusElevation = uDouble(__m['focusElevation']);
  final double hoverElevation = uDouble(__m['hoverElevation']);
  final double disabledElevation = uDouble(__m['disabledElevation']);
  final double highlightElevation = uDouble(__m['highlightElevation']);
  final ShapeBorder? shape = _unClass(__m['shape']);
  final bool enableFeedback = uBool(__m['enableFeedback']);
  final BoxConstraints? sizeConstraints = _unClass(__m['sizeConstraints']);
  final BoxConstraints? smallSizeConstraints = _unClass(__m['smallSizeConstraints']);
  final BoxConstraints? largeSizeConstraints = _unClass(__m['largeSizeConstraints']);
  final BoxConstraints? extendedSizeConstraints = _unClass(__m['extendedSizeConstraints']);
  final double extendedIconLabelSpacing = uDouble(__m['extendedIconLabelSpacing']);
  final EdgeInsetsGeometry? extendedPadding = _unClass(__m['extendedPadding']);
  final TextStyle? extendedTextStyle = _unClass(__m['extendedTextStyle']);
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

NavigationRailLabelType? _unNavigationRailLabelType(dynamic v) => v == null ? v : _uNavigationRailLabelType(v);

NavigationRailThemeData _uNavigationRailThemeData(Map<String, dynamic> __m) {
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final double elevation = uDouble(__m['elevation']);
  final TextStyle? unselectedLabelTextStyle = _unClass(__m['unselectedLabelTextStyle']);
  final TextStyle? selectedLabelTextStyle = _unClass(__m['selectedLabelTextStyle']);
  final IconThemeData? unselectedIconTheme = _unClass(__m['unselectedIconTheme']);
  final IconThemeData? selectedIconTheme = _unClass(__m['selectedIconTheme']);
  final double groupAlignment = uDouble(__m['groupAlignment']);
  final NavigationRailLabelType? labelType = _unNavigationRailLabelType(__m['labelType']);
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
  final TargetPlatform? platform = _unTargetPlatform(__m['platform']);
  final TextTheme? black = _unClass(__m['black']);
  final TextTheme? white = _unClass(__m['white']);
  final TextTheme? englishLike = _unClass(__m['englishLike']);
  final TextTheme? dense = _unClass(__m['dense']);
  final TextTheme? tall = _unClass(__m['tall']);
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
  final TargetPlatform? platform = _unTargetPlatform(__m['platform']);
  final TextTheme? black = _unClass(__m['black']);
  final TextTheme? white = _unClass(__m['white']);
  final TextTheme? englishLike = _unClass(__m['englishLike']);
  final TextTheme? dense = _unClass(__m['dense']);
  final TextTheme? tall = _unClass(__m['tall']);
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
  final TargetPlatform? platform = _unTargetPlatform(__m['platform']);
  final TextTheme? black = _unClass(__m['black']);
  final TextTheme? white = _unClass(__m['white']);
  final TextTheme? englishLike = _unClass(__m['englishLike']);
  final TextTheme? dense = _unClass(__m['dense']);
  final TextTheme? tall = _unClass(__m['tall']);
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
  final Color primaryColor = _uClass(__m['primaryColor']);
  final TextStyle? textStyle = _unClass(__m['textStyle']);
  final TextStyle? actionTextStyle = _unClass(__m['actionTextStyle']);
  final TextStyle? tabLabelTextStyle = _unClass(__m['tabLabelTextStyle']);
  final TextStyle? navTitleTextStyle = _unClass(__m['navTitleTextStyle']);
  final TextStyle? navLargeTitleTextStyle = _unClass(__m['navLargeTitleTextStyle']);
  final TextStyle? navActionTextStyle = _unClass(__m['navActionTextStyle']);
  final TextStyle? pickerTextStyle = _unClass(__m['pickerTextStyle']);
  final TextStyle? dateTimePickerTextStyle = _unClass(__m['dateTimePickerTextStyle']);
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
  final Brightness? brightness = _unBrightness(__m['brightness']);
  final Color? primaryColor = _unClass(__m['primaryColor']);
  final Color? primaryContrastingColor = _unClass(__m['primaryContrastingColor']);
  final CupertinoTextThemeData? textTheme = _unClass(__m['textTheme']);
  final Color? barBackgroundColor = _unClass(__m['barBackgroundColor']);
  final Color? scaffoldBackgroundColor = _unClass(__m['scaffoldBackgroundColor']);
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

SnackBarBehavior? _unSnackBarBehavior(dynamic v) => v == null ? v : _uSnackBarBehavior(v);

SnackBarThemeData _uSnackBarThemeData(Map<String, dynamic> __m) {
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final Color? actionTextColor = _unClass(__m['actionTextColor']);
  final Color? disabledActionTextColor = _unClass(__m['disabledActionTextColor']);
  final TextStyle? contentTextStyle = _unClass(__m['contentTextStyle']);
  final double elevation = uDouble(__m['elevation']);
  final ShapeBorder? shape = _unClass(__m['shape']);
  final SnackBarBehavior? behavior = _unSnackBarBehavior(__m['behavior']);
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
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final double elevation = uDouble(__m['elevation']);
  final Color? modalBackgroundColor = _unClass(__m['modalBackgroundColor']);
  final double modalElevation = uDouble(__m['modalElevation']);
  final ShapeBorder? shape = _unClass(__m['shape']);
  final Clip? clipBehavior = _unClip(__m['clipBehavior']);
  final BoxConstraints? constraints = _unClass(__m['constraints']);
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
  final Color? color = _unClass(__m['color']);
  final ShapeBorder? shape = _unClass(__m['shape']);
  final double elevation = uDouble(__m['elevation']);
  final TextStyle? textStyle = _unClass(__m['textStyle']);
  final bool enableFeedback = uBool(__m['enableFeedback']);
  return PopupMenuThemeData(
    color: color,
    shape: shape,
    elevation: elevation,
    textStyle: textStyle,
    enableFeedback: enableFeedback,
  );
}

MaterialBannerThemeData _uMaterialBannerThemeData(Map<String, dynamic> __m) {
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final TextStyle? contentTextStyle = _unClass(__m['contentTextStyle']);
  final EdgeInsetsGeometry? padding = _unClass(__m['padding']);
  final EdgeInsetsGeometry? leadingPadding = _unClass(__m['leadingPadding']);
  return MaterialBannerThemeData(
    backgroundColor: backgroundColor,
    contentTextStyle: contentTextStyle,
    padding: padding,
    leadingPadding: leadingPadding,
  );
}

DividerThemeData _uDividerThemeData(Map<String, dynamic> __m) {
  final Color? color = _unClass(__m['color']);
  final double space = uDouble(__m['space']);
  final double thickness = uDouble(__m['thickness']);
  final double indent = uDouble(__m['indent']);
  final double endIndent = uDouble(__m['endIndent']);
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

MainAxisAlignment? _unMainAxisAlignment(dynamic v) => v == null ? v : _uMainAxisAlignment(v);

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

MainAxisSize? _unMainAxisSize(dynamic v) => v == null ? v : _uMainAxisSize(v);

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

VerticalDirection? _unVerticalDirection(dynamic v) => v == null ? v : _uVerticalDirection(v);

ButtonBarThemeData _uButtonBarThemeData(Map<String, dynamic> __m) {
  final MainAxisAlignment? alignment = _unMainAxisAlignment(__m['alignment']);
  final MainAxisSize? mainAxisSize = _unMainAxisSize(__m['mainAxisSize']);
  final ButtonTextTheme? buttonTextTheme = _unButtonTextTheme(__m['buttonTextTheme']);
  final double buttonMinWidth = uDouble(__m['buttonMinWidth']);
  final double buttonHeight = uDouble(__m['buttonHeight']);
  final EdgeInsetsGeometry? buttonPadding = _unClass(__m['buttonPadding']);
  final bool buttonAlignedDropdown = uBool(__m['buttonAlignedDropdown']);
  final ButtonBarLayoutBehavior? layoutBehavior = _unButtonBarLayoutBehavior(__m['layoutBehavior']);
  final VerticalDirection? overflowDirection = _unVerticalDirection(__m['overflowDirection']);
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

BottomNavigationBarType? _unBottomNavigationBarType(dynamic v) => v == null ? v : _uBottomNavigationBarType(v);

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

BottomNavigationBarLandscapeLayout? _unBottomNavigationBarLandscapeLayout(dynamic v) => v == null ? v : _uBottomNavigationBarLandscapeLayout(v);

BottomNavigationBarThemeData _uBottomNavigationBarThemeData(Map<String, dynamic> __m) {
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final double elevation = uDouble(__m['elevation']);
  final IconThemeData? selectedIconTheme = _unClass(__m['selectedIconTheme']);
  final IconThemeData? unselectedIconTheme = _unClass(__m['unselectedIconTheme']);
  final Color? selectedItemColor = _unClass(__m['selectedItemColor']);
  final Color? unselectedItemColor = _unClass(__m['unselectedItemColor']);
  final TextStyle? selectedLabelStyle = _unClass(__m['selectedLabelStyle']);
  final TextStyle? unselectedLabelStyle = _unClass(__m['unselectedLabelStyle']);
  final bool showSelectedLabels = uBool(__m['showSelectedLabels']);
  final bool showUnselectedLabels = uBool(__m['showUnselectedLabels']);
  final BottomNavigationBarType? type = _unBottomNavigationBarType(__m['type']);
  final bool enableFeedback = uBool(__m['enableFeedback']);
  final BottomNavigationBarLandscapeLayout? landscapeLayout = _unBottomNavigationBarLandscapeLayout(__m['landscapeLayout']);
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
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final Color? hourMinuteTextColor = _unClass(__m['hourMinuteTextColor']);
  final Color? hourMinuteColor = _unClass(__m['hourMinuteColor']);
  final Color? dayPeriodTextColor = _unClass(__m['dayPeriodTextColor']);
  final Color? dayPeriodColor = _unClass(__m['dayPeriodColor']);
  final Color? dialHandColor = _unClass(__m['dialHandColor']);
  final Color? dialBackgroundColor = _unClass(__m['dialBackgroundColor']);
  final Color? dialTextColor = _unClass(__m['dialTextColor']);
  final Color? entryModeIconColor = _unClass(__m['entryModeIconColor']);
  final TextStyle? hourMinuteTextStyle = _unClass(__m['hourMinuteTextStyle']);
  final TextStyle? dayPeriodTextStyle = _unClass(__m['dayPeriodTextStyle']);
  final TextStyle? helpTextStyle = _unClass(__m['helpTextStyle']);
  final ShapeBorder? shape = _unClass(__m['shape']);
  final ShapeBorder? hourMinuteShape = _unClass(__m['hourMinuteShape']);
  final OutlinedBorder? dayPeriodShape = _unClass(__m['dayPeriodShape']);
  final BorderSide? dayPeriodBorderSide = _unClass(__m['dayPeriodBorderSide']);
  final InputDecorationTheme? inputDecorationTheme = _unClass(__m['inputDecorationTheme']);
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
  final MaterialStateProperty<TextStyle?>? textStyle = _unClass(__m['textStyle']);
  final MaterialStateProperty<Color?>? backgroundColor = _unClass(__m['backgroundColor']);
  final MaterialStateProperty<Color?>? foregroundColor = _unClass(__m['foregroundColor']);
  final MaterialStateProperty<Color?>? overlayColor = _unClass(__m['overlayColor']);
  final MaterialStateProperty<Color?>? shadowColor = _unClass(__m['shadowColor']);
  final MaterialStateProperty<double>? elevation = _unClass(__m['elevation']);
  final MaterialStateProperty<EdgeInsetsGeometry?>? padding = _unClass(__m['padding']);
  final MaterialStateProperty<Size?>? minimumSize = _unClass(__m['minimumSize']);
  final MaterialStateProperty<Size?>? fixedSize = _unClass(__m['fixedSize']);
  final MaterialStateProperty<Size?>? maximumSize = _unClass(__m['maximumSize']);
  final MaterialStateProperty<BorderSide?>? side = _unClass(__m['side']);
  final MaterialStateProperty<OutlinedBorder?>? shape = _unClass(__m['shape']);
  final MaterialStateProperty<MouseCursor?>? mouseCursor = _unClass(__m['mouseCursor']);
  final VisualDensity? visualDensity = _unClass(__m['visualDensity']);
  final MaterialTapTargetSize? tapTargetSize = _unMaterialTapTargetSize(__m['tapTargetSize']);
  final Duration? animationDuration = _unClass(__m['animationDuration']);
  final bool enableFeedback = uBool(__m['enableFeedback']);
  final AlignmentGeometry? alignment = _unClass(__m['alignment']);
  final InteractiveInkFeatureFactory? splashFactory = _unClass(__m['splashFactory']);
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
  final ButtonStyle? style = _unClass(__m['style']);
  return TextButtonThemeData(
    style: style,
  );
}

ElevatedButtonThemeData _uElevatedButtonThemeData(Map<String, dynamic> __m) {
  final ButtonStyle? style = _unClass(__m['style']);
  return ElevatedButtonThemeData(
    style: style,
  );
}

OutlinedButtonThemeData _uOutlinedButtonThemeData(Map<String, dynamic> __m) {
  final ButtonStyle? style = _unClass(__m['style']);
  return OutlinedButtonThemeData(
    style: style,
  );
}

TextSelectionThemeData _uTextSelectionThemeData(Map<String, dynamic> __m) {
  final Color? cursorColor = _unClass(__m['cursorColor']);
  final Color? selectionColor = _unClass(__m['selectionColor']);
  final Color? selectionHandleColor = _unClass(__m['selectionHandleColor']);
  return TextSelectionThemeData(
    cursorColor: cursorColor,
    selectionColor: selectionColor,
    selectionHandleColor: selectionHandleColor,
  );
}

DataTableThemeData _uDataTableThemeData(Map<String, dynamic> __m) {
  final Decoration? decoration = _unClass(__m['decoration']);
  final MaterialStateProperty<Color?>? dataRowColor = _unClass(__m['dataRowColor']);
  final double dataRowHeight = uDouble(__m['dataRowHeight']);
  final TextStyle? dataTextStyle = _unClass(__m['dataTextStyle']);
  final MaterialStateProperty<Color?>? headingRowColor = _unClass(__m['headingRowColor']);
  final double headingRowHeight = uDouble(__m['headingRowHeight']);
  final TextStyle? headingTextStyle = _unClass(__m['headingTextStyle']);
  final double horizontalMargin = uDouble(__m['horizontalMargin']);
  final double columnSpacing = uDouble(__m['columnSpacing']);
  final double dividerThickness = uDouble(__m['dividerThickness']);
  final double checkboxHorizontalMargin = uDouble(__m['checkboxHorizontalMargin']);
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
  final MaterialStateProperty<MouseCursor?>? mouseCursor = _unClass(__m['mouseCursor']);
  final MaterialStateProperty<Color?>? fillColor = _unClass(__m['fillColor']);
  final MaterialStateProperty<Color?>? checkColor = _unClass(__m['checkColor']);
  final MaterialStateProperty<Color?>? overlayColor = _unClass(__m['overlayColor']);
  final double splashRadius = uDouble(__m['splashRadius']);
  final MaterialTapTargetSize? materialTapTargetSize = _unMaterialTapTargetSize(__m['materialTapTargetSize']);
  final VisualDensity? visualDensity = _unClass(__m['visualDensity']);
  final OutlinedBorder? shape = _unClass(__m['shape']);
  final BorderSide? side = _unClass(__m['side']);
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
  final MaterialStateProperty<MouseCursor?>? mouseCursor = _unClass(__m['mouseCursor']);
  final MaterialStateProperty<Color?>? fillColor = _unClass(__m['fillColor']);
  final MaterialStateProperty<Color?>? overlayColor = _unClass(__m['overlayColor']);
  final double splashRadius = uDouble(__m['splashRadius']);
  final MaterialTapTargetSize? materialTapTargetSize = _unMaterialTapTargetSize(__m['materialTapTargetSize']);
  final VisualDensity? visualDensity = _unClass(__m['visualDensity']);
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
  final MaterialStateProperty<Color?>? thumbColor = _unClass(__m['thumbColor']);
  final MaterialStateProperty<Color?>? trackColor = _unClass(__m['trackColor']);
  final MaterialTapTargetSize? materialTapTargetSize = _unMaterialTapTargetSize(__m['materialTapTargetSize']);
  final MaterialStateProperty<MouseCursor?>? mouseCursor = _unClass(__m['mouseCursor']);
  final MaterialStateProperty<Color?>? overlayColor = _unClass(__m['overlayColor']);
  final double splashRadius = uDouble(__m['splashRadius']);
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
  final Color? color = _unClass(__m['color']);
  final Color? linearTrackColor = _unClass(__m['linearTrackColor']);
  final double linearMinHeight = uDouble(__m['linearMinHeight']);
  final Color? circularTrackColor = _unClass(__m['circularTrackColor']);
  final Color? refreshBackgroundColor = _unClass(__m['refreshBackgroundColor']);
  return ProgressIndicatorThemeData(
    color: color,
    linearTrackColor: linearTrackColor,
    linearMinHeight: linearMinHeight,
    circularTrackColor: circularTrackColor,
    refreshBackgroundColor: refreshBackgroundColor,
  );
}

ThemeData _uThemeData(Map<String, dynamic> __m) {
  final Brightness? brightness = _unBrightness(__m['brightness']);
  final VisualDensity? visualDensity = _unClass(__m['visualDensity']);
  final MaterialColor? primarySwatch = _unClass(__m['primarySwatch']);
  final Color? primaryColor = _unClass(__m['primaryColor']);
  final Brightness? primaryColorBrightness = _unBrightness(__m['primaryColorBrightness']);
  final Color? primaryColorLight = _unClass(__m['primaryColorLight']);
  final Color? primaryColorDark = _unClass(__m['primaryColorDark']);
  final Color? accentColor = _unClass(__m['accentColor']);
  final Brightness? accentColorBrightness = _unBrightness(__m['accentColorBrightness']);
  final Color? canvasColor = _unClass(__m['canvasColor']);
  final Color? shadowColor = _unClass(__m['shadowColor']);
  final Color? scaffoldBackgroundColor = _unClass(__m['scaffoldBackgroundColor']);
  final Color? bottomAppBarColor = _unClass(__m['bottomAppBarColor']);
  final Color? cardColor = _unClass(__m['cardColor']);
  final Color? dividerColor = _unClass(__m['dividerColor']);
  final Color? focusColor = _unClass(__m['focusColor']);
  final Color? hoverColor = _unClass(__m['hoverColor']);
  final Color? highlightColor = _unClass(__m['highlightColor']);
  final Color? splashColor = _unClass(__m['splashColor']);
  final InteractiveInkFeatureFactory? splashFactory = _unClass(__m['splashFactory']);
  final Color? selectedRowColor = _unClass(__m['selectedRowColor']);
  final Color? unselectedWidgetColor = _unClass(__m['unselectedWidgetColor']);
  final Color? disabledColor = _unClass(__m['disabledColor']);
  final Color? buttonColor = _unClass(__m['buttonColor']);
  final ButtonThemeData? buttonTheme = _unClass(__m['buttonTheme']);
  final ToggleButtonsThemeData? toggleButtonsTheme = _unClass(__m['toggleButtonsTheme']);
  final Color? secondaryHeaderColor = _unClass(__m['secondaryHeaderColor']);
  final Color? textSelectionColor = _unClass(__m['textSelectionColor']);
  final Color? cursorColor = _unClass(__m['cursorColor']);
  final Color? textSelectionHandleColor = _unClass(__m['textSelectionHandleColor']);
  final Color? backgroundColor = _unClass(__m['backgroundColor']);
  final Color? dialogBackgroundColor = _unClass(__m['dialogBackgroundColor']);
  final Color? indicatorColor = _unClass(__m['indicatorColor']);
  final Color? hintColor = _unClass(__m['hintColor']);
  final Color? errorColor = _unClass(__m['errorColor']);
  final Color? toggleableActiveColor = _unClass(__m['toggleableActiveColor']);
  final String fontFamily = uString(__m['fontFamily']);
  final TextTheme? textTheme = _unClass(__m['textTheme']);
  final TextTheme? primaryTextTheme = _unClass(__m['primaryTextTheme']);
  final TextTheme? accentTextTheme = _unClass(__m['accentTextTheme']);
  final InputDecorationTheme? inputDecorationTheme = _unClass(__m['inputDecorationTheme']);
  final IconThemeData? iconTheme = _unClass(__m['iconTheme']);
  final IconThemeData? primaryIconTheme = _unClass(__m['primaryIconTheme']);
  final IconThemeData? accentIconTheme = _unClass(__m['accentIconTheme']);
  final SliderThemeData? sliderTheme = _unClass(__m['sliderTheme']);
  final TabBarTheme? tabBarTheme = _unClass(__m['tabBarTheme']);
  final TooltipThemeData? tooltipTheme = _unClass(__m['tooltipTheme']);
  final CardTheme? cardTheme = _unClass(__m['cardTheme']);
  final ChipThemeData? chipTheme = _unClass(__m['chipTheme']);
  final TargetPlatform? platform = _unTargetPlatform(__m['platform']);
  final MaterialTapTargetSize? materialTapTargetSize = _unMaterialTapTargetSize(__m['materialTapTargetSize']);
  final bool applyElevationOverlayColor = uBool(__m['applyElevationOverlayColor']);
  final PageTransitionsTheme? pageTransitionsTheme = _unClass(__m['pageTransitionsTheme']);
  final AppBarTheme? appBarTheme = _unClass(__m['appBarTheme']);
  final ScrollbarThemeData? scrollbarTheme = _unClass(__m['scrollbarTheme']);
  final BottomAppBarTheme? bottomAppBarTheme = _unClass(__m['bottomAppBarTheme']);
  final ColorScheme? colorScheme = _unClass(__m['colorScheme']);
  final DialogTheme? dialogTheme = _unClass(__m['dialogTheme']);
  final FloatingActionButtonThemeData? floatingActionButtonTheme = _unClass(__m['floatingActionButtonTheme']);
  final NavigationRailThemeData? navigationRailTheme = _unClass(__m['navigationRailTheme']);
  final Typography? typography = _unClass(__m['typography']);
  final NoDefaultCupertinoThemeData? cupertinoOverrideTheme = _unClass(__m['cupertinoOverrideTheme']);
  final SnackBarThemeData? snackBarTheme = _unClass(__m['snackBarTheme']);
  final BottomSheetThemeData? bottomSheetTheme = _unClass(__m['bottomSheetTheme']);
  final PopupMenuThemeData? popupMenuTheme = _unClass(__m['popupMenuTheme']);
  final MaterialBannerThemeData? bannerTheme = _unClass(__m['bannerTheme']);
  final DividerThemeData? dividerTheme = _unClass(__m['dividerTheme']);
  final ButtonBarThemeData? buttonBarTheme = _unClass(__m['buttonBarTheme']);
  final BottomNavigationBarThemeData? bottomNavigationBarTheme = _unClass(__m['bottomNavigationBarTheme']);
  final TimePickerThemeData? timePickerTheme = _unClass(__m['timePickerTheme']);
  final TextButtonThemeData? textButtonTheme = _unClass(__m['textButtonTheme']);
  final ElevatedButtonThemeData? elevatedButtonTheme = _unClass(__m['elevatedButtonTheme']);
  final OutlinedButtonThemeData? outlinedButtonTheme = _unClass(__m['outlinedButtonTheme']);
  final TextSelectionThemeData? textSelectionTheme = _unClass(__m['textSelectionTheme']);
  final DataTableThemeData? dataTableTheme = _unClass(__m['dataTableTheme']);
  final CheckboxThemeData? checkboxTheme = _unClass(__m['checkboxTheme']);
  final RadioThemeData? radioTheme = _unClass(__m['radioTheme']);
  final SwitchThemeData? switchTheme = _unClass(__m['switchTheme']);
  final ProgressIndicatorThemeData? progressIndicatorTheme = _unClass(__m['progressIndicatorTheme']);
  final bool fixTextFieldOutlineLabel = uBool(__m['fixTextFieldOutlineLabel']);
  final bool useTextSelectionTheme = uBool(__m['useTextSelectionTheme']);
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
  final VisualDensity visualDensity = _uClass(__m['visualDensity']);
  final Color primaryColor = _uClass(__m['primaryColor']);
  final Brightness primaryColorBrightness = _uBrightness(__m['primaryColorBrightness']);
  final Color primaryColorLight = _uClass(__m['primaryColorLight']);
  final Color primaryColorDark = _uClass(__m['primaryColorDark']);
  final Color canvasColor = _uClass(__m['canvasColor']);
  final Color shadowColor = _uClass(__m['shadowColor']);
  final Color accentColor = _uClass(__m['accentColor']);
  final Brightness accentColorBrightness = _uBrightness(__m['accentColorBrightness']);
  final Color scaffoldBackgroundColor = _uClass(__m['scaffoldBackgroundColor']);
  final Color bottomAppBarColor = _uClass(__m['bottomAppBarColor']);
  final Color cardColor = _uClass(__m['cardColor']);
  final Color dividerColor = _uClass(__m['dividerColor']);
  final Color focusColor = _uClass(__m['focusColor']);
  final Color hoverColor = _uClass(__m['hoverColor']);
  final Color highlightColor = _uClass(__m['highlightColor']);
  final Color splashColor = _uClass(__m['splashColor']);
  final InteractiveInkFeatureFactory splashFactory = _uClass(__m['splashFactory']);
  final Color selectedRowColor = _uClass(__m['selectedRowColor']);
  final Color unselectedWidgetColor = _uClass(__m['unselectedWidgetColor']);
  final Color disabledColor = _uClass(__m['disabledColor']);
  final ButtonThemeData buttonTheme = _uClass(__m['buttonTheme']);
  final Color buttonColor = _uClass(__m['buttonColor']);
  final ToggleButtonsThemeData toggleButtonsTheme = _uClass(__m['toggleButtonsTheme']);
  final Color secondaryHeaderColor = _uClass(__m['secondaryHeaderColor']);
  final Color textSelectionColor = _uClass(__m['textSelectionColor']);
  final Color cursorColor = _uClass(__m['cursorColor']);
  final Color textSelectionHandleColor = _uClass(__m['textSelectionHandleColor']);
  final Color backgroundColor = _uClass(__m['backgroundColor']);
  final Color dialogBackgroundColor = _uClass(__m['dialogBackgroundColor']);
  final Color indicatorColor = _uClass(__m['indicatorColor']);
  final Color hintColor = _uClass(__m['hintColor']);
  final Color errorColor = _uClass(__m['errorColor']);
  final Color toggleableActiveColor = _uClass(__m['toggleableActiveColor']);
  final TextTheme textTheme = _uClass(__m['textTheme']);
  final TextTheme primaryTextTheme = _uClass(__m['primaryTextTheme']);
  final TextTheme accentTextTheme = _uClass(__m['accentTextTheme']);
  final InputDecorationTheme inputDecorationTheme = _uClass(__m['inputDecorationTheme']);
  final IconThemeData iconTheme = _uClass(__m['iconTheme']);
  final IconThemeData primaryIconTheme = _uClass(__m['primaryIconTheme']);
  final IconThemeData accentIconTheme = _uClass(__m['accentIconTheme']);
  final SliderThemeData sliderTheme = _uClass(__m['sliderTheme']);
  final TabBarTheme tabBarTheme = _uClass(__m['tabBarTheme']);
  final TooltipThemeData tooltipTheme = _uClass(__m['tooltipTheme']);
  final CardTheme cardTheme = _uClass(__m['cardTheme']);
  final ChipThemeData chipTheme = _uClass(__m['chipTheme']);
  final TargetPlatform platform = _uTargetPlatform(__m['platform']);
  final MaterialTapTargetSize materialTapTargetSize = _uMaterialTapTargetSize(__m['materialTapTargetSize']);
  final bool applyElevationOverlayColor = uBool(__m['applyElevationOverlayColor']);
  final PageTransitionsTheme pageTransitionsTheme = _uClass(__m['pageTransitionsTheme']);
  final AppBarTheme appBarTheme = _uClass(__m['appBarTheme']);
  final ScrollbarThemeData scrollbarTheme = _uClass(__m['scrollbarTheme']);
  final BottomAppBarTheme bottomAppBarTheme = _uClass(__m['bottomAppBarTheme']);
  final ColorScheme colorScheme = _uClass(__m['colorScheme']);
  final DialogTheme dialogTheme = _uClass(__m['dialogTheme']);
  final FloatingActionButtonThemeData floatingActionButtonTheme = _uClass(__m['floatingActionButtonTheme']);
  final NavigationRailThemeData navigationRailTheme = _uClass(__m['navigationRailTheme']);
  final Typography typography = _uClass(__m['typography']);
  final NoDefaultCupertinoThemeData? cupertinoOverrideTheme = _unClass(__m['cupertinoOverrideTheme']);
  final SnackBarThemeData snackBarTheme = _uClass(__m['snackBarTheme']);
  final BottomSheetThemeData bottomSheetTheme = _uClass(__m['bottomSheetTheme']);
  final PopupMenuThemeData popupMenuTheme = _uClass(__m['popupMenuTheme']);
  final MaterialBannerThemeData bannerTheme = _uClass(__m['bannerTheme']);
  final DividerThemeData dividerTheme = _uClass(__m['dividerTheme']);
  final ButtonBarThemeData buttonBarTheme = _uClass(__m['buttonBarTheme']);
  final BottomNavigationBarThemeData bottomNavigationBarTheme = _uClass(__m['bottomNavigationBarTheme']);
  final TimePickerThemeData timePickerTheme = _uClass(__m['timePickerTheme']);
  final TextButtonThemeData textButtonTheme = _uClass(__m['textButtonTheme']);
  final ElevatedButtonThemeData elevatedButtonTheme = _uClass(__m['elevatedButtonTheme']);
  final OutlinedButtonThemeData outlinedButtonTheme = _uClass(__m['outlinedButtonTheme']);
  final TextSelectionThemeData textSelectionTheme = _uClass(__m['textSelectionTheme']);
  final DataTableThemeData dataTableTheme = _uClass(__m['dataTableTheme']);
  final CheckboxThemeData checkboxTheme = _uClass(__m['checkboxTheme']);
  final RadioThemeData radioTheme = _uClass(__m['radioTheme']);
  final SwitchThemeData switchTheme = _uClass(__m['switchTheme']);
  final ProgressIndicatorThemeData progressIndicatorTheme = _uClass(__m['progressIndicatorTheme']);
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
  final ColorScheme colorScheme = _uClass(__m['colorScheme']);
  final TextTheme? textTheme = _unClass(__m['textTheme']);
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

ThemeMode? _unThemeMode(dynamic v) => v == null ? v : _uThemeMode(v);

DoNothingIntent _uDoNothingIntent(Map<String, dynamic> __m) {
  return DoNothingIntent(
  );
}

ScrollBehavior _uScrollBehavior(Map<String, dynamic> __m) {
  return ScrollBehavior(
  );
}

RouteInformation _uRouteInformation(Map<String, dynamic> __m) {
  final String location = uString(__m['location']);
  final Object? state = _unClass(__m['state']);
  return RouteInformation(
    location: location,
    state: state,
  );
}

_CallbackHookProvider _u_CallbackHookProvider(Map<String, dynamic> __m) {
  return _CallbackHookProvider(
  );
}

_StringStackTrace _u_StringStackTrace(Map<String, dynamic> __m) {
  final String _stackTrace = uString(__m['_stackTrace']);
  return _StringStackTrace(
    _stackTrace,
  );
}

MaterialApp _uMaterialApp(Map<String, dynamic> __m) {
  final Key? key = _unClass(__m['key']);
  final GlobalKey<NavigatorState>? navigatorKey = _unClass(__m['navigatorKey']);
  final GlobalKey<ScaffoldMessengerState>? scaffoldMessengerKey = _unClass(__m['scaffoldMessengerKey']);
  final Widget? home = _unClass(__m['home']);
  final Map<String, Widget Function(BuildContext)> routes = _uClass(__m['routes']);
  final String initialRoute = uString(__m['initialRoute']);
  final Route<dynamic>? Function(RouteSettings) onGenerateRoute = __m['onGenerateRoute'];
  final List<Route<dynamic>> Function(String) onGenerateInitialRoutes = __m['onGenerateInitialRoutes'];
  final Route<dynamic>? Function(RouteSettings) onUnknownRoute = __m['onUnknownRoute'];
  final List<NavigatorObserver> navigatorObservers = _uClass(__m['navigatorObservers']);
  final Widget Function(BuildContext, Widget?) builder = __m['builder'];
  final String title = uString(__m['title']);
  final String Function(BuildContext) onGenerateTitle = __m['onGenerateTitle'];
  final Color? color = _unClass(__m['color']);
  final ThemeData? theme = _unClass(__m['theme']);
  final ThemeData? darkTheme = _unClass(__m['darkTheme']);
  final ThemeData? highContrastTheme = _unClass(__m['highContrastTheme']);
  final ThemeData? highContrastDarkTheme = _unClass(__m['highContrastDarkTheme']);
  final ThemeMode? themeMode = _unThemeMode(__m['themeMode']);
  final Locale? locale = _unClass(__m['locale']);
  final Iterable<LocalizationsDelegate<dynamic>>? localizationsDelegates = _unClass(__m['localizationsDelegates']);
  final Locale? Function(List<Locale>?, Iterable<Locale>) localeListResolutionCallback = __m['localeListResolutionCallback'];
  final Locale? Function(Locale?, Iterable<Locale>) localeResolutionCallback = __m['localeResolutionCallback'];
  final Iterable<Locale> supportedLocales = _uClass(__m['supportedLocales']);
  final bool debugShowMaterialGrid = uBool(__m['debugShowMaterialGrid']);
  final bool showPerformanceOverlay = uBool(__m['showPerformanceOverlay']);
  final bool checkerboardRasterCacheImages = uBool(__m['checkerboardRasterCacheImages']);
  final bool checkerboardOffscreenLayers = uBool(__m['checkerboardOffscreenLayers']);
  final bool showSemanticsDebugger = uBool(__m['showSemanticsDebugger']);
  final bool debugShowCheckedModeBanner = uBool(__m['debugShowCheckedModeBanner']);
  final Map<ShortcutActivator, Intent>? shortcuts = _unClass(__m['shortcuts']);
  final Map<Type, Action<Intent>>? actions = _unClass(__m['actions']);
  final String restorationScopeId = uString(__m['restorationScopeId']);
  final ScrollBehavior? scrollBehavior = _unClass(__m['scrollBehavior']);
  final bool useInheritedMediaQuery = uBool(__m['useInheritedMediaQuery']);
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
  final Key? key = _unClass(__m['key']);
  final GlobalKey<ScaffoldMessengerState>? scaffoldMessengerKey = _unClass(__m['scaffoldMessengerKey']);
  final RouteInformationProvider? routeInformationProvider = _unClass(__m['routeInformationProvider']);
  final RouteInformationParser<Object> routeInformationParser = _uClass(__m['routeInformationParser']);
  final RouterDelegate<Object> routerDelegate = _uClass(__m['routerDelegate']);
  final BackButtonDispatcher? backButtonDispatcher = _unClass(__m['backButtonDispatcher']);
  final Widget Function(BuildContext, Widget?) builder = __m['builder'];
  final String title = uString(__m['title']);
  final String Function(BuildContext) onGenerateTitle = __m['onGenerateTitle'];
  final Color? color = _unClass(__m['color']);
  final ThemeData? theme = _unClass(__m['theme']);
  final ThemeData? darkTheme = _unClass(__m['darkTheme']);
  final ThemeData? highContrastTheme = _unClass(__m['highContrastTheme']);
  final ThemeData? highContrastDarkTheme = _unClass(__m['highContrastDarkTheme']);
  final ThemeMode? themeMode = _unThemeMode(__m['themeMode']);
  final Locale? locale = _unClass(__m['locale']);
  final Iterable<LocalizationsDelegate<dynamic>>? localizationsDelegates = _unClass(__m['localizationsDelegates']);
  final Locale? Function(List<Locale>?, Iterable<Locale>) localeListResolutionCallback = __m['localeListResolutionCallback'];
  final Locale? Function(Locale?, Iterable<Locale>) localeResolutionCallback = __m['localeResolutionCallback'];
  final Iterable<Locale> supportedLocales = _uClass(__m['supportedLocales']);
  final bool debugShowMaterialGrid = uBool(__m['debugShowMaterialGrid']);
  final bool showPerformanceOverlay = uBool(__m['showPerformanceOverlay']);
  final bool checkerboardRasterCacheImages = uBool(__m['checkerboardRasterCacheImages']);
  final bool checkerboardOffscreenLayers = uBool(__m['checkerboardOffscreenLayers']);
  final bool showSemanticsDebugger = uBool(__m['showSemanticsDebugger']);
  final bool debugShowCheckedModeBanner = uBool(__m['debugShowCheckedModeBanner']);
  final Map<ShortcutActivator, Intent>? shortcuts = _unClass(__m['shortcuts']);
  final Map<Type, Action<Intent>>? actions = _unClass(__m['actions']);
  final String restorationScopeId = uString(__m['restorationScopeId']);
  final ScrollBehavior? scrollBehavior = _unClass(__m['scrollBehavior']);
  final bool useInheritedMediaQuery = uBool(__m['useInheritedMediaQuery']);
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

KeyEventResult? _unKeyEventResult(dynamic v) => v == null ? v : _uKeyEventResult(v);

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
  final String debugLabel = uString(__m['debugLabel']);
  final KeyEventResult Function(FocusNode, RawKeyEvent) onKey = __m['onKey'];
  final KeyEventResult Function(FocusNode, KeyEvent) onKeyEvent = __m['onKeyEvent'];
  final bool skipTraversal = uBool(__m['skipTraversal']);
  final bool canRequestFocus = uBool(__m['canRequestFocus']);
  final bool descendantsAreFocusable = uBool(__m['descendantsAreFocusable']);
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
  final Key? key = _unClass(__m['key']);
  final void Function() onPressed = __m['onPressed'];
  final void Function() onLongPress = __m['onLongPress'];
  final ButtonStyle? style = _unClass(__m['style']);
  final FocusNode? focusNode = _unClass(__m['focusNode']);
  final bool autofocus = uBool(__m['autofocus']);
  final Clip clipBehavior = _uClip(__m['clipBehavior']);
  final Widget? child = _unClass(__m['child']);
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
  final Key? key = _unClass(__m['key']);
  final void Function() onPressed = __m['onPressed'];
  final void Function() onLongPress = __m['onLongPress'];
  final ButtonStyle? style = _unClass(__m['style']);
  final FocusNode? focusNode = _unClass(__m['focusNode']);
  final bool autofocus = uBool(__m['autofocus']);
  final Clip? clipBehavior = _unClip(__m['clipBehavior']);
  final Widget icon = _uClass(__m['icon']);
  final Widget label = _uClass(__m['label']);
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

typedef Unmarshal = dynamic Function(Map<String, dynamic> state);

final loaders = <String, Unmarshal>{
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
  '_CallbackHookProvider.': _u_CallbackHookProvider,
  '_StringStackTrace.': _u_StringStackTrace,
  'MaterialApp.': _uMaterialApp,
  'MaterialApp.router': _uMaterialAppRouter,
  'PhysicalKeyboardKey.': _uPhysicalKeyboardKey,
  'LogicalKeyboardKey.': _uLogicalKeyboardKey,
  'FocusNode.': _uFocusNode,
  'ElevatedButton.': _uElevatedButton,
  'ElevatedButton.icon': _uElevatedButtonIcon,
};
dynamic _uClass(dynamic m) => unmarshal(loaders, m);
dynamic _unClass(dynamic m) => m == null ? m : unmarshal(loaders, m);
