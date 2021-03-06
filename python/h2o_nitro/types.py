from abc import ABC
from enum import Enum
from typing import Generic, TypeVar, Callable, Any, Optional, Iterable, List, Dict


def _noop(*args, **kwargs) -> Any:
    raise f'_noop({args}, {kwargs})'


T = TypeVar('T')


# bin/cache/pkg/sky_engine/lib/core/object.dart
class Object:

    def __init__(
        self,
    ):
        self._nx_ = {
            '#t': ('Object', ''),
        }


# packages/flutter/lib/src/foundation/diagnostics.dart
class DiagnosticableTree(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('DiagnosticableTree', ''),
        }


# packages/flutter/lib/src/foundation/key.dart
class Key(Object, ABC):

    def __init__(
        self,
        value: str,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Key', ''),
            'value': value,
        }

    @staticmethod
    def empty(
    ):
        _o = Key(
            value='',
        )
        _o._nx_ = {
            '#t': ('Key', 'empty'),
        }
        return _o


# packages/flutter/lib/src/widgets/framework.dart
class Widget(DiagnosticableTree, ABC):

    def __init__(
        self,
        key: Optional[Key] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Widget', ''),
            'key': key,
        }


# packages/flutter/lib/src/widgets/framework.dart
class StatefulWidget(Widget, ABC):

    def __init__(
        self,
        key: Optional[Key] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('StatefulWidget', ''),
            'key': key,
        }


# packages/flutter/lib/src/widgets/framework.dart
class State(Object, ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('State', ''),
        }


# packages/flutter/lib/src/widgets/framework.dart
class GlobalKey(Key, ABC, Generic[T]):

    def __init__(
        self,
        debug_label: Optional[str] = None,
    ):
        super().__init__(
            value='',
        )
        self._nx_ = {
            '#t': ('GlobalKey', ''),
            'debugLabel': debug_label,
        }

    @staticmethod
    def constructor(
    ):
        _o = GlobalKey(
        )
        _o._nx_ = {
            '#t': ('GlobalKey', 'constructor'),
        }
        return _o


# bin/cache/pkg/sky_engine/lib/internal/iterable.dart
class EfficientLengthIterable(Iterable[T], ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('EfficientLengthIterable', ''),
        }


# packages/flutter/lib/src/widgets/navigator.dart
class RouteSettings(Object):

    def __init__(
        self,
        name: Optional[str] = None,
        arguments: Optional[Object] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RouteSettings', ''),
            'name': name,
            'arguments': arguments,
        }


# packages/flutter/lib/src/foundation/key.dart
class LocalKey(Key, ABC):

    def __init__(
        self,
    ):
        super().__init__(
            value='',
        )
        self._nx_ = {
            '#t': ('LocalKey', ''),
        }


# packages/flutter/lib/src/widgets/navigator.dart
class Page(RouteSettings, ABC, Generic[T]):

    def __init__(
        self,
        key: Optional[LocalKey] = None,
        name: Optional[str] = None,
        arguments: Optional[Object] = None,
        restoration_id: Optional[str] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Page', ''),
            'key': key,
            'name': name,
            'arguments': arguments,
            'restorationId': restoration_id,
        }


# packages/flutter/lib/src/widgets/navigator.dart
class Route(Object, ABC, Generic[T]):

    def __init__(
        self,
        settings: Optional[RouteSettings] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Route', ''),
            'settings': settings,
        }


# packages/flutter/lib/src/widgets/navigator.dart
class TransitionDelegate(Object, ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('TransitionDelegate', ''),
        }


# packages/flutter/lib/src/widgets/navigator.dart
class NavigatorObserver(Object):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('NavigatorObserver', ''),
        }


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
        on_generate_route: Optional[Callable[[RouteSettings], Optional[Route[Any]]]] = None,
        on_unknown_route: Optional[Callable[[RouteSettings], Optional[Route[Any]]]] = None,
        transition_delegate: Optional[TransitionDelegate[Any]] = None,
        reports_route_update_to_engine: Optional[bool] = None,
        observers: Optional[List[NavigatorObserver]] = None,
        restoration_scope_id: Optional[str] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Navigator', ''),
            'key': key,
            'pages': pages,
            'onPopPage': on_pop_page,
            'initialRoute': initial_route,
            'onGenerateInitialRoutes': on_generate_initial_routes,
            'onGenerateRoute': on_generate_route,
            'onUnknownRoute': on_unknown_route,
            'transitionDelegate': transition_delegate,
            'reportsRouteUpdateToEngine': reports_route_update_to_engine,
            'observers': observers,
            'restorationScopeId': restoration_scope_id,
        }


# packages/flutter/lib/src/widgets/navigator.dart
class NavigatorState(State[Navigator]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('NavigatorState', ''),
        }


# packages/flutter/lib/src/material/scaffold.dart
class ScaffoldMessenger(StatefulWidget):

    def __init__(
        self,
        child: Widget,
        key: Optional[Key] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ScaffoldMessenger', ''),
            'child': child,
            'key': key,
        }


# packages/flutter/lib/src/material/scaffold.dart
class ScaffoldMessengerState(State[ScaffoldMessenger]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ScaffoldMessengerState', ''),
        }


# packages/flutter/lib/src/widgets/framework.dart
class BuildContext(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('BuildContext', ''),
        }


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Color(Object):

    def __init__(
        self,
        value: int,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Color', ''),
            'value': value,
        }

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
        _o._nx_ = {
            '#t': ('Color', 'fromARGB'),
            'a': a,
            'r': r,
            'g': g,
            'b': b,
        }
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
        _o._nx_ = {
            '#t': ('Color', 'fromRGBO'),
            'r': r,
            'g': g,
            'b': b,
            'opacity': opacity,
        }
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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('VisualDensity', ''),
            'horizontal': horizontal,
            'vertical': vertical,
        }


VisualDensity.standard = VisualDensity(
)
VisualDensity.standard._nx_ = {'#t': ('VisualDensity', 'standard')}
VisualDensity.comfortable = VisualDensity(
)
VisualDensity.comfortable._nx_ = {'#t': ('VisualDensity', 'comfortable')}
VisualDensity.compact = VisualDensity(
)
VisualDensity.compact._nx_ = {'#t': ('VisualDensity', 'compact')}


# packages/flutter/lib/src/painting/colors.dart
class ColorSwatch(Color, Generic[T]):

    def __init__(
        self,
        primary: int,
        _swatch: Dict[T, Color],
    ):
        super().__init__(
            value=0,
        )
        self._nx_ = {
            '#t': ('ColorSwatch', ''),
            'primary': primary,
            '_swatch': _swatch,
        }


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
        self._nx_ = {
            '#t': ('MaterialColor', ''),
            'primary': primary,
            'swatch': swatch,
        }


# packages/flutter/lib/src/material/ink_well.dart
class InteractiveInkFeatureFactory(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('InteractiveInkFeatureFactory', ''),
        }


# packages/flutter/lib/src/material/button_theme.dart
class ButtonTextTheme(Enum):
    normal = 'normal'
    accent = 'accent'
    primary = 'primary'


# packages/flutter/lib/src/painting/edge_insets.dart
class EdgeInsetsGeometry(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('EdgeInsetsGeometry', ''),
        }


EdgeInsetsGeometry.infinity = EdgeInsetsGeometry(
)
EdgeInsetsGeometry.infinity._nx_ = {'#t': ('EdgeInsetsGeometry', 'infinity')}


# packages/flutter/lib/src/painting/borders.dart
class ShapeBorder(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ShapeBorder', ''),
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ColorScheme', ''),
            'primary': primary,
            'primaryVariant': primary_variant,
            'secondary': secondary,
            'secondaryVariant': secondary_variant,
            'surface': surface,
            'background': background,
            'error': error,
            'onPrimary': on_primary,
            'onSecondary': on_secondary,
            'onSurface': on_surface,
            'onBackground': on_background,
            'onError': on_error,
            'brightness': brightness,
        }

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
        _o._nx_ = {
            '#t': ('ColorScheme', 'light'),
            'primary': primary,
            'primaryVariant': primary_variant,
            'secondary': secondary,
            'secondaryVariant': secondary_variant,
            'surface': surface,
            'background': background,
            'error': error,
            'onPrimary': on_primary,
            'onSecondary': on_secondary,
            'onSurface': on_surface,
            'onBackground': on_background,
            'onError': on_error,
            'brightness': brightness,
        }
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
        _o._nx_ = {
            '#t': ('ColorScheme', 'dark'),
            'primary': primary,
            'primaryVariant': primary_variant,
            'secondary': secondary,
            'secondaryVariant': secondary_variant,
            'surface': surface,
            'background': background,
            'error': error,
            'onPrimary': on_primary,
            'onSecondary': on_secondary,
            'onSurface': on_surface,
            'onBackground': on_background,
            'onError': on_error,
            'brightness': brightness,
        }
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
        _o._nx_ = {
            '#t': ('ColorScheme', 'highContrastLight'),
            'primary': primary,
            'primaryVariant': primary_variant,
            'secondary': secondary,
            'secondaryVariant': secondary_variant,
            'surface': surface,
            'background': background,
            'error': error,
            'onPrimary': on_primary,
            'onSecondary': on_secondary,
            'onSurface': on_surface,
            'onBackground': on_background,
            'onError': on_error,
            'brightness': brightness,
        }
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
        _o._nx_ = {
            '#t': ('ColorScheme', 'highContrastDark'),
            'primary': primary,
            'primaryVariant': primary_variant,
            'secondary': secondary,
            'secondaryVariant': secondary_variant,
            'surface': surface,
            'background': background,
            'error': error,
            'onPrimary': on_primary,
            'onSecondary': on_secondary,
            'onSurface': on_surface,
            'onBackground': on_background,
            'onError': on_error,
            'brightness': brightness,
        }
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
        _o._nx_ = {
            '#t': ('ColorScheme', 'fromSwatch'),
            'primarySwatch': primary_swatch,
            'primaryColorDark': primary_color_dark,
            'accentColor': accent_color,
            'cardColor': card_color,
            'backgroundColor': background_color,
            'errorColor': error_color,
            'brightness': brightness,
        }
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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ButtonThemeData', ''),
            'textTheme': text_theme,
            'minWidth': min_width,
            'height': height,
            'padding': padding,
            'shape': shape,
            'layoutBehavior': layout_behavior,
            'alignedDropdown': aligned_dropdown,
            'buttonColor': button_color,
            'disabledColor': disabled_color,
            'focusColor': focus_color,
            'hoverColor': hover_color,
            'highlightColor': highlight_color,
            'splashColor': splash_color,
            'colorScheme': color_scheme,
            'materialTapTargetSize': material_tap_target_size,
        }


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontWeight(Object):
    pass


FontWeight.w100 = FontWeight(
)
FontWeight.w100._nx_ = {'#t': ('FontWeight', 'w100')}
FontWeight.w200 = FontWeight(
)
FontWeight.w200._nx_ = {'#t': ('FontWeight', 'w200')}
FontWeight.w300 = FontWeight(
)
FontWeight.w300._nx_ = {'#t': ('FontWeight', 'w300')}
FontWeight.w400 = FontWeight(
)
FontWeight.w400._nx_ = {'#t': ('FontWeight', 'w400')}
FontWeight.w500 = FontWeight(
)
FontWeight.w500._nx_ = {'#t': ('FontWeight', 'w500')}
FontWeight.w600 = FontWeight(
)
FontWeight.w600._nx_ = {'#t': ('FontWeight', 'w600')}
FontWeight.w700 = FontWeight(
)
FontWeight.w700._nx_ = {'#t': ('FontWeight', 'w700')}
FontWeight.w800 = FontWeight(
)
FontWeight.w800._nx_ = {'#t': ('FontWeight', 'w800')}
FontWeight.w900 = FontWeight(
)
FontWeight.w900._nx_ = {'#t': ('FontWeight', 'w900')}
FontWeight.normal = FontWeight(
)
FontWeight.normal._nx_ = {'#t': ('FontWeight', 'normal')}
FontWeight.bold = FontWeight(
)
FontWeight.bold._nx_ = {'#t': ('FontWeight', 'bold')}


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Locale', ''),
            '_languageCode': _language_code,
            '_countryCode': _country_code,
        }

    @staticmethod
    def from_subtags(
        language_code: Optional[str] = None,
        script_code: Optional[str] = None,
        country_code: Optional[str] = None,
    ):
        _o = Locale(
            _language_code='',
        )
        _o._nx_ = {
            '#t': ('Locale', 'fromSubtags'),
            'languageCode': language_code,
            'scriptCode': script_code,
            'countryCode': country_code,
        }
        return _o


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Paint(Object):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Paint', ''),
        }


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class OffsetBase(Object, ABC):

    def __init__(
        self,
        _dx: float,
        _dy: float,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('OffsetBase', ''),
            '_dx': _dx,
            '_dy': _dy,
        }


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
        self._nx_ = {
            '#t': ('Offset', ''),
            'dx': dx,
            'dy': dy,
        }

    @staticmethod
    def from_direction(
        direction: float,
        distance: Optional[float] = None,
    ):
        _o = Offset(
            dx=0.0,
            dy=0.0,
        )
        _o._nx_ = {
            '#t': ('Offset', 'fromDirection'),
            'direction': direction,
            'distance': distance,
        }
        return _o


Offset.zero = Offset(
    dx=0.0,
    dy=0.0,
)
Offset.zero._nx_ = {'#t': ('Offset', 'zero')}
Offset.infinite = Offset(
    dx=0.0,
    dy=0.0,
)
Offset.infinite._nx_ = {'#t': ('Offset', 'infinite')}


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Shadow(Object):

    def __init__(
        self,
        color: Optional[Color] = None,
        offset: Optional[Offset] = None,
        blur_radius: Optional[float] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Shadow', ''),
            'color': color,
            'offset': offset,
            'blurRadius': blur_radius,
        }


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeature(Object):

    def __init__(
        self,
        feature: str,
        value: Optional[int] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('FontFeature', ''),
            'feature': feature,
            'value': value,
        }

    @staticmethod
    def enable(
        feature: str,
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'enable'),
            'feature': feature,
        }
        return _o

    @staticmethod
    def disable(
        feature: str,
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'disable'),
            'feature': feature,
        }
        return _o

    @staticmethod
    def alternative(
        value: int,
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'alternative'),
            'value': value,
        }
        return _o

    @staticmethod
    def alternative_fractions(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'alternativeFractions'),
        }
        return _o

    @staticmethod
    def contextual_alternates(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'contextualAlternates'),
        }
        return _o

    @staticmethod
    def case_sensitive_forms(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'caseSensitiveForms'),
        }
        return _o

    @staticmethod
    def character_variant(
        value: int,
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'characterVariant'),
            'value': value,
        }
        return _o

    @staticmethod
    def denominator(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'denominator'),
        }
        return _o

    @staticmethod
    def fractions(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'fractions'),
        }
        return _o

    @staticmethod
    def historical_forms(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'historicalForms'),
        }
        return _o

    @staticmethod
    def historical_ligatures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'historicalLigatures'),
        }
        return _o

    @staticmethod
    def lining_figures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'liningFigures'),
        }
        return _o

    @staticmethod
    def locale_aware(
        enable: Optional[bool] = None,
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'localeAware'),
            'enable': enable,
        }
        return _o

    @staticmethod
    def notational_forms(
        value: Optional[int] = None,
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'notationalForms'),
            'value': value,
        }
        return _o

    @staticmethod
    def numerators(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'numerators'),
        }
        return _o

    @staticmethod
    def oldstyle_figures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'oldstyleFigures'),
        }
        return _o

    @staticmethod
    def ordinal_forms(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'ordinalForms'),
        }
        return _o

    @staticmethod
    def proportional_figures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'proportionalFigures'),
        }
        return _o

    @staticmethod
    def randomize(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'randomize'),
        }
        return _o

    @staticmethod
    def stylistic_alternates(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'stylisticAlternates'),
        }
        return _o

    @staticmethod
    def scientific_inferiors(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'scientificInferiors'),
        }
        return _o

    @staticmethod
    def stylistic_set(
        value: int,
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'stylisticSet'),
            'value': value,
        }
        return _o

    @staticmethod
    def subscripts(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'subscripts'),
        }
        return _o

    @staticmethod
    def superscripts(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'superscripts'),
        }
        return _o

    @staticmethod
    def swash(
        value: Optional[int] = None,
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'swash'),
            'value': value,
        }
        return _o

    @staticmethod
    def tabular_figures(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'tabularFigures'),
        }
        return _o

    @staticmethod
    def slashed_zero(
    ):
        _o = FontFeature(
            feature='',
        )
        _o._nx_ = {
            '#t': ('FontFeature', 'slashedZero'),
        }
        return _o


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextDecoration(Object):

    @staticmethod
    def combine(
        decorations: List['TextDecoration'],
    ):
        _o = TextDecoration(
        )
        _o._nx_ = {
            '#t': ('TextDecoration', 'combine'),
            'decorations': decorations,
        }
        return _o


TextDecoration.none = TextDecoration(
)
TextDecoration.none._nx_ = {'#t': ('TextDecoration', 'none')}
TextDecoration.underline = TextDecoration(
)
TextDecoration.underline._nx_ = {'#t': ('TextDecoration', 'underline')}
TextDecoration.overline = TextDecoration(
)
TextDecoration.overline._nx_ = {'#t': ('TextDecoration', 'overline')}
TextDecoration.line_through = TextDecoration(
)
TextDecoration.line_through._nx_ = {'#t': ('TextDecoration', 'lineThrough')}


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('TextStyle', ''),
            'inherit': inherit,
            'color': color,
            'backgroundColor': background_color,
            'fontSize': font_size,
            'fontWeight': font_weight,
            'fontStyle': font_style,
            'letterSpacing': letter_spacing,
            'wordSpacing': word_spacing,
            'textBaseline': text_baseline,
            'height': height,
            'leadingDistribution': leading_distribution,
            'locale': locale,
            'foreground': foreground,
            'background': background,
            'shadows': shadows,
            'fontFeatures': font_features,
            'decoration': decoration,
            'decorationColor': decoration_color,
            'decorationStyle': decoration_style,
            'decorationThickness': decoration_thickness,
            'debugLabel': debug_label,
            'fontFamily': font_family,
            'fontFamilyFallback': font_family_fallback,
            'package': package,
            'overflow': overflow,
        }


# packages/flutter/lib/src/rendering/object.dart
class Constraints(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Constraints', ''),
        }


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
        self._nx_ = {
            '#t': ('Size', ''),
            'width': width,
            'height': height,
        }

    @staticmethod
    def copy(
        source: 'Size',
    ):
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o._nx_ = {
            '#t': ('Size', 'copy'),
            'source': source,
        }
        return _o

    @staticmethod
    def square(
        dimension: float,
    ):
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o._nx_ = {
            '#t': ('Size', 'square'),
            'dimension': dimension,
        }
        return _o

    @staticmethod
    def from_width(
        width: float,
    ):
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o._nx_ = {
            '#t': ('Size', 'fromWidth'),
            'width': width,
        }
        return _o

    @staticmethod
    def from_height(
        height: float,
    ):
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o._nx_ = {
            '#t': ('Size', 'fromHeight'),
            'height': height,
        }
        return _o

    @staticmethod
    def from_radius(
        radius: float,
    ):
        _o = Size(
            width=0.0,
            height=0.0,
        )
        _o._nx_ = {
            '#t': ('Size', 'fromRadius'),
            'radius': radius,
        }
        return _o


Size.zero = Size(
    width=0.0,
    height=0.0,
)
Size.zero._nx_ = {'#t': ('Size', 'zero')}
Size.infinite = Size(
    width=0.0,
    height=0.0,
)
Size.infinite._nx_ = {'#t': ('Size', 'infinite')}


