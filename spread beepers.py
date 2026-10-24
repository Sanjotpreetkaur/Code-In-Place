from karel.stanfordkarel import *

def main():

    """
    # pre: there are a bunch of beepers on second column
    # post: the beepers are spread out. 
    what we can see?
    1. the beeper spread/line starts at the second column,
        right where our beepers were
    2. karel's position
    3. beepers will NEVER spread out to the farthest corner
    4. infinite beepers in the bag -> the bag will never be empty

    how to spread out the beepers?
    how does karel know where to put a beeper?
    0. karel at the first column, facing east
    1. move to pile, pick a beeper
    2. move and stop one step after the beepers are present
    3. put a beeper
    4. move back to wall and reposition to 0.
    5. repeat 1. 2. 3. 4. 5.
    - how long to repeat this? we dont know
    - how to stop this loop? reduce the pile to 0

    """
    move()
    while beepers_present():
        pick_beeper()
        if beepers_present():
            detect_beeper()
            put_beeper()
            return_to_wall()
            move()
    put_beeper()
    return_to_wall()

def return_to_wall():
    #pre: karel is at some posiiton on the line facing west
    #post: karel returned to the wall facing west
    turn_back()
    while front_is_clear():
        move()
    turn_back()
def detect_beeper():
    #pre: start of beeper line
    #post: one step after the end of beeper line
    #moves till a beeper is found
    while beepers_present():
        move()

def step_back():
    #pre: Karel along the line somewhere
    #post: Karel ends on the pile!!!
    turn_back()
    move()
    turn_back()


def turn_back():
    #faces back
    turn_left()
    turn_left()

def turn_right():
    #faces right
    turn_left()
    turn_left()
    turn_left()
if __name__ == '__main__':
    main()