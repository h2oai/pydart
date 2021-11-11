from enum import Enum
from typing import Generic, TypeVar, Callable, Any, Optional, Iterable, List, Dict

T = TypeVar('T')


# packages/flutter/lib/src/foundation/key.dart
class Key:
    def __init__(
            self,
            value: str,
    ):
        self.__ctor = (('',), (
            'value', value,
        ))

    @staticmethod
    def empty(
    ) -> 'Key':
        _o = Key(
            value='',
        )
        _o.__ctor = (('empty',), (
        ))
        return _o


# packages/flutter/lib/src/material/scaffold.dart
class ScaffoldMessengerState:
    pass


# packages/flutter/lib/src/widgets/framework.dart
class GlobalKey(Generic[T]):
    def __init__(
            self,
            debug_label: Optional[str] = None,
    ):
        self.__ctor = (('',), (
            'debugLabel', debug_label,
        ))

    @staticmethod
    def constructor(
    ) -> 'GlobalKey':
        _o = GlobalKey(
        )
        _o.__ctor = (('constructor',), (
        ))
        return _o


# packages/flutter/lib/src/widgets/router.dart
class RouteInformationProvider:
    pass


# bin/cache/pkg/sky_engine/lib/core/object.dart
class Object:
    pass


# packages/flutter/lib/src/widgets/router.dart
class RouteInformationParser(Generic[T]):
    pass


# packages/flutter/lib/src/widgets/router.dart
class RouterDelegate(Generic[T]):
    pass


# packages/flutter/lib/src/widgets/router.dart
class BackButtonDispatcher:
    pass


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Color:
    def __init__(
            self,
            value: int,
    ):
        self.__ctor = (('',), (
            'value', value,
        ))

    @staticmethod
    def from_argb(
            a: int,
            r: int,
            g: int,
            b: int,
    ) -> 'Color':
        _o = Color(
            value=0,
        )
        _o.__ctor = (('fromARGB',), (
            'a', a,
            'r', r,
            'g', g,
            'b', b,
        ))
        return _o

    @staticmethod
    def from_rgbo(
            r: int,
            g: int,
            b: int,
            opacity: float,
    ) -> 'Color':
        _o = Color(
            value=0,
        )
        _o.__ctor = (('fromRGBO',), (
            'r', r,
            'g', g,
            'b', b,
            'opacity', opacity,
        ))
        return _o


# packages/flutter/lib/src/material/theme_data.dart
class VisualDensity:
    minimum_density: float = -4.0
    maximum_density: float = 4.0

    def __init__(
            self,
            horizontal: Optional[float] = None,
            vertical: Optional[float] = None,
    ):
        self.__ctor = (('',), (
            'horizontal', horizontal,
            'vertical', vertical,
        ))


VisualDensity.standard = VisualDensity(
)
VisualDensity.standard.__ctor = ('standard', )
VisualDensity.comfortable = VisualDensity(
)
VisualDensity.comfortable.__ctor = ('comfortable', )
VisualDensity.compact = VisualDensity(
)
VisualDensity.compact.__ctor = ('compact', )


# bin/cache/pkg/sky_engine/lib/ui/window.dart
class Brightness(Enum):
    index = 'index'
    values = 'values'
    dark = 'dark'
    light = 'light'


# packages/flutter/lib/src/material/ink_well.dart
class InteractiveInkFeatureFactory:
    pass


# packages/flutter/lib/src/material/button_theme.dart
class ButtonTextTheme(Enum):
    index = 'index'
    values = 'values'
    normal = 'normal'
    accent = 'accent'
    primary = 'primary'


# packages/flutter/lib/src/painting/edge_insets.dart
class EdgeInsetsGeometry:
    pass


EdgeInsetsGeometry.infinity = EdgeInsetsGeometry(
)
EdgeInsetsGeometry.infinity.__ctor = ('infinity', )


# packages/flutter/lib/src/painting/borders.dart
class ShapeBorder:
    pass


# packages/flutter/lib/src/material/button_theme.dart
class ButtonBarLayoutBehavior(Enum):
    index = 'index'
    values = 'values'
    constrained = 'constrained'
    padded = 'padded'


# packages/flutter/lib/src/material/colors.dart
class MaterialColor:
    def __init__(
            self,
            primary: int,
            swatch: Dict[int, Color],
    ):
        self.__ctor = (('',), (
            'primary', primary,
            'swatch', swatch,
        ))


# packages/flutter/lib/src/material/color_scheme.dart
class ColorScheme:
    def __init__(
            self,
            primary: Color,
            primary_variant: Color,
            secondary: Color,
            secondary_variant: Color,
            surface: Color,
            background: Color,
            error: Color,
            on_primary: Color,
            on_secondary: Color,
            on_surface: Color,
            on_background: Color,
            on_error: Color,
            brightness: Brightness,
    ):
        self.__ctor = (('',), (
            'primary', primary,
            'primaryVariant', primary_variant,
            'secondary', secondary,
            'secondaryVariant', secondary_variant,
            'surface', surface,
            'background', background,
            'error', error,
            'onPrimary', on_primary,
            'onSecondary', on_secondary,
            'onSurface', on_surface,
            'onBackground', on_background,
            'onError', on_error,
            'brightness', brightness,
        ))

    @staticmethod
    def light(
            primary: Optional[Color] = None,
            primary_variant: Optional[Color] = None,
            secondary: Optional[Color] = None,
            secondary_variant: Optional[Color] = None,
            surface: Optional[Color] = None,
            background: Optional[Color] = None,
            error: Optional[Color] = None,
            on_primary: Optional[Color] = None,
            on_secondary: Optional[Color] = None,
            on_surface: Optional[Color] = None,
            on_background: Optional[Color] = None,
            on_error: Optional[Color] = None,
            brightness: Optional[Brightness] = None,
    ) -> 'ColorScheme':
        _o = ColorScheme(
            primary=Color(0),
            primary_variant=Color(0),
            secondary=Color(0),
            secondary_variant=Color(0),
            surface=Color(0),
            background=Color(0),
            error=Color(0),
            on_primary=Color(0),
            on_secondary=Color(0),
            on_surface=Color(0),
            on_background=Color(0),
            on_error=Color(0),
            brightness=Brightness.index,
        )
        _o.__ctor = (('light',), (
            'primary', primary,
            'primaryVariant', primary_variant,
            'secondary', secondary,
            'secondaryVariant', secondary_variant,
            'surface', surface,
            'background', background,
            'error', error,
            'onPrimary', on_primary,
            'onSecondary', on_secondary,
            'onSurface', on_surface,
            'onBackground', on_background,
            'onError', on_error,
            'brightness', brightness,
        ))
        return _o

    @staticmethod
    def dark(
            primary: Optional[Color] = None,
            primary_variant: Optional[Color] = None,
            secondary: Optional[Color] = None,
            secondary_variant: Optional[Color] = None,
            surface: Optional[Color] = None,
            background: Optional[Color] = None,
            error: Optional[Color] = None,
            on_primary: Optional[Color] = None,
            on_secondary: Optional[Color] = None,
            on_surface: Optional[Color] = None,
            on_background: Optional[Color] = None,
            on_error: Optional[Color] = None,
            brightness: Optional[Brightness] = None,
    ) -> 'ColorScheme':
        _o = ColorScheme(
            primary=Color(0),
            primary_variant=Color(0),
            secondary=Color(0),
            secondary_variant=Color(0),
            surface=Color(0),
            background=Color(0),
            error=Color(0),
            on_primary=Color(0),
            on_secondary=Color(0),
            on_surface=Color(0),
            on_background=Color(0),
            on_error=Color(0),
            brightness=Brightness.index,
        )
        _o.__ctor = (('dark',), (
            'primary', primary,
            'primaryVariant', primary_variant,
            'secondary', secondary,
            'secondaryVariant', secondary_variant,
            'surface', surface,
            'background', background,
            'error', error,
            'onPrimary', on_primary,
            'onSecondary', on_secondary,
            'onSurface', on_surface,
            'onBackground', on_background,
            'onError', on_error,
            'brightness', brightness,
        ))
        return _o

    @staticmethod
    def high_contrast_light(
            primary: Optional[Color] = None,
            primary_variant: Optional[Color] = None,
            secondary: Optional[Color] = None,
            secondary_variant: Optional[Color] = None,
            surface: Optional[Color] = None,
            background: Optional[Color] = None,
            error: Optional[Color] = None,
            on_primary: Optional[Color] = None,
            on_secondary: Optional[Color] = None,
            on_surface: Optional[Color] = None,
            on_background: Optional[Color] = None,
            on_error: Optional[Color] = None,
            brightness: Optional[Brightness] = None,
    ) -> 'ColorScheme':
        _o = ColorScheme(
            primary=Color(0),
            primary_variant=Color(0),
            secondary=Color(0),
            secondary_variant=Color(0),
            surface=Color(0),
            background=Color(0),
            error=Color(0),
            on_primary=Color(0),
            on_secondary=Color(0),
            on_surface=Color(0),
            on_background=Color(0),
            on_error=Color(0),
            brightness=Brightness.index,
        )
        _o.__ctor = (('highContrastLight',), (
            'primary', primary,
            'primaryVariant', primary_variant,
            'secondary', secondary,
            'secondaryVariant', secondary_variant,
            'surface', surface,
            'background', background,
            'error', error,
            'onPrimary', on_primary,
            'onSecondary', on_secondary,
            'onSurface', on_surface,
            'onBackground', on_background,
            'onError', on_error,
            'brightness', brightness,
        ))
        return _o

    @staticmethod
    def high_contrast_dark(
            primary: Optional[Color] = None,
            primary_variant: Optional[Color] = None,
            secondary: Optional[Color] = None,
            secondary_variant: Optional[Color] = None,
            surface: Optional[Color] = None,
            background: Optional[Color] = None,
            error: Optional[Color] = None,
            on_primary: Optional[Color] = None,
            on_secondary: Optional[Color] = None,
            on_surface: Optional[Color] = None,
            on_background: Optional[Color] = None,
            on_error: Optional[Color] = None,
            brightness: Optional[Brightness] = None,
    ) -> 'ColorScheme':
        _o = ColorScheme(
            primary=Color(0),
            primary_variant=Color(0),
            secondary=Color(0),
            secondary_variant=Color(0),
            surface=Color(0),
            background=Color(0),
            error=Color(0),
            on_primary=Color(0),
            on_secondary=Color(0),
            on_surface=Color(0),
            on_background=Color(0),
            on_error=Color(0),
            brightness=Brightness.index,
        )
        _o.__ctor = (('highContrastDark',), (
            'primary', primary,
            'primaryVariant', primary_variant,
            'secondary', secondary,
            'secondaryVariant', secondary_variant,
            'surface', surface,
            'background', background,
            'error', error,
            'onPrimary', on_primary,
            'onSecondary', on_secondary,
            'onSurface', on_surface,
            'onBackground', on_background,
            'onError', on_error,
            'brightness', brightness,
        ))
        return _o

    @staticmethod
    def from_swatch(
            primary_swatch: Optional[MaterialColor] = None,
            primary_color_dark: Optional[Color] = None,
            accent_color: Optional[Color] = None,
            card_color: Optional[Color] = None,
            background_color: Optional[Color] = None,
            error_color: Optional[Color] = None,
            brightness: Optional[Brightness] = None,
    ) -> 'ColorScheme':
        _o = ColorScheme(
            primary=Color(0),
            primary_variant=Color(0),
            secondary=Color(0),
            secondary_variant=Color(0),
            surface=Color(0),
            background=Color(0),
            error=Color(0),
            on_primary=Color(0),
            on_secondary=Color(0),
            on_surface=Color(0),
            on_background=Color(0),
            on_error=Color(0),
            brightness=Brightness.index,
        )
        _o.__ctor = (('fromSwatch',), (
            'primarySwatch', primary_swatch,
            'primaryColorDark', primary_color_dark,
            'accentColor', accent_color,
            'cardColor', card_color,
            'backgroundColor', background_color,
            'errorColor', error_color,
            'brightness', brightness,
        ))
        return _o


# packages/flutter/lib/src/material/theme_data.dart
class MaterialTapTargetSize(Enum):
    index = 'index'
    values = 'values'
    padded = 'padded'
    shrink_wrap = 'shrinkWrap'


# packages/flutter/lib/src/material/button_theme.dart
class ButtonThemeData:
    def __init__(
            self,
            text_theme: Optional[ButtonTextTheme] = None,
            min_width: Optional[float] = None,
            height: Optional[float] = None,
            padding: Optional[EdgeInsetsGeometry] = None,
            shape: Optional[ShapeBorder] = None,
            layout_behavior: Optional[ButtonBarLayoutBehavior] = None,
            aligned_dropdown: Optional[bool] = None,
            button_color: Optional[Color] = None,
            disabled_color: Optional[Color] = None,
            focus_color: Optional[Color] = None,
            hover_color: Optional[Color] = None,
            highlight_color: Optional[Color] = None,
            splash_color: Optional[Color] = None,
            color_scheme: Optional[ColorScheme] = None,
            material_tap_target_size: Optional[MaterialTapTargetSize] = None,
    ):
        self.__ctor = (('',), (
            'textTheme', text_theme,
            'minWidth', min_width,
            'height', height,
            'padding', padding,
            'shape', shape,
            'layoutBehavior', layout_behavior,
            'alignedDropdown', aligned_dropdown,
            'buttonColor', button_color,
            'disabledColor', disabled_color,
            'focusColor', focus_color,
            'hoverColor', hover_color,
            'highlightColor', highlight_color,
            'splashColor', splash_color,
            'colorScheme', color_scheme,
            'materialTapTargetSize', material_tap_target_size,
        ))


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontWeight:
    pass