# packages/flutter/lib/src/rendering/box.dart
class BoxConstraints(Constraints):

    def __init__(
        self,
        min_width: Optional[float] = None,
        max_width: Optional[float] = None,
        min_height: Optional[float] = None,
        max_height: Optional[float] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('BoxConstraints', ''),
            'minWidth': min_width,
            'maxWidth': max_width,
            'minHeight': min_height,
            'maxHeight': max_height,
        }

    @staticmethod
    def tight(
        size: Size,
    ):
        _o = BoxConstraints(
        )
        _o._nx_ = {
            '#t': ('BoxConstraints', 'tight'),
            'size': size,
        }
        return _o

    @staticmethod
    def tight_for(
        width: Optional[float] = None,
        height: Optional[float] = None,
    ):
        _o = BoxConstraints(
        )
        _o._nx_ = {
            '#t': ('BoxConstraints', 'tightFor'),
            'width': width,
            'height': height,
        }
        return _o

    @staticmethod
    def tight_for_finite(
        width: Optional[float] = None,
        height: Optional[float] = None,
    ):
        _o = BoxConstraints(
        )
        _o._nx_ = {
            '#t': ('BoxConstraints', 'tightForFinite'),
            'width': width,
            'height': height,
        }
        return _o

    @staticmethod
    def loose(
        size: Size,
    ):
        _o = BoxConstraints(
        )
        _o._nx_ = {
            '#t': ('BoxConstraints', 'loose'),
            'size': size,
        }
        return _o

    @staticmethod
    def expand(
        width: Optional[float] = None,
        height: Optional[float] = None,
    ):
        _o = BoxConstraints(
        )
        _o._nx_ = {
            '#t': ('BoxConstraints', 'expand'),
            'width': width,
            'height': height,
        }
        return _o


# packages/flutter/lib/src/painting/border_radius.dart
class BorderRadiusGeometry(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('BorderRadiusGeometry', ''),
        }


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class Radius(Object):

    @staticmethod
    def circular(
        radius: float,
    ):
        _o = Radius(
        )
        _o._nx_ = {
            '#t': ('Radius', 'circular'),
            'radius': radius,
        }
        return _o

    @staticmethod
    def elliptical(
        x: float,
        y: float,
    ):
        _o = Radius(
        )
        _o._nx_ = {
            '#t': ('Radius', 'elliptical'),
            'x': x,
            'y': y,
        }
        return _o


Radius.zero = Radius(
)
Radius.zero._nx_ = {'#t': ('Radius', 'zero')}


# packages/flutter/lib/src/painting/border_radius.dart
class BorderRadius(BorderRadiusGeometry):

    @staticmethod
    def all(
        radius: Radius,
    ):
        _o = BorderRadius(
        )
        _o._nx_ = {
            '#t': ('BorderRadius', 'all'),
            'radius': radius,
        }
        return _o

    @staticmethod
    def circular(
        radius: float,
    ):
        _o = BorderRadius(
        )
        _o._nx_ = {
            '#t': ('BorderRadius', 'circular'),
            'radius': radius,
        }
        return _o

    @staticmethod
    def vertical(
        top: Optional[Radius] = None,
        bottom: Optional[Radius] = None,
    ):
        _o = BorderRadius(
        )
        _o._nx_ = {
            '#t': ('BorderRadius', 'vertical'),
            'top': top,
            'bottom': bottom,
        }
        return _o

    @staticmethod
    def horizontal(
        left: Optional[Radius] = None,
        right: Optional[Radius] = None,
    ):
        _o = BorderRadius(
        )
        _o._nx_ = {
            '#t': ('BorderRadius', 'horizontal'),
            'left': left,
            'right': right,
        }
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
        _o._nx_ = {
            '#t': ('BorderRadius', 'only'),
            'topLeft': top_left,
            'topRight': top_right,
            'bottomLeft': bottom_left,
            'bottomRight': bottom_right,
        }
        return _o


BorderRadius.zero = BorderRadius(
)
BorderRadius.zero._nx_ = {'#t': ('BorderRadius', 'zero')}


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ToggleButtonsThemeData', ''),
            'textStyle': text_style,
            'constraints': constraints,
            'color': color,
            'selectedColor': selected_color,
            'disabledColor': disabled_color,
            'fillColor': fill_color,
            'focusColor': focus_color,
            'highlightColor': highlight_color,
            'hoverColor': hover_color,
            'splashColor': splash_color,
            'borderColor': border_color,
            'selectedBorderColor': selected_border_color,
            'disabledBorderColor': disabled_border_color,
            'borderRadius': border_radius,
            'borderWidth': border_width,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('TextTheme', ''),
            'headline1': headline1,
            'headline2': headline2,
            'headline3': headline3,
            'headline4': headline4,
            'headline5': headline5,
            'headline6': headline6,
            'subtitle1': subtitle1,
            'subtitle2': subtitle2,
            'bodyText1': body_text1,
            'bodyText2': body_text2,
            'caption': caption,
            'button': button,
            'overline': overline,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('BorderSide', ''),
            'color': color,
            'width': width,
            'style': style,
        }


BorderSide.none = BorderSide(
)
BorderSide.none._nx_ = {'#t': ('BorderSide', 'none')}


# packages/flutter/lib/src/material/input_border.dart
class InputBorder(ShapeBorder, ABC):

    def __init__(
        self,
        border_side: Optional[BorderSide] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('InputBorder', ''),
            'borderSide': border_side,
        }


InputBorder.none = InputBorder(
)
InputBorder.none._nx_ = {'#t': ('InputBorder', 'none')}


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('InputDecorationTheme', ''),
            'labelStyle': label_style,
            'floatingLabelStyle': floating_label_style,
            'helperStyle': helper_style,
            'helperMaxLines': helper_max_lines,
            'hintStyle': hint_style,
            'errorStyle': error_style,
            'errorMaxLines': error_max_lines,
            'floatingLabelBehavior': floating_label_behavior,
            'isDense': is_dense,
            'contentPadding': content_padding,
            'isCollapsed': is_collapsed,
            'prefixStyle': prefix_style,
            'suffixStyle': suffix_style,
            'counterStyle': counter_style,
            'filled': filled,
            'fillColor': fill_color,
            'focusColor': focus_color,
            'hoverColor': hover_color,
            'errorBorder': error_border,
            'focusedBorder': focused_border,
            'focusedErrorBorder': focused_error_border,
            'disabledBorder': disabled_border,
            'enabledBorder': enabled_border,
            'border': border,
            'alignLabelWithHint': align_label_with_hint,
            'constraints': constraints,
        }


# packages/flutter/lib/src/widgets/icon_theme_data.dart
class IconThemeData(Object):

    def __init__(
        self,
        color: Optional[Color] = None,
        opacity: Optional[float] = None,
        size: Optional[float] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('IconThemeData', ''),
            'color': color,
            'opacity': opacity,
            'size': size,
        }

    @staticmethod
    def fallback(
    ):
        _o = IconThemeData(
        )
        _o._nx_ = {
            '#t': ('IconThemeData', 'fallback'),
        }
        return _o


# packages/flutter/lib/src/material/slider_theme.dart
class SliderComponentShape(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('SliderComponentShape', ''),
        }


# packages/flutter/lib/src/material/slider_theme.dart
class SliderTickMarkShape(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('SliderTickMarkShape', ''),
        }


# packages/flutter/lib/src/material/slider_theme.dart
class SliderTrackShape(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('SliderTrackShape', ''),
        }


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderTickMarkShape(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RangeSliderTickMarkShape', ''),
        }


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderThumbShape(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RangeSliderThumbShape', ''),
        }


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderTrackShape(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RangeSliderTrackShape', ''),
        }


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderValueIndicatorShape(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RangeSliderValueIndicatorShape', ''),
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RangeValues', ''),
            'start': start,
            'end': end,
        }


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
        thumb_selector: Optional[Callable[[TextDirection, RangeValues, float, Size, Size, float], Optional[Thumb]]] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('SliderThemeData', ''),
            'trackHeight': track_height,
            'activeTrackColor': active_track_color,
            'inactiveTrackColor': inactive_track_color,
            'disabledActiveTrackColor': disabled_active_track_color,
            'disabledInactiveTrackColor': disabled_inactive_track_color,
            'activeTickMarkColor': active_tick_mark_color,
            'inactiveTickMarkColor': inactive_tick_mark_color,
            'disabledActiveTickMarkColor': disabled_active_tick_mark_color,
            'disabledInactiveTickMarkColor': disabled_inactive_tick_mark_color,
            'thumbColor': thumb_color,
            'overlappingShapeStrokeColor': overlapping_shape_stroke_color,
            'disabledThumbColor': disabled_thumb_color,
            'overlayColor': overlay_color,
            'valueIndicatorColor': value_indicator_color,
            'overlayShape': overlay_shape,
            'tickMarkShape': tick_mark_shape,
            'thumbShape': thumb_shape,
            'trackShape': track_shape,
            'valueIndicatorShape': value_indicator_shape,
            'rangeTickMarkShape': range_tick_mark_shape,
            'rangeThumbShape': range_thumb_shape,
            'rangeTrackShape': range_track_shape,
            'rangeValueIndicatorShape': range_value_indicator_shape,
            'showValueIndicator': show_value_indicator,
            'valueIndicatorTextStyle': value_indicator_text_style,
            'minThumbSeparation': min_thumb_separation,
            'thumbSelector': thumb_selector,
        }

    @staticmethod
    def from_primary_colors(
        primary_color: Color,
        primary_color_dark: Color,
        primary_color_light: Color,
        value_indicator_text_style: TextStyle,
    ):
        _o = SliderThemeData(
        )
        _o._nx_ = {
            '#t': ('SliderThemeData', 'fromPrimaryColors'),
            'primaryColor': primary_color,
            'primaryColorDark': primary_color_dark,
            'primaryColorLight': primary_color_light,
            'valueIndicatorTextStyle': value_indicator_text_style,
        }
        return _o


# packages/flutter/lib/src/painting/decoration.dart
class Decoration(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Decoration', ''),
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('TabBarTheme', ''),
            'indicator': indicator,
            'indicatorSize': indicator_size,
            'labelColor': label_color,
            'labelPadding': label_padding,
            'labelStyle': label_style,
            'unselectedLabelColor': unselected_label_color,
            'unselectedLabelStyle': unselected_label_style,
        }


# bin/cache/pkg/sky_engine/lib/core/comparable.dart
class Comparable(Object, ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Comparable', ''),
        }


# bin/cache/pkg/sky_engine/lib/core/duration.dart
class Duration(Comparable['Duration'], Object):
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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Duration', ''),
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
            'milliseconds': milliseconds,
            'microseconds': microseconds,
        }


Duration.zero = Duration(
)
Duration.zero._nx_ = {'#t': ('Duration', 'zero')}


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('TooltipThemeData', ''),
            'height': height,
            'padding': padding,
            'margin': margin,
            'verticalOffset': vertical_offset,
            'preferBelow': prefer_below,
            'excludeFromSemantics': exclude_from_semantics,
            'decoration': decoration,
            'textStyle': text_style,
            'waitDuration': wait_duration,
            'showDuration': show_duration,
            'triggerMode': trigger_mode,
            'enableFeedback': enable_feedback,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('CardTheme', ''),
            'clipBehavior': clip_behavior,
            'color': color,
            'shadowColor': shadow_color,
            'elevation': elevation,
            'margin': margin,
            'shape': shape,
        }


# packages/flutter/lib/src/painting/borders.dart
class OutlinedBorder(ShapeBorder, ABC):

    def __init__(
        self,
        side: Optional[BorderSide] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('OutlinedBorder', ''),
            'side': side,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ChipThemeData', ''),
            'backgroundColor': background_color,
            'disabledColor': disabled_color,
            'selectedColor': selected_color,
            'secondarySelectedColor': secondary_selected_color,
            'padding': padding,
            'labelStyle': label_style,
            'secondaryLabelStyle': secondary_label_style,
            'brightness': brightness,
            'deleteIconColor': delete_icon_color,
            'shadowColor': shadow_color,
            'selectedShadowColor': selected_shadow_color,
            'showCheckmark': show_checkmark,
            'checkmarkColor': checkmark_color,
            'labelPadding': label_padding,
            'side': side,
            'shape': shape,
            'elevation': elevation,
            'pressElevation': press_elevation,
        }

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
        _o._nx_ = {
            '#t': ('ChipThemeData', 'fromDefaults'),
            'secondaryColor': secondary_color,
            'labelStyle': label_style,
            'brightness': brightness,
            'primaryColor': primary_color,
        }
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
class PageTransitionsBuilder(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('PageTransitionsBuilder', ''),
        }


# packages/flutter/lib/src/material/page_transitions_theme.dart
class PageTransitionsTheme(Object):

    def __init__(
        self,
        builders: Optional[Dict[TargetPlatform, PageTransitionsBuilder]] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('PageTransitionsTheme', ''),
            'builders': builders,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('SystemUiOverlayStyle', ''),
            'systemNavigationBarColor': system_navigation_bar_color,
            'systemNavigationBarDividerColor': system_navigation_bar_divider_color,
            'systemNavigationBarIconBrightness': system_navigation_bar_icon_brightness,
            'systemNavigationBarContrastEnforced': system_navigation_bar_contrast_enforced,
            'statusBarColor': status_bar_color,
            'statusBarBrightness': status_bar_brightness,
            'statusBarIconBrightness': status_bar_icon_brightness,
            'systemStatusBarContrastEnforced': system_status_bar_contrast_enforced,
        }


SystemUiOverlayStyle.light = SystemUiOverlayStyle(
)
SystemUiOverlayStyle.light._nx_ = {'#t': ('SystemUiOverlayStyle', 'light')}
SystemUiOverlayStyle.dark = SystemUiOverlayStyle(
)
SystemUiOverlayStyle.dark._nx_ = {'#t': ('SystemUiOverlayStyle', 'dark')}


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('AppBarTheme', ''),
            'brightness': brightness,
            'color': color,
            'backgroundColor': background_color,
            'foregroundColor': foreground_color,
            'elevation': elevation,
            'shadowColor': shadow_color,
            'shape': shape,
            'iconTheme': icon_theme,
            'actionsIconTheme': actions_icon_theme,
            'textTheme': text_theme,
            'centerTitle': center_title,
            'titleSpacing': title_spacing,
            'toolbarHeight': toolbar_height,
            'toolbarTextStyle': toolbar_text_style,
            'titleTextStyle': title_text_style,
            'systemOverlayStyle': system_overlay_style,
            'backwardsCompatibility': backwards_compatibility,
        }


# packages/flutter/lib/src/material/material_state.dart
class MaterialStateProperty(Object, ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('MaterialStateProperty', ''),
        }


# packages/flutter/lib/src/material/scrollbar_theme.dart
class ScrollbarThemeData(Object):

    def __init__(
        self,
        thickness: Optional[MaterialStateProperty[Optional[float]]] = None,
        show_track_on_hover: Optional[bool] = None,
        is_always_shown: Optional[bool] = None,
        radius: Optional[Radius] = None,
        thumb_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        track_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        track_border_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        cross_axis_margin: Optional[float] = None,
        main_axis_margin: Optional[float] = None,
        min_thumb_length: Optional[float] = None,
        interactive: Optional[bool] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ScrollbarThemeData', ''),
            'thickness': thickness,
            'showTrackOnHover': show_track_on_hover,
            'isAlwaysShown': is_always_shown,
            'radius': radius,
            'thumbColor': thumb_color,
            'trackColor': track_color,
            'trackBorderColor': track_border_color,
            'crossAxisMargin': cross_axis_margin,
            'mainAxisMargin': main_axis_margin,
            'minThumbLength': min_thumb_length,
            'interactive': interactive,
        }


# packages/flutter/lib/src/painting/notched_shapes.dart
class NotchedShape(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('NotchedShape', ''),
        }


# packages/flutter/lib/src/material/bottom_app_bar_theme.dart
class BottomAppBarTheme(Object):

    def __init__(
        self,
        color: Optional[Color] = None,
        elevation: Optional[float] = None,
        shape: Optional[NotchedShape] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('BottomAppBarTheme', ''),
            'color': color,
            'elevation': elevation,
            'shape': shape,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('DialogTheme', ''),
            'backgroundColor': background_color,
            'elevation': elevation,
            'shape': shape,
            'titleTextStyle': title_text_style,
            'contentTextStyle': content_text_style,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('FloatingActionButtonThemeData', ''),
            'foregroundColor': foreground_color,
            'backgroundColor': background_color,
            'focusColor': focus_color,
            'hoverColor': hover_color,
            'splashColor': splash_color,
            'elevation': elevation,
            'focusElevation': focus_elevation,
            'hoverElevation': hover_elevation,
            'disabledElevation': disabled_elevation,
            'highlightElevation': highlight_elevation,
            'shape': shape,
            'enableFeedback': enable_feedback,
            'sizeConstraints': size_constraints,
            'smallSizeConstraints': small_size_constraints,
            'largeSizeConstraints': large_size_constraints,
            'extendedSizeConstraints': extended_size_constraints,
            'extendedIconLabelSpacing': extended_icon_label_spacing,
            'extendedPadding': extended_padding,
            'extendedTextStyle': extended_text_style,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('NavigationRailThemeData', ''),
            'backgroundColor': background_color,
            'elevation': elevation,
            'unselectedLabelTextStyle': unselected_label_text_style,
            'selectedLabelTextStyle': selected_label_text_style,
            'unselectedIconTheme': unselected_icon_theme,
            'selectedIconTheme': selected_icon_theme,
            'groupAlignment': group_alignment,
            'labelType': label_type,
        }


def _typography__text_theme(_k: str) -> TextTheme:
    _o = TextTheme(
    )
    _o._nx_ = {'#t': ('Typography', _k)}
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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Typography', ''),
            'platform': platform,
            'black': black,
            'white': white,
            'englishLike': english_like,
            'dense': dense,
            'tall': tall,
        }

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
        _o._nx_ = {
            '#t': ('Typography', 'material2014'),
            'platform': platform,
            'black': black,
            'white': white,
            'englishLike': english_like,
            'dense': dense,
            'tall': tall,
        }
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
        _o._nx_ = {
            '#t': ('Typography', 'material2018'),
            'platform': platform,
            'black': black,
            'white': white,
            'englishLike': english_like,
            'dense': dense,
            'tall': tall,
        }
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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('CupertinoTextThemeData', ''),
            'primaryColor': primary_color,
            'textStyle': text_style,
            'actionTextStyle': action_text_style,
            'tabLabelTextStyle': tab_label_text_style,
            'navTitleTextStyle': nav_title_text_style,
            'navLargeTitleTextStyle': nav_large_title_text_style,
            'navActionTextStyle': nav_action_text_style,
            'pickerTextStyle': picker_text_style,
            'dateTimePickerTextStyle': date_time_picker_text_style,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('NoDefaultCupertinoThemeData', ''),
            'brightness': brightness,
            'primaryColor': primary_color,
            'primaryContrastingColor': primary_contrasting_color,
            'textTheme': text_theme,
            'barBackgroundColor': bar_background_color,
            'scaffoldBackgroundColor': scaffold_background_color,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('SnackBarThemeData', ''),
            'backgroundColor': background_color,
            'actionTextColor': action_text_color,
            'disabledActionTextColor': disabled_action_text_color,
            'contentTextStyle': content_text_style,
            'elevation': elevation,
            'shape': shape,
            'behavior': behavior,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('BottomSheetThemeData', ''),
            'backgroundColor': background_color,
            'elevation': elevation,
            'modalBackgroundColor': modal_background_color,
            'modalElevation': modal_elevation,
            'shape': shape,
            'clipBehavior': clip_behavior,
            'constraints': constraints,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('PopupMenuThemeData', ''),
            'color': color,
            'shape': shape,
            'elevation': elevation,
            'textStyle': text_style,
            'enableFeedback': enable_feedback,
        }


