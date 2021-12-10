from h2o_nitro import *


def _sample_object():
    return Object(
    )


def _sample_route_settings():
    return RouteSettings(
        name='String 42',
        arguments=_sample_object(),
    )


def _min_sample_route_settings():
    return RouteSettings(
    )


def _sample_navigator_observer():
    return NavigatorObserver(
    )


def _sample_navigator():
    return Navigator(
        key=_notfound_key(),
        pages=[_notfound_page(), _notfound_page(), _notfound_page()],
        on_pop_page=_noop,
        initial_route='String 42',
        on_generate_initial_routes=_noop,
        on_generate_route=_noop,
        on_unknown_route=_noop,
        transition_delegate=_notfound_transition_delegate(),
        reports_route_update_to_engine=True,
        observers=[_sample_navigator_observer(), _sample_navigator_observer(), _sample_navigator_observer()],
        restoration_scope_id='String 43',
    )


def _min_sample_navigator():
    return Navigator(
    )


def _sample_navigator_state():
    return NavigatorState(
    )


def _sample_scaffold_messenger():
    return ScaffoldMessenger(
        child=_sample_navigator(),
        key=_notfound_key(),
    )


def _min_sample_scaffold_messenger():
    return ScaffoldMessenger(
        child=_sample_navigator(),
    )


def _sample_scaffold_messenger_state():
    return ScaffoldMessengerState(
    )


def _sample_color():
    return Color(
        value=42,
    )


def _sample_color__from_argb():
    return Color.from_argb(
        a=42,
        r=43,
        g=44,
        b=45,
    )


def _sample_color__from_rgbo():
    return Color.from_rgbo(
        r=42,
        g=43,
        b=44,
        opacity=0.45,
    )


def _sample_visual_density():
    return VisualDensity(
        horizontal=0.42,
        vertical=0.43,
    )


def _min_sample_visual_density():
    return VisualDensity(
    )


def _sample_color_swatch():
    return ColorSwatch(
        primary=42,
        _swatch={undefined: _sample_color(), undefined: _sample_color(), undefined: _sample_color()},
    )


def _sample_material_color():
    return MaterialColor(
        primary=42,
        swatch={43: _sample_color(), 44: _sample_color(), 45: _sample_color()},
    )


def _sample_color_scheme():
    return ColorScheme(
        primary=_sample_color(),
        primary_variant=_sample_color(),
        secondary=_sample_color(),
        secondary_variant=_sample_color(),
        surface=_sample_color(),
        background=_sample_color(),
        error=_sample_color(),
        on_primary=_sample_color(),
        on_secondary=_sample_color(),
        on_surface=_sample_color(),
        on_background=_sample_color(),
        on_error=_sample_color(),
        brightness=Brightness.light,
    )


def _sample_color_scheme__light():
    return ColorScheme.light(
        primary=_sample_color(),
        primary_variant=_sample_color(),
        secondary=_sample_color(),
        secondary_variant=_sample_color(),
        surface=_sample_color(),
        background=_sample_color(),
        error=_sample_color(),
        on_primary=_sample_color(),
        on_secondary=_sample_color(),
        on_surface=_sample_color(),
        on_background=_sample_color(),
        on_error=_sample_color(),
        brightness=Brightness.light,
    )


def _min_sample_color_scheme__light():
    return ColorScheme.light(
    )


def _sample_color_scheme__dark():
    return ColorScheme.dark(
        primary=_sample_color(),
        primary_variant=_sample_color(),
        secondary=_sample_color(),
        secondary_variant=_sample_color(),
        surface=_sample_color(),
        background=_sample_color(),
        error=_sample_color(),
        on_primary=_sample_color(),
        on_secondary=_sample_color(),
        on_surface=_sample_color(),
        on_background=_sample_color(),
        on_error=_sample_color(),
        brightness=Brightness.light,
    )


def _min_sample_color_scheme__dark():
    return ColorScheme.dark(
    )


def _sample_color_scheme__high_contrast_light():
    return ColorScheme.high_contrast_light(
        primary=_sample_color(),
        primary_variant=_sample_color(),
        secondary=_sample_color(),
        secondary_variant=_sample_color(),
        surface=_sample_color(),
        background=_sample_color(),
        error=_sample_color(),
        on_primary=_sample_color(),
        on_secondary=_sample_color(),
        on_surface=_sample_color(),
        on_background=_sample_color(),
        on_error=_sample_color(),
        brightness=Brightness.light,
    )


def _min_sample_color_scheme__high_contrast_light():
    return ColorScheme.high_contrast_light(
    )


def _sample_color_scheme__high_contrast_dark():
    return ColorScheme.high_contrast_dark(
        primary=_sample_color(),
        primary_variant=_sample_color(),
        secondary=_sample_color(),
        secondary_variant=_sample_color(),
        surface=_sample_color(),
        background=_sample_color(),
        error=_sample_color(),
        on_primary=_sample_color(),
        on_secondary=_sample_color(),
        on_surface=_sample_color(),
        on_background=_sample_color(),
        on_error=_sample_color(),
        brightness=Brightness.light,
    )


def _min_sample_color_scheme__high_contrast_dark():
    return ColorScheme.high_contrast_dark(
    )


def _sample_color_scheme__from_swatch():
    return ColorScheme.from_swatch(
        primary_swatch=_sample_material_color(),
        primary_color_dark=_sample_color(),
        accent_color=_sample_color(),
        card_color=_sample_color(),
        background_color=_sample_color(),
        error_color=_sample_color(),
        brightness=Brightness.light,
    )


def _min_sample_color_scheme__from_swatch():
    return ColorScheme.from_swatch(
    )


def _sample_button_theme_data():
    return ButtonThemeData(
        text_theme=ButtonTextTheme.primary,
        min_width=0.42,
        height=0.43,
        padding=_notfound_edge_insets_geometry(),
        shape=_notfound_shape_border(),
        layout_behavior=ButtonBarLayoutBehavior.padded,
        aligned_dropdown=True,
        button_color=_sample_color(),
        disabled_color=_sample_color(),
        focus_color=_sample_color(),
        hover_color=_sample_color(),
        highlight_color=_sample_color(),
        splash_color=_sample_color(),
        color_scheme=_sample_color_scheme(),
        material_tap_target_size=MaterialTapTargetSize.shrink_wrap,
    )


def _min_sample_button_theme_data():
    return ButtonThemeData(
    )


def _sample_locale():
    return Locale(
        _language_code='String 42',
        _country_code='String 43',
    )


def _min_sample_locale():
    return Locale(
        _language_code='String 42',
    )


def _sample_locale__from_subtags():
    return Locale.from_subtags(
        language_code='String 42',
        script_code='String 43',
        country_code='String 44',
    )


def _min_sample_locale__from_subtags():
    return Locale.from_subtags(
    )


def _sample_paint():
    return Paint(
    )


def _sample_offset():
    return Offset(
        dx=0.42,
        dy=0.43,
    )


def _sample_offset__from_direction():
    return Offset.from_direction(
        direction=0.42,
        distance=0.43,
    )


def _min_sample_offset__from_direction():
    return Offset.from_direction(
        direction=0.42,
    )


def _sample_shadow():
    return Shadow(
        color=_sample_color(),
        offset=_sample_offset(),
        blur_radius=0.42,
    )


def _min_sample_shadow():
    return Shadow(
    )


def _sample_font_feature():
    return FontFeature(
        feature='String 42',
        value=43,
    )


def _min_sample_font_feature():
    return FontFeature(
        feature='String 42',
    )


def _sample_font_feature__enable():
    return FontFeature.enable(
        feature='String 42',
    )


def _sample_font_feature__disable():
    return FontFeature.disable(
        feature='String 42',
    )


def _sample_font_feature__alternative():
    return FontFeature.alternative(
        value=42,
    )


def _sample_font_feature__alternative_fractions():
    return FontFeature.alternative_fractions(
    )


def _sample_font_feature__contextual_alternates():
    return FontFeature.contextual_alternates(
    )


def _sample_font_feature__case_sensitive_forms():
    return FontFeature.case_sensitive_forms(
    )


def _sample_font_feature__character_variant():
    return FontFeature.character_variant(
        value=42,
    )


def _sample_font_feature__denominator():
    return FontFeature.denominator(
    )


def _sample_font_feature__fractions():
    return FontFeature.fractions(
    )


def _sample_font_feature__historical_forms():
    return FontFeature.historical_forms(
    )


def _sample_font_feature__historical_ligatures():
    return FontFeature.historical_ligatures(
    )


def _sample_font_feature__lining_figures():
    return FontFeature.lining_figures(
    )


def _sample_font_feature__locale_aware():
    return FontFeature.locale_aware(
        enable=True,
    )


def _min_sample_font_feature__locale_aware():
    return FontFeature.locale_aware(
    )


def _sample_font_feature__notational_forms():
    return FontFeature.notational_forms(
        value=42,
    )


