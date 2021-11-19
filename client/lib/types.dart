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
  final name = __m['name'];
  final arguments = __m['arguments'];
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
  final key = __m['key'];
  final pages = __m['pages'];
  final onPopPage = __m['onPopPage'];
  final initialRoute = __m['initialRoute'];
  final onGenerateInitialRoutes = __m['onGenerateInitialRoutes'];
  final onGenerateRoute = __m['onGenerateRoute'];
  final onUnknownRoute = __m['onUnknownRoute'];
  final transitionDelegate = __m['transitionDelegate'];
  final reportsRouteUpdateToEngine = __m['reportsRouteUpdateToEngine'];
  final observers = __m['observers'];
  final restorationScopeId = __m['restorationScopeId'];
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
  final key = __m['key'];
  final child = __m['child'];
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
  final key = __m['key'];
  final value = __m['value'];
  return MapEntry(
    key,
    value,
  );
}

Color _uColor(Map<String, dynamic> __m) {
  final value = __m['value'];
  return Color(
    value,
  );
}

Color _ufromARGBColor(Map<String, dynamic> __m) {
  final a = __m['a'];
  final r = __m['r'];
  final g = __m['g'];
  final b = __m['b'];
  return Color.fromARGB(
    a,
    r,
    g,
    b,
  );
}

Color _ufromRGBOColor(Map<String, dynamic> __m) {
  final r = __m['r'];
  final g = __m['g'];
  final b = __m['b'];
  final opacity = __m['opacity'];
  return Color.fromRGBO(
    r,
    g,
    b,
    opacity,
  );
}

Brightness _uBrightness(String v) {
  switch(v) {
    case 'dark':
      return Brightness.dark;
    case 'light':
      return Brightness.light;
  }
  throw 'illegal enum value $v';
}

VisualDensity _uVisualDensity(Map<String, dynamic> __m) {
  final horizontal = __m['horizontal'];
  final vertical = __m['vertical'];
  return VisualDensity(
    horizontal: horizontal,
    vertical: vertical,
  );
}

ColorSwatch _uColorSwatch(Map<String, dynamic> __m) {
  final primary = __m['primary'];
  final _swatch = __m['_swatch'];
  return ColorSwatch(
    primary,
    _swatch,
  );
}

MaterialColor _uMaterialColor(Map<String, dynamic> __m) {
  final primary = __m['primary'];
  final swatch = __m['swatch'];
  return MaterialColor(
    primary,
    swatch,
  );
}

ButtonTextTheme _uButtonTextTheme(String v) {
  switch(v) {
    case 'normal':
      return ButtonTextTheme.normal;
    case 'accent':
      return ButtonTextTheme.accent;
    case 'primary':
      return ButtonTextTheme.primary;
  }
  throw 'illegal enum value $v';
}

ButtonBarLayoutBehavior _uButtonBarLayoutBehavior(String v) {
  switch(v) {
    case 'constrained':
      return ButtonBarLayoutBehavior.constrained;
    case 'padded':
      return ButtonBarLayoutBehavior.padded;
  }
  throw 'illegal enum value $v';
}