# packages/flutter/lib/src/material/banner_theme.dart
class MaterialBannerThemeData(Object):

    def __init__(
        self,
        background_color: Optional[Color] = None,
        content_text_style: Optional[TextStyle] = None,
        padding: Optional[EdgeInsetsGeometry] = None,
        leading_padding: Optional[EdgeInsetsGeometry] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('MaterialBannerThemeData', ''),
            'backgroundColor': background_color,
            'contentTextStyle': content_text_style,
            'padding': padding,
            'leadingPadding': leading_padding,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('DividerThemeData', ''),
            'color': color,
            'space': space,
            'thickness': thickness,
            'indent': indent,
            'endIndent': end_indent,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ButtonBarThemeData', ''),
            'alignment': alignment,
            'mainAxisSize': main_axis_size,
            'buttonTextTheme': button_text_theme,
            'buttonMinWidth': button_min_width,
            'buttonHeight': button_height,
            'buttonPadding': button_padding,
            'buttonAlignedDropdown': button_aligned_dropdown,
            'layoutBehavior': layout_behavior,
            'overflowDirection': overflow_direction,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('BottomNavigationBarThemeData', ''),
            'backgroundColor': background_color,
            'elevation': elevation,
            'selectedIconTheme': selected_icon_theme,
            'unselectedIconTheme': unselected_icon_theme,
            'selectedItemColor': selected_item_color,
            'unselectedItemColor': unselected_item_color,
            'selectedLabelStyle': selected_label_style,
            'unselectedLabelStyle': unselected_label_style,
            'showSelectedLabels': show_selected_labels,
            'showUnselectedLabels': show_unselected_labels,
            'type': type,
            'enableFeedback': enable_feedback,
            'landscapeLayout': landscape_layout,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('TimePickerThemeData', ''),
            'backgroundColor': background_color,
            'hourMinuteTextColor': hour_minute_text_color,
            'hourMinuteColor': hour_minute_color,
            'dayPeriodTextColor': day_period_text_color,
            'dayPeriodColor': day_period_color,
            'dialHandColor': dial_hand_color,
            'dialBackgroundColor': dial_background_color,
            'dialTextColor': dial_text_color,
            'entryModeIconColor': entry_mode_icon_color,
            'hourMinuteTextStyle': hour_minute_text_style,
            'dayPeriodTextStyle': day_period_text_style,
            'helpTextStyle': help_text_style,
            'shape': shape,
            'hourMinuteShape': hour_minute_shape,
            'dayPeriodShape': day_period_shape,
            'dayPeriodBorderSide': day_period_border_side,
            'inputDecorationTheme': input_decoration_theme,
        }


# packages/flutter/lib/src/services/mouse_cursor.dart
class MouseCursor(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('MouseCursor', ''),
        }


MouseCursor.defer = MouseCursor(
)
MouseCursor.defer._nx_ = {'#t': ('MouseCursor', 'defer')}
MouseCursor.uncontrolled = MouseCursor(
)
MouseCursor.uncontrolled._nx_ = {'#t': ('MouseCursor', 'uncontrolled')}


# packages/flutter/lib/src/painting/alignment.dart
class AlignmentGeometry(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('AlignmentGeometry', ''),
        }


# packages/flutter/lib/src/material/button_style.dart
class ButtonStyle(Object):

    def __init__(
        self,
        text_style: Optional[MaterialStateProperty[Optional[TextStyle]]] = None,
        background_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        foreground_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        overlay_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        shadow_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        elevation: Optional[MaterialStateProperty[Optional[float]]] = None,
        padding: Optional[MaterialStateProperty[Optional[EdgeInsetsGeometry]]] = None,
        minimum_size: Optional[MaterialStateProperty[Optional[Size]]] = None,
        fixed_size: Optional[MaterialStateProperty[Optional[Size]]] = None,
        maximum_size: Optional[MaterialStateProperty[Optional[Size]]] = None,
        side: Optional[MaterialStateProperty[Optional[BorderSide]]] = None,
        shape: Optional[MaterialStateProperty[Optional[OutlinedBorder]]] = None,
        mouse_cursor: Optional[MaterialStateProperty[Optional[MouseCursor]]] = None,
        visual_density: Optional[VisualDensity] = None,
        tap_target_size: Optional[MaterialTapTargetSize] = None,
        animation_duration: Optional[Duration] = None,
        enable_feedback: Optional[bool] = None,
        alignment: Optional[AlignmentGeometry] = None,
        splash_factory: Optional[InteractiveInkFeatureFactory] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ButtonStyle', ''),
            'textStyle': text_style,
            'backgroundColor': background_color,
            'foregroundColor': foreground_color,
            'overlayColor': overlay_color,
            'shadowColor': shadow_color,
            'elevation': elevation,
            'padding': padding,
            'minimumSize': minimum_size,
            'fixedSize': fixed_size,
            'maximumSize': maximum_size,
            'side': side,
            'shape': shape,
            'mouseCursor': mouse_cursor,
            'visualDensity': visual_density,
            'tapTargetSize': tap_target_size,
            'animationDuration': animation_duration,
            'enableFeedback': enable_feedback,
            'alignment': alignment,
            'splashFactory': splash_factory,
        }


# packages/flutter/lib/src/material/text_button_theme.dart
class TextButtonThemeData(Object):

    def __init__(
        self,
        style: Optional[ButtonStyle] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('TextButtonThemeData', ''),
            'style': style,
        }


# packages/flutter/lib/src/material/elevated_button_theme.dart
class ElevatedButtonThemeData(Object):

    def __init__(
        self,
        style: Optional[ButtonStyle] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ElevatedButtonThemeData', ''),
            'style': style,
        }


# packages/flutter/lib/src/material/outlined_button_theme.dart
class OutlinedButtonThemeData(Object):

    def __init__(
        self,
        style: Optional[ButtonStyle] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('OutlinedButtonThemeData', ''),
            'style': style,
        }


# packages/flutter/lib/src/material/text_selection_theme.dart
class TextSelectionThemeData(Object):

    def __init__(
        self,
        cursor_color: Optional[Color] = None,
        selection_color: Optional[Color] = None,
        selection_handle_color: Optional[Color] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('TextSelectionThemeData', ''),
            'cursorColor': cursor_color,
            'selectionColor': selection_color,
            'selectionHandleColor': selection_handle_color,
        }


# packages/flutter/lib/src/material/data_table_theme.dart
class DataTableThemeData(Object):

    def __init__(
        self,
        decoration: Optional[Decoration] = None,
        data_row_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        data_row_height: Optional[float] = None,
        data_text_style: Optional[TextStyle] = None,
        heading_row_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        heading_row_height: Optional[float] = None,
        heading_text_style: Optional[TextStyle] = None,
        horizontal_margin: Optional[float] = None,
        column_spacing: Optional[float] = None,
        divider_thickness: Optional[float] = None,
        checkbox_horizontal_margin: Optional[float] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('DataTableThemeData', ''),
            'decoration': decoration,
            'dataRowColor': data_row_color,
            'dataRowHeight': data_row_height,
            'dataTextStyle': data_text_style,
            'headingRowColor': heading_row_color,
            'headingRowHeight': heading_row_height,
            'headingTextStyle': heading_text_style,
            'horizontalMargin': horizontal_margin,
            'columnSpacing': column_spacing,
            'dividerThickness': divider_thickness,
            'checkboxHorizontalMargin': checkbox_horizontal_margin,
        }


# packages/flutter/lib/src/material/checkbox_theme.dart
class CheckboxThemeData(Object):

    def __init__(
        self,
        mouse_cursor: Optional[MaterialStateProperty[Optional[MouseCursor]]] = None,
        fill_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        check_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        overlay_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        splash_radius: Optional[float] = None,
        material_tap_target_size: Optional[MaterialTapTargetSize] = None,
        visual_density: Optional[VisualDensity] = None,
        shape: Optional[OutlinedBorder] = None,
        side: Optional[BorderSide] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('CheckboxThemeData', ''),
            'mouseCursor': mouse_cursor,
            'fillColor': fill_color,
            'checkColor': check_color,
            'overlayColor': overlay_color,
            'splashRadius': splash_radius,
            'materialTapTargetSize': material_tap_target_size,
            'visualDensity': visual_density,
            'shape': shape,
            'side': side,
        }


# packages/flutter/lib/src/material/radio_theme.dart
class RadioThemeData(Object):

    def __init__(
        self,
        mouse_cursor: Optional[MaterialStateProperty[Optional[MouseCursor]]] = None,
        fill_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        overlay_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        splash_radius: Optional[float] = None,
        material_tap_target_size: Optional[MaterialTapTargetSize] = None,
        visual_density: Optional[VisualDensity] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RadioThemeData', ''),
            'mouseCursor': mouse_cursor,
            'fillColor': fill_color,
            'overlayColor': overlay_color,
            'splashRadius': splash_radius,
            'materialTapTargetSize': material_tap_target_size,
            'visualDensity': visual_density,
        }


# packages/flutter/lib/src/material/switch_theme.dart
class SwitchThemeData(Object):

    def __init__(
        self,
        thumb_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        track_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        material_tap_target_size: Optional[MaterialTapTargetSize] = None,
        mouse_cursor: Optional[MaterialStateProperty[Optional[MouseCursor]]] = None,
        overlay_color: Optional[MaterialStateProperty[Optional[Color]]] = None,
        splash_radius: Optional[float] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('SwitchThemeData', ''),
            'thumbColor': thumb_color,
            'trackColor': track_color,
            'materialTapTargetSize': material_tap_target_size,
            'mouseCursor': mouse_cursor,
            'overlayColor': overlay_color,
            'splashRadius': splash_radius,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ProgressIndicatorThemeData', ''),
            'color': color,
            'linearTrackColor': linear_track_color,
            'linearMinHeight': linear_min_height,
            'circularTrackColor': circular_track_color,
            'refreshBackgroundColor': refresh_background_color,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ThemeData', ''),
            'brightness': brightness,
            'visualDensity': visual_density,
            'primarySwatch': primary_swatch,
            'primaryColor': primary_color,
            'primaryColorBrightness': primary_color_brightness,
            'primaryColorLight': primary_color_light,
            'primaryColorDark': primary_color_dark,
            'accentColor': accent_color,
            'accentColorBrightness': accent_color_brightness,
            'canvasColor': canvas_color,
            'shadowColor': shadow_color,
            'scaffoldBackgroundColor': scaffold_background_color,
            'bottomAppBarColor': bottom_app_bar_color,
            'cardColor': card_color,
            'dividerColor': divider_color,
            'focusColor': focus_color,
            'hoverColor': hover_color,
            'highlightColor': highlight_color,
            'splashColor': splash_color,
            'splashFactory': splash_factory,
            'selectedRowColor': selected_row_color,
            'unselectedWidgetColor': unselected_widget_color,
            'disabledColor': disabled_color,
            'buttonColor': button_color,
            'buttonTheme': button_theme,
            'toggleButtonsTheme': toggle_buttons_theme,
            'secondaryHeaderColor': secondary_header_color,
            'textSelectionColor': text_selection_color,
            'cursorColor': cursor_color,
            'textSelectionHandleColor': text_selection_handle_color,
            'backgroundColor': background_color,
            'dialogBackgroundColor': dialog_background_color,
            'indicatorColor': indicator_color,
            'hintColor': hint_color,
            'errorColor': error_color,
            'toggleableActiveColor': toggleable_active_color,
            'fontFamily': font_family,
            'textTheme': text_theme,
            'primaryTextTheme': primary_text_theme,
            'accentTextTheme': accent_text_theme,
            'inputDecorationTheme': input_decoration_theme,
            'iconTheme': icon_theme,
            'primaryIconTheme': primary_icon_theme,
            'accentIconTheme': accent_icon_theme,
            'sliderTheme': slider_theme,
            'tabBarTheme': tab_bar_theme,
            'tooltipTheme': tooltip_theme,
            'cardTheme': card_theme,
            'chipTheme': chip_theme,
            'platform': platform,
            'materialTapTargetSize': material_tap_target_size,
            'applyElevationOverlayColor': apply_elevation_overlay_color,
            'pageTransitionsTheme': page_transitions_theme,
            'appBarTheme': app_bar_theme,
            'scrollbarTheme': scrollbar_theme,
            'bottomAppBarTheme': bottom_app_bar_theme,
            'colorScheme': color_scheme,
            'dialogTheme': dialog_theme,
            'floatingActionButtonTheme': floating_action_button_theme,
            'navigationRailTheme': navigation_rail_theme,
            'typography': typography,
            'cupertinoOverrideTheme': cupertino_override_theme,
            'snackBarTheme': snack_bar_theme,
            'bottomSheetTheme': bottom_sheet_theme,
            'popupMenuTheme': popup_menu_theme,
            'bannerTheme': banner_theme,
            'dividerTheme': divider_theme,
            'buttonBarTheme': button_bar_theme,
            'bottomNavigationBarTheme': bottom_navigation_bar_theme,
            'timePickerTheme': time_picker_theme,
            'textButtonTheme': text_button_theme,
            'elevatedButtonTheme': elevated_button_theme,
            'outlinedButtonTheme': outlined_button_theme,
            'textSelectionTheme': text_selection_theme,
            'dataTableTheme': data_table_theme,
            'checkboxTheme': checkbox_theme,
            'radioTheme': radio_theme,
            'switchTheme': switch_theme,
            'progressIndicatorTheme': progress_indicator_theme,
            'fixTextFieldOutlineLabel': fix_text_field_outline_label,
            'useTextSelectionTheme': use_text_selection_theme,
        }

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
        cupertino_override_theme: Optional[NoDefaultCupertinoThemeData] = None,
    ):
        _o = ThemeData(
        )
        _o._nx_ = {
            '#t': ('ThemeData', 'raw'),
            'visualDensity': visual_density,
            'primaryColor': primary_color,
            'primaryColorBrightness': primary_color_brightness,
            'primaryColorLight': primary_color_light,
            'primaryColorDark': primary_color_dark,
            'canvasColor': canvas_color,
            'shadowColor': shadow_color,
            'accentColor': accent_color,
            'accentColorBrightness': accent_color_brightness,
            'scaffoldBackgroundColor': scaffold_background_color,
            'bottomAppBarColor': bottom_app_bar_color,
            'cardColor': card_color,
            'dividerColor': divider_color,
            'focusColor': focus_color,
            'hoverColor': hover_color,
            'highlightColor': highlight_color,
            'splashColor': splash_color,
            'splashFactory': splash_factory,
            'selectedRowColor': selected_row_color,
            'unselectedWidgetColor': unselected_widget_color,
            'disabledColor': disabled_color,
            'buttonTheme': button_theme,
            'buttonColor': button_color,
            'toggleButtonsTheme': toggle_buttons_theme,
            'secondaryHeaderColor': secondary_header_color,
            'textSelectionColor': text_selection_color,
            'cursorColor': cursor_color,
            'textSelectionHandleColor': text_selection_handle_color,
            'backgroundColor': background_color,
            'dialogBackgroundColor': dialog_background_color,
            'indicatorColor': indicator_color,
            'hintColor': hint_color,
            'errorColor': error_color,
            'toggleableActiveColor': toggleable_active_color,
            'textTheme': text_theme,
            'primaryTextTheme': primary_text_theme,
            'accentTextTheme': accent_text_theme,
            'inputDecorationTheme': input_decoration_theme,
            'iconTheme': icon_theme,
            'primaryIconTheme': primary_icon_theme,
            'accentIconTheme': accent_icon_theme,
            'sliderTheme': slider_theme,
            'tabBarTheme': tab_bar_theme,
            'tooltipTheme': tooltip_theme,
            'cardTheme': card_theme,
            'chipTheme': chip_theme,
            'platform': platform,
            'materialTapTargetSize': material_tap_target_size,
            'applyElevationOverlayColor': apply_elevation_overlay_color,
            'pageTransitionsTheme': page_transitions_theme,
            'appBarTheme': app_bar_theme,
            'scrollbarTheme': scrollbar_theme,
            'bottomAppBarTheme': bottom_app_bar_theme,
            'colorScheme': color_scheme,
            'dialogTheme': dialog_theme,
            'floatingActionButtonTheme': floating_action_button_theme,
            'navigationRailTheme': navigation_rail_theme,
            'typography': typography,
            'snackBarTheme': snack_bar_theme,
            'bottomSheetTheme': bottom_sheet_theme,
            'popupMenuTheme': popup_menu_theme,
            'bannerTheme': banner_theme,
            'dividerTheme': divider_theme,
            'buttonBarTheme': button_bar_theme,
            'bottomNavigationBarTheme': bottom_navigation_bar_theme,
            'timePickerTheme': time_picker_theme,
            'textButtonTheme': text_button_theme,
            'elevatedButtonTheme': elevated_button_theme,
            'outlinedButtonTheme': outlined_button_theme,
            'textSelectionTheme': text_selection_theme,
            'dataTableTheme': data_table_theme,
            'checkboxTheme': checkbox_theme,
            'radioTheme': radio_theme,
            'switchTheme': switch_theme,
            'progressIndicatorTheme': progress_indicator_theme,
            'fixTextFieldOutlineLabel': fix_text_field_outline_label,
            'useTextSelectionTheme': use_text_selection_theme,
            'cupertinoOverrideTheme': cupertino_override_theme,
        }
        return _o

    @staticmethod
    def from_(
        color_scheme: ColorScheme,
        text_theme: Optional[TextTheme] = None,
    ):
        _o = ThemeData(
        )
        _o._nx_ = {
            '#t': ('ThemeData', 'from'),
            'colorScheme': color_scheme,
            'textTheme': text_theme,
        }
        return _o

    @staticmethod
    def light(
    ):
        _o = ThemeData(
        )
        _o._nx_ = {
            '#t': ('ThemeData', 'light'),
        }
        return _o

    @staticmethod
    def dark(
    ):
        _o = ThemeData(
        )
        _o._nx_ = {
            '#t': ('ThemeData', 'dark'),
        }
        return _o

    @staticmethod
    def fallback(
    ):
        _o = ThemeData(
        )
        _o._nx_ = {
            '#t': ('ThemeData', 'fallback'),
        }
        return _o


# packages/flutter/lib/src/material/app.dart
class ThemeMode(Enum):
    system = 'system'
    light = 'light'
    dark = 'dark'


# packages/flutter/lib/src/widgets/localizations.dart
class LocalizationsDelegate(Object, ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('LocalizationsDelegate', ''),
        }


# packages/flutter/lib/src/widgets/shortcuts.dart
class ShortcutActivator(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ShortcutActivator', ''),
        }


# packages/flutter/lib/src/widgets/actions.dart
class Intent(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Intent', ''),
        }


Intent.do_nothing = Intent(
)
Intent.do_nothing._nx_ = {'#t': ('Intent', 'doNothing')}


# bin/cache/pkg/sky_engine/lib/core/type.dart
class Type(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Type', ''),
        }


# packages/flutter/lib/src/widgets/actions.dart
class Action(Object, ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Action', ''),
        }


# packages/flutter/lib/src/widgets/scroll_configuration.dart
class ScrollBehavior(Object):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ScrollBehavior', ''),
        }


# packages/flutter/lib/src/foundation/change_notifier.dart
class Listenable(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Listenable', ''),
        }

    @staticmethod
    def merge(
        listenables: List[Optional['Listenable']],
    ):
        _o = Listenable(
        )
        _o._nx_ = {
            '#t': ('Listenable', 'merge'),
            'listenables': listenables,
        }
        return _o


# packages/flutter/lib/src/foundation/change_notifier.dart
class ValueListenable(Listenable, ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ValueListenable', ''),
        }


