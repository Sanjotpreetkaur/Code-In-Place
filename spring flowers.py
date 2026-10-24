from karel.stanfordkarel import *

def main():
    """
    Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
    Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
    """
    while front_is_clear():
        find_stem()
        climb_stem()
        flower_making()      
        descend_stem()
        
def flower_making():
    if front_is_clear():
        flower()
    else:
        turn_left()
        turn_left()
        
def find_stem():
    move_to_wall()
    
def climb_stem():
    turn_left()
    while right_is_blocked() and front_is_clear():
        move()
        
def flower():
    put_beeper()
    petal()
    turn_right()
    petal()
    turn_right()
    petal()

def petal():
    move()
    put_beeper()
    
def descend_stem():
    move()
    move_to_wall()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_to_wall():
    while front_is_clear():
        move()

if __name__ == '__main__':
    main()