def _min_sample_font_feature__notational_forms():
    return FontFeature.notational_forms(
    )


def _sample_font_feature__numerators():
    return FontFeature.numerators(
    )


def _sample_font_feature__oldstyle_figures():
    return FontFeature.oldstyle_figures(
    )


def _sample_font_feature__ordinal_forms():
    return FontFeature.ordinal_forms(
    )


def _sample_font_feature__proportional_figures():
    return FontFeature.proportional_figures(
    )


def _sample_font_feature__randomize():
    return FontFeature.randomize(
    )


def _sample_font_feature__stylistic_alternates():
    return FontFeature.stylistic_alternates(
    )


def _sample_font_feature__scientific_inferiors():
    return FontFeature.scientific_inferiors(
    )


def _sample_font_feature__stylistic_set():
    return FontFeature.stylistic_set(
        value=42,
    )


def _sample_font_feature__subscripts():
    return FontFeature.subscripts(
    )


def _sample_font_feature__superscripts():
    return FontFeature.superscripts(
    )


def _sample_font_feature__swash():
    return FontFeature.swash(
        value=42,
    )


def _min_sample_font_feature__swash():
    return FontFeature.swash(
    )


def _sample_font_feature__tabular_figures():
    return FontFeature.tabular_figures(
    )


def _sample_font_feature__slashed_zero():
    return FontFeature.slashed_zero(
    )


def _sample_text_decoration__combine():
    return TextDecoration.combine(
        decorations=[_sample_text_decoration(), _sample_text_decoration(), _sample_text_decoration()],
    )


def _sample_text_style():
    return TextStyle(
        inherit=True,
        color=_sample_color(),
        background_color=_sample_color(),
        font_size=0.42,
        font_weight=_sample_font_weight(),
        font_style=FontStyle.italic,
        letter_spacing=0.43,
        word_spacing=0.44,
        text_baseline=TextBaseline.ideographic,
        height=0.45,
        leading_distribution=TextLeadingDistribution.even,
        locale=_sample_locale(),
        foreground=_sample_paint(),
        background=_sample_paint(),
        shadows=[_sample_shadow(), _sample_shadow(), _sample_shadow()],
        font_features=[_sample_font_feature(), _sample_font_feature(), _sample_font_feature()],
        decoration=_sample_text_decoration(),
        decoration_color=_sample_color(),
        decoration_style=TextDecorationStyle.wavy,
        decoration_thickness=0.46,
        debug_label='String 47',
        font_family='String 48',
        font_family_fallback=['String 49', 'String 50', 'String 51'],
        package='String 52',
        overflow=TextOverflow.visible,
    )


def _min_sample_text_style():
    return TextStyle(
    )


def _sample_size():
    return Size(
        width=0.42,
        height=0.43,
    )


def _sample_size__copy():
    return Size.copy(
        source=_sample_size(),
    )


def _sample_size__square():
    return Size.square(
        dimension=0.42,
    )


def _sample_size__from_width():
    return Size.from_width(
        width=0.42,
    )


def _sample_size__from_height():
    return Size.from_height(
        height=0.42,
    )


def _sample_size__from_radius():
    return Size.from_radius(
        radius=0.42,
    )


def _sample_box_constraints():
    return BoxConstraints(
        min_width=0.42,
        max_width=0.43,
        min_height=0.44,
        max_height=0.45,
    )


def _min_sample_box_constraints():
    return BoxConstraints(
    )


def _sample_box_constraints__tight():
    return BoxConstraints.tight(
        size=_sample_size(),
    )


def _sample_box_constraints__tight_for():
    return BoxConstraints.tight_for(
        width=0.42,
        height=0.43,
    )


def _min_sample_box_constraints__tight_for():
    return BoxConstraints.tight_for(
    )


def _sample_box_constraints__tight_for_finite():
    return BoxConstraints.tight_for_finite(
        width=0.42,
        height=0.43,
    )


def _min_sample_box_constraints__tight_for_finite():
    return BoxConstraints.tight_for_finite(
    )


def _sample_box_constraints__loose():
    return BoxConstraints.loose(
        size=_sample_size(),
    )


def _sample_box_constraints__expand():
    return BoxConstraints.expand(
        width=0.42,
        height=0.43,
    )


def _min_sample_box_constraints__expand():
    return BoxConstraints.expand(
    )


def _sample_radius__circular():
    return Radius.circular(
        radius=0.42,
    )


def _sample_radius__elliptical():
    return Radius.elliptical(
        x=0.42,
        y=0.43,
    )


def _sample_border_radius__all():
    return BorderRadius.all(
        radius=_sample_radius(),
    )


def _sample_border_radius__circular():
    return BorderRadius.circular(
        radius=0.42,
    )


def _sample_border_radius__vertical():
    return BorderRadius.vertical(
        top=_sample_radius(),
        bottom=_sample_radius(),
    )


def _min_sample_border_radius__vertical():
    return BorderRadius.vertical(
    )


def _sample_border_radius__horizontal():
    return BorderRadius.horizontal(
        left=_sample_radius(),
        right=_sample_radius(),
    )


def _min_sample_border_radius__horizontal():
    return BorderRadius.horizontal(
    )


def _sample_border_radius__only():
    return BorderRadius.only(
        top_left=_sample_radius(),
        top_right=_sample_radius(),
        bottom_left=_sample_radius(),
        bottom_right=_sample_radius(),
    )


def _min_sample_border_radius__only():
    return BorderRadius.only(
    )


def _sample_toggle_buttons_theme_data():
    return ToggleButtonsThemeData(
        text_style=_sample_text_style(),
        constraints=_sample_box_constraints(),
        color=_sample_color(),
        selected_color=_sample_color(),
        disabled_color=_sample_color(),
        fill_color=_sample_color(),
        focus_color=_sample_color(),
        highlight_color=_sample_color(),
        hover_color=_sample_color(),
        splash_color=_sample_color(),
        border_color=_sample_color(),
        selected_border_color=_sample_color(),
        disabled_border_color=_sample_color(),
        border_radius=_sample_border_radius(),
        border_width=0.42,
    )


def _min_sample_toggle_buttons_theme_data():
    return ToggleButtonsThemeData(
    )


def _sample_text_theme():
    return TextTheme(
        headline1=_sample_text_style(),
        headline2=_sample_text_style(),
        headline3=_sample_text_style(),
        headline4=_sample_text_style(),
        headline5=_sample_text_style(),
        headline6=_sample_text_style(),
        subtitle1=_sample_text_style(),
        subtitle2=_sample_text_style(),
        body_text1=_sample_text_style(),
        body_text2=_sample_text_style(),
        caption=_sample_text_style(),
        button=_sample_text_style(),
        overline=_sample_text_style(),
    )


def _min_sample_text_theme():
    return TextTheme(
    )


def _sample_border_side():
    return BorderSide(
        color=_sample_color(),
        width=0.42,
        style=BorderStyle.solid,
    )


def _min_sample_border_side():
    return BorderSide(
    )


def _sample_input_decoration_theme():
    return InputDecorationTheme(
        label_style=_sample_text_style(),
        floating_label_style=_sample_text_style(),
        helper_style=_sample_text_style(),
        helper_max_lines=42,
        hint_style=_sample_text_style(),
        error_style=_sample_text_style(),
        error_max_lines=43,
        floating_label_behavior=FloatingLabelBehavior.always,
        is_dense=True,
        content_padding=_notfound_edge_insets_geometry(),
        is_collapsed=True,
        prefix_style=_sample_text_style(),
        suffix_style=_sample_text_style(),
        counter_style=_sample_text_style(),
        filled=True,
        fill_color=_sample_color(),
        focus_color=_sample_color(),
        hover_color=_sample_color(),
        error_border=_notfound_input_border(),
        focused_border=_notfound_input_border(),
        focused_error_border=_notfound_input_border(),
        disabled_border=_notfound_input_border(),
        enabled_border=_notfound_input_border(),
        border=_notfound_input_border(),
        align_label_with_hint=True,
        constraints=_sample_box_constraints(),
    )


def _min_sample_input_decoration_theme():
    return InputDecorationTheme(
    )


def _sample_icon_theme_data():
    return IconThemeData(
        color=_sample_color(),
        opacity=0.42,
        size=0.43,
    )


def _min_sample_icon_theme_data():
    return IconThemeData(
    )


def _sample_icon_theme_data__fallback():
    return IconThemeData.fallback(
    )


def _sample_range_values():
    return RangeValues(
        start=0.42,
        end=0.43,
    )