# packages/flutter/lib/src/widgets/router.dart
class RouteInformation(Object):

    def __init__(
        self,
        location: Optional[str] = None,
        state: Optional[Object] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RouteInformation', ''),
            'location': location,
            'state': state,
        }


# packages/flutter/lib/src/widgets/router.dart
class RouteInformationProvider(ValueListenable[RouteInformation], ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RouteInformationProvider', ''),
        }


# packages/flutter/lib/src/widgets/router.dart
class RouteInformationParser(Object, ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RouteInformationParser', ''),
        }


# packages/flutter/lib/src/widgets/router.dart
class RouterDelegate(Listenable, ABC, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RouterDelegate', ''),
        }


# packages/flutter/lib/src/widgets/router.dart
class _CallbackHookProvider(Object, Generic[T]):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('_CallbackHookProvider', ''),
        }


# bin/cache/pkg/sky_engine/lib/async/future.dart
class FutureOr(Object, ABC, Generic[T]):
    pass


# bin/cache/pkg/sky_engine/lib/core/stacktrace.dart
class StackTrace(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('StackTrace', ''),
        }

    @staticmethod
    def from_string(
        stack_trace_string: str,
    ):
        _o = StackTrace(
        )
        _o._nx_ = {
            '#t': ('StackTrace', 'fromString'),
            'stackTraceString': stack_trace_string,
        }
        return _o


StackTrace.empty = StackTrace(
)
StackTrace.empty._nx_ = {'#t': ('StackTrace', 'empty')}


# bin/cache/pkg/sky_engine/lib/async/future.dart
class Future(Object, ABC, Generic[T]):

    def __init__(
        self,
        computation: Callable[[], FutureOr[T]],
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('Future', ''),
            'computation': computation,
        }

    @staticmethod
    def microtask(
        computation: Callable[[], FutureOr[T]],
    ):
        _o = Future(
            computation=_noop,
        )
        _o._nx_ = {
            '#t': ('Future', 'microtask'),
            'computation': computation,
        }
        return _o

    @staticmethod
    def sync(
        computation: Callable[[], FutureOr[T]],
    ):
        _o = Future(
            computation=_noop,
        )
        _o._nx_ = {
            '#t': ('Future', 'sync'),
            'computation': computation,
        }
        return _o

    @staticmethod
    def value(
        value: Optional[FutureOr[T]] = None,
    ):
        _o = Future(
            computation=_noop,
        )
        _o._nx_ = {
            '#t': ('Future', 'value'),
            'value': value,
        }
        return _o

    @staticmethod
    def error(
        error: Object,
        stack_trace: Optional[StackTrace] = None,
    ):
        _o = Future(
            computation=_noop,
        )
        _o._nx_ = {
            '#t': ('Future', 'error'),
            'error': error,
            'stackTrace': stack_trace,
        }
        return _o

    @staticmethod
    def delayed(
        duration: Duration,
        computation: Optional[Callable[[], FutureOr[T]]] = None,
    ):
        _o = Future(
            computation=_noop,
        )
        _o._nx_ = {
            '#t': ('Future', 'delayed'),
            'duration': duration,
            'computation': computation,
        }
        return _o


