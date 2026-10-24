from karel.stanfordkarel import *

def main():

    while right_is_blocked():
        build_column()
        if front_is_clear():
            move_to_top()
            move_to_pillar()
            move_to_bottom()
        else:
            turn_right()
    turn_left()
    
def move_to_bottom():
    turn_right()
    move_to_wall()
    turn_left()
    
def move_to_top():
    turn_left()
    move_to_wall()
    turn_right()

def move_to_pillar():
    if front_is_clear():
        move()
    while left_is_clear():
        move()

def build_column():
    turn_left()
    spread_beepers()
    turn_around()
    move_to_wall()
    turn_left()
    
def spread_beepers():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    
def move_to_wall():
    while front_is_clear():
        move()
        
def turn_right():
    for i in range(3):
        turn_left()
        
def turn_around():
    turn_left()
    turn_left()
    
if __name__ == '__main__':
    main()