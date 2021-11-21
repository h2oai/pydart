import 'dart:ui';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/services.dart';

Object _uObject(Map<String, dynamic> __m) {
  return Object(
  );
}

RouteSettings _uRouteSettings(Map<String, dynamic> __m) {
  final String? name = __m['name'];
  final Object? arguments = __m['arguments'];
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
  final Key? key = __m['key'];
  final List<Page<dynamic>>? pages = __m['pages'];
  final func<Route<dynamic>, dynamic, bool>? onPopPage = __m['onPopPage'];
  final String? initialRoute = __m['initialRoute'];
  final func<NavigatorState, String, List<Route<dynamic>>>? onGenerateInitialRoutes = __m['onGenerateInitialRoutes'];
  final func<RouteSettings, Route<dynamic>>? onGenerateRoute = __m['onGenerateRoute'];
  final func<RouteSettings, Route<dynamic>>? onUnknownRoute = __m['onUnknownRoute'];
  final TransitionDelegate<dynamic>? transitionDelegate = __m['transitionDelegate'];
  final bool? reportsRouteUpdateToEngine = __m['reportsRouteUpdateToEngine'];
  final List<NavigatorObserver>? observers = __m['observers'];
  final String? restorationScopeId = __m['restorationScopeId'];
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
  final Key? key = __m['key'];
  final Widget child = __m['child'];
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
  final int value = __m['value'];
  return Color(
    value,
  );
}

Color _ufromARGBColor(Map<String, dynamic> __m) {
  final int a = __m['a'];
  final int r = __m['r'];
  final int g = __m['g'];
  final int b = __m['b'];
  return Color.fromARGB(
    a,
    r,
    g,
    b,
  );
}

Color _ufromRGBOColor(Map<String, dynamic> __m) {
  final int r = __m['r'];
  final int g = __m['g'];
  final int b = __m['b'];
  final double opacity = __m['opacity'];
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
  final double? horizontal = __m['horizontal'];
  final double? vertical = __m['vertical'];
  return VisualDensity(
    horizontal: horizontal,
    vertical: vertical,
  );
}

ColorSwatch _uColorSwatch(Map<String, dynamic> __m) {
  final int primary = __m['primary'];
  final Map<T, Color> _swatch = __m['_swatch'];
  return ColorSwatch(
    primary,
    _swatch,
  );
}