def _sample_slider_theme_data():
    return SliderThemeData(
        track_height=0.42,
        active_track_color=_sample_color(),
        inactive_track_color=_sample_color(),
        disabled_active_track_color=_sample_color(),
        disabled_inactive_track_color=_sample_color(),
        active_tick_mark_color=_sample_color(),
        inactive_tick_mark_color=_sample_color(),
        disabled_active_tick_mark_color=_sample_color(),
        disabled_inactive_tick_mark_color=_sample_color(),
        thumb_color=_sample_color(),
        overlapping_shape_stroke_color=_sample_color(),
        disabled_thumb_color=_sample_color(),
        overlay_color=_sample_color(),
        value_indicator_color=_sample_color(),
        overlay_shape=_notfound_slider_component_shape(),
        tick_mark_shape=_notfound_slider_tick_mark_shape(),
        thumb_shape=_notfound_slider_component_shape(),
        track_shape=_notfound_slider_track_shape(),
        value_indicator_shape=_notfound_slider_component_shape(),
        range_tick_mark_shape=_notfound_range_slider_tick_mark_shape(),
        range_thumb_shape=_notfound_range_slider_thumb_shape(),
        range_track_shape=_notfound_range_slider_track_shape(),
        range_value_indicator_shape=_notfound_range_slider_value_indicator_shape(),
        show_value_indicator=ShowValueIndicator.never,
        value_indicator_text_style=_sample_text_style(),
        min_thumb_separation=0.43,
        thumb_selector=_noop,
    )


def _min_sample_slider_theme_data():
    return SliderThemeData(
    )


def _sample_slider_theme_data__from_primary_colors():
    return SliderThemeData.from_primary_colors(
        primary_color=_sample_color(),
        primary_color_dark=_sample_color(),
        primary_color_light=_sample_color(),
        value_indicator_text_style=_sample_text_style(),
    )


def _sample_tab_bar_theme():
    return TabBarTheme(
        indicator=_notfound_decoration(),
        indicator_size=TabBarIndicatorSize.label,
        label_color=_sample_color(),
        label_padding=_notfound_edge_insets_geometry(),
        label_style=_sample_text_style(),
        unselected_label_color=_sample_color(),
        unselected_label_style=_sample_text_style(),
    )


def _min_sample_tab_bar_theme():
    return TabBarTheme(
    )


def _sample_duration():
    return Duration(
        days=42,
        hours=43,
        minutes=44,
        seconds=45,
        milliseconds=46,
        microseconds=47,
    )


def _min_sample_duration():
    return Duration(
    )


def _sample_tooltip_theme_data():
    return TooltipThemeData(
        height=0.42,
        padding=_notfound_edge_insets_geometry(),
        margin=_notfound_edge_insets_geometry(),
        vertical_offset=0.43,
        prefer_below=True,
        exclude_from_semantics=True,
        decoration=_notfound_decoration(),
        text_style=_sample_text_style(),
        wait_duration=_sample_duration(),
        show_duration=_sample_duration(),
        trigger_mode=TooltipTriggerMode.tap,
        enable_feedback=True,
    )


def _min_sample_tooltip_theme_data():
    return TooltipThemeData(
    )


def _sample_card_theme():
    return CardTheme(
        clip_behavior=Clip.anti_alias_with_save_layer,
        color=_sample_color(),
        shadow_color=_sample_color(),
        elevation=0.42,
        margin=_notfound_edge_insets_geometry(),
        shape=_notfound_shape_border(),
    )


def _min_sample_card_theme():
    return CardTheme(
    )


def _sample_chip_theme_data():
    return ChipThemeData(
        background_color=_sample_color(),
        disabled_color=_sample_color(),
        selected_color=_sample_color(),
        secondary_selected_color=_sample_color(),
        padding=_notfound_edge_insets_geometry(),
        label_style=_sample_text_style(),
        secondary_label_style=_sample_text_style(),
        brightness=Brightness.light,
        delete_icon_color=_sample_color(),
        shadow_color=_sample_color(),
        selected_shadow_color=_sample_color(),
        show_checkmark=True,
        checkmark_color=_sample_color(),
        label_padding=_notfound_edge_insets_geometry(),
        side=_sample_border_side(),
        shape=_notfound_outlined_border(),
        elevation=0.42,
        press_elevation=0.43,
    )


def _min_sample_chip_theme_data():
    return ChipThemeData(
        background_color=_sample_color(),
        disabled_color=_sample_color(),
        selected_color=_sample_color(),
        secondary_selected_color=_sample_color(),
        padding=_notfound_edge_insets_geometry(),
        label_style=_sample_text_style(),
        secondary_label_style=_sample_text_style(),
        brightness=Brightness.light,
    )


def _sample_chip_theme_data__from_defaults():
    return ChipThemeData.from_defaults(
        secondary_color=_sample_color(),
        label_style=_sample_text_style(),
        brightness=Brightness.light,
        primary_color=_sample_color(),
    )


def _min_sample_chip_theme_data__from_defaults():
    return ChipThemeData.from_defaults(
        secondary_color=_sample_color(),
        label_style=_sample_text_style(),
    )


def _sample_page_transitions_theme():
    return PageTransitionsTheme(
        builders={TargetPlatform.windows: _notfound_page_transitions_builder(), TargetPlatform.windows: _notfound_page_transitions_builder(), TargetPlatform.windows: _notfound_page_transitions_builder()},
    )


def _min_sample_page_transitions_theme():
    return PageTransitionsTheme(
    )


def _sample_system_ui_overlay_style():
    return SystemUiOverlayStyle(
        system_navigation_bar_color=_sample_color(),
        system_navigation_bar_divider_color=_sample_color(),
        system_navigation_bar_icon_brightness=Brightness.light,
        system_navigation_bar_contrast_enforced=True,
        status_bar_color=_sample_color(),
        status_bar_brightness=Brightness.light,
        status_bar_icon_brightness=Brightness.light,
        system_status_bar_contrast_enforced=True,
    )


def _min_sample_system_ui_overlay_style():
    return SystemUiOverlayStyle(
    )


def _sample_app_bar_theme():
    return AppBarTheme(
        brightness=Brightness.light,
        color=_sample_color(),
        background_color=_sample_color(),
        foreground_color=_sample_color(),
        elevation=0.42,
        shadow_color=_sample_color(),
        shape=_notfound_shape_border(),
        icon_theme=_sample_icon_theme_data(),
        actions_icon_theme=_sample_icon_theme_data(),
        text_theme=_sample_text_theme(),
        center_title=True,
        title_spacing=0.43,
        toolbar_height=0.44,
        toolbar_text_style=_sample_text_style(),
        title_text_style=_sample_text_style(),
        system_overlay_style=_sample_system_ui_overlay_style(),
        backwards_compatibility=True,
    )


def _min_sample_app_bar_theme():
    return AppBarTheme(
    )


def _sample_scrollbar_theme_data():
    return ScrollbarThemeData(
        thickness=_notfound_material_state_property(),
        show_track_on_hover=True,
        is_always_shown=True,
        radius=_sample_radius(),
        thumb_color=_notfound_material_state_property(),
        track_color=_notfound_material_state_property(),
        track_border_color=_notfound_material_state_property(),
        cross_axis_margin=0.42,
        main_axis_margin=0.43,
        min_thumb_length=0.44,
        interactive=True,
    )


def _min_sample_scrollbar_theme_data():
    return ScrollbarThemeData(
    )


def _sample_bottom_app_bar_theme():
    return BottomAppBarTheme(
        color=_sample_color(),
        elevation=0.42,
        shape=_notfound_notched_shape(),
    )


def _min_sample_bottom_app_bar_theme():
    return BottomAppBarTheme(
    )


def _sample_dialog_theme():
    return DialogTheme(
        background_color=_sample_color(),
        elevation=0.42,
        shape=_notfound_shape_border(),
        title_text_style=_sample_text_style(),
        content_text_style=_sample_text_style(),
    )


def _min_sample_dialog_theme():
    return DialogTheme(
    )


def _sample_floating_action_button_theme_data():
    return FloatingActionButtonThemeData(
        foreground_color=_sample_color(),
        background_color=_sample_color(),
        focus_color=_sample_color(),
        hover_color=_sample_color(),
        splash_color=_sample_color(),
        elevation=0.42,
        focus_elevation=0.43,
        hover_elevation=0.44,
        disabled_elevation=0.45,
        highlight_elevation=0.46,
        shape=_notfound_shape_border(),
        enable_feedback=True,
        size_constraints=_sample_box_constraints(),
        small_size_constraints=_sample_box_constraints(),
        large_size_constraints=_sample_box_constraints(),
        extended_size_constraints=_sample_box_constraints(),
        extended_icon_label_spacing=0.47,
        extended_padding=_notfound_edge_insets_geometry(),
        extended_text_style=_sample_text_style(),
    )


def _min_sample_floating_action_button_theme_data():
    return FloatingActionButtonThemeData(
    )


def _sample_navigation_rail_theme_data():
    return NavigationRailThemeData(
        background_color=_sample_color(),
        elevation=0.42,
        unselected_label_text_style=_sample_text_style(),
        selected_label_text_style=_sample_text_style(),
        unselected_icon_theme=_sample_icon_theme_data(),
        selected_icon_theme=_sample_icon_theme_data(),
        group_alignment=0.43,
        label_type=NavigationRailLabelType.all,
    )