# packages/flutter/lib/src/widgets/router.dart
class BackButtonDispatcher(_CallbackHookProvider[Future[bool]], ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('BackButtonDispatcher', ''),
        }


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
        on_generate_route: Optional[Callable[[RouteSettings], Optional[Route[Any]]]] = None,
        on_generate_initial_routes: Optional[Callable[[str], List[Route[Any]]]] = None,
        on_unknown_route: Optional[Callable[[RouteSettings], Optional[Route[Any]]]] = None,
        navigator_observers: Optional[List[NavigatorObserver]] = None,
        builder: Optional[Callable[[BuildContext, Optional[Widget]], Widget]] = None,
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
        locale_list_resolution_callback: Optional[Callable[[Optional[List[Locale]], Iterable[Locale]], Optional[Locale]]] = None,
        locale_resolution_callback: Optional[Callable[[Optional[Locale], Iterable[Locale]], Optional[Locale]]] = None,
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
        self._nx_ = {
            '#t': ('MaterialApp', ''),
            'key': key,
            'navigatorKey': navigator_key,
            'scaffoldMessengerKey': scaffold_messenger_key,
            'home': home,
            'routes': routes,
            'initialRoute': initial_route,
            'onGenerateRoute': on_generate_route,
            'onGenerateInitialRoutes': on_generate_initial_routes,
            'onUnknownRoute': on_unknown_route,
            'navigatorObservers': navigator_observers,
            'builder': builder,
            'title': title,
            'onGenerateTitle': on_generate_title,
            'color': color,
            'theme': theme,
            'darkTheme': dark_theme,
            'highContrastTheme': high_contrast_theme,
            'highContrastDarkTheme': high_contrast_dark_theme,
            'themeMode': theme_mode,
            'locale': locale,
            'localizationsDelegates': localizations_delegates,
            'localeListResolutionCallback': locale_list_resolution_callback,
            'localeResolutionCallback': locale_resolution_callback,
            'supportedLocales': supported_locales,
            'debugShowMaterialGrid': debug_show_material_grid,
            'showPerformanceOverlay': show_performance_overlay,
            'checkerboardRasterCacheImages': checkerboard_raster_cache_images,
            'checkerboardOffscreenLayers': checkerboard_offscreen_layers,
            'showSemanticsDebugger': show_semantics_debugger,
            'debugShowCheckedModeBanner': debug_show_checked_mode_banner,
            'shortcuts': shortcuts,
            'actions': actions,
            'restorationScopeId': restoration_scope_id,
            'scrollBehavior': scroll_behavior,
            'useInheritedMediaQuery': use_inherited_media_query,
        }

    @staticmethod
    def router(
        route_information_parser: RouteInformationParser[Object],
        router_delegate: RouterDelegate[Object],
        key: Optional[Key] = None,
        scaffold_messenger_key: Optional[GlobalKey[ScaffoldMessengerState]] = None,
        route_information_provider: Optional[RouteInformationProvider] = None,
        back_button_dispatcher: Optional[BackButtonDispatcher] = None,
        builder: Optional[Callable[[BuildContext, Optional[Widget]], Widget]] = None,
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
        locale_list_resolution_callback: Optional[Callable[[Optional[List[Locale]], Iterable[Locale]], Optional[Locale]]] = None,
        locale_resolution_callback: Optional[Callable[[Optional[Locale], Iterable[Locale]], Optional[Locale]]] = None,
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
        _o._nx_ = {
            '#t': ('MaterialApp', 'router'),
            'routeInformationParser': route_information_parser,
            'routerDelegate': router_delegate,
            'key': key,
            'scaffoldMessengerKey': scaffold_messenger_key,
            'routeInformationProvider': route_information_provider,
            'backButtonDispatcher': back_button_dispatcher,
            'builder': builder,
            'title': title,
            'onGenerateTitle': on_generate_title,
            'color': color,
            'theme': theme,
            'darkTheme': dark_theme,
            'highContrastTheme': high_contrast_theme,
            'highContrastDarkTheme': high_contrast_dark_theme,
            'themeMode': theme_mode,
            'locale': locale,
            'localizationsDelegates': localizations_delegates,
            'localeListResolutionCallback': locale_list_resolution_callback,
            'localeResolutionCallback': locale_resolution_callback,
            'supportedLocales': supported_locales,
            'debugShowMaterialGrid': debug_show_material_grid,
            'showPerformanceOverlay': show_performance_overlay,
            'checkerboardRasterCacheImages': checkerboard_raster_cache_images,
            'checkerboardOffscreenLayers': checkerboard_offscreen_layers,
            'showSemanticsDebugger': show_semantics_debugger,
            'debugShowCheckedModeBanner': debug_show_checked_mode_banner,
            'shortcuts': shortcuts,
            'actions': actions,
            'restorationScopeId': restoration_scope_id,
            'scrollBehavior': scroll_behavior,
            'useInheritedMediaQuery': use_inherited_media_query,
        }
        return _o


# packages/flutter/lib/src/services/raw_keyboard.dart
class RawKeyEventData(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RawKeyEventData', ''),
        }


# packages/flutter/lib/src/services/raw_keyboard.dart
class RawKeyEvent(Object, ABC):

    def __init__(
        self,
        data: RawKeyEventData,
        character: Optional[str] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('RawKeyEvent', ''),
            'data': data,
            'character': character,
        }

    @staticmethod
    def from_message(
        message: Dict[str, Any],
    ):
        _o = RawKeyEvent(
            data=RawKeyEventData(),
        )
        _o._nx_ = {
            '#t': ('RawKeyEvent', 'fromMessage'),
            'message': message,
        }
        return _o


# packages/flutter/lib/src/widgets/focus_manager.dart
class KeyEventResult(Enum):
    handled = 'handled'
    ignored = 'ignored'
    skip_remaining_handlers = 'skipRemainingHandlers'


# packages/flutter/lib/src/services/keyboard_key.dart
class KeyboardKey(Object, ABC):

    def __init__(
        self,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('KeyboardKey', ''),
        }


# packages/flutter/lib/src/services/keyboard_key.dart
class PhysicalKeyboardKey(KeyboardKey):

    def __init__(
        self,
        usb_hid_usage: int,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('PhysicalKeyboardKey', ''),
            'usbHidUsage': usb_hid_usage,
        }


PhysicalKeyboardKey.hyper = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.hyper._nx_ = {'#t': ('PhysicalKeyboardKey', 'hyper')}
PhysicalKeyboardKey.super_key = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.super_key._nx_ = {'#t': ('PhysicalKeyboardKey', 'superKey')}
PhysicalKeyboardKey.fn = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.fn._nx_ = {'#t': ('PhysicalKeyboardKey', 'fn')}
PhysicalKeyboardKey.fn_lock = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.fn_lock._nx_ = {'#t': ('PhysicalKeyboardKey', 'fnLock')}
PhysicalKeyboardKey.suspend = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.suspend._nx_ = {'#t': ('PhysicalKeyboardKey', 'suspend')}
PhysicalKeyboardKey.resume = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.resume._nx_ = {'#t': ('PhysicalKeyboardKey', 'resume')}
PhysicalKeyboardKey.turbo = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.turbo._nx_ = {'#t': ('PhysicalKeyboardKey', 'turbo')}
PhysicalKeyboardKey.privacy_screen_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.privacy_screen_toggle._nx_ = {'#t': ('PhysicalKeyboardKey', 'privacyScreenToggle')}
PhysicalKeyboardKey.sleep = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.sleep._nx_ = {'#t': ('PhysicalKeyboardKey', 'sleep')}
PhysicalKeyboardKey.wake_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.wake_up._nx_ = {'#t': ('PhysicalKeyboardKey', 'wakeUp')}
PhysicalKeyboardKey.display_toggle_int_ext = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.display_toggle_int_ext._nx_ = {'#t': ('PhysicalKeyboardKey', 'displayToggleIntExt')}
PhysicalKeyboardKey.game_button1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button1._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton1')}
PhysicalKeyboardKey.game_button2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button2._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton2')}
PhysicalKeyboardKey.game_button3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button3._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton3')}
PhysicalKeyboardKey.game_button4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button4._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton4')}
PhysicalKeyboardKey.game_button5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button5._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton5')}
PhysicalKeyboardKey.game_button6 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button6._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton6')}
PhysicalKeyboardKey.game_button7 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button7._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton7')}
PhysicalKeyboardKey.game_button8 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button8._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton8')}
PhysicalKeyboardKey.game_button9 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button9._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton9')}
PhysicalKeyboardKey.game_button10 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button10._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton10')}
PhysicalKeyboardKey.game_button11 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button11._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton11')}
PhysicalKeyboardKey.game_button12 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button12._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton12')}
PhysicalKeyboardKey.game_button13 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button13._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton13')}
PhysicalKeyboardKey.game_button14 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button14._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton14')}
PhysicalKeyboardKey.game_button15 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button15._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton15')}
PhysicalKeyboardKey.game_button16 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button16._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButton16')}
PhysicalKeyboardKey.game_button_a = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_a._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonA')}
PhysicalKeyboardKey.game_button_b = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_b._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonB')}
PhysicalKeyboardKey.game_button_c = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_c._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonC')}
PhysicalKeyboardKey.game_button_left1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_left1._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonLeft1')}
PhysicalKeyboardKey.game_button_left2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_left2._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonLeft2')}
PhysicalKeyboardKey.game_button_mode = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_mode._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonMode')}
PhysicalKeyboardKey.game_button_right1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_right1._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonRight1')}
PhysicalKeyboardKey.game_button_right2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_right2._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonRight2')}
PhysicalKeyboardKey.game_button_select = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_select._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonSelect')}
PhysicalKeyboardKey.game_button_start = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_start._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonStart')}
PhysicalKeyboardKey.game_button_thumb_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_thumb_left._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonThumbLeft')}
PhysicalKeyboardKey.game_button_thumb_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_thumb_right._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonThumbRight')}
PhysicalKeyboardKey.game_button_x = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_x._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonX')}
PhysicalKeyboardKey.game_button_y = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_y._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonY')}
PhysicalKeyboardKey.game_button_z = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.game_button_z._nx_ = {'#t': ('PhysicalKeyboardKey', 'gameButtonZ')}
PhysicalKeyboardKey.usb_reserved = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.usb_reserved._nx_ = {'#t': ('PhysicalKeyboardKey', 'usbReserved')}
PhysicalKeyboardKey.usb_error_roll_over = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.usb_error_roll_over._nx_ = {'#t': ('PhysicalKeyboardKey', 'usbErrorRollOver')}
PhysicalKeyboardKey.usb_post_fail = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.usb_post_fail._nx_ = {'#t': ('PhysicalKeyboardKey', 'usbPostFail')}
PhysicalKeyboardKey.usb_error_undefined = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.usb_error_undefined._nx_ = {'#t': ('PhysicalKeyboardKey', 'usbErrorUndefined')}
PhysicalKeyboardKey.key_a = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_a._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyA')}
PhysicalKeyboardKey.key_b = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_b._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyB')}
PhysicalKeyboardKey.key_c = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_c._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyC')}
PhysicalKeyboardKey.key_d = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_d._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyD')}
PhysicalKeyboardKey.key_e = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_e._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyE')}
PhysicalKeyboardKey.key_f = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_f._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyF')}
PhysicalKeyboardKey.key_g = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_g._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyG')}
PhysicalKeyboardKey.key_h = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_h._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyH')}
PhysicalKeyboardKey.key_i = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_i._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyI')}
PhysicalKeyboardKey.key_j = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_j._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyJ')}
PhysicalKeyboardKey.key_k = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_k._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyK')}
PhysicalKeyboardKey.key_l = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_l._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyL')}
PhysicalKeyboardKey.key_m = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_m._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyM')}
PhysicalKeyboardKey.key_n = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_n._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyN')}
PhysicalKeyboardKey.key_o = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_o._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyO')}
PhysicalKeyboardKey.key_p = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_p._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyP')}
PhysicalKeyboardKey.key_q = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_q._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyQ')}
PhysicalKeyboardKey.key_r = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_r._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyR')}
PhysicalKeyboardKey.key_s = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_s._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyS')}
PhysicalKeyboardKey.key_t = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_t._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyT')}
PhysicalKeyboardKey.key_u = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_u._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyU')}
PhysicalKeyboardKey.key_v = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_v._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyV')}
PhysicalKeyboardKey.key_w = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_w._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyW')}
PhysicalKeyboardKey.key_x = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_x._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyX')}
PhysicalKeyboardKey.key_y = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_y._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyY')}
PhysicalKeyboardKey.key_z = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.key_z._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyZ')}
PhysicalKeyboardKey.digit1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit1._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit1')}
PhysicalKeyboardKey.digit2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit2._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit2')}
PhysicalKeyboardKey.digit3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit3._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit3')}
PhysicalKeyboardKey.digit4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit4._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit4')}
PhysicalKeyboardKey.digit5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit5._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit5')}
PhysicalKeyboardKey.digit6 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit6._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit6')}
PhysicalKeyboardKey.digit7 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit7._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit7')}
PhysicalKeyboardKey.digit8 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit8._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit8')}
PhysicalKeyboardKey.digit9 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit9._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit9')}
PhysicalKeyboardKey.digit0 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.digit0._nx_ = {'#t': ('PhysicalKeyboardKey', 'digit0')}
PhysicalKeyboardKey.enter = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.enter._nx_ = {'#t': ('PhysicalKeyboardKey', 'enter')}
PhysicalKeyboardKey.escape = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.escape._nx_ = {'#t': ('PhysicalKeyboardKey', 'escape')}
PhysicalKeyboardKey.backspace = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.backspace._nx_ = {'#t': ('PhysicalKeyboardKey', 'backspace')}
PhysicalKeyboardKey.tab = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.tab._nx_ = {'#t': ('PhysicalKeyboardKey', 'tab')}
PhysicalKeyboardKey.space = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.space._nx_ = {'#t': ('PhysicalKeyboardKey', 'space')}
PhysicalKeyboardKey.minus = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.minus._nx_ = {'#t': ('PhysicalKeyboardKey', 'minus')}
PhysicalKeyboardKey.equal = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.equal._nx_ = {'#t': ('PhysicalKeyboardKey', 'equal')}
PhysicalKeyboardKey.bracket_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.bracket_left._nx_ = {'#t': ('PhysicalKeyboardKey', 'bracketLeft')}
PhysicalKeyboardKey.bracket_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.bracket_right._nx_ = {'#t': ('PhysicalKeyboardKey', 'bracketRight')}
PhysicalKeyboardKey.backslash = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.backslash._nx_ = {'#t': ('PhysicalKeyboardKey', 'backslash')}
PhysicalKeyboardKey.semicolon = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.semicolon._nx_ = {'#t': ('PhysicalKeyboardKey', 'semicolon')}
PhysicalKeyboardKey.quote = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.quote._nx_ = {'#t': ('PhysicalKeyboardKey', 'quote')}
PhysicalKeyboardKey.backquote = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.backquote._nx_ = {'#t': ('PhysicalKeyboardKey', 'backquote')}
PhysicalKeyboardKey.comma = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.comma._nx_ = {'#t': ('PhysicalKeyboardKey', 'comma')}
PhysicalKeyboardKey.period = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.period._nx_ = {'#t': ('PhysicalKeyboardKey', 'period')}
PhysicalKeyboardKey.slash = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.slash._nx_ = {'#t': ('PhysicalKeyboardKey', 'slash')}
PhysicalKeyboardKey.caps_lock = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.caps_lock._nx_ = {'#t': ('PhysicalKeyboardKey', 'capsLock')}
PhysicalKeyboardKey.f1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f1._nx_ = {'#t': ('PhysicalKeyboardKey', 'f1')}
PhysicalKeyboardKey.f2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f2._nx_ = {'#t': ('PhysicalKeyboardKey', 'f2')}
PhysicalKeyboardKey.f3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f3._nx_ = {'#t': ('PhysicalKeyboardKey', 'f3')}
PhysicalKeyboardKey.f4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f4._nx_ = {'#t': ('PhysicalKeyboardKey', 'f4')}
PhysicalKeyboardKey.f5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f5._nx_ = {'#t': ('PhysicalKeyboardKey', 'f5')}
PhysicalKeyboardKey.f6 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f6._nx_ = {'#t': ('PhysicalKeyboardKey', 'f6')}
PhysicalKeyboardKey.f7 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f7._nx_ = {'#t': ('PhysicalKeyboardKey', 'f7')}
PhysicalKeyboardKey.f8 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f8._nx_ = {'#t': ('PhysicalKeyboardKey', 'f8')}
PhysicalKeyboardKey.f9 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f9._nx_ = {'#t': ('PhysicalKeyboardKey', 'f9')}
PhysicalKeyboardKey.f10 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f10._nx_ = {'#t': ('PhysicalKeyboardKey', 'f10')}
PhysicalKeyboardKey.f11 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f11._nx_ = {'#t': ('PhysicalKeyboardKey', 'f11')}
PhysicalKeyboardKey.f12 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f12._nx_ = {'#t': ('PhysicalKeyboardKey', 'f12')}
PhysicalKeyboardKey.print_screen = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.print_screen._nx_ = {'#t': ('PhysicalKeyboardKey', 'printScreen')}
PhysicalKeyboardKey.scroll_lock = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.scroll_lock._nx_ = {'#t': ('PhysicalKeyboardKey', 'scrollLock')}
PhysicalKeyboardKey.pause = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.pause._nx_ = {'#t': ('PhysicalKeyboardKey', 'pause')}
PhysicalKeyboardKey.insert = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.insert._nx_ = {'#t': ('PhysicalKeyboardKey', 'insert')}
PhysicalKeyboardKey.home = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.home._nx_ = {'#t': ('PhysicalKeyboardKey', 'home')}
PhysicalKeyboardKey.page_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.page_up._nx_ = {'#t': ('PhysicalKeyboardKey', 'pageUp')}
PhysicalKeyboardKey.delete = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.delete._nx_ = {'#t': ('PhysicalKeyboardKey', 'delete')}
PhysicalKeyboardKey.end = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.end._nx_ = {'#t': ('PhysicalKeyboardKey', 'end')}
PhysicalKeyboardKey.page_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.page_down._nx_ = {'#t': ('PhysicalKeyboardKey', 'pageDown')}
PhysicalKeyboardKey.arrow_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.arrow_right._nx_ = {'#t': ('PhysicalKeyboardKey', 'arrowRight')}
PhysicalKeyboardKey.arrow_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.arrow_left._nx_ = {'#t': ('PhysicalKeyboardKey', 'arrowLeft')}
PhysicalKeyboardKey.arrow_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.arrow_down._nx_ = {'#t': ('PhysicalKeyboardKey', 'arrowDown')}
PhysicalKeyboardKey.arrow_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.arrow_up._nx_ = {'#t': ('PhysicalKeyboardKey', 'arrowUp')}
PhysicalKeyboardKey.num_lock = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.num_lock._nx_ = {'#t': ('PhysicalKeyboardKey', 'numLock')}
PhysicalKeyboardKey.numpad_divide = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_divide._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadDivide')}
PhysicalKeyboardKey.numpad_multiply = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_multiply._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadMultiply')}
PhysicalKeyboardKey.numpad_subtract = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_subtract._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadSubtract')}
PhysicalKeyboardKey.numpad_add = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_add._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadAdd')}
PhysicalKeyboardKey.numpad_enter = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_enter._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadEnter')}
PhysicalKeyboardKey.numpad1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad1._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad1')}
PhysicalKeyboardKey.numpad2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad2._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad2')}
PhysicalKeyboardKey.numpad3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad3._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad3')}
PhysicalKeyboardKey.numpad4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad4._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad4')}
PhysicalKeyboardKey.numpad5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad5._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad5')}
PhysicalKeyboardKey.numpad6 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad6._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad6')}
PhysicalKeyboardKey.numpad7 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad7._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad7')}
PhysicalKeyboardKey.numpad8 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad8._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad8')}
PhysicalKeyboardKey.numpad9 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad9._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad9')}
PhysicalKeyboardKey.numpad0 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad0._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpad0')}
PhysicalKeyboardKey.numpad_decimal = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_decimal._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadDecimal')}
PhysicalKeyboardKey.intl_backslash = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.intl_backslash._nx_ = {'#t': ('PhysicalKeyboardKey', 'intlBackslash')}
PhysicalKeyboardKey.context_menu = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.context_menu._nx_ = {'#t': ('PhysicalKeyboardKey', 'contextMenu')}
PhysicalKeyboardKey.power = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.power._nx_ = {'#t': ('PhysicalKeyboardKey', 'power')}
PhysicalKeyboardKey.numpad_equal = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_equal._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadEqual')}
PhysicalKeyboardKey.f13 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f13._nx_ = {'#t': ('PhysicalKeyboardKey', 'f13')}
PhysicalKeyboardKey.f14 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f14._nx_ = {'#t': ('PhysicalKeyboardKey', 'f14')}
PhysicalKeyboardKey.f15 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f15._nx_ = {'#t': ('PhysicalKeyboardKey', 'f15')}
PhysicalKeyboardKey.f16 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f16._nx_ = {'#t': ('PhysicalKeyboardKey', 'f16')}
PhysicalKeyboardKey.f17 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f17._nx_ = {'#t': ('PhysicalKeyboardKey', 'f17')}
PhysicalKeyboardKey.f18 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f18._nx_ = {'#t': ('PhysicalKeyboardKey', 'f18')}
PhysicalKeyboardKey.f19 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f19._nx_ = {'#t': ('PhysicalKeyboardKey', 'f19')}
PhysicalKeyboardKey.f20 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f20._nx_ = {'#t': ('PhysicalKeyboardKey', 'f20')}
PhysicalKeyboardKey.f21 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f21._nx_ = {'#t': ('PhysicalKeyboardKey', 'f21')}
PhysicalKeyboardKey.f22 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f22._nx_ = {'#t': ('PhysicalKeyboardKey', 'f22')}
PhysicalKeyboardKey.f23 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f23._nx_ = {'#t': ('PhysicalKeyboardKey', 'f23')}
PhysicalKeyboardKey.f24 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.f24._nx_ = {'#t': ('PhysicalKeyboardKey', 'f24')}
PhysicalKeyboardKey.open = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.open._nx_ = {'#t': ('PhysicalKeyboardKey', 'open')}
PhysicalKeyboardKey.help = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.help._nx_ = {'#t': ('PhysicalKeyboardKey', 'help')}
PhysicalKeyboardKey.select = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.select._nx_ = {'#t': ('PhysicalKeyboardKey', 'select')}
PhysicalKeyboardKey.again = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.again._nx_ = {'#t': ('PhysicalKeyboardKey', 'again')}
PhysicalKeyboardKey.undo = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.undo._nx_ = {'#t': ('PhysicalKeyboardKey', 'undo')}
PhysicalKeyboardKey.cut = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.cut._nx_ = {'#t': ('PhysicalKeyboardKey', 'cut')}
PhysicalKeyboardKey.copy = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.copy._nx_ = {'#t': ('PhysicalKeyboardKey', 'copy')}
PhysicalKeyboardKey.paste = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.paste._nx_ = {'#t': ('PhysicalKeyboardKey', 'paste')}
PhysicalKeyboardKey.find = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.find._nx_ = {'#t': ('PhysicalKeyboardKey', 'find')}
PhysicalKeyboardKey.audio_volume_mute = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.audio_volume_mute._nx_ = {'#t': ('PhysicalKeyboardKey', 'audioVolumeMute')}
PhysicalKeyboardKey.audio_volume_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.audio_volume_up._nx_ = {'#t': ('PhysicalKeyboardKey', 'audioVolumeUp')}
PhysicalKeyboardKey.audio_volume_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.audio_volume_down._nx_ = {'#t': ('PhysicalKeyboardKey', 'audioVolumeDown')}
PhysicalKeyboardKey.numpad_comma = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_comma._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadComma')}
PhysicalKeyboardKey.intl_ro = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.intl_ro._nx_ = {'#t': ('PhysicalKeyboardKey', 'intlRo')}
PhysicalKeyboardKey.kana_mode = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.kana_mode._nx_ = {'#t': ('PhysicalKeyboardKey', 'kanaMode')}
PhysicalKeyboardKey.intl_yen = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.intl_yen._nx_ = {'#t': ('PhysicalKeyboardKey', 'intlYen')}
PhysicalKeyboardKey.convert = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.convert._nx_ = {'#t': ('PhysicalKeyboardKey', 'convert')}
PhysicalKeyboardKey.non_convert = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.non_convert._nx_ = {'#t': ('PhysicalKeyboardKey', 'nonConvert')}
PhysicalKeyboardKey.lang1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang1._nx_ = {'#t': ('PhysicalKeyboardKey', 'lang1')}
PhysicalKeyboardKey.lang2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang2._nx_ = {'#t': ('PhysicalKeyboardKey', 'lang2')}
PhysicalKeyboardKey.lang3 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang3._nx_ = {'#t': ('PhysicalKeyboardKey', 'lang3')}
PhysicalKeyboardKey.lang4 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang4._nx_ = {'#t': ('PhysicalKeyboardKey', 'lang4')}
PhysicalKeyboardKey.lang5 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lang5._nx_ = {'#t': ('PhysicalKeyboardKey', 'lang5')}
PhysicalKeyboardKey.abort = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.abort._nx_ = {'#t': ('PhysicalKeyboardKey', 'abort')}
PhysicalKeyboardKey.props = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.props._nx_ = {'#t': ('PhysicalKeyboardKey', 'props')}
PhysicalKeyboardKey.numpad_paren_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_paren_left._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadParenLeft')}
PhysicalKeyboardKey.numpad_paren_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_paren_right._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadParenRight')}
PhysicalKeyboardKey.numpad_backspace = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_backspace._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadBackspace')}
PhysicalKeyboardKey.numpad_memory_store = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_store._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadMemoryStore')}
PhysicalKeyboardKey.numpad_memory_recall = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_recall._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadMemoryRecall')}
PhysicalKeyboardKey.numpad_memory_clear = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_clear._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadMemoryClear')}
PhysicalKeyboardKey.numpad_memory_add = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_add._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadMemoryAdd')}
PhysicalKeyboardKey.numpad_memory_subtract = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_memory_subtract._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadMemorySubtract')}
PhysicalKeyboardKey.numpad_sign_change = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_sign_change._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadSignChange')}
PhysicalKeyboardKey.numpad_clear = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_clear._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadClear')}
PhysicalKeyboardKey.numpad_clear_entry = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.numpad_clear_entry._nx_ = {'#t': ('PhysicalKeyboardKey', 'numpadClearEntry')}
PhysicalKeyboardKey.control_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.control_left._nx_ = {'#t': ('PhysicalKeyboardKey', 'controlLeft')}
PhysicalKeyboardKey.shift_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.shift_left._nx_ = {'#t': ('PhysicalKeyboardKey', 'shiftLeft')}
PhysicalKeyboardKey.alt_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.alt_left._nx_ = {'#t': ('PhysicalKeyboardKey', 'altLeft')}
PhysicalKeyboardKey.meta_left = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.meta_left._nx_ = {'#t': ('PhysicalKeyboardKey', 'metaLeft')}
PhysicalKeyboardKey.control_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.control_right._nx_ = {'#t': ('PhysicalKeyboardKey', 'controlRight')}
PhysicalKeyboardKey.shift_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.shift_right._nx_ = {'#t': ('PhysicalKeyboardKey', 'shiftRight')}
PhysicalKeyboardKey.alt_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.alt_right._nx_ = {'#t': ('PhysicalKeyboardKey', 'altRight')}
PhysicalKeyboardKey.meta_right = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.meta_right._nx_ = {'#t': ('PhysicalKeyboardKey', 'metaRight')}
PhysicalKeyboardKey.info = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.info._nx_ = {'#t': ('PhysicalKeyboardKey', 'info')}
PhysicalKeyboardKey.closed_caption_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.closed_caption_toggle._nx_ = {'#t': ('PhysicalKeyboardKey', 'closedCaptionToggle')}
PhysicalKeyboardKey.brightness_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_up._nx_ = {'#t': ('PhysicalKeyboardKey', 'brightnessUp')}
PhysicalKeyboardKey.brightness_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_down._nx_ = {'#t': ('PhysicalKeyboardKey', 'brightnessDown')}
PhysicalKeyboardKey.brightness_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_toggle._nx_ = {'#t': ('PhysicalKeyboardKey', 'brightnessToggle')}
PhysicalKeyboardKey.brightness_minimum = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_minimum._nx_ = {'#t': ('PhysicalKeyboardKey', 'brightnessMinimum')}
PhysicalKeyboardKey.brightness_maximum = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_maximum._nx_ = {'#t': ('PhysicalKeyboardKey', 'brightnessMaximum')}
PhysicalKeyboardKey.brightness_auto = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.brightness_auto._nx_ = {'#t': ('PhysicalKeyboardKey', 'brightnessAuto')}
PhysicalKeyboardKey.kbd_illum_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.kbd_illum_up._nx_ = {'#t': ('PhysicalKeyboardKey', 'kbdIllumUp')}
PhysicalKeyboardKey.kbd_illum_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.kbd_illum_down._nx_ = {'#t': ('PhysicalKeyboardKey', 'kbdIllumDown')}
PhysicalKeyboardKey.media_last = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_last._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaLast')}
PhysicalKeyboardKey.launch_phone = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_phone._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchPhone')}
PhysicalKeyboardKey.program_guide = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.program_guide._nx_ = {'#t': ('PhysicalKeyboardKey', 'programGuide')}
PhysicalKeyboardKey.exit = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.exit._nx_ = {'#t': ('PhysicalKeyboardKey', 'exit')}
PhysicalKeyboardKey.channel_up = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.channel_up._nx_ = {'#t': ('PhysicalKeyboardKey', 'channelUp')}
PhysicalKeyboardKey.channel_down = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.channel_down._nx_ = {'#t': ('PhysicalKeyboardKey', 'channelDown')}
PhysicalKeyboardKey.media_play = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_play._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaPlay')}
PhysicalKeyboardKey.media_pause = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_pause._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaPause')}
PhysicalKeyboardKey.media_record = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_record._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaRecord')}
PhysicalKeyboardKey.media_fast_forward = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_fast_forward._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaFastForward')}
PhysicalKeyboardKey.media_rewind = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_rewind._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaRewind')}
PhysicalKeyboardKey.media_track_next = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_track_next._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaTrackNext')}
PhysicalKeyboardKey.media_track_previous = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_track_previous._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaTrackPrevious')}
PhysicalKeyboardKey.media_stop = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_stop._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaStop')}
PhysicalKeyboardKey.eject = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.eject._nx_ = {'#t': ('PhysicalKeyboardKey', 'eject')}
PhysicalKeyboardKey.media_play_pause = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_play_pause._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaPlayPause')}
PhysicalKeyboardKey.speech_input_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.speech_input_toggle._nx_ = {'#t': ('PhysicalKeyboardKey', 'speechInputToggle')}
PhysicalKeyboardKey.bass_boost = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.bass_boost._nx_ = {'#t': ('PhysicalKeyboardKey', 'bassBoost')}
PhysicalKeyboardKey.media_select = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.media_select._nx_ = {'#t': ('PhysicalKeyboardKey', 'mediaSelect')}
PhysicalKeyboardKey.launch_word_processor = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_word_processor._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchWordProcessor')}
PhysicalKeyboardKey.launch_spreadsheet = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_spreadsheet._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchSpreadsheet')}
PhysicalKeyboardKey.launch_mail = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_mail._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchMail')}
PhysicalKeyboardKey.launch_contacts = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_contacts._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchContacts')}
PhysicalKeyboardKey.launch_calendar = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_calendar._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchCalendar')}
PhysicalKeyboardKey.launch_app2 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_app2._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchApp2')}
PhysicalKeyboardKey.launch_app1 = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_app1._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchApp1')}
PhysicalKeyboardKey.launch_internet_browser = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_internet_browser._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchInternetBrowser')}
PhysicalKeyboardKey.log_off = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.log_off._nx_ = {'#t': ('PhysicalKeyboardKey', 'logOff')}
PhysicalKeyboardKey.lock_screen = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.lock_screen._nx_ = {'#t': ('PhysicalKeyboardKey', 'lockScreen')}
PhysicalKeyboardKey.launch_control_panel = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_control_panel._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchControlPanel')}
PhysicalKeyboardKey.select_task = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.select_task._nx_ = {'#t': ('PhysicalKeyboardKey', 'selectTask')}
PhysicalKeyboardKey.launch_documents = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_documents._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchDocuments')}
PhysicalKeyboardKey.spell_check = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.spell_check._nx_ = {'#t': ('PhysicalKeyboardKey', 'spellCheck')}
PhysicalKeyboardKey.launch_keyboard_layout = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_keyboard_layout._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchKeyboardLayout')}
PhysicalKeyboardKey.launch_screen_saver = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_screen_saver._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchScreenSaver')}
PhysicalKeyboardKey.launch_audio_browser = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_audio_browser._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchAudioBrowser')}
PhysicalKeyboardKey.launch_assistant = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.launch_assistant._nx_ = {'#t': ('PhysicalKeyboardKey', 'launchAssistant')}
PhysicalKeyboardKey.new_key = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.new_key._nx_ = {'#t': ('PhysicalKeyboardKey', 'newKey')}
PhysicalKeyboardKey.close = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.close._nx_ = {'#t': ('PhysicalKeyboardKey', 'close')}
PhysicalKeyboardKey.save = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.save._nx_ = {'#t': ('PhysicalKeyboardKey', 'save')}
PhysicalKeyboardKey.print = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.print._nx_ = {'#t': ('PhysicalKeyboardKey', 'print')}
PhysicalKeyboardKey.browser_search = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_search._nx_ = {'#t': ('PhysicalKeyboardKey', 'browserSearch')}
PhysicalKeyboardKey.browser_home = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_home._nx_ = {'#t': ('PhysicalKeyboardKey', 'browserHome')}
PhysicalKeyboardKey.browser_back = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_back._nx_ = {'#t': ('PhysicalKeyboardKey', 'browserBack')}
PhysicalKeyboardKey.browser_forward = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_forward._nx_ = {'#t': ('PhysicalKeyboardKey', 'browserForward')}
PhysicalKeyboardKey.browser_stop = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_stop._nx_ = {'#t': ('PhysicalKeyboardKey', 'browserStop')}
PhysicalKeyboardKey.browser_refresh = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_refresh._nx_ = {'#t': ('PhysicalKeyboardKey', 'browserRefresh')}
PhysicalKeyboardKey.browser_favorites = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.browser_favorites._nx_ = {'#t': ('PhysicalKeyboardKey', 'browserFavorites')}
PhysicalKeyboardKey.zoom_in = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.zoom_in._nx_ = {'#t': ('PhysicalKeyboardKey', 'zoomIn')}
PhysicalKeyboardKey.zoom_out = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.zoom_out._nx_ = {'#t': ('PhysicalKeyboardKey', 'zoomOut')}
PhysicalKeyboardKey.zoom_toggle = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.zoom_toggle._nx_ = {'#t': ('PhysicalKeyboardKey', 'zoomToggle')}
PhysicalKeyboardKey.redo = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.redo._nx_ = {'#t': ('PhysicalKeyboardKey', 'redo')}
PhysicalKeyboardKey.mail_reply = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.mail_reply._nx_ = {'#t': ('PhysicalKeyboardKey', 'mailReply')}
PhysicalKeyboardKey.mail_forward = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.mail_forward._nx_ = {'#t': ('PhysicalKeyboardKey', 'mailForward')}
PhysicalKeyboardKey.mail_send = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.mail_send._nx_ = {'#t': ('PhysicalKeyboardKey', 'mailSend')}
PhysicalKeyboardKey.keyboard_layout_select = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.keyboard_layout_select._nx_ = {'#t': ('PhysicalKeyboardKey', 'keyboardLayoutSelect')}
PhysicalKeyboardKey.show_all_windows = PhysicalKeyboardKey(
    usb_hid_usage=0,
)
PhysicalKeyboardKey.show_all_windows._nx_ = {'#t': ('PhysicalKeyboardKey', 'showAllWindows')}


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('LogicalKeyboardKey', ''),
            'keyId': key_id,
        }