MaterialColor _uMaterialColor(Map<String, dynamic> __m) {
  final int primary = __m['primary'];
  final Map<int, Color> swatch = __m['swatch'];
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
  final Color primary = __m['primary'];
  final Color primaryVariant = __m['primaryVariant'];
  final Color secondary = __m['secondary'];
  final Color secondaryVariant = __m['secondaryVariant'];
  final Color surface = __m['surface'];
  final Color background = __m['background'];
  final Color error = __m['error'];
  final Color onPrimary = __m['onPrimary'];
  final Color onSecondary = __m['onSecondary'];
  final Color onSurface = __m['onSurface'];
  final Color onBackground = __m['onBackground'];
  final Color onError = __m['onError'];
  final Brightness brightness = __m['brightness'];
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

ColorScheme _ulightColorScheme(Map<String, dynamic> __m) {
  final Color? primary = __m['primary'];
  final Color? primaryVariant = __m['primaryVariant'];
  final Color? secondary = __m['secondary'];
  final Color? secondaryVariant = __m['secondaryVariant'];
  final Color? surface = __m['surface'];
  final Color? background = __m['background'];
  final Color? error = __m['error'];
  final Color? onPrimary = __m['onPrimary'];
  final Color? onSecondary = __m['onSecondary'];
  final Color? onSurface = __m['onSurface'];
  final Color? onBackground = __m['onBackground'];
  final Color? onError = __m['onError'];
  final Brightness? brightness = __m['brightness'];
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

ColorScheme _udarkColorScheme(Map<String, dynamic> __m) {
  final Color? primary = __m['primary'];
  final Color? primaryVariant = __m['primaryVariant'];
  final Color? secondary = __m['secondary'];
  final Color? secondaryVariant = __m['secondaryVariant'];
  final Color? surface = __m['surface'];
  final Color? background = __m['background'];
  final Color? error = __m['error'];
  final Color? onPrimary = __m['onPrimary'];
  final Color? onSecondary = __m['onSecondary'];
  final Color? onSurface = __m['onSurface'];
  final Color? onBackground = __m['onBackground'];
  final Color? onError = __m['onError'];
  final Brightness? brightness = __m['brightness'];
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

ColorScheme _uhighContrastLightColorScheme(Map<String, dynamic> __m) {
  final Color? primary = __m['primary'];
  final Color? primaryVariant = __m['primaryVariant'];
  final Color? secondary = __m['secondary'];
  final Color? secondaryVariant = __m['secondaryVariant'];
  final Color? surface = __m['surface'];
  final Color? background = __m['background'];
  final Color? error = __m['error'];
  final Color? onPrimary = __m['onPrimary'];
  final Color? onSecondary = __m['onSecondary'];
  final Color? onSurface = __m['onSurface'];
  final Color? onBackground = __m['onBackground'];
  final Color? onError = __m['onError'];
  final Brightness? brightness = __m['brightness'];
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

ColorScheme _uhighContrastDarkColorScheme(Map<String, dynamic> __m) {
  final Color? primary = __m['primary'];
  final Color? primaryVariant = __m['primaryVariant'];
  final Color? secondary = __m['secondary'];
  final Color? secondaryVariant = __m['secondaryVariant'];
  final Color? surface = __m['surface'];
  final Color? background = __m['background'];
  final Color? error = __m['error'];
  final Color? onPrimary = __m['onPrimary'];
  final Color? onSecondary = __m['onSecondary'];
  final Color? onSurface = __m['onSurface'];
  final Color? onBackground = __m['onBackground'];
  final Color? onError = __m['onError'];
  final Brightness? brightness = __m['brightness'];
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

ColorScheme _ufromSwatchColorScheme(Map<String, dynamic> __m) {
  final MaterialColor? primarySwatch = __m['primarySwatch'];
  final Color? primaryColorDark = __m['primaryColorDark'];
  final Color? accentColor = __m['accentColor'];
  final Color? cardColor = __m['cardColor'];
  final Color? backgroundColor = __m['backgroundColor'];
  final Color? errorColor = __m['errorColor'];
  final Brightness? brightness = __m['brightness'];
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
  final ButtonTextTheme? textTheme = __m['textTheme'];
  final double? minWidth = __m['minWidth'];
  final double? height = __m['height'];
  final EdgeInsetsGeometry? padding = __m['padding'];
  final ShapeBorder? shape = __m['shape'];
  final ButtonBarLayoutBehavior? layoutBehavior = __m['layoutBehavior'];
  final bool? alignedDropdown = __m['alignedDropdown'];
  final Color? buttonColor = __m['buttonColor'];
  final Color? disabledColor = __m['disabledColor'];
  final Color? focusColor = __m['focusColor'];
  final Color? hoverColor = __m['hoverColor'];
  final Color? highlightColor = __m['highlightColor'];
  final Color? splashColor = __m['splashColor'];
  final ColorScheme? colorScheme = __m['colorScheme'];
  final MaterialTapTargetSize? materialTapTargetSize = __m['materialTapTargetSize'];
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
  final String _languageCode = __m['_languageCode'];
  final String? _countryCode = __m['_countryCode'];
  return Locale(
    _languageCode,
    _countryCode,
  );
}

Locale _ufromSubtagsLocale(Map<String, dynamic> __m) {
  final String? languageCode = __m['languageCode'];
  final String? scriptCode = __m['scriptCode'];
  final String? countryCode = __m['countryCode'];
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
  final double dx = __m['dx'];
  final double dy = __m['dy'];
  return Offset(
    dx,
    dy,
  );
}

Offset _ufromDirectionOffset(Map<String, dynamic> __m) {
  final double direction = __m['direction'];
  final double? distance = __m['distance'];
  return Offset.fromDirection(
    direction,
    distance,
  );
}

Shadow _uShadow(Map<String, dynamic> __m) {
  final Color? color = __m['color'];
  final Offset? offset = __m['offset'];
  final double? blurRadius = __m['blurRadius'];
  return Shadow(
    color: color,
    offset: offset,
    blurRadius: blurRadius,
  );
}

FontFeature _uFontFeature(Map<String, dynamic> __m) {
  final String feature = __m['feature'];
  final int? value = __m['value'];
  return FontFeature(
    feature,
    value,
  );
}

FontFeature _uenableFontFeature(Map<String, dynamic> __m) {
  final String feature = __m['feature'];
  return FontFeature.enable(
    feature,
  );
}

FontFeature _udisableFontFeature(Map<String, dynamic> __m) {
  final String feature = __m['feature'];
  return FontFeature.disable(
    feature,
  );
}

FontFeature _ualternativeFontFeature(Map<String, dynamic> __m) {
  final int value = __m['value'];
  return FontFeature.alternative(
    value,
  );
}

FontFeature _ualternativeFractionsFontFeature(Map<String, dynamic> __m) {
  return FontFeature.alternativeFractions(
  );
}

FontFeature _ucontextualAlternatesFontFeature(Map<String, dynamic> __m) {
  return FontFeature.contextualAlternates(
  );
}

FontFeature _ucaseSensitiveFormsFontFeature(Map<String, dynamic> __m) {
  return FontFeature.caseSensitiveForms(
  );
}

FontFeature _ucharacterVariantFontFeature(Map<String, dynamic> __m) {
  final int value = __m['value'];
  return FontFeature.characterVariant(
    value,
  );
}

FontFeature _udenominatorFontFeature(Map<String, dynamic> __m) {
  return FontFeature.denominator(
  );
}

FontFeature _ufractionsFontFeature(Map<String, dynamic> __m) {
  return FontFeature.fractions(
  );
}

FontFeature _uhistoricalFormsFontFeature(Map<String, dynamic> __m) {
  return FontFeature.historicalForms(
  );
}

FontFeature _uhistoricalLigaturesFontFeature(Map<String, dynamic> __m) {
  return FontFeature.historicalLigatures(
  );
}

FontFeature _uliningFiguresFontFeature(Map<String, dynamic> __m) {
  return FontFeature.liningFigures(
  );
}

FontFeature _ulocaleAwareFontFeature(Map<String, dynamic> __m) {
  final bool? enable = __m['enable'];
  return FontFeature.localeAware(
    enable: enable,
  );
}

FontFeature _unotationalFormsFontFeature(Map<String, dynamic> __m) {
  final int? value = __m['value'];
  return FontFeature.notationalForms(
    value,
  );
}

FontFeature _unumeratorsFontFeature(Map<String, dynamic> __m) {
  return FontFeature.numerators(
  );
}

FontFeature _uoldstyleFiguresFontFeature(Map<String, dynamic> __m) {
  return FontFeature.oldstyleFigures(
  );
}

FontFeature _uordinalFormsFontFeature(Map<String, dynamic> __m) {
  return FontFeature.ordinalForms(
  );
}

FontFeature _uproportionalFiguresFontFeature(Map<String, dynamic> __m) {
  return FontFeature.proportionalFigures(
  );
}

FontFeature _urandomizeFontFeature(Map<String, dynamic> __m) {
  return FontFeature.randomize(
  );
}

FontFeature _ustylisticAlternatesFontFeature(Map<String, dynamic> __m) {
  return FontFeature.stylisticAlternates(
  );
}

FontFeature _uscientificInferiorsFontFeature(Map<String, dynamic> __m) {
  return FontFeature.scientificInferiors(
  );
}

FontFeature _ustylisticSetFontFeature(Map<String, dynamic> __m) {
  final int value = __m['value'];
  return FontFeature.stylisticSet(
    value,
  );
}

FontFeature _usubscriptsFontFeature(Map<String, dynamic> __m) {
  return FontFeature.subscripts(
  );
}

FontFeature _usuperscriptsFontFeature(Map<String, dynamic> __m) {
  return FontFeature.superscripts(
  );
}

FontFeature _uswashFontFeature(Map<String, dynamic> __m) {
  final int? value = __m['value'];
  return FontFeature.swash(
    value,
  );
}

FontFeature _utabularFiguresFontFeature(Map<String, dynamic> __m) {
  return FontFeature.tabularFigures(
  );
}

FontFeature _uslashedZeroFontFeature(Map<String, dynamic> __m) {
  return FontFeature.slashedZero(
  );
}

TextDecoration _ucombineTextDecoration(Map<String, dynamic> __m) {
  final List<TextDecoration> decorations = __m['decorations'];
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
  final bool? inherit = __m['inherit'];
  final Color? color = __m['color'];
  final Color? backgroundColor = __m['backgroundColor'];
  final double? fontSize = __m['fontSize'];
  final FontWeight? fontWeight = __m['fontWeight'];
  final FontStyle? fontStyle = __m['fontStyle'];
  final double? letterSpacing = __m['letterSpacing'];
  final double? wordSpacing = __m['wordSpacing'];
  final TextBaseline? textBaseline = __m['textBaseline'];
  final double? height = __m['height'];
  final TextLeadingDistribution? leadingDistribution = __m['leadingDistribution'];
  final Locale? locale = __m['locale'];
  final Paint? foreground = __m['foreground'];
  final Paint? background = __m['background'];
  final List<Shadow>? shadows = __m['shadows'];
  final List<FontFeature>? fontFeatures = __m['fontFeatures'];
  final TextDecoration? decoration = __m['decoration'];
  final Color? decorationColor = __m['decorationColor'];
  final TextDecorationStyle? decorationStyle = __m['decorationStyle'];
  final double? decorationThickness = __m['decorationThickness'];
  final String? debugLabel = __m['debugLabel'];
  final String? fontFamily = __m['fontFamily'];
  final List<String>? fontFamilyFallback = __m['fontFamilyFallback'];
  final String? package = __m['package'];
  final TextOverflow? overflow = __m['overflow'];
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
  final double width = __m['width'];
  final double height = __m['height'];
  return Size(
    width,
    height,
  );
}

Size _ucopySize(Map<String, dynamic> __m) {
  final Size source = __m['source'];
  return Size.copy(
    source,
  );
}

Size _usquareSize(Map<String, dynamic> __m) {
  final double dimension = __m['dimension'];
  return Size.square(
    dimension,
  );
}

Size _ufromWidthSize(Map<String, dynamic> __m) {
  final double width = __m['width'];
  return Size.fromWidth(
    width,
  );
}

Size _ufromHeightSize(Map<String, dynamic> __m) {
  final double height = __m['height'];
  return Size.fromHeight(
    height,
  );
}

Size _ufromRadiusSize(Map<String, dynamic> __m) {
  final double radius = __m['radius'];
  return Size.fromRadius(
    radius,
  );
}

BoxConstraints _uBoxConstraints(Map<String, dynamic> __m) {
  final double? minWidth = __m['minWidth'];
  final double? maxWidth = __m['maxWidth'];
  final double? minHeight = __m['minHeight'];
  final double? maxHeight = __m['maxHeight'];
  return BoxConstraints(
    minWidth: minWidth,
    maxWidth: maxWidth,
    minHeight: minHeight,
    maxHeight: maxHeight,
  );
}

BoxConstraints _utightBoxConstraints(Map<String, dynamic> __m) {
  final Size size = __m['size'];
  return BoxConstraints.tight(
    size,
  );
}

BoxConstraints _utightForBoxConstraints(Map<String, dynamic> __m) {
  final double? width = __m['width'];
  final double? height = __m['height'];
  return BoxConstraints.tightFor(
    width: width,
    height: height,
  );
}

BoxConstraints _utightForFiniteBoxConstraints(Map<String, dynamic> __m) {
  final double? width = __m['width'];
  final double? height = __m['height'];
  return BoxConstraints.tightForFinite(
    width: width,
    height: height,
  );
}

BoxConstraints _ulooseBoxConstraints(Map<String, dynamic> __m) {
  final Size size = __m['size'];
  return BoxConstraints.loose(
    size,
  );
}

BoxConstraints _uexpandBoxConstraints(Map<String, dynamic> __m) {
  final double? width = __m['width'];
  final double? height = __m['height'];
  return BoxConstraints.expand(
    width: width,
    height: height,
  );
}

Radius _ucircularRadius(Map<String, dynamic> __m) {
  final double radius = __m['radius'];
  return Radius.circular(
    radius,
  );
}

Radius _uellipticalRadius(Map<String, dynamic> __m) {
  final double x = __m['x'];
  final double y = __m['y'];
  return Radius.elliptical(
    x,
    y,
  );
}

BorderRadius _uallBorderRadius(Map<String, dynamic> __m) {
  final Radius radius = __m['radius'];
  return BorderRadius.all(
    radius,
  );
}

BorderRadius _ucircularBorderRadius(Map<String, dynamic> __m) {
  final double radius = __m['radius'];
  return BorderRadius.circular(
    radius,
  );
}

BorderRadius _uverticalBorderRadius(Map<String, dynamic> __m) {
  final Radius? top = __m['top'];
  final Radius? bottom = __m['bottom'];
  return BorderRadius.vertical(
    top: top,
    bottom: bottom,
  );
}

BorderRadius _uhorizontalBorderRadius(Map<String, dynamic> __m) {
  final Radius? left = __m['left'];
  final Radius? right = __m['right'];
  return BorderRadius.horizontal(
    left: left,
    right: right,
  );
}

BorderRadius _uonlyBorderRadius(Map<String, dynamic> __m) {
  final Radius? topLeft = __m['topLeft'];
  final Radius? topRight = __m['topRight'];
  final Radius? bottomLeft = __m['bottomLeft'];
  final Radius? bottomRight = __m['bottomRight'];
  return BorderRadius.only(
    topLeft: topLeft,
    topRight: topRight,
    bottomLeft: bottomLeft,
    bottomRight: bottomRight,
  );
}

ToggleButtonsThemeData _uToggleButtonsThemeData(Map<String, dynamic> __m) {
  final TextStyle? textStyle = __m['textStyle'];
  final BoxConstraints? constraints = __m['constraints'];
  final Color? color = __m['color'];
  final Color? selectedColor = __m['selectedColor'];
  final Color? disabledColor = __m['disabledColor'];
  final Color? fillColor = __m['fillColor'];
  final Color? focusColor = __m['focusColor'];
  final Color? highlightColor = __m['highlightColor'];
  final Color? hoverColor = __m['hoverColor'];
  final Color? splashColor = __m['splashColor'];
  final Color? borderColor = __m['borderColor'];
  final Color? selectedBorderColor = __m['selectedBorderColor'];
  final Color? disabledBorderColor = __m['disabledBorderColor'];
  final BorderRadius? borderRadius = __m['borderRadius'];
  final double? borderWidth = __m['borderWidth'];
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
  final TextStyle? headline1 = __m['headline1'];
  final TextStyle? headline2 = __m['headline2'];
  final TextStyle? headline3 = __m['headline3'];
  final TextStyle? headline4 = __m['headline4'];
  final TextStyle? headline5 = __m['headline5'];
  final TextStyle? headline6 = __m['headline6'];
  final TextStyle? subtitle1 = __m['subtitle1'];
  final TextStyle? subtitle2 = __m['subtitle2'];
  final TextStyle? bodyText1 = __m['bodyText1'];
  final TextStyle? bodyText2 = __m['bodyText2'];
  final TextStyle? caption = __m['caption'];
  final TextStyle? button = __m['button'];
  final TextStyle? overline = __m['overline'];
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
  final Color? color = __m['color'];
  final double? width = __m['width'];
  final BorderStyle? style = __m['style'];
  return BorderSide(
    color: color,
    width: width,
    style: style,
  );
}

InputDecorationTheme _uInputDecorationTheme(Map<String, dynamic> __m) {
  final TextStyle? labelStyle = __m['labelStyle'];
  final TextStyle? floatingLabelStyle = __m['floatingLabelStyle'];
  final TextStyle? helperStyle = __m['helperStyle'];
  final int? helperMaxLines = __m['helperMaxLines'];
  final TextStyle? hintStyle = __m['hintStyle'];
  final TextStyle? errorStyle = __m['errorStyle'];
  final int? errorMaxLines = __m['errorMaxLines'];
  final FloatingLabelBehavior? floatingLabelBehavior = __m['floatingLabelBehavior'];
  final bool? isDense = __m['isDense'];
  final EdgeInsetsGeometry? contentPadding = __m['contentPadding'];
  final bool? isCollapsed = __m['isCollapsed'];
  final TextStyle? prefixStyle = __m['prefixStyle'];
  final TextStyle? suffixStyle = __m['suffixStyle'];
  final TextStyle? counterStyle = __m['counterStyle'];
  final bool? filled = __m['filled'];
  final Color? fillColor = __m['fillColor'];
  final Color? focusColor = __m['focusColor'];
  final Color? hoverColor = __m['hoverColor'];
  final InputBorder? errorBorder = __m['errorBorder'];
  final InputBorder? focusedBorder = __m['focusedBorder'];
  final InputBorder? focusedErrorBorder = __m['focusedErrorBorder'];
  final InputBorder? disabledBorder = __m['disabledBorder'];
  final InputBorder? enabledBorder = __m['enabledBorder'];
  final InputBorder? border = __m['border'];
  final bool? alignLabelWithHint = __m['alignLabelWithHint'];
  final BoxConstraints? constraints = __m['constraints'];
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
  final Color? color = __m['color'];
  final double? opacity = __m['opacity'];
  final double? size = __m['size'];
  return IconThemeData(
    color: color,
    opacity: opacity,
    size: size,
  );
}

IconThemeData _ufallbackIconThemeData(Map<String, dynamic> __m) {
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
  final double start = __m['start'];
  final double end = __m['end'];
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
  final double? trackHeight = __m['trackHeight'];
  final Color? activeTrackColor = __m['activeTrackColor'];
  final Color? inactiveTrackColor = __m['inactiveTrackColor'];
  final Color? disabledActiveTrackColor = __m['disabledActiveTrackColor'];
  final Color? disabledInactiveTrackColor = __m['disabledInactiveTrackColor'];
  final Color? activeTickMarkColor = __m['activeTickMarkColor'];
  final Color? inactiveTickMarkColor = __m['inactiveTickMarkColor'];
  final Color? disabledActiveTickMarkColor = __m['disabledActiveTickMarkColor'];
  final Color? disabledInactiveTickMarkColor = __m['disabledInactiveTickMarkColor'];
  final Color? thumbColor = __m['thumbColor'];
  final Color? overlappingShapeStrokeColor = __m['overlappingShapeStrokeColor'];
  final Color? disabledThumbColor = __m['disabledThumbColor'];
  final Color? overlayColor = __m['overlayColor'];
  final Color? valueIndicatorColor = __m['valueIndicatorColor'];
  final SliderComponentShape? overlayShape = __m['overlayShape'];
  final SliderTickMarkShape? tickMarkShape = __m['tickMarkShape'];
  final SliderComponentShape? thumbShape = __m['thumbShape'];
  final SliderTrackShape? trackShape = __m['trackShape'];
  final SliderComponentShape? valueIndicatorShape = __m['valueIndicatorShape'];
  final RangeSliderTickMarkShape? rangeTickMarkShape = __m['rangeTickMarkShape'];
  final RangeSliderThumbShape? rangeThumbShape = __m['rangeThumbShape'];
  final RangeSliderTrackShape? rangeTrackShape = __m['rangeTrackShape'];
  final RangeSliderValueIndicatorShape? rangeValueIndicatorShape = __m['rangeValueIndicatorShape'];
  final ShowValueIndicator? showValueIndicator = __m['showValueIndicator'];
  final TextStyle? valueIndicatorTextStyle = __m['valueIndicatorTextStyle'];
  final double? minThumbSeparation = __m['minThumbSeparation'];
  final func<TextDirection, RangeValues, double, Size, Size, double, Thumb>? thumbSelector = __m['thumbSelector'];
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

SliderThemeData _ufromPrimaryColorsSliderThemeData(Map<String, dynamic> __m) {
  final Color primaryColor = __m['primaryColor'];
  final Color primaryColorDark = __m['primaryColorDark'];
  final Color primaryColorLight = __m['primaryColorLight'];
  final TextStyle valueIndicatorTextStyle = __m['valueIndicatorTextStyle'];
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
  final Decoration? indicator = __m['indicator'];
  final TabBarIndicatorSize? indicatorSize = __m['indicatorSize'];
  final Color? labelColor = __m['labelColor'];
  final EdgeInsetsGeometry? labelPadding = __m['labelPadding'];
  final TextStyle? labelStyle = __m['labelStyle'];
  final Color? unselectedLabelColor = __m['unselectedLabelColor'];
  final TextStyle? unselectedLabelStyle = __m['unselectedLabelStyle'];
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
  final int? days = __m['days'];
  final int? hours = __m['hours'];
  final int? minutes = __m['minutes'];
  final int? seconds = __m['seconds'];
  final int? milliseconds = __m['milliseconds'];
  final int? microseconds = __m['microseconds'];
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
  final double? height = __m['height'];
  final EdgeInsetsGeometry? padding = __m['padding'];
  final EdgeInsetsGeometry? margin = __m['margin'];
  final double? verticalOffset = __m['verticalOffset'];
  final bool? preferBelow = __m['preferBelow'];
  final bool? excludeFromSemantics = __m['excludeFromSemantics'];
  final Decoration? decoration = __m['decoration'];
  final TextStyle? textStyle = __m['textStyle'];
  final Duration? waitDuration = __m['waitDuration'];
  final Duration? showDuration = __m['showDuration'];
  final TooltipTriggerMode? triggerMode = __m['triggerMode'];
  final bool? enableFeedback = __m['enableFeedback'];
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
  final Clip? clipBehavior = __m['clipBehavior'];
  final Color? color = __m['color'];
  final Color? shadowColor = __m['shadowColor'];
  final double? elevation = __m['elevation'];
  final EdgeInsetsGeometry? margin = __m['margin'];
  final ShapeBorder? shape = __m['shape'];
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
  final Color backgroundColor = __m['backgroundColor'];
  final Color? deleteIconColor = __m['deleteIconColor'];
  final Color disabledColor = __m['disabledColor'];
  final Color selectedColor = __m['selectedColor'];
  final Color secondarySelectedColor = __m['secondarySelectedColor'];
  final Color? shadowColor = __m['shadowColor'];
  final Color? selectedShadowColor = __m['selectedShadowColor'];
  final bool? showCheckmark = __m['showCheckmark'];
  final Color? checkmarkColor = __m['checkmarkColor'];
  final EdgeInsetsGeometry? labelPadding = __m['labelPadding'];
  final EdgeInsetsGeometry padding = __m['padding'];
  final BorderSide? side = __m['side'];
  final OutlinedBorder? shape = __m['shape'];
  final TextStyle labelStyle = __m['labelStyle'];
  final TextStyle secondaryLabelStyle = __m['secondaryLabelStyle'];
  final Brightness brightness = __m['brightness'];
  final double? elevation = __m['elevation'];
  final double? pressElevation = __m['pressElevation'];
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

ChipThemeData _ufromDefaultsChipThemeData(Map<String, dynamic> __m) {
  final Brightness? brightness = __m['brightness'];
  final Color? primaryColor = __m['primaryColor'];
  final Color secondaryColor = __m['secondaryColor'];
  final TextStyle labelStyle = __m['labelStyle'];
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
  final Map<TargetPlatform, PageTransitionsBuilder>? builders = __m['builders'];
  return PageTransitionsTheme(
    builders: builders,
  );
}

SystemUiOverlayStyle _uSystemUiOverlayStyle(Map<String, dynamic> __m) {
  final Color? systemNavigationBarColor = __m['systemNavigationBarColor'];
  final Color? systemNavigationBarDividerColor = __m['systemNavigationBarDividerColor'];
  final Brightness? systemNavigationBarIconBrightness = __m['systemNavigationBarIconBrightness'];
  final bool? systemNavigationBarContrastEnforced = __m['systemNavigationBarContrastEnforced'];
  final Color? statusBarColor = __m['statusBarColor'];
  final Brightness? statusBarBrightness = __m['statusBarBrightness'];
  final Brightness? statusBarIconBrightness = __m['statusBarIconBrightness'];
  final bool? systemStatusBarContrastEnforced = __m['systemStatusBarContrastEnforced'];
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
  final Brightness? brightness = __m['brightness'];
  final Color? color = __m['color'];
  final Color? backgroundColor = __m['backgroundColor'];
  final Color? foregroundColor = __m['foregroundColor'];
  final double? elevation = __m['elevation'];
  final Color? shadowColor = __m['shadowColor'];
  final ShapeBorder? shape = __m['shape'];
  final IconThemeData? iconTheme = __m['iconTheme'];
  final IconThemeData? actionsIconTheme = __m['actionsIconTheme'];
  final TextTheme? textTheme = __m['textTheme'];
  final bool? centerTitle = __m['centerTitle'];
  final double? titleSpacing = __m['titleSpacing'];
  final double? toolbarHeight = __m['toolbarHeight'];
  final TextStyle? toolbarTextStyle = __m['toolbarTextStyle'];
  final TextStyle? titleTextStyle = __m['titleTextStyle'];
  final SystemUiOverlayStyle? systemOverlayStyle = __m['systemOverlayStyle'];
  final bool? backwardsCompatibility = __m['backwardsCompatibility'];
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
  final MaterialStateProperty<double>? thickness = __m['thickness'];
  final bool? showTrackOnHover = __m['showTrackOnHover'];
  final bool? isAlwaysShown = __m['isAlwaysShown'];
  final Radius? radius = __m['radius'];
  final MaterialStateProperty<Color>? thumbColor = __m['thumbColor'];
  final MaterialStateProperty<Color>? trackColor = __m['trackColor'];
  final MaterialStateProperty<Color>? trackBorderColor = __m['trackBorderColor'];
  final double? crossAxisMargin = __m['crossAxisMargin'];
  final double? mainAxisMargin = __m['mainAxisMargin'];
  final double? minThumbLength = __m['minThumbLength'];
  final bool? interactive = __m['interactive'];
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
  final Color? color = __m['color'];
  final double? elevation = __m['elevation'];
  final NotchedShape? shape = __m['shape'];
  return BottomAppBarTheme(
    color: color,
    elevation: elevation,
    shape: shape,
  );
}

DialogTheme _uDialogTheme(Map<String, dynamic> __m) {
  final Color? backgroundColor = __m['backgroundColor'];
  final double? elevation = __m['elevation'];
  final ShapeBorder? shape = __m['shape'];
  final TextStyle? titleTextStyle = __m['titleTextStyle'];
  final TextStyle? contentTextStyle = __m['contentTextStyle'];
  return DialogTheme(
    backgroundColor: backgroundColor,
    elevation: elevation,
    shape: shape,
    titleTextStyle: titleTextStyle,
    contentTextStyle: contentTextStyle,
  );
}

FloatingActionButtonThemeData _uFloatingActionButtonThemeData(Map<String, dynamic> __m) {
  final Color? foregroundColor = __m['foregroundColor'];
  final Color? backgroundColor = __m['backgroundColor'];
  final Color? focusColor = __m['focusColor'];
  final Color? hoverColor = __m['hoverColor'];
  final Color? splashColor = __m['splashColor'];
  final double? elevation = __m['elevation'];
  final double? focusElevation = __m['focusElevation'];
  final double? hoverElevation = __m['hoverElevation'];
  final double? disabledElevation = __m['disabledElevation'];
  final double? highlightElevation = __m['highlightElevation'];
  final ShapeBorder? shape = __m['shape'];
  final bool? enableFeedback = __m['enableFeedback'];
  final BoxConstraints? sizeConstraints = __m['sizeConstraints'];
  final BoxConstraints? smallSizeConstraints = __m['smallSizeConstraints'];
  final BoxConstraints? largeSizeConstraints = __m['largeSizeConstraints'];
  final BoxConstraints? extendedSizeConstraints = __m['extendedSizeConstraints'];
  final double? extendedIconLabelSpacing = __m['extendedIconLabelSpacing'];
  final EdgeInsetsGeometry? extendedPadding = __m['extendedPadding'];
  final TextStyle? extendedTextStyle = __m['extendedTextStyle'];
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
  final Color? backgroundColor = __m['backgroundColor'];
  final double? elevation = __m['elevation'];
  final TextStyle? unselectedLabelTextStyle = __m['unselectedLabelTextStyle'];
  final TextStyle? selectedLabelTextStyle = __m['selectedLabelTextStyle'];
  final IconThemeData? unselectedIconTheme = __m['unselectedIconTheme'];
  final IconThemeData? selectedIconTheme = __m['selectedIconTheme'];
  final double? groupAlignment = __m['groupAlignment'];
  final NavigationRailLabelType? labelType = __m['labelType'];
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
  final TargetPlatform? platform = __m['platform'];
  final TextTheme? black = __m['black'];
  final TextTheme? white = __m['white'];
  final TextTheme? englishLike = __m['englishLike'];
  final TextTheme? dense = __m['dense'];
  final TextTheme? tall = __m['tall'];
  return Typography(
    platform: platform,
    black: black,
    white: white,
    englishLike: englishLike,
    dense: dense,
    tall: tall,
  );
}

Typography _umaterial2014Typography(Map<String, dynamic> __m) {
  final TargetPlatform? platform = __m['platform'];
  final TextTheme? black = __m['black'];
  final TextTheme? white = __m['white'];
  final TextTheme? englishLike = __m['englishLike'];
  final TextTheme? dense = __m['dense'];
  final TextTheme? tall = __m['tall'];
  return Typography.material2014(
    platform: platform,
    black: black,
    white: white,
    englishLike: englishLike,
    dense: dense,
    tall: tall,
  );
}

Typography _umaterial2018Typography(Map<String, dynamic> __m) {
  final TargetPlatform? platform = __m['platform'];
  final TextTheme? black = __m['black'];
  final TextTheme? white = __m['white'];
  final TextTheme? englishLike = __m['englishLike'];
  final TextTheme? dense = __m['dense'];
  final TextTheme? tall = __m['tall'];
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
  final Color? primaryColor = __m['primaryColor'];
  final TextStyle? textStyle = __m['textStyle'];
  final TextStyle? actionTextStyle = __m['actionTextStyle'];
  final TextStyle? tabLabelTextStyle = __m['tabLabelTextStyle'];
  final TextStyle? navTitleTextStyle = __m['navTitleTextStyle'];
  final TextStyle? navLargeTitleTextStyle = __m['navLargeTitleTextStyle'];
  final TextStyle? navActionTextStyle = __m['navActionTextStyle'];
  final TextStyle? pickerTextStyle = __m['pickerTextStyle'];
  final TextStyle? dateTimePickerTextStyle = __m['dateTimePickerTextStyle'];
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
  final Brightness? brightness = __m['brightness'];
  final Color? primaryColor = __m['primaryColor'];
  final Color? primaryContrastingColor = __m['primaryContrastingColor'];
  final CupertinoTextThemeData? textTheme = __m['textTheme'];
  final Color? barBackgroundColor = __m['barBackgroundColor'];
  final Color? scaffoldBackgroundColor = __m['scaffoldBackgroundColor'];
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
  final Color? backgroundColor = __m['backgroundColor'];
  final Color? actionTextColor = __m['actionTextColor'];
  final Color? disabledActionTextColor = __m['disabledActionTextColor'];
  final TextStyle? contentTextStyle = __m['contentTextStyle'];
  final double? elevation = __m['elevation'];
  final ShapeBorder? shape = __m['shape'];
  final SnackBarBehavior? behavior = __m['behavior'];
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
  final Color? backgroundColor = __m['backgroundColor'];
  final double? elevation = __m['elevation'];
  final Color? modalBackgroundColor = __m['modalBackgroundColor'];
  final double? modalElevation = __m['modalElevation'];
  final ShapeBorder? shape = __m['shape'];
  final Clip? clipBehavior = __m['clipBehavior'];
  final BoxConstraints? constraints = __m['constraints'];
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
  final Color? color = __m['color'];
  final ShapeBorder? shape = __m['shape'];
  final double? elevation = __m['elevation'];
  final TextStyle? textStyle = __m['textStyle'];
  final bool? enableFeedback = __m['enableFeedback'];
  return PopupMenuThemeData(
    color: color,
    shape: shape,
    elevation: elevation,
    textStyle: textStyle,
    enableFeedback: enableFeedback,
  );
}

MaterialBannerThemeData _uMaterialBannerThemeData(Map<String, dynamic> __m) {
  final Color? backgroundColor = __m['backgroundColor'];
  final TextStyle? contentTextStyle = __m['contentTextStyle'];
  final EdgeInsetsGeometry? padding = __m['padding'];
  final EdgeInsetsGeometry? leadingPadding = __m['leadingPadding'];
  return MaterialBannerThemeData(
    backgroundColor: backgroundColor,
    contentTextStyle: contentTextStyle,
    padding: padding,
    leadingPadding: leadingPadding,
  );
}

DividerThemeData _uDividerThemeData(Map<String, dynamic> __m) {
  final Color? color = __m['color'];
  final double? space = __m['space'];
  final double? thickness = __m['thickness'];
  final double? indent = __m['indent'];
  final double? endIndent = __m['endIndent'];
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
  final MainAxisAlignment? alignment = __m['alignment'];
  final MainAxisSize? mainAxisSize = __m['mainAxisSize'];
  final ButtonTextTheme? buttonTextTheme = __m['buttonTextTheme'];
  final double? buttonMinWidth = __m['buttonMinWidth'];
  final double? buttonHeight = __m['buttonHeight'];
  final EdgeInsetsGeometry? buttonPadding = __m['buttonPadding'];
  final bool? buttonAlignedDropdown = __m['buttonAlignedDropdown'];
  final ButtonBarLayoutBehavior? layoutBehavior = __m['layoutBehavior'];
  final VerticalDirection? overflowDirection = __m['overflowDirection'];
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
  final Color? backgroundColor = __m['backgroundColor'];
  final double? elevation = __m['elevation'];
  final IconThemeData? selectedIconTheme = __m['selectedIconTheme'];
  final IconThemeData? unselectedIconTheme = __m['unselectedIconTheme'];
  final Color? selectedItemColor = __m['selectedItemColor'];
  final Color? unselectedItemColor = __m['unselectedItemColor'];
  final TextStyle? selectedLabelStyle = __m['selectedLabelStyle'];
  final TextStyle? unselectedLabelStyle = __m['unselectedLabelStyle'];
  final bool? showSelectedLabels = __m['showSelectedLabels'];
  final bool? showUnselectedLabels = __m['showUnselectedLabels'];
  final BottomNavigationBarType? type = __m['type'];
  final bool? enableFeedback = __m['enableFeedback'];
  final BottomNavigationBarLandscapeLayout? landscapeLayout = __m['landscapeLayout'];
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
  final Color? backgroundColor = __m['backgroundColor'];
  final Color? hourMinuteTextColor = __m['hourMinuteTextColor'];
  final Color? hourMinuteColor = __m['hourMinuteColor'];
  final Color? dayPeriodTextColor = __m['dayPeriodTextColor'];
  final Color? dayPeriodColor = __m['dayPeriodColor'];
  final Color? dialHandColor = __m['dialHandColor'];
  final Color? dialBackgroundColor = __m['dialBackgroundColor'];
  final Color? dialTextColor = __m['dialTextColor'];
  final Color? entryModeIconColor = __m['entryModeIconColor'];
  final TextStyle? hourMinuteTextStyle = __m['hourMinuteTextStyle'];
  final TextStyle? dayPeriodTextStyle = __m['dayPeriodTextStyle'];
  final TextStyle? helpTextStyle = __m['helpTextStyle'];
  final ShapeBorder? shape = __m['shape'];
  final ShapeBorder? hourMinuteShape = __m['hourMinuteShape'];
  final OutlinedBorder? dayPeriodShape = __m['dayPeriodShape'];
  final BorderSide? dayPeriodBorderSide = __m['dayPeriodBorderSide'];
  final InputDecorationTheme? inputDecorationTheme = __m['inputDecorationTheme'];
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
  final MaterialStateProperty<TextStyle>? textStyle = __m['textStyle'];
  final MaterialStateProperty<Color>? backgroundColor = __m['backgroundColor'];
  final MaterialStateProperty<Color>? foregroundColor = __m['foregroundColor'];
  final MaterialStateProperty<Color>? overlayColor = __m['overlayColor'];
  final MaterialStateProperty<Color>? shadowColor = __m['shadowColor'];
  final MaterialStateProperty<double>? elevation = __m['elevation'];
  final MaterialStateProperty<EdgeInsetsGeometry>? padding = __m['padding'];
  final MaterialStateProperty<Size>? minimumSize = __m['minimumSize'];
  final MaterialStateProperty<Size>? fixedSize = __m['fixedSize'];
  final MaterialStateProperty<Size>? maximumSize = __m['maximumSize'];
  final MaterialStateProperty<BorderSide>? side = __m['side'];
  final MaterialStateProperty<OutlinedBorder>? shape = __m['shape'];
  final MaterialStateProperty<MouseCursor>? mouseCursor = __m['mouseCursor'];
  final VisualDensity? visualDensity = __m['visualDensity'];
  final MaterialTapTargetSize? tapTargetSize = __m['tapTargetSize'];
  final Duration? animationDuration = __m['animationDuration'];
  final bool? enableFeedback = __m['enableFeedback'];
  final AlignmentGeometry? alignment = __m['alignment'];
  final InteractiveInkFeatureFactory? splashFactory = __m['splashFactory'];
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
  final ButtonStyle? style = __m['style'];
  return TextButtonThemeData(
    style: style,
  );
}

ElevatedButtonThemeData _uElevatedButtonThemeData(Map<String, dynamic> __m) {
  final ButtonStyle? style = __m['style'];
  return ElevatedButtonThemeData(
    style: style,
  );
}

OutlinedButtonThemeData _uOutlinedButtonThemeData(Map<String, dynamic> __m) {
  final ButtonStyle? style = __m['style'];
  return OutlinedButtonThemeData(
    style: style,
  );
}

TextSelectionThemeData _uTextSelectionThemeData(Map<String, dynamic> __m) {
  final Color? cursorColor = __m['cursorColor'];
  final Color? selectionColor = __m['selectionColor'];
  final Color? selectionHandleColor = __m['selectionHandleColor'];
  return TextSelectionThemeData(
    cursorColor: cursorColor,
    selectionColor: selectionColor,
    selectionHandleColor: selectionHandleColor,
  );
}

DataTableThemeData _uDataTableThemeData(Map<String, dynamic> __m) {
  final Decoration? decoration = __m['decoration'];
  final MaterialStateProperty<Color>? dataRowColor = __m['dataRowColor'];
  final double? dataRowHeight = __m['dataRowHeight'];
  final TextStyle? dataTextStyle = __m['dataTextStyle'];
  final MaterialStateProperty<Color>? headingRowColor = __m['headingRowColor'];
  final double? headingRowHeight = __m['headingRowHeight'];
  final TextStyle? headingTextStyle = __m['headingTextStyle'];
  final double? horizontalMargin = __m['horizontalMargin'];
  final double? columnSpacing = __m['columnSpacing'];
  final double? dividerThickness = __m['dividerThickness'];
  final double? checkboxHorizontalMargin = __m['checkboxHorizontalMargin'];
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
  final MaterialStateProperty<MouseCursor>? mouseCursor = __m['mouseCursor'];
  final MaterialStateProperty<Color>? fillColor = __m['fillColor'];
  final MaterialStateProperty<Color>? checkColor = __m['checkColor'];
  final MaterialStateProperty<Color>? overlayColor = __m['overlayColor'];
  final double? splashRadius = __m['splashRadius'];
  final MaterialTapTargetSize? materialTapTargetSize = __m['materialTapTargetSize'];
  final VisualDensity? visualDensity = __m['visualDensity'];
  final OutlinedBorder? shape = __m['shape'];
  final BorderSide? side = __m['side'];
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
  final MaterialStateProperty<MouseCursor>? mouseCursor = __m['mouseCursor'];
  final MaterialStateProperty<Color>? fillColor = __m['fillColor'];
  final MaterialStateProperty<Color>? overlayColor = __m['overlayColor'];
  final double? splashRadius = __m['splashRadius'];
  final MaterialTapTargetSize? materialTapTargetSize = __m['materialTapTargetSize'];
  final VisualDensity? visualDensity = __m['visualDensity'];
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
  final MaterialStateProperty<Color>? thumbColor = __m['thumbColor'];
  final MaterialStateProperty<Color>? trackColor = __m['trackColor'];
  final MaterialTapTargetSize? materialTapTargetSize = __m['materialTapTargetSize'];
  final MaterialStateProperty<MouseCursor>? mouseCursor = __m['mouseCursor'];
  final MaterialStateProperty<Color>? overlayColor = __m['overlayColor'];
  final double? splashRadius = __m['splashRadius'];
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
  final Color? color = __m['color'];
  final Color? linearTrackColor = __m['linearTrackColor'];
  final double? linearMinHeight = __m['linearMinHeight'];
  final Color? circularTrackColor = __m['circularTrackColor'];
  final Color? refreshBackgroundColor = __m['refreshBackgroundColor'];
  return ProgressIndicatorThemeData(
    color: color,
    linearTrackColor: linearTrackColor,
    linearMinHeight: linearMinHeight,
    circularTrackColor: circularTrackColor,
    refreshBackgroundColor: refreshBackgroundColor,
  );
}

ThemeData _uThemeData(Map<String, dynamic> __m) {
  final Brightness? brightness = __m['brightness'];
  final VisualDensity? visualDensity = __m['visualDensity'];
  final MaterialColor? primarySwatch = __m['primarySwatch'];
  final Color? primaryColor = __m['primaryColor'];
  final Brightness? primaryColorBrightness = __m['primaryColorBrightness'];
  final Color? primaryColorLight = __m['primaryColorLight'];
  final Color? primaryColorDark = __m['primaryColorDark'];
  final Color? accentColor = __m['accentColor'];
  final Brightness? accentColorBrightness = __m['accentColorBrightness'];
  final Color? canvasColor = __m['canvasColor'];
  final Color? shadowColor = __m['shadowColor'];
  final Color? scaffoldBackgroundColor = __m['scaffoldBackgroundColor'];
  final Color? bottomAppBarColor = __m['bottomAppBarColor'];
  final Color? cardColor = __m['cardColor'];
  final Color? dividerColor = __m['dividerColor'];
  final Color? focusColor = __m['focusColor'];
  final Color? hoverColor = __m['hoverColor'];
  final Color? highlightColor = __m['highlightColor'];
  final Color? splashColor = __m['splashColor'];
  final InteractiveInkFeatureFactory? splashFactory = __m['splashFactory'];
  final Color? selectedRowColor = __m['selectedRowColor'];
  final Color? unselectedWidgetColor = __m['unselectedWidgetColor'];
  final Color? disabledColor = __m['disabledColor'];
  final Color? buttonColor = __m['buttonColor'];
  final ButtonThemeData? buttonTheme = __m['buttonTheme'];
  final ToggleButtonsThemeData? toggleButtonsTheme = __m['toggleButtonsTheme'];
  final Color? secondaryHeaderColor = __m['secondaryHeaderColor'];
  final Color? textSelectionColor = __m['textSelectionColor'];
  final Color? cursorColor = __m['cursorColor'];
  final Color? textSelectionHandleColor = __m['textSelectionHandleColor'];
  final Color? backgroundColor = __m['backgroundColor'];
  final Color? dialogBackgroundColor = __m['dialogBackgroundColor'];
  final Color? indicatorColor = __m['indicatorColor'];
  final Color? hintColor = __m['hintColor'];
  final Color? errorColor = __m['errorColor'];
  final Color? toggleableActiveColor = __m['toggleableActiveColor'];
  final String? fontFamily = __m['fontFamily'];
  final TextTheme? textTheme = __m['textTheme'];
  final TextTheme? primaryTextTheme = __m['primaryTextTheme'];
  final TextTheme? accentTextTheme = __m['accentTextTheme'];
  final InputDecorationTheme? inputDecorationTheme = __m['inputDecorationTheme'];
  final IconThemeData? iconTheme = __m['iconTheme'];
  final IconThemeData? primaryIconTheme = __m['primaryIconTheme'];
  final IconThemeData? accentIconTheme = __m['accentIconTheme'];
  final SliderThemeData? sliderTheme = __m['sliderTheme'];
  final TabBarTheme? tabBarTheme = __m['tabBarTheme'];
  final TooltipThemeData? tooltipTheme = __m['tooltipTheme'];
  final CardTheme? cardTheme = __m['cardTheme'];
  final ChipThemeData? chipTheme = __m['chipTheme'];
  final TargetPlatform? platform = __m['platform'];
  final MaterialTapTargetSize? materialTapTargetSize = __m['materialTapTargetSize'];
  final bool? applyElevationOverlayColor = __m['applyElevationOverlayColor'];
  final PageTransitionsTheme? pageTransitionsTheme = __m['pageTransitionsTheme'];
  final AppBarTheme? appBarTheme = __m['appBarTheme'];
  final ScrollbarThemeData? scrollbarTheme = __m['scrollbarTheme'];
  final BottomAppBarTheme? bottomAppBarTheme = __m['bottomAppBarTheme'];
  final ColorScheme? colorScheme = __m['colorScheme'];
  final DialogTheme? dialogTheme = __m['dialogTheme'];
  final FloatingActionButtonThemeData? floatingActionButtonTheme = __m['floatingActionButtonTheme'];
  final NavigationRailThemeData? navigationRailTheme = __m['navigationRailTheme'];
  final Typography? typography = __m['typography'];
  final NoDefaultCupertinoThemeData? cupertinoOverrideTheme = __m['cupertinoOverrideTheme'];
  final SnackBarThemeData? snackBarTheme = __m['snackBarTheme'];
  final BottomSheetThemeData? bottomSheetTheme = __m['bottomSheetTheme'];
  final PopupMenuThemeData? popupMenuTheme = __m['popupMenuTheme'];
  final MaterialBannerThemeData? bannerTheme = __m['bannerTheme'];
  final DividerThemeData? dividerTheme = __m['dividerTheme'];
  final ButtonBarThemeData? buttonBarTheme = __m['buttonBarTheme'];
  final BottomNavigationBarThemeData? bottomNavigationBarTheme = __m['bottomNavigationBarTheme'];
  final TimePickerThemeData? timePickerTheme = __m['timePickerTheme'];
  final TextButtonThemeData? textButtonTheme = __m['textButtonTheme'];
  final ElevatedButtonThemeData? elevatedButtonTheme = __m['elevatedButtonTheme'];
  final OutlinedButtonThemeData? outlinedButtonTheme = __m['outlinedButtonTheme'];
  final TextSelectionThemeData? textSelectionTheme = __m['textSelectionTheme'];
  final DataTableThemeData? dataTableTheme = __m['dataTableTheme'];
  final CheckboxThemeData? checkboxTheme = __m['checkboxTheme'];
  final RadioThemeData? radioTheme = __m['radioTheme'];
  final SwitchThemeData? switchTheme = __m['switchTheme'];
  final ProgressIndicatorThemeData? progressIndicatorTheme = __m['progressIndicatorTheme'];
  final bool? fixTextFieldOutlineLabel = __m['fixTextFieldOutlineLabel'];
  final bool? useTextSelectionTheme = __m['useTextSelectionTheme'];
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

ThemeData _urawThemeData(Map<String, dynamic> __m) {
  final VisualDensity visualDensity = __m['visualDensity'];
  final Color primaryColor = __m['primaryColor'];
  final Brightness primaryColorBrightness = __m['primaryColorBrightness'];
  final Color primaryColorLight = __m['primaryColorLight'];
  final Color primaryColorDark = __m['primaryColorDark'];
  final Color canvasColor = __m['canvasColor'];
  final Color shadowColor = __m['shadowColor'];
  final Color accentColor = __m['accentColor'];
  final Brightness accentColorBrightness = __m['accentColorBrightness'];
  final Color scaffoldBackgroundColor = __m['scaffoldBackgroundColor'];
  final Color bottomAppBarColor = __m['bottomAppBarColor'];
  final Color cardColor = __m['cardColor'];
  final Color dividerColor = __m['dividerColor'];
  final Color focusColor = __m['focusColor'];
  final Color hoverColor = __m['hoverColor'];
  final Color highlightColor = __m['highlightColor'];
  final Color splashColor = __m['splashColor'];
  final InteractiveInkFeatureFactory splashFactory = __m['splashFactory'];
  final Color selectedRowColor = __m['selectedRowColor'];
  final Color unselectedWidgetColor = __m['unselectedWidgetColor'];
  final Color disabledColor = __m['disabledColor'];
  final ButtonThemeData buttonTheme = __m['buttonTheme'];
  final Color buttonColor = __m['buttonColor'];
  final ToggleButtonsThemeData toggleButtonsTheme = __m['toggleButtonsTheme'];
  final Color secondaryHeaderColor = __m['secondaryHeaderColor'];
  final Color textSelectionColor = __m['textSelectionColor'];
  final Color cursorColor = __m['cursorColor'];
  final Color textSelectionHandleColor = __m['textSelectionHandleColor'];
  final Color backgroundColor = __m['backgroundColor'];
  final Color dialogBackgroundColor = __m['dialogBackgroundColor'];
  final Color indicatorColor = __m['indicatorColor'];
  final Color hintColor = __m['hintColor'];
  final Color errorColor = __m['errorColor'];
  final Color toggleableActiveColor = __m['toggleableActiveColor'];
  final TextTheme textTheme = __m['textTheme'];
  final TextTheme primaryTextTheme = __m['primaryTextTheme'];
  final TextTheme accentTextTheme = __m['accentTextTheme'];
  final InputDecorationTheme inputDecorationTheme = __m['inputDecorationTheme'];
  final IconThemeData iconTheme = __m['iconTheme'];
  final IconThemeData primaryIconTheme = __m['primaryIconTheme'];
  final IconThemeData accentIconTheme = __m['accentIconTheme'];
  final SliderThemeData sliderTheme = __m['sliderTheme'];
  final TabBarTheme tabBarTheme = __m['tabBarTheme'];
  final TooltipThemeData tooltipTheme = __m['tooltipTheme'];
  final CardTheme cardTheme = __m['cardTheme'];
  final ChipThemeData chipTheme = __m['chipTheme'];
  final TargetPlatform platform = __m['platform'];
  final MaterialTapTargetSize materialTapTargetSize = __m['materialTapTargetSize'];
  final bool applyElevationOverlayColor = __m['applyElevationOverlayColor'];
  final PageTransitionsTheme pageTransitionsTheme = __m['pageTransitionsTheme'];
  final AppBarTheme appBarTheme = __m['appBarTheme'];
  final ScrollbarThemeData scrollbarTheme = __m['scrollbarTheme'];
  final BottomAppBarTheme bottomAppBarTheme = __m['bottomAppBarTheme'];
  final ColorScheme colorScheme = __m['colorScheme'];
  final DialogTheme dialogTheme = __m['dialogTheme'];
  final FloatingActionButtonThemeData floatingActionButtonTheme = __m['floatingActionButtonTheme'];
  final NavigationRailThemeData navigationRailTheme = __m['navigationRailTheme'];
  final Typography typography = __m['typography'];
  final NoDefaultCupertinoThemeData cupertinoOverrideTheme = __m['cupertinoOverrideTheme'];
  final SnackBarThemeData snackBarTheme = __m['snackBarTheme'];
  final BottomSheetThemeData bottomSheetTheme = __m['bottomSheetTheme'];
  final PopupMenuThemeData popupMenuTheme = __m['popupMenuTheme'];
  final MaterialBannerThemeData bannerTheme = __m['bannerTheme'];
  final DividerThemeData dividerTheme = __m['dividerTheme'];
  final ButtonBarThemeData buttonBarTheme = __m['buttonBarTheme'];
  final BottomNavigationBarThemeData bottomNavigationBarTheme = __m['bottomNavigationBarTheme'];
  final TimePickerThemeData timePickerTheme = __m['timePickerTheme'];
  final TextButtonThemeData textButtonTheme = __m['textButtonTheme'];
  final ElevatedButtonThemeData elevatedButtonTheme = __m['elevatedButtonTheme'];
  final OutlinedButtonThemeData outlinedButtonTheme = __m['outlinedButtonTheme'];
  final TextSelectionThemeData textSelectionTheme = __m['textSelectionTheme'];
  final DataTableThemeData dataTableTheme = __m['dataTableTheme'];
  final CheckboxThemeData checkboxTheme = __m['checkboxTheme'];
  final RadioThemeData radioTheme = __m['radioTheme'];
  final SwitchThemeData switchTheme = __m['switchTheme'];
  final ProgressIndicatorThemeData progressIndicatorTheme = __m['progressIndicatorTheme'];
  final bool fixTextFieldOutlineLabel = __m['fixTextFieldOutlineLabel'];
  final bool useTextSelectionTheme = __m['useTextSelectionTheme'];
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

ThemeData _ufromThemeData(Map<String, dynamic> __m) {
  final ColorScheme colorScheme = __m['colorScheme'];
  final TextTheme? textTheme = __m['textTheme'];
  return ThemeData.from(
    colorScheme: colorScheme,
    textTheme: textTheme,
  );
}

ThemeData _ulightThemeData(Map<String, dynamic> __m) {
  return ThemeData.light(
  );
}

ThemeData _udarkThemeData(Map<String, dynamic> __m) {
  return ThemeData.dark(
  );
}

ThemeData _ufallbackThemeData(Map<String, dynamic> __m) {
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
  return ScrollBehavior(
  );
}

RouteInformation _uRouteInformation(Map<String, dynamic> __m) {
  final String? location = __m['location'];
  final Object? state = __m['state'];
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
  final String _stackTrace = __m['_stackTrace'];
  return _StringStackTrace(
    _stackTrace,
  );
}

MaterialApp _uMaterialApp(Map<String, dynamic> __m) {
  final Key? key = __m['key'];
  final GlobalKey<NavigatorState>? navigatorKey = __m['navigatorKey'];
  final GlobalKey<ScaffoldMessengerState>? scaffoldMessengerKey = __m['scaffoldMessengerKey'];
  final Widget? home = __m['home'];
  final Map<String, func<BuildContext, Widget>>? routes = __m['routes'];
  final String? initialRoute = __m['initialRoute'];
  final func<RouteSettings, Route<dynamic>>? onGenerateRoute = __m['onGenerateRoute'];
  final func<String, List<Route<dynamic>>>? onGenerateInitialRoutes = __m['onGenerateInitialRoutes'];
  final func<RouteSettings, Route<dynamic>>? onUnknownRoute = __m['onUnknownRoute'];
  final List<NavigatorObserver>? navigatorObservers = __m['navigatorObservers'];
  final func<BuildContext, Widget, Widget>? builder = __m['builder'];
  final String? title = __m['title'];
  final func<BuildContext, String>? onGenerateTitle = __m['onGenerateTitle'];
  final Color? color = __m['color'];
  final ThemeData? theme = __m['theme'];
  final ThemeData? darkTheme = __m['darkTheme'];
  final ThemeData? highContrastTheme = __m['highContrastTheme'];
  final ThemeData? highContrastDarkTheme = __m['highContrastDarkTheme'];
  final ThemeMode? themeMode = __m['themeMode'];
  final Locale? locale = __m['locale'];
  final Iterable<LocalizationsDelegate<dynamic>>? localizationsDelegates = __m['localizationsDelegates'];
  final func<List<Locale>, Iterable<Locale>, Locale>? localeListResolutionCallback = __m['localeListResolutionCallback'];
  final func<Locale, Iterable<Locale>, Locale>? localeResolutionCallback = __m['localeResolutionCallback'];
  final Iterable<Locale>? supportedLocales = __m['supportedLocales'];
  final bool? debugShowMaterialGrid = __m['debugShowMaterialGrid'];
  final bool? showPerformanceOverlay = __m['showPerformanceOverlay'];
  final bool? checkerboardRasterCacheImages = __m['checkerboardRasterCacheImages'];
  final bool? checkerboardOffscreenLayers = __m['checkerboardOffscreenLayers'];
  final bool? showSemanticsDebugger = __m['showSemanticsDebugger'];
  final bool? debugShowCheckedModeBanner = __m['debugShowCheckedModeBanner'];
  final Map<ShortcutActivator, Intent>? shortcuts = __m['shortcuts'];
  final Map<Type, Action<Intent>>? actions = __m['actions'];
  final String? restorationScopeId = __m['restorationScopeId'];
  final ScrollBehavior? scrollBehavior = __m['scrollBehavior'];
  final bool? useInheritedMediaQuery = __m['useInheritedMediaQuery'];
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

MaterialApp _urouterMaterialApp(Map<String, dynamic> __m) {
  final Key? key = __m['key'];
  final GlobalKey<ScaffoldMessengerState>? scaffoldMessengerKey = __m['scaffoldMessengerKey'];
  final RouteInformationProvider? routeInformationProvider = __m['routeInformationProvider'];
  final RouteInformationParser<Object> routeInformationParser = __m['routeInformationParser'];
  final RouterDelegate<Object> routerDelegate = __m['routerDelegate'];
  final BackButtonDispatcher? backButtonDispatcher = __m['backButtonDispatcher'];
  final func<BuildContext, Widget, Widget>? builder = __m['builder'];
  final String? title = __m['title'];
  final func<BuildContext, String>? onGenerateTitle = __m['onGenerateTitle'];
  final Color? color = __m['color'];
  final ThemeData? theme = __m['theme'];
  final ThemeData? darkTheme = __m['darkTheme'];
  final ThemeData? highContrastTheme = __m['highContrastTheme'];
  final ThemeData? highContrastDarkTheme = __m['highContrastDarkTheme'];
  final ThemeMode? themeMode = __m['themeMode'];
  final Locale? locale = __m['locale'];
  final Iterable<LocalizationsDelegate<dynamic>>? localizationsDelegates = __m['localizationsDelegates'];
  final func<List<Locale>, Iterable<Locale>, Locale>? localeListResolutionCallback = __m['localeListResolutionCallback'];
  final func<Locale, Iterable<Locale>, Locale>? localeResolutionCallback = __m['localeResolutionCallback'];
  final Iterable<Locale>? supportedLocales = __m['supportedLocales'];
  final bool? debugShowMaterialGrid = __m['debugShowMaterialGrid'];
  final bool? showPerformanceOverlay = __m['showPerformanceOverlay'];
  final bool? checkerboardRasterCacheImages = __m['checkerboardRasterCacheImages'];
  final bool? checkerboardOffscreenLayers = __m['checkerboardOffscreenLayers'];
  final bool? showSemanticsDebugger = __m['showSemanticsDebugger'];
  final bool? debugShowCheckedModeBanner = __m['debugShowCheckedModeBanner'];
  final Map<ShortcutActivator, Intent>? shortcuts = __m['shortcuts'];
  final Map<Type, Action<Intent>>? actions = __m['actions'];
  final String? restorationScopeId = __m['restorationScopeId'];
  final ScrollBehavior? scrollBehavior = __m['scrollBehavior'];
  final bool? useInheritedMediaQuery = __m['useInheritedMediaQuery'];
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
  final int usbHidUsage = __m['usbHidUsage'];
  return PhysicalKeyboardKey(
    usbHidUsage,
  );
}

LogicalKeyboardKey _uLogicalKeyboardKey(Map<String, dynamic> __m) {
  final int keyId = __m['keyId'];
  return LogicalKeyboardKey(
    keyId,
  );
}

FocusNode _uFocusNode(Map<String, dynamic> __m) {
  final String? debugLabel = __m['debugLabel'];
  final func<FocusNode, RawKeyEvent, KeyEventResult>? onKey = __m['onKey'];
  final func<FocusNode, KeyEvent, KeyEventResult>? onKeyEvent = __m['onKeyEvent'];
  final bool? skipTraversal = __m['skipTraversal'];
  final bool? canRequestFocus = __m['canRequestFocus'];
  final bool? descendantsAreFocusable = __m['descendantsAreFocusable'];
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
  final Key? key = __m['key'];
  final func<void> onPressed = __m['onPressed'];
  final func<void>? onLongPress = __m['onLongPress'];
  final ButtonStyle? style = __m['style'];
  final FocusNode? focusNode = __m['focusNode'];
  final bool? autofocus = __m['autofocus'];
  final Clip? clipBehavior = __m['clipBehavior'];
  final Widget child = __m['child'];
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

ElevatedButton _uiconElevatedButton(Map<String, dynamic> __m) {
  final Key? key = __m['key'];
  final func<void> onPressed = __m['onPressed'];
  final func<void>? onLongPress = __m['onLongPress'];
  final ButtonStyle? style = __m['style'];
  final FocusNode? focusNode = __m['focusNode'];
  final bool? autofocus = __m['autofocus'];
  final Clip? clipBehavior = __m['clipBehavior'];
  final Widget icon = __m['icon'];
  final Widget label = __m['label'];
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
  'Color.fromARGB': _ufromARGBColor,
  'Color.fromRGBO': _ufromRGBOColor,
  'VisualDensity.': _uVisualDensity,
  'ColorSwatch.': _uColorSwatch,
  'MaterialColor.': _uMaterialColor,
  'ColorScheme.': _uColorScheme,
  'ColorScheme.light': _ulightColorScheme,
  'ColorScheme.dark': _udarkColorScheme,
  'ColorScheme.highContrastLight': _uhighContrastLightColorScheme,
  'ColorScheme.highContrastDark': _uhighContrastDarkColorScheme,
  'ColorScheme.fromSwatch': _ufromSwatchColorScheme,
  'ButtonThemeData.': _uButtonThemeData,
  'Locale.': _uLocale,
  'Locale.fromSubtags': _ufromSubtagsLocale,
  'Paint.': _uPaint,
  'Offset.': _uOffset,
  'Offset.fromDirection': _ufromDirectionOffset,
  'Shadow.': _uShadow,
  'FontFeature.': _uFontFeature,
  'FontFeature.enable': _uenableFontFeature,
  'FontFeature.disable': _udisableFontFeature,
  'FontFeature.alternative': _ualternativeFontFeature,
  'FontFeature.alternativeFractions': _ualternativeFractionsFontFeature,
  'FontFeature.contextualAlternates': _ucontextualAlternatesFontFeature,
  'FontFeature.caseSensitiveForms': _ucaseSensitiveFormsFontFeature,
  'FontFeature.characterVariant': _ucharacterVariantFontFeature,
  'FontFeature.denominator': _udenominatorFontFeature,
  'FontFeature.fractions': _ufractionsFontFeature,
  'FontFeature.historicalForms': _uhistoricalFormsFontFeature,
  'FontFeature.historicalLigatures': _uhistoricalLigaturesFontFeature,
  'FontFeature.liningFigures': _uliningFiguresFontFeature,
  'FontFeature.localeAware': _ulocaleAwareFontFeature,
  'FontFeature.notationalForms': _unotationalFormsFontFeature,
  'FontFeature.numerators': _unumeratorsFontFeature,
  'FontFeature.oldstyleFigures': _uoldstyleFiguresFontFeature,
  'FontFeature.ordinalForms': _uordinalFormsFontFeature,
  'FontFeature.proportionalFigures': _uproportionalFiguresFontFeature,
  'FontFeature.randomize': _urandomizeFontFeature,
  'FontFeature.stylisticAlternates': _ustylisticAlternatesFontFeature,
  'FontFeature.scientificInferiors': _uscientificInferiorsFontFeature,
  'FontFeature.stylisticSet': _ustylisticSetFontFeature,
  'FontFeature.subscripts': _usubscriptsFontFeature,
  'FontFeature.superscripts': _usuperscriptsFontFeature,
  'FontFeature.swash': _uswashFontFeature,
  'FontFeature.tabularFigures': _utabularFiguresFontFeature,
  'FontFeature.slashedZero': _uslashedZeroFontFeature,
  'TextDecoration.combine': _ucombineTextDecoration,
  'TextStyle.': _uTextStyle,
  'Size.': _uSize,
  'Size.copy': _ucopySize,
  'Size.square': _usquareSize,
  'Size.fromWidth': _ufromWidthSize,
  'Size.fromHeight': _ufromHeightSize,
  'Size.fromRadius': _ufromRadiusSize,
  'BoxConstraints.': _uBoxConstraints,
  'BoxConstraints.tight': _utightBoxConstraints,
  'BoxConstraints.tightFor': _utightForBoxConstraints,
  'BoxConstraints.tightForFinite': _utightForFiniteBoxConstraints,
  'BoxConstraints.loose': _ulooseBoxConstraints,
  'BoxConstraints.expand': _uexpandBoxConstraints,
  'Radius.circular': _ucircularRadius,
  'Radius.elliptical': _uellipticalRadius,
  'BorderRadius.all': _uallBorderRadius,
  'BorderRadius.circular': _ucircularBorderRadius,
  'BorderRadius.vertical': _uverticalBorderRadius,
  'BorderRadius.horizontal': _uhorizontalBorderRadius,
  'BorderRadius.only': _uonlyBorderRadius,
  'ToggleButtonsThemeData.': _uToggleButtonsThemeData,
  'TextTheme.': _uTextTheme,
  'BorderSide.': _uBorderSide,
  'InputDecorationTheme.': _uInputDecorationTheme,
  'IconThemeData.': _uIconThemeData,
  'IconThemeData.fallback': _ufallbackIconThemeData,
  'RangeValues.': _uRangeValues,
  'SliderThemeData.': _uSliderThemeData,
  'SliderThemeData.fromPrimaryColors': _ufromPrimaryColorsSliderThemeData,
  'TabBarTheme.': _uTabBarTheme,
  'Duration.': _uDuration,
  'TooltipThemeData.': _uTooltipThemeData,
  'CardTheme.': _uCardTheme,
  'ChipThemeData.': _uChipThemeData,
  'ChipThemeData.fromDefaults': _ufromDefaultsChipThemeData,
  'PageTransitionsTheme.': _uPageTransitionsTheme,
  'SystemUiOverlayStyle.': _uSystemUiOverlayStyle,
  'AppBarTheme.': _uAppBarTheme,
  'ScrollbarThemeData.': _uScrollbarThemeData,
  'BottomAppBarTheme.': _uBottomAppBarTheme,
  'DialogTheme.': _uDialogTheme,
  'FloatingActionButtonThemeData.': _uFloatingActionButtonThemeData,
  'NavigationRailThemeData.': _uNavigationRailThemeData,
  'Typography.': _uTypography,
  'Typography.material2014': _umaterial2014Typography,
  'Typography.material2018': _umaterial2018Typography,
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
  'ThemeData.raw': _urawThemeData,
  'ThemeData.from': _ufromThemeData,
  'ThemeData.light': _ulightThemeData,
  'ThemeData.dark': _udarkThemeData,
  'ThemeData.fallback': _ufallbackThemeData,
  'DoNothingIntent.': _uDoNothingIntent,
  'ScrollBehavior.': _uScrollBehavior,
  'RouteInformation.': _uRouteInformation,
  '_CallbackHookProvider.': _u_CallbackHookProvider,
  '_StringStackTrace.': _u_StringStackTrace,
  'MaterialApp.': _uMaterialApp,
  'MaterialApp.router': _urouterMaterialApp,
  'PhysicalKeyboardKey.': _uPhysicalKeyboardKey,
  'LogicalKeyboardKey.': _uLogicalKeyboardKey,
  'FocusNode.': _uFocusNode,
  'ElevatedButton.': _uElevatedButton,
  'ElevatedButton.icon': _uiconElevatedButton,
};