FontWeight.w100 = FontWeight(
)
FontWeight.w100.__ctor = ('w100', )
FontWeight.w200 = FontWeight(
)
FontWeight.w200.__ctor = ('w200', )
FontWeight.w300 = FontWeight(
)
FontWeight.w300.__ctor = ('w300', )
FontWeight.w400 = FontWeight(
)
FontWeight.w400.__ctor = ('w400', )
FontWeight.w500 = FontWeight(
)
FontWeight.w500.__ctor = ('w500', )
FontWeight.w600 = FontWeight(
)
FontWeight.w600.__ctor = ('w600', )
FontWeight.w700 = FontWeight(
)
FontWeight.w700.__ctor = ('w700', )
FontWeight.w800 = FontWeight(
)
FontWeight.w800.__ctor = ('w800', )
FontWeight.w900 = FontWeight(
)
FontWeight.w900.__ctor = ('w900', )
FontWeight.normal = FontWeight(
)
FontWeight.normal.__ctor = ('normal', )
FontWeight.bold = FontWeight(
)
FontWeight.bold.__ctor = ('bold', )


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontStyle(Enum):
    index = 'index'
    values = 'values'
    normal = 'normal'
    italic = 'italic'


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextBaseline(Enum):
    index = 'index'
    values = 'values'
    alphabetic = 'alphabetic'
    ideographic = 'ideographic'


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextLeadingDistribution(Enum):
    index = 'index'
    values = 'values'
    proportional = 'proportional'
    even = 'even'


# bin/cache/pkg/sky_engine/lib/ui/platform_dispatcher.dart
class Locale:
    def __init__(
            self,
            _language_code: str,
            _country_code: Optional[str] = None,
    ):
        self.__ctor = (('',), (
            '_languageCode', _language_code,
            '_countryCode', _country_code,
        ))

    @staticmethod
    def from_subtags(
            language_code: Optional[str] = None,
            script_code: Optional[str] = None,
            country_code: Optional[str] = None,
    ) -> 'Locale':
        _o = Locale(
            _language_code='',
        )
        _o.__ctor = (('fromSubtags',), (
            'languageCode', language_code,
            'scriptCode', script_code,
            'countryCode', country_code,
        ))
        return _o


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Paint:
    pass


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class Offset:
    def __init__(
            self,
            dx: float,
            dy: float,
    ):
        self.__ctor = (('',), (
            'dx', dx,
            'dy', dy,
        ))

    @staticmethod
    def from_direction(
            direction: float,
            distance: Optional[float] = None,
    ) -> 'Offset':
        _o = Offset(
            dx=0.0,
            dy=0.0,
        )
        _o.__ctor = (('fromDirection',), (
            'direction', direction,
            'distance', distance,
        ))
        return _o


