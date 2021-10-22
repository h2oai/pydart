from enum import Enum
from typing import Callable, Optional, Iterable, List, Dict


# bin/cache/pkg/sky_engine/lib/ui/window.dart
class Brightness(Enum):
    INDEX = 'index'
    VALUES = 'values'
    DARK = 'dark'
    LIGHT = 'light'


# packages/flutter/lib/src/material/button_theme.dart
class ButtonTextTheme(Enum):
    INDEX = 'index'
    VALUES = 'values'
    NORMAL = 'normal'
    ACCENT = 'accent'
    PRIMARY = 'primary'


# packages/flutter/lib/src/material/button_theme.dart
class ButtonBarLayoutBehavior(Enum):
    INDEX = 'index'
    VALUES = 'values'
    CONSTRAINED = 'constrained'
    PADDED = 'padded'


# packages/flutter/lib/src/material/theme_data.dart
class MaterialTapTargetSize(Enum):
    INDEX = 'index'
    VALUES = 'values'
    PADDED = 'padded'
    SHRINK_WRAP = 'shrinkWrap'


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontStyle(Enum):
    INDEX = 'index'
    VALUES = 'values'
    NORMAL = 'normal'
    ITALIC = 'italic'


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextBaseline(Enum):
    INDEX = 'index'
    VALUES = 'values'
    ALPHABETIC = 'alphabetic'
    IDEOGRAPHIC = 'ideographic'


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextLeadingDistribution(Enum):
    INDEX = 'index'
    VALUES = 'values'
    PROPORTIONAL = 'proportional'
    EVEN = 'even'


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class TextDecorationStyle(Enum):
    INDEX = 'index'
    VALUES = 'values'
    SOLID = 'solid'
    DOUBLE = 'double'
    DOTTED = 'dotted'
    DASHED = 'dashed'
    WAVY = 'wavy'


# packages/flutter/lib/src/painting/text_painter.dart
class TextOverflow(Enum):
    INDEX = 'index'
    VALUES = 'values'
    CLIP = 'clip'
    FADE = 'fade'
    ELLIPSIS = 'ellipsis'
    VISIBLE = 'visible'


# packages/flutter/lib/src/material/input_decorator.dart
class FloatingLabelBehavior(Enum):
    INDEX = 'index'
    VALUES = 'values'
    NEVER = 'never'
    AUTO = 'auto'
    ALWAYS = 'always'


# packages/flutter/lib/src/painting/borders.dart
class BorderStyle(Enum):
    INDEX = 'index'
    VALUES = 'values'
    NONE = 'none'
    SOLID = 'solid'


# packages/flutter/lib/src/material/slider_theme.dart
class ShowValueIndicator(Enum):
    INDEX = 'index'
    VALUES = 'values'
    ONLY_FOR_DISCRETE = 'onlyForDiscrete'
    ONLY_FOR_CONTINUOUS = 'onlyForContinuous'
    ALWAYS = 'always'
    NEVER = 'never'


# packages/flutter/lib/src/material/tabs.dart
class TabBarIndicatorSize(Enum):
    INDEX = 'index'
    VALUES = 'values'
    TAB = 'tab'
    LABEL = 'label'


# packages/flutter/lib/src/material/tooltip_theme.dart
class TooltipTriggerMode(Enum):
    INDEX = 'index'
    VALUES = 'values'
    MANUAL = 'manual'
    LONG_PRESS = 'longPress'
    TAP = 'tap'


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Clip(Enum):
    INDEX = 'index'
    VALUES = 'values'
    NONE = 'none'
    HARD_EDGE = 'hardEdge'
    ANTI_ALIAS = 'antiAlias'
    ANTI_ALIAS_WITH_SAVE_LAYER = 'antiAliasWithSaveLayer'


# packages/flutter/lib/src/foundation/platform.dart
class TargetPlatform(Enum):
    INDEX = 'index'
    VALUES = 'values'
    ANDROID = 'android'
    FUCHSIA = 'fuchsia'
    I_OS = 'iOS'
    LINUX = 'linux'
    MAC_OS = 'macOS'
    WINDOWS = 'windows'


# packages/flutter/lib/src/material/navigation_rail.dart
class NavigationRailLabelType(Enum):
    INDEX = 'index'
    VALUES = 'values'
    NONE = 'none'
    SELECTED = 'selected'
    ALL = 'all'


# packages/flutter/lib/src/material/snack_bar_theme.dart
class SnackBarBehavior(Enum):
    INDEX = 'index'
    VALUES = 'values'
    FIXED = 'fixed'
    FLOATING = 'floating'


# packages/flutter/lib/src/rendering/flex.dart
class MainAxisAlignment(Enum):
    INDEX = 'index'
    VALUES = 'values'
    START = 'start'
    END = 'end'
    CENTER = 'center'
    SPACE_BETWEEN = 'spaceBetween'
    SPACE_AROUND = 'spaceAround'
    SPACE_EVENLY = 'spaceEvenly'


# packages/flutter/lib/src/rendering/flex.dart
class MainAxisSize(Enum):
    INDEX = 'index'
    VALUES = 'values'
    MIN = 'min'
    MAX = 'max'


# packages/flutter/lib/src/painting/basic_types.dart
class VerticalDirection(Enum):
    INDEX = 'index'
    VALUES = 'values'
    UP = 'up'
    DOWN = 'down'


# packages/flutter/lib/src/material/bottom_navigation_bar.dart
class BottomNavigationBarType(Enum):
    INDEX = 'index'
    VALUES = 'values'
    FIXED = 'fixed'
    SHIFTING = 'shifting'


# packages/flutter/lib/src/material/bottom_navigation_bar.dart
class BottomNavigationBarLandscapeLayout(Enum):
    INDEX = 'index'
    VALUES = 'values'
    SPREAD = 'spread'
    CENTERED = 'centered'
    LINEAR = 'linear'


# packages/flutter/lib/src/material/app.dart
class ThemeMode(Enum):
    INDEX = 'index'
    VALUES = 'values'
    SYSTEM = 'system'
    LIGHT = 'light'
    DARK = 'dark'


# packages/flutter/lib/src/foundation/key.dart
class KeyWithEmpty:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/foundation/key.dart
class Key:
    def __init__(
            self,
            value: str,
    ):
        self.value = value

    @staticmethod
    def with_empty(
    ) -> KeyWithEmpty:
        return KeyWithEmpty(
        )


# packages/flutter/lib/src/material/scaffold.dart
class ScaffoldMessengerState:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/widgets/router.dart
class RouteInformationProvider:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/core/object.dart
class Object:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/widgets/router.dart
class BackButtonDispatcher:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class ColorWithFromARGB:
    def __init__(
            self,
            a: int,
            r: int,
            g: int,
            b: int,
    ):
        self.a = a
        self.r = r
        self.g = g
        self.b = b


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class ColorWithFromRGBO:
    def __init__(
            self,
            r: int,
            g: int,
            b: int,
            opacity: float,
    ):
        self.r = r
        self.g = g
        self.b = b
        self.opacity = opacity


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Color:
    def __init__(
            self,
            value: int,
    ):
        self.value = value

    @staticmethod
    def with_fromARGB(
            a: int,
            r: int,
            g: int,
            b: int,
    ) -> ColorWithFromARGB:
        return ColorWithFromARGB(
            a,
            r,
            g,
            b,
        )

    @staticmethod
    def with_fromRGBO(
            r: int,
            g: int,
            b: int,
            opacity: float,
    ) -> ColorWithFromRGBO:
        return ColorWithFromRGBO(
            r,
            g,
            b,
            opacity,
        )


# packages/flutter/lib/src/material/theme_data.dart
class VisualDensity:
    def __init__(
            self,
            horizontal: Optional[float] = None,
            vertical: Optional[float] = None,
    ):
        self.horizontal = horizontal
        self.vertical = vertical


# packages/flutter/lib/src/material/ink_well.dart
class InteractiveInkFeatureFactory:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/painting/edge_insets.dart
class EdgeInsetsGeometry:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/painting/borders.dart
class ShapeBorder:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/colors.dart
class MaterialColor:
    def __init__(
            self,
            primary: int,
            swatch: Dict[int, Color],
    ):
        self.primary = primary
        self.swatch = swatch