def _min_sample_navigation_rail_theme_data():
    return NavigationRailThemeData(
    )


def _sample_typography():
    return Typography(
        platform=TargetPlatform.windows,
        black=_sample_text_theme(),
        white=_sample_text_theme(),
        english_like=_sample_text_theme(),
        dense=_sample_text_theme(),
        tall=_sample_text_theme(),
    )


def _min_sample_typography():
    return Typography(
    )


def _sample_typography__material2014():
    return Typography.material2014(
        platform=TargetPlatform.windows,
        black=_sample_text_theme(),
        white=_sample_text_theme(),
        english_like=_sample_text_theme(),
        dense=_sample_text_theme(),
        tall=_sample_text_theme(),
    )


def _min_sample_typography__material2014():
    return Typography.material2014(
    )


def _sample_typography__material2018():
    return Typography.material2018(
        platform=TargetPlatform.windows,
        black=_sample_text_theme(),
        white=_sample_text_theme(),
        english_like=_sample_text_theme(),
        dense=_sample_text_theme(),
        tall=_sample_text_theme(),
    )


def _min_sample_typography__material2018():
    return Typography.material2018(
    )


def _sample_cupertino_text_theme_data():
    return CupertinoTextThemeData(
        primary_color=_sample_color(),
        text_style=_sample_text_style(),
        action_text_style=_sample_text_style(),
        tab_label_text_style=_sample_text_style(),
        nav_title_text_style=_sample_text_style(),
        nav_large_title_text_style=_sample_text_style(),
        nav_action_text_style=_sample_text_style(),
        picker_text_style=_sample_text_style(),
        date_time_picker_text_style=_sample_text_style(),
    )


def _min_sample_cupertino_text_theme_data():
    return CupertinoTextThemeData(
    )


def _sample_no_default_cupertino_theme_data():
    return NoDefaultCupertinoThemeData(
        brightness=Brightness.light,
        primary_color=_sample_color(),
        primary_contrasting_color=_sample_color(),
        text_theme=_sample_cupertino_text_theme_data(),
        bar_background_color=_sample_color(),
        scaffold_background_color=_sample_color(),
    )


def _min_sample_no_default_cupertino_theme_data():
    return NoDefaultCupertinoThemeData(
    )


def _sample_snack_bar_theme_data():
    return SnackBarThemeData(
        background_color=_sample_color(),
        action_text_color=_sample_color(),
        disabled_action_text_color=_sample_color(),
        content_text_style=_sample_text_style(),
        elevation=0.42,
        shape=_notfound_shape_border(),
        behavior=SnackBarBehavior.floating,
    )


def _min_sample_snack_bar_theme_data():
    return SnackBarThemeData(
    )


def _sample_bottom_sheet_theme_data():
    return BottomSheetThemeData(
        background_color=_sample_color(),
        elevation=0.42,
        modal_background_color=_sample_color(),
        modal_elevation=0.43,
        shape=_notfound_shape_border(),
        clip_behavior=Clip.anti_alias_with_save_layer,
        constraints=_sample_box_constraints(),
    )


def _min_sample_bottom_sheet_theme_data():
    return BottomSheetThemeData(
    )


def _sample_popup_menu_theme_data():
    return PopupMenuThemeData(
        color=_sample_color(),
        shape=_notfound_shape_border(),
        elevation=0.42,
        text_style=_sample_text_style(),
        enable_feedback=True,
    )


def _min_sample_popup_menu_theme_data():
    return PopupMenuThemeData(
    )


def _sample_material_banner_theme_data():
    return MaterialBannerThemeData(
        background_color=_sample_color(),
        content_text_style=_sample_text_style(),
        padding=_notfound_edge_insets_geometry(),
        leading_padding=_notfound_edge_insets_geometry(),
    )


def _min_sample_material_banner_theme_data():
    return MaterialBannerThemeData(
    )


def _sample_divider_theme_data():
    return DividerThemeData(
        color=_sample_color(),
        space=0.42,
        thickness=0.43,
        indent=0.44,
        end_indent=0.45,
    )


def _min_sample_divider_theme_data():
    return DividerThemeData(
    )


def _sample_button_bar_theme_data():
    return ButtonBarThemeData(
        alignment=MainAxisAlignment.space_evenly,
        main_axis_size=MainAxisSize.max,
        button_text_theme=ButtonTextTheme.primary,
        button_min_width=0.42,
        button_height=0.43,
        button_padding=_notfound_edge_insets_geometry(),
        button_aligned_dropdown=True,
        layout_behavior=ButtonBarLayoutBehavior.padded,
        overflow_direction=VerticalDirection.down,
    )


def _min_sample_button_bar_theme_data():
    return ButtonBarThemeData(
    )


def _sample_bottom_navigation_bar_theme_data():
    return BottomNavigationBarThemeData(
        background_color=_sample_color(),
        elevation=0.42,
        selected_icon_theme=_sample_icon_theme_data(),
        unselected_icon_theme=_sample_icon_theme_data(),
        selected_item_color=_sample_color(),
        unselected_item_color=_sample_color(),
        selected_label_style=_sample_text_style(),
        unselected_label_style=_sample_text_style(),
        show_selected_labels=True,
        show_unselected_labels=True,
        type=BottomNavigationBarType.shifting,
        enable_feedback=True,
        landscape_layout=BottomNavigationBarLandscapeLayout.linear,
    )


def _min_sample_bottom_navigation_bar_theme_data():
    return BottomNavigationBarThemeData(
    )


def _sample_time_picker_theme_data():
    return TimePickerThemeData(
        background_color=_sample_color(),
        hour_minute_text_color=_sample_color(),
        hour_minute_color=_sample_color(),
        day_period_text_color=_sample_color(),
        day_period_color=_sample_color(),
        dial_hand_color=_sample_color(),
        dial_background_color=_sample_color(),
        dial_text_color=_sample_color(),
        entry_mode_icon_color=_sample_color(),
        hour_minute_text_style=_sample_text_style(),
        day_period_text_style=_sample_text_style(),
        help_text_style=_sample_text_style(),
        shape=_notfound_shape_border(),
        hour_minute_shape=_notfound_shape_border(),
        day_period_shape=_notfound_outlined_border(),
        day_period_border_side=_sample_border_side(),
        input_decoration_theme=_sample_input_decoration_theme(),
    )


def _min_sample_time_picker_theme_data():
    return TimePickerThemeData(
    )


def _sample_button_style():
    return ButtonStyle(
        text_style=_notfound_material_state_property(),
        background_color=_notfound_material_state_property(),
        foreground_color=_notfound_material_state_property(),
        overlay_color=_notfound_material_state_property(),
        shadow_color=_notfound_material_state_property(),
        elevation=_notfound_material_state_property(),
        padding=_notfound_material_state_property(),
        minimum_size=_notfound_material_state_property(),
        fixed_size=_notfound_material_state_property(),
        maximum_size=_notfound_material_state_property(),
        side=_notfound_material_state_property(),
        shape=_notfound_material_state_property(),
        mouse_cursor=_notfound_material_state_property(),
        visual_density=_sample_visual_density(),
        tap_target_size=MaterialTapTargetSize.shrink_wrap,
        animation_duration=_sample_duration(),
        enable_feedback=True,
        alignment=_notfound_alignment_geometry(),
        splash_factory=_notfound_interactive_ink_feature_factory(),
    )


def _min_sample_button_style():
    return ButtonStyle(
    )


def _sample_text_button_theme_data():
    return TextButtonThemeData(
        style=_sample_button_style(),
    )


def _min_sample_text_button_theme_data():
    return TextButtonThemeData(
    )


def _sample_elevated_button_theme_data():
    return ElevatedButtonThemeData(
        style=_sample_button_style(),
    )


def _min_sample_elevated_button_theme_data():
    return ElevatedButtonThemeData(
    )


def _sample_outlined_button_theme_data():
    return OutlinedButtonThemeData(
        style=_sample_button_style(),
    )


def _min_sample_outlined_button_theme_data():
    return OutlinedButtonThemeData(
    )


def _sample_text_selection_theme_data():
    return TextSelectionThemeData(
        cursor_color=_sample_color(),
        selection_color=_sample_color(),
        selection_handle_color=_sample_color(),
    )


def _min_sample_text_selection_theme_data():
    return TextSelectionThemeData(
    )


def _sample_data_table_theme_data():
    return DataTableThemeData(
        decoration=_notfound_decoration(),
        data_row_color=_notfound_material_state_property(),
        data_row_height=0.42,
        data_text_style=_sample_text_style(),
        heading_row_color=_notfound_material_state_property(),
        heading_row_height=0.43,
        heading_text_style=_sample_text_style(),
        horizontal_margin=0.44,
        column_spacing=0.45,
        divider_thickness=0.46,
        checkbox_horizontal_margin=0.47,
    )


