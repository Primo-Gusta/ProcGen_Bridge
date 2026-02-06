@tool
extends EditorPlugin

var dock

func _enter_tree() -> void:
	dock = preload("res://addons/procgen_bridge/dock_panel.tscn").instantiate()
	add_control_to_dock(DOCK_SLOT_RIGHT_BL, dock)
