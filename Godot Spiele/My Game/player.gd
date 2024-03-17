extends CharacterBody2D

const SPEED = 100.0
const ALLEC = 2.0

var input: Vector2
var bla: Vector2

func get_input() -> Vector2:
	input = Vector2.ZERO
	var horizontal = false
	var vertical = false

	if Input.get_action_strength("move_right") and vertical == false:
		input.x += 1.0
		horizontal = true
		
	if Input.get_action_strength("move_left") and vertical == false:
		input.x -= 1.0
		horizontal = true
		
	if Input.get_action_strength("move_down") and horizontal == false:
		input.y += 1.0
		vertical = true
		
	if Input.get_action_strength("move_up") and horizontal == false :
		input.y -= 1.0
		vertical = true
	
	return input.normalized()

func _process(delta: float) -> void:
	var playerInput: Vector2 = get_input()
	
	velocity = playerInput * SPEED
	
	move_and_slide()


