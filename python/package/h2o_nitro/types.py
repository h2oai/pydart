from enum import Enum
from typing import Callable, Optional


class MaterialTapTargetSize(Enum):
    INDEX = 'index'
    VALUES = 'values'
    PADDED = 'padded'
    SHRINK_WRAP = 'shrinkWrap'


class Clip(Enum):
    INDEX = 'index'
    VALUES = 'values'
    NONE = 'none'
    HARD_EDGE = 'hardEdge'
    ANTI_ALIAS = 'antiAlias'
    ANTI_ALIAS_WITH_SAVE_LAYER = 'antiAliasWithSaveLayer'


class KeyWithEmpty:
    def __init__(
            self,
    ):
        pass


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


class MaterialStateProperty:
    def __init__(
            self,
    ):
        pass


class VisualDensity:
    def __init__(
            self,
            horizontal: Optional[float] = None,
            vertical: Optional[float] = None,
    ):
        self.horizontal = horizontal
        self.vertical = vertical


class DurationWith_microseconds:
    def __init__(
            self,
            _duration: int,
    ):
        self._duration = _duration


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


class AlignmentGeometry:
    def __init__(
            self,
    ):
        pass


class InteractiveInkFeatureFactory:
    def __init__(
            self,
    ):
        pass


class ButtonStyle:
    def __init__(
            self,
            text_style: Optional[MaterialStateProperty] = None,
            background_color: Optional[MaterialStateProperty] = None,
            foreground_color: Optional[MaterialStateProperty] = None,
            overlay_color: Optional[MaterialStateProperty] = None,
            shadow_color: Optional[MaterialStateProperty] = None,
            elevation: Optional[MaterialStateProperty] = None,
            padding: Optional[MaterialStateProperty] = None,
            minimum_size: Optional[MaterialStateProperty] = None,
            fixed_size: Optional[MaterialStateProperty] = None,
            maximum_size: Optional[MaterialStateProperty] = None,
            side: Optional[MaterialStateProperty] = None,
            shape: Optional[MaterialStateProperty] = None,
            mouse_cursor: Optional[MaterialStateProperty] = None,
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


class Widget:
    def __init__(
            self,
            key: Optional[Key] = None,
    ):
        self.key = key


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
        self.key = key
        self.on_pressed = on_pressed
        self.on_long_press = on_long_press
        self.style = style
        self.focus_node = focus_node
        self.autofocus = autofocus
        self.clip_behavior = clip_behavior
        self.icon = icon
        self.label = label


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
        self.key = key
        self.on_pressed = on_pressed
        self.on_long_press = on_long_press
        self.style = style
        self.focus_node = focus_node
        self.autofocus = autofocus
        self.clip_behavior = clip_behavior
        self.child = child

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
            key,
            on_pressed,
            on_long_press,
            style,
            focus_node,
            autofocus,
            clip_behavior,
            icon,
            label,
        )
