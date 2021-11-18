from abc import ABC
from enum import Enum
from typing import Generic, TypeVar, Callable, Any, Optional, Iterable, List, Dict


def _noop(*args, **kwargs):
    pass


T = TypeVar('T')


# bin/cache/pkg/sky_engine/lib/core/object.dart
class Object:
    pass


# packages/flutter/lib/src/foundation/diagnostics.dart
class DiagnosticableTree(ABC, Object):
    pass


# packages/flutter/lib/src/foundation/key.dart
class Key(ABC, Object):

    def __init__(
        self,
        value: str,
    ):
        self.__ctor = (('',), (
            'value', value,
        ))

    @staticmethod
    def empty(
    ):
        _o = Key(
            value='',
        )
        _o.__ctor = (('empty',), (
        ))
        return _o


# packages/flutter/lib/src/widgets/framework.dart
class Widget(ABC, DiagnosticableTree):

    def __init__(
        self,
        key: Optional[Key] = None,
    ):
        self.__ctor = (('',), (
            'key', key,
        ))


# packages/flutter/lib/src/widgets/framework.dart
class StatefulWidget(ABC, Widget):

    def __init__(
        self,
        key: Optional[Key] = None,
    ):
        super().__init__(
        )
        self.__ctor = (('',), (
            'key', key,
        ))


# packages/flutter/lib/src/widgets/framework.dart
class State(ABC, Generic[T], Object):
    pass


# packages/flutter/lib/src/widgets/framework.dart
class GlobalKey(ABC, Generic[T], Key):

    def __init__(
        self,
        debug_label: Optional[str] = None,
    ):
        super().__init__(
            value='',
        )
        self.__ctor = (('',), (
            'debugLabel', debug_label,
        ))

    @staticmethod
    def constructor(
    ):
        _o = GlobalKey(
        )
        _o.__ctor = (('constructor',), (
        ))
        return _o


# bin/cache/pkg/sky_engine/lib/internal/iterable.dart
class EfficientLengthIterable(ABC, Generic[T], Iterable[T]):
    pass


# packages/flutter/lib/src/widgets/navigator.dart
class RouteSettings(Object):

    def __init__(
        self,
        name: Optional[str] = None,
        arguments: Optional[Object] = None,
    ):
        self.__ctor = (('',), (
            'name', name,
            'arguments', arguments,
        ))


# packages/flutter/lib/src/foundation/key.dart
class LocalKey(ABC, Key):
    pass


# packages/flutter/lib/src/widgets/navigator.dart
class Page(ABC, Generic[T], RouteSettings):

    def __init__(
        self,
        key: Optional[LocalKey] = None,
        name: Optional[str] = None,
        arguments: Optional[Object] = None,
        restoration_id: Optional[str] = None,
    ):
        super().__init__(
        )
        self.__ctor = (('',), (
            'key', key,
            'name', name,
            'arguments', arguments,
            'restorationId', restoration_id,
        ))


# packages/flutter/lib/src/widgets/navigator.dart
class Route(ABC, Generic[T], Object):

    def __init__(
        self,
        settings: Optional[RouteSettings] = None,
    ):
        self.__ctor = (('',), (
            'settings', settings,
        ))


# packages/flutter/lib/src/widgets/navigator.dart
class TransitionDelegate(ABC, Generic[T], Object):
    pass


# packages/flutter/lib/src/widgets/navigator.dart
class NavigatorObserver(Object):
    pass


# packages/flutter/lib/src/widgets/navigator.dart
class Navigator(StatefulWidget):
    default_route_name: str = '/'

    def __init__(
        self,
        key: Optional[Key] = None,
        pages: Optional[List[Page[Any]]] = None,
        on_pop_page: Optional[Callable[[Route[Any], Any], bool]] = None,
        initial_route: Optional[str] = None,
        on_generate_initial_routes: Optional[Callable[['NavigatorState', str], List[Route[Any]]]] = None,
        on_generate_route: Optional[Callable[[RouteSettings], Route[Any]]] = None,
        on_unknown_route: Optional[Callable[[RouteSettings], Route[Any]]] = None,
        transition_delegate: Optional[TransitionDelegate[Any]] = None,
        reports_route_update_to_engine: Optional[bool] = None,
        observers: Optional[List[NavigatorObserver]] = None,
        restoration_scope_id: Optional[str] = None,
    ):
        super().__init__(
        )
        self.__ctor = (('',), (
            'key', key,
            'pages', pages,
            'onPopPage', on_pop_page,
            'initialRoute', initial_route,
            'onGenerateInitialRoutes', on_generate_initial_routes,
            'onGenerateRoute', on_generate_route,
            'onUnknownRoute', on_unknown_route,
            'transitionDelegate', transition_delegate,
            'reportsRouteUpdateToEngine', reports_route_update_to_engine,
            'observers', observers,
            'restorationScopeId', restoration_scope_id,
        ))


# packages/flutter/lib/src/widgets/navigator.dart
class NavigatorState(State[Navigator]):
    pass


# packages/flutter/lib/src/material/scaffold.dart
class ScaffoldMessenger(StatefulWidget):

    def __init__(
        self,
        child: Widget,
        key: Optional[Key] = None,
    ):
        super().__init__(
        )
        self.__ctor = (('',), (
            'child', child,
            'key', key,
        ))


# packages/flutter/lib/src/material/scaffold.dart
class ScaffoldMessengerState(State[ScaffoldMessenger]):
    pass


# packages/flutter/lib/src/widgets/framework.dart
class BuildContext(ABC, Object):
    pass


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Color(Object):

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
    ):
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
    ):
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


# bin/cache/pkg/sky_engine/lib/ui/window.dart
class Brightness(Enum):
    dark = 'dark'
    light = 'light'


# packages/flutter/lib/src/material/theme_data.dart
class VisualDensity(Object):
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
VisualDensity.standard.__ctor = (('standard',),)
VisualDensity.comfortable = VisualDensity(
)
VisualDensity.comfortable.__ctor = (('comfortable',),)
VisualDensity.compact = VisualDensity(
)
VisualDensity.compact.__ctor = (('compact',),)


# packages/flutter/lib/src/painting/colors.dart
class ColorSwatch(Generic[T], Color):

    def __init__(
        self,
        primary: int,
        _swatch: Dict[T, Color],
    ):
        super().__init__(
            value=0,
        )
        self.__ctor = (('',), (
            'primary', primary,
            '_swatch', _swatch,
        ))


# packages/flutter/lib/src/material/colors.dart
class MaterialColor(ColorSwatch[int]):

    def __init__(
        self,
        primary: int,
        swatch: Dict[int, Color],
    ):
        super().__init__(
            primary=0,
            _swatch={},
        )
        self.__ctor = (('',), (
            'primary', primary,
            'swatch', swatch,
        ))


# packages/flutter/lib/src/material/ink_well.dart
class InteractiveInkFeatureFactory(ABC, Object):
    pass


# packages/flutter/lib/src/material/button_theme.dart
class ButtonTextTheme(Enum):
    normal = 'normal'
    accent = 'accent'
    primary = 'primary'


# packages/flutter/lib/src/painting/edge_insets.dart
class EdgeInsetsGeometry(ABC, Object):
    pass


EdgeInsetsGeometry.infinity = EdgeInsetsGeometry(
)
EdgeInsetsGeometry.infinity.__ctor = (('infinity',),)


# packages/flutter/lib/src/painting/borders.dart
class ShapeBorder(ABC, Object):
    pass


# packages/flutter/lib/src/material/button_theme.dart
class ButtonBarLayoutBehavior(Enum):
    constrained = 'constrained'
    padded = 'padded'


# packages/flutter/lib/src/material/color_scheme.dart
class ColorScheme(Object):

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
    ):
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
            brightness=Brightness.dark,
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
    ):
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
            brightness=Brightness.dark,
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
    ):
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
            brightness=Brightness.dark,
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
    ):
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
            brightness=Brightness.dark,
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
    ):
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
            brightness=Brightness.dark,
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
    padded = 'padded'
    shrink_wrap = 'shrinkWrap'


# packages/flutter/lib/src/material/button_theme.dart
class ButtonThemeData(Object):

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
class FontWeight(Object):
    pass


FontWeight.w100 = FontWeight(
)
FontWeight.w100.__ctor = (('w100',),)
FontWeight.w200 = FontWeight(
)
FontWeight.w200.__ctor = (('w200',),)
FontWeight.w300 = FontWeight(
)
FontWeight.w300.__ctor = (('w300',),)
FontWeight.w400 = FontWeight(
)
FontWeight.w400.__ctor = (('w400',),)
FontWeight.w500 = FontWeight(
)
FontWeight.w500.__ctor = (('w500',),)
FontWeight.w600 = FontWeight(
)
FontWeight.w600.__ctor = (('w600',),)
FontWeight.w700 = FontWeight(
)
FontWeight.w700.__ctor = (('w700',),)
FontWeight.w800 = FontWeight(
)
FontWeight.w800.__ctor = (('w800',),)
FontWeight.w900 = FontWeight(
)
FontWeight.w900.__ctor = (('w900',),)
FontWeight.normal = FontWeight(
)
FontWeight.normal.__ctor = (('normal',),)
FontWeight.bold = FontWeight(
)
FontWeight.bold.__ctor = (('bold',),)


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontStyle(Enum):
    normal = 'normal'
    italic = 'italic'


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextBaseline(Enum):
    alphabetic = 'alphabetic'
    ideographic = 'ideographic'


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextLeadingDistribution(Enum):
    proportional = 'proportional'
    even = 'even'


# bin/cache/pkg/sky_engine/lib/ui/platform_dispatcher.dart
class Locale(Object):

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
    ):
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
class Paint(Object):
    pass


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class OffsetBase(ABC, Object):

    def __init__(
        self,
        _dx: float,
        _dy: float,
    ):
        self.__ctor = (('',), (
            '_dx', _dx,
            '_dy', _dy,
        ))


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class Offset(OffsetBase):

    def __init__(
        self,
        dx: float,
        dy: float,
    ):
        super().__init__(
            _dx=0.0,
            _dy=0.0,
        )
        self.__ctor = (('',), (
            'dx', dx,
            'dy', dy,
        ))

    @staticmethod
    def from_direction(
        direction: float,
        distance: Optional[float] = None,
    ):
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
Offset.zero.__ctor = (('zero',),)
Offset.infinite = Offset(
    dx=0.0,
    dy=0.0,
)
Offset.infinite.__ctor = (('infinite',),)


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Shadow(Object):

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
class FontFeature(Object):

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
    ):
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
    ):
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
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('alternative',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def alternative_fractions(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('alternativeFractions',), (
        ))
        return _o

    @staticmethod
    def contextual_alternates(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('contextualAlternates',), (
        ))
        return _o

    @staticmethod
    def case_sensitive_forms(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('caseSensitiveForms',), (
        ))
        return _o

    @staticmethod
    def character_variant(
        value: int,
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('characterVariant',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def denominator(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('denominator',), (
        ))
        return _o

    @staticmethod
    def fractions(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('fractions',), (
        ))
        return _o

    @staticmethod
    def historical_forms(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('historicalForms',), (
        ))
        return _o

    @staticmethod
    def historical_ligatures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('historicalLigatures',), (
        ))
        return _o

    @staticmethod
    def lining_figures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('liningFigures',), (
        ))
        return _o

    @staticmethod
    def locale_aware(
        enable: Optional[bool] = None,
    ):
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
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('notationalForms',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def numerators(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('numerators',), (
        ))
        return _o

    @staticmethod
    def oldstyle_figures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('oldstyleFigures',), (
        ))
        return _o

    @staticmethod
    def ordinal_forms(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('ordinalForms',), (
        ))
        return _o

    @staticmethod
    def proportional_figures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('proportionalFigures',), (
        ))
        return _o

    @staticmethod
    def randomize(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('randomize',), (
        ))
        return _o

    @staticmethod
    def stylistic_alternates(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('stylisticAlternates',), (
        ))
        return _o

    @staticmethod
    def scientific_inferiors(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('scientificInferiors',), (
        ))
        return _o

    @staticmethod
    def stylistic_set(
        value: int,
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('stylisticSet',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def subscripts(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('subscripts',), (
        ))
        return _o

    @staticmethod
    def superscripts(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('superscripts',), (
        ))
        return _o

    @staticmethod
    def swash(
        value: Optional[int] = None,
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('swash',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def tabular_figures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('tabularFigures',), (
        ))
        return _o

    @staticmethod
    def slashed_zero(
    ):
        _o = FontFeature(
            feature='',
        )
        _o.__ctor = (('slashedZero',), (
        ))
        return _o


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextDecoration(Object):

    @staticmethod
    def combine(
        decorations: List['TextDecoration'],
    ):
        _o = TextDecoration(
        )
        _o.__ctor = (('combine',), (
            'decorations', decorations,
        ))
        return _o


TextDecoration.none = TextDecoration(
)
TextDecoration.none.__ctor = (('none',),)
TextDecoration.underline = TextDecoration(
)
TextDecoration.underline.__ctor = (('underline',),)
TextDecoration.overline = TextDecoration(
)
TextDecoration.overline.__ctor = (('overline',),)
TextDecoration.line_through = TextDecoration(
)
TextDecoration.line_through.__ctor = (('lineThrough',),)


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextDecorationStyle(Enum):
    solid = 'solid'
    float = 'double'
    dotted = 'dotted'
    dashed = 'dashed'
    wavy = 'wavy'


# packages/flutter/lib/src/painting/text_painter.dart
class TextOverflow(Enum):
    clip = 'clip'
    fade = 'fade'
    ellipsis = 'ellipsis'
    visible = 'visible'


# packages/flutter/lib/src/painting/text_style.dart
class TextStyle(Object):

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


# packages/flutter/lib/src/rendering/object.dart
class Constraints(ABC, Object):
    pass


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class Size(OffsetBase):

    def __init__(
        self,
        width: float,
        height: float,
    ):
        super().__init__(
            _dx=0.0,
            _dy=0.0,
        )
        self.__ctor = (('',), (
            'width', width,
            'height', height,
        ))

    @staticmethod
    def copy(
        source: 'Size',
    ):
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
    ):
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
    ):
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
    ):
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
    ):
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
Size.zero.__ctor = (('zero',),)
Size.infinite = Size(
    width=0.0,
    height=0.0,
)
Size.infinite.__ctor = (('infinite',),)