def _min_sample_data_table_theme_data():
    return DataTableThemeData(
    )


def _sample_checkbox_theme_data():
    return CheckboxThemeData(
        mouse_cursor=_notfound_material_state_property(),
        fill_color=_notfound_material_state_property(),
        check_color=_notfound_material_state_property(),
        overlay_color=_notfound_material_state_property(),
        splash_radius=0.42,
        material_tap_target_size=MaterialTapTargetSize.shrink_wrap,
        visual_density=_sample_visual_density(),
        shape=_notfound_outlined_border(),
        side=_sample_border_side(),
    )


def _min_sample_checkbox_theme_data():
    return CheckboxThemeData(
    )


def _sample_radio_theme_data():
    return RadioThemeData(
        mouse_cursor=_notfound_material_state_property(),
        fill_color=_notfound_material_state_property(),
        overlay_color=_notfound_material_state_property(),
        splash_radius=0.42,
        material_tap_target_size=MaterialTapTargetSize.shrink_wrap,
        visual_density=_sample_visual_density(),
    )


def _min_sample_radio_theme_data():
    return RadioThemeData(
    )


def _sample_switch_theme_data():
    return SwitchThemeData(
        thumb_color=_notfound_material_state_property(),
        track_color=_notfound_material_state_property(),
        material_tap_target_size=MaterialTapTargetSize.shrink_wrap,
        mouse_cursor=_notfound_material_state_property(),
        overlay_color=_notfound_material_state_property(),
        splash_radius=0.42,
    )


def _min_sample_switch_theme_data():
    return SwitchThemeData(
    )


def _sample_progress_indicator_theme_data():
    return ProgressIndicatorThemeData(
        color=_sample_color(),
        linear_track_color=_sample_color(),
        linear_min_height=0.42,
        circular_track_color=_sample_color(),
        refresh_background_color=_sample_color(),
    )


def _min_sample_progress_indicator_theme_data():
    return ProgressIndicatorThemeData(
    )


def _sample_theme_data():
    return ThemeData(
        brightness=Brightness.light,
        visual_density=_sample_visual_density(),
        primary_swatch=_sample_material_color(),
        primary_color=_sample_color(),
        primary_color_brightness=Brightness.light,
        primary_color_light=_sample_color(),
        primary_color_dark=_sample_color(),
        accent_color=_sample_color(),
        accent_color_brightness=Brightness.light,
        canvas_color=_sample_color(),
        shadow_color=_sample_color(),
        scaffold_background_color=_sample_color(),
        bottom_app_bar_color=_sample_color(),
        card_color=_sample_color(),
        divider_color=_sample_color(),
        focus_color=_sample_color(),
        hover_color=_sample_color(),
        highlight_color=_sample_color(),
        splash_color=_sample_color(),
        splash_factory=_notfound_interactive_ink_feature_factory(),
        selected_row_color=_sample_color(),
        unselected_widget_color=_sample_color(),
        disabled_color=_sample_color(),
        button_color=_sample_color(),
        button_theme=_sample_button_theme_data(),
        toggle_buttons_theme=_sample_toggle_buttons_theme_data(),
        secondary_header_color=_sample_color(),
        text_selection_color=_sample_color(),
        cursor_color=_sample_color(),
        text_selection_handle_color=_sample_color(),
        background_color=_sample_color(),
        dialog_background_color=_sample_color(),
        indicator_color=_sample_color(),
        hint_color=_sample_color(),
        error_color=_sample_color(),
        toggleable_active_color=_sample_color(),
        font_family='String 42',
        text_theme=_sample_text_theme(),
        primary_text_theme=_sample_text_theme(),
        accent_text_theme=_sample_text_theme(),
        input_decoration_theme=_sample_input_decoration_theme(),
        icon_theme=_sample_icon_theme_data(),
        primary_icon_theme=_sample_icon_theme_data(),
        accent_icon_theme=_sample_icon_theme_data(),
        slider_theme=_sample_slider_theme_data(),
        tab_bar_theme=_sample_tab_bar_theme(),
        tooltip_theme=_sample_tooltip_theme_data(),
        card_theme=_sample_card_theme(),
        chip_theme=_sample_chip_theme_data(),
        platform=TargetPlatform.windows,
        material_tap_target_size=MaterialTapTargetSize.shrink_wrap,
        apply_elevation_overlay_color=True,
        page_transitions_theme=_sample_page_transitions_theme(),
        app_bar_theme=_sample_app_bar_theme(),
        scrollbar_theme=_sample_scrollbar_theme_data(),
        bottom_app_bar_theme=_sample_bottom_app_bar_theme(),
        color_scheme=_sample_color_scheme(),
        dialog_theme=_sample_dialog_theme(),
        floating_action_button_theme=_sample_floating_action_button_theme_data(),
        navigation_rail_theme=_sample_navigation_rail_theme_data(),
        typography=_sample_typography(),
        cupertino_override_theme=_sample_no_default_cupertino_theme_data(),
        snack_bar_theme=_sample_snack_bar_theme_data(),
        bottom_sheet_theme=_sample_bottom_sheet_theme_data(),
        popup_menu_theme=_sample_popup_menu_theme_data(),
        banner_theme=_sample_material_banner_theme_data(),
        divider_theme=_sample_divider_theme_data(),
        button_bar_theme=_sample_button_bar_theme_data(),
        bottom_navigation_bar_theme=_sample_bottom_navigation_bar_theme_data(),
        time_picker_theme=_sample_time_picker_theme_data(),
        text_button_theme=_sample_text_button_theme_data(),
        elevated_button_theme=_sample_elevated_button_theme_data(),
        outlined_button_theme=_sample_outlined_button_theme_data(),
        text_selection_theme=_sample_text_selection_theme_data(),
        data_table_theme=_sample_data_table_theme_data(),
        checkbox_theme=_sample_checkbox_theme_data(),
        radio_theme=_sample_radio_theme_data(),
        switch_theme=_sample_switch_theme_data(),
        progress_indicator_theme=_sample_progress_indicator_theme_data(),
        fix_text_field_outline_label=True,
        use_text_selection_theme=True,
    )


def _min_sample_theme_data():
    return ThemeData(
    )


def _sample_theme_data__raw():
    return ThemeData.raw(
        visual_density=_sample_visual_density(),
        primary_color=_sample_color(),
        primary_color_brightness=Brightness.light,
        primary_color_light=_sample_color(),
        primary_color_dark=_sample_color(),
        canvas_color=_sample_color(),
        shadow_color=_sample_color(),
        accent_color=_sample_color(),
        accent_color_brightness=Brightness.light,
        scaffold_background_color=_sample_color(),
        bottom_app_bar_color=_sample_color(),
        card_color=_sample_color(),
        divider_color=_sample_color(),
        focus_color=_sample_color(),
        hover_color=_sample_color(),
        highlight_color=_sample_color(),
        splash_color=_sample_color(),
        splash_factory=_notfound_interactive_ink_feature_factory(),
        selected_row_color=_sample_color(),
        unselected_widget_color=_sample_color(),
        disabled_color=_sample_color(),
        button_theme=_sample_button_theme_data(),
        button_color=_sample_color(),
        toggle_buttons_theme=_sample_toggle_buttons_theme_data(),
        secondary_header_color=_sample_color(),
        text_selection_color=_sample_color(),
        cursor_color=_sample_color(),
        text_selection_handle_color=_sample_color(),
        background_color=_sample_color(),
        dialog_background_color=_sample_color(),
        indicator_color=_sample_color(),
        hint_color=_sample_color(),
        error_color=_sample_color(),
        toggleable_active_color=_sample_color(),
        text_theme=_sample_text_theme(),
        primary_text_theme=_sample_text_theme(),
        accent_text_theme=_sample_text_theme(),
        input_decoration_theme=_sample_input_decoration_theme(),
        icon_theme=_sample_icon_theme_data(),
        primary_icon_theme=_sample_icon_theme_data(),
        accent_icon_theme=_sample_icon_theme_data(),
        slider_theme=_sample_slider_theme_data(),
        tab_bar_theme=_sample_tab_bar_theme(),
        tooltip_theme=_sample_tooltip_theme_data(),
        card_theme=_sample_card_theme(),
        chip_theme=_sample_chip_theme_data(),
        platform=TargetPlatform.windows,
        material_tap_target_size=MaterialTapTargetSize.shrink_wrap,
        apply_elevation_overlay_color=True,
        page_transitions_theme=_sample_page_transitions_theme(),
        app_bar_theme=_sample_app_bar_theme(),
        scrollbar_theme=_sample_scrollbar_theme_data(),
        bottom_app_bar_theme=_sample_bottom_app_bar_theme(),
        color_scheme=_sample_color_scheme(),
        dialog_theme=_sample_dialog_theme(),
        floating_action_button_theme=_sample_floating_action_button_theme_data(),
        navigation_rail_theme=_sample_navigation_rail_theme_data(),
        typography=_sample_typography(),
        snack_bar_theme=_sample_snack_bar_theme_data(),
        bottom_sheet_theme=_sample_bottom_sheet_theme_data(),
        popup_menu_theme=_sample_popup_menu_theme_data(),
        banner_theme=_sample_material_banner_theme_data(),
        divider_theme=_sample_divider_theme_data(),
        button_bar_theme=_sample_button_bar_theme_data(),
        bottom_navigation_bar_theme=_sample_bottom_navigation_bar_theme_data(),
        time_picker_theme=_sample_time_picker_theme_data(),
        text_button_theme=_sample_text_button_theme_data(),
        elevated_button_theme=_sample_elevated_button_theme_data(),
        outlined_button_theme=_sample_outlined_button_theme_data(),
        text_selection_theme=_sample_text_selection_theme_data(),
        data_table_theme=_sample_data_table_theme_data(),
        checkbox_theme=_sample_checkbox_theme_data(),
        radio_theme=_sample_radio_theme_data(),
        switch_theme=_sample_switch_theme_data(),
        progress_indicator_theme=_sample_progress_indicator_theme_data(),
        fix_text_field_outline_label=True,
        use_text_selection_theme=True,
        cupertino_override_theme=_sample_no_default_cupertino_theme_data(),
    )


