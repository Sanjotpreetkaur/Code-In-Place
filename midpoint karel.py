from karel.stanfordkarel import *

def main():
    """
    Things to remember:
    1. Karel cannot count
    2. Karel's world is always square.
    3. if odd, in centre
    4. if even, in left of two centres
    """
    """
    how to proceed:
    1. place beepers on line
    2. pick last beeper
    3. return to c1
    4. pick beeper
    5. return l and take a step back
    6. pick beeper
    7. return to c1, take one step forward
    8. pick beeper
    9. return to l and take 2 step forward
    10 repeat till no beepers left
    """
    place_beepers()
    step_back()
    end_of_beepers()
    turn_around()
    move()
    while beepers_present():

        end_of_beepers()
        step_back()
        if beepers_present():
            pick_beeper()
            move()
    step_back()
    put_beeper()
    if left_is_blocked():
        turn_around()

def end_of_beepers():
    while beepers_present():
        if front_is_clear():
            move()
        else:
            pick_beeper()
            
def place_beepers():
    while front_is_clear():
        put_beeper()
        move()

def step_back():
    turn_around()
    move()

def turn_around():
    turn_left()
    turn_left()
    
if __name__ == '__main__':
    main()