# packages/flutter/lib/src/rendering/box.dart
class BoxConstraints(Constraints):

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
    ):
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
    ):
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
    ):
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
    ):
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
    ):
        _o = BoxConstraints(
        )
        _o.__ctor = (('expand',), (
            'width', width,
            'height', height,
        ))
        return _o


# packages/flutter/lib/src/painting/border_radius.dart
class BorderRadiusGeometry(ABC, Object):
    pass


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class Radius(Object):

    @staticmethod
    def circular(
        radius: float,
    ):
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
    ):
        _o = Radius(
        )
        _o.__ctor = (('elliptical',), (
            'x', x,
            'y', y,
        ))
        return _o


Radius.zero = Radius(
)
Radius.zero.__ctor = (('zero',),)


# packages/flutter/lib/src/painting/border_radius.dart
class BorderRadius(BorderRadiusGeometry):

    @staticmethod
    def all(
        radius: Radius,
    ):
        _o = BorderRadius(
        )
        _o.__ctor = (('all',), (
            'radius', radius,
        ))
        return _o

    @staticmethod
    def circular(
        radius: float,
    ):
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
    ):
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
    ):
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
    ):
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
BorderRadius.zero.__ctor = (('zero',),)


# packages/flutter/lib/src/material/toggle_buttons_theme.dart
class ToggleButtonsThemeData(Object):

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
class TextTheme(Object):

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
    never = 'never'
    auto = 'auto'
    always = 'always'


# packages/flutter/lib/src/painting/borders.dart
class BorderStyle(Enum):
    none = 'none'
    solid = 'solid'


# packages/flutter/lib/src/painting/borders.dart
class BorderSide(Object):

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
BorderSide.none.__ctor = (('none',),)


# packages/flutter/lib/src/material/input_border.dart
class InputBorder(ABC, ShapeBorder):

    def __init__(
        self,
        border_side: Optional[BorderSide] = None,
    ):
        self.__ctor = (('',), (
            'borderSide', border_side,
        ))


InputBorder.none = InputBorder(
)
InputBorder.none.__ctor = (('none',),)


# packages/flutter/lib/src/material/input_decorator.dart
class InputDecorationTheme(Object):

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
class IconThemeData(Object):

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
    ):
        _o = IconThemeData(
        )
        _o.__ctor = (('fallback',), (
        ))
        return _o


# packages/flutter/lib/src/material/slider_theme.dart
class SliderComponentShape(ABC, Object):
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class SliderTickMarkShape(ABC, Object):
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class SliderTrackShape(ABC, Object):
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderTickMarkShape(ABC, Object):
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderThumbShape(ABC, Object):
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderTrackShape(ABC, Object):
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderValueIndicatorShape(ABC, Object):
    pass


# packages/flutter/lib/src/material/slider_theme.dart
class ShowValueIndicator(Enum):
    only_for_discrete = 'onlyForDiscrete'
    only_for_continuous = 'onlyForContinuous'
    always = 'always'
    never = 'never'


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextDirection(Enum):
    rtl = 'rtl'
    ltr = 'ltr'


# packages/flutter/lib/src/material/slider_theme.dart
class RangeValues(Object):

    def __init__(
        self,
        start: float,
        end: float,
    ):
        self.__ctor = (('',), (
            'start', start,
            'end', end,
        ))


# packages/flutter/lib/src/material/slider_theme.dart
class Thumb(Enum):
    start = 'start'
    end = 'end'


# packages/flutter/lib/src/material/slider_theme.dart
class SliderThemeData(Object):

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
        thumb_selector: Optional[Callable[[TextDirection, RangeValues, float, Size, Size, float], Thumb]] = None,
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
    ):
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
class Decoration(ABC, Object):
    pass


# packages/flutter/lib/src/material/tabs.dart
class TabBarIndicatorSize(Enum):
    tab = 'tab'
    label = 'label'


# packages/flutter/lib/src/material/tab_bar_theme.dart
class TabBarTheme(Object):

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


# bin/cache/pkg/sky_engine/lib/core/comparable.dart
class Comparable(ABC, Generic[T], Object):
    pass


# bin/cache/pkg/sky_engine/lib/core/duration.dart
class Duration(Object, Comparable['Duration']):
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
Duration.zero.__ctor = (('zero',),)


# packages/flutter/lib/src/material/tooltip_theme.dart
class TooltipTriggerMode(Enum):
    manual = 'manual'
    long_press = 'longPress'
    tap = 'tap'


# packages/flutter/lib/src/material/tooltip_theme.dart
class TooltipThemeData(Object):

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
    none = 'none'
    hard_edge = 'hardEdge'
    anti_alias = 'antiAlias'
    anti_alias_with_save_layer = 'antiAliasWithSaveLayer'


# packages/flutter/lib/src/material/card_theme.dart
class CardTheme(Object):

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
class OutlinedBorder(ABC, ShapeBorder):

    def __init__(
        self,
        side: Optional[BorderSide] = None,
    ):
        self.__ctor = (('',), (
            'side', side,
        ))


# packages/flutter/lib/src/material/chip_theme.dart
class ChipThemeData(Object):

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
            'disabledColor', disabled_color,
            'selectedColor', selected_color,
            'secondarySelectedColor', secondary_selected_color,
            'padding', padding,
            'labelStyle', label_style,
            'secondaryLabelStyle', secondary_label_style,
            'brightness', brightness,
            'deleteIconColor', delete_icon_color,
            'shadowColor', shadow_color,
            'selectedShadowColor', selected_shadow_color,
            'showCheckmark', show_checkmark,
            'checkmarkColor', checkmark_color,
            'labelPadding', label_padding,
            'side', side,
            'shape', shape,
            'elevation', elevation,
            'pressElevation', press_elevation,
        ))

    @staticmethod
    def from_defaults(
        secondary_color: Color,
        label_style: TextStyle,
        brightness: Optional[Brightness] = None,
        primary_color: Optional[Color] = None,
    ):
        _o = ChipThemeData(
            background_color=Color(0),
            disabled_color=Color(0),
            selected_color=Color(0),
            secondary_selected_color=Color(0),
            padding=EdgeInsetsGeometry(),
            label_style=TextStyle(),
            secondary_label_style=TextStyle(),
            brightness=Brightness.dark,
        )
        _o.__ctor = (('fromDefaults',), (
            'secondaryColor', secondary_color,
            'labelStyle', label_style,
            'brightness', brightness,
            'primaryColor', primary_color,
        ))
        return _o


# packages/flutter/lib/src/foundation/platform.dart
class TargetPlatform(Enum):
    android = 'android'
    fuchsia = 'fuchsia'
    i_os = 'iOS'
    linux = 'linux'
    mac_os = 'macOS'
    windows = 'windows'


# packages/flutter/lib/src/material/page_transitions_theme.dart
class PageTransitionsBuilder(ABC, Object):
    pass


# packages/flutter/lib/src/material/page_transitions_theme.dart
class PageTransitionsTheme(Object):

    def __init__(
        self,
        builders: Optional[Dict[TargetPlatform, PageTransitionsBuilder]] = None,
    ):
        self.__ctor = (('',), (
            'builders', builders,
        ))


# packages/flutter/lib/src/services/system_chrome.dart
class SystemUiOverlayStyle(Object):

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
SystemUiOverlayStyle.light.__ctor = (('light',),)
SystemUiOverlayStyle.dark = SystemUiOverlayStyle(
)
SystemUiOverlayStyle.dark.__ctor = (('dark',),)


# packages/flutter/lib/src/material/app_bar_theme.dart
class AppBarTheme(Object):

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
class MaterialStateProperty(ABC, Generic[T], Object):
    pass


# packages/flutter/lib/src/material/scrollbar_theme.dart
class ScrollbarThemeData(Object):

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
class NotchedShape(ABC, Object):
    pass


# packages/flutter/lib/src/material/bottom_app_bar_theme.dart
class BottomAppBarTheme(Object):

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
class DialogTheme(Object):

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
class FloatingActionButtonThemeData(Object):

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
    none = 'none'
    selected = 'selected'
    all = 'all'


# packages/flutter/lib/src/material/navigation_rail_theme.dart
class NavigationRailThemeData(Object):

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
class Typography(Object):
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
    ):
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
    ):
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
class CupertinoTextThemeData(Object):

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
class NoDefaultCupertinoThemeData(Object):

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
    fixed = 'fixed'
    floating = 'floating'


# packages/flutter/lib/src/material/snack_bar_theme.dart
class SnackBarThemeData(Object):

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
class BottomSheetThemeData(Object):

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
class PopupMenuThemeData(Object):

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
class MaterialBannerThemeData(Object):

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
class DividerThemeData(Object):

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
    start = 'start'
    end = 'end'
    center = 'center'
    space_between = 'spaceBetween'
    space_around = 'spaceAround'
    space_evenly = 'spaceEvenly'


# packages/flutter/lib/src/rendering/flex.dart
class MainAxisSize(Enum):
    min = 'min'
    max = 'max'


# packages/flutter/lib/src/painting/basic_types.dart
class VerticalDirection(Enum):
    up = 'up'
    down = 'down'


# packages/flutter/lib/src/material/button_bar_theme.dart
class ButtonBarThemeData(Object):

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
    fixed = 'fixed'
    shifting = 'shifting'


# packages/flutter/lib/src/material/bottom_navigation_bar.dart
class BottomNavigationBarLandscapeLayout(Enum):
    spread = 'spread'
    centered = 'centered'
    linear = 'linear'


# packages/flutter/lib/src/material/bottom_navigation_bar_theme.dart
class BottomNavigationBarThemeData(Object):

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
class TimePickerThemeData(Object):

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
class MouseCursor(ABC, Object):
    pass


MouseCursor.defer = MouseCursor(
)
MouseCursor.defer.__ctor = (('defer',),)
MouseCursor.uncontrolled = MouseCursor(
)
MouseCursor.uncontrolled.__ctor = (('uncontrolled',),)


# packages/flutter/lib/src/painting/alignment.dart
class AlignmentGeometry(ABC, Object):
    pass


# packages/flutter/lib/src/material/button_style.dart
class ButtonStyle(Object):

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
class TextButtonThemeData(Object):

    def __init__(
        self,
        style: Optional[ButtonStyle] = None,
    ):
        self.__ctor = (('',), (
            'style', style,
        ))


# packages/flutter/lib/src/material/elevated_button_theme.dart
class ElevatedButtonThemeData(Object):

    def __init__(
        self,
        style: Optional[ButtonStyle] = None,
    ):
        self.__ctor = (('',), (
            'style', style,
        ))


# packages/flutter/lib/src/material/outlined_button_theme.dart
class OutlinedButtonThemeData(Object):

    def __init__(
        self,
        style: Optional[ButtonStyle] = None,
    ):
        self.__ctor = (('',), (
            'style', style,
        ))


# packages/flutter/lib/src/material/text_selection_theme.dart
class TextSelectionThemeData(Object):

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
class DataTableThemeData(Object):

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
class CheckboxThemeData(Object):

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
class RadioThemeData(Object):

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
class SwitchThemeData(Object):

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
class ProgressIndicatorThemeData(Object):

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
class ThemeData(Object):

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
    ):
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
    ):
        _o = ThemeData(
        )
        _o.__ctor = (('from',), (
            'colorScheme', color_scheme,
            'textTheme', text_theme,
        ))
        return _o

    @staticmethod
    def light(
    ):
        _o = ThemeData(
        )
        _o.__ctor = (('light',), (
        ))
        return _o

    @staticmethod
    def dark(
    ):
        _o = ThemeData(
        )
        _o.__ctor = (('dark',), (
        ))
        return _o

    @staticmethod
    def fallback(
    ):
        _o = ThemeData(
        )
        _o.__ctor = (('fallback',), (
        ))
        return _o


# packages/flutter/lib/src/material/app.dart
class ThemeMode(Enum):
    system = 'system'
    light = 'light'
    dark = 'dark'


# packages/flutter/lib/src/widgets/localizations.dart
class LocalizationsDelegate(ABC, Generic[T], Object):
    pass


# packages/flutter/lib/src/widgets/shortcuts.dart
class ShortcutActivator(ABC, Object):
    pass


# packages/flutter/lib/src/widgets/actions.dart
class DoNothingIntent('Intent'):
    pass


def _intent__do_nothing_intent(_k: str) -> DoNothingIntent:
    _o = DoNothingIntent(
    )
    _o.__ctor = (('Intent', _k),)
    return _o