LogicalKeyboardKey.space = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.space._nx_ = {'#t': ('LogicalKeyboardKey', 'space')}
LogicalKeyboardKey.exclamation = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.exclamation._nx_ = {'#t': ('LogicalKeyboardKey', 'exclamation')}
LogicalKeyboardKey.quote = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.quote._nx_ = {'#t': ('LogicalKeyboardKey', 'quote')}
LogicalKeyboardKey.number_sign = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.number_sign._nx_ = {'#t': ('LogicalKeyboardKey', 'numberSign')}
LogicalKeyboardKey.dollar = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.dollar._nx_ = {'#t': ('LogicalKeyboardKey', 'dollar')}
LogicalKeyboardKey.percent = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.percent._nx_ = {'#t': ('LogicalKeyboardKey', 'percent')}
LogicalKeyboardKey.ampersand = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.ampersand._nx_ = {'#t': ('LogicalKeyboardKey', 'ampersand')}
LogicalKeyboardKey.quote_single = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.quote_single._nx_ = {'#t': ('LogicalKeyboardKey', 'quoteSingle')}
LogicalKeyboardKey.parenthesis_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.parenthesis_left._nx_ = {'#t': ('LogicalKeyboardKey', 'parenthesisLeft')}
LogicalKeyboardKey.parenthesis_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.parenthesis_right._nx_ = {'#t': ('LogicalKeyboardKey', 'parenthesisRight')}
LogicalKeyboardKey.asterisk = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.asterisk._nx_ = {'#t': ('LogicalKeyboardKey', 'asterisk')}
LogicalKeyboardKey.add = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.add._nx_ = {'#t': ('LogicalKeyboardKey', 'add')}
LogicalKeyboardKey.comma = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.comma._nx_ = {'#t': ('LogicalKeyboardKey', 'comma')}
LogicalKeyboardKey.minus = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.minus._nx_ = {'#t': ('LogicalKeyboardKey', 'minus')}
LogicalKeyboardKey.period = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.period._nx_ = {'#t': ('LogicalKeyboardKey', 'period')}
LogicalKeyboardKey.slash = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.slash._nx_ = {'#t': ('LogicalKeyboardKey', 'slash')}
LogicalKeyboardKey.digit0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit0._nx_ = {'#t': ('LogicalKeyboardKey', 'digit0')}
LogicalKeyboardKey.digit1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit1._nx_ = {'#t': ('LogicalKeyboardKey', 'digit1')}
LogicalKeyboardKey.digit2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit2._nx_ = {'#t': ('LogicalKeyboardKey', 'digit2')}
LogicalKeyboardKey.digit3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit3._nx_ = {'#t': ('LogicalKeyboardKey', 'digit3')}
LogicalKeyboardKey.digit4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit4._nx_ = {'#t': ('LogicalKeyboardKey', 'digit4')}
LogicalKeyboardKey.digit5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit5._nx_ = {'#t': ('LogicalKeyboardKey', 'digit5')}
LogicalKeyboardKey.digit6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit6._nx_ = {'#t': ('LogicalKeyboardKey', 'digit6')}
LogicalKeyboardKey.digit7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit7._nx_ = {'#t': ('LogicalKeyboardKey', 'digit7')}
LogicalKeyboardKey.digit8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit8._nx_ = {'#t': ('LogicalKeyboardKey', 'digit8')}
LogicalKeyboardKey.digit9 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.digit9._nx_ = {'#t': ('LogicalKeyboardKey', 'digit9')}
LogicalKeyboardKey.colon = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.colon._nx_ = {'#t': ('LogicalKeyboardKey', 'colon')}
LogicalKeyboardKey.semicolon = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.semicolon._nx_ = {'#t': ('LogicalKeyboardKey', 'semicolon')}
LogicalKeyboardKey.less = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.less._nx_ = {'#t': ('LogicalKeyboardKey', 'less')}
LogicalKeyboardKey.equal = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.equal._nx_ = {'#t': ('LogicalKeyboardKey', 'equal')}
LogicalKeyboardKey.greater = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.greater._nx_ = {'#t': ('LogicalKeyboardKey', 'greater')}
LogicalKeyboardKey.question = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.question._nx_ = {'#t': ('LogicalKeyboardKey', 'question')}
LogicalKeyboardKey.at = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.at._nx_ = {'#t': ('LogicalKeyboardKey', 'at')}
LogicalKeyboardKey.bracket_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.bracket_left._nx_ = {'#t': ('LogicalKeyboardKey', 'bracketLeft')}
LogicalKeyboardKey.backslash = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.backslash._nx_ = {'#t': ('LogicalKeyboardKey', 'backslash')}
LogicalKeyboardKey.bracket_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.bracket_right._nx_ = {'#t': ('LogicalKeyboardKey', 'bracketRight')}
LogicalKeyboardKey.caret = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.caret._nx_ = {'#t': ('LogicalKeyboardKey', 'caret')}
LogicalKeyboardKey.underscore = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.underscore._nx_ = {'#t': ('LogicalKeyboardKey', 'underscore')}
LogicalKeyboardKey.backquote = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.backquote._nx_ = {'#t': ('LogicalKeyboardKey', 'backquote')}
LogicalKeyboardKey.key_a = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_a._nx_ = {'#t': ('LogicalKeyboardKey', 'keyA')}
LogicalKeyboardKey.key_b = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_b._nx_ = {'#t': ('LogicalKeyboardKey', 'keyB')}
LogicalKeyboardKey.key_c = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_c._nx_ = {'#t': ('LogicalKeyboardKey', 'keyC')}
LogicalKeyboardKey.key_d = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_d._nx_ = {'#t': ('LogicalKeyboardKey', 'keyD')}
LogicalKeyboardKey.key_e = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_e._nx_ = {'#t': ('LogicalKeyboardKey', 'keyE')}
LogicalKeyboardKey.key_f = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_f._nx_ = {'#t': ('LogicalKeyboardKey', 'keyF')}
LogicalKeyboardKey.key_g = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_g._nx_ = {'#t': ('LogicalKeyboardKey', 'keyG')}
LogicalKeyboardKey.key_h = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_h._nx_ = {'#t': ('LogicalKeyboardKey', 'keyH')}
LogicalKeyboardKey.key_i = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_i._nx_ = {'#t': ('LogicalKeyboardKey', 'keyI')}
LogicalKeyboardKey.key_j = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_j._nx_ = {'#t': ('LogicalKeyboardKey', 'keyJ')}
LogicalKeyboardKey.key_k = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_k._nx_ = {'#t': ('LogicalKeyboardKey', 'keyK')}
LogicalKeyboardKey.key_l = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_l._nx_ = {'#t': ('LogicalKeyboardKey', 'keyL')}
LogicalKeyboardKey.key_m = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_m._nx_ = {'#t': ('LogicalKeyboardKey', 'keyM')}
LogicalKeyboardKey.key_n = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_n._nx_ = {'#t': ('LogicalKeyboardKey', 'keyN')}
LogicalKeyboardKey.key_o = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_o._nx_ = {'#t': ('LogicalKeyboardKey', 'keyO')}
LogicalKeyboardKey.key_p = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_p._nx_ = {'#t': ('LogicalKeyboardKey', 'keyP')}
LogicalKeyboardKey.key_q = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_q._nx_ = {'#t': ('LogicalKeyboardKey', 'keyQ')}
LogicalKeyboardKey.key_r = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_r._nx_ = {'#t': ('LogicalKeyboardKey', 'keyR')}
LogicalKeyboardKey.key_s = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_s._nx_ = {'#t': ('LogicalKeyboardKey', 'keyS')}
LogicalKeyboardKey.key_t = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_t._nx_ = {'#t': ('LogicalKeyboardKey', 'keyT')}
LogicalKeyboardKey.key_u = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_u._nx_ = {'#t': ('LogicalKeyboardKey', 'keyU')}
LogicalKeyboardKey.key_v = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_v._nx_ = {'#t': ('LogicalKeyboardKey', 'keyV')}
LogicalKeyboardKey.key_w = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_w._nx_ = {'#t': ('LogicalKeyboardKey', 'keyW')}
LogicalKeyboardKey.key_x = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_x._nx_ = {'#t': ('LogicalKeyboardKey', 'keyX')}
LogicalKeyboardKey.key_y = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_y._nx_ = {'#t': ('LogicalKeyboardKey', 'keyY')}
LogicalKeyboardKey.key_z = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key_z._nx_ = {'#t': ('LogicalKeyboardKey', 'keyZ')}
LogicalKeyboardKey.brace_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.brace_left._nx_ = {'#t': ('LogicalKeyboardKey', 'braceLeft')}
LogicalKeyboardKey.bar = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.bar._nx_ = {'#t': ('LogicalKeyboardKey', 'bar')}
LogicalKeyboardKey.brace_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.brace_right._nx_ = {'#t': ('LogicalKeyboardKey', 'braceRight')}
LogicalKeyboardKey.tilde = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tilde._nx_ = {'#t': ('LogicalKeyboardKey', 'tilde')}
LogicalKeyboardKey.unidentified = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.unidentified._nx_ = {'#t': ('LogicalKeyboardKey', 'unidentified')}
LogicalKeyboardKey.backspace = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.backspace._nx_ = {'#t': ('LogicalKeyboardKey', 'backspace')}
LogicalKeyboardKey.tab = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tab._nx_ = {'#t': ('LogicalKeyboardKey', 'tab')}
LogicalKeyboardKey.enter = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.enter._nx_ = {'#t': ('LogicalKeyboardKey', 'enter')}
LogicalKeyboardKey.escape = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.escape._nx_ = {'#t': ('LogicalKeyboardKey', 'escape')}
LogicalKeyboardKey.delete = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.delete._nx_ = {'#t': ('LogicalKeyboardKey', 'delete')}
LogicalKeyboardKey.accel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.accel._nx_ = {'#t': ('LogicalKeyboardKey', 'accel')}
LogicalKeyboardKey.alt_graph = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alt_graph._nx_ = {'#t': ('LogicalKeyboardKey', 'altGraph')}
LogicalKeyboardKey.caps_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.caps_lock._nx_ = {'#t': ('LogicalKeyboardKey', 'capsLock')}
LogicalKeyboardKey.fn = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.fn._nx_ = {'#t': ('LogicalKeyboardKey', 'fn')}
LogicalKeyboardKey.fn_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.fn_lock._nx_ = {'#t': ('LogicalKeyboardKey', 'fnLock')}
LogicalKeyboardKey.hyper = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hyper._nx_ = {'#t': ('LogicalKeyboardKey', 'hyper')}
LogicalKeyboardKey.num_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.num_lock._nx_ = {'#t': ('LogicalKeyboardKey', 'numLock')}
LogicalKeyboardKey.scroll_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.scroll_lock._nx_ = {'#t': ('LogicalKeyboardKey', 'scrollLock')}
LogicalKeyboardKey.super_key = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.super_key._nx_ = {'#t': ('LogicalKeyboardKey', 'superKey')}
LogicalKeyboardKey.symbol = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.symbol._nx_ = {'#t': ('LogicalKeyboardKey', 'symbol')}
LogicalKeyboardKey.symbol_lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.symbol_lock._nx_ = {'#t': ('LogicalKeyboardKey', 'symbolLock')}
LogicalKeyboardKey.shift_level5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.shift_level5._nx_ = {'#t': ('LogicalKeyboardKey', 'shiftLevel5')}
LogicalKeyboardKey.arrow_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.arrow_down._nx_ = {'#t': ('LogicalKeyboardKey', 'arrowDown')}
LogicalKeyboardKey.arrow_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.arrow_left._nx_ = {'#t': ('LogicalKeyboardKey', 'arrowLeft')}
LogicalKeyboardKey.arrow_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.arrow_right._nx_ = {'#t': ('LogicalKeyboardKey', 'arrowRight')}
LogicalKeyboardKey.arrow_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.arrow_up._nx_ = {'#t': ('LogicalKeyboardKey', 'arrowUp')}
LogicalKeyboardKey.end = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.end._nx_ = {'#t': ('LogicalKeyboardKey', 'end')}
LogicalKeyboardKey.home = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.home._nx_ = {'#t': ('LogicalKeyboardKey', 'home')}
LogicalKeyboardKey.page_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.page_down._nx_ = {'#t': ('LogicalKeyboardKey', 'pageDown')}
LogicalKeyboardKey.page_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.page_up._nx_ = {'#t': ('LogicalKeyboardKey', 'pageUp')}
LogicalKeyboardKey.clear = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.clear._nx_ = {'#t': ('LogicalKeyboardKey', 'clear')}
LogicalKeyboardKey.copy = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.copy._nx_ = {'#t': ('LogicalKeyboardKey', 'copy')}
LogicalKeyboardKey.cr_sel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.cr_sel._nx_ = {'#t': ('LogicalKeyboardKey', 'crSel')}
LogicalKeyboardKey.cut = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.cut._nx_ = {'#t': ('LogicalKeyboardKey', 'cut')}
LogicalKeyboardKey.erase_eof = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.erase_eof._nx_ = {'#t': ('LogicalKeyboardKey', 'eraseEof')}
LogicalKeyboardKey.ex_sel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.ex_sel._nx_ = {'#t': ('LogicalKeyboardKey', 'exSel')}
LogicalKeyboardKey.insert = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.insert._nx_ = {'#t': ('LogicalKeyboardKey', 'insert')}
LogicalKeyboardKey.paste = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.paste._nx_ = {'#t': ('LogicalKeyboardKey', 'paste')}
LogicalKeyboardKey.redo = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.redo._nx_ = {'#t': ('LogicalKeyboardKey', 'redo')}
LogicalKeyboardKey.undo = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.undo._nx_ = {'#t': ('LogicalKeyboardKey', 'undo')}
LogicalKeyboardKey.accept = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.accept._nx_ = {'#t': ('LogicalKeyboardKey', 'accept')}
LogicalKeyboardKey.again = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.again._nx_ = {'#t': ('LogicalKeyboardKey', 'again')}
LogicalKeyboardKey.attn = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.attn._nx_ = {'#t': ('LogicalKeyboardKey', 'attn')}
LogicalKeyboardKey.cancel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.cancel._nx_ = {'#t': ('LogicalKeyboardKey', 'cancel')}
LogicalKeyboardKey.context_menu = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.context_menu._nx_ = {'#t': ('LogicalKeyboardKey', 'contextMenu')}
LogicalKeyboardKey.execute = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.execute._nx_ = {'#t': ('LogicalKeyboardKey', 'execute')}
LogicalKeyboardKey.find = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.find._nx_ = {'#t': ('LogicalKeyboardKey', 'find')}
LogicalKeyboardKey.help = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.help._nx_ = {'#t': ('LogicalKeyboardKey', 'help')}
LogicalKeyboardKey.pause = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.pause._nx_ = {'#t': ('LogicalKeyboardKey', 'pause')}
LogicalKeyboardKey.play = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.play._nx_ = {'#t': ('LogicalKeyboardKey', 'play')}
LogicalKeyboardKey.props = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.props._nx_ = {'#t': ('LogicalKeyboardKey', 'props')}
LogicalKeyboardKey.select = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.select._nx_ = {'#t': ('LogicalKeyboardKey', 'select')}
LogicalKeyboardKey.zoom_in = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zoom_in._nx_ = {'#t': ('LogicalKeyboardKey', 'zoomIn')}
LogicalKeyboardKey.zoom_out = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zoom_out._nx_ = {'#t': ('LogicalKeyboardKey', 'zoomOut')}
LogicalKeyboardKey.brightness_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.brightness_down._nx_ = {'#t': ('LogicalKeyboardKey', 'brightnessDown')}
LogicalKeyboardKey.brightness_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.brightness_up._nx_ = {'#t': ('LogicalKeyboardKey', 'brightnessUp')}
LogicalKeyboardKey.camera = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.camera._nx_ = {'#t': ('LogicalKeyboardKey', 'camera')}
LogicalKeyboardKey.eject = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.eject._nx_ = {'#t': ('LogicalKeyboardKey', 'eject')}
LogicalKeyboardKey.log_off = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.log_off._nx_ = {'#t': ('LogicalKeyboardKey', 'logOff')}
LogicalKeyboardKey.power = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.power._nx_ = {'#t': ('LogicalKeyboardKey', 'power')}
LogicalKeyboardKey.power_off = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.power_off._nx_ = {'#t': ('LogicalKeyboardKey', 'powerOff')}
LogicalKeyboardKey.print_screen = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.print_screen._nx_ = {'#t': ('LogicalKeyboardKey', 'printScreen')}
LogicalKeyboardKey.hibernate = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hibernate._nx_ = {'#t': ('LogicalKeyboardKey', 'hibernate')}
LogicalKeyboardKey.standby = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.standby._nx_ = {'#t': ('LogicalKeyboardKey', 'standby')}
LogicalKeyboardKey.wake_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.wake_up._nx_ = {'#t': ('LogicalKeyboardKey', 'wakeUp')}
LogicalKeyboardKey.all_candidates = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.all_candidates._nx_ = {'#t': ('LogicalKeyboardKey', 'allCandidates')}
LogicalKeyboardKey.alphanumeric = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alphanumeric._nx_ = {'#t': ('LogicalKeyboardKey', 'alphanumeric')}
LogicalKeyboardKey.code_input = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.code_input._nx_ = {'#t': ('LogicalKeyboardKey', 'codeInput')}
LogicalKeyboardKey.compose = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.compose._nx_ = {'#t': ('LogicalKeyboardKey', 'compose')}
LogicalKeyboardKey.convert = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.convert._nx_ = {'#t': ('LogicalKeyboardKey', 'convert')}
LogicalKeyboardKey.final_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.final_mode._nx_ = {'#t': ('LogicalKeyboardKey', 'finalMode')}
LogicalKeyboardKey.group_first = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.group_first._nx_ = {'#t': ('LogicalKeyboardKey', 'groupFirst')}
LogicalKeyboardKey.group_last = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.group_last._nx_ = {'#t': ('LogicalKeyboardKey', 'groupLast')}
LogicalKeyboardKey.group_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.group_next._nx_ = {'#t': ('LogicalKeyboardKey', 'groupNext')}
LogicalKeyboardKey.group_previous = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.group_previous._nx_ = {'#t': ('LogicalKeyboardKey', 'groupPrevious')}
LogicalKeyboardKey.mode_change = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.mode_change._nx_ = {'#t': ('LogicalKeyboardKey', 'modeChange')}
LogicalKeyboardKey.next_candidate = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.next_candidate._nx_ = {'#t': ('LogicalKeyboardKey', 'nextCandidate')}
LogicalKeyboardKey.non_convert = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.non_convert._nx_ = {'#t': ('LogicalKeyboardKey', 'nonConvert')}
LogicalKeyboardKey.previous_candidate = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.previous_candidate._nx_ = {'#t': ('LogicalKeyboardKey', 'previousCandidate')}
LogicalKeyboardKey.process = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.process._nx_ = {'#t': ('LogicalKeyboardKey', 'process')}
LogicalKeyboardKey.single_candidate = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.single_candidate._nx_ = {'#t': ('LogicalKeyboardKey', 'singleCandidate')}
LogicalKeyboardKey.hangul_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hangul_mode._nx_ = {'#t': ('LogicalKeyboardKey', 'hangulMode')}
LogicalKeyboardKey.hanja_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hanja_mode._nx_ = {'#t': ('LogicalKeyboardKey', 'hanjaMode')}
LogicalKeyboardKey.junja_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.junja_mode._nx_ = {'#t': ('LogicalKeyboardKey', 'junjaMode')}
LogicalKeyboardKey.eisu = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.eisu._nx_ = {'#t': ('LogicalKeyboardKey', 'eisu')}
LogicalKeyboardKey.hankaku = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hankaku._nx_ = {'#t': ('LogicalKeyboardKey', 'hankaku')}
LogicalKeyboardKey.hiragana = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hiragana._nx_ = {'#t': ('LogicalKeyboardKey', 'hiragana')}
LogicalKeyboardKey.hiragana_katakana = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.hiragana_katakana._nx_ = {'#t': ('LogicalKeyboardKey', 'hiraganaKatakana')}
LogicalKeyboardKey.kana_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.kana_mode._nx_ = {'#t': ('LogicalKeyboardKey', 'kanaMode')}
LogicalKeyboardKey.kanji_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.kanji_mode._nx_ = {'#t': ('LogicalKeyboardKey', 'kanjiMode')}
LogicalKeyboardKey.katakana = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.katakana._nx_ = {'#t': ('LogicalKeyboardKey', 'katakana')}
LogicalKeyboardKey.romaji = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.romaji._nx_ = {'#t': ('LogicalKeyboardKey', 'romaji')}
LogicalKeyboardKey.zenkaku = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zenkaku._nx_ = {'#t': ('LogicalKeyboardKey', 'zenkaku')}
LogicalKeyboardKey.zenkaku_hankaku = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zenkaku_hankaku._nx_ = {'#t': ('LogicalKeyboardKey', 'zenkakuHankaku')}
LogicalKeyboardKey.f1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f1._nx_ = {'#t': ('LogicalKeyboardKey', 'f1')}
LogicalKeyboardKey.f2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f2._nx_ = {'#t': ('LogicalKeyboardKey', 'f2')}
LogicalKeyboardKey.f3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f3._nx_ = {'#t': ('LogicalKeyboardKey', 'f3')}
LogicalKeyboardKey.f4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f4._nx_ = {'#t': ('LogicalKeyboardKey', 'f4')}
LogicalKeyboardKey.f5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f5._nx_ = {'#t': ('LogicalKeyboardKey', 'f5')}
LogicalKeyboardKey.f6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f6._nx_ = {'#t': ('LogicalKeyboardKey', 'f6')}
LogicalKeyboardKey.f7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f7._nx_ = {'#t': ('LogicalKeyboardKey', 'f7')}
LogicalKeyboardKey.f8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f8._nx_ = {'#t': ('LogicalKeyboardKey', 'f8')}
LogicalKeyboardKey.f9 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f9._nx_ = {'#t': ('LogicalKeyboardKey', 'f9')}
LogicalKeyboardKey.f10 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f10._nx_ = {'#t': ('LogicalKeyboardKey', 'f10')}
LogicalKeyboardKey.f11 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f11._nx_ = {'#t': ('LogicalKeyboardKey', 'f11')}
LogicalKeyboardKey.f12 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f12._nx_ = {'#t': ('LogicalKeyboardKey', 'f12')}
LogicalKeyboardKey.f13 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f13._nx_ = {'#t': ('LogicalKeyboardKey', 'f13')}
LogicalKeyboardKey.f14 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f14._nx_ = {'#t': ('LogicalKeyboardKey', 'f14')}
LogicalKeyboardKey.f15 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f15._nx_ = {'#t': ('LogicalKeyboardKey', 'f15')}
LogicalKeyboardKey.f16 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f16._nx_ = {'#t': ('LogicalKeyboardKey', 'f16')}
LogicalKeyboardKey.f17 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f17._nx_ = {'#t': ('LogicalKeyboardKey', 'f17')}
LogicalKeyboardKey.f18 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f18._nx_ = {'#t': ('LogicalKeyboardKey', 'f18')}
LogicalKeyboardKey.f19 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f19._nx_ = {'#t': ('LogicalKeyboardKey', 'f19')}
LogicalKeyboardKey.f20 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f20._nx_ = {'#t': ('LogicalKeyboardKey', 'f20')}
LogicalKeyboardKey.f21 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f21._nx_ = {'#t': ('LogicalKeyboardKey', 'f21')}
LogicalKeyboardKey.f22 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f22._nx_ = {'#t': ('LogicalKeyboardKey', 'f22')}
LogicalKeyboardKey.f23 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f23._nx_ = {'#t': ('LogicalKeyboardKey', 'f23')}
LogicalKeyboardKey.f24 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.f24._nx_ = {'#t': ('LogicalKeyboardKey', 'f24')}
LogicalKeyboardKey.soft1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft1._nx_ = {'#t': ('LogicalKeyboardKey', 'soft1')}
LogicalKeyboardKey.soft2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft2._nx_ = {'#t': ('LogicalKeyboardKey', 'soft2')}
LogicalKeyboardKey.soft3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft3._nx_ = {'#t': ('LogicalKeyboardKey', 'soft3')}
LogicalKeyboardKey.soft4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft4._nx_ = {'#t': ('LogicalKeyboardKey', 'soft4')}
LogicalKeyboardKey.soft5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft5._nx_ = {'#t': ('LogicalKeyboardKey', 'soft5')}
LogicalKeyboardKey.soft6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft6._nx_ = {'#t': ('LogicalKeyboardKey', 'soft6')}
LogicalKeyboardKey.soft7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft7._nx_ = {'#t': ('LogicalKeyboardKey', 'soft7')}
LogicalKeyboardKey.soft8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.soft8._nx_ = {'#t': ('LogicalKeyboardKey', 'soft8')}
LogicalKeyboardKey.close = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.close._nx_ = {'#t': ('LogicalKeyboardKey', 'close')}
LogicalKeyboardKey.mail_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.mail_forward._nx_ = {'#t': ('LogicalKeyboardKey', 'mailForward')}
LogicalKeyboardKey.mail_reply = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.mail_reply._nx_ = {'#t': ('LogicalKeyboardKey', 'mailReply')}
LogicalKeyboardKey.mail_send = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.mail_send._nx_ = {'#t': ('LogicalKeyboardKey', 'mailSend')}
LogicalKeyboardKey.media_play_pause = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_play_pause._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaPlayPause')}
LogicalKeyboardKey.media_stop = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_stop._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaStop')}
LogicalKeyboardKey.media_track_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_track_next._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaTrackNext')}
LogicalKeyboardKey.media_track_previous = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_track_previous._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaTrackPrevious')}
LogicalKeyboardKey.new_key = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.new_key._nx_ = {'#t': ('LogicalKeyboardKey', 'newKey')}
LogicalKeyboardKey.open = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.open._nx_ = {'#t': ('LogicalKeyboardKey', 'open')}
LogicalKeyboardKey.print = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.print._nx_ = {'#t': ('LogicalKeyboardKey', 'print')}
LogicalKeyboardKey.save = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.save._nx_ = {'#t': ('LogicalKeyboardKey', 'save')}
LogicalKeyboardKey.spell_check = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.spell_check._nx_ = {'#t': ('LogicalKeyboardKey', 'spellCheck')}
LogicalKeyboardKey.audio_volume_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_volume_down._nx_ = {'#t': ('LogicalKeyboardKey', 'audioVolumeDown')}
LogicalKeyboardKey.audio_volume_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_volume_up._nx_ = {'#t': ('LogicalKeyboardKey', 'audioVolumeUp')}
LogicalKeyboardKey.audio_volume_mute = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_volume_mute._nx_ = {'#t': ('LogicalKeyboardKey', 'audioVolumeMute')}
LogicalKeyboardKey.launch_application2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_application2._nx_ = {'#t': ('LogicalKeyboardKey', 'launchApplication2')}
LogicalKeyboardKey.launch_calendar = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_calendar._nx_ = {'#t': ('LogicalKeyboardKey', 'launchCalendar')}
LogicalKeyboardKey.launch_mail = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_mail._nx_ = {'#t': ('LogicalKeyboardKey', 'launchMail')}
LogicalKeyboardKey.launch_media_player = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_media_player._nx_ = {'#t': ('LogicalKeyboardKey', 'launchMediaPlayer')}
LogicalKeyboardKey.launch_music_player = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_music_player._nx_ = {'#t': ('LogicalKeyboardKey', 'launchMusicPlayer')}
LogicalKeyboardKey.launch_application1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_application1._nx_ = {'#t': ('LogicalKeyboardKey', 'launchApplication1')}
LogicalKeyboardKey.launch_screen_saver = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_screen_saver._nx_ = {'#t': ('LogicalKeyboardKey', 'launchScreenSaver')}
LogicalKeyboardKey.launch_spreadsheet = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_spreadsheet._nx_ = {'#t': ('LogicalKeyboardKey', 'launchSpreadsheet')}
LogicalKeyboardKey.launch_web_browser = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_web_browser._nx_ = {'#t': ('LogicalKeyboardKey', 'launchWebBrowser')}
LogicalKeyboardKey.launch_web_cam = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_web_cam._nx_ = {'#t': ('LogicalKeyboardKey', 'launchWebCam')}
LogicalKeyboardKey.launch_word_processor = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_word_processor._nx_ = {'#t': ('LogicalKeyboardKey', 'launchWordProcessor')}
LogicalKeyboardKey.launch_contacts = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_contacts._nx_ = {'#t': ('LogicalKeyboardKey', 'launchContacts')}
LogicalKeyboardKey.launch_phone = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_phone._nx_ = {'#t': ('LogicalKeyboardKey', 'launchPhone')}
LogicalKeyboardKey.launch_assistant = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_assistant._nx_ = {'#t': ('LogicalKeyboardKey', 'launchAssistant')}
LogicalKeyboardKey.launch_control_panel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.launch_control_panel._nx_ = {'#t': ('LogicalKeyboardKey', 'launchControlPanel')}
LogicalKeyboardKey.browser_back = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_back._nx_ = {'#t': ('LogicalKeyboardKey', 'browserBack')}
LogicalKeyboardKey.browser_favorites = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_favorites._nx_ = {'#t': ('LogicalKeyboardKey', 'browserFavorites')}
LogicalKeyboardKey.browser_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_forward._nx_ = {'#t': ('LogicalKeyboardKey', 'browserForward')}
LogicalKeyboardKey.browser_home = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_home._nx_ = {'#t': ('LogicalKeyboardKey', 'browserHome')}
LogicalKeyboardKey.browser_refresh = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_refresh._nx_ = {'#t': ('LogicalKeyboardKey', 'browserRefresh')}
LogicalKeyboardKey.browser_search = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_search._nx_ = {'#t': ('LogicalKeyboardKey', 'browserSearch')}
LogicalKeyboardKey.browser_stop = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.browser_stop._nx_ = {'#t': ('LogicalKeyboardKey', 'browserStop')}
LogicalKeyboardKey.audio_balance_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_balance_left._nx_ = {'#t': ('LogicalKeyboardKey', 'audioBalanceLeft')}
LogicalKeyboardKey.audio_balance_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_balance_right._nx_ = {'#t': ('LogicalKeyboardKey', 'audioBalanceRight')}
LogicalKeyboardKey.audio_bass_boost_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_bass_boost_down._nx_ = {'#t': ('LogicalKeyboardKey', 'audioBassBoostDown')}
LogicalKeyboardKey.audio_bass_boost_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_bass_boost_up._nx_ = {'#t': ('LogicalKeyboardKey', 'audioBassBoostUp')}
LogicalKeyboardKey.audio_fader_front = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_fader_front._nx_ = {'#t': ('LogicalKeyboardKey', 'audioFaderFront')}
LogicalKeyboardKey.audio_fader_rear = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_fader_rear._nx_ = {'#t': ('LogicalKeyboardKey', 'audioFaderRear')}
LogicalKeyboardKey.audio_surround_mode_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_surround_mode_next._nx_ = {'#t': ('LogicalKeyboardKey', 'audioSurroundModeNext')}
LogicalKeyboardKey.avr_input = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.avr_input._nx_ = {'#t': ('LogicalKeyboardKey', 'avrInput')}
LogicalKeyboardKey.avr_power = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.avr_power._nx_ = {'#t': ('LogicalKeyboardKey', 'avrPower')}
LogicalKeyboardKey.channel_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.channel_down._nx_ = {'#t': ('LogicalKeyboardKey', 'channelDown')}
LogicalKeyboardKey.channel_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.channel_up._nx_ = {'#t': ('LogicalKeyboardKey', 'channelUp')}
LogicalKeyboardKey.color_f0_red = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f0_red._nx_ = {'#t': ('LogicalKeyboardKey', 'colorF0Red')}
LogicalKeyboardKey.color_f1_green = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f1_green._nx_ = {'#t': ('LogicalKeyboardKey', 'colorF1Green')}
LogicalKeyboardKey.color_f2_yellow = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f2_yellow._nx_ = {'#t': ('LogicalKeyboardKey', 'colorF2Yellow')}
LogicalKeyboardKey.color_f3_blue = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f3_blue._nx_ = {'#t': ('LogicalKeyboardKey', 'colorF3Blue')}
LogicalKeyboardKey.color_f4_grey = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f4_grey._nx_ = {'#t': ('LogicalKeyboardKey', 'colorF4Grey')}
LogicalKeyboardKey.color_f5_brown = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.color_f5_brown._nx_ = {'#t': ('LogicalKeyboardKey', 'colorF5Brown')}
LogicalKeyboardKey.closed_caption_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.closed_caption_toggle._nx_ = {'#t': ('LogicalKeyboardKey', 'closedCaptionToggle')}
LogicalKeyboardKey.dimmer = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.dimmer._nx_ = {'#t': ('LogicalKeyboardKey', 'dimmer')}
LogicalKeyboardKey.display_swap = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.display_swap._nx_ = {'#t': ('LogicalKeyboardKey', 'displaySwap')}
LogicalKeyboardKey.exit = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.exit._nx_ = {'#t': ('LogicalKeyboardKey', 'exit')}
LogicalKeyboardKey.favorite_clear0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_clear0._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteClear0')}
LogicalKeyboardKey.favorite_clear1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_clear1._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteClear1')}
LogicalKeyboardKey.favorite_clear2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_clear2._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteClear2')}
LogicalKeyboardKey.favorite_clear3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_clear3._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteClear3')}
LogicalKeyboardKey.favorite_recall0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_recall0._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteRecall0')}
LogicalKeyboardKey.favorite_recall1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_recall1._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteRecall1')}
LogicalKeyboardKey.favorite_recall2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_recall2._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteRecall2')}
LogicalKeyboardKey.favorite_recall3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_recall3._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteRecall3')}
LogicalKeyboardKey.favorite_store0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_store0._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteStore0')}
LogicalKeyboardKey.favorite_store1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_store1._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteStore1')}
LogicalKeyboardKey.favorite_store2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_store2._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteStore2')}
LogicalKeyboardKey.favorite_store3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.favorite_store3._nx_ = {'#t': ('LogicalKeyboardKey', 'favoriteStore3')}
LogicalKeyboardKey.guide = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.guide._nx_ = {'#t': ('LogicalKeyboardKey', 'guide')}
LogicalKeyboardKey.guide_next_day = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.guide_next_day._nx_ = {'#t': ('LogicalKeyboardKey', 'guideNextDay')}
LogicalKeyboardKey.guide_previous_day = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.guide_previous_day._nx_ = {'#t': ('LogicalKeyboardKey', 'guidePreviousDay')}
LogicalKeyboardKey.info = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.info._nx_ = {'#t': ('LogicalKeyboardKey', 'info')}
LogicalKeyboardKey.instant_replay = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.instant_replay._nx_ = {'#t': ('LogicalKeyboardKey', 'instantReplay')}
LogicalKeyboardKey.link = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.link._nx_ = {'#t': ('LogicalKeyboardKey', 'link')}
LogicalKeyboardKey.list_program = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.list_program._nx_ = {'#t': ('LogicalKeyboardKey', 'listProgram')}
LogicalKeyboardKey.live_content = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.live_content._nx_ = {'#t': ('LogicalKeyboardKey', 'liveContent')}
LogicalKeyboardKey.lock = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lock._nx_ = {'#t': ('LogicalKeyboardKey', 'lock')}
LogicalKeyboardKey.media_apps = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_apps._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaApps')}
LogicalKeyboardKey.media_fast_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_fast_forward._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaFastForward')}
LogicalKeyboardKey.media_last = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_last._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaLast')}
LogicalKeyboardKey.media_pause = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_pause._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaPause')}
LogicalKeyboardKey.media_play = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_play._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaPlay')}
LogicalKeyboardKey.media_record = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_record._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaRecord')}
LogicalKeyboardKey.media_rewind = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_rewind._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaRewind')}
LogicalKeyboardKey.media_skip = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_skip._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaSkip')}
LogicalKeyboardKey.next_favorite_channel = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.next_favorite_channel._nx_ = {'#t': ('LogicalKeyboardKey', 'nextFavoriteChannel')}
LogicalKeyboardKey.next_user_profile = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.next_user_profile._nx_ = {'#t': ('LogicalKeyboardKey', 'nextUserProfile')}
LogicalKeyboardKey.on_demand = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.on_demand._nx_ = {'#t': ('LogicalKeyboardKey', 'onDemand')}
LogicalKeyboardKey.p_in_pdown = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.p_in_pdown._nx_ = {'#t': ('LogicalKeyboardKey', 'pInPDown')}
LogicalKeyboardKey.p_in_pmove = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.p_in_pmove._nx_ = {'#t': ('LogicalKeyboardKey', 'pInPMove')}
LogicalKeyboardKey.p_in_ptoggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.p_in_ptoggle._nx_ = {'#t': ('LogicalKeyboardKey', 'pInPToggle')}
LogicalKeyboardKey.p_in_pup = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.p_in_pup._nx_ = {'#t': ('LogicalKeyboardKey', 'pInPUp')}
LogicalKeyboardKey.play_speed_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.play_speed_down._nx_ = {'#t': ('LogicalKeyboardKey', 'playSpeedDown')}
LogicalKeyboardKey.play_speed_reset = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.play_speed_reset._nx_ = {'#t': ('LogicalKeyboardKey', 'playSpeedReset')}
LogicalKeyboardKey.play_speed_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.play_speed_up._nx_ = {'#t': ('LogicalKeyboardKey', 'playSpeedUp')}
LogicalKeyboardKey.random_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.random_toggle._nx_ = {'#t': ('LogicalKeyboardKey', 'randomToggle')}
LogicalKeyboardKey.rc_low_battery = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.rc_low_battery._nx_ = {'#t': ('LogicalKeyboardKey', 'rcLowBattery')}
LogicalKeyboardKey.record_speed_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.record_speed_next._nx_ = {'#t': ('LogicalKeyboardKey', 'recordSpeedNext')}
LogicalKeyboardKey.rf_bypass = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.rf_bypass._nx_ = {'#t': ('LogicalKeyboardKey', 'rfBypass')}
LogicalKeyboardKey.scan_channels_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.scan_channels_toggle._nx_ = {'#t': ('LogicalKeyboardKey', 'scanChannelsToggle')}
LogicalKeyboardKey.screen_mode_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.screen_mode_next._nx_ = {'#t': ('LogicalKeyboardKey', 'screenModeNext')}
LogicalKeyboardKey.settings = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.settings._nx_ = {'#t': ('LogicalKeyboardKey', 'settings')}
LogicalKeyboardKey.split_screen_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.split_screen_toggle._nx_ = {'#t': ('LogicalKeyboardKey', 'splitScreenToggle')}
LogicalKeyboardKey.stb_input = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.stb_input._nx_ = {'#t': ('LogicalKeyboardKey', 'stbInput')}
LogicalKeyboardKey.stb_power = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.stb_power._nx_ = {'#t': ('LogicalKeyboardKey', 'stbPower')}
LogicalKeyboardKey.subtitle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.subtitle._nx_ = {'#t': ('LogicalKeyboardKey', 'subtitle')}
LogicalKeyboardKey.teletext = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.teletext._nx_ = {'#t': ('LogicalKeyboardKey', 'teletext')}
LogicalKeyboardKey.tv = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv._nx_ = {'#t': ('LogicalKeyboardKey', 'tv')}
LogicalKeyboardKey.tv_input = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInput')}
LogicalKeyboardKey.tv_power = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_power._nx_ = {'#t': ('LogicalKeyboardKey', 'tvPower')}
LogicalKeyboardKey.video_mode_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.video_mode_next._nx_ = {'#t': ('LogicalKeyboardKey', 'videoModeNext')}
LogicalKeyboardKey.wink = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.wink._nx_ = {'#t': ('LogicalKeyboardKey', 'wink')}
LogicalKeyboardKey.zoom_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.zoom_toggle._nx_ = {'#t': ('LogicalKeyboardKey', 'zoomToggle')}
LogicalKeyboardKey.dvr = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.dvr._nx_ = {'#t': ('LogicalKeyboardKey', 'dvr')}
LogicalKeyboardKey.media_audio_track = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_audio_track._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaAudioTrack')}
LogicalKeyboardKey.media_skip_backward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_skip_backward._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaSkipBackward')}
LogicalKeyboardKey.media_skip_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_skip_forward._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaSkipForward')}
LogicalKeyboardKey.media_step_backward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_step_backward._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaStepBackward')}
LogicalKeyboardKey.media_step_forward = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_step_forward._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaStepForward')}
LogicalKeyboardKey.media_top_menu = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_top_menu._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaTopMenu')}
LogicalKeyboardKey.navigate_in = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.navigate_in._nx_ = {'#t': ('LogicalKeyboardKey', 'navigateIn')}
LogicalKeyboardKey.navigate_next = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.navigate_next._nx_ = {'#t': ('LogicalKeyboardKey', 'navigateNext')}
LogicalKeyboardKey.navigate_out = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.navigate_out._nx_ = {'#t': ('LogicalKeyboardKey', 'navigateOut')}
LogicalKeyboardKey.navigate_previous = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.navigate_previous._nx_ = {'#t': ('LogicalKeyboardKey', 'navigatePrevious')}
LogicalKeyboardKey.pairing = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.pairing._nx_ = {'#t': ('LogicalKeyboardKey', 'pairing')}
LogicalKeyboardKey.media_close = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.media_close._nx_ = {'#t': ('LogicalKeyboardKey', 'mediaClose')}
LogicalKeyboardKey.audio_bass_boost_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_bass_boost_toggle._nx_ = {'#t': ('LogicalKeyboardKey', 'audioBassBoostToggle')}
LogicalKeyboardKey.audio_treble_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_treble_down._nx_ = {'#t': ('LogicalKeyboardKey', 'audioTrebleDown')}
LogicalKeyboardKey.audio_treble_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.audio_treble_up._nx_ = {'#t': ('LogicalKeyboardKey', 'audioTrebleUp')}
LogicalKeyboardKey.microphone_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.microphone_toggle._nx_ = {'#t': ('LogicalKeyboardKey', 'microphoneToggle')}
LogicalKeyboardKey.microphone_volume_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.microphone_volume_down._nx_ = {'#t': ('LogicalKeyboardKey', 'microphoneVolumeDown')}
LogicalKeyboardKey.microphone_volume_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.microphone_volume_up._nx_ = {'#t': ('LogicalKeyboardKey', 'microphoneVolumeUp')}
LogicalKeyboardKey.microphone_volume_mute = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.microphone_volume_mute._nx_ = {'#t': ('LogicalKeyboardKey', 'microphoneVolumeMute')}
LogicalKeyboardKey.speech_correction_list = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.speech_correction_list._nx_ = {'#t': ('LogicalKeyboardKey', 'speechCorrectionList')}
LogicalKeyboardKey.speech_input_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.speech_input_toggle._nx_ = {'#t': ('LogicalKeyboardKey', 'speechInputToggle')}
LogicalKeyboardKey.app_switch = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.app_switch._nx_ = {'#t': ('LogicalKeyboardKey', 'appSwitch')}
LogicalKeyboardKey.call = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.call._nx_ = {'#t': ('LogicalKeyboardKey', 'call')}
LogicalKeyboardKey.camera_focus = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.camera_focus._nx_ = {'#t': ('LogicalKeyboardKey', 'cameraFocus')}
LogicalKeyboardKey.end_call = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.end_call._nx_ = {'#t': ('LogicalKeyboardKey', 'endCall')}
LogicalKeyboardKey.go_back = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.go_back._nx_ = {'#t': ('LogicalKeyboardKey', 'goBack')}
LogicalKeyboardKey.go_home = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.go_home._nx_ = {'#t': ('LogicalKeyboardKey', 'goHome')}
LogicalKeyboardKey.headset_hook = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.headset_hook._nx_ = {'#t': ('LogicalKeyboardKey', 'headsetHook')}
LogicalKeyboardKey.last_number_redial = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.last_number_redial._nx_ = {'#t': ('LogicalKeyboardKey', 'lastNumberRedial')}
LogicalKeyboardKey.notification = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.notification._nx_ = {'#t': ('LogicalKeyboardKey', 'notification')}
LogicalKeyboardKey.manner_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.manner_mode._nx_ = {'#t': ('LogicalKeyboardKey', 'mannerMode')}
LogicalKeyboardKey.voice_dial = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.voice_dial._nx_ = {'#t': ('LogicalKeyboardKey', 'voiceDial')}
LogicalKeyboardKey.tv3_dmode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv3_dmode._nx_ = {'#t': ('LogicalKeyboardKey', 'tv3DMode')}
LogicalKeyboardKey.tv_antenna_cable = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_antenna_cable._nx_ = {'#t': ('LogicalKeyboardKey', 'tvAntennaCable')}
LogicalKeyboardKey.tv_audio_description = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_audio_description._nx_ = {'#t': ('LogicalKeyboardKey', 'tvAudioDescription')}
LogicalKeyboardKey.tv_audio_description_mix_down = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_audio_description_mix_down._nx_ = {'#t': ('LogicalKeyboardKey', 'tvAudioDescriptionMixDown')}
LogicalKeyboardKey.tv_audio_description_mix_up = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_audio_description_mix_up._nx_ = {'#t': ('LogicalKeyboardKey', 'tvAudioDescriptionMixUp')}
LogicalKeyboardKey.tv_contents_menu = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_contents_menu._nx_ = {'#t': ('LogicalKeyboardKey', 'tvContentsMenu')}
LogicalKeyboardKey.tv_data_service = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_data_service._nx_ = {'#t': ('LogicalKeyboardKey', 'tvDataService')}
LogicalKeyboardKey.tv_input_component1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_component1._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInputComponent1')}
LogicalKeyboardKey.tv_input_component2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_component2._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInputComponent2')}
LogicalKeyboardKey.tv_input_composite1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_composite1._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInputComposite1')}
LogicalKeyboardKey.tv_input_composite2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_composite2._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInputComposite2')}
LogicalKeyboardKey.tv_input_hdmi1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_hdmi1._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInputHDMI1')}
LogicalKeyboardKey.tv_input_hdmi2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_hdmi2._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInputHDMI2')}
LogicalKeyboardKey.tv_input_hdmi3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_hdmi3._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInputHDMI3')}
LogicalKeyboardKey.tv_input_hdmi4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_hdmi4._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInputHDMI4')}
LogicalKeyboardKey.tv_input_vga1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_input_vga1._nx_ = {'#t': ('LogicalKeyboardKey', 'tvInputVGA1')}
LogicalKeyboardKey.tv_media_context = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_media_context._nx_ = {'#t': ('LogicalKeyboardKey', 'tvMediaContext')}
LogicalKeyboardKey.tv_network = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_network._nx_ = {'#t': ('LogicalKeyboardKey', 'tvNetwork')}
LogicalKeyboardKey.tv_number_entry = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_number_entry._nx_ = {'#t': ('LogicalKeyboardKey', 'tvNumberEntry')}
LogicalKeyboardKey.tv_radio_service = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_radio_service._nx_ = {'#t': ('LogicalKeyboardKey', 'tvRadioService')}
LogicalKeyboardKey.tv_satellite = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_satellite._nx_ = {'#t': ('LogicalKeyboardKey', 'tvSatellite')}
LogicalKeyboardKey.tv_satellite_bs = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_satellite_bs._nx_ = {'#t': ('LogicalKeyboardKey', 'tvSatelliteBS')}
LogicalKeyboardKey.tv_satellite_cs = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_satellite_cs._nx_ = {'#t': ('LogicalKeyboardKey', 'tvSatelliteCS')}
LogicalKeyboardKey.tv_satellite_toggle = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_satellite_toggle._nx_ = {'#t': ('LogicalKeyboardKey', 'tvSatelliteToggle')}
LogicalKeyboardKey.tv_terrestrial_analog = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_terrestrial_analog._nx_ = {'#t': ('LogicalKeyboardKey', 'tvTerrestrialAnalog')}
LogicalKeyboardKey.tv_terrestrial_digital = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_terrestrial_digital._nx_ = {'#t': ('LogicalKeyboardKey', 'tvTerrestrialDigital')}
LogicalKeyboardKey.tv_timer = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.tv_timer._nx_ = {'#t': ('LogicalKeyboardKey', 'tvTimer')}
LogicalKeyboardKey.key11 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key11._nx_ = {'#t': ('LogicalKeyboardKey', 'key11')}
LogicalKeyboardKey.key12 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.key12._nx_ = {'#t': ('LogicalKeyboardKey', 'key12')}
LogicalKeyboardKey.suspend = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.suspend._nx_ = {'#t': ('LogicalKeyboardKey', 'suspend')}
LogicalKeyboardKey.resume = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.resume._nx_ = {'#t': ('LogicalKeyboardKey', 'resume')}
LogicalKeyboardKey.sleep = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.sleep._nx_ = {'#t': ('LogicalKeyboardKey', 'sleep')}
LogicalKeyboardKey.abort = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.abort._nx_ = {'#t': ('LogicalKeyboardKey', 'abort')}
LogicalKeyboardKey.lang1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang1._nx_ = {'#t': ('LogicalKeyboardKey', 'lang1')}
LogicalKeyboardKey.lang2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang2._nx_ = {'#t': ('LogicalKeyboardKey', 'lang2')}
LogicalKeyboardKey.lang3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang3._nx_ = {'#t': ('LogicalKeyboardKey', 'lang3')}
LogicalKeyboardKey.lang4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang4._nx_ = {'#t': ('LogicalKeyboardKey', 'lang4')}
LogicalKeyboardKey.lang5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.lang5._nx_ = {'#t': ('LogicalKeyboardKey', 'lang5')}
LogicalKeyboardKey.intl_backslash = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.intl_backslash._nx_ = {'#t': ('LogicalKeyboardKey', 'intlBackslash')}
LogicalKeyboardKey.intl_ro = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.intl_ro._nx_ = {'#t': ('LogicalKeyboardKey', 'intlRo')}
LogicalKeyboardKey.intl_yen = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.intl_yen._nx_ = {'#t': ('LogicalKeyboardKey', 'intlYen')}
LogicalKeyboardKey.control_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.control_left._nx_ = {'#t': ('LogicalKeyboardKey', 'controlLeft')}
LogicalKeyboardKey.control_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.control_right._nx_ = {'#t': ('LogicalKeyboardKey', 'controlRight')}
LogicalKeyboardKey.shift_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.shift_left._nx_ = {'#t': ('LogicalKeyboardKey', 'shiftLeft')}
LogicalKeyboardKey.shift_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.shift_right._nx_ = {'#t': ('LogicalKeyboardKey', 'shiftRight')}
LogicalKeyboardKey.alt_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alt_left._nx_ = {'#t': ('LogicalKeyboardKey', 'altLeft')}
LogicalKeyboardKey.alt_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alt_right._nx_ = {'#t': ('LogicalKeyboardKey', 'altRight')}
LogicalKeyboardKey.meta_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.meta_left._nx_ = {'#t': ('LogicalKeyboardKey', 'metaLeft')}
LogicalKeyboardKey.meta_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.meta_right._nx_ = {'#t': ('LogicalKeyboardKey', 'metaRight')}
LogicalKeyboardKey.control = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.control._nx_ = {'#t': ('LogicalKeyboardKey', 'control')}
LogicalKeyboardKey.shift = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.shift._nx_ = {'#t': ('LogicalKeyboardKey', 'shift')}
LogicalKeyboardKey.alt = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.alt._nx_ = {'#t': ('LogicalKeyboardKey', 'alt')}
LogicalKeyboardKey.meta = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.meta._nx_ = {'#t': ('LogicalKeyboardKey', 'meta')}
LogicalKeyboardKey.numpad_enter = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_enter._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadEnter')}
LogicalKeyboardKey.numpad_paren_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_paren_left._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadParenLeft')}
LogicalKeyboardKey.numpad_paren_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_paren_right._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadParenRight')}
LogicalKeyboardKey.numpad_multiply = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_multiply._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadMultiply')}
LogicalKeyboardKey.numpad_add = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_add._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadAdd')}
LogicalKeyboardKey.numpad_comma = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_comma._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadComma')}
LogicalKeyboardKey.numpad_subtract = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_subtract._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadSubtract')}
LogicalKeyboardKey.numpad_decimal = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_decimal._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadDecimal')}
LogicalKeyboardKey.numpad_divide = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_divide._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadDivide')}
LogicalKeyboardKey.numpad0 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad0._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad0')}
LogicalKeyboardKey.numpad1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad1._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad1')}
LogicalKeyboardKey.numpad2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad2._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad2')}
LogicalKeyboardKey.numpad3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad3._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad3')}
LogicalKeyboardKey.numpad4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad4._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad4')}
LogicalKeyboardKey.numpad5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad5._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad5')}
LogicalKeyboardKey.numpad6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad6._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad6')}
LogicalKeyboardKey.numpad7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad7._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad7')}
LogicalKeyboardKey.numpad8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad8._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad8')}
LogicalKeyboardKey.numpad9 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad9._nx_ = {'#t': ('LogicalKeyboardKey', 'numpad9')}
LogicalKeyboardKey.numpad_equal = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.numpad_equal._nx_ = {'#t': ('LogicalKeyboardKey', 'numpadEqual')}
LogicalKeyboardKey.game_button1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button1._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton1')}
LogicalKeyboardKey.game_button2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button2._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton2')}
LogicalKeyboardKey.game_button3 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button3._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton3')}
LogicalKeyboardKey.game_button4 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button4._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton4')}
LogicalKeyboardKey.game_button5 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button5._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton5')}
LogicalKeyboardKey.game_button6 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button6._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton6')}
LogicalKeyboardKey.game_button7 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button7._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton7')}
LogicalKeyboardKey.game_button8 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button8._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton8')}
LogicalKeyboardKey.game_button9 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button9._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton9')}
LogicalKeyboardKey.game_button10 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button10._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton10')}
LogicalKeyboardKey.game_button11 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button11._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton11')}
LogicalKeyboardKey.game_button12 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button12._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton12')}
LogicalKeyboardKey.game_button13 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button13._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton13')}
LogicalKeyboardKey.game_button14 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button14._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton14')}
LogicalKeyboardKey.game_button15 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button15._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton15')}
LogicalKeyboardKey.game_button16 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button16._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButton16')}
LogicalKeyboardKey.game_button_a = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_a._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonA')}
LogicalKeyboardKey.game_button_b = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_b._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonB')}
LogicalKeyboardKey.game_button_c = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_c._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonC')}
LogicalKeyboardKey.game_button_left1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_left1._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonLeft1')}
LogicalKeyboardKey.game_button_left2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_left2._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonLeft2')}
LogicalKeyboardKey.game_button_mode = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_mode._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonMode')}
LogicalKeyboardKey.game_button_right1 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_right1._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonRight1')}
LogicalKeyboardKey.game_button_right2 = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_right2._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonRight2')}
LogicalKeyboardKey.game_button_select = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_select._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonSelect')}
LogicalKeyboardKey.game_button_start = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_start._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonStart')}
LogicalKeyboardKey.game_button_thumb_left = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_thumb_left._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonThumbLeft')}
LogicalKeyboardKey.game_button_thumb_right = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_thumb_right._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonThumbRight')}
LogicalKeyboardKey.game_button_x = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_x._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonX')}
LogicalKeyboardKey.game_button_y = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_y._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonY')}
LogicalKeyboardKey.game_button_z = LogicalKeyboardKey(
    key_id=0,
)
LogicalKeyboardKey.game_button_z._nx_ = {'#t': ('LogicalKeyboardKey', 'gameButtonZ')}


