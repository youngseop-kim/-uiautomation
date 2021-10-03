
from base import UIAutomationClient
from base import UIAutomationElementClass
from base import UIAutomationElementArrayClass

from base import ObjectResolverReference

class ObjectResolverReferenceForClass(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[UIAutomationElementClass.__name__] = \
            (UIAutomationElementClass, 'ObjectResolverForAutomationElement',)
        self[UIAutomationElementArrayClass.__name__] = \
            (UIAutomationElementArrayClass, 'ObjectResolverForAutomationElementArray',)

class ObjectResolverReferenceForPattern(ObjectResolverReference):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self['annotation'] = \
            (10023, UIAutomationClient.IUIAutomationAnnotationPattern,)
        self['custom_navigation'] = \
            (10033, UIAutomationClient.IUIAutomationCustomNavigationPattern,)
        self['dock'] = \
            (10011, UIAutomationClient.IUIAutomationDockPattern,)
        self['drag'] = \
            (10030, UIAutomationClient.IUIAutomationDragPattern,)
        self['drop_target'] = \
            (10031, UIAutomationClient.IUIAutomationDropTargetPattern,)
        self['expand_collapse'] = \
            (10005, UIAutomationClient.IUIAutomationExpandCollapsePattern,)
        self['grid_item'] = \
            (10007, UIAutomationClient.IUIAutomationGridItemPattern,)
        self['grid'] = \
            (10006, UIAutomationClient.IUIAutomationGridPattern,)
        self['invoke'] = \
            (10000, UIAutomationClient.IUIAutomationInvokePattern,)
        self['item_container'] = \
            (10019, UIAutomationClient.IUIAutomationItemContainerPattern,)
        self['legacy_iaccessible'] = \
            (10018, UIAutomationClient.IUIAutomationLegacyIAccessiblePattern,)
        self['multiple_view'] = \
            (10008, UIAutomationClient.IUIAutomationMultipleViewPattern,)
        self['object_model'] = \
            (10022, UIAutomationClient.IUIAutomationObjectModelPattern,)
        self['range_value'] = \
            (10003, UIAutomationClient.IUIAutomationRangeValuePattern,)
        self['scroll_item'] = \
            (10017, UIAutomationClient.IUIAutomationScrollItemPattern,)
        self['scroll'] = \
            (10004, UIAutomationClient.IUIAutomationScrollPattern,)
        self['selection_item'] = \
            (10010, UIAutomationClient.IUIAutomationSelectionItemPattern,)
        self['selection'] = \
            (10001, UIAutomationClient.IUIAutomationSelectionPattern,)
        self['spreadsheet'] = \
            (10026, UIAutomationClient.IUIAutomationSpreadsheetItemPattern,)
        self['spreadsheet_item'] = \
            (10027, UIAutomationClient.IUIAutomationSpreadsheetPattern,)
        self['styles'] = \
            (10025, UIAutomationClient.IUIAutomationStylesPattern,)
        self['synchronized_input'] = \
            (10021, UIAutomationClient.IUIAutomationSynchronizedInputPattern,)
        self['table_item'] = \
            (10013, UIAutomationClient.IUIAutomationTableItemPattern,)
        self['table'] = \
            (10012, UIAutomationClient.IUIAutomationTablePattern,)
        self['text_child'] = \
            (10029, UIAutomationClient.IUIAutomationTextChildPattern,)
        self['text_edit'] = \
            (10032, UIAutomationClient.IUIAutomationTextEditPattern,)
        self['text'] = \
            (10014, UIAutomationClient.IUIAutomationTextPattern,)
        self['text2'] = \
            (10024, UIAutomationClient.IUIAutomationTextPattern,)
        self['toggle'] = \
            (10015, UIAutomationClient.IUIAutomationTogglePattern,)
        self['transform'] = \
            (10016, UIAutomationClient.IUIAutomationTransformPattern,)
        self['transform2'] = \
            (10028, UIAutomationClient.IUIAutomationTransformPattern,)
        self['value'] = \
            (10002, UIAutomationClient.IUIAutomationValuePattern,)
        self['virtualized_item'] = \
            (10020, UIAutomationClient.IUIAutomationVirtualizedItemPattern,)
        self['window'] = \
            (10009, UIAutomationClient.IUIAutomationWindowPattern,)

class ObjectResolverReferenceForProperty(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # automation element property
        self['acceleratory_key'] = (30006, None,)
        self['access_key'] = (30007, None,)
        self['annotation_objects'] = (30156, None,)
        self['annotation_types'] = (30155, None,)
        self['aria_properties'] = (30102, None,)
        self['aria_role'] = (30101, None,)
        self['automation_id'] = (30011, None,)
        self['bounding_rectangle'] = (30001, None,)
        self['center_point'] = (30165, None,)
        self['class_name'] = (30012, None,)
        self['clickable_point'] = (30014, None,)
        self['controller_for'] = (30104, None,)
        self['control_type'] = (30003, None,)
        self['culture'] = (30015, None,)
        self['described_by'] = (30105, None,)
        self['fill_color'] = (30160, None,)
        self['fill_type'] = (30162, None,)
        self['flows_from'] = (30148, None,)
        self['flows_to'] = (30106, None,)
        self['framework_id'] = (30024, None,)
        self['full_description'] = (30159, None,)
        self['has_keyboard_focus'] = (30008, None,)
        self['heading_level'] = (30173, None,)
        self['help_text'] = (30013, None,)
        self['is_content_element'] = (30017, None,)
        self['is_control_element'] = (30016, None,)
        self['is_data_valid_for_form'] = (30103, None,)
        self['is_dialog'] = (30174, None,)
        self['is_enabled'] = (30010, None,)
        self['is_keyboard_focusable'] = (30009, None,)
        self['is_offscreen'] = (30022, None,)
        self['is_password'] = (30019, None,)
        self['is_peripheral'] = (30150, None,)
        self['is_required_for_form'] = (30025, None,)
        self['item_status'] = (30026, None,)
        self['item_type'] = (30021, None,)
        self['labeled_by'] = (30018, None,)
        self['landmark_type'] = (30157, None,)
        self['level'] = (30154, None,)
        self['live_setting'] = (30135, None,)
        self['localized_control_type'] = (30004, None,)
        self['localized_landmark_type'] = (30158, None,)
        self['name'] = (30005, None,)
        self['native_window_handle'] = (30020, None,)
        self['optimize_for_visual_content'] = (30111, None,)
        self['orientation'] = (30023, None,)
        self['outline_color'] = (30161, None,)
        self['outline_thickness'] = (30164, None,)
        self['position_in_set'] = (30152, None,)
        self['process_id'] = (30002, None,)
        self['provider_description'] = (30107, None,)
        self['rotation'] = (30166, None,)
        self['runtime_id'] = (30000, None,)
        self['size'] = (30167, None,)
        self['size_of_set'] = (30153, None,)
        self['visual_effects'] = (30163, None,)

        # control pattern property
        self['annotation_annotation_type_id'] = (30113, None,)
        self['annotation_annotation_type_name'] = (30114, None,)
        self['annotation_author'] = (30115, None,)
        self['annotation_date_time'] = (30116, None,)
        self['annotation_target'] = (30117, None,)
        self['dock_dock_position'] = (30069, None,)
        self['drag_drop_effect'] = (30139, None,)
        self['drag_drop_effects'] = (30140, None,)
        self['drag_is_grabbed'] = (30138, None,)
        self['drag_grabbed_items'] = (30144, None,)
        self['drop_target_drop_target_effect'] = (30142, None,)
        self['drop_target_drop_target_effects'] = (30143, None,)
        self['expand_collapse_expand_collapse_state'] = (30070, None,)
        self['grid_column_count'] = (30063, None,)
        self['grid_item_column'] = (30065, None,)
        self['grid_item_column_span'] = (30067, None,)
        self['grid_item_containing_grid'] = (30068, None,)
        self['grid_item_row'] = (30064, None,)
        self['grid_item_row_span'] = (30066, None,)
        self['grid_row_count'] = (30062, None,)
        self['legacy_iaccessible_child_id'] = (30091, None,)
        self['legacy_iaccessible_default_action'] = (30100, None,)
        self['legacy_iaccessible_description'] = (30094, None,)
        self['legacy_iaccessible_help'] = (30097, None,)
        self['legacy_iaccessible_keyboard_shortcut'] = (30098, None,)
        self['legacy_iaccessible_name'] = (30092, None,)
        self['legacy_iaccessible_role'] = (30095, None,)
        self['legacy_iaccessible_selection'] = (30099, None,)
        self['legacy_iaccessible_state'] = (30096, None,)
        self['legacy_iaccessible_value'] = (30093, None,)
        self['multiple_view_current_view'] = (30071, None,)
        self['multiple_view_supported_view'] = (30072, None,)
        self['range_value_is_read_only'] = (30048, None,)
        self['range_value_large_change'] = (30051, None,)
        self['range_value_maximum'] = (30050, None,)
        self['range_value_minimum'] = (30049, None,)
        self['range_value_small_change'] = (30052, None,)
        self['range_value_value'] = (30047, None,)
        self['scroll_horizontally_scrollable'] = (30057, None,)
        self['scroll_horizontal_scroll_percent'] = (30053, None,)
        self['scroll_horizontal_view_size'] = (30054, None,)
        self['scroll_vertically_scrollable'] = (30058, None,)
        self['scroll_vertical_scroll_percent'] = (30055, None,)
        self['scroll_vertical_view_size'] = (30056, None,)
        self['selection_can_select_multiple'] = (30060, None,)
        self['selection_is_selection_required'] = (30061, None,)
        self['selection_selection'] = (30059, None,)
        self['selection_item_is_selected'] = (30079, None,)
        self['selection_item_selection_container'] = (30080, None,)
        self['spreadsheet_item_formula'] = (30129, None,)
        self['spreadsheet_item_annotation_objects'] = (30130, None,)
        self['spreadsheet_item_annotation_types'] = (30131, None,)
        self['styles_extended_properties'] = (30126, None,)
        self['styles_fill_color'] = (30122, None,)
        self['styles_fill_pattern_color'] = (30125, None,)
        self['styles_fill_pattern_style'] = (30123, None,)
        self['styles_shape'] = (30124, None,)
        self['styles_style_id'] = (30120, None,)
        self['styles_style_name'] = (30121, None,)
        self['table_column_headers'] = (30082, None,)
        self['table_item_column_header_items'] = (30085, None,)
        self['table_row_headers'] = (30081, None,)
        self['table_row_or_column_major'] = (30083, None,)
        self['table_item_row_header_items'] = (30084, None,)
        self['toggle_toggle_state'] = (30086, None,)
        self['transform_can_move'] = (30087, None,)
        self['transform_can_resize'] = (30088, None,)
        self['transform_can_rotate'] = (30089, None,)
        self['transform2_can_zoom'] = (30133, None,)
        self['transform2_zoom_level'] = (30145, None,)
        self['transform2_zoom_maximum'] = (30147, None,)
        self['transform2_zoom_minimum'] = (30146, None,)
        self['value_is_read_only'] = (30046, None,)
        self['value_value'] = (30045, None,)
        self['window_can_maximize'] = (30073, None,)
        self['window_can_minimize'] = (30074, None,)
        self['window_is_modal'] = (30077, None,)
        self['window_is_topmost'] = (30078, None,)
        self['window_window_interaction_state'] = (30076, None,)
        self['window_window_visual_state'] = (30075, None,)

        # control pattern availabiity property
        self['is_annotation_pattern_available'] = (30118, None,)
        self['is_custom_navigation_pattern_available'] = (30151, None,)
        self['is_dock_pattern_available'] = (30027, None,)
        self['is_drag_pattern_available'] = (30137, None,)
        self['is_drop_target_pattern_available'] = (30141, None,)
        self['is_expand_collapse_pattern_available'] = (30028, None,)
        self['is_grid_item_pattern_available'] = (30029, None,)
        self['is_grid_pattern_available'] = (30030, None,)
        self['is_invoke_pattern_available'] = (30031, None,)
        self['is_item_container_pattern_available'] = (30108, None,)
        self['is_legacy_iaccessible_pattern_available'] = (30090, None,)
        self['is_multiple_view_pattern_available'] = (30032, None,)
        self['is_object_model_pattern_available'] = (30112, None,)
        self['is_range_value_pattern_available'] = (30033, None,)
        self['is_scroll_item_pattern_available'] = (30035, None,)
        self['is_scroll_pattern_available'] = (30034, None,)
        self['is_selection_item_pattern_available'] = (30036, None,)
        self['is_selection_pattern_available'] = (30037, None,)
        self['is_spreadsheet_pattern_available'] = (30128, None,)
        self['is_spreadsheet_item_pattern_available'] = (30132, None,)
        self['is_styles_pattern_available'] = (30127, None,)
        self['is_synchronized_input_pattern_available'] = (30110, None,)
        self['is_table_item_pattern_available'] = (30039, None,)
        self['is_table_pattern_available'] = (30038, None,)
        self['is_text_child_pattern_available'] = (30136, None,)
        self['is_text_edit_pattern_available'] = (30149, None,)
        self['is_text_pattern_available'] = (30040, None,)
        self['is_text_pattern_2_available'] = (30119, None,)
        self['is_toggle_pattern_available'] = (30041, None,)
        self['is_transform_pattern_available'] = (30042, None,)
        self['is_transform_pattern_2_available'] = (30134, None,)
        self['is_value_pattern_available'] = (30043, None,)
        self['is_virtualized_item_pattern_available'] = (30109, None,)
        self['is_window_pattern_available'] = (30044, None,)

class ObjectResolverReferenceForAnnotationAnnotationTypeId(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[60020] = 'advanced_proofing_issue'
        self[60019] = 'author'
        self[60022] = 'circular_reference_error'
        self[60003] = 'comment'
        self[60018] = 'conflicting_change'
        self[60021] = 'data_validation_error'
        self[60012] = 'deletion_change'
        self[60016] = 'editing_locked_changed'
        self[60009] = 'endnote'
        self[60017] = 'external_change'
        self[60007] = 'footer'
        self[60010] = 'footnote'
        self[60014] = 'format_change'
        self[60004] = 'formular_error'
        self[60002] = 'grammar_error'
        self[60006] = 'header'
        self[60008] = 'highlighted'
        self[60011] = 'insertion_change'
        self[60023] = 'mathematics'
        self[60013] = 'move_change'
        self[60001] = 'spelling_error'
        self[60005] = 'track_changes'
        self[60000] = 'unknown'
        self[60015] = 'unsynced_change'

class ObjectResolverReferenceForLegacyIAccessibleRole(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                
        self[10] = 'client'
        self[54] = 'animation'
        self[14] = 'application'
        self[19] = 'border'
        self[56] = 'button_drop_down'
        self[58] = 'button_drop_down_grid'
        self[57] = 'button_menu'
        self[7] = 'caret'
        self[29] = 'cell'
        self[32] = 'character'
        self[17] = 'chart'
        self[44] = 'check_button'
        self[61] = 'clock'
        self[27] = 'column'
        self[25] = 'column_header'
        self[46] = 'combo_box'
        self[6] = 'cursor'
        self[-1] = 'default'
        self[53] = 'diagram'
        self[49] = 'dial'
        self[18] = 'dialog'
        self[15] = 'document'
        self[47] = 'drop_list'
        self[55] = 'equation'
        self[40] = 'graphic'
        self[4] = 'grip'
        self[20] = 'grouping'
        self[31] = 'help_balloon'
        self[50] = 'hotkey_field'
        self[39] = 'indicator'
        self[63] = 'ip_address'
        self[30] = 'link'
        self[33] = 'list'
        self[34] = 'list_item'
        self[2] = 'menu_bar'
        self[12] = 'menu_item'
        self[11] = 'menu_popup'
        self[0] = 'none'
        self[35] = 'outline'
        self[64] = 'outline_button'
        self[36] = 'outline_item'
        self[37] = 'page_tab'
        self[60] = 'page_tab_list'
        self[16] = 'pane'
        self[48] = 'progress_bar'
        self[38] = 'property_page'
        self[43] = 'push_button'
        self[45] = 'radio_button'
        self[28] = 'row'
        self[26] = 'row_header'
        self[3] = 'scroll_bar'
        self[21] = 'separator'
        self[51] = 'slider'
        self[5] = 'sound'
        self[52] = 'spin_button'
        self[62] = 'split_button'
        self[41] = 'static_text'
        self[23] = 'status_bar'
        self[24] = 'table'
        self[42] = 'text'
        self[1] = 'title_bar'
        self[22] = 'tool_bar'
        self[13] = 'tool_tip'
        self[59] = 'white_space'
        self[9] = 'window'

class ObjectResolverReferenceForControlType(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[50040] = 'app_bar'
        self[50000] = 'button'
        self[50001] = 'calendar'
        self[50002] = 'check_box'
        self[50003] = 'combo_box'
        self[50025] = 'custom'
        self[50028] = 'data_grid'
        self[50029] = 'data_item'
        self[50030] = 'document'
        self[50004] = 'edit'
        self[50026] = 'group'
        self[50034] = 'header'
        self[50035] = 'header_item'
        self[50005] = 'hyperlink'
        self[50006] = 'image'
        self[50008] = 'list'
        self[50007] = 'list_item'
        self[50010] = 'menu_bar'
        self[50009] = 'menu'
        self[50011] = 'menu_item'
        self[50033] = 'pane'
        self[50012] = 'progress_bar'
        self[50013] = 'radio_button'
        self[50014] = 'scroll_bar'
        self[50039] = 'semantic_zoom'
        self[50038] = 'separator'
        self[50015] = 'slider'
        self[50016] = 'spinner'
        self[50031] = 'split_button'
        self[50017] = 'status_bar'
        self[50018] = 'tab'
        self[50019] = 'tab_item'
        self[50036] = 'table'
        self[50020] = 'text'
        self[50027] = 'thumb'
        self[50037] = 'title_bar'
        self[50021] = 'tool_bar'
        self[50022] = 'tool_tip'
        self[50023] = 'tree'
        self[50024] = 'tree_item'
        self[50032] = 'window'

class ObjectResolverReferenceForToggleToggleState(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[0] = 'off'
        self[1] = 'on'
        self[2] = 'indeterminate'

class ObjectResolverReferenceForWindowWindowVisualState(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[0] = 'running'
        self[1] = 'closing'
        self[2] = 'ready_for_user_interaction'
        self[3] = 'blocked_by_modal_window'
        self[4] = 'not_responding'

class ObjectResolverReferenceForWindowWindowInteractionState(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[0] = 'normal'
        self[1] = 'maximized'
        self[2] = 'minimized'

class ObjectResolverReferenceForVisualEffects(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[0] = 'none'
        self[1] = 'shadow'
        self[2] = 'reflection'
        self[3] = 'glow'
        self[4] = 'soft_edges'
        self[5] = 'bevel'
        
class ObjectResolverReferenceForDockDockPosition(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[0] = 'top'
        self[1] = 'left'
        self[2] = 'bottom'
        self[3] = 'right'
        self[4] = 'fill'
        self[5] = 'none'
        
class ObjectResolverReferenceForExpandCollapseExpandCollapseState(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[0] = 'collapsed'
        self[1] = 'expanded'
        self[2] = 'partially_expanded'
        self[3] = 'leaf_node'
        
class ObjectResolverReferenceForFillType(ObjectResolverReference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self[0] = 'none'
        self[1] = 'color'
        self[2] = 'gradient'
        self[3] = 'picture'
        self[4] = 'pattern'