# packages/flutter/lib/src/widgets/actions.dart
class Intent(ABC, Object):
    do_nothing: DoNothingIntent = _intent__do_nothing_intent('doNothing')


# bin/cache/pkg/sky_engine/lib/core/type.dart
class Type(ABC, Object):
    pass


# packages/flutter/lib/src/widgets/actions.dart
class Action(ABC, Generic[T], Object):
    pass


# packages/flutter/lib/src/widgets/scroll_configuration.dart
class ScrollBehavior(Object):
    pass


# packages/flutter/lib/src/foundation/change_notifier.dart
class Listenable(ABC, Object):

    @staticmethod
    def merge(
        listenables: List['Listenable'],
    ):
        _o = Listenable(
        )
        _o.__ctor = (('merge',), (
            'listenables', listenables,
        ))
        return _o


# packages/flutter/lib/src/foundation/change_notifier.dart
class ValueListenable(ABC, Generic[T], Listenable):
    pass


# packages/flutter/lib/src/widgets/router.dart
class RouteInformation(Object):

    def __init__(
        self,
        location: Optional[str] = None,
        state: Optional[Object] = None,
    ):
        self.__ctor = (('',), (
            'location', location,
            'state', state,
        ))


# packages/flutter/lib/src/widgets/router.dart
class RouteInformationProvider(ABC, ValueListenable[RouteInformation]):
    pass


# packages/flutter/lib/src/widgets/router.dart
class RouteInformationParser(ABC, Generic[T], Object):
    pass


# packages/flutter/lib/src/widgets/router.dart
class RouterDelegate(ABC, Generic[T], Listenable):
    pass


# packages/flutter/lib/src/widgets/router.dart
class _CallbackHookProvider(Generic[T], Object):
    pass


# bin/cache/pkg/sky_engine/lib/async/future.dart
class FutureOr(ABC, Generic[T], Object):
    pass


# bin/cache/pkg/sky_engine/lib/core/stacktrace.dart
class _StringStackTrace(Object, 'StackTrace'):

    def __init__(
        self,
        _stack_trace: str,
    ):
        self.__ctor = (('',), (
            '_stackTrace', _stack_trace,
        ))


def _stack_trace___string_stack_trace(_k: str) -> _StringStackTrace:
    _o = _StringStackTrace(
        _stack_trace='',
    )
    _o.__ctor = (('StackTrace', _k),)
    return _o


# bin/cache/pkg/sky_engine/lib/core/stacktrace.dart
class StackTrace(ABC, Object):
    empty: _StringStackTrace = _stack_trace___string_stack_trace('empty')

    @staticmethod
    def from_string(
        stack_trace_string: str,
    ):
        _o = StackTrace(
        )
        _o.__ctor = (('fromString',), (
            'stackTraceString', stack_trace_string,
        ))
        return _o


# bin/cache/pkg/sky_engine/lib/async/future.dart
class Future(ABC, Generic[T], Object):

    def __init__(
        self,
        computation: Callable[[], FutureOr[T]],
    ):
        self.__ctor = (('',), (
            'computation', computation,
        ))

    @staticmethod
    def microtask(
        computation: Callable[[], FutureOr[T]],
    ):
        _o = Future(
            computation=_noop,
        )
        _o.__ctor = (('microtask',), (
            'computation', computation,
        ))
        return _o

    @staticmethod
    def sync(
        computation: Callable[[], FutureOr[T]],
    ):
        _o = Future(
            computation=_noop,
        )
        _o.__ctor = (('sync',), (
            'computation', computation,
        ))
        return _o

    @staticmethod
    def value(
        value: Optional[FutureOr[T]] = None,
    ):
        _o = Future(
            computation=_noop,
        )
        _o.__ctor = (('value',), (
            'value', value,
        ))
        return _o

    @staticmethod
    def error(
        error: Object,
        stack_trace: Optional[StackTrace] = None,
    ):
        _o = Future(
            computation=_noop,
        )
        _o.__ctor = (('error',), (
            'error', error,
            'stackTrace', stack_trace,
        ))
        return _o

    @staticmethod
    def delayed(
        duration: Duration,
        computation: Optional[Callable[[], FutureOr[T]]] = None,
    ):
        _o = Future(
            computation=_noop,
        )
        _o.__ctor = (('delayed',), (
            'duration', duration,
            'computation', computation,
        ))
        return _o


# packages/flutter/lib/src/widgets/router.dart
class BackButtonDispatcher(ABC, _CallbackHookProvider[Future[bool]]):
    pass