# packages/flutter/lib/src/services/hardware_keyboard.dart
class KeyEvent(Object, ABC):

    def __init__(
        self,
        physical_key: PhysicalKeyboardKey,
        logical_key: LogicalKeyboardKey,
        time_stamp: Duration,
        character: Optional[str] = None,
        synthesized: Optional[bool] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('KeyEvent', ''),
            'physicalKey': physical_key,
            'logicalKey': logical_key,
            'timeStamp': time_stamp,
            'character': character,
            'synthesized': synthesized,
        }


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
        super().__init__(
        )
        self._nx_ = {
            '#t': ('FocusNode', ''),
            'debugLabel': debug_label,
            'onKey': on_key,
            'onKeyEvent': on_key_event,
            'skipTraversal': skip_traversal,
            'canRequestFocus': can_request_focus,
            'descendantsAreFocusable': descendants_are_focusable,
        }


# packages/flutter/lib/src/material/button_style_button.dart
class ButtonStyleButton(StatefulWidget, ABC):

    def __init__(
        self,
        autofocus: bool,
        clip_behavior: Clip,
        key: Optional[Key] = None,
        on_pressed: Optional[Callable[[], None]] = None,
        on_long_press: Optional[Callable[[], None]] = None,
        style: Optional[ButtonStyle] = None,
        focus_node: Optional[FocusNode] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(
        )
        self._nx_ = {
            '#t': ('ButtonStyleButton', ''),
            'autofocus': autofocus,
            'clipBehavior': clip_behavior,
            'key': key,
            'onPressed': on_pressed,
            'onLongPress': on_long_press,
            'style': style,
            'focusNode': focus_node,
            'child': child,
        }


# packages/flutter/lib/src/material/elevated_button.dart
class ElevatedButton(ButtonStyleButton):

    def __init__(
        self,
        key: Optional[Key] = None,
        on_pressed: Optional[Callable[[], None]] = None,
        on_long_press: Optional[Callable[[], None]] = None,
        style: Optional[ButtonStyle] = None,
        focus_node: Optional[FocusNode] = None,
        autofocus: Optional[bool] = None,
        clip_behavior: Optional[Clip] = None,
        child: Optional[Widget] = None,
    ):
        super().__init__(
            autofocus=False,
            clip_behavior=Clip.none,
        )
        self._nx_ = {
            '#t': ('ElevatedButton', ''),
            'key': key,
            'onPressed': on_pressed,
            'onLongPress': on_long_press,
            'style': style,
            'focusNode': focus_node,
            'autofocus': autofocus,
            'clipBehavior': clip_behavior,
            'child': child,
        }

    @staticmethod
    def icon(
        icon: Widget,
        label: Widget,
        key: Optional[Key] = None,
        on_pressed: Optional[Callable[[], None]] = None,
        on_long_press: Optional[Callable[[], None]] = None,
        style: Optional[ButtonStyle] = None,
        focus_node: Optional[FocusNode] = None,
        autofocus: Optional[bool] = None,
        clip_behavior: Optional[Clip] = None,
    ):
        _o = ElevatedButton(
        )
        _o._nx_ = {
            '#t': ('ElevatedButton', 'icon'),
            'icon': icon,
            'label': label,
            'key': key,
            'onPressed': on_pressed,
            'onLongPress': on_long_press,
            'style': style,
            'focusNode': focus_node,
            'autofocus': autofocus,
            'clipBehavior': clip_behavior,
        }
        return _o