def _min_sample_theme_data__raw():
    return ThemeData.raw(
        visual_density=_sample_visual_density(),
        primary_color=_sample_color(),
        primary_color_brightness=Brightness.light,
        primary_color_light=_sample_color(),
        primary_color_dark=_sample_color(),
        canvas_color=_sample_color(),
        shadow_color=_sample_color(),
        accent_color=_sample_color(),
        accent_color_brightness=Brightness.light,
        scaffold_background_color=_sample_color(),
        bottom_app_bar_color=_sample_color(),
        card_color=_sample_color(),
        divider_color=_sample_color(),
        focus_color=_sample_color(),
        hover_color=_sample_color(),
        highlight_color=_sample_color(),
        splash_color=_sample_color(),
        splash_factory=_notfound_interactive_ink_feature_factory(),
        selected_row_color=_sample_color(),
        unselected_widget_color=_sample_color(),
        disabled_color=_sample_color(),
        button_theme=_sample_button_theme_data(),
        button_color=_sample_color(),
        toggle_buttons_theme=_sample_toggle_buttons_theme_data(),
        secondary_header_color=_sample_color(),
        text_selection_color=_sample_color(),
        cursor_color=_sample_color(),
        text_selection_handle_color=_sample_color(),
        background_color=_sample_color(),
        dialog_background_color=_sample_color(),
        indicator_color=_sample_color(),
        hint_color=_sample_color(),
        error_color=_sample_color(),
        toggleable_active_color=_sample_color(),
        text_theme=_sample_text_theme(),
        primary_text_theme=_sample_text_theme(),
        accent_text_theme=_sample_text_theme(),
        input_decoration_theme=_sample_input_decoration_theme(),
        icon_theme=_sample_icon_theme_data(),
        primary_icon_theme=_sample_icon_theme_data(),
        accent_icon_theme=_sample_icon_theme_data(),
        slider_theme=_sample_slider_theme_data(),
        tab_bar_theme=_sample_tab_bar_theme(),
        tooltip_theme=_sample_tooltip_theme_data(),
        card_theme=_sample_card_theme(),
        chip_theme=_sample_chip_theme_data(),
        platform=TargetPlatform.windows,
        material_tap_target_size=MaterialTapTargetSize.shrink_wrap,
        apply_elevation_overlay_color=True,
        page_transitions_theme=_sample_page_transitions_theme(),
        app_bar_theme=_sample_app_bar_theme(),
        scrollbar_theme=_sample_scrollbar_theme_data(),
        bottom_app_bar_theme=_sample_bottom_app_bar_theme(),
        color_scheme=_sample_color_scheme(),
        dialog_theme=_sample_dialog_theme(),
        floating_action_button_theme=_sample_floating_action_button_theme_data(),
        navigation_rail_theme=_sample_navigation_rail_theme_data(),
        typography=_sample_typography(),
        snack_bar_theme=_sample_snack_bar_theme_data(),
        bottom_sheet_theme=_sample_bottom_sheet_theme_data(),
        popup_menu_theme=_sample_popup_menu_theme_data(),
        banner_theme=_sample_material_banner_theme_data(),
        divider_theme=_sample_divider_theme_data(),
        button_bar_theme=_sample_button_bar_theme_data(),
        bottom_navigation_bar_theme=_sample_bottom_navigation_bar_theme_data(),
        time_picker_theme=_sample_time_picker_theme_data(),
        text_button_theme=_sample_text_button_theme_data(),
        elevated_button_theme=_sample_elevated_button_theme_data(),
        outlined_button_theme=_sample_outlined_button_theme_data(),
        text_selection_theme=_sample_text_selection_theme_data(),
        data_table_theme=_sample_data_table_theme_data(),
        checkbox_theme=_sample_checkbox_theme_data(),
        radio_theme=_sample_radio_theme_data(),
        switch_theme=_sample_switch_theme_data(),
        progress_indicator_theme=_sample_progress_indicator_theme_data(),
        fix_text_field_outline_label=True,
        use_text_selection_theme=True,
    )


def _sample_theme_data__from():
    return ThemeData.from_(
        color_scheme=_sample_color_scheme(),
        text_theme=_sample_text_theme(),
    )


def _min_sample_theme_data__from():
    return ThemeData.from_(
        color_scheme=_sample_color_scheme(),
    )


def _sample_theme_data__light():
    return ThemeData.light(
    )


def _sample_theme_data__dark():
    return ThemeData.dark(
    )


def _sample_theme_data__fallback():
    return ThemeData.fallback(
    )


def _sample_scroll_behavior():
    return ScrollBehavior(
    )


def _sample_route_information():
    return RouteInformation(
        location='String 42',
        state=_sample_object(),
    )


def _min_sample_route_information():
    return RouteInformation(
    )


def _sample__callback_hook_provider():
    return _CallbackHookProvider(
    )


def _sample_material_app():
    return MaterialApp(
        key=_notfound_key(),
        navigator_key=_notfound_global_key(),
        scaffold_messenger_key=_notfound_global_key(),
        home=_sample_navigator(),
        routes={'String 42': _noop, 'String 43': _noop, 'String 44': _noop},
        initial_route='String 45',
        on_generate_route=_noop,
        on_generate_initial_routes=_noop,
        on_unknown_route=_noop,
        navigator_observers=[_sample_navigator_observer(), _sample_navigator_observer(), _sample_navigator_observer()],
        builder=_noop,
        title='String 46',
        on_generate_title=_noop,
        color=_sample_color(),
        theme=_sample_theme_data(),
        dark_theme=_sample_theme_data(),
        high_contrast_theme=_sample_theme_data(),
        high_contrast_dark_theme=_sample_theme_data(),
        theme_mode=ThemeMode.dark,
        locale=_sample_locale(),
        localizations_delegates=_notfound_iterable(),
        locale_list_resolution_callback=_noop,
        locale_resolution_callback=_noop,
        supported_locales=_notfound_iterable(),
        debug_show_material_grid=True,
        show_performance_overlay=True,
        checkerboard_raster_cache_images=True,
        checkerboard_offscreen_layers=True,
        show_semantics_debugger=True,
        debug_show_checked_mode_banner=True,
        shortcuts={_notfound_shortcut_activator(): _notfound_intent(), _notfound_shortcut_activator(): _notfound_intent(), _notfound_shortcut_activator(): _notfound_intent()},
        actions={_notfound_type(): _notfound_action(), _notfound_type(): _notfound_action(), _notfound_type(): _notfound_action()},
        restoration_scope_id='String 47',
        scroll_behavior=_sample_scroll_behavior(),
        use_inherited_media_query=True,
    )


def _min_sample_material_app():
    return MaterialApp(
    )


def _sample_material_app__router():
    return MaterialApp.router(
        route_information_parser=_notfound_route_information_parser(),
        router_delegate=_notfound_router_delegate(),
        key=_notfound_key(),
        scaffold_messenger_key=_notfound_global_key(),
        route_information_provider=_notfound_route_information_provider(),
        back_button_dispatcher=_notfound_back_button_dispatcher(),
        builder=_noop,
        title='String 42',
        on_generate_title=_noop,
        color=_sample_color(),
        theme=_sample_theme_data(),
        dark_theme=_sample_theme_data(),
        high_contrast_theme=_sample_theme_data(),
        high_contrast_dark_theme=_sample_theme_data(),
        theme_mode=ThemeMode.dark,
        locale=_sample_locale(),
        localizations_delegates=_notfound_iterable(),
        locale_list_resolution_callback=_noop,
        locale_resolution_callback=_noop,
        supported_locales=_notfound_iterable(),
        debug_show_material_grid=True,
        show_performance_overlay=True,
        checkerboard_raster_cache_images=True,
        checkerboard_offscreen_layers=True,
        show_semantics_debugger=True,
        debug_show_checked_mode_banner=True,
        shortcuts={_notfound_shortcut_activator(): _notfound_intent(), _notfound_shortcut_activator(): _notfound_intent(), _notfound_shortcut_activator(): _notfound_intent()},
        actions={_notfound_type(): _notfound_action(), _notfound_type(): _notfound_action(), _notfound_type(): _notfound_action()},
        restoration_scope_id='String 43',
        scroll_behavior=_sample_scroll_behavior(),
        use_inherited_media_query=True,
    )