# packages/flutter/lib/src/material/app.dart
class MaterialApp(StatefulWidget):

    def __init__(
        self,
        key: Optional[Key] = None,
        navigator_key: Optional[GlobalKey[NavigatorState]] = None,
        scaffold_messenger_key: Optional[GlobalKey[ScaffoldMessengerState]] = None,
        home: Optional[Widget] = None,
        routes: Optional[Dict[str, Callable[[BuildContext], Widget]]] = None,
        initial_route: Optional[str] = None,
        on_generate_route: Optional[Callable[[RouteSettings], Route[Any]]] = None,
        on_generate_initial_routes: Optional[Callable[[str], List[Route[Any]]]] = None,
        on_unknown_route: Optional[Callable[[RouteSettings], Route[Any]]] = None,
        navigator_observers: Optional[List[NavigatorObserver]] = None,
        builder: Optional[Callable[[BuildContext, Widget], Widget]] = None,
        title: Optional[str] = None,
        on_generate_title: Optional[Callable[[BuildContext], str]] = None,
        color: Optional[Color] = None,
        theme: Optional[ThemeData] = None,
        dark_theme: Optional[ThemeData] = None,
        high_contrast_theme: Optional[ThemeData] = None,
        high_contrast_dark_theme: Optional[ThemeData] = None,
        theme_mode: Optional[ThemeMode] = None,
        locale: Optional[Locale] = None,
        localizations_delegates: Optional[Iterable[LocalizationsDelegate[Any]]] = None,
        locale_list_resolution_callback: Optional[Callable[[List[Locale], Iterable[Locale]], Locale]] = None,
        locale_resolution_callback: Optional[Callable[[Locale, Iterable[Locale]], Locale]] = None,
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
        super().__init__(
        )
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
        builder: Optional[Callable[[BuildContext, Widget], Widget]] = None,
        title: Optional[str] = None,
        on_generate_title: Optional[Callable[[BuildContext], str]] = None,
        color: Optional[Color] = None,
        theme: Optional[ThemeData] = None,
        dark_theme: Optional[ThemeData] = None,
        high_contrast_theme: Optional[ThemeData] = None,
        high_contrast_dark_theme: Optional[ThemeData] = None,
        theme_mode: Optional[ThemeMode] = None,
        locale: Optional[Locale] = None,
        localizations_delegates: Optional[Iterable[LocalizationsDelegate[Any]]] = None,
        locale_list_resolution_callback: Optional[Callable[[List[Locale], Iterable[Locale]], Locale]] = None,
        locale_resolution_callback: Optional[Callable[[Locale, Iterable[Locale]], Locale]] = None,
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
        _o = MaterialApp(
        )
        _o.__ctor = (('router',), (
            'routeInformationParser', route_information_parser,
            'routerDelegate', router_delegate,
            'key', key,
            'scaffoldMessengerKey', scaffold_messenger_key,
            'routeInformationProvider', route_information_provider,
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


# packages/flutter/lib/src/services/raw_keyboard.dart
class RawKeyEventData(ABC, Object):
    pass


# packages/flutter/lib/src/services/raw_keyboard.dart
class RawKeyEvent(ABC, Object):

    def __init__(
        self,
        data: RawKeyEventData,
        character: Optional[str] = None,
    ):
        self.__ctor = (('',), (
            'data', data,
            'character', character,
        ))

    @staticmethod
    def from_message(
        message: Dict[str, Any],
    ):
        _o = RawKeyEvent(
            data=RawKeyEventData(),
        )
        _o.__ctor = (('fromMessage',), (
            'message', message,
        ))
        return _o


# packages/flutter/lib/src/widgets/focus_manager.dart
class KeyEventResult(Enum):
    handled = 'handled'
    ignored = 'ignored'
    skip_remaining_handlers = 'skipRemainingHandlers'


# packages/flutter/lib/src/services/keyboard_key.dart
class KeyboardKey(ABC, Object):
    pass


# packages/flutter/lib/src/services/keyboard_key.dart
class PhysicalKeyboardKey(KeyboardKey):

    def __init__(
        self,
        usb_hid_usage: int,
    ):
        self.__ctor = (('',), (
            'usbHidUsage', usb_hid_usage,
        ))


PhysicalKeyboardKey.hyper = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.hyper.__ctor = (('hyper',),)
PhysicalKeyboardKey.super_key = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.super_key.__ctor = (('superKey',),)
PhysicalKeyboardKey.fn = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.fn.__ctor = (('fn',),)
PhysicalKeyboardKey.fn_lock = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.fn_lock.__ctor = (('fnLock',),)
PhysicalKeyboardKey.suspend = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.suspend.__ctor = (('suspend',),)
PhysicalKeyboardKey.resume = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.resume.__ctor = (('resume',),)
PhysicalKeyboardKey.turbo = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.turbo.__ctor = (('turbo',),)
PhysicalKeyboardKey.privacy_screen_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.privacy_screen_toggle.__ctor = (('privacyScreenToggle',),)
PhysicalKeyboardKey.sleep = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.sleep.__ctor = (('sleep',),)
PhysicalKeyboardKey.wake_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.wake_up.__ctor = (('wakeUp',),)
PhysicalKeyboardKey.display_toggle_int_ext = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.display_toggle_int_ext.__ctor = (('displayToggleIntExt',),)
PhysicalKeyboardKey.game_button1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button1.__ctor = (('gameButton1',),)
PhysicalKeyboardKey.game_button2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button2.__ctor = (('gameButton2',),)
PhysicalKeyboardKey.game_button3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button3.__ctor = (('gameButton3',),)
PhysicalKeyboardKey.game_button4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button4.__ctor = (('gameButton4',),)
PhysicalKeyboardKey.game_button5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button5.__ctor = (('gameButton5',),)
PhysicalKeyboardKey.game_button6 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button6.__ctor = (('gameButton6',),)
PhysicalKeyboardKey.game_button7 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button7.__ctor = (('gameButton7',),)
PhysicalKeyboardKey.game_button8 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button8.__ctor = (('gameButton8',),)
PhysicalKeyboardKey.game_button9 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button9.__ctor = (('gameButton9',),)
PhysicalKeyboardKey.game_button10 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button10.__ctor = (('gameButton10',),)
PhysicalKeyboardKey.game_button11 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button11.__ctor = (('gameButton11',),)
PhysicalKeyboardKey.game_button12 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button12.__ctor = (('gameButton12',),)
PhysicalKeyboardKey.game_button13 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button13.__ctor = (('gameButton13',),)
PhysicalKeyboardKey.game_button14 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button14.__ctor = (('gameButton14',),)
PhysicalKeyboardKey.game_button15 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button15.__ctor = (('gameButton15',),)
PhysicalKeyboardKey.game_button16 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button16.__ctor = (('gameButton16',),)
PhysicalKeyboardKey.game_button_a = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_a.__ctor = (('gameButtonA',),)
PhysicalKeyboardKey.game_button_b = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_b.__ctor = (('gameButtonB',),)
PhysicalKeyboardKey.game_button_c = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_c.__ctor = (('gameButtonC',),)
PhysicalKeyboardKey.game_button_left1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_left1.__ctor = (('gameButtonLeft1',),)
PhysicalKeyboardKey.game_button_left2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_left2.__ctor = (('gameButtonLeft2',),)
PhysicalKeyboardKey.game_button_mode = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_mode.__ctor = (('gameButtonMode',),)
PhysicalKeyboardKey.game_button_right1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_right1.__ctor = (('gameButtonRight1',),)
PhysicalKeyboardKey.game_button_right2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_right2.__ctor = (('gameButtonRight2',),)
PhysicalKeyboardKey.game_button_select = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_select.__ctor = (('gameButtonSelect',),)
PhysicalKeyboardKey.game_button_start = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_start.__ctor = (('gameButtonStart',),)
PhysicalKeyboardKey.game_button_thumb_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_thumb_left.__ctor = (('gameButtonThumbLeft',),)
PhysicalKeyboardKey.game_button_thumb_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_thumb_right.__ctor = (('gameButtonThumbRight',),)
PhysicalKeyboardKey.game_button_x = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_x.__ctor = (('gameButtonX',),)
PhysicalKeyboardKey.game_button_y = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_y.__ctor = (('gameButtonY',),)
PhysicalKeyboardKey.game_button_z = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_z.__ctor = (('gameButtonZ',),)
PhysicalKeyboardKey.usb_reserved = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.usb_reserved.__ctor = (('usbReserved',),)
PhysicalKeyboardKey.usb_error_roll_over = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.usb_error_roll_over.__ctor = (('usbErrorRollOver',),)
PhysicalKeyboardKey.usb_post_fail = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.usb_post_fail.__ctor = (('usbPostFail',),)
PhysicalKeyboardKey.usb_error_undefined = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.usb_error_undefined.__ctor = (('usbErrorUndefined',),)
PhysicalKeyboardKey.key_a = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_a.__ctor = (('keyA',),)
PhysicalKeyboardKey.key_b = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_b.__ctor = (('keyB',),)
PhysicalKeyboardKey.key_c = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_c.__ctor = (('keyC',),)
PhysicalKeyboardKey.key_d = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_d.__ctor = (('keyD',),)
PhysicalKeyboardKey.key_e = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_e.__ctor = (('keyE',),)
PhysicalKeyboardKey.key_f = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_f.__ctor = (('keyF',),)
PhysicalKeyboardKey.key_g = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_g.__ctor = (('keyG',),)
PhysicalKeyboardKey.key_h = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_h.__ctor = (('keyH',),)
PhysicalKeyboardKey.key_i = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_i.__ctor = (('keyI',),)
PhysicalKeyboardKey.key_j = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_j.__ctor = (('keyJ',),)
PhysicalKeyboardKey.key_k = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_k.__ctor = (('keyK',),)
PhysicalKeyboardKey.key_l = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_l.__ctor = (('keyL',),)
PhysicalKeyboardKey.key_m = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_m.__ctor = (('keyM',),)
PhysicalKeyboardKey.key_n = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_n.__ctor = (('keyN',),)
PhysicalKeyboardKey.key_o = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_o.__ctor = (('keyO',),)
PhysicalKeyboardKey.key_p = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_p.__ctor = (('keyP',),)
PhysicalKeyboardKey.key_q = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_q.__ctor = (('keyQ',),)
PhysicalKeyboardKey.key_r = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_r.__ctor = (('keyR',),)
PhysicalKeyboardKey.key_s = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_s.__ctor = (('keyS',),)
PhysicalKeyboardKey.key_t = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_t.__ctor = (('keyT',),)
PhysicalKeyboardKey.key_u = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_u.__ctor = (('keyU',),)
PhysicalKeyboardKey.key_v = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_v.__ctor = (('keyV',),)
PhysicalKeyboardKey.key_w = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_w.__ctor = (('keyW',),)
PhysicalKeyboardKey.key_x = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_x.__ctor = (('keyX',),)
PhysicalKeyboardKey.key_y = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_y.__ctor = (('keyY',),)
PhysicalKeyboardKey.key_z = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_z.__ctor = (('keyZ',),)
PhysicalKeyboardKey.digit1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit1.__ctor = (('digit1',),)
PhysicalKeyboardKey.digit2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit2.__ctor = (('digit2',),)
PhysicalKeyboardKey.digit3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit3.__ctor = (('digit3',),)
PhysicalKeyboardKey.digit4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit4.__ctor = (('digit4',),)
PhysicalKeyboardKey.digit5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit5.__ctor = (('digit5',),)
PhysicalKeyboardKey.digit6 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit6.__ctor = (('digit6',),)
PhysicalKeyboardKey.digit7 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit7.__ctor = (('digit7',),)
PhysicalKeyboardKey.digit8 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit8.__ctor = (('digit8',),)
PhysicalKeyboardKey.digit9 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit9.__ctor = (('digit9',),)
PhysicalKeyboardKey.digit0 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit0.__ctor = (('digit0',),)
PhysicalKeyboardKey.enter = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.enter.__ctor = (('enter',),)
PhysicalKeyboardKey.escape = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.escape.__ctor = (('escape',),)
PhysicalKeyboardKey.backspace = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.backspace.__ctor = (('backspace',),)
PhysicalKeyboardKey.tab = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.tab.__ctor = (('tab',),)
PhysicalKeyboardKey.space = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.space.__ctor = (('space',),)
PhysicalKeyboardKey.minus = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.minus.__ctor = (('minus',),)
PhysicalKeyboardKey.equal = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.equal.__ctor = (('equal',),)
PhysicalKeyboardKey.bracket_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.bracket_left.__ctor = (('bracketLeft',),)
PhysicalKeyboardKey.bracket_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.bracket_right.__ctor = (('bracketRight',),)
PhysicalKeyboardKey.backslash = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.backslash.__ctor = (('backslash',),)
PhysicalKeyboardKey.semicolon = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.semicolon.__ctor = (('semicolon',),)
PhysicalKeyboardKey.quote = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.quote.__ctor = (('quote',),)
PhysicalKeyboardKey.backquote = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.backquote.__ctor = (('backquote',),)
PhysicalKeyboardKey.comma = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.comma.__ctor = (('comma',),)
PhysicalKeyboardKey.period = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.period.__ctor = (('period',),)
PhysicalKeyboardKey.slash = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.slash.__ctor = (('slash',),)
PhysicalKeyboardKey.caps_lock = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.caps_lock.__ctor = (('capsLock',),)
PhysicalKeyboardKey.f1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f1.__ctor = (('f1',),)
PhysicalKeyboardKey.f2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f2.__ctor = (('f2',),)
PhysicalKeyboardKey.f3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f3.__ctor = (('f3',),)
PhysicalKeyboardKey.f4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f4.__ctor = (('f4',),)
PhysicalKeyboardKey.f5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f5.__ctor = (('f5',),)
PhysicalKeyboardKey.f6 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f6.__ctor = (('f6',),)
PhysicalKeyboardKey.f7 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f7.__ctor = (('f7',),)
PhysicalKeyboardKey.f8 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f8.__ctor = (('f8',),)
PhysicalKeyboardKey.f9 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f9.__ctor = (('f9',),)
PhysicalKeyboardKey.f10 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f10.__ctor = (('f10',),)
PhysicalKeyboardKey.f11 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f11.__ctor = (('f11',),)
PhysicalKeyboardKey.f12 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f12.__ctor = (('f12',),)
PhysicalKeyboardKey.print_screen = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.print_screen.__ctor = (('printScreen',),)
PhysicalKeyboardKey.scroll_lock = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.scroll_lock.__ctor = (('scrollLock',),)
PhysicalKeyboardKey.pause = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.pause.__ctor = (('pause',),)
PhysicalKeyboardKey.insert = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.insert.__ctor = (('insert',),)
PhysicalKeyboardKey.home = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.home.__ctor = (('home',),)
PhysicalKeyboardKey.page_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.page_up.__ctor = (('pageUp',),)
PhysicalKeyboardKey.delete = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.delete.__ctor = (('delete',),)
PhysicalKeyboardKey.end = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.end.__ctor = (('end',),)
PhysicalKeyboardKey.page_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.page_down.__ctor = (('pageDown',),)
PhysicalKeyboardKey.arrow_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.arrow_right.__ctor = (('arrowRight',),)
PhysicalKeyboardKey.arrow_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.arrow_left.__ctor = (('arrowLeft',),)
PhysicalKeyboardKey.arrow_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.arrow_down.__ctor = (('arrowDown',),)
PhysicalKeyboardKey.arrow_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.arrow_up.__ctor = (('arrowUp',),)
PhysicalKeyboardKey.num_lock = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.num_lock.__ctor = (('numLock',),)
PhysicalKeyboardKey.numpad_divide = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_divide.__ctor = (('numpadDivide',),)
PhysicalKeyboardKey.numpad_multiply = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_multiply.__ctor = (('numpadMultiply',),)
PhysicalKeyboardKey.numpad_subtract = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_subtract.__ctor = (('numpadSubtract',),)
PhysicalKeyboardKey.numpad_add = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_add.__ctor = (('numpadAdd',),)
PhysicalKeyboardKey.numpad_enter = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_enter.__ctor = (('numpadEnter',),)
PhysicalKeyboardKey.numpad1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad1.__ctor = (('numpad1',),)
PhysicalKeyboardKey.numpad2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad2.__ctor = (('numpad2',),)
PhysicalKeyboardKey.numpad3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad3.__ctor = (('numpad3',),)
PhysicalKeyboardKey.numpad4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad4.__ctor = (('numpad4',),)
PhysicalKeyboardKey.numpad5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad5.__ctor = (('numpad5',),)
PhysicalKeyboardKey.numpad6 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad6.__ctor = (('numpad6',),)
PhysicalKeyboardKey.numpad7 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad7.__ctor = (('numpad7',),)
PhysicalKeyboardKey.numpad8 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad8.__ctor = (('numpad8',),)
PhysicalKeyboardKey.numpad9 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad9.__ctor = (('numpad9',),)
PhysicalKeyboardKey.numpad0 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad0.__ctor = (('numpad0',),)
PhysicalKeyboardKey.numpad_decimal = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_decimal.__ctor = (('numpadDecimal',),)
PhysicalKeyboardKey.intl_backslash = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.intl_backslash.__ctor = (('intlBackslash',),)
PhysicalKeyboardKey.context_menu = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.context_menu.__ctor = (('contextMenu',),)
PhysicalKeyboardKey.power = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.power.__ctor = (('power',),)
PhysicalKeyboardKey.numpad_equal = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_equal.__ctor = (('numpadEqual',),)
PhysicalKeyboardKey.f13 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f13.__ctor = (('f13',),)
PhysicalKeyboardKey.f14 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f14.__ctor = (('f14',),)
PhysicalKeyboardKey.f15 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f15.__ctor = (('f15',),)
PhysicalKeyboardKey.f16 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f16.__ctor = (('f16',),)
PhysicalKeyboardKey.f17 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f17.__ctor = (('f17',),)
PhysicalKeyboardKey.f18 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f18.__ctor = (('f18',),)
PhysicalKeyboardKey.f19 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f19.__ctor = (('f19',),)
PhysicalKeyboardKey.f20 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f20.__ctor = (('f20',),)
PhysicalKeyboardKey.f21 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f21.__ctor = (('f21',),)
PhysicalKeyboardKey.f22 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f22.__ctor = (('f22',),)
PhysicalKeyboardKey.f23 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f23.__ctor = (('f23',),)
PhysicalKeyboardKey.f24 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f24.__ctor = (('f24',),)
PhysicalKeyboardKey.open = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.open.__ctor = (('open',),)
PhysicalKeyboardKey.help = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.help.__ctor = (('help',),)
PhysicalKeyboardKey.select = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.select.__ctor = (('select',),)
PhysicalKeyboardKey.again = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.again.__ctor = (('again',),)
PhysicalKeyboardKey.undo = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.undo.__ctor = (('undo',),)
PhysicalKeyboardKey.cut = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.cut.__ctor = (('cut',),)
PhysicalKeyboardKey.copy = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.copy.__ctor = (('copy',),)
PhysicalKeyboardKey.paste = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.paste.__ctor = (('paste',),)
PhysicalKeyboardKey.find = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.find.__ctor = (('find',),)
PhysicalKeyboardKey.audio_volume_mute = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.audio_volume_mute.__ctor = (('audioVolumeMute',),)
PhysicalKeyboardKey.audio_volume_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.audio_volume_up.__ctor = (('audioVolumeUp',),)
PhysicalKeyboardKey.audio_volume_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.audio_volume_down.__ctor = (('audioVolumeDown',),)
PhysicalKeyboardKey.numpad_comma = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_comma.__ctor = (('numpadComma',),)
PhysicalKeyboardKey.intl_ro = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.intl_ro.__ctor = (('intlRo',),)
PhysicalKeyboardKey.kana_mode = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.kana_mode.__ctor = (('kanaMode',),)
PhysicalKeyboardKey.intl_yen = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.intl_yen.__ctor = (('intlYen',),)
PhysicalKeyboardKey.convert = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.convert.__ctor = (('convert',),)
PhysicalKeyboardKey.non_convert = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.non_convert.__ctor = (('nonConvert',),)
PhysicalKeyboardKey.lang1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang1.__ctor = (('lang1',),)
PhysicalKeyboardKey.lang2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang2.__ctor = (('lang2',),)
PhysicalKeyboardKey.lang3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang3.__ctor = (('lang3',),)
PhysicalKeyboardKey.lang4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang4.__ctor = (('lang4',),)
PhysicalKeyboardKey.lang5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang5.__ctor = (('lang5',),)
PhysicalKeyboardKey.abort = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.abort.__ctor = (('abort',),)
PhysicalKeyboardKey.props = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.props.__ctor = (('props',),)
PhysicalKeyboardKey.numpad_paren_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_paren_left.__ctor = (('numpadParenLeft',),)
PhysicalKeyboardKey.numpad_paren_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_paren_right.__ctor = (('numpadParenRight',),)
PhysicalKeyboardKey.numpad_backspace = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_backspace.__ctor = (('numpadBackspace',),)
PhysicalKeyboardKey.numpad_memory_store = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_store.__ctor = (('numpadMemoryStore',),)
PhysicalKeyboardKey.numpad_memory_recall = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_recall.__ctor = (('numpadMemoryRecall',),)
PhysicalKeyboardKey.numpad_memory_clear = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_clear.__ctor = (('numpadMemoryClear',),)
PhysicalKeyboardKey.numpad_memory_add = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_add.__ctor = (('numpadMemoryAdd',),)
PhysicalKeyboardKey.numpad_memory_subtract = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_subtract.__ctor = (('numpadMemorySubtract',),)
PhysicalKeyboardKey.numpad_sign_change = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_sign_change.__ctor = (('numpadSignChange',),)
PhysicalKeyboardKey.numpad_clear = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_clear.__ctor = (('numpadClear',),)
PhysicalKeyboardKey.numpad_clear_entry = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_clear_entry.__ctor = (('numpadClearEntry',),)
PhysicalKeyboardKey.control_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.control_left.__ctor = (('controlLeft',),)
PhysicalKeyboardKey.shift_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.shift_left.__ctor = (('shiftLeft',),)
PhysicalKeyboardKey.alt_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.alt_left.__ctor = (('altLeft',),)
PhysicalKeyboardKey.meta_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.meta_left.__ctor = (('metaLeft',),)
PhysicalKeyboardKey.control_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.control_right.__ctor = (('controlRight',),)
PhysicalKeyboardKey.shift_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.shift_right.__ctor = (('shiftRight',),)
PhysicalKeyboardKey.alt_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.alt_right.__ctor = (('altRight',),)
PhysicalKeyboardKey.meta_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.meta_right.__ctor = (('metaRight',),)
PhysicalKeyboardKey.info = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.info.__ctor = (('info',),)
PhysicalKeyboardKey.closed_caption_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.closed_caption_toggle.__ctor = (('closedCaptionToggle',),)
PhysicalKeyboardKey.brightness_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_up.__ctor = (('brightnessUp',),)
PhysicalKeyboardKey.brightness_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_down.__ctor = (('brightnessDown',),)
PhysicalKeyboardKey.brightness_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_toggle.__ctor = (('brightnessToggle',),)
PhysicalKeyboardKey.brightness_minimum = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_minimum.__ctor = (('brightnessMinimum',),)
PhysicalKeyboardKey.brightness_maximum = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_maximum.__ctor = (('brightnessMaximum',),)
PhysicalKeyboardKey.brightness_auto = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_auto.__ctor = (('brightnessAuto',),)
PhysicalKeyboardKey.kbd_illum_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.kbd_illum_up.__ctor = (('kbdIllumUp',),)
PhysicalKeyboardKey.kbd_illum_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.kbd_illum_down.__ctor = (('kbdIllumDown',),)
PhysicalKeyboardKey.media_last = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_last.__ctor = (('mediaLast',),)
PhysicalKeyboardKey.launch_phone = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_phone.__ctor = (('launchPhone',),)
PhysicalKeyboardKey.program_guide = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.program_guide.__ctor = (('programGuide',),)
PhysicalKeyboardKey.exit = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.exit.__ctor = (('exit',),)
PhysicalKeyboardKey.channel_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.channel_up.__ctor = (('channelUp',),)
PhysicalKeyboardKey.channel_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.channel_down.__ctor = (('channelDown',),)
PhysicalKeyboardKey.media_play = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_play.__ctor = (('mediaPlay',),)
PhysicalKeyboardKey.media_pause = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_pause.__ctor = (('mediaPause',),)
PhysicalKeyboardKey.media_record = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_record.__ctor = (('mediaRecord',),)
PhysicalKeyboardKey.media_fast_forward = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_fast_forward.__ctor = (('mediaFastForward',),)
PhysicalKeyboardKey.media_rewind = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_rewind.__ctor = (('mediaRewind',),)
PhysicalKeyboardKey.media_track_next = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_track_next.__ctor = (('mediaTrackNext',),)
PhysicalKeyboardKey.media_track_previous = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_track_previous.__ctor = (('mediaTrackPrevious',),)
PhysicalKeyboardKey.media_stop = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_stop.__ctor = (('mediaStop',),)
PhysicalKeyboardKey.eject = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.eject.__ctor = (('eject',),)
PhysicalKeyboardKey.media_play_pause = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_play_pause.__ctor = (('mediaPlayPause',),)
PhysicalKeyboardKey.speech_input_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.speech_input_toggle.__ctor = (('speechInputToggle',),)
PhysicalKeyboardKey.bass_boost = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.bass_boost.__ctor = (('bassBoost',),)
PhysicalKeyboardKey.media_select = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_select.__ctor = (('mediaSelect',),)
PhysicalKeyboardKey.launch_word_processor = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_word_processor.__ctor = (('launchWordProcessor',),)
PhysicalKeyboardKey.launch_spreadsheet = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_spreadsheet.__ctor = (('launchSpreadsheet',),)
PhysicalKeyboardKey.launch_mail = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_mail.__ctor = (('launchMail',),)
PhysicalKeyboardKey.launch_contacts = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_contacts.__ctor = (('launchContacts',),)
PhysicalKeyboardKey.launch_calendar = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_calendar.__ctor = (('launchCalendar',),)
PhysicalKeyboardKey.launch_app2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_app2.__ctor = (('launchApp2',),)
PhysicalKeyboardKey.launch_app1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_app1.__ctor = (('launchApp1',),)
PhysicalKeyboardKey.launch_internet_browser = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_internet_browser.__ctor = (('launchInternetBrowser',),)
PhysicalKeyboardKey.log_off = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.log_off.__ctor = (('logOff',),)
PhysicalKeyboardKey.lock_screen = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lock_screen.__ctor = (('lockScreen',),)
PhysicalKeyboardKey.launch_control_panel = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_control_panel.__ctor = (('launchControlPanel',),)
PhysicalKeyboardKey.select_task = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.select_task.__ctor = (('selectTask',),)
PhysicalKeyboardKey.launch_documents = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_documents.__ctor = (('launchDocuments',),)
PhysicalKeyboardKey.spell_check = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.spell_check.__ctor = (('spellCheck',),)
PhysicalKeyboardKey.launch_keyboard_layout = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_keyboard_layout.__ctor = (('launchKeyboardLayout',),)
PhysicalKeyboardKey.launch_screen_saver = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_screen_saver.__ctor = (('launchScreenSaver',),)
PhysicalKeyboardKey.launch_audio_browser = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_audio_browser.__ctor = (('launchAudioBrowser',),)
PhysicalKeyboardKey.launch_assistant = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_assistant.__ctor = (('launchAssistant',),)
PhysicalKeyboardKey.new_key = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.new_key.__ctor = (('newKey',),)
PhysicalKeyboardKey.close = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.close.__ctor = (('close',),)
PhysicalKeyboardKey.save = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.save.__ctor = (('save',),)
PhysicalKeyboardKey.print = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.print.__ctor = (('print',),)
PhysicalKeyboardKey.browser_search = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_search.__ctor = (('browserSearch',),)
PhysicalKeyboardKey.browser_home = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_home.__ctor = (('browserHome',),)
PhysicalKeyboardKey.browser_back = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_back.__ctor = (('browserBack',),)
PhysicalKeyboardKey.browser_forward = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_forward.__ctor = (('browserForward',),)
PhysicalKeyboardKey.browser_stop = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_stop.__ctor = (('browserStop',),)
PhysicalKeyboardKey.browser_refresh = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_refresh.__ctor = (('browserRefresh',),)
PhysicalKeyboardKey.browser_favorites = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_favorites.__ctor = (('browserFavorites',),)
PhysicalKeyboardKey.zoom_in = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.zoom_in.__ctor = (('zoomIn',),)
PhysicalKeyboardKey.zoom_out = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.zoom_out.__ctor = (('zoomOut',),)
PhysicalKeyboardKey.zoom_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.zoom_toggle.__ctor = (('zoomToggle',),)
PhysicalKeyboardKey.redo = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.redo.__ctor = (('redo',),)
PhysicalKeyboardKey.mail_reply = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.mail_reply.__ctor = (('mailReply',),)
PhysicalKeyboardKey.mail_forward = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.mail_forward.__ctor = (('mailForward',),)
PhysicalKeyboardKey.mail_send = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.mail_send.__ctor = (('mailSend',),)
PhysicalKeyboardKey.keyboard_layout_select = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.keyboard_layout_select.__ctor = (('keyboardLayoutSelect',),)
PhysicalKeyboardKey.show_all_windows = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.show_all_windows.__ctor = (('showAllWindows',),)


# packages/flutter/lib/src/services/keyboard_key.dart
class LogicalKeyboardKey(KeyboardKey):
    value_mask: int = 4294967295
    plane_mask: int = 1095216660480
    unicode_plane: int = 0
    unprintable_plane: int = 4294967296
    flutter_plane: int = 8589934592
    start_of_platform_planes: int = 73014444032
    android_plane: int = 73014444032
    fuchsia_plane: int = 77309411328
    ios_plane: int = 81604378624
    macos_plane: int = 85899345920
    gtk_plane: int = 90194313216
    windows_plane: int = 94489280512
    web_plane: int = 98784247808
    glfw_plane: int = 103079215104

    def __init__(
        self,
        key_id: int,
    ):
        self.__ctor = (('',), (
            'keyId', key_id,
        ))


LogicalKeyboardKey.space = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.space.__ctor = (('space',),)
LogicalKeyboardKey.exclamation = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.exclamation.__ctor = (('exclamation',),)
LogicalKeyboardKey.quote = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.quote.__ctor = (('quote',),)
LogicalKeyboardKey.number_sign = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.number_sign.__ctor = (('numberSign',),)
LogicalKeyboardKey.dollar = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.dollar.__ctor = (('dollar',),)
LogicalKeyboardKey.percent = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.percent.__ctor = (('percent',),)
LogicalKeyboardKey.ampersand = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.ampersand.__ctor = (('ampersand',),)
LogicalKeyboardKey.quote_single = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.quote_single.__ctor = (('quoteSingle',),)
LogicalKeyboardKey.parenthesis_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.parenthesis_left.__ctor = (('parenthesisLeft',),)
LogicalKeyboardKey.parenthesis_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.parenthesis_right.__ctor = (('parenthesisRight',),)
LogicalKeyboardKey.asterisk = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.asterisk.__ctor = (('asterisk',),)
LogicalKeyboardKey.add = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.add.__ctor = (('add',),)
LogicalKeyboardKey.comma = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.comma.__ctor = (('comma',),)
LogicalKeyboardKey.minus = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.minus.__ctor = (('minus',),)
LogicalKeyboardKey.period = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.period.__ctor = (('period',),)
LogicalKeyboardKey.slash = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.slash.__ctor = (('slash',),)
LogicalKeyboardKey.digit0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit0.__ctor = (('digit0',),)
LogicalKeyboardKey.digit1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit1.__ctor = (('digit1',),)
LogicalKeyboardKey.digit2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit2.__ctor = (('digit2',),)
LogicalKeyboardKey.digit3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit3.__ctor = (('digit3',),)
LogicalKeyboardKey.digit4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit4.__ctor = (('digit4',),)
LogicalKeyboardKey.digit5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit5.__ctor = (('digit5',),)
LogicalKeyboardKey.digit6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit6.__ctor = (('digit6',),)
LogicalKeyboardKey.digit7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit7.__ctor = (('digit7',),)
LogicalKeyboardKey.digit8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit8.__ctor = (('digit8',),)
LogicalKeyboardKey.digit9 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit9.__ctor = (('digit9',),)
LogicalKeyboardKey.colon = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.colon.__ctor = (('colon',),)
LogicalKeyboardKey.semicolon = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.semicolon.__ctor = (('semicolon',),)
LogicalKeyboardKey.less = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.less.__ctor = (('less',),)
LogicalKeyboardKey.equal = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.equal.__ctor = (('equal',),)
LogicalKeyboardKey.greater = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.greater.__ctor = (('greater',),)
LogicalKeyboardKey.question = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.question.__ctor = (('question',),)
LogicalKeyboardKey.at = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.at.__ctor = (('at',),)
LogicalKeyboardKey.bracket_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.bracket_left.__ctor = (('bracketLeft',),)
LogicalKeyboardKey.backslash = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.backslash.__ctor = (('backslash',),)
LogicalKeyboardKey.bracket_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.bracket_right.__ctor = (('bracketRight',),)
LogicalKeyboardKey.caret = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.caret.__ctor = (('caret',),)
LogicalKeyboardKey.underscore = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.underscore.__ctor = (('underscore',),)
LogicalKeyboardKey.backquote = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.backquote.__ctor = (('backquote',),)
LogicalKeyboardKey.key_a = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_a.__ctor = (('keyA',),)
LogicalKeyboardKey.key_b = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_b.__ctor = (('keyB',),)
LogicalKeyboardKey.key_c = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_c.__ctor = (('keyC',),)
LogicalKeyboardKey.key_d = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_d.__ctor = (('keyD',),)
LogicalKeyboardKey.key_e = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_e.__ctor = (('keyE',),)
LogicalKeyboardKey.key_f = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_f.__ctor = (('keyF',),)
LogicalKeyboardKey.key_g = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_g.__ctor = (('keyG',),)
LogicalKeyboardKey.key_h = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_h.__ctor = (('keyH',),)
LogicalKeyboardKey.key_i = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_i.__ctor = (('keyI',),)
LogicalKeyboardKey.key_j = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_j.__ctor = (('keyJ',),)
LogicalKeyboardKey.key_k = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_k.__ctor = (('keyK',),)
LogicalKeyboardKey.key_l = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_l.__ctor = (('keyL',),)
LogicalKeyboardKey.key_m = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_m.__ctor = (('keyM',),)
LogicalKeyboardKey.key_n = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_n.__ctor = (('keyN',),)
LogicalKeyboardKey.key_o = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_o.__ctor = (('keyO',),)
LogicalKeyboardKey.key_p = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_p.__ctor = (('keyP',),)
LogicalKeyboardKey.key_q = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_q.__ctor = (('keyQ',),)
LogicalKeyboardKey.key_r = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_r.__ctor = (('keyR',),)
LogicalKeyboardKey.key_s = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_s.__ctor = (('keyS',),)
LogicalKeyboardKey.key_t = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_t.__ctor = (('keyT',),)
LogicalKeyboardKey.key_u = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_u.__ctor = (('keyU',),)
LogicalKeyboardKey.key_v = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_v.__ctor = (('keyV',),)
LogicalKeyboardKey.key_w = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_w.__ctor = (('keyW',),)
LogicalKeyboardKey.key_x = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_x.__ctor = (('keyX',),)
LogicalKeyboardKey.key_y = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_y.__ctor = (('keyY',),)
LogicalKeyboardKey.key_z = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_z.__ctor = (('keyZ',),)
LogicalKeyboardKey.brace_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.brace_left.__ctor = (('braceLeft',),)
LogicalKeyboardKey.bar = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.bar.__ctor = (('bar',),)
LogicalKeyboardKey.brace_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.brace_right.__ctor = (('braceRight',),)
LogicalKeyboardKey.tilde = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tilde.__ctor = (('tilde',),)
LogicalKeyboardKey.unidentified = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.unidentified.__ctor = (('unidentified',),)
LogicalKeyboardKey.backspace = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.backspace.__ctor = (('backspace',),)
LogicalKeyboardKey.tab = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tab.__ctor = (('tab',),)
LogicalKeyboardKey.enter = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.enter.__ctor = (('enter',),)
LogicalKeyboardKey.escape = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.escape.__ctor = (('escape',),)
LogicalKeyboardKey.delete = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.delete.__ctor = (('delete',),)
LogicalKeyboardKey.accel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.accel.__ctor = (('accel',),)
LogicalKeyboardKey.alt_graph = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alt_graph.__ctor = (('altGraph',),)
LogicalKeyboardKey.caps_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.caps_lock.__ctor = (('capsLock',),)
LogicalKeyboardKey.fn = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.fn.__ctor = (('fn',),)
LogicalKeyboardKey.fn_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.fn_lock.__ctor = (('fnLock',),)
LogicalKeyboardKey.hyper = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hyper.__ctor = (('hyper',),)
LogicalKeyboardKey.num_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.num_lock.__ctor = (('numLock',),)
LogicalKeyboardKey.scroll_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.scroll_lock.__ctor = (('scrollLock',),)
LogicalKeyboardKey.super_key = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.super_key.__ctor = (('superKey',),)
LogicalKeyboardKey.symbol = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.symbol.__ctor = (('symbol',),)
LogicalKeyboardKey.symbol_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.symbol_lock.__ctor = (('symbolLock',),)
LogicalKeyboardKey.shift_level5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.shift_level5.__ctor = (('shiftLevel5',),)
LogicalKeyboardKey.arrow_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.arrow_down.__ctor = (('arrowDown',),)
LogicalKeyboardKey.arrow_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.arrow_left.__ctor = (('arrowLeft',),)
LogicalKeyboardKey.arrow_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.arrow_right.__ctor = (('arrowRight',),)
LogicalKeyboardKey.arrow_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.arrow_up.__ctor = (('arrowUp',),)
LogicalKeyboardKey.end = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.end.__ctor = (('end',),)
LogicalKeyboardKey.home = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.home.__ctor = (('home',),)
LogicalKeyboardKey.page_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.page_down.__ctor = (('pageDown',),)
LogicalKeyboardKey.page_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.page_up.__ctor = (('pageUp',),)
LogicalKeyboardKey.clear = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.clear.__ctor = (('clear',),)
LogicalKeyboardKey.copy = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.copy.__ctor = (('copy',),)
LogicalKeyboardKey.cr_sel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.cr_sel.__ctor = (('crSel',),)
LogicalKeyboardKey.cut = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.cut.__ctor = (('cut',),)
LogicalKeyboardKey.erase_eof = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.erase_eof.__ctor = (('eraseEof',),)
LogicalKeyboardKey.ex_sel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.ex_sel.__ctor = (('exSel',),)
LogicalKeyboardKey.insert = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.insert.__ctor = (('insert',),)
LogicalKeyboardKey.paste = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.paste.__ctor = (('paste',),)
LogicalKeyboardKey.redo = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.redo.__ctor = (('redo',),)
LogicalKeyboardKey.undo = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.undo.__ctor = (('undo',),)
LogicalKeyboardKey.accept = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.accept.__ctor = (('accept',),)
LogicalKeyboardKey.again = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.again.__ctor = (('again',),)
LogicalKeyboardKey.attn = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.attn.__ctor = (('attn',),)
LogicalKeyboardKey.cancel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.cancel.__ctor = (('cancel',),)
LogicalKeyboardKey.context_menu = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.context_menu.__ctor = (('contextMenu',),)
LogicalKeyboardKey.execute = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.execute.__ctor = (('execute',),)
LogicalKeyboardKey.find = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.find.__ctor = (('find',),)
LogicalKeyboardKey.help = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.help.__ctor = (('help',),)
LogicalKeyboardKey.pause = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.pause.__ctor = (('pause',),)
LogicalKeyboardKey.play = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.play.__ctor = (('play',),)
LogicalKeyboardKey.props = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.props.__ctor = (('props',),)
LogicalKeyboardKey.select = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.select.__ctor = (('select',),)
LogicalKeyboardKey.zoom_in = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zoom_in.__ctor = (('zoomIn',),)
LogicalKeyboardKey.zoom_out = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zoom_out.__ctor = (('zoomOut',),)
LogicalKeyboardKey.brightness_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.brightness_down.__ctor = (('brightnessDown',),)
LogicalKeyboardKey.brightness_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.brightness_up.__ctor = (('brightnessUp',),)
LogicalKeyboardKey.camera = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.camera.__ctor = (('camera',),)
LogicalKeyboardKey.eject = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.eject.__ctor = (('eject',),)
LogicalKeyboardKey.log_off = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.log_off.__ctor = (('logOff',),)
LogicalKeyboardKey.power = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.power.__ctor = (('power',),)
LogicalKeyboardKey.power_off = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.power_off.__ctor = (('powerOff',),)
LogicalKeyboardKey.print_screen = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.print_screen.__ctor = (('printScreen',),)
LogicalKeyboardKey.hibernate = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hibernate.__ctor = (('hibernate',),)
LogicalKeyboardKey.standby = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.standby.__ctor = (('standby',),)
LogicalKeyboardKey.wake_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.wake_up.__ctor = (('wakeUp',),)
LogicalKeyboardKey.all_candidates = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.all_candidates.__ctor = (('allCandidates',),)
LogicalKeyboardKey.alphanumeric = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alphanumeric.__ctor = (('alphanumeric',),)
LogicalKeyboardKey.code_input = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.code_input.__ctor = (('codeInput',),)
LogicalKeyboardKey.compose = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.compose.__ctor = (('compose',),)
LogicalKeyboardKey.convert = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.convert.__ctor = (('convert',),)
LogicalKeyboardKey.final_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.final_mode.__ctor = (('finalMode',),)
LogicalKeyboardKey.group_first = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.group_first.__ctor = (('groupFirst',),)
LogicalKeyboardKey.group_last = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.group_last.__ctor = (('groupLast',),)
LogicalKeyboardKey.group_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.group_next.__ctor = (('groupNext',),)
LogicalKeyboardKey.group_previous = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.group_previous.__ctor = (('groupPrevious',),)
LogicalKeyboardKey.mode_change = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.mode_change.__ctor = (('modeChange',),)
LogicalKeyboardKey.next_candidate = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.next_candidate.__ctor = (('nextCandidate',),)
LogicalKeyboardKey.non_convert = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.non_convert.__ctor = (('nonConvert',),)
LogicalKeyboardKey.previous_candidate = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.previous_candidate.__ctor = (('previousCandidate',),)
LogicalKeyboardKey.process = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.process.__ctor = (('process',),)
LogicalKeyboardKey.single_candidate = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.single_candidate.__ctor = (('singleCandidate',),)
LogicalKeyboardKey.hangul_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hangul_mode.__ctor = (('hangulMode',),)
LogicalKeyboardKey.hanja_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hanja_mode.__ctor = (('hanjaMode',),)
LogicalKeyboardKey.junja_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.junja_mode.__ctor = (('junjaMode',),)
LogicalKeyboardKey.eisu = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.eisu.__ctor = (('eisu',),)
LogicalKeyboardKey.hankaku = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hankaku.__ctor = (('hankaku',),)
LogicalKeyboardKey.hiragana = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hiragana.__ctor = (('hiragana',),)
LogicalKeyboardKey.hiragana_katakana = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hiragana_katakana.__ctor = (('hiraganaKatakana',),)
LogicalKeyboardKey.kana_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.kana_mode.__ctor = (('kanaMode',),)
LogicalKeyboardKey.kanji_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.kanji_mode.__ctor = (('kanjiMode',),)
LogicalKeyboardKey.katakana = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.katakana.__ctor = (('katakana',),)
LogicalKeyboardKey.romaji = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.romaji.__ctor = (('romaji',),)
LogicalKeyboardKey.zenkaku = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zenkaku.__ctor = (('zenkaku',),)
LogicalKeyboardKey.zenkaku_hankaku = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zenkaku_hankaku.__ctor = (('zenkakuHankaku',),)
LogicalKeyboardKey.f1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f1.__ctor = (('f1',),)
LogicalKeyboardKey.f2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f2.__ctor = (('f2',),)
LogicalKeyboardKey.f3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f3.__ctor = (('f3',),)
LogicalKeyboardKey.f4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f4.__ctor = (('f4',),)
LogicalKeyboardKey.f5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f5.__ctor = (('f5',),)
LogicalKeyboardKey.f6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f6.__ctor = (('f6',),)
LogicalKeyboardKey.f7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f7.__ctor = (('f7',),)
LogicalKeyboardKey.f8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f8.__ctor = (('f8',),)
LogicalKeyboardKey.f9 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f9.__ctor = (('f9',),)
LogicalKeyboardKey.f10 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f10.__ctor = (('f10',),)
LogicalKeyboardKey.f11 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f11.__ctor = (('f11',),)
LogicalKeyboardKey.f12 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f12.__ctor = (('f12',),)
LogicalKeyboardKey.f13 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f13.__ctor = (('f13',),)
LogicalKeyboardKey.f14 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f14.__ctor = (('f14',),)
LogicalKeyboardKey.f15 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f15.__ctor = (('f15',),)
LogicalKeyboardKey.f16 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f16.__ctor = (('f16',),)
LogicalKeyboardKey.f17 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f17.__ctor = (('f17',),)
LogicalKeyboardKey.f18 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f18.__ctor = (('f18',),)
LogicalKeyboardKey.f19 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f19.__ctor = (('f19',),)
LogicalKeyboardKey.f20 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f20.__ctor = (('f20',),)
LogicalKeyboardKey.f21 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f21.__ctor = (('f21',),)
LogicalKeyboardKey.f22 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f22.__ctor = (('f22',),)
LogicalKeyboardKey.f23 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f23.__ctor = (('f23',),)
LogicalKeyboardKey.f24 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f24.__ctor = (('f24',),)
LogicalKeyboardKey.soft1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft1.__ctor = (('soft1',),)
LogicalKeyboardKey.soft2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft2.__ctor = (('soft2',),)
LogicalKeyboardKey.soft3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft3.__ctor = (('soft3',),)
LogicalKeyboardKey.soft4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft4.__ctor = (('soft4',),)
LogicalKeyboardKey.soft5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft5.__ctor = (('soft5',),)
LogicalKeyboardKey.soft6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft6.__ctor = (('soft6',),)
LogicalKeyboardKey.soft7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft7.__ctor = (('soft7',),)
LogicalKeyboardKey.soft8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft8.__ctor = (('soft8',),)
LogicalKeyboardKey.close = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.close.__ctor = (('close',),)
LogicalKeyboardKey.mail_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.mail_forward.__ctor = (('mailForward',),)
LogicalKeyboardKey.mail_reply = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.mail_reply.__ctor = (('mailReply',),)
LogicalKeyboardKey.mail_send = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.mail_send.__ctor = (('mailSend',),)
LogicalKeyboardKey.media_play_pause = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_play_pause.__ctor = (('mediaPlayPause',),)
LogicalKeyboardKey.media_stop = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_stop.__ctor = (('mediaStop',),)
LogicalKeyboardKey.media_track_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_track_next.__ctor = (('mediaTrackNext',),)
LogicalKeyboardKey.media_track_previous = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_track_previous.__ctor = (('mediaTrackPrevious',),)
LogicalKeyboardKey.new_key = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.new_key.__ctor = (('newKey',),)
LogicalKeyboardKey.open = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.open.__ctor = (('open',),)
LogicalKeyboardKey.print = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.print.__ctor = (('print',),)
LogicalKeyboardKey.save = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.save.__ctor = (('save',),)
LogicalKeyboardKey.spell_check = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.spell_check.__ctor = (('spellCheck',),)
LogicalKeyboardKey.audio_volume_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_volume_down.__ctor = (('audioVolumeDown',),)
LogicalKeyboardKey.audio_volume_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_volume_up.__ctor = (('audioVolumeUp',),)
LogicalKeyboardKey.audio_volume_mute = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_volume_mute.__ctor = (('audioVolumeMute',),)
LogicalKeyboardKey.launch_application2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_application2.__ctor = (('launchApplication2',),)
LogicalKeyboardKey.launch_calendar = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_calendar.__ctor = (('launchCalendar',),)
LogicalKeyboardKey.launch_mail = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_mail.__ctor = (('launchMail',),)
LogicalKeyboardKey.launch_media_player = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_media_player.__ctor = (('launchMediaPlayer',),)
LogicalKeyboardKey.launch_music_player = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_music_player.__ctor = (('launchMusicPlayer',),)
LogicalKeyboardKey.launch_application1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_application1.__ctor = (('launchApplication1',),)
LogicalKeyboardKey.launch_screen_saver = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_screen_saver.__ctor = (('launchScreenSaver',),)
LogicalKeyboardKey.launch_spreadsheet = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_spreadsheet.__ctor = (('launchSpreadsheet',),)
LogicalKeyboardKey.launch_web_browser = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_web_browser.__ctor = (('launchWebBrowser',),)
LogicalKeyboardKey.launch_web_cam = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_web_cam.__ctor = (('launchWebCam',),)
LogicalKeyboardKey.launch_word_processor = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_word_processor.__ctor = (('launchWordProcessor',),)
LogicalKeyboardKey.launch_contacts = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_contacts.__ctor = (('launchContacts',),)
LogicalKeyboardKey.launch_phone = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_phone.__ctor = (('launchPhone',),)
LogicalKeyboardKey.launch_assistant = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_assistant.__ctor = (('launchAssistant',),)
LogicalKeyboardKey.launch_control_panel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_control_panel.__ctor = (('launchControlPanel',),)
LogicalKeyboardKey.browser_back = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_back.__ctor = (('browserBack',),)
LogicalKeyboardKey.browser_favorites = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_favorites.__ctor = (('browserFavorites',),)
LogicalKeyboardKey.browser_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_forward.__ctor = (('browserForward',),)
LogicalKeyboardKey.browser_home = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_home.__ctor = (('browserHome',),)
LogicalKeyboardKey.browser_refresh = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_refresh.__ctor = (('browserRefresh',),)
LogicalKeyboardKey.browser_search = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_search.__ctor = (('browserSearch',),)
LogicalKeyboardKey.browser_stop = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_stop.__ctor = (('browserStop',),)
LogicalKeyboardKey.audio_balance_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_balance_left.__ctor = (('audioBalanceLeft',),)
LogicalKeyboardKey.audio_balance_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_balance_right.__ctor = (('audioBalanceRight',),)
LogicalKeyboardKey.audio_bass_boost_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_bass_boost_down.__ctor = (('audioBassBoostDown',),)
LogicalKeyboardKey.audio_bass_boost_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_bass_boost_up.__ctor = (('audioBassBoostUp',),)
LogicalKeyboardKey.audio_fader_front = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_fader_front.__ctor = (('audioFaderFront',),)
LogicalKeyboardKey.audio_fader_rear = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_fader_rear.__ctor = (('audioFaderRear',),)
LogicalKeyboardKey.audio_surround_mode_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_surround_mode_next.__ctor = (('audioSurroundModeNext',),)
LogicalKeyboardKey.avr_input = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.avr_input.__ctor = (('avrInput',),)
LogicalKeyboardKey.avr_power = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.avr_power.__ctor = (('avrPower',),)
LogicalKeyboardKey.channel_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.channel_down.__ctor = (('channelDown',),)
LogicalKeyboardKey.channel_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.channel_up.__ctor = (('channelUp',),)
LogicalKeyboardKey.color_f0_red = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f0_red.__ctor = (('colorF0Red',),)
LogicalKeyboardKey.color_f1_green = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f1_green.__ctor = (('colorF1Green',),)
LogicalKeyboardKey.color_f2_yellow = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f2_yellow.__ctor = (('colorF2Yellow',),)
LogicalKeyboardKey.color_f3_blue = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f3_blue.__ctor = (('colorF3Blue',),)
LogicalKeyboardKey.color_f4_grey = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f4_grey.__ctor = (('colorF4Grey',),)
LogicalKeyboardKey.color_f5_brown = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f5_brown.__ctor = (('colorF5Brown',),)
LogicalKeyboardKey.closed_caption_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.closed_caption_toggle.__ctor = (('closedCaptionToggle',),)
LogicalKeyboardKey.dimmer = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.dimmer.__ctor = (('dimmer',),)
LogicalKeyboardKey.display_swap = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.display_swap.__ctor = (('displaySwap',),)
LogicalKeyboardKey.exit = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.exit.__ctor = (('exit',),)
LogicalKeyboardKey.favorite_clear0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_clear0.__ctor = (('favoriteClear0',),)
LogicalKeyboardKey.favorite_clear1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_clear1.__ctor = (('favoriteClear1',),)
LogicalKeyboardKey.favorite_clear2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_clear2.__ctor = (('favoriteClear2',),)
LogicalKeyboardKey.favorite_clear3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_clear3.__ctor = (('favoriteClear3',),)
LogicalKeyboardKey.favorite_recall0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_recall0.__ctor = (('favoriteRecall0',),)
LogicalKeyboardKey.favorite_recall1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_recall1.__ctor = (('favoriteRecall1',),)
LogicalKeyboardKey.favorite_recall2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_recall2.__ctor = (('favoriteRecall2',),)
LogicalKeyboardKey.favorite_recall3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_recall3.__ctor = (('favoriteRecall3',),)
LogicalKeyboardKey.favorite_store0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_store0.__ctor = (('favoriteStore0',),)
LogicalKeyboardKey.favorite_store1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_store1.__ctor = (('favoriteStore1',),)
LogicalKeyboardKey.favorite_store2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_store2.__ctor = (('favoriteStore2',),)
LogicalKeyboardKey.favorite_store3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_store3.__ctor = (('favoriteStore3',),)
LogicalKeyboardKey.guide = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.guide.__ctor = (('guide',),)
LogicalKeyboardKey.guide_next_day = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.guide_next_day.__ctor = (('guideNextDay',),)
LogicalKeyboardKey.guide_previous_day = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.guide_previous_day.__ctor = (('guidePreviousDay',),)
LogicalKeyboardKey.info = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.info.__ctor = (('info',),)
LogicalKeyboardKey.instant_replay = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.instant_replay.__ctor = (('instantReplay',),)
LogicalKeyboardKey.link = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.link.__ctor = (('link',),)
LogicalKeyboardKey.list_program = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.list_program.__ctor = (('listProgram',),)
LogicalKeyboardKey.live_content = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.live_content.__ctor = (('liveContent',),)
LogicalKeyboardKey.lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lock.__ctor = (('lock',),)
LogicalKeyboardKey.media_apps = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_apps.__ctor = (('mediaApps',),)
LogicalKeyboardKey.media_fast_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_fast_forward.__ctor = (('mediaFastForward',),)
LogicalKeyboardKey.media_last = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_last.__ctor = (('mediaLast',),)
LogicalKeyboardKey.media_pause = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_pause.__ctor = (('mediaPause',),)
LogicalKeyboardKey.media_play = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_play.__ctor = (('mediaPlay',),)
LogicalKeyboardKey.media_record = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_record.__ctor = (('mediaRecord',),)
LogicalKeyboardKey.media_rewind = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_rewind.__ctor = (('mediaRewind',),)
LogicalKeyboardKey.media_skip = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_skip.__ctor = (('mediaSkip',),)
LogicalKeyboardKey.next_favorite_channel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.next_favorite_channel.__ctor = (('nextFavoriteChannel',),)
LogicalKeyboardKey.next_user_profile = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.next_user_profile.__ctor = (('nextUserProfile',),)
LogicalKeyboardKey.on_demand = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.on_demand.__ctor = (('onDemand',),)
LogicalKeyboardKey.p_in_pdown = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.p_in_pdown.__ctor = (('pInPDown',),)
LogicalKeyboardKey.p_in_pmove = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.p_in_pmove.__ctor = (('pInPMove',),)
LogicalKeyboardKey.p_in_ptoggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.p_in_ptoggle.__ctor = (('pInPToggle',),)
LogicalKeyboardKey.p_in_pup = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.p_in_pup.__ctor = (('pInPUp',),)
LogicalKeyboardKey.play_speed_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.play_speed_down.__ctor = (('playSpeedDown',),)
LogicalKeyboardKey.play_speed_reset = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.play_speed_reset.__ctor = (('playSpeedReset',),)
LogicalKeyboardKey.play_speed_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.play_speed_up.__ctor = (('playSpeedUp',),)
LogicalKeyboardKey.random_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.random_toggle.__ctor = (('randomToggle',),)
LogicalKeyboardKey.rc_low_battery = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.rc_low_battery.__ctor = (('rcLowBattery',),)
LogicalKeyboardKey.record_speed_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.record_speed_next.__ctor = (('recordSpeedNext',),)
LogicalKeyboardKey.rf_bypass = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.rf_bypass.__ctor = (('rfBypass',),)
LogicalKeyboardKey.scan_channels_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.scan_channels_toggle.__ctor = (('scanChannelsToggle',),)
LogicalKeyboardKey.screen_mode_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.screen_mode_next.__ctor = (('screenModeNext',),)
LogicalKeyboardKey.settings = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.settings.__ctor = (('settings',),)
LogicalKeyboardKey.split_screen_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.split_screen_toggle.__ctor = (('splitScreenToggle',),)
LogicalKeyboardKey.stb_input = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.stb_input.__ctor = (('stbInput',),)
LogicalKeyboardKey.stb_power = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.stb_power.__ctor = (('stbPower',),)
LogicalKeyboardKey.subtitle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.subtitle.__ctor = (('subtitle',),)
LogicalKeyboardKey.teletext = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.teletext.__ctor = (('teletext',),)
LogicalKeyboardKey.tv = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv.__ctor = (('tv',),)
LogicalKeyboardKey.tv_input = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input.__ctor = (('tvInput',),)
LogicalKeyboardKey.tv_power = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_power.__ctor = (('tvPower',),)
LogicalKeyboardKey.video_mode_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.video_mode_next.__ctor = (('videoModeNext',),)
LogicalKeyboardKey.wink = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.wink.__ctor = (('wink',),)
LogicalKeyboardKey.zoom_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zoom_toggle.__ctor = (('zoomToggle',),)
LogicalKeyboardKey.dvr = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.dvr.__ctor = (('dvr',),)
LogicalKeyboardKey.media_audio_track = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_audio_track.__ctor = (('mediaAudioTrack',),)
LogicalKeyboardKey.media_skip_backward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_skip_backward.__ctor = (('mediaSkipBackward',),)
LogicalKeyboardKey.media_skip_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_skip_forward.__ctor = (('mediaSkipForward',),)
LogicalKeyboardKey.media_step_backward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_step_backward.__ctor = (('mediaStepBackward',),)
LogicalKeyboardKey.media_step_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_step_forward.__ctor = (('mediaStepForward',),)
LogicalKeyboardKey.media_top_menu = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_top_menu.__ctor = (('mediaTopMenu',),)
LogicalKeyboardKey.navigate_in = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.navigate_in.__ctor = (('navigateIn',),)
LogicalKeyboardKey.navigate_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.navigate_next.__ctor = (('navigateNext',),)
LogicalKeyboardKey.navigate_out = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.navigate_out.__ctor = (('navigateOut',),)
LogicalKeyboardKey.navigate_previous = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.navigate_previous.__ctor = (('navigatePrevious',),)
LogicalKeyboardKey.pairing = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.pairing.__ctor = (('pairing',),)
LogicalKeyboardKey.media_close = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_close.__ctor = (('mediaClose',),)
LogicalKeyboardKey.audio_bass_boost_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_bass_boost_toggle.__ctor = (('audioBassBoostToggle',),)
LogicalKeyboardKey.audio_treble_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_treble_down.__ctor = (('audioTrebleDown',),)
LogicalKeyboardKey.audio_treble_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_treble_up.__ctor = (('audioTrebleUp',),)
LogicalKeyboardKey.microphone_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.microphone_toggle.__ctor = (('microphoneToggle',),)
LogicalKeyboardKey.microphone_volume_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.microphone_volume_down.__ctor = (('microphoneVolumeDown',),)
LogicalKeyboardKey.microphone_volume_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.microphone_volume_up.__ctor = (('microphoneVolumeUp',),)
LogicalKeyboardKey.microphone_volume_mute = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.microphone_volume_mute.__ctor = (('microphoneVolumeMute',),)
LogicalKeyboardKey.speech_correction_list = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.speech_correction_list.__ctor = (('speechCorrectionList',),)
LogicalKeyboardKey.speech_input_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.speech_input_toggle.__ctor = (('speechInputToggle',),)
LogicalKeyboardKey.app_switch = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.app_switch.__ctor = (('appSwitch',),)
LogicalKeyboardKey.call = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.call.__ctor = (('call',),)
LogicalKeyboardKey.camera_focus = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.camera_focus.__ctor = (('cameraFocus',),)
LogicalKeyboardKey.end_call = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.end_call.__ctor = (('endCall',),)
LogicalKeyboardKey.go_back = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.go_back.__ctor = (('goBack',),)
LogicalKeyboardKey.go_home = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.go_home.__ctor = (('goHome',),)
LogicalKeyboardKey.headset_hook = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.headset_hook.__ctor = (('headsetHook',),)
LogicalKeyboardKey.last_number_redial = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.last_number_redial.__ctor = (('lastNumberRedial',),)
LogicalKeyboardKey.notification = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.notification.__ctor = (('notification',),)
LogicalKeyboardKey.manner_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.manner_mode.__ctor = (('mannerMode',),)
LogicalKeyboardKey.voice_dial = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.voice_dial.__ctor = (('voiceDial',),)
LogicalKeyboardKey.tv3_dmode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv3_dmode.__ctor = (('tv3DMode',),)
LogicalKeyboardKey.tv_antenna_cable = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_antenna_cable.__ctor = (('tvAntennaCable',),)
LogicalKeyboardKey.tv_audio_description = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_audio_description.__ctor = (('tvAudioDescription',),)
LogicalKeyboardKey.tv_audio_description_mix_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_audio_description_mix_down.__ctor = (('tvAudioDescriptionMixDown',),)
LogicalKeyboardKey.tv_audio_description_mix_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_audio_description_mix_up.__ctor = (('tvAudioDescriptionMixUp',),)
LogicalKeyboardKey.tv_contents_menu = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_contents_menu.__ctor = (('tvContentsMenu',),)
LogicalKeyboardKey.tv_data_service = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_data_service.__ctor = (('tvDataService',),)
LogicalKeyboardKey.tv_input_component1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_component1.__ctor = (('tvInputComponent1',),)
LogicalKeyboardKey.tv_input_component2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_component2.__ctor = (('tvInputComponent2',),)
LogicalKeyboardKey.tv_input_composite1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_composite1.__ctor = (('tvInputComposite1',),)
LogicalKeyboardKey.tv_input_composite2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_composite2.__ctor = (('tvInputComposite2',),)
LogicalKeyboardKey.tv_input_hdmi1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_hdmi1.__ctor = (('tvInputHDMI1',),)
LogicalKeyboardKey.tv_input_hdmi2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_hdmi2.__ctor = (('tvInputHDMI2',),)
LogicalKeyboardKey.tv_input_hdmi3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_hdmi3.__ctor = (('tvInputHDMI3',),)
LogicalKeyboardKey.tv_input_hdmi4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_hdmi4.__ctor = (('tvInputHDMI4',),)
LogicalKeyboardKey.tv_input_vga1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_vga1.__ctor = (('tvInputVGA1',),)
LogicalKeyboardKey.tv_media_context = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_media_context.__ctor = (('tvMediaContext',),)
LogicalKeyboardKey.tv_network = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_network.__ctor = (('tvNetwork',),)
LogicalKeyboardKey.tv_number_entry = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_number_entry.__ctor = (('tvNumberEntry',),)
LogicalKeyboardKey.tv_radio_service = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_radio_service.__ctor = (('tvRadioService',),)
LogicalKeyboardKey.tv_satellite = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_satellite.__ctor = (('tvSatellite',),)
LogicalKeyboardKey.tv_satellite_bs = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_satellite_bs.__ctor = (('tvSatelliteBS',),)
LogicalKeyboardKey.tv_satellite_cs = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_satellite_cs.__ctor = (('tvSatelliteCS',),)
LogicalKeyboardKey.tv_satellite_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_satellite_toggle.__ctor = (('tvSatelliteToggle',),)
LogicalKeyboardKey.tv_terrestrial_analog = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_terrestrial_analog.__ctor = (('tvTerrestrialAnalog',),)
LogicalKeyboardKey.tv_terrestrial_digital = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_terrestrial_digital.__ctor = (('tvTerrestrialDigital',),)
LogicalKeyboardKey.tv_timer = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_timer.__ctor = (('tvTimer',),)
LogicalKeyboardKey.key11 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key11.__ctor = (('key11',),)
LogicalKeyboardKey.key12 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key12.__ctor = (('key12',),)
LogicalKeyboardKey.suspend = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.suspend.__ctor = (('suspend',),)
LogicalKeyboardKey.resume = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.resume.__ctor = (('resume',),)
LogicalKeyboardKey.sleep = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.sleep.__ctor = (('sleep',),)
LogicalKeyboardKey.abort = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.abort.__ctor = (('abort',),)
LogicalKeyboardKey.lang1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang1.__ctor = (('lang1',),)
LogicalKeyboardKey.lang2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang2.__ctor = (('lang2',),)
LogicalKeyboardKey.lang3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang3.__ctor = (('lang3',),)
LogicalKeyboardKey.lang4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang4.__ctor = (('lang4',),)
LogicalKeyboardKey.lang5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang5.__ctor = (('lang5',),)
LogicalKeyboardKey.intl_backslash = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.intl_backslash.__ctor = (('intlBackslash',),)
LogicalKeyboardKey.intl_ro = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.intl_ro.__ctor = (('intlRo',),)
LogicalKeyboardKey.intl_yen = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.intl_yen.__ctor = (('intlYen',),)
LogicalKeyboardKey.control_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.control_left.__ctor = (('controlLeft',),)
LogicalKeyboardKey.control_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.control_right.__ctor = (('controlRight',),)
LogicalKeyboardKey.shift_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.shift_left.__ctor = (('shiftLeft',),)
LogicalKeyboardKey.shift_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.shift_right.__ctor = (('shiftRight',),)
LogicalKeyboardKey.alt_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alt_left.__ctor = (('altLeft',),)
LogicalKeyboardKey.alt_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alt_right.__ctor = (('altRight',),)
LogicalKeyboardKey.meta_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.meta_left.__ctor = (('metaLeft',),)
LogicalKeyboardKey.meta_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.meta_right.__ctor = (('metaRight',),)
LogicalKeyboardKey.control = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.control.__ctor = (('control',),)
LogicalKeyboardKey.shift = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.shift.__ctor = (('shift',),)
LogicalKeyboardKey.alt = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alt.__ctor = (('alt',),)
LogicalKeyboardKey.meta = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.meta.__ctor = (('meta',),)
LogicalKeyboardKey.numpad_enter = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_enter.__ctor = (('numpadEnter',),)
LogicalKeyboardKey.numpad_paren_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_paren_left.__ctor = (('numpadParenLeft',),)
LogicalKeyboardKey.numpad_paren_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_paren_right.__ctor = (('numpadParenRight',),)
LogicalKeyboardKey.numpad_multiply = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_multiply.__ctor = (('numpadMultiply',),)
LogicalKeyboardKey.numpad_add = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_add.__ctor = (('numpadAdd',),)
LogicalKeyboardKey.numpad_comma = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_comma.__ctor = (('numpadComma',),)
LogicalKeyboardKey.numpad_subtract = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_subtract.__ctor = (('numpadSubtract',),)
LogicalKeyboardKey.numpad_decimal = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_decimal.__ctor = (('numpadDecimal',),)
LogicalKeyboardKey.numpad_divide = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_divide.__ctor = (('numpadDivide',),)
LogicalKeyboardKey.numpad0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad0.__ctor = (('numpad0',),)
LogicalKeyboardKey.numpad1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad1.__ctor = (('numpad1',),)
LogicalKeyboardKey.numpad2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad2.__ctor = (('numpad2',),)
LogicalKeyboardKey.numpad3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad3.__ctor = (('numpad3',),)
LogicalKeyboardKey.numpad4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad4.__ctor = (('numpad4',),)
LogicalKeyboardKey.numpad5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad5.__ctor = (('numpad5',),)
LogicalKeyboardKey.numpad6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad6.__ctor = (('numpad6',),)
LogicalKeyboardKey.numpad7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad7.__ctor = (('numpad7',),)
LogicalKeyboardKey.numpad8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad8.__ctor = (('numpad8',),)
LogicalKeyboardKey.numpad9 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad9.__ctor = (('numpad9',),)
LogicalKeyboardKey.numpad_equal = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_equal.__ctor = (('numpadEqual',),)
LogicalKeyboardKey.game_button1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button1.__ctor = (('gameButton1',),)
LogicalKeyboardKey.game_button2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button2.__ctor = (('gameButton2',),)
LogicalKeyboardKey.game_button3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button3.__ctor = (('gameButton3',),)
LogicalKeyboardKey.game_button4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button4.__ctor = (('gameButton4',),)
LogicalKeyboardKey.game_button5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button5.__ctor = (('gameButton5',),)
LogicalKeyboardKey.game_button6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button6.__ctor = (('gameButton6',),)
LogicalKeyboardKey.game_button7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button7.__ctor = (('gameButton7',),)
LogicalKeyboardKey.game_button8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button8.__ctor = (('gameButton8',),)
LogicalKeyboardKey.game_button9 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button9.__ctor = (('gameButton9',),)
LogicalKeyboardKey.game_button10 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button10.__ctor = (('gameButton10',),)
LogicalKeyboardKey.game_button11 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button11.__ctor = (('gameButton11',),)
LogicalKeyboardKey.game_button12 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button12.__ctor = (('gameButton12',),)
LogicalKeyboardKey.game_button13 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button13.__ctor = (('gameButton13',),)
LogicalKeyboardKey.game_button14 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button14.__ctor = (('gameButton14',),)
LogicalKeyboardKey.game_button15 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button15.__ctor = (('gameButton15',),)
LogicalKeyboardKey.game_button16 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button16.__ctor = (('gameButton16',),)
LogicalKeyboardKey.game_button_a = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_a.__ctor = (('gameButtonA',),)
LogicalKeyboardKey.game_button_b = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_b.__ctor = (('gameButtonB',),)
LogicalKeyboardKey.game_button_c = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_c.__ctor = (('gameButtonC',),)
LogicalKeyboardKey.game_button_left1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_left1.__ctor = (('gameButtonLeft1',),)
LogicalKeyboardKey.game_button_left2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_left2.__ctor = (('gameButtonLeft2',),)
LogicalKeyboardKey.game_button_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_mode.__ctor = (('gameButtonMode',),)
LogicalKeyboardKey.game_button_right1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_right1.__ctor = (('gameButtonRight1',),)
LogicalKeyboardKey.game_button_right2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_right2.__ctor = (('gameButtonRight2',),)
LogicalKeyboardKey.game_button_select = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_select.__ctor = (('gameButtonSelect',),)
LogicalKeyboardKey.game_button_start = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_start.__ctor = (('gameButtonStart',),)
LogicalKeyboardKey.game_button_thumb_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_thumb_left.__ctor = (('gameButtonThumbLeft',),)
LogicalKeyboardKey.game_button_thumb_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_thumb_right.__ctor = (('gameButtonThumbRight',),)
LogicalKeyboardKey.game_button_x = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_x.__ctor = (('gameButtonX',),)
LogicalKeyboardKey.game_button_y = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_y.__ctor = (('gameButtonY',),)
LogicalKeyboardKey.game_button_z = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_z.__ctor = (('gameButtonZ',),)


# packages/flutter/lib/src/services/hardware_keyboard.dart
class KeyEvent(ABC, Object):

    def __init__(
        self,
        physical_key: PhysicalKeyboardKey,
        logical_key: LogicalKeyboardKey,
        time_stamp: Duration,
        character: Optional[str] = None,
        synthesized: Optional[bool] = None,
    ):
        self.__ctor = (('',), (
            'physicalKey', physical_key,
            'logicalKey', logical_key,
            'timeStamp', time_stamp,
            'character', character,
            'synthesized', synthesized,
        ))


# packages/flutter/lib/src/widgets/focus_manager.dart
class FocusNode(Object):

    def __init__(
        self,
        debug_label: Optional[str] = None,
        on_key: Optional[Callable[['FocusNode', RawKeyEvent], KeyEventResult]] = None,
        on_key_event: Optional[Callable[['FocusNode', KeyEvent], KeyEventResult]] = None,
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


# packages/flutter/lib/src/material/button_style_button.dart
class ButtonStyleButton(ABC, StatefulWidget):

    def __init__(
        self,
        on_pressed: Callable[[], None],
        on_long_press: Callable[[], None],
        style: ButtonStyle,
        focus_node: FocusNode,
        autofocus: bool,
        clip_behavior: Clip,
        child: Widget,
        key: Optional[Key] = None,
    ):
        super().__init__(
        )
        self.__ctor = (('',), (
            'onPressed', on_pressed,
            'onLongPress', on_long_press,
            'style', style,
            'focusNode', focus_node,
            'autofocus', autofocus,
            'clipBehavior', clip_behavior,
            'child', child,
            'key', key,
        ))


# packages/flutter/lib/src/material/elevated_button.dart
class ElevatedButton(ButtonStyleButton):

    def __init__(
        self,
        on_pressed: Callable[[], None],
        child: Widget,
        key: Optional[Key] = None,
        on_long_press: Optional[Callable[[], None]] = None,
        style: Optional[ButtonStyle] = None,
        focus_node: Optional[FocusNode] = None,
        autofocus: Optional[bool] = None,
        clip_behavior: Optional[Clip] = None,
    ):
        super().__init__(
            on_pressed=_noop,
            on_long_press=_noop,
            style=ButtonStyle(),
            focus_node=FocusNode(),
            autofocus=False,
            clip_behavior=Clip.none,
            child=Widget(),
        )
        self.__ctor = (('',), (
            'onPressed', on_pressed,
            'child', child,
            'key', key,
            'onLongPress', on_long_press,
            'style', style,
            'focusNode', focus_node,
            'autofocus', autofocus,
            'clipBehavior', clip_behavior,
        ))

    @staticmethod
    def icon(
        on_pressed: Callable[[], None],
        icon: Widget,
        label: Widget,
        key: Optional[Key] = None,
        on_long_press: Optional[Callable[[], None]] = None,
        style: Optional[ButtonStyle] = None,
        focus_node: Optional[FocusNode] = None,
        autofocus: Optional[bool] = None,
        clip_behavior: Optional[Clip] = None,
    ):
        _o = ElevatedButton(
            on_pressed=_noop,
            child=Widget(),
        )
        _o.__ctor = (('icon',), (
            'onPressed', on_pressed,
            'icon', icon,
            'label', label,
            'key', key,
            'onLongPress', on_long_press,
            'style', style,
            'focusNode', focus_node,
            'autofocus', autofocus,
            'clipBehavior', clip_behavior,
        ))
        return _o
