def turn_right():
       turn_left()
       turn_left()
       turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()    
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else: 
        move()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