def _min_sample_material_app__router():
    return MaterialApp.router(
        route_information_parser=_notfound_route_information_parser(),
        router_delegate=_notfound_router_delegate(),
    )


def _sample_physical_keyboard_key():
    return PhysicalKeyboardKey(
        usb_hid_usage=42,
    )


def _sample_logical_keyboard_key():
    return LogicalKeyboardKey(
        key_id=42,
    )


def _sample_focus_node():
    return FocusNode(
        debug_label='String 42',
        on_key=_noop,
        on_key_event=_noop,
        skip_traversal=True,
        can_request_focus=True,
        descendants_are_focusable=True,
    )


def _min_sample_focus_node():
    return FocusNode(
    )


def _sample_elevated_button():
    return ElevatedButton(
        key=_notfound_key(),
        on_pressed=_noop,
        on_long_press=_noop,
        style=_sample_button_style(),
        focus_node=_sample_focus_node(),
        autofocus=True,
        clip_behavior=Clip.anti_alias_with_save_layer,
        child=_sample_navigator(),
    )


def _min_sample_elevated_button():
    return ElevatedButton(
    )


def _sample_elevated_button__icon():
    return ElevatedButton.icon(
        icon=_sample_navigator(),
        label=_sample_navigator(),
        key=_notfound_key(),
        on_pressed=_noop,
        on_long_press=_noop,
        style=_sample_button_style(),
        focus_node=_sample_focus_node(),
        autofocus=True,
        clip_behavior=Clip.anti_alias_with_save_layer,
    )


def _min_sample_elevated_button__icon():
    return ElevatedButton.icon(
        icon=_sample_navigator(),
        label=_sample_navigator(),
    )