# packages/flutter/lib/src/material/color_scheme.dart
class ColorSchemeWithLight:
    def __init__(
            self,
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
        self.primary = primary
        self.primary_variant = primary_variant
        self.secondary = secondary
        self.secondary_variant = secondary_variant
        self.surface = surface
        self.background = background
        self.error = error
        self.on_primary = on_primary
        self.on_secondary = on_secondary
        self.on_surface = on_surface
        self.on_background = on_background
        self.on_error = on_error
        self.brightness = brightness


# packages/flutter/lib/src/material/color_scheme.dart
class ColorSchemeWithDark:
    def __init__(
            self,
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
        self.primary = primary
        self.primary_variant = primary_variant
        self.secondary = secondary
        self.secondary_variant = secondary_variant
        self.surface = surface
        self.background = background
        self.error = error
        self.on_primary = on_primary
        self.on_secondary = on_secondary
        self.on_surface = on_surface
        self.on_background = on_background
        self.on_error = on_error
        self.brightness = brightness


# packages/flutter/lib/src/material/color_scheme.dart
class ColorSchemeWithHighContrastLight:
    def __init__(
            self,
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
        self.primary = primary
        self.primary_variant = primary_variant
        self.secondary = secondary
        self.secondary_variant = secondary_variant
        self.surface = surface
        self.background = background
        self.error = error
        self.on_primary = on_primary
        self.on_secondary = on_secondary
        self.on_surface = on_surface
        self.on_background = on_background
        self.on_error = on_error
        self.brightness = brightness


# packages/flutter/lib/src/material/color_scheme.dart
class ColorSchemeWithHighContrastDark:
    def __init__(
            self,
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
        self.primary = primary
        self.primary_variant = primary_variant
        self.secondary = secondary
        self.secondary_variant = secondary_variant
        self.surface = surface
        self.background = background
        self.error = error
        self.on_primary = on_primary
        self.on_secondary = on_secondary
        self.on_surface = on_surface
        self.on_background = on_background
        self.on_error = on_error
        self.brightness = brightness


# packages/flutter/lib/src/material/color_scheme.dart
class ColorSchemeWithFromSwatch:
    def __init__(
            self,
            primary_swatch: Optional[MaterialColor] = None,
            primary_color_dark: Optional[Color] = None,
            accent_color: Optional[Color] = None,
            card_color: Optional[Color] = None,
            background_color: Optional[Color] = None,
            error_color: Optional[Color] = None,
            brightness: Optional[Brightness] = None,
    ):
        self.primary_swatch = primary_swatch
        self.primary_color_dark = primary_color_dark
        self.accent_color = accent_color
        self.card_color = card_color
        self.background_color = background_color
        self.error_color = error_color
        self.brightness = brightness


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
        self.primary = primary
        self.primary_variant = primary_variant
        self.secondary = secondary
        self.secondary_variant = secondary_variant
        self.surface = surface
        self.background = background
        self.error = error
        self.on_primary = on_primary
        self.on_secondary = on_secondary
        self.on_surface = on_surface
        self.on_background = on_background
        self.on_error = on_error
        self.brightness = brightness

    @staticmethod
    def with_light(
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
    ) -> ColorSchemeWithLight:
        return ColorSchemeWithLight(
            primary,
            primary_variant,
            secondary,
            secondary_variant,
            surface,
            background,
            error,
            on_primary,
            on_secondary,
            on_surface,
            on_background,
            on_error,
            brightness,
        )

    @staticmethod
    def with_dark(
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
    ) -> ColorSchemeWithDark:
        return ColorSchemeWithDark(
            primary,
            primary_variant,
            secondary,
            secondary_variant,
            surface,
            background,
            error,
            on_primary,
            on_secondary,
            on_surface,
            on_background,
            on_error,
            brightness,
        )

    @staticmethod
    def with_highContrastLight(
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
    ) -> ColorSchemeWithHighContrastLight:
        return ColorSchemeWithHighContrastLight(
            primary,
            primary_variant,
            secondary,
            secondary_variant,
            surface,
            background,
            error,
            on_primary,
            on_secondary,
            on_surface,
            on_background,
            on_error,
            brightness,
        )

    @staticmethod
    def with_highContrastDark(
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
    ) -> ColorSchemeWithHighContrastDark:
        return ColorSchemeWithHighContrastDark(
            primary,
            primary_variant,
            secondary,
            secondary_variant,
            surface,
            background,
            error,
            on_primary,
            on_secondary,
            on_surface,
            on_background,
            on_error,
            brightness,
        )

    @staticmethod
    def with_fromSwatch(
            primary_swatch: Optional[MaterialColor] = None,
            primary_color_dark: Optional[Color] = None,
            accent_color: Optional[Color] = None,
            card_color: Optional[Color] = None,
            background_color: Optional[Color] = None,
            error_color: Optional[Color] = None,
            brightness: Optional[Brightness] = None,
    ) -> ColorSchemeWithFromSwatch:
        return ColorSchemeWithFromSwatch(
            primary_swatch,
            primary_color_dark,
            accent_color,
            card_color,
            background_color,
            error_color,
            brightness,
        )


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
        self.text_theme = text_theme
        self.min_width = min_width
        self.height = height
        self.padding = padding
        self.shape = shape
        self.layout_behavior = layout_behavior
        self.aligned_dropdown = aligned_dropdown
        self.button_color = button_color
        self.disabled_color = disabled_color
        self.focus_color = focus_color
        self.hover_color = hover_color
        self.highlight_color = highlight_color
        self.splash_color = splash_color
        self.color_scheme = color_scheme
        self.material_tap_target_size = material_tap_target_size


# bin/cache/pkg/sky_engine/lib/ui/platform_dispatcher.dart
class LocaleWithFromSubtags:
    def __init__(
            self,
            language_code: Optional[str] = None,
            script_code: Optional[str] = None,
            country_code: Optional[str] = None,
    ):
        self.language_code = language_code
        self.script_code = script_code
        self.country_code = country_code


# bin/cache/pkg/sky_engine/lib/ui/platform_dispatcher.dart
class Locale:
    def __init__(
            self,
            _language_code: str,
            _country_code: Optional[str] = None,
    ):
        self._language_code = _language_code
        self._country_code = _country_code

    @staticmethod
    def with_fromSubtags(
            language_code: Optional[str] = None,
            script_code: Optional[str] = None,
            country_code: Optional[str] = None,
    ) -> LocaleWithFromSubtags:
        return LocaleWithFromSubtags(
            language_code,
            script_code,
            country_code,
        )


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Paint:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class OffsetWithFromDirection:
    def __init__(
            self,
            direction: float,
            distance: Optional[float] = None,
    ):
        self.direction = direction
        self.distance = distance


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class Offset:
    def __init__(
            self,
            dx: float,
            dy: float,
    ):
        self.dx = dx
        self.dy = dy

    @staticmethod
    def with_fromDirection(
            direction: float,
            distance: Optional[float] = None,
    ) -> OffsetWithFromDirection:
        return OffsetWithFromDirection(
            direction,
            distance,
        )


# bin/cache/pkg/sky_engine/lib/ui/painting.dart
class Shadow:
    def __init__(
            self,
            color: Optional[Color] = None,
            offset: Optional[Offset] = None,
            blur_radius: Optional[float] = None,
    ):
        self.color = color
        self.offset = offset
        self.blur_radius = blur_radius


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithEnable:
    def __init__(
            self,
            feature: str,
    ):
        self.feature = feature


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithDisable:
    def __init__(
            self,
            feature: str,
    ):
        self.feature = feature


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithAlternative:
    def __init__(
            self,
            value: int,
    ):
        self.value = value


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithAlternativeFractions:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithContextualAlternates:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithCaseSensitiveForms:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithCharacterVariant:
    def __init__(
            self,
            value: int,
    ):
        self.value = value


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithDenominator:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithFractions:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithHistoricalForms:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithHistoricalLigatures:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithLiningFigures:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithLocaleAware:
    def __init__(
            self,
            enable: Optional[bool] = None,
    ):
        self.enable = enable


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithNotationalForms:
    def __init__(
            self,
            value: Optional[int] = None,
    ):
        self.value = value


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithNumerators:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithOldstyleFigures:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithOrdinalForms:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithProportionalFigures:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithRandomize:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithStylisticAlternates:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithScientificInferiors:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithStylisticSet:
    def __init__(
            self,
            value: int,
    ):
        self.value = value


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithSubscripts:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithSuperscripts:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithSwash:
    def __init__(
            self,
            value: Optional[int] = None,
    ):
        self.value = value


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithTabularFigures:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeatureWithSlashedZero:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/ui/text.dart
class FontFeature:
    def __init__(
            self,
            feature: str,
            value: Optional[int] = None,
    ):
        self.feature = feature
        self.value = value

    @staticmethod
    def with_enable(
            feature: str,
    ) -> FontFeatureWithEnable:
        return FontFeatureWithEnable(
            feature,
        )

    @staticmethod
    def with_disable(
            feature: str,
    ) -> FontFeatureWithDisable:
        return FontFeatureWithDisable(
            feature,
        )

    @staticmethod
    def with_alternative(
            value: int,
    ) -> FontFeatureWithAlternative:
        return FontFeatureWithAlternative(
            value,
        )

    @staticmethod
    def with_alternativeFractions(
    ) -> FontFeatureWithAlternativeFractions:
        return FontFeatureWithAlternativeFractions(
        )

    @staticmethod
    def with_contextualAlternates(
    ) -> FontFeatureWithContextualAlternates:
        return FontFeatureWithContextualAlternates(
        )

    @staticmethod
    def with_caseSensitiveForms(
    ) -> FontFeatureWithCaseSensitiveForms:
        return FontFeatureWithCaseSensitiveForms(
        )

    @staticmethod
    def with_characterVariant(
            value: int,
    ) -> FontFeatureWithCharacterVariant:
        return FontFeatureWithCharacterVariant(
            value,
        )

    @staticmethod
    def with_denominator(
    ) -> FontFeatureWithDenominator:
        return FontFeatureWithDenominator(
        )

    @staticmethod
    def with_fractions(
    ) -> FontFeatureWithFractions:
        return FontFeatureWithFractions(
        )

    @staticmethod
    def with_historicalForms(
    ) -> FontFeatureWithHistoricalForms:
        return FontFeatureWithHistoricalForms(
        )

    @staticmethod
    def with_historicalLigatures(
    ) -> FontFeatureWithHistoricalLigatures:
        return FontFeatureWithHistoricalLigatures(
        )

    @staticmethod
    def with_liningFigures(
    ) -> FontFeatureWithLiningFigures:
        return FontFeatureWithLiningFigures(
        )

    @staticmethod
    def with_localeAware(
            enable: Optional[bool] = None,
    ) -> FontFeatureWithLocaleAware:
        return FontFeatureWithLocaleAware(
            enable,
        )

    @staticmethod
    def with_notationalForms(
            value: Optional[int] = None,
    ) -> FontFeatureWithNotationalForms:
        return FontFeatureWithNotationalForms(
            value,
        )

    @staticmethod
    def with_numerators(
    ) -> FontFeatureWithNumerators:
        return FontFeatureWithNumerators(
        )

    @staticmethod
    def with_oldstyleFigures(
    ) -> FontFeatureWithOldstyleFigures:
        return FontFeatureWithOldstyleFigures(
        )

    @staticmethod
    def with_ordinalForms(
    ) -> FontFeatureWithOrdinalForms:
        return FontFeatureWithOrdinalForms(
        )

    @staticmethod
    def with_proportionalFigures(
    ) -> FontFeatureWithProportionalFigures:
        return FontFeatureWithProportionalFigures(
        )

    @staticmethod
    def with_randomize(
    ) -> FontFeatureWithRandomize:
        return FontFeatureWithRandomize(
        )

    @staticmethod
    def with_stylisticAlternates(
    ) -> FontFeatureWithStylisticAlternates:
        return FontFeatureWithStylisticAlternates(
        )

    @staticmethod
    def with_scientificInferiors(
    ) -> FontFeatureWithScientificInferiors:
        return FontFeatureWithScientificInferiors(
        )

    @staticmethod
    def with_stylisticSet(
            value: int,
    ) -> FontFeatureWithStylisticSet:
        return FontFeatureWithStylisticSet(
            value,
        )

    @staticmethod
    def with_subscripts(
    ) -> FontFeatureWithSubscripts:
        return FontFeatureWithSubscripts(
        )

    @staticmethod
    def with_superscripts(
    ) -> FontFeatureWithSuperscripts:
        return FontFeatureWithSuperscripts(
        )

    @staticmethod
    def with_swash(
            value: Optional[int] = None,
    ) -> FontFeatureWithSwash:
        return FontFeatureWithSwash(
            value,
        )

    @staticmethod
    def with_tabularFigures(
    ) -> FontFeatureWithTabularFigures:
        return FontFeatureWithTabularFigures(
        )

    @staticmethod
    def with_slashedZero(
    ) -> FontFeatureWithSlashedZero:
        return FontFeatureWithSlashedZero(
        )


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
        self.inherit = inherit
        self.color = color
        self.background_color = background_color
        self.font_size = font_size
        self.font_weight = font_weight
        self.font_style = font_style
        self.letter_spacing = letter_spacing
        self.word_spacing = word_spacing
        self.text_baseline = text_baseline
        self.height = height
        self.leading_distribution = leading_distribution
        self.locale = locale
        self.foreground = foreground
        self.background = background
        self.shadows = shadows
        self.font_features = font_features
        self.decoration = decoration
        self.decoration_color = decoration_color
        self.decoration_style = decoration_style
        self.decoration_thickness = decoration_thickness
        self.debug_label = debug_label
        self.font_family = font_family
        self.font_family_fallback = font_family_fallback
        self.package = package
        self.overflow = overflow


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class SizeWithCopy:
    def __init__(
            self,
            source: Size,
    ):
        self.source = source


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class SizeWithSquare:
    def __init__(
            self,
            dimension: float,
    ):
        self.dimension = dimension


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class SizeWithFromWidth:
    def __init__(
            self,
            width: float,
    ):
        self.width = width


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class SizeWithFromHeight:
    def __init__(
            self,
            height: float,
    ):
        self.height = height


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class SizeWithFromRadius:
    def __init__(
            self,
            radius: float,
    ):
        self.radius = radius


# bin/cache/pkg/sky_engine/lib/ui/geometry.dart
class Size:
    def __init__(
            self,
            width: float,
            height: float,
    ):
        self.width = width
        self.height = height

    @staticmethod
    def with_copy(
            source: Size,
    ) -> SizeWithCopy:
        return SizeWithCopy(
            source,
        )

    @staticmethod
    def with_square(
            dimension: float,
    ) -> SizeWithSquare:
        return SizeWithSquare(
            dimension,
        )

    @staticmethod
    def with_fromWidth(
            width: float,
    ) -> SizeWithFromWidth:
        return SizeWithFromWidth(
            width,
        )

    @staticmethod
    def with_fromHeight(
            height: float,
    ) -> SizeWithFromHeight:
        return SizeWithFromHeight(
            height,
        )

    @staticmethod
    def with_fromRadius(
            radius: float,
    ) -> SizeWithFromRadius:
        return SizeWithFromRadius(
            radius,
        )


# packages/flutter/lib/src/rendering/box.dart
class BoxConstraintsWithTight:
    def __init__(
            self,
            size: Size,
    ):
        self.size = size


# packages/flutter/lib/src/rendering/box.dart
class BoxConstraintsWithTightFor:
    def __init__(
            self,
            width: Optional[float] = None,
            height: Optional[float] = None,
    ):
        self.width = width
        self.height = height


# packages/flutter/lib/src/rendering/box.dart
class BoxConstraintsWithTightForFinite:
    def __init__(
            self,
            width: Optional[float] = None,
            height: Optional[float] = None,
    ):
        self.width = width
        self.height = height


# packages/flutter/lib/src/rendering/box.dart
class BoxConstraintsWithLoose:
    def __init__(
            self,
            size: Size,
    ):
        self.size = size


# packages/flutter/lib/src/rendering/box.dart
class BoxConstraintsWithExpand:
    def __init__(
            self,
            width: Optional[float] = None,
            height: Optional[float] = None,
    ):
        self.width = width
        self.height = height


# packages/flutter/lib/src/rendering/box.dart
class BoxConstraints:
    def __init__(
            self,
            min_width: Optional[float] = None,
            max_width: Optional[float] = None,
            min_height: Optional[float] = None,
            max_height: Optional[float] = None,
    ):
        self.min_width = min_width
        self.max_width = max_width
        self.min_height = min_height
        self.max_height = max_height

    @staticmethod
    def with_tight(
            size: Size,
    ) -> BoxConstraintsWithTight:
        return BoxConstraintsWithTight(
            size,
        )

    @staticmethod
    def with_tightFor(
            width: Optional[float] = None,
            height: Optional[float] = None,
    ) -> BoxConstraintsWithTightFor:
        return BoxConstraintsWithTightFor(
            width,
            height,
        )

    @staticmethod
    def with_tightForFinite(
            width: Optional[float] = None,
            height: Optional[float] = None,
    ) -> BoxConstraintsWithTightForFinite:
        return BoxConstraintsWithTightForFinite(
            width,
            height,
        )

    @staticmethod
    def with_loose(
            size: Size,
    ) -> BoxConstraintsWithLoose:
        return BoxConstraintsWithLoose(
            size,
        )

    @staticmethod
    def with_expand(
            width: Optional[float] = None,
            height: Optional[float] = None,
    ) -> BoxConstraintsWithExpand:
        return BoxConstraintsWithExpand(
            width,
            height,
        )


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
        self.text_style = text_style
        self.constraints = constraints
        self.color = color
        self.selected_color = selected_color
        self.disabled_color = disabled_color
        self.fill_color = fill_color
        self.focus_color = focus_color
        self.highlight_color = highlight_color
        self.hover_color = hover_color
        self.splash_color = splash_color
        self.border_color = border_color
        self.selected_border_color = selected_border_color
        self.disabled_border_color = disabled_border_color
        self.border_radius = border_radius
        self.border_width = border_width


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
        self.headline1 = headline1
        self.headline2 = headline2
        self.headline3 = headline3
        self.headline4 = headline4
        self.headline5 = headline5
        self.headline6 = headline6
        self.subtitle1 = subtitle1
        self.subtitle2 = subtitle2
        self.body_text1 = body_text1
        self.body_text2 = body_text2
        self.caption = caption
        self.button = button
        self.overline = overline


# packages/flutter/lib/src/painting/borders.dart
class BorderSide:
    def __init__(
            self,
            color: Optional[Color] = None,
            width: Optional[float] = None,
            style: Optional[BorderStyle] = None,
    ):
        self.color = color
        self.width = width
        self.style = style


# packages/flutter/lib/src/material/input_border.dart
class InputBorder:
    def __init__(
            self,
            border_side: Optional[BorderSide] = None,
    ):
        self.border_side = border_side


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
        self.label_style = label_style
        self.floating_label_style = floating_label_style
        self.helper_style = helper_style
        self.helper_max_lines = helper_max_lines
        self.hint_style = hint_style
        self.error_style = error_style
        self.error_max_lines = error_max_lines
        self.floating_label_behavior = floating_label_behavior
        self.is_dense = is_dense
        self.content_padding = content_padding
        self.is_collapsed = is_collapsed
        self.prefix_style = prefix_style
        self.suffix_style = suffix_style
        self.counter_style = counter_style
        self.filled = filled
        self.fill_color = fill_color
        self.focus_color = focus_color
        self.hover_color = hover_color
        self.error_border = error_border
        self.focused_border = focused_border
        self.focused_error_border = focused_error_border
        self.disabled_border = disabled_border
        self.enabled_border = enabled_border
        self.border = border
        self.align_label_with_hint = align_label_with_hint
        self.constraints = constraints


# packages/flutter/lib/src/widgets/icon_theme_data.dart
class IconThemeDataWithFallback:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/widgets/icon_theme_data.dart
class IconThemeData:
    def __init__(
            self,
            color: Optional[Color] = None,
            opacity: Optional[float] = None,
            size: Optional[float] = None,
    ):
        self.color = color
        self.opacity = opacity
        self.size = size

    @staticmethod
    def with_fallback(
    ) -> IconThemeDataWithFallback:
        return IconThemeDataWithFallback(
        )


# packages/flutter/lib/src/material/slider_theme.dart
class SliderThemeDataWithFromPrimaryColors:
    def __init__(
            self,
            primary_color: Color,
            primary_color_dark: Color,
            primary_color_light: Color,
            value_indicator_text_style: TextStyle,
    ):
        self.primary_color = primary_color
        self.primary_color_dark = primary_color_dark
        self.primary_color_light = primary_color_light
        self.value_indicator_text_style = value_indicator_text_style


# packages/flutter/lib/src/material/slider_theme.dart
class SliderComponentShape:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/slider_theme.dart
class SliderTickMarkShape:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/slider_theme.dart
class SliderTrackShape:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderTickMarkShape:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderThumbShape:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderTrackShape:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/slider_theme.dart
class RangeSliderValueIndicatorShape:
    def __init__(
            self,
    ):
        pass


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
        self.track_height = track_height
        self.active_track_color = active_track_color
        self.inactive_track_color = inactive_track_color
        self.disabled_active_track_color = disabled_active_track_color
        self.disabled_inactive_track_color = disabled_inactive_track_color
        self.active_tick_mark_color = active_tick_mark_color
        self.inactive_tick_mark_color = inactive_tick_mark_color
        self.disabled_active_tick_mark_color = disabled_active_tick_mark_color
        self.disabled_inactive_tick_mark_color = disabled_inactive_tick_mark_color
        self.thumb_color = thumb_color
        self.overlapping_shape_stroke_color = overlapping_shape_stroke_color
        self.disabled_thumb_color = disabled_thumb_color
        self.overlay_color = overlay_color
        self.value_indicator_color = value_indicator_color
        self.overlay_shape = overlay_shape
        self.tick_mark_shape = tick_mark_shape
        self.thumb_shape = thumb_shape
        self.track_shape = track_shape
        self.value_indicator_shape = value_indicator_shape
        self.range_tick_mark_shape = range_tick_mark_shape
        self.range_thumb_shape = range_thumb_shape
        self.range_track_shape = range_track_shape
        self.range_value_indicator_shape = range_value_indicator_shape
        self.show_value_indicator = show_value_indicator
        self.value_indicator_text_style = value_indicator_text_style
        self.min_thumb_separation = min_thumb_separation
        self.thumb_selector = thumb_selector

    @staticmethod
    def with_fromPrimaryColors(
            primary_color: Color,
            primary_color_dark: Color,
            primary_color_light: Color,
            value_indicator_text_style: TextStyle,
    ) -> SliderThemeDataWithFromPrimaryColors:
        return SliderThemeDataWithFromPrimaryColors(
            primary_color,
            primary_color_dark,
            primary_color_light,
            value_indicator_text_style,
        )


# packages/flutter/lib/src/painting/decoration.dart
class Decoration:
    def __init__(
            self,
    ):
        pass


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
        self.indicator = indicator
        self.indicator_size = indicator_size
        self.label_color = label_color
        self.label_padding = label_padding
        self.label_style = label_style
        self.unselected_label_color = unselected_label_color
        self.unselected_label_style = unselected_label_style


# bin/cache/pkg/sky_engine/lib/core/duration.dart
class DurationWith_microseconds:
    def __init__(
            self,
            _duration: int,
    ):
        self._duration = _duration


# bin/cache/pkg/sky_engine/lib/core/duration.dart
class Duration:
    def __init__(
            self,
            days: Optional[int] = None,
            hours: Optional[int] = None,
            minutes: Optional[int] = None,
            seconds: Optional[int] = None,
            milliseconds: Optional[int] = None,
            microseconds: Optional[int] = None,
    ):
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds
        self.microseconds = microseconds

    @staticmethod
    def with__microseconds(
            _duration: int,
    ) -> DurationWith_microseconds:
        return DurationWith_microseconds(
            _duration,
        )


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
        self.height = height
        self.padding = padding
        self.margin = margin
        self.vertical_offset = vertical_offset
        self.prefer_below = prefer_below
        self.exclude_from_semantics = exclude_from_semantics
        self.decoration = decoration
        self.text_style = text_style
        self.wait_duration = wait_duration
        self.show_duration = show_duration
        self.trigger_mode = trigger_mode
        self.enable_feedback = enable_feedback


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
        self.clip_behavior = clip_behavior
        self.color = color
        self.shadow_color = shadow_color
        self.elevation = elevation
        self.margin = margin
        self.shape = shape


# packages/flutter/lib/src/material/chip_theme.dart
class ChipThemeDataWithFromDefaults:
    def __init__(
            self,
            secondary_color: Color,
            label_style: TextStyle,
            brightness: Optional[Brightness] = None,
            primary_color: Optional[Color] = None,
    ):
        self.secondary_color = secondary_color
        self.label_style = label_style
        self.brightness = brightness
        self.primary_color = primary_color


# packages/flutter/lib/src/painting/borders.dart
class OutlinedBorder:
    def __init__(
            self,
            side: Optional[BorderSide] = None,
    ):
        self.side = side


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
        self.background_color = background_color
        self.disabled_color = disabled_color
        self.selected_color = selected_color
        self.secondary_selected_color = secondary_selected_color
        self.padding = padding
        self.label_style = label_style
        self.secondary_label_style = secondary_label_style
        self.brightness = brightness
        self.delete_icon_color = delete_icon_color
        self.shadow_color = shadow_color
        self.selected_shadow_color = selected_shadow_color
        self.show_checkmark = show_checkmark
        self.checkmark_color = checkmark_color
        self.label_padding = label_padding
        self.side = side
        self.shape = shape
        self.elevation = elevation
        self.press_elevation = press_elevation

    @staticmethod
    def with_fromDefaults(
            secondary_color: Color,
            label_style: TextStyle,
            brightness: Optional[Brightness] = None,
            primary_color: Optional[Color] = None,
    ) -> ChipThemeDataWithFromDefaults:
        return ChipThemeDataWithFromDefaults(
            secondary_color,
            label_style,
            brightness,
            primary_color,
        )


# packages/flutter/lib/src/material/page_transitions_theme.dart
class PageTransitionsBuilder:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/page_transitions_theme.dart
class PageTransitionsTheme:
    def __init__(
            self,
            builders: Optional[Dict[TargetPlatform, PageTransitionsBuilder]] = None,
    ):
        self.builders = builders


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
        self.system_navigation_bar_color = system_navigation_bar_color
        self.system_navigation_bar_divider_color = system_navigation_bar_divider_color
        self.system_navigation_bar_icon_brightness = system_navigation_bar_icon_brightness
        self.system_navigation_bar_contrast_enforced = system_navigation_bar_contrast_enforced
        self.status_bar_color = status_bar_color
        self.status_bar_brightness = status_bar_brightness
        self.status_bar_icon_brightness = status_bar_icon_brightness
        self.system_status_bar_contrast_enforced = system_status_bar_contrast_enforced


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
        self.brightness = brightness
        self.color = color
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.elevation = elevation
        self.shadow_color = shadow_color
        self.shape = shape
        self.icon_theme = icon_theme
        self.actions_icon_theme = actions_icon_theme
        self.text_theme = text_theme
        self.center_title = center_title
        self.title_spacing = title_spacing
        self.toolbar_height = toolbar_height
        self.toolbar_text_style = toolbar_text_style
        self.title_text_style = title_text_style
        self.system_overlay_style = system_overlay_style
        self.backwards_compatibility = backwards_compatibility


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
        self.thickness = thickness
        self.show_track_on_hover = show_track_on_hover
        self.is_always_shown = is_always_shown
        self.radius = radius
        self.thumb_color = thumb_color
        self.track_color = track_color
        self.track_border_color = track_border_color
        self.cross_axis_margin = cross_axis_margin
        self.main_axis_margin = main_axis_margin
        self.min_thumb_length = min_thumb_length
        self.interactive = interactive


# packages/flutter/lib/src/painting/notched_shapes.dart
class NotchedShape:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/bottom_app_bar_theme.dart
class BottomAppBarTheme:
    def __init__(
            self,
            color: Optional[Color] = None,
            elevation: Optional[float] = None,
            shape: Optional[NotchedShape] = None,
    ):
        self.color = color
        self.elevation = elevation
        self.shape = shape


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
        self.background_color = background_color
        self.elevation = elevation
        self.shape = shape
        self.title_text_style = title_text_style
        self.content_text_style = content_text_style


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
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.focus_color = focus_color
        self.hover_color = hover_color
        self.splash_color = splash_color
        self.elevation = elevation
        self.focus_elevation = focus_elevation
        self.hover_elevation = hover_elevation
        self.disabled_elevation = disabled_elevation
        self.highlight_elevation = highlight_elevation
        self.shape = shape
        self.enable_feedback = enable_feedback
        self.size_constraints = size_constraints
        self.small_size_constraints = small_size_constraints
        self.large_size_constraints = large_size_constraints
        self.extended_size_constraints = extended_size_constraints
        self.extended_icon_label_spacing = extended_icon_label_spacing
        self.extended_padding = extended_padding
        self.extended_text_style = extended_text_style


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
        self.background_color = background_color
        self.elevation = elevation
        self.unselected_label_text_style = unselected_label_text_style
        self.selected_label_text_style = selected_label_text_style
        self.unselected_icon_theme = unselected_icon_theme
        self.selected_icon_theme = selected_icon_theme
        self.group_alignment = group_alignment
        self.label_type = label_type


# packages/flutter/lib/src/material/typography.dart
class TypographyWithMaterial2014:
    def __init__(
            self,
            platform: Optional[TargetPlatform] = None,
            black: Optional[TextTheme] = None,
            white: Optional[TextTheme] = None,
            english_like: Optional[TextTheme] = None,
            dense: Optional[TextTheme] = None,
            tall: Optional[TextTheme] = None,
    ):
        self.platform = platform
        self.black = black
        self.white = white
        self.english_like = english_like
        self.dense = dense
        self.tall = tall


# packages/flutter/lib/src/material/typography.dart
class TypographyWithMaterial2018:
    def __init__(
            self,
            platform: Optional[TargetPlatform] = None,
            black: Optional[TextTheme] = None,
            white: Optional[TextTheme] = None,
            english_like: Optional[TextTheme] = None,
            dense: Optional[TextTheme] = None,
            tall: Optional[TextTheme] = None,
    ):
        self.platform = platform
        self.black = black
        self.white = white
        self.english_like = english_like
        self.dense = dense
        self.tall = tall


# packages/flutter/lib/src/material/typography.dart
class TypographyWith_withPlatform:
    def __init__(
            self,
            platform: TargetPlatform,
            black: TextTheme,
            white: TextTheme,
            english_like: TextTheme,
            dense: TextTheme,
            tall: TextTheme,
    ):
        self.platform = platform
        self.black = black
        self.white = white
        self.english_like = english_like
        self.dense = dense
        self.tall = tall


# packages/flutter/lib/src/material/typography.dart
class TypographyWith_:
    def __init__(
            self,
            black: TextTheme,
            white: TextTheme,
            english_like: TextTheme,
            dense: TextTheme,
            tall: TextTheme,
    ):
        self.black = black
        self.white = white
        self.english_like = english_like
        self.dense = dense
        self.tall = tall


# packages/flutter/lib/src/material/typography.dart
class Typography:
    def __init__(
            self,
            platform: Optional[TargetPlatform] = None,
            black: Optional[TextTheme] = None,
            white: Optional[TextTheme] = None,
            english_like: Optional[TextTheme] = None,
            dense: Optional[TextTheme] = None,
            tall: Optional[TextTheme] = None,
    ):
        self.platform = platform
        self.black = black
        self.white = white
        self.english_like = english_like
        self.dense = dense
        self.tall = tall

    @staticmethod
    def with_material2014(
            platform: Optional[TargetPlatform] = None,
            black: Optional[TextTheme] = None,
            white: Optional[TextTheme] = None,
            english_like: Optional[TextTheme] = None,
            dense: Optional[TextTheme] = None,
            tall: Optional[TextTheme] = None,
    ) -> TypographyWithMaterial2014:
        return TypographyWithMaterial2014(
            platform,
            black,
            white,
            english_like,
            dense,
            tall,
        )

    @staticmethod
    def with_material2018(
            platform: Optional[TargetPlatform] = None,
            black: Optional[TextTheme] = None,
            white: Optional[TextTheme] = None,
            english_like: Optional[TextTheme] = None,
            dense: Optional[TextTheme] = None,
            tall: Optional[TextTheme] = None,
    ) -> TypographyWithMaterial2018:
        return TypographyWithMaterial2018(
            platform,
            black,
            white,
            english_like,
            dense,
            tall,
        )

    @staticmethod
    def with__withPlatform(
            platform: TargetPlatform,
            black: TextTheme,
            white: TextTheme,
            english_like: TextTheme,
            dense: TextTheme,
            tall: TextTheme,
    ) -> TypographyWith_withPlatform:
        return TypographyWith_withPlatform(
            platform,
            black,
            white,
            english_like,
            dense,
            tall,
        )

    @staticmethod
    def with__(
            black: TextTheme,
            white: TextTheme,
            english_like: TextTheme,
            dense: TextTheme,
            tall: TextTheme,
    ) -> TypographyWith_:
        return TypographyWith_(
            black,
            white,
            english_like,
            dense,
            tall,
        )


# packages/flutter/lib/src/cupertino/text_theme.dart
class _TextThemeDefaultsBuilder:
    def __init__(
            self,
            label_color: Color,
            inactive_gray_color: Color,
    ):
        self.label_color = label_color
        self.inactive_gray_color = inactive_gray_color


# packages/flutter/lib/src/cupertino/text_theme.dart
class CupertinoTextThemeDataWith_raw:
    def __init__(
            self,
            _defaults: _TextThemeDefaultsBuilder,
            _primary_color: Color,
            _text_style: TextStyle,
            _action_text_style: TextStyle,
            _tab_label_text_style: TextStyle,
            _nav_title_text_style: TextStyle,
            _nav_large_title_text_style: TextStyle,
            _nav_action_text_style: TextStyle,
            _picker_text_style: TextStyle,
            _date_time_picker_text_style: TextStyle,
    ):
        self._defaults = _defaults
        self._primary_color = _primary_color
        self._text_style = _text_style
        self._action_text_style = _action_text_style
        self._tab_label_text_style = _tab_label_text_style
        self._nav_title_text_style = _nav_title_text_style
        self._nav_large_title_text_style = _nav_large_title_text_style
        self._nav_action_text_style = _nav_action_text_style
        self._picker_text_style = _picker_text_style
        self._date_time_picker_text_style = _date_time_picker_text_style


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
        self.primary_color = primary_color
        self.text_style = text_style
        self.action_text_style = action_text_style
        self.tab_label_text_style = tab_label_text_style
        self.nav_title_text_style = nav_title_text_style
        self.nav_large_title_text_style = nav_large_title_text_style
        self.nav_action_text_style = nav_action_text_style
        self.picker_text_style = picker_text_style
        self.date_time_picker_text_style = date_time_picker_text_style

    @staticmethod
    def with__raw(
            _defaults: _TextThemeDefaultsBuilder,
            _primary_color: Color,
            _text_style: TextStyle,
            _action_text_style: TextStyle,
            _tab_label_text_style: TextStyle,
            _nav_title_text_style: TextStyle,
            _nav_large_title_text_style: TextStyle,
            _nav_action_text_style: TextStyle,
            _picker_text_style: TextStyle,
            _date_time_picker_text_style: TextStyle,
    ) -> CupertinoTextThemeDataWith_raw:
        return CupertinoTextThemeDataWith_raw(
            _defaults,
            _primary_color,
            _text_style,
            _action_text_style,
            _tab_label_text_style,
            _nav_title_text_style,
            _nav_large_title_text_style,
            _nav_action_text_style,
            _picker_text_style,
            _date_time_picker_text_style,
        )


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
        self.brightness = brightness
        self.primary_color = primary_color
        self.primary_contrasting_color = primary_contrasting_color
        self.text_theme = text_theme
        self.bar_background_color = bar_background_color
        self.scaffold_background_color = scaffold_background_color


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
        self.background_color = background_color
        self.action_text_color = action_text_color
        self.disabled_action_text_color = disabled_action_text_color
        self.content_text_style = content_text_style
        self.elevation = elevation
        self.shape = shape
        self.behavior = behavior


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
        self.background_color = background_color
        self.elevation = elevation
        self.modal_background_color = modal_background_color
        self.modal_elevation = modal_elevation
        self.shape = shape
        self.clip_behavior = clip_behavior
        self.constraints = constraints


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
        self.color = color
        self.shape = shape
        self.elevation = elevation
        self.text_style = text_style
        self.enable_feedback = enable_feedback


# packages/flutter/lib/src/material/banner_theme.dart
class MaterialBannerThemeData:
    def __init__(
            self,
            background_color: Optional[Color] = None,
            content_text_style: Optional[TextStyle] = None,
            padding: Optional[EdgeInsetsGeometry] = None,
            leading_padding: Optional[EdgeInsetsGeometry] = None,
    ):
        self.background_color = background_color
        self.content_text_style = content_text_style
        self.padding = padding
        self.leading_padding = leading_padding


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
        self.color = color
        self.space = space
        self.thickness = thickness
        self.indent = indent
        self.end_indent = end_indent


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
        self.alignment = alignment
        self.main_axis_size = main_axis_size
        self.button_text_theme = button_text_theme
        self.button_min_width = button_min_width
        self.button_height = button_height
        self.button_padding = button_padding
        self.button_aligned_dropdown = button_aligned_dropdown
        self.layout_behavior = layout_behavior
        self.overflow_direction = overflow_direction


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
        self.background_color = background_color
        self.elevation = elevation
        self.selected_icon_theme = selected_icon_theme
        self.unselected_icon_theme = unselected_icon_theme
        self.selected_item_color = selected_item_color
        self.unselected_item_color = unselected_item_color
        self.selected_label_style = selected_label_style
        self.unselected_label_style = unselected_label_style
        self.show_selected_labels = show_selected_labels
        self.show_unselected_labels = show_unselected_labels
        self.type = type
        self.enable_feedback = enable_feedback
        self.landscape_layout = landscape_layout


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
        self.background_color = background_color
        self.hour_minute_text_color = hour_minute_text_color
        self.hour_minute_color = hour_minute_color
        self.day_period_text_color = day_period_text_color
        self.day_period_color = day_period_color
        self.dial_hand_color = dial_hand_color
        self.dial_background_color = dial_background_color
        self.dial_text_color = dial_text_color
        self.entry_mode_icon_color = entry_mode_icon_color
        self.hour_minute_text_style = hour_minute_text_style
        self.day_period_text_style = day_period_text_style
        self.help_text_style = help_text_style
        self.shape = shape
        self.hour_minute_shape = hour_minute_shape
        self.day_period_shape = day_period_shape
        self.day_period_border_side = day_period_border_side
        self.input_decoration_theme = input_decoration_theme


# packages/flutter/lib/src/services/mouse_cursor.dart
class MouseCursor:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/painting/alignment.dart
class AlignmentGeometry:
    def __init__(
            self,
    ):
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
        self.text_style = text_style
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.overlay_color = overlay_color
        self.shadow_color = shadow_color
        self.elevation = elevation
        self.padding = padding
        self.minimum_size = minimum_size
        self.fixed_size = fixed_size
        self.maximum_size = maximum_size
        self.side = side
        self.shape = shape
        self.mouse_cursor = mouse_cursor
        self.visual_density = visual_density
        self.tap_target_size = tap_target_size
        self.animation_duration = animation_duration
        self.enable_feedback = enable_feedback
        self.alignment = alignment
        self.splash_factory = splash_factory


# packages/flutter/lib/src/material/text_button_theme.dart
class TextButtonThemeData:
    def __init__(
            self,
            style: Optional[ButtonStyle] = None,
    ):
        self.style = style


# packages/flutter/lib/src/material/elevated_button_theme.dart
class ElevatedButtonThemeData:
    def __init__(
            self,
            style: Optional[ButtonStyle] = None,
    ):
        self.style = style


# packages/flutter/lib/src/material/outlined_button_theme.dart
class OutlinedButtonThemeData:
    def __init__(
            self,
            style: Optional[ButtonStyle] = None,
    ):
        self.style = style


# packages/flutter/lib/src/material/text_selection_theme.dart
class TextSelectionThemeData:
    def __init__(
            self,
            cursor_color: Optional[Color] = None,
            selection_color: Optional[Color] = None,
            selection_handle_color: Optional[Color] = None,
    ):
        self.cursor_color = cursor_color
        self.selection_color = selection_color
        self.selection_handle_color = selection_handle_color


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
        self.decoration = decoration
        self.data_row_color = data_row_color
        self.data_row_height = data_row_height
        self.data_text_style = data_text_style
        self.heading_row_color = heading_row_color
        self.heading_row_height = heading_row_height
        self.heading_text_style = heading_text_style
        self.horizontal_margin = horizontal_margin
        self.column_spacing = column_spacing
        self.divider_thickness = divider_thickness
        self.checkbox_horizontal_margin = checkbox_horizontal_margin


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
        self.mouse_cursor = mouse_cursor
        self.fill_color = fill_color
        self.check_color = check_color
        self.overlay_color = overlay_color
        self.splash_radius = splash_radius
        self.material_tap_target_size = material_tap_target_size
        self.visual_density = visual_density
        self.shape = shape
        self.side = side


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
        self.mouse_cursor = mouse_cursor
        self.fill_color = fill_color
        self.overlay_color = overlay_color
        self.splash_radius = splash_radius
        self.material_tap_target_size = material_tap_target_size
        self.visual_density = visual_density


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
        self.thumb_color = thumb_color
        self.track_color = track_color
        self.material_tap_target_size = material_tap_target_size
        self.mouse_cursor = mouse_cursor
        self.overlay_color = overlay_color
        self.splash_radius = splash_radius


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
        self.color = color
        self.linear_track_color = linear_track_color
        self.linear_min_height = linear_min_height
        self.circular_track_color = circular_track_color
        self.refresh_background_color = refresh_background_color


# packages/flutter/lib/src/material/theme_data.dart
class ThemeDataWithRaw:
    def __init__(
            self,
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
        self.visual_density = visual_density
        self.primary_color = primary_color
        self.primary_color_brightness = primary_color_brightness
        self.primary_color_light = primary_color_light
        self.primary_color_dark = primary_color_dark
        self.canvas_color = canvas_color
        self.shadow_color = shadow_color
        self.accent_color = accent_color
        self.accent_color_brightness = accent_color_brightness
        self.scaffold_background_color = scaffold_background_color
        self.bottom_app_bar_color = bottom_app_bar_color
        self.card_color = card_color
        self.divider_color = divider_color
        self.focus_color = focus_color
        self.hover_color = hover_color
        self.highlight_color = highlight_color
        self.splash_color = splash_color
        self.splash_factory = splash_factory
        self.selected_row_color = selected_row_color
        self.unselected_widget_color = unselected_widget_color
        self.disabled_color = disabled_color
        self.button_theme = button_theme
        self.button_color = button_color
        self.toggle_buttons_theme = toggle_buttons_theme
        self.secondary_header_color = secondary_header_color
        self.text_selection_color = text_selection_color
        self.cursor_color = cursor_color
        self.text_selection_handle_color = text_selection_handle_color
        self.background_color = background_color
        self.dialog_background_color = dialog_background_color
        self.indicator_color = indicator_color
        self.hint_color = hint_color
        self.error_color = error_color
        self.toggleable_active_color = toggleable_active_color
        self.text_theme = text_theme
        self.primary_text_theme = primary_text_theme
        self.accent_text_theme = accent_text_theme
        self.input_decoration_theme = input_decoration_theme
        self.icon_theme = icon_theme
        self.primary_icon_theme = primary_icon_theme
        self.accent_icon_theme = accent_icon_theme
        self.slider_theme = slider_theme
        self.tab_bar_theme = tab_bar_theme
        self.tooltip_theme = tooltip_theme
        self.card_theme = card_theme
        self.chip_theme = chip_theme
        self.platform = platform
        self.material_tap_target_size = material_tap_target_size
        self.apply_elevation_overlay_color = apply_elevation_overlay_color
        self.page_transitions_theme = page_transitions_theme
        self.app_bar_theme = app_bar_theme
        self.scrollbar_theme = scrollbar_theme
        self.bottom_app_bar_theme = bottom_app_bar_theme
        self.color_scheme = color_scheme
        self.dialog_theme = dialog_theme
        self.floating_action_button_theme = floating_action_button_theme
        self.navigation_rail_theme = navigation_rail_theme
        self.typography = typography
        self.cupertino_override_theme = cupertino_override_theme
        self.snack_bar_theme = snack_bar_theme
        self.bottom_sheet_theme = bottom_sheet_theme
        self.popup_menu_theme = popup_menu_theme
        self.banner_theme = banner_theme
        self.divider_theme = divider_theme
        self.button_bar_theme = button_bar_theme
        self.bottom_navigation_bar_theme = bottom_navigation_bar_theme
        self.time_picker_theme = time_picker_theme
        self.text_button_theme = text_button_theme
        self.elevated_button_theme = elevated_button_theme
        self.outlined_button_theme = outlined_button_theme
        self.text_selection_theme = text_selection_theme
        self.data_table_theme = data_table_theme
        self.checkbox_theme = checkbox_theme
        self.radio_theme = radio_theme
        self.switch_theme = switch_theme
        self.progress_indicator_theme = progress_indicator_theme
        self.fix_text_field_outline_label = fix_text_field_outline_label
        self.use_text_selection_theme = use_text_selection_theme


# packages/flutter/lib/src/material/theme_data.dart
class ThemeDataWithFrom:
    def __init__(
            self,
            color_scheme: ColorScheme,
            text_theme: Optional[TextTheme] = None,
    ):
        self.color_scheme = color_scheme
        self.text_theme = text_theme


# packages/flutter/lib/src/material/theme_data.dart
class ThemeDataWithLight:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/theme_data.dart
class ThemeDataWithDark:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/theme_data.dart
class ThemeDataWithFallback:
    def __init__(
            self,
    ):
        pass


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
        self.brightness = brightness
        self.visual_density = visual_density
        self.primary_swatch = primary_swatch
        self.primary_color = primary_color
        self.primary_color_brightness = primary_color_brightness
        self.primary_color_light = primary_color_light
        self.primary_color_dark = primary_color_dark
        self.accent_color = accent_color
        self.accent_color_brightness = accent_color_brightness
        self.canvas_color = canvas_color
        self.shadow_color = shadow_color
        self.scaffold_background_color = scaffold_background_color
        self.bottom_app_bar_color = bottom_app_bar_color
        self.card_color = card_color
        self.divider_color = divider_color
        self.focus_color = focus_color
        self.hover_color = hover_color
        self.highlight_color = highlight_color
        self.splash_color = splash_color
        self.splash_factory = splash_factory
        self.selected_row_color = selected_row_color
        self.unselected_widget_color = unselected_widget_color
        self.disabled_color = disabled_color
        self.button_color = button_color
        self.button_theme = button_theme
        self.toggle_buttons_theme = toggle_buttons_theme
        self.secondary_header_color = secondary_header_color
        self.text_selection_color = text_selection_color
        self.cursor_color = cursor_color
        self.text_selection_handle_color = text_selection_handle_color
        self.background_color = background_color
        self.dialog_background_color = dialog_background_color
        self.indicator_color = indicator_color
        self.hint_color = hint_color
        self.error_color = error_color
        self.toggleable_active_color = toggleable_active_color
        self.font_family = font_family
        self.text_theme = text_theme
        self.primary_text_theme = primary_text_theme
        self.accent_text_theme = accent_text_theme
        self.input_decoration_theme = input_decoration_theme
        self.icon_theme = icon_theme
        self.primary_icon_theme = primary_icon_theme
        self.accent_icon_theme = accent_icon_theme
        self.slider_theme = slider_theme
        self.tab_bar_theme = tab_bar_theme
        self.tooltip_theme = tooltip_theme
        self.card_theme = card_theme
        self.chip_theme = chip_theme
        self.platform = platform
        self.material_tap_target_size = material_tap_target_size
        self.apply_elevation_overlay_color = apply_elevation_overlay_color
        self.page_transitions_theme = page_transitions_theme
        self.app_bar_theme = app_bar_theme
        self.scrollbar_theme = scrollbar_theme
        self.bottom_app_bar_theme = bottom_app_bar_theme
        self.color_scheme = color_scheme
        self.dialog_theme = dialog_theme
        self.floating_action_button_theme = floating_action_button_theme
        self.navigation_rail_theme = navigation_rail_theme
        self.typography = typography
        self.cupertino_override_theme = cupertino_override_theme
        self.snack_bar_theme = snack_bar_theme
        self.bottom_sheet_theme = bottom_sheet_theme
        self.popup_menu_theme = popup_menu_theme
        self.banner_theme = banner_theme
        self.divider_theme = divider_theme
        self.button_bar_theme = button_bar_theme
        self.bottom_navigation_bar_theme = bottom_navigation_bar_theme
        self.time_picker_theme = time_picker_theme
        self.text_button_theme = text_button_theme
        self.elevated_button_theme = elevated_button_theme
        self.outlined_button_theme = outlined_button_theme
        self.text_selection_theme = text_selection_theme
        self.data_table_theme = data_table_theme
        self.checkbox_theme = checkbox_theme
        self.radio_theme = radio_theme
        self.switch_theme = switch_theme
        self.progress_indicator_theme = progress_indicator_theme
        self.fix_text_field_outline_label = fix_text_field_outline_label
        self.use_text_selection_theme = use_text_selection_theme

    @staticmethod
    def with_raw(
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
    ) -> ThemeDataWithRaw:
        return ThemeDataWithRaw(
            visual_density,
            primary_color,
            primary_color_brightness,
            primary_color_light,
            primary_color_dark,
            canvas_color,
            shadow_color,
            accent_color,
            accent_color_brightness,
            scaffold_background_color,
            bottom_app_bar_color,
            card_color,
            divider_color,
            focus_color,
            hover_color,
            highlight_color,
            splash_color,
            splash_factory,
            selected_row_color,
            unselected_widget_color,
            disabled_color,
            button_theme,
            button_color,
            toggle_buttons_theme,
            secondary_header_color,
            text_selection_color,
            cursor_color,
            text_selection_handle_color,
            background_color,
            dialog_background_color,
            indicator_color,
            hint_color,
            error_color,
            toggleable_active_color,
            text_theme,
            primary_text_theme,
            accent_text_theme,
            input_decoration_theme,
            icon_theme,
            primary_icon_theme,
            accent_icon_theme,
            slider_theme,
            tab_bar_theme,
            tooltip_theme,
            card_theme,
            chip_theme,
            platform,
            material_tap_target_size,
            apply_elevation_overlay_color,
            page_transitions_theme,
            app_bar_theme,
            scrollbar_theme,
            bottom_app_bar_theme,
            color_scheme,
            dialog_theme,
            floating_action_button_theme,
            navigation_rail_theme,
            typography,
            cupertino_override_theme,
            snack_bar_theme,
            bottom_sheet_theme,
            popup_menu_theme,
            banner_theme,
            divider_theme,
            button_bar_theme,
            bottom_navigation_bar_theme,
            time_picker_theme,
            text_button_theme,
            elevated_button_theme,
            outlined_button_theme,
            text_selection_theme,
            data_table_theme,
            checkbox_theme,
            radio_theme,
            switch_theme,
            progress_indicator_theme,
            fix_text_field_outline_label,
            use_text_selection_theme,
        )

    @staticmethod
    def with_from(
            color_scheme: ColorScheme,
            text_theme: Optional[TextTheme] = None,
    ) -> ThemeDataWithFrom:
        return ThemeDataWithFrom(
            color_scheme,
            text_theme,
        )

    @staticmethod
    def with_light(
    ) -> ThemeDataWithLight:
        return ThemeDataWithLight(
        )

    @staticmethod
    def with_dark(
    ) -> ThemeDataWithDark:
        return ThemeDataWithDark(
        )

    @staticmethod
    def with_fallback(
    ) -> ThemeDataWithFallback:
        return ThemeDataWithFallback(
        )


# packages/flutter/lib/src/widgets/shortcuts.dart
class ShortcutActivator:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/widgets/actions.dart
class Intent:
    def __init__(
            self,
    ):
        pass


# bin/cache/pkg/sky_engine/lib/core/type.dart
class Type:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/widgets/scroll_configuration.dart
class ScrollBehavior:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/material/app.dart
class MaterialAppWithRouter:
    def __init__(
            self,
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
            localizations_delegates: Optional[Iterable[LocalizationsDelegate[any]]] = None,
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
        self.route_information_parser = route_information_parser
        self.router_delegate = router_delegate
        self.key = key
        self.scaffold_messenger_key = scaffold_messenger_key
        self.route_information_provider = route_information_provider
        self.back_button_dispatcher = back_button_dispatcher
        self.builder = builder
        self.title = title
        self.on_generate_title = on_generate_title
        self.color = color
        self.theme = theme
        self.dark_theme = dark_theme
        self.high_contrast_theme = high_contrast_theme
        self.high_contrast_dark_theme = high_contrast_dark_theme
        self.theme_mode = theme_mode
        self.locale = locale
        self.localizations_delegates = localizations_delegates
        self.locale_list_resolution_callback = locale_list_resolution_callback
        self.locale_resolution_callback = locale_resolution_callback
        self.supported_locales = supported_locales
        self.debug_show_material_grid = debug_show_material_grid
        self.show_performance_overlay = show_performance_overlay
        self.checkerboard_raster_cache_images = checkerboard_raster_cache_images
        self.checkerboard_offscreen_layers = checkerboard_offscreen_layers
        self.show_semantics_debugger = show_semantics_debugger
        self.debug_show_checked_mode_banner = debug_show_checked_mode_banner
        self.shortcuts = shortcuts
        self.actions = actions
        self.restoration_scope_id = restoration_scope_id
        self.scroll_behavior = scroll_behavior
        self.use_inherited_media_query = use_inherited_media_query


# packages/flutter/lib/src/widgets/navigator.dart
class NavigatorState:
    def __init__(
            self,
    ):
        pass


# packages/flutter/lib/src/widgets/framework.dart
class Widget:
    def __init__(
            self,
            key: Optional[Key] = None,
    ):
        self.key = key


# packages/flutter/lib/src/widgets/navigator.dart
class NavigatorObserver:
    def __init__(
            self,
    ):
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
            localizations_delegates: Optional[Iterable[LocalizationsDelegate[any]]] = None,
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
        self.key = key
        self.navigator_key = navigator_key
        self.scaffold_messenger_key = scaffold_messenger_key
        self.home = home
        self.routes = routes
        self.initial_route = initial_route
        self.on_generate_route = on_generate_route
        self.on_generate_initial_routes = on_generate_initial_routes
        self.on_unknown_route = on_unknown_route
        self.navigator_observers = navigator_observers
        self.builder = builder
        self.title = title
        self.on_generate_title = on_generate_title
        self.color = color
        self.theme = theme
        self.dark_theme = dark_theme
        self.high_contrast_theme = high_contrast_theme
        self.high_contrast_dark_theme = high_contrast_dark_theme
        self.theme_mode = theme_mode
        self.locale = locale
        self.localizations_delegates = localizations_delegates
        self.locale_list_resolution_callback = locale_list_resolution_callback
        self.locale_resolution_callback = locale_resolution_callback
        self.supported_locales = supported_locales
        self.debug_show_material_grid = debug_show_material_grid
        self.show_performance_overlay = show_performance_overlay
        self.checkerboard_raster_cache_images = checkerboard_raster_cache_images
        self.checkerboard_offscreen_layers = checkerboard_offscreen_layers
        self.show_semantics_debugger = show_semantics_debugger
        self.debug_show_checked_mode_banner = debug_show_checked_mode_banner
        self.shortcuts = shortcuts
        self.actions = actions
        self.restoration_scope_id = restoration_scope_id
        self.scroll_behavior = scroll_behavior
        self.use_inherited_media_query = use_inherited_media_query

    @staticmethod
    def with_router(
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
            localizations_delegates: Optional[Iterable[LocalizationsDelegate[any]]] = None,
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
    ) -> MaterialAppWithRouter:
        return MaterialAppWithRouter(
            route_information_parser,
            router_delegate,
            key,
            scaffold_messenger_key,
            route_information_provider,
            back_button_dispatcher,
            builder,
            title,
            on_generate_title,
            color,
            theme,
            dark_theme,
            high_contrast_theme,
            high_contrast_dark_theme,
            theme_mode,
            locale,
            localizations_delegates,
            locale_list_resolution_callback,
            locale_resolution_callback,
            supported_locales,
            debug_show_material_grid,
            show_performance_overlay,
            checkerboard_raster_cache_images,
            checkerboard_offscreen_layers,
            show_semantics_debugger,
            debug_show_checked_mode_banner,
            shortcuts,
            actions,
            restoration_scope_id,
            scroll_behavior,
            use_inherited_media_query,
        )


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
        self.debug_label = debug_label
        self.on_key = on_key
        self.on_key_event = on_key_event
        self.skip_traversal = skip_traversal
        self.can_request_focus = can_request_focus
        self.descendants_are_focusable = descendants_are_focusable


# packages/flutter/lib/src/material/elevated_button.dart
class ElevatedButtonWithIcon:
    def __init__(
            self,
            on_pressed: Callable,
            icon: Widget,
            label: Widget,
            key: Optional[Key] = None,
            on_long_press: Optional[Callable] = None,
            style: Optional[ButtonStyle] = None,
            focus_node: Optional[FocusNode] = None,
            autofocus: Optional[bool] = None,
            clip_behavior: Optional[Clip] = None,
    ):
        self.on_pressed = on_pressed
        self.icon = icon
        self.label = label
        self.key = key
        self.on_long_press = on_long_press
        self.style = style
        self.focus_node = focus_node
        self.autofocus = autofocus
        self.clip_behavior = clip_behavior


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
        self.on_pressed = on_pressed
        self.child = child
        self.key = key
        self.on_long_press = on_long_press
        self.style = style
        self.focus_node = focus_node
        self.autofocus = autofocus
        self.clip_behavior = clip_behavior

    @staticmethod
    def with_icon(
            on_pressed: Callable,
            icon: Widget,
            label: Widget,
            key: Optional[Key] = None,
            on_long_press: Optional[Callable] = None,
            style: Optional[ButtonStyle] = None,
            focus_node: Optional[FocusNode] = None,
            autofocus: Optional[bool] = None,
            clip_behavior: Optional[Clip] = None,
    ) -> ElevatedButtonWithIcon:
        return ElevatedButtonWithIcon(
            on_pressed,
            icon,
            label,
            key,
            on_long_press,
            style,
            focus_node,
            autofocus,
            clip_behavior,
        )
