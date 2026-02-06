@tool
extends Control
var http_client: HTTPRequest
var target_layer: TileMapLayer

@onready var width: SpinBox = $MainBox/ConfigBox/ConfigValues/SpinBox
@onready var height: SpinBox = $MainBox/ConfigBox/ConfigValues/SpinBox2
@onready var smoothness: SpinBox = $MainBox/ConfigBox/ConfigValues/SpinBox3
@onready var seed: SpinBox = $MainBox/ConfigBox/ConfigValues/SpinBox4

func _ready():
	if not http_client:
		http_client = HTTPRequest.new()
		add_child(http_client)
		http_client.request_completed.connect(_on_request_completed)

func _on_button_pressed() -> void:
	var selection = EditorInterface.get_selection().get_selected_nodes()
	
	if selection.is_empty() or not selection[0] is TileMapLayer:
		printerr("Erro: Selecione um TileMapLayer na árvore de cenas!")
		return
	
	target_layer = selection[0]
	if not target_layer.tile_set:
		printerr("Erro: O TileMapLayer selecionado não tem um TileSet configurado!")
		return

	send_api_call()

func send_api_call():
	var url = "http://127.0.0.1:8000/generate?width=%d&height=%d&seed=%d&smoothness=%d" % [
		width.value, height.value, seed.value, smoothness.value
	]
	
	print("Chamando API: ", url)
	var error = http_client.request(url)
	if error != OK:
		printerr("Erro ao iniciar request: ", error)

func _on_request_completed(_result, response_code, _headers, body):
	print("Resposta da API: ", response_code)
	if response_code != 200: return

	var json = JSON.parse_string(body.get_string_from_utf8())
	if json and json.has("map"):
		draw_in_editor(json["map"])

func draw_in_editor(map_data: Array):
	target_layer.clear()
	
	for y in range(map_data.size()):
		for x in range(map_data[y].size()):
			var val = map_data[y][x]
			var atlas_coords = Vector2i(1, 0) if val == 1 else Vector2i(0, 0)
			target_layer.set_cell(Vector2i(x, y), 0, atlas_coords)
	
	target_layer.notify_property_list_changed()
	target_layer.queue_redraw()
	
	print("Sucesso! Mapa desenhado no Editor.")