Offset.zero = Offset(
    dx=0.0,
    dy=0.0,
)
Offset.zero.__ctor = ('zero', )
Offset.infinite = Offset(
    dx=0.0,
    dy=0.0,
)
Offset.infinite.__ctor = ('infinite', )


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Shadow:
    def __init__(
            self,
            color: Optional[Color] = None,
            offset: Optional[Offset] = None,
            blur_radius: Optional[float] = None,
    ):
        self.__ctor = (('',), (
            'color', color,
            'offset', offset,
            'blurRadius', blur_radius,
        ))


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeature:
    def __init__(
            self,
            feature: str,
            value: Optional[int] = None,
    ):
        self.__ctor = (('',), (
            'feature', feature,
            'value', value,
        ))

    @staticmethod
    def enable(
            feature: str,
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('enable',), (
            'feature', feature,
        ))
        return _o

    @staticmethod
    def disable(
            feature: str,
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('disable',), (
            'feature', feature,
        ))
        return _o

    @staticmethod
    def alternative(
            value: int,
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('alternative',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def alternative_fractions(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('alternativeFractions',), (
        ))
        return _o

    @staticmethod
    def contextual_alternates(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('contextualAlternates',), (
        ))
        return _o

    @staticmethod
    def case_sensitive_forms(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('caseSensitiveForms',), (
        ))
        return _o

    @staticmethod
    def character_variant(
            value: int,
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('characterVariant',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def denominator(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('denominator',), (
        ))
        return _o

    @staticmethod
    def fractions(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('fractions',), (
        ))
        return _o

    @staticmethod
    def historical_forms(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('historicalForms',), (
        ))
        return _o

    @staticmethod
    def historical_ligatures(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('historicalLigatures',), (
        ))
        return _o

    @staticmethod
    def lining_figures(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('liningFigures',), (
        ))
        return _o

    @staticmethod
    def locale_aware(
            enable: Optional[bool] = None,
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('localeAware',), (
            'enable', enable,
        ))
        return _o

    @staticmethod
    def notational_forms(
            value: Optional[int] = None,
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('notationalForms',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def numerators(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('numerators',), (
        ))
        return _o

    @staticmethod
    def oldstyle_figures(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('oldstyleFigures',), (
        ))
        return _o

    @staticmethod
    def ordinal_forms(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('ordinalForms',), (
        ))
        return _o

    @staticmethod
    def proportional_figures(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('proportionalFigures',), (
        ))
        return _o

    @staticmethod
    def randomize(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('randomize',), (
        ))
        return _o

    @staticmethod
    def stylistic_alternates(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('stylisticAlternates',), (
        ))
        return _o

    @staticmethod
    def scientific_inferiors(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('scientificInferiors',), (
        ))
        return _o

    @staticmethod
    def stylistic_set(
            value: int,
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('stylisticSet',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def subscripts(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('subscripts',), (
        ))
        return _o

    @staticmethod
    def superscripts(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('superscripts',), (
        ))
        return _o

    @staticmethod
    def swash(
            value: Optional[int] = None,
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('swash',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def tabular_figures(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('tabularFigures',), (
        ))
        return _o

    @staticmethod
    def slashed_zero(
    ) -> 'FontFeature':
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('slashedZero',), (
        ))
        return _o


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextDecoration:

    @staticmethod
    def combine(
            decorations: List['TextDecoration'],
    ) -> 'TextDecoration':
        _o = TextDecoration(
        )
        _o.__ctor = (('combine',), (
            'decorations', decorations,
        ))
        return _o


TextDecoration.none = TextDecoration(
)
TextDecoration.none.__ctor = ('none', )
TextDecoration.underline = TextDecoration(
)
TextDecoration.underline.__ctor = ('underline', )
TextDecoration.overline = TextDecoration(
)
TextDecoration.overline.__ctor = ('overline', )
TextDecoration.line_through = TextDecoration(
)
TextDecoration.line_through.__ctor = ('line_through', )


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextDecorationStyle(Enum):
    index = 'index'
    values = 'values'
    solid = 'solid'
    double = 'double'
    dotted = 'dotted'
    dashed = 'dashed'
    wavy = 'wavy'


# packages/flutter/lib/src/painting/text_painter.dart
class TextOverflow(Enum):
    index = 'index'
    values = 'values'
    clip = 'clip'
    fade = 'fade'
    ellipsis = 'ellipsis'
    visible = 'visible'


# packages/flutter/lib/src/painting/text_style.dart
class TextStyle:
    def __init__(
            self,
            inherit: Optional[bool] = None,
            color: Optional[Color] = None,
            background_color: Optional[Color] = None,
            font_size: Optional[float] = None,
            font_weight: Optional[FontWeight] = None,
            font_style: Optional[FontStyle] = None,
            letter_spacing: Optional[float] = None,
            word_spacing: Optional[float] = None,
            text_baseline: Optional[TextBaseline] = None,
            height: Optional[float] = None,
            leading_distribution: Optional[TextLeadingDistribution] = None,
            locale: Optional[Locale] = None,
            foreground: Optional[Paint] = None,
            background: Optional[Paint] = None,
            shadows: Optional[List[Shadow]] = None,
            font_features: Optional[List[FontFeature]] = None,
            decoration: Optional[TextDecoration] = None,
            decoration_color: Optional[Color] = None,
            decoration_style: Optional[TextDecorationStyle] = None,
            decoration_thickness: Optional[float] = None,
            debug_label: Optional[str] = None,
            font_family: Optional[str] = None,
            font_family_fallback: Optional[List[str]] = None,
            package: Optional[str] = None,
            overflow: Optional[TextOverflow] = None,
    ):
        self.__ctor = (('',), (
            'inherit', inherit,
            'color', color,
            'backgroundColor', background_color,
            'fontSize', font_size,
            'fontWeight', font_weight,
            'fontStyle', font_style,
            'letterSpacing', letter_spacing,
            'wordSpacing', word_spacing,
            'textBaseline', text_baseline,
            'height', height,
            'leadingDistribution', leading_distribution,
            'locale', locale,
            'foreground', foreground,
            'background', background,
            'shadows', shadows,
            'fontFeatures', font_features,
            'decoration', decoration,
            'decorationColor', decoration_color,
            'decorationStyle', decoration_style,
            'decorationThickness', decoration_thickness,
            'debugLabel', debug_label,
            'fontFamily', font_family,
            'fontFamilyFallback', font_family_fallback,
            'package', package,
            'overflow', overflow,
        ))


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class Size:
    def __init__(
            self,
            width: float,
            height: float,
    ):
        self.__ctor = (('',), (
            'width', width,
            'height', height,
        ))

    @staticmethod
    def copy(
            source: 'Size',
    ) -> 'Size':
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o.__ctor = (('copy',), (
            'source', source,
        ))
        return _o

    @staticmethod
    def square(
            dimension: float,
    ) -> 'Size':
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o.__ctor = (('square',), (
            'dimension', dimension,
        ))
        return _o

    @staticmethod
    def from_width(
            width: float,
    ) -> 'Size':
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o.__ctor = (('fromWidth',), (
            'width', width,
        ))
        return _o

    @staticmethod
    def from_height(
            height: float,
    ) -> 'Size':
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o.__ctor = (('fromHeight',), (
            'height', height,
        ))
        return _o

    @staticmethod
    def from_radius(
            radius: float,
    ) -> 'Size':
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o.__ctor = (('fromRadius',), (
            'radius', radius,
        ))
        return _o


Size.zero = Size(
    width=0.0,
    height=0.0,
)
Size.zero.__ctor = ('zero', )
Size.infinite = Size(
    width=0.0,
    height=0.0,
)
Size.infinite.__ctor = ('infinite', )


# packages/flutter/lib/src/rendering/box.dart
class BoxConstraints:
    def __init__(
            self,
            min_width: Optional[float] = None,
            max_width: Optional[float] = None,
            min_height: Optional[float] = None,
            max_height: Optional[float] = None,
    ):
        self.__ctor = (('',), (
            'minWidth', min_width,
            'maxWidth', max_width,
            'minHeight', min_height,
            'maxHeight', max_height,
        ))

    @staticmethod
    def tight(
            size: Size,
    ) -> 'BoxConstraints':
        _o = BoxConstraints(
        )
        _o.__ctor = (('tight',), (
            'size', size,
        ))
        return _o

    @staticmethod
    def tight_for(
            width: Optional[float] = None,
            height: Optional[float] = None,
    ) -> 'BoxConstraints':
        _o = BoxConstraints(
        )
        _o.__ctor = (('tightFor',), (
            'width', width,
            'height', height,
        ))
        return _o

    @staticmethod
    def tight_for_finite(
            width: Optional[float] = None,
            height: Optional[float] = None,
    ) -> 'BoxConstraints':
        _o = BoxConstraints(
        )
        _o.__ctor = (('tightForFinite',), (
            'width', width,
            'height', height,
        ))
        return _o

    @staticmethod
    def loose(
            size: Size,
    ) -> 'BoxConstraints':
        _o = BoxConstraints(
        )
        _o.__ctor = (('loose',), (
            'size', size,
        ))
        return _o

    @staticmethod
    def expand(
            width: Optional[float] = None,
            height: Optional[float] = None,
    ) -> 'BoxConstraints':
        _o = BoxConstraints(
        )
        _o.__ctor = (('expand',), (
            'width', width,
            'height', height,
        ))
        return _o


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class Radius:

    @staticmethod
    def circular(
            radius: float,
    ) -> 'Radius':
        _o = Radius(
        )
        _o.__ctor = (('circular',), (
            'radius', radius,
        ))
        return _o

    @staticmethod
    def elliptical(
            x: float,
            y: float,
    ) -> 'Radius':
        _o = Radius(
        )
        _o.__ctor = (('elliptical',), (
            'x', x,
            'y', y,
        ))
        return _o


Radius.zero = Radius(
)
Radius.zero.__ctor = ('zero', )


# packages/flutter/lib/src/painting/border_radius.dart
class BorderRadius:

    @staticmethod
    def all(
            radius: Radius,
    ) -> 'BorderRadius':
        _o = BorderRadius(
        )
        _o.__ctor = (('all',), (
            'radius', radius,
        ))
        return _o

    @staticmethod
    def circular(
            radius: float,
    ) -> 'BorderRadius':
        _o = BorderRadius(
        )
        _o.__ctor = (('circular',), (
            'radius', radius,
        ))
        return _o

    @staticmethod
    def vertical(
            top: Optional[Radius] = None,
            bottom: Optional[Radius] = None,
    ) -> 'BorderRadius':
        _o = BorderRadius(
        )
        _o.__ctor = (('vertical',), (
            'top', top,
            'bottom', bottom,
        ))
        return _o

    @staticmethod
    def horizontal(
            left: Optional[Radius] = None,
            right: Optional[Radius] = None,
    ) -> 'BorderRadius':
        _o = BorderRadius(
        )
        _o.__ctor = (('horizontal',), (
            'left', left,
            'right', right,
        ))
        return _o

    @staticmethod
    def only(
            top_left: Optional[Radius] = None,
            top_right: Optional[Radius] = None,
            bottom_left: Optional[Radius] = None,
            bottom_right: Optional[Radius] = None,
    ) -> 'BorderRadius':
        _o = BorderRadius(
        )
        _o.__ctor = (('only',), (
            'topLeft', top_left,
            'topRight', top_right,
            'bottomLeft', bottom_left,
            'bottomRight', bottom_right,
        ))
        return _o


BorderRadius.zero = BorderRadius(
)
BorderRadius.zero.__ctor = ('zero', )


# packages/flutter/lib/src/material/toggle_buttons_theme.dart
class ToggleButtonsThemeData:
    def __init__(
            self,
            text_style: Optional[TextStyle] = None,
            constraints: Optional[BoxConstraints] = None,
            color: Optional[Color] = None,
            selected_color: Optional[Color] = None,
            disabled_color: Optional[Color] = None,
            fill_color: Optional[Color] = None,
            focus_color: Optional[Color] = None,
            highlight_color: Optional[Color] = None,
            hover_color: Optional[Color] = None,
            splash_color: Optional[Color] = None,
            border_color: Optional[Color] = None,
            selected_border_color: Optional[Color] = None,
            disabled_border_color: Optional[Color] = None,
            border_radius: Optional[BorderRadius] = None,
            border_width: Optional[float] = None,
    ):
        self.__ctor = (('',), (
            'textStyle', text_style,
            'constraints', constraints,
            'color', color,
            'selectedColor', selected_color,
            'disabledColor', disabled_color,
            'fillColor', fill_color,
            'focusColor', focus_color,
            'highlightColor', highlight_color,
            'hoverColor', hover_color,
            'splashColor', splash_color,
            'borderColor', border_color,
            'selectedBorderColor', selected_border_color,
            'disabledBorderColor', disabled_border_color,
            'borderRadius', border_radius,
            'borderWidth', border_width,
        ))


# packages/flutter/lib/src/material/text_theme.dart
class TextTheme:
    def __init__(
            self,
            headline1: Optional[TextStyle] = None,
            headline2: Optional[TextStyle] = None,
            headline3: Optional[TextStyle] = None,
            headline4: Optional[TextStyle] = None,
            headline5: Optional[TextStyle] = None,
            headline6: Optional[TextStyle] = None,
            subtitle1: Optional[TextStyle] = None,
            subtitle2: Optional[TextStyle] = None,
            body_text1: Optional[TextStyle] = None,
            body_text2: Optional[TextStyle] = None,
            caption: Optional[TextStyle] = None,
            button: Optional[TextStyle] = None,
            overline: Optional[TextStyle] = None,
    ):
        self.__ctor = (('',), (
            'headline1', headline1,
            'headline2', headline2,
            'headline3', headline3,
            'headline4', headline4,
            'headline5', headline5,
            'headline6', headline6,
            'subtitle1', subtitle1,
            'subtitle2', subtitle2,
            'bodyText1', body_text1,
            'bodyText2', body_text2,
            'caption', caption,
            'button', button,
            'overline', overline,
        ))


# packages/flutter/lib/src/material/input_decorator.dart
class FloatingLabelBehavior(Enum):
    index = 'index'
    values = 'values'
    never = 'never'
    auto = 'auto'
    always = 'always'


# packages/flutter/lib/src/painting/borders.dart
class BorderStyle(Enum):
    index = 'index'
    values = 'values'
    none = 'none'
    solid = 'solid'


# packages/flutter/lib/src/painting/borders.dart
class BorderSide:
    def __init__(
            self,
            color: Optional[Color] = None,
            width: Optional[float] = None,
            style: Optional[BorderStyle] = None,
    ):
        self.__ctor = (('',), (
            'color', color,
            'width', width,
            'style', style,
        ))


BorderSide.none = BorderSide(
)
BorderSide.none.__ctor = ('none', )


# packages/flutter/lib/src/material/input_border.dart
class InputBorder:
    def __init__(
            self,
            border_side: Optional[BorderSide] = None,
    ):
        self.__ctor = (('',), (
            'borderSide', border_side,
        ))


InputBorder.none = InputBorder(
)
InputBorder.none.__ctor = ('none', )


# packages/flutter/lib/src/material/input_decorator.dart
class InputDecorationTheme:
    def __init__(
            self,
            label_style: Optional[TextStyle] = None,
            floating_label_style: Optional[TextStyle] = None,
            helper_style: Optional[TextStyle] = None,
            helper_max_lines: Optional[int] = None,
            hint_style: Optional[TextStyle] = None,
            error_style: Optional[TextStyle] = None,
            error_max_lines: Optional[int] = None,
            floating_label_behavior: Optional[FloatingLabelBehavior] = None,
            is_dense: Optional[bool] = None,
            content_padding: Optional[EdgeInsetsGeometry] = None,
            is_collapsed: Optional[bool] = None,
            prefix_style: Optional[TextStyle] = None,
            suffix_style: Optional[TextStyle] = None,
            counter_style: Optional[TextStyle] = None,
            filled: Optional[bool] = None,
            fill_color: Optional[Color] = None,
            focus_color: Optional[Color] = None,
            hover_color: Optional[Color] = None,
            error_border: Optional[InputBorder] = None,
            focused_border: Optional[InputBorder] = None,
            focused_error_border: Optional[InputBorder] = None,
            disabled_border: Optional[InputBorder] = None,
            enabled_border: Optional[InputBorder] = None,
            border: Optional[InputBorder] = None,
            align_label_with_hint: Optional[bool] = None,
            constraints: Optional[BoxConstraints] = None,
    ):
        self.__ctor = (('',), (
            'labelStyle', label_style,
            'floatingLabelStyle', floating_label_style,
            'helperStyle', helper_style,
            'helperMaxLines', helper_max_lines,
            'hintStyle', hint_style,
            'errorStyle', error_style,
            'errorMaxLines', error_max_lines,
            'floatingLabelBehavior', floating_label_behavior,
            'isDense', is_dense,
            'contentPadding', content_padding,
            'isCollapsed', is_collapsed,
            'prefixStyle', prefix_style,
            'suffixStyle', suffix_style,
            'counterStyle', counter_style,
            'filled', filled,
            'fillColor', fill_color,
            'focusColor', focus_color,
            'hoverColor', hover_color,
            'errorBorder', error_border,
            'focusedBorder', focused_border,
            'focusedErrorBorder', focused_error_border,
            'disabledBorder', disabled_border,
            'enabledBorder', enabled_border,
            'border', border,
            'alignLabelWithHint', align_label_with_hint,
            'constraints', constraints,
        ))


# packages/flutter/lib/src/widgets/icon_theme_data.dart
class IconThemeData:
    def __init__(
            self,
            color: Optional[Color] = None,
            opacity: Optional[float] = None,
            size: Optional[float] = None,
    ):
        self.__ctor = (('',), (
            'color', color,
            'opacity', opacity,
            'size', size,
        ))

    @staticmethod
    def fallback(
    ) -> 'IconThemeData':
        _o = IconThemeData(
        )
        _o.__ctor = (('fallback',), (
        ))
        return _o


# packages/flutter/lib/src/material/slider_theme.dart
class SliderComponentShape:
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class SliderTickMarkShape:
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class SliderTrackShape:
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderTickMarkShape:
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderThumbShape:
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderTrackShape:
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderValueIndicatorShape:
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class ShowValueIndicator(Enum):
    index = 'index'
    values = 'values'
    only_for_discrete = 'onlyForDiscrete'
    only_for_continuous = 'onlyForContinuous'
    always = 'always'
    never = 'never'


# packages/flutter/lib/src/material/slider_theme.dart
class SliderThemeData:
    def __init__(
            self,
            track_height: Optional[float] = None,
            active_track_color: Optional[Color] = None,
            inactive_track_color: Optional[Color] = None,
            disabled_active_track_color: Optional[Color] = None,
            disabled_inactive_track_color: Optional[Color] = None,
            active_tick_mark_color: Optional[Color] = None,
            inactive_tick_mark_color: Optional[Color] = None,
            disabled_active_tick_mark_color: Optional[Color] = None,
            disabled_inactive_tick_mark_color: Optional[Color] = None,
            thumb_color: Optional[Color] = None,
            overlapping_shape_stroke_color: Optional[Color] = None,
            disabled_thumb_color: Optional[Color] = None,
            overlay_color: Optional[Color] = None,
            value_indicator_color: Optional[Color] = None,
            overlay_shape: Optional[SliderComponentShape] = None,
            tick_mark_shape: Optional[SliderTickMarkShape] = None,
            thumb_shape: Optional[SliderComponentShape] = None,
            track_shape: Optional[SliderTrackShape] = None,
            value_indicator_shape: Optional[SliderComponentShape] = None,
            range_tick_mark_shape: Optional[RangeSliderTickMarkShape] = None,
            range_thumb_shape: Optional[RangeSliderThumbShape] = None,
            range_track_shape: Optional[RangeSliderTrackShape] = None,
            range_value_indicator_shape: Optional[RangeSliderValueIndicatorShape] = None,
            show_value_indicator: Optional[ShowValueIndicator] = None,
            value_indicator_text_style: Optional[TextStyle] = None,
            min_thumb_separation: Optional[float] = None,
            thumb_selector: Optional[Callable] = None,
    ):
        self.__ctor = (('',), (
            'trackHeight', track_height,
            'activeTrackColor', active_track_color,
            'inactiveTrackColor', inactive_track_color,
            'disabledActiveTrackColor', disabled_active_track_color,
            'disabledInactiveTrackColor', disabled_inactive_track_color,
            'activeTickMarkColor', active_tick_mark_color,
            'inactiveTickMarkColor', inactive_tick_mark_color,
            'disabledActiveTickMarkColor', disabled_active_tick_mark_color,
            'disabledInactiveTickMarkColor', disabled_inactive_tick_mark_color,
            'thumbColor', thumb_color,
            'overlappingShapeStrokeColor', overlapping_shape_stroke_color,
            'disabledThumbColor', disabled_thumb_color,
            'overlayColor', overlay_color,
            'valueIndicatorColor', value_indicator_color,
            'overlayShape', overlay_shape,
            'tickMarkShape', tick_mark_shape,
            'thumbShape', thumb_shape,
            'trackShape', track_shape,
            'valueIndicatorShape', value_indicator_shape,
            'rangeTickMarkShape', range_tick_mark_shape,
            'rangeThumbShape', range_thumb_shape,
            'rangeTrackShape', range_track_shape,
            'rangeValueIndicatorShape', range_value_indicator_shape,
            'showValueIndicator', show_value_indicator,
            'valueIndicatorTextStyle', value_indicator_text_style,
            'minThumbSeparation', min_thumb_separation,
            'thumbSelector', thumb_selector,
        ))

    @staticmethod
    def from_primary_colors(
            primary_color: Color,
            primary_color_dark: Color,
            primary_color_light: Color,
            value_indicator_text_style: TextStyle,
    ) -> 'SliderThemeData':
        _o = SliderThemeData(
        )
        _o.__ctor = (('fromPrimaryColors',), (
            'primaryColor', primary_color,
            'primaryColorDark', primary_color_dark,
            'primaryColorLight', primary_color_light,
            'valueIndicatorTextStyle', value_indicator_text_style,
        ))
        return _o


# packages/flutter/lib/src/painting/decoration.dart
class Decoration:
    pass


# packages/flutter/lib/src/material/tabs.dart
class TabBarIndicatorSize(Enum):
    index = 'index'
    values = 'values'
    tab = 'tab'
    label = 'label'


# packages/flutter/lib/src/material/tab_bar_theme.dart
class TabBarTheme:
    def __init__(
            self,
            indicator: Optional[Decoration] = None,
            indicator_size: Optional[TabBarIndicatorSize] = None,
            label_color: Optional[Color] = None,
            label_padding: Optional[EdgeInsetsGeometry] = None,
            label_style: Optional[TextStyle] = None,
            unselected_label_color: Optional[Color] = None,
            unselected_label_style: Optional[TextStyle] = None,
    ):
        self.__ctor = (('',), (
            'indicator', indicator,
            'indicatorSize', indicator_size,
            'labelColor', label_color,
            'labelPadding', label_padding,
            'labelStyle', label_style,
            'unselectedLabelColor', unselected_label_color,
            'unselectedLabelStyle', unselected_label_style,
        ))


# bin/cache/pkg/sky_engine/lib/core/duration.dart
class Duration:
    microseconds_per_millisecond: int = 1000
    milliseconds_per_second: int = 1000
    seconds_per_minute: int = 60
    minutes_per_hour: int = 60
    hours_per_day: int = 24
    microseconds_per_second: int = 1000000
    microseconds_per_minute: int = 60000000
    microseconds_per_hour: int = 3600000000
    microseconds_per_day: int = 86400000000
    milliseconds_per_minute: int = 60000
    milliseconds_per_hour: int = 3600000
    milliseconds_per_day: int = 86400000
    seconds_per_hour: int = 3600
    seconds_per_day: int = 86400
    minutes_per_day: int = 1440

    def __init__(
            self,
            days: Optional[int] = None,
            hours: Optional[int] = None,
            minutes: Optional[int] = None,
            seconds: Optional[int] = None,
            milliseconds: Optional[int] = None,
            microseconds: Optional[int] = None,
    ):
        self.__ctor = (('',), (
            'days', days,
            'hours', hours,
            'minutes', minutes,
            'seconds', seconds,
            'milliseconds', milliseconds,
            'microseconds', microseconds,
        ))


Duration.zero = Duration(
)
Duration.zero.__ctor = ('zero', )


# packages/flutter/lib/src/material/tooltip_theme.dart
class TooltipTriggerMode(Enum):
    index = 'index'
    values = 'values'
    manual = 'manual'
    long_press = 'longPress'
    tap = 'tap'


# packages/flutter/lib/src/material/tooltip_theme.dart
class TooltipThemeData:
    def __init__(
            self,
            height: Optional[float] = None,
            padding: Optional[EdgeInsetsGeometry] = None,
            margin: Optional[EdgeInsetsGeometry] = None,
            vertical_offset: Optional[float] = None,
            prefer_below: Optional[bool] = None,
            exclude_from_semantics: Optional[bool] = None,
            decoration: Optional[Decoration] = None,
            text_style: Optional[TextStyle] = None,
            wait_duration: Optional[Duration] = None,
            show_duration: Optional[Duration] = None,
            trigger_mode: Optional[TooltipTriggerMode] = None,
            enable_feedback: Optional[bool] = None,
    ):
        self.__ctor = (('',), (
            'height', height,
            'padding', padding,
            'margin', margin,
            'verticalOffset', vertical_offset,
            'preferBelow', prefer_below,
            'excludeFromSemantics', exclude_from_semantics,
            'decoration', decoration,
            'textStyle', text_style,
            'waitDuration', wait_duration,
            'showDuration', show_duration,
            'triggerMode', trigger_mode,
            'enableFeedback', enable_feedback,
        ))


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Clip(Enum):
    index = 'index'
    values = 'values'
    none = 'none'
    hard_edge = 'hardEdge'
    anti_alias = 'antiAlias'
    anti_alias_with_save_layer = 'antiAliasWithSaveLayer'


# packages/flutter/lib/src/material/card_theme.dart
class CardTheme:
    def __init__(
            self,
            clip_behavior: Optional[Clip] = None,
            color: Optional[Color] = None,
            shadow_color: Optional[Color] = None,
            elevation: Optional[float] = None,
            margin: Optional[EdgeInsetsGeometry] = None,
            shape: Optional[ShapeBorder] = None,
    ):
        self.__ctor = (('',), (
            'clipBehavior', clip_behavior,
            'color', color,
            'shadowColor', shadow_color,
            'elevation', elevation,
            'margin', margin,
            'shape', shape,
        ))


# packages/flutter/lib/src/painting/borders.dart
class OutlinedBorder:
    def __init__(
            self,
            side: Optional[BorderSide] = None,
    ):
        self.__ctor = (('',), (
            'side', side,
        ))


# packages/flutter/lib/src/material/chip_theme.dart
class ChipThemeData:
    def __init__(
            self,
            background_color: Color,
            disabled_color: Color,
            selected_color: Color,
            secondary_selected_color: Color,
            padding: EdgeInsetsGeometry,
            label_style: TextStyle,
            secondary_label_style: TextStyle,
            brightness: Brightness,
            delete_icon_color: Optional[Color] = None,
            shadow_color: Optional[Color] = None,
            selected_shadow_color: Optional[Color] = None,
            show_checkmark: Optional[bool] = None,
            checkmark_color: Optional[Color] = None,
            label_padding: Optional[EdgeInsetsGeometry] = None,
            side: Optional[BorderSide] = None,
            shape: Optional[OutlinedBorder] = None,
            elevation: Optional[float] = None,
            press_elevation: Optional[float] = None,
    ):
        self.__ctor = (('',), (
            'backgroundColor', background_color,
            'deleteIconColor', delete_icon_color,
            'disabledColor', disabled_color,
            'selectedColor', selected_color,
            'secondarySelectedColor', secondary_selected_color,
            'shadowColor', shadow_color,
            'selectedShadowColor', selected_shadow_color,
            'showCheckmark', show_checkmark,
            'checkmarkColor', checkmark_color,
            'labelPadding', label_padding,
            'padding', padding,
            'side', side,
            'shape', shape,
            'labelStyle', label_style,
            'secondaryLabelStyle', secondary_label_style,
            'brightness', brightness,
            'elevation', elevation,
            'pressElevation', press_elevation,
        ))

    @staticmethod
    def from_defaults(
            secondary_color: Color,
            label_style: TextStyle,
            brightness: Optional[Brightness] = None,
            primary_color: Optional[Color] = None,
    ) -> 'ChipThemeData':
        _o = ChipThemeData(
            background_color=Color(0),
            disabled_color=Color(0),
            selected_color=Color(0),
            secondary_selected_color=Color(0),
            padding=EdgeInsetsGeometry(),
            label_style=TextStyle(),
            secondary_label_style=TextStyle(),
            brightness=Brightness.index,
        )
        _o.__ctor = (('fromDefaults',), (
            'brightness', brightness,
            'primaryColor', primary_color,
            'secondaryColor', secondary_color,
            'labelStyle', label_style,
        ))
        return _o


# packages/flutter/lib/src/foundation/platform.dart
class TargetPlatform(Enum):
    index = 'index'
    values = 'values'
    android = 'android'
    fuchsia = 'fuchsia'
    i_os = 'iOS'
    linux = 'linux'
    mac_os = 'macOS'
    windows = 'windows'


# packages/flutter/lib/src/material/page_transitions_theme.dart
class PageTransitionsBuilder:
    pass


# packages/flutter/lib/src/material/page_transitions_theme.dart
class PageTransitionsTheme:
    def __init__(
            self,
            builders: Optional[Dict[TargetPlatform, PageTransitionsBuilder]] = None,
    ):
        self.__ctor = (('',), (
            'builders', builders,
        ))


# packages/flutter/lib/src/services/system_chrome.dart
class SystemUiOverlayStyle:
    def __init__(
            self,
            system_navigation_bar_color: Optional[Color] = None,
            system_navigation_bar_divider_color: Optional[Color] = None,
            system_navigation_bar_icon_brightness: Optional[Brightness] = None,
            system_navigation_bar_contrast_enforced: Optional[bool] = None,
            status_bar_color: Optional[Color] = None,
            status_bar_brightness: Optional[Brightness] = None,
            status_bar_icon_brightness: Optional[Brightness] = None,
            system_status_bar_contrast_enforced: Optional[bool] = None,
    ):
        self.__ctor = (('',), (
            'systemNavigationBarColor', system_navigation_bar_color,
            'systemNavigationBarDividerColor', system_navigation_bar_divider_color,
            'systemNavigationBarIconBrightness', system_navigation_bar_icon_brightness,
            'systemNavigationBarContrastEnforced', system_navigation_bar_contrast_enforced,
            'statusBarColor', status_bar_color,
            'statusBarBrightness', status_bar_brightness,
            'statusBarIconBrightness', status_bar_icon_brightness,
            'systemStatusBarContrastEnforced', system_status_bar_contrast_enforced,
        ))


SystemUiOverlayStyle.light = SystemUiOverlayStyle(
)
SystemUiOverlayStyle.light.__ctor = ('light', )
SystemUiOverlayStyle.dark = SystemUiOverlayStyle(
)
SystemUiOverlayStyle.dark.__ctor = ('dark', )


# packages/flutter/lib/src/material/app_bar_theme.dart
class AppBarTheme:
    def __init__(
            self,
            brightness: Optional[Brightness] = None,
            color: Optional[Color] = None,
            background_color: Optional[Color] = None,
            foreground_color: Optional[Color] = None,
            elevation: Optional[float] = None,
            shadow_color: Optional[Color] = None,
            shape: Optional[ShapeBorder] = None,
            icon_theme: Optional[IconThemeData] = None,
            actions_icon_theme: Optional[IconThemeData] = None,
            text_theme: Optional[TextTheme] = None,
            center_title: Optional[bool] = None,
            title_spacing: Optional[float] = None,
            toolbar_height: Optional[float] = None,
            toolbar_text_style: Optional[TextStyle] = None,
            title_text_style: Optional[TextStyle] = None,
            system_overlay_style: Optional[SystemUiOverlayStyle] = None,
            backwards_compatibility: Optional[bool] = None,
    ):
        self.__ctor = (('',), (
            'brightness', brightness,
            'color', color,
            'backgroundColor', background_color,
            'foregroundColor', foreground_color,
            'elevation', elevation,
            'shadowColor', shadow_color,
            'shape', shape,
            'iconTheme', icon_theme,
            'actionsIconTheme', actions_icon_theme,
            'textTheme', text_theme,
            'centerTitle', center_title,
            'titleSpacing', title_spacing,
            'toolbarHeight', toolbar_height,
            'toolbarTextStyle', toolbar_text_style,
            'titleTextStyle', title_text_style,
            'systemOverlayStyle', system_overlay_style,
            'backwardsCompatibility', backwards_compatibility,
        ))


# packages/flutter/lib/src/material/material_state.dart
class MaterialStateProperty(Generic[T]):
    pass


# packages/flutter/lib/src/material/scrollbar_theme.dart
class ScrollbarThemeData:
    def __init__(
            self,
            thickness: Optional[MaterialStateProperty[float]] = None,
            show_track_on_hover: Optional[bool] = None,
            is_always_shown: Optional[bool] = None,
            radius: Optional[Radius] = None,
            thumb_color: Optional[MaterialStateProperty[Color]] = None,
            track_color: Optional[MaterialStateProperty[Color]] = None,
            track_border_color: Optional[MaterialStateProperty[Color]] = None,
            cross_axis_margin: Optional[float] = None,
            main_axis_margin: Optional[float] = None,
            min_thumb_length: Optional[float] = None,
            interactive: Optional[bool] = None,
    ):
        self.__ctor = (('',), (
            'thickness', thickness,
            'showTrackOnHover', show_track_on_hover,
            'isAlwaysShown', is_always_shown,
            'radius', radius,
            'thumbColor', thumb_color,
            'trackColor', track_color,
            'trackBorderColor', track_border_color,
            'crossAxisMargin', cross_axis_margin,
            'mainAxisMargin', main_axis_margin,
            'minThumbLength', min_thumb_length,
            'interactive', interactive,
        ))


# packages/flutter/lib/src/painting/notched_shapes.dart
class NotchedShape:
    pass


# packages/flutter/lib/src/material/bottom_app_bar_theme.dart
class BottomAppBarTheme:
    def __init__(
            self,
            color: Optional[Color] = None,
            elevation: Optional[float] = None,
            shape: Optional[NotchedShape] = None,
    ):
        self.__ctor = (('',), (
            'color', color,
            'elevation', elevation,
            'shape', shape,
        ))


# packages/flutter/lib/src/material/dialog_theme.dart
class DialogTheme:
    def __init__(
            self,
            background_color: Optional[Color] = None,
            elevation: Optional[float] = None,
            shape: Optional[ShapeBorder] = None,
            title_text_style: Optional[TextStyle] = None,
            content_text_style: Optional[TextStyle] = None,
    ):
        self.__ctor = (('',), (
            'backgroundColor', background_color,
            'elevation', elevation,
            'shape', shape,
            'titleTextStyle', title_text_style,
            'contentTextStyle', content_text_style,
        ))


# packages/flutter/lib/src/material/floating_action_button_theme.dart
class FloatingActionButtonThemeData:
    def __init__(
            self,
            foreground_color: Optional[Color] = None,
            background_color: Optional[Color] = None,
            focus_color: Optional[Color] = None,
            hover_color: Optional[Color] = None,
            splash_color: Optional[Color] = None,
            elevation: Optional[float] = None,
            focus_elevation: Optional[float] = None,
            hover_elevation: Optional[float] = None,
            disabled_elevation: Optional[float] = None,
            highlight_elevation: Optional[float] = None,
            shape: Optional[ShapeBorder] = None,
            enable_feedback: Optional[bool] = None,
            size_constraints: Optional[BoxConstraints] = None,
            small_size_constraints: Optional[BoxConstraints] = None,
            large_size_constraints: Optional[BoxConstraints] = None,
            extended_size_constraints: Optional[BoxConstraints] = None,
            extended_icon_label_spacing: Optional[float] = None,
            extended_padding: Optional[EdgeInsetsGeometry] = None,
            extended_text_style: Optional[TextStyle] = None,
    ):
        self.__ctor = (('',), (
            'foregroundColor', foreground_color,
            'backgroundColor', background_color,
            'focusColor', focus_color,
            'hoverColor', hover_color,
            'splashColor', splash_color,
            'elevation', elevation,
            'focusElevation', focus_elevation,
            'hoverElevation', hover_elevation,
            'disabledElevation', disabled_elevation,
            'highlightElevation', highlight_elevation,
            'shape', shape,
            'enableFeedback', enable_feedback,
            'sizeConstraints', size_constraints,
            'smallSizeConstraints', small_size_constraints,
            'largeSizeConstraints', large_size_constraints,
            'extendedSizeConstraints', extended_size_constraints,
            'extendedIconLabelSpacing', extended_icon_label_spacing,
            'extendedPadding', extended_padding,
            'extendedTextStyle', extended_text_style,
        ))


# packages/flutter/lib/src/material/navigation_rail.dart
class NavigationRailLabelType(Enum):
    index = 'index'
    values = 'values'
    none = 'none'
    selected = 'selected'
    all = 'all'


# packages/flutter/lib/src/material/navigation_rail_theme.dart
class NavigationRailThemeData:
    def __init__(
            self,
            background_color: Optional[Color] = None,
            elevation: Optional[float] = None,
            unselected_label_text_style: Optional[TextStyle] = None,
            selected_label_text_style: Optional[TextStyle] = None,
            unselected_icon_theme: Optional[IconThemeData] = None,
            selected_icon_theme: Optional[IconThemeData] = None,
            group_alignment: Optional[float] = None,
            label_type: Optional[NavigationRailLabelType] = None,
    ):
        self.__ctor = (('',), (
            'backgroundColor', background_color,
            'elevation', elevation,
            'unselectedLabelTextStyle', unselected_label_text_style,
            'selectedLabelTextStyle', selected_label_text_style,
            'unselectedIconTheme', unselected_icon_theme,
            'selectedIconTheme', selected_icon_theme,
            'groupAlignment', group_alignment,
            'labelType', label_type,
        ))


def _typography__text_theme(_k: str) -> TextTheme:
    _o = TextTheme(
    )
    _o.__ctor = (('Typography', _k),)
    return _o


# packages/flutter/lib/src/material/typography.dart
class Typography:
    black_mountain_view: TextTheme = _typography__text_theme('blackMountainView')
    white_mountain_view: TextTheme = _typography__text_theme('whiteMountainView')
    black_redmond: TextTheme = _typography__text_theme('blackRedmond')
    white_redmond: TextTheme = _typography__text_theme('whiteRedmond')
    black_helsinki: TextTheme = _typography__text_theme('blackHelsinki')
    white_helsinki: TextTheme = _typography__text_theme('whiteHelsinki')
    black_cupertino: TextTheme = _typography__text_theme('blackCupertino')
    white_cupertino: TextTheme = _typography__text_theme('whiteCupertino')
    black_redwood_city: TextTheme = _typography__text_theme('blackRedwoodCity')
    white_redwood_city: TextTheme = _typography__text_theme('whiteRedwoodCity')
    english_like2014: TextTheme = _typography__text_theme('englishLike2014')
    english_like2018: TextTheme = _typography__text_theme('englishLike2018')
    dense2014: TextTheme = _typography__text_theme('dense2014')
    dense2018: TextTheme = _typography__text_theme('dense2018')
    tall2014: TextTheme = _typography__text_theme('tall2014')
    tall2018: TextTheme = _typography__text_theme('tall2018')

    def __init__(
            self,
            platform: Optional[TargetPlatform] = None,
            black: Optional[TextTheme] = None,
            white: Optional[TextTheme] = None,
            english_like: Optional[TextTheme] = None,
            dense: Optional[TextTheme] = None,
            tall: Optional[TextTheme] = None,
    ):
        self.__ctor = (('',), (
            'platform', platform,
            'black', black,
            'white', white,
            'englishLike', english_like,
            'dense', dense,
            'tall', tall,
        ))

    @staticmethod
    def material2014(
            platform: Optional[TargetPlatform] = None,
            black: Optional[TextTheme] = None,
            white: Optional[TextTheme] = None,
            english_like: Optional[TextTheme] = None,
            dense: Optional[TextTheme] = None,
            tall: Optional[TextTheme] = None,
    ) -> 'Typography':
        _o = Typography(
        )
        _o.__ctor = (('material2014',), (
            'platform', platform,
            'black', black,
            'white', white,
            'englishLike', english_like,
            'dense', dense,
            'tall', tall,
        ))
        return _o

    @staticmethod
    def material2018(
            platform: Optional[TargetPlatform] = None,
            black: Optional[TextTheme] = None,
            white: Optional[TextTheme] = None,
            english_like: Optional[TextTheme] = None,
            dense: Optional[TextTheme] = None,
            tall: Optional[TextTheme] = None,
    ) -> 'Typography':
        _o = Typography(
        )
        _o.__ctor = (('material2018',), (
            'platform', platform,
            'black', black,
            'white', white,
            'englishLike', english_like,
            'dense', dense,
            'tall', tall,
        ))
        return _o


# packages/flutter/lib/src/cupertino/text_theme.dart
class CupertinoTextThemeData:
    def __init__(
            self,
            primary_color: Optional[Color] = None,
            text_style: Optional[TextStyle] = None,
            action_text_style: Optional[TextStyle] = None,
            tab_label_text_style: Optional[TextStyle] = None,
            nav_title_text_style: Optional[TextStyle] = None,
            nav_large_title_text_style: Optional[TextStyle] = None,
            nav_action_text_style: Optional[TextStyle] = None,
            picker_text_style: Optional[TextStyle] = None,
            date_time_picker_text_style: Optional[TextStyle] = None,
    ):
        self.__ctor = (('',), (
            'primaryColor', primary_color,
            'textStyle', text_style,
            'actionTextStyle', action_text_style,
            'tabLabelTextStyle', tab_label_text_style,
            'navTitleTextStyle', nav_title_text_style,
            'navLargeTitleTextStyle', nav_large_title_text_style,
            'navActionTextStyle', nav_action_text_style,
            'pickerTextStyle', picker_text_style,
            'dateTimePickerTextStyle', date_time_picker_text_style,
        ))


# packages/flutter/lib/src/cupertino/theme.dart
class NoDefaultCupertinoThemeData:
    def __init__(
            self,
            brightness: Optional[Brightness] = None,
            primary_color: Optional[Color] = None,
            primary_contrasting_color: Optional[Color] = None,
            text_theme: Optional[CupertinoTextThemeData] = None,
            bar_background_color: Optional[Color] = None,
            scaffold_background_color: Optional[Color] = None,
    ):
        self.__ctor = (('',), (
            'brightness', brightness,
            'primaryColor', primary_color,
            'primaryContrastingColor', primary_contrasting_color,
            'textTheme', text_theme,
            'barBackgroundColor', bar_background_color,
            'scaffoldBackgroundColor', scaffold_background_color,
        ))


# packages/flutter/lib/src/material/snack_bar_theme.dart
class SnackBarBehavior(Enum):
    index = 'index'
    values = 'values'
    fixed = 'fixed'
    floating = 'floating'


# packages/flutter/lib/src/material/snack_bar_theme.dart
class SnackBarThemeData:
    def __init__(
            self,
            background_color: Optional[Color] = None,
            action_text_color: Optional[Color] = None,
            disabled_action_text_color: Optional[Color] = None,
            content_text_style: Optional[TextStyle] = None,
            elevation: Optional[float] = None,
            shape: Optional[ShapeBorder] = None,
            behavior: Optional[SnackBarBehavior] = None,
    ):
        self.__ctor = (('',), (
            'backgroundColor', background_color,
            'actionTextColor', action_text_color,
            'disabledActionTextColor', disabled_action_text_color,
            'contentTextStyle', content_text_style,
            'elevation', elevation,
            'shape', shape,
            'behavior', behavior,
        ))


# packages/flutter/lib/src/material/bottom_sheet_theme.dart
class BottomSheetThemeData:
    def __init__(
            self,
            background_color: Optional[Color] = None,
            elevation: Optional[float] = None,
            modal_background_color: Optional[Color] = None,
            modal_elevation: Optional[float] = None,
            shape: Optional[ShapeBorder] = None,
            clip_behavior: Optional[Clip] = None,
            constraints: Optional[BoxConstraints] = None,
    ):
        self.__ctor = (('',), (
            'backgroundColor', background_color,
            'elevation', elevation,
            'modalBackgroundColor', modal_background_color,
            'modalElevation', modal_elevation,
            'shape', shape,
            'clipBehavior', clip_behavior,
            'constraints', constraints,
        ))


# packages/flutter/lib/src/material/popup_menu_theme.dart
class PopupMenuThemeData:
    def __init__(
            self,
            color: Optional[Color] = None,
            shape: Optional[ShapeBorder] = None,
            elevation: Optional[float] = None,
            text_style: Optional[TextStyle] = None,
            enable_feedback: Optional[bool] = None,
    ):
        self.__ctor = (('',), (
            'color', color,
            'shape', shape,
            'elevation', elevation,
            'textStyle', text_style,
            'enableFeedback', enable_feedback,
        ))


# packages/flutter/lib/src/material/banner_theme.dart
class MaterialBannerThemeData:
    def __init__(
            self,
            background_color: Optional[Color] = None,
            content_text_style: Optional[TextStyle] = None,
            padding: Optional[EdgeInsetsGeometry] = None,
            leading_padding: Optional[EdgeInsetsGeometry] = None,
    ):
        self.__ctor = (('',), (
            'backgroundColor', background_color,
            'contentTextStyle', content_text_style,
            'padding', padding,
            'leadingPadding', leading_padding,
        ))


# packages/flutter/lib/src/material/divider_theme.dart
class DividerThemeData:
    def __init__(
            self,
            color: Optional[Color] = None,
            space: Optional[float] = None,
            thickness: Optional[float] = None,
            indent: Optional[float] = None,
            end_indent: Optional[float] = None,
    ):
        self.__ctor = (('',), (
            'color', color,
            'space', space,
            'thickness', thickness,
            'indent', indent,
            'endIndent', end_indent,
        ))


# packages/flutter/lib/src/rendering/flex.dart
class MainAxisAlignment(Enum):
    index = 'index'
    values = 'values'
    start = 'start'
    end = 'end'
    center = 'center'
    space_between = 'spaceBetween'
    space_around = 'spaceAround'
    space_evenly = 'spaceEvenly'


# packages/flutter/lib/src/rendering/flex.dart
class MainAxisSize(Enum):
    index = 'index'
    values = 'values'
    min = 'min'
    max = 'max'


# packages/flutter/lib/src/painting/basic_types.dart
class VerticalDirection(Enum):
    index = 'index'
    values = 'values'
    up = 'up'
    down = 'down'


# packages/flutter/lib/src/material/button_bar_theme.dart
class ButtonBarThemeData:
    def __init__(
            self,
            alignment: Optional[MainAxisAlignment] = None,
            main_axis_size: Optional[MainAxisSize] = None,
            button_text_theme: Optional[ButtonTextTheme] = None,
            button_min_width: Optional[float] = None,
            button_height: Optional[float] = None,
            button_padding: Optional[EdgeInsetsGeometry] = None,
            button_aligned_dropdown: Optional[bool] = None,
            layout_behavior: Optional[ButtonBarLayoutBehavior] = None,
            overflow_direction: Optional[VerticalDirection] = None,
    ):
        self.__ctor = (('',), (
            'alignment', alignment,
            'mainAxisSize', main_axis_size,
            'buttonTextTheme', button_text_theme,
            'buttonMinWidth', button_min_width,
            'buttonHeight', button_height,
            'buttonPadding', button_padding,
            'buttonAlignedDropdown', button_aligned_dropdown,
            'layoutBehavior', layout_behavior,
            'overflowDirection', overflow_direction,
        ))


# packages/flutter/lib/src/material/bottom_navigation_bar.dart
class BottomNavigationBarType(Enum):
    index = 'index'
    values = 'values'
    fixed = 'fixed'
    shifting = 'shifting'


# packages/flutter/lib/src/material/bottom_navigation_bar.dart
class BottomNavigationBarLandscapeLayout(Enum):
    index = 'index'
    values = 'values'
    spread = 'spread'
    centered = 'centered'
    linear = 'linear'


# packages/flutter/lib/src/material/bottom_navigation_bar_theme.dart
class BottomNavigationBarThemeData:
    def __init__(
            self,
            background_color: Optional[Color] = None,
            elevation: Optional[float] = None,
            selected_icon_theme: Optional[IconThemeData] = None,
            unselected_icon_theme: Optional[IconThemeData] = None,
            selected_item_color: Optional[Color] = None,
            unselected_item_color: Optional[Color] = None,
            selected_label_style: Optional[TextStyle] = None,
            unselected_label_style: Optional[TextStyle] = None,
            show_selected_labels: Optional[bool] = None,
            show_unselected_labels: Optional[bool] = None,
            type: Optional[BottomNavigationBarType] = None,
            enable_feedback: Optional[bool] = None,
            landscape_layout: Optional[BottomNavigationBarLandscapeLayout] = None,
    ):
        self.__ctor = (('',), (
            'backgroundColor', background_color,
            'elevation', elevation,
            'selectedIconTheme', selected_icon_theme,
            'unselectedIconTheme', unselected_icon_theme,
            'selectedItemColor', selected_item_color,
            'unselectedItemColor', unselected_item_color,
            'selectedLabelStyle', selected_label_style,
            'unselectedLabelStyle', unselected_label_style,
            'showSelectedLabels', show_selected_labels,
            'showUnselectedLabels', show_unselected_labels,
            'type', type,
            'enableFeedback', enable_feedback,
            'landscapeLayout', landscape_layout,
        ))


# packages/flutter/lib/src/material/time_picker_theme.dart
class TimePickerThemeData:
    def __init__(
            self,
            background_color: Optional[Color] = None,
            hour_minute_text_color: Optional[Color] = None,
            hour_minute_color: Optional[Color] = None,
            day_period_text_color: Optional[Color] = None,
            day_period_color: Optional[Color] = None,
            dial_hand_color: Optional[Color] = None,
            dial_background_color: Optional[Color] = None,
            dial_text_color: Optional[Color] = None,
            entry_mode_icon_color: Optional[Color] = None,
            hour_minute_text_style: Optional[TextStyle] = None,
            day_period_text_style: Optional[TextStyle] = None,
            help_text_style: Optional[TextStyle] = None,
            shape: Optional[ShapeBorder] = None,
            hour_minute_shape: Optional[ShapeBorder] = None,
            day_period_shape: Optional[OutlinedBorder] = None,
            day_period_border_side: Optional[BorderSide] = None,
            input_decoration_theme: Optional[InputDecorationTheme] = None,
    ):
        self.__ctor = (('',), (
            'backgroundColor', background_color,
            'hourMinuteTextColor', hour_minute_text_color,
            'hourMinuteColor', hour_minute_color,
            'dayPeriodTextColor', day_period_text_color,
            'dayPeriodColor', day_period_color,
            'dialHandColor', dial_hand_color,
            'dialBackgroundColor', dial_background_color,
            'dialTextColor', dial_text_color,
            'entryModeIconColor', entry_mode_icon_color,
            'hourMinuteTextStyle', hour_minute_text_style,
            'dayPeriodTextStyle', day_period_text_style,
            'helpTextStyle', help_text_style,
            'shape', shape,
            'hourMinuteShape', hour_minute_shape,
            'dayPeriodShape', day_period_shape,
            'dayPeriodBorderSide', day_period_border_side,
            'inputDecorationTheme', input_decoration_theme,
        ))


# packages/flutter/lib/src/services/mouse_cursor.dart
class MouseCursor:
    pass


MouseCursor.defer = MouseCursor(
)
MouseCursor.defer.__ctor = ('defer', )
MouseCursor.uncontrolled = MouseCursor(
)
MouseCursor.uncontrolled.__ctor = ('uncontrolled', )


# packages/flutter/lib/src/painting/alignment.dart
class AlignmentGeometry:
    pass


# packages/flutter/lib/src/material/button_style.dart
class ButtonStyle:
    def __init__(
            self,
            text_style: Optional[MaterialStateProperty[TextStyle]] = None,
            background_color: Optional[MaterialStateProperty[Color]] = None,
            foreground_color: Optional[MaterialStateProperty[Color]] = None,
            overlay_color: Optional[MaterialStateProperty[Color]] = None,
            shadow_color: Optional[MaterialStateProperty[Color]] = None,
            elevation: Optional[MaterialStateProperty[float]] = None,
            padding: Optional[MaterialStateProperty[EdgeInsetsGeometry]] = None,
            minimum_size: Optional[MaterialStateProperty[Size]] = None,
            fixed_size: Optional[MaterialStateProperty[Size]] = None,
            maximum_size: Optional[MaterialStateProperty[Size]] = None,
            side: Optional[MaterialStateProperty[BorderSide]] = None,
            shape: Optional[MaterialStateProperty[OutlinedBorder]] = None,
            mouse_cursor: Optional[MaterialStateProperty[MouseCursor]] = None,
            visual_density: Optional[VisualDensity] = None,
            tap_target_size: Optional[MaterialTapTargetSize] = None,
            animation_duration: Optional[Duration] = None,
            enable_feedback: Optional[bool] = None,
            alignment: Optional[AlignmentGeometry] = None,
            splash_factory: Optional[InteractiveInkFeatureFactory] = None,
    ):
        self.__ctor = (('',), (
            'textStyle', text_style,
            'backgroundColor', background_color,
            'foregroundColor', foreground_color,
            'overlayColor', overlay_color,
            'shadowColor', shadow_color,
            'elevation', elevation,
            'padding', padding,
            'minimumSize', minimum_size,
            'fixedSize', fixed_size,
            'maximumSize', maximum_size,
            'side', side,
            'shape', shape,
            'mouseCursor', mouse_cursor,
            'visualDensity', visual_density,
            'tapTargetSize', tap_target_size,
            'animationDuration', animation_duration,
            'enableFeedback', enable_feedback,
            'alignment', alignment,
            'splashFactory', splash_factory,
        ))


# packages/flutter/lib/src/material/text_button_theme.dart
class TextButtonThemeData:
    def __init__(
            self,
            style: Optional[ButtonStyle] = None,
    ):
        self.__ctor = (('',), (
            'style', style,
        ))


# packages/flutter/lib/src/material/elevated_button_theme.dart
class ElevatedButtonThemeData:
    def __init__(
            self,
            style: Optional[ButtonStyle] = None,
    ):
        self.__ctor = (('',), (
            'style', style,
        ))


# packages/flutter/lib/src/material/outlined_button_theme.dart
class OutlinedButtonThemeData:
    def __init__(
            self,
            style: Optional[ButtonStyle] = None,
    ):
        self.__ctor = (('',), (
            'style', style,
        ))


# packages/flutter/lib/src/material/text_selection_theme.dart
class TextSelectionThemeData:
    def __init__(
            self,
            cursor_color: Optional[Color] = None,
            selection_color: Optional[Color] = None,
            selection_handle_color: Optional[Color] = None,
    ):
        self.__ctor = (('',), (
            'cursorColor', cursor_color,
            'selectionColor', selection_color,
            'selectionHandleColor', selection_handle_color,
        ))


# packages/flutter/lib/src/material/data_table_theme.dart
class DataTableThemeData:
    def __init__(
            self,
            decoration: Optional[Decoration] = None,
            data_row_color: Optional[MaterialStateProperty[Color]] = None,
            data_row_height: Optional[float] = None,
            data_text_style: Optional[TextStyle] = None,
            heading_row_color: Optional[MaterialStateProperty[Color]] = None,
            heading_row_height: Optional[float] = None,
            heading_text_style: Optional[TextStyle] = None,
            horizontal_margin: Optional[float] = None,
            column_spacing: Optional[float] = None,
            divider_thickness: Optional[float] = None,
            checkbox_horizontal_margin: Optional[float] = None,
    ):
        self.__ctor = (('',), (
            'decoration', decoration,
            'dataRowColor', data_row_color,
            'dataRowHeight', data_row_height,
            'dataTextStyle', data_text_style,
            'headingRowColor', heading_row_color,
            'headingRowHeight', heading_row_height,
            'headingTextStyle', heading_text_style,
            'horizontalMargin', horizontal_margin,
            'columnSpacing', column_spacing,
            'dividerThickness', divider_thickness,
            'checkboxHorizontalMargin', checkbox_horizontal_margin,
        ))


# packages/flutter/lib/src/material/checkbox_theme.dart
class CheckboxThemeData:
    def __init__(
            self,
            mouse_cursor: Optional[MaterialStateProperty[MouseCursor]] = None,
            fill_color: Optional[MaterialStateProperty[Color]] = None,
            check_color: Optional[MaterialStateProperty[Color]] = None,
            overlay_color: Optional[MaterialStateProperty[Color]] = None,
            splash_radius: Optional[float] = None,
            material_tap_target_size: Optional[MaterialTapTargetSize] = None,
            visual_density: Optional[VisualDensity] = None,
            shape: Optional[OutlinedBorder] = None,
            side: Optional[BorderSide] = None,
    ):
        self.__ctor = (('',), (
            'mouseCursor', mouse_cursor,
            'fillColor', fill_color,
            'checkColor', check_color,
            'overlayColor', overlay_color,
            'splashRadius', splash_radius,
            'materialTapTargetSize', material_tap_target_size,
            'visualDensity', visual_density,
            'shape', shape,
            'side', side,
        ))


# packages/flutter/lib/src/material/radio_theme.dart
class RadioThemeData:
    def __init__(
            self,
            mouse_cursor: Optional[MaterialStateProperty[MouseCursor]] = None,
            fill_color: Optional[MaterialStateProperty[Color]] = None,
            overlay_color: Optional[MaterialStateProperty[Color]] = None,
            splash_radius: Optional[float] = None,
            material_tap_target_size: Optional[MaterialTapTargetSize] = None,
            visual_density: Optional[VisualDensity] = None,
    ):
        self.__ctor = (('',), (
            'mouseCursor', mouse_cursor,
            'fillColor', fill_color,
            'overlayColor', overlay_color,
            'splashRadius', splash_radius,
            'materialTapTargetSize', material_tap_target_size,
            'visualDensity', visual_density,
        ))


# packages/flutter/lib/src/material/switch_theme.dart
class SwitchThemeData:
    def __init__(
            self,
            thumb_color: Optional[MaterialStateProperty[Color]] = None,
            track_color: Optional[MaterialStateProperty[Color]] = None,
            material_tap_target_size: Optional[MaterialTapTargetSize] = None,
            mouse_cursor: Optional[MaterialStateProperty[MouseCursor]] = None,
            overlay_color: Optional[MaterialStateProperty[Color]] = None,
            splash_radius: Optional[float] = None,
    ):
        self.__ctor = (('',), (
            'thumbColor', thumb_color,
            'trackColor', track_color,
            'materialTapTargetSize', material_tap_target_size,
            'mouseCursor', mouse_cursor,
            'overlayColor', overlay_color,
            'splashRadius', splash_radius,
        ))


# packages/flutter/lib/src/material/progress_indicator_theme.dart
class ProgressIndicatorThemeData:
    def __init__(
            self,
            color: Optional[Color] = None,
            linear_track_color: Optional[Color] = None,
            linear_min_height: Optional[float] = None,
            circular_track_color: Optional[Color] = None,
            refresh_background_color: Optional[Color] = None,
    ):
        self.__ctor = (('',), (
            'color', color,
            'linearTrackColor', linear_track_color,
            'linearMinHeight', linear_min_height,
            'circularTrackColor', circular_track_color,
            'refreshBackgroundColor', refresh_background_color,
        ))


# packages/flutter/lib/src/material/theme_data.dart
class ThemeData:
    def __init__(
            self,
            brightness: Optional[Brightness] = None,
            visual_density: Optional[VisualDensity] = None,
            primary_swatch: Optional[MaterialColor] = None,
            primary_color: Optional[Color] = None,
            primary_color_brightness: Optional[Brightness] = None,
            primary_color_light: Optional[Color] = None,
            primary_color_dark: Optional[Color] = None,
            accent_color: Optional[Color] = None,
            accent_color_brightness: Optional[Brightness] = None,
            canvas_color: Optional[Color] = None,
            shadow_color: Optional[Color] = None,
            scaffold_background_color: Optional[Color] = None,
            bottom_app_bar_color: Optional[Color] = None,
            card_color: Optional[Color] = None,
            divider_color: Optional[Color] = None,
            focus_color: Optional[Color] = None,
            hover_color: Optional[Color] = None,
            highlight_color: Optional[Color] = None,
            splash_color: Optional[Color] = None,
            splash_factory: Optional[InteractiveInkFeatureFactory] = None,
            selected_row_color: Optional[Color] = None,
            unselected_widget_color: Optional[Color] = None,
            disabled_color: Optional[Color] = None,
            button_color: Optional[Color] = None,
            button_theme: Optional[ButtonThemeData] = None,
            toggle_buttons_theme: Optional[ToggleButtonsThemeData] = None,
            secondary_header_color: Optional[Color] = None,
            text_selection_color: Optional[Color] = None,
            cursor_color: Optional[Color] = None,
            text_selection_handle_color: Optional[Color] = None,
            background_color: Optional[Color] = None,
            dialog_background_color: Optional[Color] = None,
            indicator_color: Optional[Color] = None,
            hint_color: Optional[Color] = None,
            error_color: Optional[Color] = None,
            toggleable_active_color: Optional[Color] = None,
            font_family: Optional[str] = None,
            text_theme: Optional[TextTheme] = None,
            primary_text_theme: Optional[TextTheme] = None,
            accent_text_theme: Optional[TextTheme] = None,
            input_decoration_theme: Optional[InputDecorationTheme] = None,
            icon_theme: Optional[IconThemeData] = None,
            primary_icon_theme: Optional[IconThemeData] = None,
            accent_icon_theme: Optional[IconThemeData] = None,
            slider_theme: Optional[SliderThemeData] = None,
            tab_bar_theme: Optional[TabBarTheme] = None,
            tooltip_theme: Optional[TooltipThemeData] = None,
            card_theme: Optional[CardTheme] = None,
            chip_theme: Optional[ChipThemeData] = None,
            platform: Optional[TargetPlatform] = None,
            material_tap_target_size: Optional[MaterialTapTargetSize] = None,
            apply_elevation_overlay_color: Optional[bool] = None,
            page_transitions_theme: Optional[PageTransitionsTheme] = None,
            app_bar_theme: Optional[AppBarTheme] = None,
            scrollbar_theme: Optional[ScrollbarThemeData] = None,
            bottom_app_bar_theme: Optional[BottomAppBarTheme] = None,
            color_scheme: Optional[ColorScheme] = None,
            dialog_theme: Optional[DialogTheme] = None,
            floating_action_button_theme: Optional[FloatingActionButtonThemeData] = None,
            navigation_rail_theme: Optional[NavigationRailThemeData] = None,
            typography: Optional[Typography] = None,
            cupertino_override_theme: Optional[NoDefaultCupertinoThemeData] = None,
            snack_bar_theme: Optional[SnackBarThemeData] = None,
            bottom_sheet_theme: Optional[BottomSheetThemeData] = None,
            popup_menu_theme: Optional[PopupMenuThemeData] = None,
            banner_theme: Optional[MaterialBannerThemeData] = None,
            divider_theme: Optional[DividerThemeData] = None,
            button_bar_theme: Optional[ButtonBarThemeData] = None,
            bottom_navigation_bar_theme: Optional[BottomNavigationBarThemeData] = None,
            time_picker_theme: Optional[TimePickerThemeData] = None,
            text_button_theme: Optional[TextButtonThemeData] = None,
            elevated_button_theme: Optional[ElevatedButtonThemeData] = None,
            outlined_button_theme: Optional[OutlinedButtonThemeData] = None,
            text_selection_theme: Optional[TextSelectionThemeData] = None,
            data_table_theme: Optional[DataTableThemeData] = None,
            checkbox_theme: Optional[CheckboxThemeData] = None,
            radio_theme: Optional[RadioThemeData] = None,
            switch_theme: Optional[SwitchThemeData] = None,
            progress_indicator_theme: Optional[ProgressIndicatorThemeData] = None,
            fix_text_field_outline_label: Optional[bool] = None,
            use_text_selection_theme: Optional[bool] = None,
    ):
        self.__ctor = (('',), (
            'brightness', brightness,
            'visualDensity', visual_density,
            'primarySwatch', primary_swatch,
            'primaryColor', primary_color,
            'primaryColorBrightness', primary_color_brightness,
            'primaryColorLight', primary_color_light,
            'primaryColorDark', primary_color_dark,
            'accentColor', accent_color,
            'accentColorBrightness', accent_color_brightness,
            'canvasColor', canvas_color,
            'shadowColor', shadow_color,
            'scaffoldBackgroundColor', scaffold_background_color,
            'bottomAppBarColor', bottom_app_bar_color,
            'cardColor', card_color,
            'dividerColor', divider_color,
            'focusColor', focus_color,
            'hoverColor', hover_color,
            'highlightColor', highlight_color,
            'splashColor', splash_color,
            'splashFactory', splash_factory,
            'selectedRowColor', selected_row_color,
            'unselectedWidgetColor', unselected_widget_color,
            'disabledColor', disabled_color,
            'buttonColor', button_color,
            'buttonTheme', button_theme,
            'toggleButtonsTheme', toggle_buttons_theme,
            'secondaryHeaderColor', secondary_header_color,
            'textSelectionColor', text_selection_color,
            'cursorColor', cursor_color,
            'textSelectionHandleColor', text_selection_handle_color,
            'backgroundColor', background_color,
            'dialogBackgroundColor', dialog_background_color,
            'indicatorColor', indicator_color,
            'hintColor', hint_color,
            'errorColor', error_color,
            'toggleableActiveColor', toggleable_active_color,
            'fontFamily', font_family,
            'textTheme', text_theme,
            'primaryTextTheme', primary_text_theme,
            'accentTextTheme', accent_text_theme,
            'inputDecorationTheme', input_decoration_theme,
            'iconTheme', icon_theme,
            'primaryIconTheme', primary_icon_theme,
            'accentIconTheme', accent_icon_theme,
            'sliderTheme', slider_theme,
            'tabBarTheme', tab_bar_theme,
            'tooltipTheme', tooltip_theme,
            'cardTheme', card_theme,
            'chipTheme', chip_theme,
            'platform', platform,
            'materialTapTargetSize', material_tap_target_size,
            'applyElevationOverlayColor', apply_elevation_overlay_color,
            'pageTransitionsTheme', page_transitions_theme,
            'appBarTheme', app_bar_theme,
            'scrollbarTheme', scrollbar_theme,
            'bottomAppBarTheme', bottom_app_bar_theme,
            'colorScheme', color_scheme,
            'dialogTheme', dialog_theme,
            'floatingActionButtonTheme', floating_action_button_theme,
            'navigationRailTheme', navigation_rail_theme,
            'typography', typography,
            'cupertinoOverrideTheme', cupertino_override_theme,
            'snackBarTheme', snack_bar_theme,
            'bottomSheetTheme', bottom_sheet_theme,
            'popupMenuTheme', popup_menu_theme,
            'bannerTheme', banner_theme,
            'dividerTheme', divider_theme,
            'buttonBarTheme', button_bar_theme,
            'bottomNavigationBarTheme', bottom_navigation_bar_theme,
            'timePickerTheme', time_picker_theme,
            'textButtonTheme', text_button_theme,
            'elevatedButtonTheme', elevated_button_theme,
            'outlinedButtonTheme', outlined_button_theme,
            'textSelectionTheme', text_selection_theme,
            'dataTableTheme', data_table_theme,
            'checkboxTheme', checkbox_theme,
            'radioTheme', radio_theme,
            'switchTheme', switch_theme,
            'progressIndicatorTheme', progress_indicator_theme,
            'fixTextFieldOutlineLabel', fix_text_field_outline_label,
            'useTextSelectionTheme', use_text_selection_theme,
        ))

    @staticmethod
    def raw(
            visual_density: VisualDensity,
            primary_color: Color,
            primary_color_brightness: Brightness,
            primary_color_light: Color,
            primary_color_dark: Color,
            canvas_color: Color,
            shadow_color: Color,
            accent_color: Color,
            accent_color_brightness: Brightness,
            scaffold_background_color: Color,
            bottom_app_bar_color: Color,
            card_color: Color,
            divider_color: Color,
            focus_color: Color,
            hover_color: Color,
            highlight_color: Color,
            splash_color: Color,
            splash_factory: InteractiveInkFeatureFactory,
            selected_row_color: Color,
            unselected_widget_color: Color,
            disabled_color: Color,
            button_theme: ButtonThemeData,
            button_color: Color,
            toggle_buttons_theme: ToggleButtonsThemeData,
            secondary_header_color: Color,
            text_selection_color: Color,
            cursor_color: Color,
            text_selection_handle_color: Color,
            background_color: Color,
            dialog_background_color: Color,
            indicator_color: Color,
            hint_color: Color,
            error_color: Color,
            toggleable_active_color: Color,
            text_theme: TextTheme,
            primary_text_theme: TextTheme,
            accent_text_theme: TextTheme,
            input_decoration_theme: InputDecorationTheme,
            icon_theme: IconThemeData,
            primary_icon_theme: IconThemeData,
            accent_icon_theme: IconThemeData,
            slider_theme: SliderThemeData,
            tab_bar_theme: TabBarTheme,
            tooltip_theme: TooltipThemeData,
            card_theme: CardTheme,
            chip_theme: ChipThemeData,
            platform: TargetPlatform,
            material_tap_target_size: MaterialTapTargetSize,
            apply_elevation_overlay_color: bool,
            page_transitions_theme: PageTransitionsTheme,
            app_bar_theme: AppBarTheme,
            scrollbar_theme: ScrollbarThemeData,
            bottom_app_bar_theme: BottomAppBarTheme,
            color_scheme: ColorScheme,
            dialog_theme: DialogTheme,
            floating_action_button_theme: FloatingActionButtonThemeData,
            navigation_rail_theme: NavigationRailThemeData,
            typography: Typography,
            cupertino_override_theme: NoDefaultCupertinoThemeData,
            snack_bar_theme: SnackBarThemeData,
            bottom_sheet_theme: BottomSheetThemeData,
            popup_menu_theme: PopupMenuThemeData,
            banner_theme: MaterialBannerThemeData,
            divider_theme: DividerThemeData,
            button_bar_theme: ButtonBarThemeData,
            bottom_navigation_bar_theme: BottomNavigationBarThemeData,
            time_picker_theme: TimePickerThemeData,
            text_button_theme: TextButtonThemeData,
            elevated_button_theme: ElevatedButtonThemeData,
            outlined_button_theme: OutlinedButtonThemeData,
            text_selection_theme: TextSelectionThemeData,
            data_table_theme: DataTableThemeData,
            checkbox_theme: CheckboxThemeData,
            radio_theme: RadioThemeData,
            switch_theme: SwitchThemeData,
            progress_indicator_theme: ProgressIndicatorThemeData,
            fix_text_field_outline_label: bool,
            use_text_selection_theme: bool,
    ) -> 'ThemeData':
        _o = ThemeData(
        )
        _o.__ctor = (('raw',), (
            'visualDensity', visual_density,
            'primaryColor', primary_color,
            'primaryColorBrightness', primary_color_brightness,
            'primaryColorLight', primary_color_light,
            'primaryColorDark', primary_color_dark,
            'canvasColor', canvas_color,
            'shadowColor', shadow_color,
            'accentColor', accent_color,
            'accentColorBrightness', accent_color_brightness,
            'scaffoldBackgroundColor', scaffold_background_color,
            'bottomAppBarColor', bottom_app_bar_color,
            'cardColor', card_color,
            'dividerColor', divider_color,
            'focusColor', focus_color,
            'hoverColor', hover_color,
            'highlightColor', highlight_color,
            'splashColor', splash_color,
            'splashFactory', splash_factory,
            'selectedRowColor', selected_row_color,
            'unselectedWidgetColor', unselected_widget_color,
            'disabledColor', disabled_color,
            'buttonTheme', button_theme,
            'buttonColor', button_color,
            'toggleButtonsTheme', toggle_buttons_theme,
            'secondaryHeaderColor', secondary_header_color,
            'textSelectionColor', text_selection_color,
            'cursorColor', cursor_color,
            'textSelectionHandleColor', text_selection_handle_color,
            'backgroundColor', background_color,
            'dialogBackgroundColor', dialog_background_color,
            'indicatorColor', indicator_color,
            'hintColor', hint_color,
            'errorColor', error_color,
            'toggleableActiveColor', toggleable_active_color,
            'textTheme', text_theme,
            'primaryTextTheme', primary_text_theme,
            'accentTextTheme', accent_text_theme,
            'inputDecorationTheme', input_decoration_theme,
            'iconTheme', icon_theme,
            'primaryIconTheme', primary_icon_theme,
            'accentIconTheme', accent_icon_theme,
            'sliderTheme', slider_theme,
            'tabBarTheme', tab_bar_theme,
            'tooltipTheme', tooltip_theme,
            'cardTheme', card_theme,
            'chipTheme', chip_theme,
            'platform', platform,
            'materialTapTargetSize', material_tap_target_size,
            'applyElevationOverlayColor', apply_elevation_overlay_color,
            'pageTransitionsTheme', page_transitions_theme,
            'appBarTheme', app_bar_theme,
            'scrollbarTheme', scrollbar_theme,
            'bottomAppBarTheme', bottom_app_bar_theme,
            'colorScheme', color_scheme,
            'dialogTheme', dialog_theme,
            'floatingActionButtonTheme', floating_action_button_theme,
            'navigationRailTheme', navigation_rail_theme,
            'typography', typography,
            'cupertinoOverrideTheme', cupertino_override_theme,
            'snackBarTheme', snack_bar_theme,
            'bottomSheetTheme', bottom_sheet_theme,
            'popupMenuTheme', popup_menu_theme,
            'bannerTheme', banner_theme,
            'dividerTheme', divider_theme,
            'buttonBarTheme', button_bar_theme,
            'bottomNavigationBarTheme', bottom_navigation_bar_theme,
            'timePickerTheme', time_picker_theme,
            'textButtonTheme', text_button_theme,
            'elevatedButtonTheme', elevated_button_theme,
            'outlinedButtonTheme', outlined_button_theme,
            'textSelectionTheme', text_selection_theme,
            'dataTableTheme', data_table_theme,
            'checkboxTheme', checkbox_theme,
            'radioTheme', radio_theme,
            'switchTheme', switch_theme,
            'progressIndicatorTheme', progress_indicator_theme,
            'fixTextFieldOutlineLabel', fix_text_field_outline_label,
            'useTextSelectionTheme', use_text_selection_theme,
        ))
        return _o

    @staticmethod
    def from_(
            color_scheme: ColorScheme,
            text_theme: Optional[TextTheme] = None,
    ) -> 'ThemeData':
        _o = ThemeData(
        )
        _o.__ctor = (('from',), (
            'colorScheme', color_scheme,
            'textTheme', text_theme,
        ))
        return _o

    @staticmethod
    def light(
    ) -> 'ThemeData':
        _o = ThemeData(
        )
        _o.__ctor = (('light',), (
        ))
        return _o

    @staticmethod
    def dark(
    ) -> 'ThemeData':
        _o = ThemeData(
        )
        _o.__ctor = (('dark',), (
        ))
        return _o

    @staticmethod
    def fallback(
    ) -> 'ThemeData':
        _o = ThemeData(
        )
        _o.__ctor = (('fallback',), (
        ))
        return _o


# packages/flutter/lib/src/material/app.dart
class ThemeMode(Enum):
    index = 'index'
    values = 'values'
    system = 'system'
    light = 'light'
    dark = 'dark'


# packages/flutter/lib/src/widgets/localizations.dart
class LocalizationsDelegate(Generic[T]):
    pass


# packages/flutter/lib/src/widgets/shortcuts.dart
class ShortcutActivator:
    pass


# packages/flutter/lib/src/widgets/actions.dart
class DoNothingIntent:
    pass


def _intent__do_nothing_intent(_k: str) -> DoNothingIntent:
    _o = DoNothingIntent(
    )
    _o.__ctor = (('Intent', _k),)
    return _o


# packages/flutter/lib/src/widgets/actions.dart
class Intent:
    do_nothing: DoNothingIntent = _intent__do_nothing_intent('doNothing')


# bin/cache/pkg/sky_engine/lib/core/type.dart
class Type:
    pass


# packages/flutter/lib/src/widgets/actions.dart
class Action(Generic[T]):
    pass


# packages/flutter/lib/src/widgets/scroll_configuration.dart
class ScrollBehavior:
    pass


# packages/flutter/lib/src/widgets/navigator.dart
class NavigatorState:
    pass


# packages/flutter/lib/src/widgets/framework.dart
class Widget:
    def __init__(
            self,
            key: Optional[Key] = None,
    ):
        self.__ctor = (('',), (
            'key', key,
        ))


# packages/flutter/lib/src/widgets/navigator.dart
class NavigatorObserver:
    pass


# packages/flutter/lib/src/material/app.dart
class MaterialApp:
    def __init__(
            self,
            key: Optional[Key] = None,
            navigator_key: Optional[GlobalKey[NavigatorState]] = None,
            scaffold_messenger_key: Optional[GlobalKey[ScaffoldMessengerState]] = None,
            home: Optional[Widget] = None,
            routes: Optional[Dict[str, Callable]] = None,
            initial_route: Optional[str] = None,
            on_generate_route: Optional[Callable] = None,
            on_generate_initial_routes: Optional[Callable] = None,
            on_unknown_route: Optional[Callable] = None,
            navigator_observers: Optional[List[NavigatorObserver]] = None,
            builder: Optional[Callable] = None,
            title: Optional[str] = None,
            on_generate_title: Optional[Callable] = None,
            color: Optional[Color] = None,
            theme: Optional[ThemeData] = None,
            dark_theme: Optional[ThemeData] = None,
            high_contrast_theme: Optional[ThemeData] = None,
            high_contrast_dark_theme: Optional[ThemeData] = None,
            theme_mode: Optional[ThemeMode] = None,
            locale: Optional[Locale] = None,
            localizations_delegates: Optional[Iterable[LocalizationsDelegate[Any]]] = None,
            locale_list_resolution_callback: Optional[Callable] = None,
            locale_resolution_callback: Optional[Callable] = None,
            supported_locales: Optional[Iterable[Locale]] = None,
            debug_show_material_grid: Optional[bool] = None,
            show_performance_overlay: Optional[bool] = None,
            checkerboard_raster_cache_images: Optional[bool] = None,
            checkerboard_offscreen_layers: Optional[bool] = None,
            show_semantics_debugger: Optional[bool] = None,
            debug_show_checked_mode_banner: Optional[bool] = None,
            shortcuts: Optional[Dict[ShortcutActivator, Intent]] = None,
            actions: Optional[Dict[Type, Action[Intent]]] = None,
            restoration_scope_id: Optional[str] = None,
            scroll_behavior: Optional[ScrollBehavior] = None,
            use_inherited_media_query: Optional[bool] = None,
    ):
        self.__ctor = (('',), (
            'key', key,
            'navigatorKey', navigator_key,
            'scaffoldMessengerKey', scaffold_messenger_key,
            'home', home,
            'routes', routes,
            'initialRoute', initial_route,
            'onGenerateRoute', on_generate_route,
            'onGenerateInitialRoutes', on_generate_initial_routes,
            'onUnknownRoute', on_unknown_route,
            'navigatorObservers', navigator_observers,
            'builder', builder,
            'title', title,
            'onGenerateTitle', on_generate_title,
            'color', color,
            'theme', theme,
            'darkTheme', dark_theme,
            'highContrastTheme', high_contrast_theme,
            'highContrastDarkTheme', high_contrast_dark_theme,
            'themeMode', theme_mode,
            'locale', locale,
            'localizationsDelegates', localizations_delegates,
            'localeListResolutionCallback', locale_list_resolution_callback,
            'localeResolutionCallback', locale_resolution_callback,
            'supportedLocales', supported_locales,
            'debugShowMaterialGrid', debug_show_material_grid,
            'showPerformanceOverlay', show_performance_overlay,
            'checkerboardRasterCacheImages', checkerboard_raster_cache_images,
            'checkerboardOffscreenLayers', checkerboard_offscreen_layers,
            'showSemanticsDebugger', show_semantics_debugger,
            'debugShowCheckedModeBanner', debug_show_checked_mode_banner,
            'shortcuts', shortcuts,
            'actions', actions,
            'restorationScopeId', restoration_scope_id,
            'scrollBehavior', scroll_behavior,
            'useInheritedMediaQuery', use_inherited_media_query,
        ))

    @staticmethod
    def router(
            route_information_parser: RouteInformationParser[Object],
            router_delegate: RouterDelegate[Object],
            key: Optional[Key] = None,
            scaffold_messenger_key: Optional[GlobalKey[ScaffoldMessengerState]] = None,
            route_information_provider: Optional[RouteInformationProvider] = None,
            back_button_dispatcher: Optional[BackButtonDispatcher] = None,
            builder: Optional[Callable] = None,
            title: Optional[str] = None,
            on_generate_title: Optional[Callable] = None,
            color: Optional[Color] = None,
            theme: Optional[ThemeData] = None,
            dark_theme: Optional[ThemeData] = None,
            high_contrast_theme: Optional[ThemeData] = None,
            high_contrast_dark_theme: Optional[ThemeData] = None,
            theme_mode: Optional[ThemeMode] = None,
            locale: Optional[Locale] = None,
            localizations_delegates: Optional[Iterable[LocalizationsDelegate[Any]]] = None,
            locale_list_resolution_callback: Optional[Callable] = None,
            locale_resolution_callback: Optional[Callable] = None,
            supported_locales: Optional[Iterable[Locale]] = None,
            debug_show_material_grid: Optional[bool] = None,
            show_performance_overlay: Optional[bool] = None,
            checkerboard_raster_cache_images: Optional[bool] = None,
            checkerboard_offscreen_layers: Optional[bool] = None,
            show_semantics_debugger: Optional[bool] = None,
            debug_show_checked_mode_banner: Optional[bool] = None,
            shortcuts: Optional[Dict[ShortcutActivator, Intent]] = None,
            actions: Optional[Dict[Type, Action[Intent]]] = None,
            restoration_scope_id: Optional[str] = None,
            scroll_behavior: Optional[ScrollBehavior] = None,
            use_inherited_media_query: Optional[bool] = None,
    ) -> 'MaterialApp':
        _o = MaterialApp(
        )
        _o.__ctor = (('router',), (
            'key', key,
            'scaffoldMessengerKey', scaffold_messenger_key,
            'routeInformationProvider', route_information_provider,
            'routeInformationParser', route_information_parser,
            'routerDelegate', router_delegate,
            'backButtonDispatcher', back_button_dispatcher,
            'builder', builder,
            'title', title,
            'onGenerateTitle', on_generate_title,
            'color', color,
            'theme', theme,
            'darkTheme', dark_theme,
            'highContrastTheme', high_contrast_theme,
            'highContrastDarkTheme', high_contrast_dark_theme,
            'themeMode', theme_mode,
            'locale', locale,
            'localizationsDelegates', localizations_delegates,
            'localeListResolutionCallback', locale_list_resolution_callback,
            'localeResolutionCallback', locale_resolution_callback,
            'supportedLocales', supported_locales,
            'debugShowMaterialGrid', debug_show_material_grid,
            'showPerformanceOverlay', show_performance_overlay,
            'checkerboardRasterCacheImages', checkerboard_raster_cache_images,
            'checkerboardOffscreenLayers', checkerboard_offscreen_layers,
            'showSemanticsDebugger', show_semantics_debugger,
            'debugShowCheckedModeBanner', debug_show_checked_mode_banner,
            'shortcuts', shortcuts,
            'actions', actions,
            'restorationScopeId', restoration_scope_id,
            'scrollBehavior', scroll_behavior,
            'useInheritedMediaQuery', use_inherited_media_query,
        ))
        return _o


# packages/flutter/lib/src/widgets/focus_manager.dart
class FocusNode:
    def __init__(
            self,
            debug_label: Optional[str] = None,
            on_key: Optional[Callable] = None,
            on_key_event: Optional[Callable] = None,
            skip_traversal: Optional[bool] = None,
            can_request_focus: Optional[bool] = None,
            descendants_are_focusable: Optional[bool] = None,
    ):
        self.__ctor = (('',), (
            'debugLabel', debug_label,
            'onKey', on_key,
            'onKeyEvent', on_key_event,
            'skipTraversal', skip_traversal,
            'canRequestFocus', can_request_focus,
            'descendantsAreFocusable', descendants_are_focusable,
        ))


# packages/flutter/lib/src/material/elevated_button.dart
class ElevatedButton:
    def __init__(
            self,
            on_pressed: Callable,
            child: Widget,
            key: Optional[Key] = None,
            on_long_press: Optional[Callable] = None,
            style: Optional[ButtonStyle] = None,
            focus_node: Optional[FocusNode] = None,
            autofocus: Optional[bool] = None,
            clip_behavior: Optional[Clip] = None,
    ):
        self.__ctor = (('',), (
            'key', key,
            'onPressed', on_pressed,
            'onLongPress', on_long_press,
            'style', style,
            'focusNode', focus_node,
            'autofocus', autofocus,
            'clipBehavior', clip_behavior,
            'child', child,
        ))

    @staticmethod
    def icon(
            on_pressed: Callable,
            icon: Widget,
            label: Widget,
            key: Optional[Key] = None,
            on_long_press: Optional[Callable] = None,
            style: Optional[ButtonStyle] = None,
            focus_node: Optional[FocusNode] = None,
            autofocus: Optional[bool] = None,
            clip_behavior: Optional[Clip] = None,
    ) -> 'ElevatedButton':
        _o = ElevatedButton(
            on_pressed=None,
            child=Widget(),
        )
        _o.__ctor = (('icon',), (
            'key', key,
            'onPressed', on_pressed,
            'onLongPress', on_long_press,
            'style', style,
            'focusNode', focus_node,
            'autofocus', autofocus,
            'clipBehavior', clip_behavior,
            'icon', icon,
            'label', label,
        ))
        return _o
