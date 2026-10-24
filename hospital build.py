from karel.stanfordkarel import *

def main():
    #pre : Karel is in first column, first row  
    #post: Karel is at last column, first row
    #what does this mean? karel has moved!
    #Karel has build hospitals along the way
    while front_is_clear():
        move()
        if beepers_present():
            build_hospital()
            
def build_hospital():
    pick_beeper()
    turn_left()
    column()
    turn_right()
    move()
    turn_right()
    column()
    turn_left()
    
def column():
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()