ColorScheme _uColorScheme(Map<String, dynamic> __m) {
  final primary = __m['primary'];
  final primaryVariant = __m['primaryVariant'];
  final secondary = __m['secondary'];
  final secondaryVariant = __m['secondaryVariant'];
  final surface = __m['surface'];
  final background = __m['background'];
  final error = __m['error'];
  final onPrimary = __m['onPrimary'];
  final onSecondary = __m['onSecondary'];
  final onSurface = __m['onSurface'];
  final onBackground = __m['onBackground'];
  final onError = __m['onError'];
  final brightness = __m['brightness'];
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
  final primary = __m['primary'];
  final primaryVariant = __m['primaryVariant'];
  final secondary = __m['secondary'];
  final secondaryVariant = __m['secondaryVariant'];
  final surface = __m['surface'];
  final background = __m['background'];
  final error = __m['error'];
  final onPrimary = __m['onPrimary'];
  final onSecondary = __m['onSecondary'];
  final onSurface = __m['onSurface'];
  final onBackground = __m['onBackground'];
  final onError = __m['onError'];
  final brightness = __m['brightness'];
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
  final primary = __m['primary'];
  final primaryVariant = __m['primaryVariant'];
  final secondary = __m['secondary'];
  final secondaryVariant = __m['secondaryVariant'];
  final surface = __m['surface'];
  final background = __m['background'];
  final error = __m['error'];
  final onPrimary = __m['onPrimary'];
  final onSecondary = __m['onSecondary'];
  final onSurface = __m['onSurface'];
  final onBackground = __m['onBackground'];
  final onError = __m['onError'];
  final brightness = __m['brightness'];
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
  final primary = __m['primary'];
  final primaryVariant = __m['primaryVariant'];
  final secondary = __m['secondary'];
  final secondaryVariant = __m['secondaryVariant'];
  final surface = __m['surface'];
  final background = __m['background'];
  final error = __m['error'];
  final onPrimary = __m['onPrimary'];
  final onSecondary = __m['onSecondary'];
  final onSurface = __m['onSurface'];
  final onBackground = __m['onBackground'];
  final onError = __m['onError'];
  final brightness = __m['brightness'];
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
  final primary = __m['primary'];
  final primaryVariant = __m['primaryVariant'];
  final secondary = __m['secondary'];
  final secondaryVariant = __m['secondaryVariant'];
  final surface = __m['surface'];
  final background = __m['background'];
  final error = __m['error'];
  final onPrimary = __m['onPrimary'];
  final onSecondary = __m['onSecondary'];
  final onSurface = __m['onSurface'];
  final onBackground = __m['onBackground'];
  final onError = __m['onError'];
  final brightness = __m['brightness'];
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
  final primarySwatch = __m['primarySwatch'];
  final primaryColorDark = __m['primaryColorDark'];
  final accentColor = __m['accentColor'];
  final cardColor = __m['cardColor'];
  final backgroundColor = __m['backgroundColor'];
  final errorColor = __m['errorColor'];
  final brightness = __m['brightness'];
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

MaterialTapTargetSize _uMaterialTapTargetSize(String v) {
  switch(v) {
    case 'padded':
      return MaterialTapTargetSize.padded;
    case 'shrinkWrap':
      return MaterialTapTargetSize.shrinkWrap;
  }
  throw 'illegal enum value $v';
}

ButtonThemeData _uButtonThemeData(Map<String, dynamic> __m) {
  final textTheme = __m['textTheme'];
  final minWidth = __m['minWidth'];
  final height = __m['height'];
  final padding = __m['padding'];
  final shape = __m['shape'];
  final layoutBehavior = __m['layoutBehavior'];
  final alignedDropdown = __m['alignedDropdown'];
  final buttonColor = __m['buttonColor'];
  final disabledColor = __m['disabledColor'];
  final focusColor = __m['focusColor'];
  final hoverColor = __m['hoverColor'];
  final highlightColor = __m['highlightColor'];
  final splashColor = __m['splashColor'];
  final colorScheme = __m['colorScheme'];
  final materialTapTargetSize = __m['materialTapTargetSize'];
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

FontWeight _uFontWeight(Map<String, dynamic> __m) {
  return FontWeight(
  );
}

FontStyle _uFontStyle(String v) {
  switch(v) {
    case 'normal':
      return FontStyle.normal;
    case 'italic':
      return FontStyle.italic;
  }
  throw 'illegal enum value $v';
}

TextBaseline _uTextBaseline(String v) {
  switch(v) {
    case 'alphabetic':
      return TextBaseline.alphabetic;
    case 'ideographic':
      return TextBaseline.ideographic;
  }
  throw 'illegal enum value $v';
}

TextLeadingDistribution _uTextLeadingDistribution(String v) {
  switch(v) {
    case 'proportional':
      return TextLeadingDistribution.proportional;
    case 'even':
      return TextLeadingDistribution.even;
  }
  throw 'illegal enum value $v';
}

Locale _uLocale(Map<String, dynamic> __m) {
  final _languageCode = __m['_languageCode'];
  final _countryCode = __m['_countryCode'];
  return Locale(
    _languageCode,
    _countryCode,
  );
}

Locale _ufromSubtagsLocale(Map<String, dynamic> __m) {
  final languageCode = __m['languageCode'];
  final scriptCode = __m['scriptCode'];
  final countryCode = __m['countryCode'];
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
  final dx = __m['dx'];
  final dy = __m['dy'];
  return Offset(
    dx,
    dy,
  );
}

Offset _ufromDirectionOffset(Map<String, dynamic> __m) {
  final direction = __m['direction'];
  final distance = __m['distance'];
  return Offset.fromDirection(
    direction,
    distance,
  );
}

Shadow _uShadow(Map<String, dynamic> __m) {
  final color = __m['color'];
  final offset = __m['offset'];
  final blurRadius = __m['blurRadius'];
  return Shadow(
    color: color,
    offset: offset,
    blurRadius: blurRadius,
  );
}

FontFeature _uFontFeature(Map<String, dynamic> __m) {
  final feature = __m['feature'];
  final value = __m['value'];
  return FontFeature(
    feature,
    value,
  );
}

FontFeature _uenableFontFeature(Map<String, dynamic> __m) {
  final feature = __m['feature'];
  return FontFeature.enable(
    feature,
  );
}

FontFeature _udisableFontFeature(Map<String, dynamic> __m) {
  final feature = __m['feature'];
  return FontFeature.disable(
    feature,
  );
}

FontFeature _ualternativeFontFeature(Map<String, dynamic> __m) {
  final value = __m['value'];
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
  final value = __m['value'];
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
  final enable = __m['enable'];
  return FontFeature.localeAware(
    enable: enable,
  );
}

FontFeature _unotationalFormsFontFeature(Map<String, dynamic> __m) {
  final value = __m['value'];
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
  final value = __m['value'];
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
  final value = __m['value'];
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

TextDecoration _uTextDecoration(Map<String, dynamic> __m) {
  return TextDecoration(
  );
}

TextDecoration _ucombineTextDecoration(Map<String, dynamic> __m) {
  final decorations = __m['decorations'];
  return TextDecoration.combine(
    decorations,
  );
}

TextDecorationStyle _uTextDecorationStyle(String v) {
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
  throw 'illegal enum value $v';
}

TextOverflow _uTextOverflow(String v) {
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
  throw 'illegal enum value $v';
}

TextStyle _uTextStyle(Map<String, dynamic> __m) {
  final inherit = __m['inherit'];
  final color = __m['color'];
  final backgroundColor = __m['backgroundColor'];
  final fontSize = __m['fontSize'];
  final fontWeight = __m['fontWeight'];
  final fontStyle = __m['fontStyle'];
  final letterSpacing = __m['letterSpacing'];
  final wordSpacing = __m['wordSpacing'];
  final textBaseline = __m['textBaseline'];
  final height = __m['height'];
  final leadingDistribution = __m['leadingDistribution'];
  final locale = __m['locale'];
  final foreground = __m['foreground'];
  final background = __m['background'];
  final shadows = __m['shadows'];
  final fontFeatures = __m['fontFeatures'];
  final decoration = __m['decoration'];
  final decorationColor = __m['decorationColor'];
  final decorationStyle = __m['decorationStyle'];
  final decorationThickness = __m['decorationThickness'];
  final debugLabel = __m['debugLabel'];
  final fontFamily = __m['fontFamily'];
  final fontFamilyFallback = __m['fontFamilyFallback'];
  final package = __m['package'];
  final overflow = __m['overflow'];
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
  final width = __m['width'];
  final height = __m['height'];
  return Size(
    width,
    height,
  );
}

Size _ucopySize(Map<String, dynamic> __m) {
  final source = __m['source'];
  return Size.copy(
    source,
  );
}

Size _usquareSize(Map<String, dynamic> __m) {
  final dimension = __m['dimension'];
  return Size.square(
    dimension,
  );
}

Size _ufromWidthSize(Map<String, dynamic> __m) {
  final width = __m['width'];
  return Size.fromWidth(
    width,
  );
}

Size _ufromHeightSize(Map<String, dynamic> __m) {
  final height = __m['height'];
  return Size.fromHeight(
    height,
  );
}

Size _ufromRadiusSize(Map<String, dynamic> __m) {
  final radius = __m['radius'];
  return Size.fromRadius(
    radius,
  );
}

BoxConstraints _uBoxConstraints(Map<String, dynamic> __m) {
  final minWidth = __m['minWidth'];
  final maxWidth = __m['maxWidth'];
  final minHeight = __m['minHeight'];
  final maxHeight = __m['maxHeight'];
  return BoxConstraints(
    minWidth: minWidth,
    maxWidth: maxWidth,
    minHeight: minHeight,
    maxHeight: maxHeight,
  );
}

BoxConstraints _utightBoxConstraints(Map<String, dynamic> __m) {
  final size = __m['size'];
  return BoxConstraints.tight(
    size,
  );
}

BoxConstraints _utightForBoxConstraints(Map<String, dynamic> __m) {
  final width = __m['width'];
  final height = __m['height'];
  return BoxConstraints.tightFor(
    width: width,
    height: height,
  );
}

BoxConstraints _utightForFiniteBoxConstraints(Map<String, dynamic> __m) {
  final width = __m['width'];
  final height = __m['height'];
  return BoxConstraints.tightForFinite(
    width: width,
    height: height,
  );
}

BoxConstraints _ulooseBoxConstraints(Map<String, dynamic> __m) {
  final size = __m['size'];
  return BoxConstraints.loose(
    size,
  );
}

BoxConstraints _uexpandBoxConstraints(Map<String, dynamic> __m) {
  final width = __m['width'];
  final height = __m['height'];
  return BoxConstraints.expand(
    width: width,
    height: height,
  );
}

Radius _uRadius(Map<String, dynamic> __m) {
  return Radius(
  );
}

Radius _ucircularRadius(Map<String, dynamic> __m) {
  final radius = __m['radius'];
  return Radius.circular(
    radius,
  );
}

Radius _uellipticalRadius(Map<String, dynamic> __m) {
  final x = __m['x'];
  final y = __m['y'];
  return Radius.elliptical(
    x,
    y,
  );
}

BorderRadius _uBorderRadius(Map<String, dynamic> __m) {
  return BorderRadius(
  );
}

BorderRadius _uallBorderRadius(Map<String, dynamic> __m) {
  final radius = __m['radius'];
  return BorderRadius.all(
    radius,
  );
}

BorderRadius _ucircularBorderRadius(Map<String, dynamic> __m) {
  final radius = __m['radius'];
  return BorderRadius.circular(
    radius,
  );
}

BorderRadius _uverticalBorderRadius(Map<String, dynamic> __m) {
  final top = __m['top'];
  final bottom = __m['bottom'];
  return BorderRadius.vertical(
    top: top,
    bottom: bottom,
  );
}

BorderRadius _uhorizontalBorderRadius(Map<String, dynamic> __m) {
  final left = __m['left'];
  final right = __m['right'];
  return BorderRadius.horizontal(
    left: left,
    right: right,
  );
}

BorderRadius _uonlyBorderRadius(Map<String, dynamic> __m) {
  final topLeft = __m['topLeft'];
  final topRight = __m['topRight'];
  final bottomLeft = __m['bottomLeft'];
  final bottomRight = __m['bottomRight'];
  return BorderRadius.only(
    topLeft: topLeft,
    topRight: topRight,
    bottomLeft: bottomLeft,
    bottomRight: bottomRight,
  );
}

ToggleButtonsThemeData _uToggleButtonsThemeData(Map<String, dynamic> __m) {
  final textStyle = __m['textStyle'];
  final constraints = __m['constraints'];
  final color = __m['color'];
  final selectedColor = __m['selectedColor'];
  final disabledColor = __m['disabledColor'];
  final fillColor = __m['fillColor'];
  final focusColor = __m['focusColor'];
  final highlightColor = __m['highlightColor'];
  final hoverColor = __m['hoverColor'];
  final splashColor = __m['splashColor'];
  final borderColor = __m['borderColor'];
  final selectedBorderColor = __m['selectedBorderColor'];
  final disabledBorderColor = __m['disabledBorderColor'];
  final borderRadius = __m['borderRadius'];
  final borderWidth = __m['borderWidth'];
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
  final headline1 = __m['headline1'];
  final headline2 = __m['headline2'];
  final headline3 = __m['headline3'];
  final headline4 = __m['headline4'];
  final headline5 = __m['headline5'];
  final headline6 = __m['headline6'];
  final subtitle1 = __m['subtitle1'];
  final subtitle2 = __m['subtitle2'];
  final bodyText1 = __m['bodyText1'];
  final bodyText2 = __m['bodyText2'];
  final caption = __m['caption'];
  final button = __m['button'];
  final overline = __m['overline'];
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

FloatingLabelBehavior _uFloatingLabelBehavior(String v) {
  switch(v) {
    case 'never':
      return FloatingLabelBehavior.never;
    case 'auto':
      return FloatingLabelBehavior.auto;
    case 'always':
      return FloatingLabelBehavior.always;
  }
  throw 'illegal enum value $v';
}

BorderStyle _uBorderStyle(String v) {
  switch(v) {
    case 'none':
      return BorderStyle.none;
    case 'solid':
      return BorderStyle.solid;
  }
  throw 'illegal enum value $v';
}

BorderSide _uBorderSide(Map<String, dynamic> __m) {
  final color = __m['color'];
  final width = __m['width'];
  final style = __m['style'];
  return BorderSide(
    color: color,
    width: width,
    style: style,
  );
}

InputDecorationTheme _uInputDecorationTheme(Map<String, dynamic> __m) {
  final labelStyle = __m['labelStyle'];
  final floatingLabelStyle = __m['floatingLabelStyle'];
  final helperStyle = __m['helperStyle'];
  final helperMaxLines = __m['helperMaxLines'];
  final hintStyle = __m['hintStyle'];
  final errorStyle = __m['errorStyle'];
  final errorMaxLines = __m['errorMaxLines'];
  final floatingLabelBehavior = __m['floatingLabelBehavior'];
  final isDense = __m['isDense'];
  final contentPadding = __m['contentPadding'];
  final isCollapsed = __m['isCollapsed'];
  final prefixStyle = __m['prefixStyle'];
  final suffixStyle = __m['suffixStyle'];
  final counterStyle = __m['counterStyle'];
  final filled = __m['filled'];
  final fillColor = __m['fillColor'];
  final focusColor = __m['focusColor'];
  final hoverColor = __m['hoverColor'];
  final errorBorder = __m['errorBorder'];
  final focusedBorder = __m['focusedBorder'];
  final focusedErrorBorder = __m['focusedErrorBorder'];
  final disabledBorder = __m['disabledBorder'];
  final enabledBorder = __m['enabledBorder'];
  final border = __m['border'];
  final alignLabelWithHint = __m['alignLabelWithHint'];
  final constraints = __m['constraints'];
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
  final color = __m['color'];
  final opacity = __m['opacity'];
  final size = __m['size'];
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

ShowValueIndicator _uShowValueIndicator(String v) {
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
  throw 'illegal enum value $v';
}

TextDirection _uTextDirection(String v) {
  switch(v) {
    case 'rtl':
      return TextDirection.rtl;
    case 'ltr':
      return TextDirection.ltr;
  }
  throw 'illegal enum value $v';
}

RangeValues _uRangeValues(Map<String, dynamic> __m) {
  final start = __m['start'];
  final end = __m['end'];
  return RangeValues(
    start,
    end,
  );
}

Thumb _uThumb(String v) {
  switch(v) {
    case 'start':
      return Thumb.start;
    case 'end':
      return Thumb.end;
  }
  throw 'illegal enum value $v';
}

SliderThemeData _uSliderThemeData(Map<String, dynamic> __m) {
  final trackHeight = __m['trackHeight'];
  final activeTrackColor = __m['activeTrackColor'];
  final inactiveTrackColor = __m['inactiveTrackColor'];
  final disabledActiveTrackColor = __m['disabledActiveTrackColor'];
  final disabledInactiveTrackColor = __m['disabledInactiveTrackColor'];
  final activeTickMarkColor = __m['activeTickMarkColor'];
  final inactiveTickMarkColor = __m['inactiveTickMarkColor'];
  final disabledActiveTickMarkColor = __m['disabledActiveTickMarkColor'];
  final disabledInactiveTickMarkColor = __m['disabledInactiveTickMarkColor'];
  final thumbColor = __m['thumbColor'];
  final overlappingShapeStrokeColor = __m['overlappingShapeStrokeColor'];
  final disabledThumbColor = __m['disabledThumbColor'];
  final overlayColor = __m['overlayColor'];
  final valueIndicatorColor = __m['valueIndicatorColor'];
  final overlayShape = __m['overlayShape'];
  final tickMarkShape = __m['tickMarkShape'];
  final thumbShape = __m['thumbShape'];
  final trackShape = __m['trackShape'];
  final valueIndicatorShape = __m['valueIndicatorShape'];
  final rangeTickMarkShape = __m['rangeTickMarkShape'];
  final rangeThumbShape = __m['rangeThumbShape'];
  final rangeTrackShape = __m['rangeTrackShape'];
  final rangeValueIndicatorShape = __m['rangeValueIndicatorShape'];
  final showValueIndicator = __m['showValueIndicator'];
  final valueIndicatorTextStyle = __m['valueIndicatorTextStyle'];
  final minThumbSeparation = __m['minThumbSeparation'];
  final thumbSelector = __m['thumbSelector'];
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
  final primaryColor = __m['primaryColor'];
  final primaryColorDark = __m['primaryColorDark'];
  final primaryColorLight = __m['primaryColorLight'];
  final valueIndicatorTextStyle = __m['valueIndicatorTextStyle'];
  return SliderThemeData.fromPrimaryColors(
    primaryColor: primaryColor,
    primaryColorDark: primaryColorDark,
    primaryColorLight: primaryColorLight,
    valueIndicatorTextStyle: valueIndicatorTextStyle,
  );
}

TabBarIndicatorSize _uTabBarIndicatorSize(String v) {
  switch(v) {
    case 'tab':
      return TabBarIndicatorSize.tab;
    case 'label':
      return TabBarIndicatorSize.label;
  }
  throw 'illegal enum value $v';
}

TabBarTheme _uTabBarTheme(Map<String, dynamic> __m) {
  final indicator = __m['indicator'];
  final indicatorSize = __m['indicatorSize'];
  final labelColor = __m['labelColor'];
  final labelPadding = __m['labelPadding'];
  final labelStyle = __m['labelStyle'];
  final unselectedLabelColor = __m['unselectedLabelColor'];
  final unselectedLabelStyle = __m['unselectedLabelStyle'];
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
  final days = __m['days'];
  final hours = __m['hours'];
  final minutes = __m['minutes'];
  final seconds = __m['seconds'];
  final milliseconds = __m['milliseconds'];
  final microseconds = __m['microseconds'];
  return Duration(
    days: days,
    hours: hours,
    minutes: minutes,
    seconds: seconds,
    milliseconds: milliseconds,
    microseconds: microseconds,
  );
}

TooltipTriggerMode _uTooltipTriggerMode(String v) {
  switch(v) {
    case 'manual':
      return TooltipTriggerMode.manual;
    case 'longPress':
      return TooltipTriggerMode.longPress;
    case 'tap':
      return TooltipTriggerMode.tap;
  }
  throw 'illegal enum value $v';
}

TooltipThemeData _uTooltipThemeData(Map<String, dynamic> __m) {
  final height = __m['height'];
  final padding = __m['padding'];
  final margin = __m['margin'];
  final verticalOffset = __m['verticalOffset'];
  final preferBelow = __m['preferBelow'];
  final excludeFromSemantics = __m['excludeFromSemantics'];
  final decoration = __m['decoration'];
  final textStyle = __m['textStyle'];
  final waitDuration = __m['waitDuration'];
  final showDuration = __m['showDuration'];
  final triggerMode = __m['triggerMode'];
  final enableFeedback = __m['enableFeedback'];
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

Clip _uClip(String v) {
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
  throw 'illegal enum value $v';
}

CardTheme _uCardTheme(Map<String, dynamic> __m) {
  final clipBehavior = __m['clipBehavior'];
  final color = __m['color'];
  final shadowColor = __m['shadowColor'];
  final elevation = __m['elevation'];
  final margin = __m['margin'];
  final shape = __m['shape'];
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
  final backgroundColor = __m['backgroundColor'];
  final deleteIconColor = __m['deleteIconColor'];
  final disabledColor = __m['disabledColor'];
  final selectedColor = __m['selectedColor'];
  final secondarySelectedColor = __m['secondarySelectedColor'];
  final shadowColor = __m['shadowColor'];
  final selectedShadowColor = __m['selectedShadowColor'];
  final showCheckmark = __m['showCheckmark'];
  final checkmarkColor = __m['checkmarkColor'];
  final labelPadding = __m['labelPadding'];
  final padding = __m['padding'];
  final side = __m['side'];
  final shape = __m['shape'];
  final labelStyle = __m['labelStyle'];
  final secondaryLabelStyle = __m['secondaryLabelStyle'];
  final brightness = __m['brightness'];
  final elevation = __m['elevation'];
  final pressElevation = __m['pressElevation'];
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
  final brightness = __m['brightness'];
  final primaryColor = __m['primaryColor'];
  final secondaryColor = __m['secondaryColor'];
  final labelStyle = __m['labelStyle'];
  return ChipThemeData.fromDefaults(
    brightness: brightness,
    primaryColor: primaryColor,
    secondaryColor: secondaryColor,
    labelStyle: labelStyle,
  );
}

TargetPlatform _uTargetPlatform(String v) {
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
  throw 'illegal enum value $v';
}

PageTransitionsTheme _uPageTransitionsTheme(Map<String, dynamic> __m) {
  final builders = __m['builders'];
  return PageTransitionsTheme(
    builders: builders,
  );
}

SystemUiOverlayStyle _uSystemUiOverlayStyle(Map<String, dynamic> __m) {
  final systemNavigationBarColor = __m['systemNavigationBarColor'];
  final systemNavigationBarDividerColor = __m['systemNavigationBarDividerColor'];
  final systemNavigationBarIconBrightness = __m['systemNavigationBarIconBrightness'];
  final systemNavigationBarContrastEnforced = __m['systemNavigationBarContrastEnforced'];
  final statusBarColor = __m['statusBarColor'];
  final statusBarBrightness = __m['statusBarBrightness'];
  final statusBarIconBrightness = __m['statusBarIconBrightness'];
  final systemStatusBarContrastEnforced = __m['systemStatusBarContrastEnforced'];
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
  final brightness = __m['brightness'];
  final color = __m['color'];
  final backgroundColor = __m['backgroundColor'];
  final foregroundColor = __m['foregroundColor'];
  final elevation = __m['elevation'];
  final shadowColor = __m['shadowColor'];
  final shape = __m['shape'];
  final iconTheme = __m['iconTheme'];
  final actionsIconTheme = __m['actionsIconTheme'];
  final textTheme = __m['textTheme'];
  final centerTitle = __m['centerTitle'];
  final titleSpacing = __m['titleSpacing'];
  final toolbarHeight = __m['toolbarHeight'];
  final toolbarTextStyle = __m['toolbarTextStyle'];
  final titleTextStyle = __m['titleTextStyle'];
  final systemOverlayStyle = __m['systemOverlayStyle'];
  final backwardsCompatibility = __m['backwardsCompatibility'];
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
  final thickness = __m['thickness'];
  final showTrackOnHover = __m['showTrackOnHover'];
  final isAlwaysShown = __m['isAlwaysShown'];
  final radius = __m['radius'];
  final thumbColor = __m['thumbColor'];
  final trackColor = __m['trackColor'];
  final trackBorderColor = __m['trackBorderColor'];
  final crossAxisMargin = __m['crossAxisMargin'];
  final mainAxisMargin = __m['mainAxisMargin'];
  final minThumbLength = __m['minThumbLength'];
  final interactive = __m['interactive'];
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
  final color = __m['color'];
  final elevation = __m['elevation'];
  final shape = __m['shape'];
  return BottomAppBarTheme(
    color: color,
    elevation: elevation,
    shape: shape,
  );
}

DialogTheme _uDialogTheme(Map<String, dynamic> __m) {
  final backgroundColor = __m['backgroundColor'];
  final elevation = __m['elevation'];
  final shape = __m['shape'];
  final titleTextStyle = __m['titleTextStyle'];
  final contentTextStyle = __m['contentTextStyle'];
  return DialogTheme(
    backgroundColor: backgroundColor,
    elevation: elevation,
    shape: shape,
    titleTextStyle: titleTextStyle,
    contentTextStyle: contentTextStyle,
  );
}

FloatingActionButtonThemeData _uFloatingActionButtonThemeData(Map<String, dynamic> __m) {
  final foregroundColor = __m['foregroundColor'];
  final backgroundColor = __m['backgroundColor'];
  final focusColor = __m['focusColor'];
  final hoverColor = __m['hoverColor'];
  final splashColor = __m['splashColor'];
  final elevation = __m['elevation'];
  final focusElevation = __m['focusElevation'];
  final hoverElevation = __m['hoverElevation'];
  final disabledElevation = __m['disabledElevation'];
  final highlightElevation = __m['highlightElevation'];
  final shape = __m['shape'];
  final enableFeedback = __m['enableFeedback'];
  final sizeConstraints = __m['sizeConstraints'];
  final smallSizeConstraints = __m['smallSizeConstraints'];
  final largeSizeConstraints = __m['largeSizeConstraints'];
  final extendedSizeConstraints = __m['extendedSizeConstraints'];
  final extendedIconLabelSpacing = __m['extendedIconLabelSpacing'];
  final extendedPadding = __m['extendedPadding'];
  final extendedTextStyle = __m['extendedTextStyle'];
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

NavigationRailLabelType _uNavigationRailLabelType(String v) {
  switch(v) {
    case 'none':
      return NavigationRailLabelType.none;
    case 'selected':
      return NavigationRailLabelType.selected;
    case 'all':
      return NavigationRailLabelType.all;
  }
  throw 'illegal enum value $v';
}

NavigationRailThemeData _uNavigationRailThemeData(Map<String, dynamic> __m) {
  final backgroundColor = __m['backgroundColor'];
  final elevation = __m['elevation'];
  final unselectedLabelTextStyle = __m['unselectedLabelTextStyle'];
  final selectedLabelTextStyle = __m['selectedLabelTextStyle'];
  final unselectedIconTheme = __m['unselectedIconTheme'];
  final selectedIconTheme = __m['selectedIconTheme'];
  final groupAlignment = __m['groupAlignment'];
  final labelType = __m['labelType'];
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
  final platform = __m['platform'];
  final black = __m['black'];
  final white = __m['white'];
  final englishLike = __m['englishLike'];
  final dense = __m['dense'];
  final tall = __m['tall'];
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
  final platform = __m['platform'];
  final black = __m['black'];
  final white = __m['white'];
  final englishLike = __m['englishLike'];
  final dense = __m['dense'];
  final tall = __m['tall'];
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
  final platform = __m['platform'];
  final black = __m['black'];
  final white = __m['white'];
  final englishLike = __m['englishLike'];
  final dense = __m['dense'];
  final tall = __m['tall'];
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
  final primaryColor = __m['primaryColor'];
  final textStyle = __m['textStyle'];
  final actionTextStyle = __m['actionTextStyle'];
  final tabLabelTextStyle = __m['tabLabelTextStyle'];
  final navTitleTextStyle = __m['navTitleTextStyle'];
  final navLargeTitleTextStyle = __m['navLargeTitleTextStyle'];
  final navActionTextStyle = __m['navActionTextStyle'];
  final pickerTextStyle = __m['pickerTextStyle'];
  final dateTimePickerTextStyle = __m['dateTimePickerTextStyle'];
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
  final brightness = __m['brightness'];
  final primaryColor = __m['primaryColor'];
  final primaryContrastingColor = __m['primaryContrastingColor'];
  final textTheme = __m['textTheme'];
  final barBackgroundColor = __m['barBackgroundColor'];
  final scaffoldBackgroundColor = __m['scaffoldBackgroundColor'];
  return NoDefaultCupertinoThemeData(
    brightness: brightness,
    primaryColor: primaryColor,
    primaryContrastingColor: primaryContrastingColor,
    textTheme: textTheme,
    barBackgroundColor: barBackgroundColor,
    scaffoldBackgroundColor: scaffoldBackgroundColor,
  );
}

SnackBarBehavior _uSnackBarBehavior(String v) {
  switch(v) {
    case 'fixed':
      return SnackBarBehavior.fixed;
    case 'floating':
      return SnackBarBehavior.floating;
  }
  throw 'illegal enum value $v';
}

SnackBarThemeData _uSnackBarThemeData(Map<String, dynamic> __m) {
  final backgroundColor = __m['backgroundColor'];
  final actionTextColor = __m['actionTextColor'];
  final disabledActionTextColor = __m['disabledActionTextColor'];
  final contentTextStyle = __m['contentTextStyle'];
  final elevation = __m['elevation'];
  final shape = __m['shape'];
  final behavior = __m['behavior'];
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
  final backgroundColor = __m['backgroundColor'];
  final elevation = __m['elevation'];
  final modalBackgroundColor = __m['modalBackgroundColor'];
  final modalElevation = __m['modalElevation'];
  final shape = __m['shape'];
  final clipBehavior = __m['clipBehavior'];
  final constraints = __m['constraints'];
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
  final color = __m['color'];
  final shape = __m['shape'];
  final elevation = __m['elevation'];
  final textStyle = __m['textStyle'];
  final enableFeedback = __m['enableFeedback'];
  return PopupMenuThemeData(
    color: color,
    shape: shape,
    elevation: elevation,
    textStyle: textStyle,
    enableFeedback: enableFeedback,
  );
}

MaterialBannerThemeData _uMaterialBannerThemeData(Map<String, dynamic> __m) {
  final backgroundColor = __m['backgroundColor'];
  final contentTextStyle = __m['contentTextStyle'];
  final padding = __m['padding'];
  final leadingPadding = __m['leadingPadding'];
  return MaterialBannerThemeData(
    backgroundColor: backgroundColor,
    contentTextStyle: contentTextStyle,
    padding: padding,
    leadingPadding: leadingPadding,
  );
}

DividerThemeData _uDividerThemeData(Map<String, dynamic> __m) {
  final color = __m['color'];
  final space = __m['space'];
  final thickness = __m['thickness'];
  final indent = __m['indent'];
  final endIndent = __m['endIndent'];
  return DividerThemeData(
    color: color,
    space: space,
    thickness: thickness,
    indent: indent,
    endIndent: endIndent,
  );
}

MainAxisAlignment _uMainAxisAlignment(String v) {
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
  throw 'illegal enum value $v';
}

MainAxisSize _uMainAxisSize(String v) {
  switch(v) {
    case 'min':
      return MainAxisSize.min;
    case 'max':
      return MainAxisSize.max;
  }
  throw 'illegal enum value $v';
}

VerticalDirection _uVerticalDirection(String v) {
  switch(v) {
    case 'up':
      return VerticalDirection.up;
    case 'down':
      return VerticalDirection.down;
  }
  throw 'illegal enum value $v';
}

ButtonBarThemeData _uButtonBarThemeData(Map<String, dynamic> __m) {
  final alignment = __m['alignment'];
  final mainAxisSize = __m['mainAxisSize'];
  final buttonTextTheme = __m['buttonTextTheme'];
  final buttonMinWidth = __m['buttonMinWidth'];
  final buttonHeight = __m['buttonHeight'];
  final buttonPadding = __m['buttonPadding'];
  final buttonAlignedDropdown = __m['buttonAlignedDropdown'];
  final layoutBehavior = __m['layoutBehavior'];
  final overflowDirection = __m['overflowDirection'];
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

BottomNavigationBarType _uBottomNavigationBarType(String v) {
  switch(v) {
    case 'fixed':
      return BottomNavigationBarType.fixed;
    case 'shifting':
      return BottomNavigationBarType.shifting;
  }
  throw 'illegal enum value $v';
}

BottomNavigationBarLandscapeLayout _uBottomNavigationBarLandscapeLayout(String v) {
  switch(v) {
    case 'spread':
      return BottomNavigationBarLandscapeLayout.spread;
    case 'centered':
      return BottomNavigationBarLandscapeLayout.centered;
    case 'linear':
      return BottomNavigationBarLandscapeLayout.linear;
  }
  throw 'illegal enum value $v';
}

BottomNavigationBarThemeData _uBottomNavigationBarThemeData(Map<String, dynamic> __m) {
  final backgroundColor = __m['backgroundColor'];
  final elevation = __m['elevation'];
  final selectedIconTheme = __m['selectedIconTheme'];
  final unselectedIconTheme = __m['unselectedIconTheme'];
  final selectedItemColor = __m['selectedItemColor'];
  final unselectedItemColor = __m['unselectedItemColor'];
  final selectedLabelStyle = __m['selectedLabelStyle'];
  final unselectedLabelStyle = __m['unselectedLabelStyle'];
  final showSelectedLabels = __m['showSelectedLabels'];
  final showUnselectedLabels = __m['showUnselectedLabels'];
  final type = __m['type'];
  final enableFeedback = __m['enableFeedback'];
  final landscapeLayout = __m['landscapeLayout'];
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
  final backgroundColor = __m['backgroundColor'];
  final hourMinuteTextColor = __m['hourMinuteTextColor'];
  final hourMinuteColor = __m['hourMinuteColor'];
  final dayPeriodTextColor = __m['dayPeriodTextColor'];
  final dayPeriodColor = __m['dayPeriodColor'];
  final dialHandColor = __m['dialHandColor'];
  final dialBackgroundColor = __m['dialBackgroundColor'];
  final dialTextColor = __m['dialTextColor'];
  final entryModeIconColor = __m['entryModeIconColor'];
  final hourMinuteTextStyle = __m['hourMinuteTextStyle'];
  final dayPeriodTextStyle = __m['dayPeriodTextStyle'];
  final helpTextStyle = __m['helpTextStyle'];
  final shape = __m['shape'];
  final hourMinuteShape = __m['hourMinuteShape'];
  final dayPeriodShape = __m['dayPeriodShape'];
  final dayPeriodBorderSide = __m['dayPeriodBorderSide'];
  final inputDecorationTheme = __m['inputDecorationTheme'];
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
  final textStyle = __m['textStyle'];
  final backgroundColor = __m['backgroundColor'];
  final foregroundColor = __m['foregroundColor'];
  final overlayColor = __m['overlayColor'];
  final shadowColor = __m['shadowColor'];
  final elevation = __m['elevation'];
  final padding = __m['padding'];
  final minimumSize = __m['minimumSize'];
  final fixedSize = __m['fixedSize'];
  final maximumSize = __m['maximumSize'];
  final side = __m['side'];
  final shape = __m['shape'];
  final mouseCursor = __m['mouseCursor'];
  final visualDensity = __m['visualDensity'];
  final tapTargetSize = __m['tapTargetSize'];
  final animationDuration = __m['animationDuration'];
  final enableFeedback = __m['enableFeedback'];
  final alignment = __m['alignment'];
  final splashFactory = __m['splashFactory'];
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
  final style = __m['style'];
  return TextButtonThemeData(
    style: style,
  );
}

ElevatedButtonThemeData _uElevatedButtonThemeData(Map<String, dynamic> __m) {
  final style = __m['style'];
  return ElevatedButtonThemeData(
    style: style,
  );
}

OutlinedButtonThemeData _uOutlinedButtonThemeData(Map<String, dynamic> __m) {
  final style = __m['style'];
  return OutlinedButtonThemeData(
    style: style,
  );
}

TextSelectionThemeData _uTextSelectionThemeData(Map<String, dynamic> __m) {
  final cursorColor = __m['cursorColor'];
  final selectionColor = __m['selectionColor'];
  final selectionHandleColor = __m['selectionHandleColor'];
  return TextSelectionThemeData(
    cursorColor: cursorColor,
    selectionColor: selectionColor,
    selectionHandleColor: selectionHandleColor,
  );
}

DataTableThemeData _uDataTableThemeData(Map<String, dynamic> __m) {
  final decoration = __m['decoration'];
  final dataRowColor = __m['dataRowColor'];
  final dataRowHeight = __m['dataRowHeight'];
  final dataTextStyle = __m['dataTextStyle'];
  final headingRowColor = __m['headingRowColor'];
  final headingRowHeight = __m['headingRowHeight'];
  final headingTextStyle = __m['headingTextStyle'];
  final horizontalMargin = __m['horizontalMargin'];
  final columnSpacing = __m['columnSpacing'];
  final dividerThickness = __m['dividerThickness'];
  final checkboxHorizontalMargin = __m['checkboxHorizontalMargin'];
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
  final mouseCursor = __m['mouseCursor'];
  final fillColor = __m['fillColor'];
  final checkColor = __m['checkColor'];
  final overlayColor = __m['overlayColor'];
  final splashRadius = __m['splashRadius'];
  final materialTapTargetSize = __m['materialTapTargetSize'];
  final visualDensity = __m['visualDensity'];
  final shape = __m['shape'];
  final side = __m['side'];
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
  final mouseCursor = __m['mouseCursor'];
  final fillColor = __m['fillColor'];
  final overlayColor = __m['overlayColor'];
  final splashRadius = __m['splashRadius'];
  final materialTapTargetSize = __m['materialTapTargetSize'];
  final visualDensity = __m['visualDensity'];
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
  final thumbColor = __m['thumbColor'];
  final trackColor = __m['trackColor'];
  final materialTapTargetSize = __m['materialTapTargetSize'];
  final mouseCursor = __m['mouseCursor'];
  final overlayColor = __m['overlayColor'];
  final splashRadius = __m['splashRadius'];
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
  final color = __m['color'];
  final linearTrackColor = __m['linearTrackColor'];
  final linearMinHeight = __m['linearMinHeight'];
  final circularTrackColor = __m['circularTrackColor'];
  final refreshBackgroundColor = __m['refreshBackgroundColor'];
  return ProgressIndicatorThemeData(
    color: color,
    linearTrackColor: linearTrackColor,
    linearMinHeight: linearMinHeight,
    circularTrackColor: circularTrackColor,
    refreshBackgroundColor: refreshBackgroundColor,
  );
}

ThemeData _uThemeData(Map<String, dynamic> __m) {
  final brightness = __m['brightness'];
  final visualDensity = __m['visualDensity'];
  final primarySwatch = __m['primarySwatch'];
  final primaryColor = __m['primaryColor'];
  final primaryColorBrightness = __m['primaryColorBrightness'];
  final primaryColorLight = __m['primaryColorLight'];
  final primaryColorDark = __m['primaryColorDark'];
  final accentColor = __m['accentColor'];
  final accentColorBrightness = __m['accentColorBrightness'];
  final canvasColor = __m['canvasColor'];
  final shadowColor = __m['shadowColor'];
  final scaffoldBackgroundColor = __m['scaffoldBackgroundColor'];
  final bottomAppBarColor = __m['bottomAppBarColor'];
  final cardColor = __m['cardColor'];
  final dividerColor = __m['dividerColor'];
  final focusColor = __m['focusColor'];
  final hoverColor = __m['hoverColor'];
  final highlightColor = __m['highlightColor'];
  final splashColor = __m['splashColor'];
  final splashFactory = __m['splashFactory'];
  final selectedRowColor = __m['selectedRowColor'];
  final unselectedWidgetColor = __m['unselectedWidgetColor'];
  final disabledColor = __m['disabledColor'];
  final buttonColor = __m['buttonColor'];
  final buttonTheme = __m['buttonTheme'];
  final toggleButtonsTheme = __m['toggleButtonsTheme'];
  final secondaryHeaderColor = __m['secondaryHeaderColor'];
  final textSelectionColor = __m['textSelectionColor'];
  final cursorColor = __m['cursorColor'];
  final textSelectionHandleColor = __m['textSelectionHandleColor'];
  final backgroundColor = __m['backgroundColor'];
  final dialogBackgroundColor = __m['dialogBackgroundColor'];
  final indicatorColor = __m['indicatorColor'];
  final hintColor = __m['hintColor'];
  final errorColor = __m['errorColor'];
  final toggleableActiveColor = __m['toggleableActiveColor'];
  final fontFamily = __m['fontFamily'];
  final textTheme = __m['textTheme'];
  final primaryTextTheme = __m['primaryTextTheme'];
  final accentTextTheme = __m['accentTextTheme'];
  final inputDecorationTheme = __m['inputDecorationTheme'];
  final iconTheme = __m['iconTheme'];
  final primaryIconTheme = __m['primaryIconTheme'];
  final accentIconTheme = __m['accentIconTheme'];
  final sliderTheme = __m['sliderTheme'];
  final tabBarTheme = __m['tabBarTheme'];
  final tooltipTheme = __m['tooltipTheme'];
  final cardTheme = __m['cardTheme'];
  final chipTheme = __m['chipTheme'];
  final platform = __m['platform'];
  final materialTapTargetSize = __m['materialTapTargetSize'];
  final applyElevationOverlayColor = __m['applyElevationOverlayColor'];
  final pageTransitionsTheme = __m['pageTransitionsTheme'];
  final appBarTheme = __m['appBarTheme'];
  final scrollbarTheme = __m['scrollbarTheme'];
  final bottomAppBarTheme = __m['bottomAppBarTheme'];
  final colorScheme = __m['colorScheme'];
  final dialogTheme = __m['dialogTheme'];
  final floatingActionButtonTheme = __m['floatingActionButtonTheme'];
  final navigationRailTheme = __m['navigationRailTheme'];
  final typography = __m['typography'];
  final cupertinoOverrideTheme = __m['cupertinoOverrideTheme'];
  final snackBarTheme = __m['snackBarTheme'];
  final bottomSheetTheme = __m['bottomSheetTheme'];
  final popupMenuTheme = __m['popupMenuTheme'];
  final bannerTheme = __m['bannerTheme'];
  final dividerTheme = __m['dividerTheme'];
  final buttonBarTheme = __m['buttonBarTheme'];
  final bottomNavigationBarTheme = __m['bottomNavigationBarTheme'];
  final timePickerTheme = __m['timePickerTheme'];
  final textButtonTheme = __m['textButtonTheme'];
  final elevatedButtonTheme = __m['elevatedButtonTheme'];
  final outlinedButtonTheme = __m['outlinedButtonTheme'];
  final textSelectionTheme = __m['textSelectionTheme'];
  final dataTableTheme = __m['dataTableTheme'];
  final checkboxTheme = __m['checkboxTheme'];
  final radioTheme = __m['radioTheme'];
  final switchTheme = __m['switchTheme'];
  final progressIndicatorTheme = __m['progressIndicatorTheme'];
  final fixTextFieldOutlineLabel = __m['fixTextFieldOutlineLabel'];
  final useTextSelectionTheme = __m['useTextSelectionTheme'];
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
  final visualDensity = __m['visualDensity'];
  final primaryColor = __m['primaryColor'];
  final primaryColorBrightness = __m['primaryColorBrightness'];
  final primaryColorLight = __m['primaryColorLight'];
  final primaryColorDark = __m['primaryColorDark'];
  final canvasColor = __m['canvasColor'];
  final shadowColor = __m['shadowColor'];
  final accentColor = __m['accentColor'];
  final accentColorBrightness = __m['accentColorBrightness'];
  final scaffoldBackgroundColor = __m['scaffoldBackgroundColor'];
  final bottomAppBarColor = __m['bottomAppBarColor'];
  final cardColor = __m['cardColor'];
  final dividerColor = __m['dividerColor'];
  final focusColor = __m['focusColor'];
  final hoverColor = __m['hoverColor'];
  final highlightColor = __m['highlightColor'];
  final splashColor = __m['splashColor'];
  final splashFactory = __m['splashFactory'];
  final selectedRowColor = __m['selectedRowColor'];
  final unselectedWidgetColor = __m['unselectedWidgetColor'];
  final disabledColor = __m['disabledColor'];
  final buttonTheme = __m['buttonTheme'];
  final buttonColor = __m['buttonColor'];
  final toggleButtonsTheme = __m['toggleButtonsTheme'];
  final secondaryHeaderColor = __m['secondaryHeaderColor'];
  final textSelectionColor = __m['textSelectionColor'];
  final cursorColor = __m['cursorColor'];
  final textSelectionHandleColor = __m['textSelectionHandleColor'];
  final backgroundColor = __m['backgroundColor'];
  final dialogBackgroundColor = __m['dialogBackgroundColor'];
  final indicatorColor = __m['indicatorColor'];
  final hintColor = __m['hintColor'];
  final errorColor = __m['errorColor'];
  final toggleableActiveColor = __m['toggleableActiveColor'];
  final textTheme = __m['textTheme'];
  final primaryTextTheme = __m['primaryTextTheme'];
  final accentTextTheme = __m['accentTextTheme'];
  final inputDecorationTheme = __m['inputDecorationTheme'];
  final iconTheme = __m['iconTheme'];
  final primaryIconTheme = __m['primaryIconTheme'];
  final accentIconTheme = __m['accentIconTheme'];
  final sliderTheme = __m['sliderTheme'];
  final tabBarTheme = __m['tabBarTheme'];
  final tooltipTheme = __m['tooltipTheme'];
  final cardTheme = __m['cardTheme'];
  final chipTheme = __m['chipTheme'];
  final platform = __m['platform'];
  final materialTapTargetSize = __m['materialTapTargetSize'];
  final applyElevationOverlayColor = __m['applyElevationOverlayColor'];
  final pageTransitionsTheme = __m['pageTransitionsTheme'];
  final appBarTheme = __m['appBarTheme'];
  final scrollbarTheme = __m['scrollbarTheme'];
  final bottomAppBarTheme = __m['bottomAppBarTheme'];
  final colorScheme = __m['colorScheme'];
  final dialogTheme = __m['dialogTheme'];
  final floatingActionButtonTheme = __m['floatingActionButtonTheme'];
  final navigationRailTheme = __m['navigationRailTheme'];
  final typography = __m['typography'];
  final cupertinoOverrideTheme = __m['cupertinoOverrideTheme'];
  final snackBarTheme = __m['snackBarTheme'];
  final bottomSheetTheme = __m['bottomSheetTheme'];
  final popupMenuTheme = __m['popupMenuTheme'];
  final bannerTheme = __m['bannerTheme'];
  final dividerTheme = __m['dividerTheme'];
  final buttonBarTheme = __m['buttonBarTheme'];
  final bottomNavigationBarTheme = __m['bottomNavigationBarTheme'];
  final timePickerTheme = __m['timePickerTheme'];
  final textButtonTheme = __m['textButtonTheme'];
  final elevatedButtonTheme = __m['elevatedButtonTheme'];
  final outlinedButtonTheme = __m['outlinedButtonTheme'];
  final textSelectionTheme = __m['textSelectionTheme'];
  final dataTableTheme = __m['dataTableTheme'];
  final checkboxTheme = __m['checkboxTheme'];
  final radioTheme = __m['radioTheme'];
  final switchTheme = __m['switchTheme'];
  final progressIndicatorTheme = __m['progressIndicatorTheme'];
  final fixTextFieldOutlineLabel = __m['fixTextFieldOutlineLabel'];
  final useTextSelectionTheme = __m['useTextSelectionTheme'];
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
  final colorScheme = __m['colorScheme'];
  final textTheme = __m['textTheme'];
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

ThemeMode _uThemeMode(String v) {
  switch(v) {
    case 'system':
      return ThemeMode.system;
    case 'light':
      return ThemeMode.light;
    case 'dark':
      return ThemeMode.dark;
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
  final location = __m['location'];
  final state = __m['state'];
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
  final _stackTrace = __m['_stackTrace'];
  return _StringStackTrace(
    _stackTrace,
  );
}

MaterialApp _uMaterialApp(Map<String, dynamic> __m) {
  final key = __m['key'];
  final navigatorKey = __m['navigatorKey'];
  final scaffoldMessengerKey = __m['scaffoldMessengerKey'];
  final home = __m['home'];
  final routes = __m['routes'];
  final initialRoute = __m['initialRoute'];
  final onGenerateRoute = __m['onGenerateRoute'];
  final onGenerateInitialRoutes = __m['onGenerateInitialRoutes'];
  final onUnknownRoute = __m['onUnknownRoute'];
  final navigatorObservers = __m['navigatorObservers'];
  final builder = __m['builder'];
  final title = __m['title'];
  final onGenerateTitle = __m['onGenerateTitle'];
  final color = __m['color'];
  final theme = __m['theme'];
  final darkTheme = __m['darkTheme'];
  final highContrastTheme = __m['highContrastTheme'];
  final highContrastDarkTheme = __m['highContrastDarkTheme'];
  final themeMode = __m['themeMode'];
  final locale = __m['locale'];
  final localizationsDelegates = __m['localizationsDelegates'];
  final localeListResolutionCallback = __m['localeListResolutionCallback'];
  final localeResolutionCallback = __m['localeResolutionCallback'];
  final supportedLocales = __m['supportedLocales'];
  final debugShowMaterialGrid = __m['debugShowMaterialGrid'];
  final showPerformanceOverlay = __m['showPerformanceOverlay'];
  final checkerboardRasterCacheImages = __m['checkerboardRasterCacheImages'];
  final checkerboardOffscreenLayers = __m['checkerboardOffscreenLayers'];
  final showSemanticsDebugger = __m['showSemanticsDebugger'];
  final debugShowCheckedModeBanner = __m['debugShowCheckedModeBanner'];
  final shortcuts = __m['shortcuts'];
  final actions = __m['actions'];
  final restorationScopeId = __m['restorationScopeId'];
  final scrollBehavior = __m['scrollBehavior'];
  final useInheritedMediaQuery = __m['useInheritedMediaQuery'];
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
  final key = __m['key'];
  final scaffoldMessengerKey = __m['scaffoldMessengerKey'];
  final routeInformationProvider = __m['routeInformationProvider'];
  final routeInformationParser = __m['routeInformationParser'];
  final routerDelegate = __m['routerDelegate'];
  final backButtonDispatcher = __m['backButtonDispatcher'];
  final builder = __m['builder'];
  final title = __m['title'];
  final onGenerateTitle = __m['onGenerateTitle'];
  final color = __m['color'];
  final theme = __m['theme'];
  final darkTheme = __m['darkTheme'];
  final highContrastTheme = __m['highContrastTheme'];
  final highContrastDarkTheme = __m['highContrastDarkTheme'];
  final themeMode = __m['themeMode'];
  final locale = __m['locale'];
  final localizationsDelegates = __m['localizationsDelegates'];
  final localeListResolutionCallback = __m['localeListResolutionCallback'];
  final localeResolutionCallback = __m['localeResolutionCallback'];
  final supportedLocales = __m['supportedLocales'];
  final debugShowMaterialGrid = __m['debugShowMaterialGrid'];
  final showPerformanceOverlay = __m['showPerformanceOverlay'];
  final checkerboardRasterCacheImages = __m['checkerboardRasterCacheImages'];
  final checkerboardOffscreenLayers = __m['checkerboardOffscreenLayers'];
  final showSemanticsDebugger = __m['showSemanticsDebugger'];
  final debugShowCheckedModeBanner = __m['debugShowCheckedModeBanner'];
  final shortcuts = __m['shortcuts'];
  final actions = __m['actions'];
  final restorationScopeId = __m['restorationScopeId'];
  final scrollBehavior = __m['scrollBehavior'];
  final useInheritedMediaQuery = __m['useInheritedMediaQuery'];
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

AppBar _uAppBar(Map<String, dynamic> __m) {
  final key = __m['key'];
  final leading = __m['leading'];
  final automaticallyImplyLeading = __m['automaticallyImplyLeading'];
  final title = __m['title'];
  final actions = __m['actions'];
  final flexibleSpace = __m['flexibleSpace'];
  final bottom = __m['bottom'];
  final elevation = __m['elevation'];
  final shadowColor = __m['shadowColor'];
  final shape = __m['shape'];
  final backgroundColor = __m['backgroundColor'];
  final foregroundColor = __m['foregroundColor'];
  final brightness = __m['brightness'];
  final iconTheme = __m['iconTheme'];
  final actionsIconTheme = __m['actionsIconTheme'];
  final textTheme = __m['textTheme'];
  final primary = __m['primary'];
  final centerTitle = __m['centerTitle'];
  final excludeHeaderSemantics = __m['excludeHeaderSemantics'];
  final titleSpacing = __m['titleSpacing'];
  final toolbarOpacity = __m['toolbarOpacity'];
  final bottomOpacity = __m['bottomOpacity'];
  final toolbarHeight = __m['toolbarHeight'];
  final leadingWidth = __m['leadingWidth'];
  final backwardsCompatibility = __m['backwardsCompatibility'];
  final toolbarTextStyle = __m['toolbarTextStyle'];
  final titleTextStyle = __m['titleTextStyle'];
  final systemOverlayStyle = __m['systemOverlayStyle'];
  return AppBar(
    key: key,
    leading: leading,
    automaticallyImplyLeading: automaticallyImplyLeading,
    title: title,
    actions: actions,
    flexibleSpace: flexibleSpace,
    bottom: bottom,
    elevation: elevation,
    shadowColor: shadowColor,
    shape: shape,
    backgroundColor: backgroundColor,
    foregroundColor: foregroundColor,
    brightness: brightness,
    iconTheme: iconTheme,
    actionsIconTheme: actionsIconTheme,
    textTheme: textTheme,
    primary: primary,
    centerTitle: centerTitle,
    excludeHeaderSemantics: excludeHeaderSemantics,
    titleSpacing: titleSpacing,
    toolbarOpacity: toolbarOpacity,
    bottomOpacity: bottomOpacity,
    toolbarHeight: toolbarHeight,
    leadingWidth: leadingWidth,
    backwardsCompatibility: backwardsCompatibility,
    toolbarTextStyle: toolbarTextStyle,
    titleTextStyle: titleTextStyle,
    systemOverlayStyle: systemOverlayStyle,
  );
}

KeyEventResult _uKeyEventResult(String v) {
  switch(v) {
    case 'handled':
      return KeyEventResult.handled;
    case 'ignored':
      return KeyEventResult.ignored;
    case 'skipRemainingHandlers':
      return KeyEventResult.skipRemainingHandlers;
  }
  throw 'illegal enum value $v';
}

PhysicalKeyboardKey _uPhysicalKeyboardKey(Map<String, dynamic> __m) {
  final usbHidUsage = __m['usbHidUsage'];
  return PhysicalKeyboardKey(
    usbHidUsage,
  );
}

LogicalKeyboardKey _uLogicalKeyboardKey(Map<String, dynamic> __m) {
  final keyId = __m['keyId'];
  return LogicalKeyboardKey(
    keyId,
  );
}

FocusNode _uFocusNode(Map<String, dynamic> __m) {
  final debugLabel = __m['debugLabel'];
  final onKey = __m['onKey'];
  final onKeyEvent = __m['onKeyEvent'];
  final skipTraversal = __m['skipTraversal'];
  final canRequestFocus = __m['canRequestFocus'];
  final descendantsAreFocusable = __m['descendantsAreFocusable'];
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
  final key = __m['key'];
  final onPressed = __m['onPressed'];
  final onLongPress = __m['onLongPress'];
  final style = __m['style'];
  final focusNode = __m['focusNode'];
  final autofocus = __m['autofocus'];
  final clipBehavior = __m['clipBehavior'];
  final child = __m['child'];
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
  final key = __m['key'];
  final onPressed = __m['onPressed'];
  final onLongPress = __m['onLongPress'];
  final style = __m['style'];
  final focusNode = __m['focusNode'];
  final autofocus = __m['autofocus'];
  final clipBehavior = __m['clipBehavior'];
  final icon = __m['icon'];
  final label = __m['label'];
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

ListTile _uListTile(Map<String, dynamic> __m) {
  final key = __m['key'];
  final leading = __m['leading'];
  final title = __m['title'];
  final subtitle = __m['subtitle'];
  final trailing = __m['trailing'];
  final isThreeLine = __m['isThreeLine'];
  final dense = __m['dense'];
  final visualDensity = __m['visualDensity'];
  final shape = __m['shape'];
  final contentPadding = __m['contentPadding'];
  final enabled = __m['enabled'];
  final onTap = __m['onTap'];
  final onLongPress = __m['onLongPress'];
  final mouseCursor = __m['mouseCursor'];
  final selected = __m['selected'];
  final focusColor = __m['focusColor'];
  final hoverColor = __m['hoverColor'];
  final focusNode = __m['focusNode'];
  final autofocus = __m['autofocus'];
  final tileColor = __m['tileColor'];
  final selectedTileColor = __m['selectedTileColor'];
  final enableFeedback = __m['enableFeedback'];
  final horizontalTitleGap = __m['horizontalTitleGap'];
  final minVerticalPadding = __m['minVerticalPadding'];
  final minLeadingWidth = __m['minLeadingWidth'];
  return ListTile(
    key: key,
    leading: leading,
    title: title,
    subtitle: subtitle,
    trailing: trailing,
    isThreeLine: isThreeLine,
    dense: dense,
    visualDensity: visualDensity,
    shape: shape,
    contentPadding: contentPadding,
    enabled: enabled,
    onTap: onTap,
    onLongPress: onLongPress,
    mouseCursor: mouseCursor,
    selected: selected,
    focusColor: focusColor,
    hoverColor: hoverColor,
    focusNode: focusNode,
    autofocus: autofocus,
    tileColor: tileColor,
    selectedTileColor: selectedTileColor,
    enableFeedback: enableFeedback,
    horizontalTitleGap: horizontalTitleGap,
    minVerticalPadding: minVerticalPadding,
    minLeadingWidth: minLeadingWidth,
  );
}

DragStartBehavior _uDragStartBehavior(String v) {
  switch(v) {
    case 'down':
      return DragStartBehavior.down;
    case 'start':
      return DragStartBehavior.start;
  }
  throw 'illegal enum value $v';
}

Scaffold _uScaffold(Map<String, dynamic> __m) {
  final key = __m['key'];
  final appBar = __m['appBar'];
  final body = __m['body'];
  final floatingActionButton = __m['floatingActionButton'];
  final floatingActionButtonLocation = __m['floatingActionButtonLocation'];
  final floatingActionButtonAnimator = __m['floatingActionButtonAnimator'];
  final persistentFooterButtons = __m['persistentFooterButtons'];
  final drawer = __m['drawer'];
  final onDrawerChanged = __m['onDrawerChanged'];
  final endDrawer = __m['endDrawer'];
  final onEndDrawerChanged = __m['onEndDrawerChanged'];
  final bottomNavigationBar = __m['bottomNavigationBar'];
  final bottomSheet = __m['bottomSheet'];
  final backgroundColor = __m['backgroundColor'];
  final resizeToAvoidBottomInset = __m['resizeToAvoidBottomInset'];
  final primary = __m['primary'];
  final drawerDragStartBehavior = __m['drawerDragStartBehavior'];
  final extendBody = __m['extendBody'];
  final extendBodyBehindAppBar = __m['extendBodyBehindAppBar'];
  final drawerScrimColor = __m['drawerScrimColor'];
  final drawerEdgeDragWidth = __m['drawerEdgeDragWidth'];
  final drawerEnableOpenDragGesture = __m['drawerEnableOpenDragGesture'];
  final endDrawerEnableOpenDragGesture = __m['endDrawerEnableOpenDragGesture'];
  final restorationId = __m['restorationId'];
  return Scaffold(
    key: key,
    appBar: appBar,
    body: body,
    floatingActionButton: floatingActionButton,
    floatingActionButtonLocation: floatingActionButtonLocation,
    floatingActionButtonAnimator: floatingActionButtonAnimator,
    persistentFooterButtons: persistentFooterButtons,
    drawer: drawer,
    onDrawerChanged: onDrawerChanged,
    endDrawer: endDrawer,
    onEndDrawerChanged: onEndDrawerChanged,
    bottomNavigationBar: bottomNavigationBar,
    bottomSheet: bottomSheet,
    backgroundColor: backgroundColor,
    resizeToAvoidBottomInset: resizeToAvoidBottomInset,
    primary: primary,
    drawerDragStartBehavior: drawerDragStartBehavior,
    extendBody: extendBody,
    extendBodyBehindAppBar: extendBodyBehindAppBar,
    drawerScrimColor: drawerScrimColor,
    drawerEdgeDragWidth: drawerEdgeDragWidth,
    drawerEnableOpenDragGesture: drawerEnableOpenDragGesture,
    endDrawerEnableOpenDragGesture: endDrawerEnableOpenDragGesture,
    restorationId: restorationId,
  );
}

WindowPadding _uWindowPadding(Map<String, dynamic> __m) {
  return WindowPadding(
  );
}

EdgeInsets _uEdgeInsets(Map<String, dynamic> __m) {
  return EdgeInsets(
  );
}

EdgeInsets _ufromLTRBEdgeInsets(Map<String, dynamic> __m) {
  final left = __m['left'];
  final top = __m['top'];
  final right = __m['right'];
  final bottom = __m['bottom'];
  return EdgeInsets.fromLTRB(
    left,
    top,
    right,
    bottom,
  );
}

EdgeInsets _uallEdgeInsets(Map<String, dynamic> __m) {
  final value = __m['value'];
  return EdgeInsets.all(
    value,
  );
}

EdgeInsets _uonlyEdgeInsets(Map<String, dynamic> __m) {
  final left = __m['left'];
  final top = __m['top'];
  final right = __m['right'];
  final bottom = __m['bottom'];
  return EdgeInsets.only(
    left: left,
    top: top,
    right: right,
    bottom: bottom,
  );
}

EdgeInsets _usymmetricEdgeInsets(Map<String, dynamic> __m) {
  final vertical = __m['vertical'];
  final horizontal = __m['horizontal'];
  return EdgeInsets.symmetric(
    vertical: vertical,
    horizontal: horizontal,
  );
}

EdgeInsets _ufromWindowPaddingEdgeInsets(Map<String, dynamic> __m) {
  final padding = __m['padding'];
  final devicePixelRatio = __m['devicePixelRatio'];
  return EdgeInsets.fromWindowPadding(
    padding,
    devicePixelRatio,
  );
}

Axis _uAxis(String v) {
  switch(v) {
    case 'horizontal':
      return Axis.horizontal;
    case 'vertical':
      return Axis.vertical;
  }
  throw 'illegal enum value $v';
}

ChangeNotifier _uChangeNotifier(Map<String, dynamic> __m) {
  return ChangeNotifier(
  );
}

ScrollController _uScrollController(Map<String, dynamic> __m) {
  final initialScrollOffset = __m['initialScrollOffset'];
  final keepScrollOffset = __m['keepScrollOffset'];
  final debugLabel = __m['debugLabel'];
  return ScrollController(
    initialScrollOffset: initialScrollOffset,
    keepScrollOffset: keepScrollOffset,
    debugLabel: debugLabel,
  );
}

ScrollPhysics _uScrollPhysics(Map<String, dynamic> __m) {
  final parent = __m['parent'];
  return ScrollPhysics(
    parent: parent,
  );
}

ScrollViewKeyboardDismissBehavior _uScrollViewKeyboardDismissBehavior(String v) {
  switch(v) {
    case 'manual':
      return ScrollViewKeyboardDismissBehavior.manual;
    case 'onDrag':
      return ScrollViewKeyboardDismissBehavior.onDrag;
  }
  throw 'illegal enum value $v';
}

ListView _uListView(Map<String, dynamic> __m) {
  final key = __m['key'];
  final scrollDirection = __m['scrollDirection'];
  final reverse = __m['reverse'];
  final controller = __m['controller'];
  final primary = __m['primary'];
  final physics = __m['physics'];
  final shrinkWrap = __m['shrinkWrap'];
  final padding = __m['padding'];
  final itemExtent = __m['itemExtent'];
  final prototypeItem = __m['prototypeItem'];
  final addAutomaticKeepAlives = __m['addAutomaticKeepAlives'];
  final addRepaintBoundaries = __m['addRepaintBoundaries'];
  final addSemanticIndexes = __m['addSemanticIndexes'];
  final cacheExtent = __m['cacheExtent'];
  final children = __m['children'];
  final semanticChildCount = __m['semanticChildCount'];
  final dragStartBehavior = __m['dragStartBehavior'];
  final keyboardDismissBehavior = __m['keyboardDismissBehavior'];
  final restorationId = __m['restorationId'];
  final clipBehavior = __m['clipBehavior'];
  return ListView(
    key: key,
    scrollDirection: scrollDirection,
    reverse: reverse,
    controller: controller,
    primary: primary,
    physics: physics,
    shrinkWrap: shrinkWrap,
    padding: padding,
    itemExtent: itemExtent,
    prototypeItem: prototypeItem,
    addAutomaticKeepAlives: addAutomaticKeepAlives,
    addRepaintBoundaries: addRepaintBoundaries,
    addSemanticIndexes: addSemanticIndexes,
    cacheExtent: cacheExtent,
    children: children,
    semanticChildCount: semanticChildCount,
    dragStartBehavior: dragStartBehavior,
    keyboardDismissBehavior: keyboardDismissBehavior,
    restorationId: restorationId,
    clipBehavior: clipBehavior,
  );
}

ListView _ubuilderListView(Map<String, dynamic> __m) {
  final key = __m['key'];
  final scrollDirection = __m['scrollDirection'];
  final reverse = __m['reverse'];
  final controller = __m['controller'];
  final primary = __m['primary'];
  final physics = __m['physics'];
  final shrinkWrap = __m['shrinkWrap'];
  final padding = __m['padding'];
  final itemExtent = __m['itemExtent'];
  final prototypeItem = __m['prototypeItem'];
  final itemBuilder = __m['itemBuilder'];
  final itemCount = __m['itemCount'];
  final addAutomaticKeepAlives = __m['addAutomaticKeepAlives'];
  final addRepaintBoundaries = __m['addRepaintBoundaries'];
  final addSemanticIndexes = __m['addSemanticIndexes'];
  final cacheExtent = __m['cacheExtent'];
  final semanticChildCount = __m['semanticChildCount'];
  final dragStartBehavior = __m['dragStartBehavior'];
  final keyboardDismissBehavior = __m['keyboardDismissBehavior'];
  final restorationId = __m['restorationId'];
  final clipBehavior = __m['clipBehavior'];
  return ListView.builder(
    key: key,
    scrollDirection: scrollDirection,
    reverse: reverse,
    controller: controller,
    primary: primary,
    physics: physics,
    shrinkWrap: shrinkWrap,
    padding: padding,
    itemExtent: itemExtent,
    prototypeItem: prototypeItem,
    itemBuilder: itemBuilder,
    itemCount: itemCount,
    addAutomaticKeepAlives: addAutomaticKeepAlives,
    addRepaintBoundaries: addRepaintBoundaries,
    addSemanticIndexes: addSemanticIndexes,
    cacheExtent: cacheExtent,
    semanticChildCount: semanticChildCount,
    dragStartBehavior: dragStartBehavior,
    keyboardDismissBehavior: keyboardDismissBehavior,
    restorationId: restorationId,
    clipBehavior: clipBehavior,
  );
}

ListView _useparatedListView(Map<String, dynamic> __m) {
  final key = __m['key'];
  final scrollDirection = __m['scrollDirection'];
  final reverse = __m['reverse'];
  final controller = __m['controller'];
  final primary = __m['primary'];
  final physics = __m['physics'];
  final shrinkWrap = __m['shrinkWrap'];
  final padding = __m['padding'];
  final itemBuilder = __m['itemBuilder'];
  final separatorBuilder = __m['separatorBuilder'];
  final itemCount = __m['itemCount'];
  final addAutomaticKeepAlives = __m['addAutomaticKeepAlives'];
  final addRepaintBoundaries = __m['addRepaintBoundaries'];
  final addSemanticIndexes = __m['addSemanticIndexes'];
  final cacheExtent = __m['cacheExtent'];
  final dragStartBehavior = __m['dragStartBehavior'];
  final keyboardDismissBehavior = __m['keyboardDismissBehavior'];
  final restorationId = __m['restorationId'];
  final clipBehavior = __m['clipBehavior'];
  return ListView.separated(
    key: key,
    scrollDirection: scrollDirection,
    reverse: reverse,
    controller: controller,
    primary: primary,
    physics: physics,
    shrinkWrap: shrinkWrap,
    padding: padding,
    itemBuilder: itemBuilder,
    separatorBuilder: separatorBuilder,
    itemCount: itemCount,
    addAutomaticKeepAlives: addAutomaticKeepAlives,
    addRepaintBoundaries: addRepaintBoundaries,
    addSemanticIndexes: addSemanticIndexes,
    cacheExtent: cacheExtent,
    dragStartBehavior: dragStartBehavior,
    keyboardDismissBehavior: keyboardDismissBehavior,
    restorationId: restorationId,
    clipBehavior: clipBehavior,
  );
}

ListView _ucustomListView(Map<String, dynamic> __m) {
  final key = __m['key'];
  final scrollDirection = __m['scrollDirection'];
  final reverse = __m['reverse'];
  final controller = __m['controller'];
  final primary = __m['primary'];
  final physics = __m['physics'];
  final shrinkWrap = __m['shrinkWrap'];
  final padding = __m['padding'];
  final itemExtent = __m['itemExtent'];
  final prototypeItem = __m['prototypeItem'];
  final childrenDelegate = __m['childrenDelegate'];
  final cacheExtent = __m['cacheExtent'];
  final semanticChildCount = __m['semanticChildCount'];
  final dragStartBehavior = __m['dragStartBehavior'];
  final keyboardDismissBehavior = __m['keyboardDismissBehavior'];
  final restorationId = __m['restorationId'];
  final clipBehavior = __m['clipBehavior'];
  return ListView.custom(
    key: key,
    scrollDirection: scrollDirection,
    reverse: reverse,
    controller: controller,
    primary: primary,
    physics: physics,
    shrinkWrap: shrinkWrap,
    padding: padding,
    itemExtent: itemExtent,
    prototypeItem: prototypeItem,
    childrenDelegate: childrenDelegate,
    cacheExtent: cacheExtent,
    semanticChildCount: semanticChildCount,
    dragStartBehavior: dragStartBehavior,
    keyboardDismissBehavior: keyboardDismissBehavior,
    restorationId: restorationId,
    clipBehavior: clipBehavior,
  );
}

StrutStyle _uStrutStyle(Map<String, dynamic> __m) {
  final fontFamily = __m['fontFamily'];
  final fontFamilyFallback = __m['fontFamilyFallback'];
  final fontSize = __m['fontSize'];
  final height = __m['height'];
  final leadingDistribution = __m['leadingDistribution'];
  final leading = __m['leading'];
  final fontWeight = __m['fontWeight'];
  final fontStyle = __m['fontStyle'];
  final forceStrutHeight = __m['forceStrutHeight'];
  final debugLabel = __m['debugLabel'];
  final package = __m['package'];
  return StrutStyle(
    fontFamily: fontFamily,
    fontFamilyFallback: fontFamilyFallback,
    fontSize: fontSize,
    height: height,
    leadingDistribution: leadingDistribution,
    leading: leading,
    fontWeight: fontWeight,
    fontStyle: fontStyle,
    forceStrutHeight: forceStrutHeight,
    debugLabel: debugLabel,
    package: package,
  );
}

StrutStyle _ufromTextStyleStrutStyle(Map<String, dynamic> __m) {
  final textStyle = __m['textStyle'];
  final fontFamily = __m['fontFamily'];
  final fontFamilyFallback = __m['fontFamilyFallback'];
  final fontSize = __m['fontSize'];
  final height = __m['height'];
  final leadingDistribution = __m['leadingDistribution'];
  final leading = __m['leading'];
  final fontWeight = __m['fontWeight'];
  final fontStyle = __m['fontStyle'];
  final forceStrutHeight = __m['forceStrutHeight'];
  final debugLabel = __m['debugLabel'];
  final package = __m['package'];
  return StrutStyle.fromTextStyle(
    textStyle,
    fontFamily: fontFamily,
    fontFamilyFallback: fontFamilyFallback,
    fontSize: fontSize,
    height: height,
    leadingDistribution: leadingDistribution,
    leading: leading,
    fontWeight: fontWeight,
    fontStyle: fontStyle,
    forceStrutHeight: forceStrutHeight,
    debugLabel: debugLabel,
    package: package,
  );
}

TextAlign _uTextAlign(String v) {
  switch(v) {
    case 'left':
      return TextAlign.left;
    case 'right':
      return TextAlign.right;
    case 'center':
      return TextAlign.center;
    case 'justify':
      return TextAlign.justify;
    case 'start':
      return TextAlign.start;
    case 'end':
      return TextAlign.end;
  }
  throw 'illegal enum value $v';
}

TextWidthBasis _uTextWidthBasis(String v) {
  switch(v) {
    case 'parent':
      return TextWidthBasis.parent;
    case 'longestLine':
      return TextWidthBasis.longestLine;
  }
  throw 'illegal enum value $v';
}

TextHeightBehavior _uTextHeightBehavior(Map<String, dynamic> __m) {
  final applyHeightToFirstAscent = __m['applyHeightToFirstAscent'];
  final applyHeightToLastDescent = __m['applyHeightToLastDescent'];
  final leadingDistribution = __m['leadingDistribution'];
  return TextHeightBehavior(
    applyHeightToFirstAscent: applyHeightToFirstAscent,
    applyHeightToLastDescent: applyHeightToLastDescent,
    leadingDistribution: leadingDistribution,
  );
}

Text _uText(Map<String, dynamic> __m) {
  final data = __m['data'];
  final key = __m['key'];
  final style = __m['style'];
  final strutStyle = __m['strutStyle'];
  final textAlign = __m['textAlign'];
  final textDirection = __m['textDirection'];
  final locale = __m['locale'];
  final softWrap = __m['softWrap'];
  final overflow = __m['overflow'];
  final textScaleFactor = __m['textScaleFactor'];
  final maxLines = __m['maxLines'];
  final semanticsLabel = __m['semanticsLabel'];
  final textWidthBasis = __m['textWidthBasis'];
  final textHeightBehavior = __m['textHeightBehavior'];
  return Text(
    data,
    key: key,
    style: style,
    strutStyle: strutStyle,
    textAlign: textAlign,
    textDirection: textDirection,
    locale: locale,
    softWrap: softWrap,
    overflow: overflow,
    textScaleFactor: textScaleFactor,
    maxLines: maxLines,
    semanticsLabel: semanticsLabel,
    textWidthBasis: textWidthBasis,
    textHeightBehavior: textHeightBehavior,
  );
}

Text _urichText(Map<String, dynamic> __m) {
  final textSpan = __m['textSpan'];
  final key = __m['key'];
  final style = __m['style'];
  final strutStyle = __m['strutStyle'];
  final textAlign = __m['textAlign'];
  final textDirection = __m['textDirection'];
  final locale = __m['locale'];
  final softWrap = __m['softWrap'];
  final overflow = __m['overflow'];
  final textScaleFactor = __m['textScaleFactor'];
  final maxLines = __m['maxLines'];
  final semanticsLabel = __m['semanticsLabel'];
  final textWidthBasis = __m['textWidthBasis'];
  final textHeightBehavior = __m['textHeightBehavior'];
  return Text.rich(
    textSpan,
    key: key,
    style: style,
    strutStyle: strutStyle,
    textAlign: textAlign,
    textDirection: textDirection,
    locale: locale,
    softWrap: softWrap,
    overflow: overflow,
    textScaleFactor: textScaleFactor,
    maxLines: maxLines,
    semanticsLabel: semanticsLabel,
    textWidthBasis: textWidthBasis,
    textHeightBehavior: textHeightBehavior,
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
  'FontWeight.': _uFontWeight,
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
  'TextDecoration.': _uTextDecoration,
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
  'Radius.': _uRadius,
  'Radius.circular': _ucircularRadius,
  'Radius.elliptical': _uellipticalRadius,
  'BorderRadius.': _uBorderRadius,
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
  'AppBar.': _uAppBar,
  'PhysicalKeyboardKey.': _uPhysicalKeyboardKey,
  'LogicalKeyboardKey.': _uLogicalKeyboardKey,
  'FocusNode.': _uFocusNode,
  'ElevatedButton.': _uElevatedButton,
  'ElevatedButton.icon': _uiconElevatedButton,
  'ListTile.': _uListTile,
  'Scaffold.': _uScaffold,
  'WindowPadding.': _uWindowPadding,
  'EdgeInsets.': _uEdgeInsets,
  'EdgeInsets.fromLTRB': _ufromLTRBEdgeInsets,
  'EdgeInsets.all': _uallEdgeInsets,
  'EdgeInsets.only': _uonlyEdgeInsets,
  'EdgeInsets.symmetric': _usymmetricEdgeInsets,
  'EdgeInsets.fromWindowPadding': _ufromWindowPaddingEdgeInsets,
  'ChangeNotifier.': _uChangeNotifier,
  'ScrollController.': _uScrollController,
  'ScrollPhysics.': _uScrollPhysics,
  'ListView.': _uListView,
  'ListView.builder': _ubuilderListView,
  'ListView.separated': _useparatedListView,
  'ListView.custom': _ucustomListView,
  'StrutStyle.': _uStrutStyle,
  'StrutStyle.fromTextStyle': _ufromTextStyleStrutStyle,
  'TextHeightBehavior.': _uTextHeightBehavior,
  'Text.': _uText,
  'Text.rich': _urichText,
};
