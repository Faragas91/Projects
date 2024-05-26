extends RigidBody2D

<<<<<<< HEAD
var force = 1000
	
func _physics_process(delta):
	if Input.is_action_pressed("move_right"):
		apply_force(Vector2(force,0))
	if Input.is_action_pressed("move_left"):
		apply_force(Vector2(-force,0))
	if Input.is_action_pressed("move_up"):
		apply_force(Vector2(0,-force))
	if Input.is_action_pressed("move_down"):
		apply_force(Vector2(0,force))
=======
func _ready():
	apply_impulse(Vector2(95, 5))
>>>>>>> 21528e722ee42941e32e014fabfbecb9f452e6a1
	