dump_list = [
    ('Object', _sample_object()),
    ('RouteSettings', _sample_route_settings()),
    ('RouteSettings.min', _min_sample_route_settings()),
    ('NavigatorObserver', _sample_navigator_observer()),
    ('Navigator', _sample_navigator()),
    ('Navigator.min', _min_sample_navigator()),
    ('NavigatorState', _sample_navigator_state()),
    ('ScaffoldMessenger', _sample_scaffold_messenger()),
    ('ScaffoldMessenger.min', _min_sample_scaffold_messenger()),
    ('ScaffoldMessengerState', _sample_scaffold_messenger_state()),
    ('Color', _sample_color()),
    ('Color_fromARGB', _sample_color__from_argb()),
    ('Color_fromRGBO', _sample_color__from_rgbo()),
    ('VisualDensity', _sample_visual_density()),
    ('VisualDensity.min', _min_sample_visual_density()),
    ('ColorSwatch', _sample_color_swatch()),
    ('MaterialColor', _sample_material_color()),
    ('ColorScheme', _sample_color_scheme()),
    ('ColorScheme_light', _sample_color_scheme__light()),
    ('ColorScheme_light.min', _min_sample_color_scheme__light()),
    ('ColorScheme_dark', _sample_color_scheme__dark()),
    ('ColorScheme_dark.min', _min_sample_color_scheme__dark()),
    ('ColorScheme_highContrastLight', _sample_color_scheme__high_contrast_light()),
    ('ColorScheme_highContrastLight.min', _min_sample_color_scheme__high_contrast_light()),
    ('ColorScheme_highContrastDark', _sample_color_scheme__high_contrast_dark()),
    ('ColorScheme_highContrastDark.min', _min_sample_color_scheme__high_contrast_dark()),
    ('ColorScheme_fromSwatch', _sample_color_scheme__from_swatch()),
    ('ColorScheme_fromSwatch.min', _min_sample_color_scheme__from_swatch()),
    ('ButtonThemeData', _sample_button_theme_data()),
    ('ButtonThemeData.min', _min_sample_button_theme_data()),
    ('Locale', _sample_locale()),
    ('Locale.min', _min_sample_locale()),
    ('Locale_fromSubtags', _sample_locale__from_subtags()),
    ('Locale_fromSubtags.min', _min_sample_locale__from_subtags()),
    ('Paint', _sample_paint()),
    ('Offset', _sample_offset()),
    ('Offset_fromDirection', _sample_offset__from_direction()),
    ('Offset_fromDirection.min', _min_sample_offset__from_direction()),
    ('Shadow', _sample_shadow()),
    ('Shadow.min', _min_sample_shadow()),
    ('FontFeature', _sample_font_feature()),
    ('FontFeature.min', _min_sample_font_feature()),
    ('FontFeature_enable', _sample_font_feature__enable()),
    ('FontFeature_disable', _sample_font_feature__disable()),
    ('FontFeature_alternative', _sample_font_feature__alternative()),
    ('FontFeature_alternativeFractions', _sample_font_feature__alternative_fractions()),
    ('FontFeature_contextualAlternates', _sample_font_feature__contextual_alternates()),
    ('FontFeature_caseSensitiveForms', _sample_font_feature__case_sensitive_forms()),
    ('FontFeature_characterVariant', _sample_font_feature__character_variant()),
    ('FontFeature_denominator', _sample_font_feature__denominator()),
    ('FontFeature_fractions', _sample_font_feature__fractions()),
    ('FontFeature_historicalForms', _sample_font_feature__historical_forms()),
    ('FontFeature_historicalLigatures', _sample_font_feature__historical_ligatures()),
    ('FontFeature_liningFigures', _sample_font_feature__lining_figures()),
    ('FontFeature_localeAware', _sample_font_feature__locale_aware()),
    ('FontFeature_localeAware.min', _min_sample_font_feature__locale_aware()),
    ('FontFeature_notationalForms', _sample_font_feature__notational_forms()),
    ('FontFeature_notationalForms.min', _min_sample_font_feature__notational_forms()),
    ('FontFeature_numerators', _sample_font_feature__numerators()),
    ('FontFeature_oldstyleFigures', _sample_font_feature__oldstyle_figures()),
    ('FontFeature_ordinalForms', _sample_font_feature__ordinal_forms()),
    ('FontFeature_proportionalFigures', _sample_font_feature__proportional_figures()),
    ('FontFeature_randomize', _sample_font_feature__randomize()),
    ('FontFeature_stylisticAlternates', _sample_font_feature__stylistic_alternates()),
    ('FontFeature_scientificInferiors', _sample_font_feature__scientific_inferiors()),
    ('FontFeature_stylisticSet', _sample_font_feature__stylistic_set()),
    ('FontFeature_subscripts', _sample_font_feature__subscripts()),
    ('FontFeature_superscripts', _sample_font_feature__superscripts()),
    ('FontFeature_swash', _sample_font_feature__swash()),
    ('FontFeature_swash.min', _min_sample_font_feature__swash()),
    ('FontFeature_tabularFigures', _sample_font_feature__tabular_figures()),
    ('FontFeature_slashedZero', _sample_font_feature__slashed_zero()),
    ('TextDecoration_combine', _sample_text_decoration__combine()),
    ('TextStyle', _sample_text_style()),
    ('TextStyle.min', _min_sample_text_style()),
    ('Size', _sample_size()),
    ('Size_copy', _sample_size__copy()),
    ('Size_square', _sample_size__square()),
    ('Size_fromWidth', _sample_size__from_width()),
    ('Size_fromHeight', _sample_size__from_height()),
    ('Size_fromRadius', _sample_size__from_radius()),
    ('BoxConstraints', _sample_box_constraints()),
    ('BoxConstraints.min', _min_sample_box_constraints()),
    ('BoxConstraints_tight', _sample_box_constraints__tight()),
    ('BoxConstraints_tightFor', _sample_box_constraints__tight_for()),
    ('BoxConstraints_tightFor.min', _min_sample_box_constraints__tight_for()),
    ('BoxConstraints_tightForFinite', _sample_box_constraints__tight_for_finite()),
    ('BoxConstraints_tightForFinite.min', _min_sample_box_constraints__tight_for_finite()),
    ('BoxConstraints_loose', _sample_box_constraints__loose()),
    ('BoxConstraints_expand', _sample_box_constraints__expand()),
    ('BoxConstraints_expand.min', _min_sample_box_constraints__expand()),
    ('Radius_circular', _sample_radius__circular()),
    ('Radius_elliptical', _sample_radius__elliptical()),
    ('BorderRadius_all', _sample_border_radius__all()),
    ('BorderRadius_circular', _sample_border_radius__circular()),
    ('BorderRadius_vertical', _sample_border_radius__vertical()),
    ('BorderRadius_vertical.min', _min_sample_border_radius__vertical()),
    ('BorderRadius_horizontal', _sample_border_radius__horizontal()),
    ('BorderRadius_horizontal.min', _min_sample_border_radius__horizontal()),
    ('BorderRadius_only', _sample_border_radius__only()),
    ('BorderRadius_only.min', _min_sample_border_radius__only()),
    ('ToggleButtonsThemeData', _sample_toggle_buttons_theme_data()),
    ('ToggleButtonsThemeData.min', _min_sample_toggle_buttons_theme_data()),
    ('TextTheme', _sample_text_theme()),
    ('TextTheme.min', _min_sample_text_theme()),
    ('BorderSide', _sample_border_side()),
    ('BorderSide.min', _min_sample_border_side()),
    ('InputDecorationTheme', _sample_input_decoration_theme()),
    ('InputDecorationTheme.min', _min_sample_input_decoration_theme()),
    ('IconThemeData', _sample_icon_theme_data()),
    ('IconThemeData.min', _min_sample_icon_theme_data()),
    ('IconThemeData_fallback', _sample_icon_theme_data__fallback()),
    ('RangeValues', _sample_range_values()),
    ('SliderThemeData', _sample_slider_theme_data()),
    ('SliderThemeData.min', _min_sample_slider_theme_data()),
    ('SliderThemeData_fromPrimaryColors', _sample_slider_theme_data__from_primary_colors()),
    ('TabBarTheme', _sample_tab_bar_theme()),
    ('TabBarTheme.min', _min_sample_tab_bar_theme()),
    ('Duration', _sample_duration()),
    ('Duration.min', _min_sample_duration()),
    ('TooltipThemeData', _sample_tooltip_theme_data()),
    ('TooltipThemeData.min', _min_sample_tooltip_theme_data()),
    ('CardTheme', _sample_card_theme()),
    ('CardTheme.min', _min_sample_card_theme()),
    ('ChipThemeData', _sample_chip_theme_data()),
    ('ChipThemeData.min', _min_sample_chip_theme_data()),
    ('ChipThemeData_fromDefaults', _sample_chip_theme_data__from_defaults()),
    ('ChipThemeData_fromDefaults.min', _min_sample_chip_theme_data__from_defaults()),
    ('PageTransitionsTheme', _sample_page_transitions_theme()),
    ('PageTransitionsTheme.min', _min_sample_page_transitions_theme()),
    ('SystemUiOverlayStyle', _sample_system_ui_overlay_style()),
    ('SystemUiOverlayStyle.min', _min_sample_system_ui_overlay_style()),
    ('AppBarTheme', _sample_app_bar_theme()),
    ('AppBarTheme.min', _min_sample_app_bar_theme()),
    ('ScrollbarThemeData', _sample_scrollbar_theme_data()),
    ('ScrollbarThemeData.min', _min_sample_scrollbar_theme_data()),
    ('BottomAppBarTheme', _sample_bottom_app_bar_theme()),
    ('BottomAppBarTheme.min', _min_sample_bottom_app_bar_theme()),
    ('DialogTheme', _sample_dialog_theme()),
    ('DialogTheme.min', _min_sample_dialog_theme()),
    ('FloatingActionButtonThemeData', _sample_floating_action_button_theme_data()),
    ('FloatingActionButtonThemeData.min', _min_sample_floating_action_button_theme_data()),
    ('NavigationRailThemeData', _sample_navigation_rail_theme_data()),
    ('NavigationRailThemeData.min', _min_sample_navigation_rail_theme_data()),
    ('Typography', _sample_typography()),
    ('Typography.min', _min_sample_typography()),
    ('Typography_material2014', _sample_typography__material2014()),
    ('Typography_material2014.min', _min_sample_typography__material2014()),
    ('Typography_material2018', _sample_typography__material2018()),
    ('Typography_material2018.min', _min_sample_typography__material2018()),
    ('CupertinoTextThemeData', _sample_cupertino_text_theme_data()),
    ('CupertinoTextThemeData.min', _min_sample_cupertino_text_theme_data()),
    ('NoDefaultCupertinoThemeData', _sample_no_default_cupertino_theme_data()),
    ('NoDefaultCupertinoThemeData.min', _min_sample_no_default_cupertino_theme_data()),
    ('SnackBarThemeData', _sample_snack_bar_theme_data()),
    ('SnackBarThemeData.min', _min_sample_snack_bar_theme_data()),
    ('BottomSheetThemeData', _sample_bottom_sheet_theme_data()),
    ('BottomSheetThemeData.min', _min_sample_bottom_sheet_theme_data()),
    ('PopupMenuThemeData', _sample_popup_menu_theme_data()),
    ('PopupMenuThemeData.min', _min_sample_popup_menu_theme_data()),
    ('MaterialBannerThemeData', _sample_material_banner_theme_data()),
    ('MaterialBannerThemeData.min', _min_sample_material_banner_theme_data()),
    ('DividerThemeData', _sample_divider_theme_data()),
    ('DividerThemeData.min', _min_sample_divider_theme_data()),
    ('ButtonBarThemeData', _sample_button_bar_theme_data()),
    ('ButtonBarThemeData.min', _min_sample_button_bar_theme_data()),
    ('BottomNavigationBarThemeData', _sample_bottom_navigation_bar_theme_data()),
    ('BottomNavigationBarThemeData.min', _min_sample_bottom_navigation_bar_theme_data()),
    ('TimePickerThemeData', _sample_time_picker_theme_data()),
    ('TimePickerThemeData.min', _min_sample_time_picker_theme_data()),
    ('ButtonStyle', _sample_button_style()),
    ('ButtonStyle.min', _min_sample_button_style()),
    ('TextButtonThemeData', _sample_text_button_theme_data()),
    ('TextButtonThemeData.min', _min_sample_text_button_theme_data()),
    ('ElevatedButtonThemeData', _sample_elevated_button_theme_data()),
    ('ElevatedButtonThemeData.min', _min_sample_elevated_button_theme_data()),
    ('OutlinedButtonThemeData', _sample_outlined_button_theme_data()),
    ('OutlinedButtonThemeData.min', _min_sample_outlined_button_theme_data()),
    ('TextSelectionThemeData', _sample_text_selection_theme_data()),
    ('TextSelectionThemeData.min', _min_sample_text_selection_theme_data()),
    ('DataTableThemeData', _sample_data_table_theme_data()),
    ('DataTableThemeData.min', _min_sample_data_table_theme_data()),
    ('CheckboxThemeData', _sample_checkbox_theme_data()),
    ('CheckboxThemeData.min', _min_sample_checkbox_theme_data()),
    ('RadioThemeData', _sample_radio_theme_data()),
    ('RadioThemeData.min', _min_sample_radio_theme_data()),
    ('SwitchThemeData', _sample_switch_theme_data()),
    ('SwitchThemeData.min', _min_sample_switch_theme_data()),
    ('ProgressIndicatorThemeData', _sample_progress_indicator_theme_data()),
    ('ProgressIndicatorThemeData.min', _min_sample_progress_indicator_theme_data()),
    ('ThemeData', _sample_theme_data()),
    ('ThemeData.min', _min_sample_theme_data()),
    ('ThemeData_raw', _sample_theme_data__raw()),
    ('ThemeData_raw.min', _min_sample_theme_data__raw()),
    ('ThemeData_from', _sample_theme_data__from()),
    ('ThemeData_from.min', _min_sample_theme_data__from()),
    ('ThemeData_light', _sample_theme_data__light()),
    ('ThemeData_dark', _sample_theme_data__dark()),
    ('ThemeData_fallback', _sample_theme_data__fallback()),
    ('ScrollBehavior', _sample_scroll_behavior()),
    ('RouteInformation', _sample_route_information()),
    ('RouteInformation.min', _min_sample_route_information()),
    ('_CallbackHookProvider', _sample__callback_hook_provider()),
    ('MaterialApp', _sample_material_app()),
    ('MaterialApp.min', _min_sample_material_app()),
    ('MaterialApp_router', _sample_material_app__router()),
    ('MaterialApp_router.min', _min_sample_material_app__router()),
    ('PhysicalKeyboardKey', _sample_physical_keyboard_key()),
    ('LogicalKeyboardKey', _sample_logical_keyboard_key()),
    ('FocusNode', _sample_focus_node()),
    ('FocusNode.min', _min_sample_focus_node()),
    ('ElevatedButton', _sample_elevated_button()),
    ('ElevatedButton.min', _min_sample_elevated_button()),
    ('ElevatedButton_icon', _sample_elevated_button__icon()),
    ('ElevatedButton_icon.min', _min_sample_elevated_button__icon()),
]
