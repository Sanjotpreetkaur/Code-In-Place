from graphics import Canvas
import random
"""
code takes in a string, a word. or it is defined
it check the strings present and used respective functions and display them
make a dictionary of the functions and assign each function to a list. 
"""
# constants   
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
# difference between 2 lines in the coordinate system 
PLANE_SPACE = 15
# centre of the canvas axis
CENTRE_WIDTH = CANVAS_WIDTH/2
CENTRE_HEIGHT = CANVAS_HEIGHT/2
# Check if width is actually required
BREADTH = PLANE_SPACE
WIDTH = 2*PLANE_SPACE
HEIGHT = 3*PLANE_SPACE

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    functions = dict_letters()
    
    #coordinate_plane(canvas, PLANE_SPACE)
    word = "CODING CORNER SECTION"
    
    # number of characters in one line and no of lines
    num_charac, num_line = words_specifics(word)
    print(num_charac, num_line)
    # number of spaces occupied by letter for example, "HI" has 2
    num_space = (num_charac/num_line)
    #starting coordinates of first alphabet/word such that it is centered on the canvas
    START_X = (CENTRE_WIDTH-int((1/2)*(6*4.5)*PLANE_SPACE))
    START_Y = (CENTRE_HEIGHT-int((1/2)*(3*5)*PLANE_SPACE))
    """
    takes in a word and prints the word
    """
    
    x1 = START_X
    y1 = START_Y
    for i in word:
        color = random_color()
        if i != " ":
            obj = functions[i](canvas, x1, y1, color)
            x1 = update_x(canvas, obj)
        else:
            y1 = update_y(canvas, obj)
            x1 = START_X
            
def words_specifics(word):
    charac_len = 0
    line_len = 1
    for i in word:
        if i !=" ":
            charac_len += 1
        else:
            line_len += 1
    return charac_len, line_len

def dict_letters():
    dict_letters = {}
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dict_letters[i] = globals()["letter_"+ i]
    return dict_letters

def random_color():
    color_list =["#e8c237", "#f46387", "#9400F4", "#abc76e", "#e4292e", "#c24244", "DodgerBlue", "#7c1033", "#04e057", "#4fd399", "#a6b115", "#5e22e2", "#ab4911", "#ad465c", "#ebde33", "#5b83fd", "#5b75cf", "#fe33d9", "#eeb816", "#de27e5"]
    return random.choice(color_list)

def coordinate_plane(canvas, SPACE):
    # GRID to see coordinates. it is proportional. 
    for i in range(0, int(CANVAS_WIDTH/SPACE)):
        h_line = canvas.create_line(0, i*SPACE, CANVAS_WIDTH, i*SPACE)
        v_line = canvas.create_line(i*SPACE, 0, i*SPACE, CANVAS_HEIGHT)

def update_x(canvas, prev_obj):
    left_x = canvas.get_left_x(prev_obj)
    new_x = left_x + 4*PLANE_SPACE
    return new_x

def update_y(canvas, prev_obj):
    top_y = canvas.get_top_y(prev_obj)
    new_y = top_y + 4*PLANE_SPACE
    return new_y

def vertical_rec(canvas, x1, y1, color, x2 = BREADTH, y2 = HEIGHT):
    # one long rectangle with 3*PLANE_SPACE length in the letter I
    # return object id so that it can be picked up in updating the coordinates
    obj_id = canvas.create_rectangle(x1, y1, x1 + x2, y1 + y2, color)
    return obj_id

def horiz_rec(canvas, x1, y1, color, x2 = HEIGHT, y2 = BREADTH):
    # one long horizontal rectangle with 3*PLANE SPACE LENGTH
    # return object id so that it can be picked up in updating the coordinates
    obj_id = canvas.create_rectangle(x1, y1, x1+x2, y1+y2, color)
    return obj_id
def right_angular(canvas, x1, y1, color, x2 = HEIGHT, y2 = HEIGHT):
    obj_id = canvas.create_polygon(
        x1, y1,
        x1+BREADTH, y1,
        x1+x2, y1+y2, 
        x1+x2-BREADTH, y1+y2,
        color = color
    )
    return obj_id
def loop(canvas, x1, y1, x2, y2, gap, color):
    #the loops in D, R, P, B
    
    canvas.create_oval(
        x1, y1, x2, y2, color
    )
    canvas.create_oval(
        x1+ gap, y1+gap, x2-gap, y2 - gap, "white"
    )
    top_obj = canvas.create_rectangle(x1, y1, x1+ BREADTH*1.2, y1+ HEIGHT, color)
    return top_obj

def letter_S(canvas, x1, y1, color):
    # three hor, two half verticals
    top_obj = horiz_rec(canvas, x1, y1, color, y2=BREADTH*0.7)
    horiz_rec(canvas, x1, y1+BREADTH*1.2, color, y2=BREADTH*0.7)
    horiz_rec(canvas, x1, y1+WIDTH*1.2, color, y2=BREADTH*0.6)
    vertical_rec(canvas, x1, y1, color, y2=BREADTH*1.2)
    vertical_rec(canvas, x1+WIDTH, y1+BREADTH*1.2, color, y2=BREADTH*1.8)
    return top_obj

def letter_T(canvas, x1, y1, color):
    # one hor, one vertical
    top_obj = horiz_rec(canvas, x1, y1, color)
    vertical_rec(canvas, x1+BREADTH, y1, color)
    return top_obj

def letter_G(canvas, x1, y1, color):
    # one vertical, two hor, one half ver, one half hor
    top_obj = vertical_rec(canvas, x1, y1, color)
    horiz_rec(canvas, x1, y1, color, y2=BREADTH*0.7)
    horiz_rec(canvas, x1, y1+WIDTH*1.3, color, y2 = BREADTH*0.4)
    vertical_rec(canvas, x1 + WIDTH*1.1, y1 + BREADTH, color, x2=BREADTH*0.8, y2=WIDTH)
    horiz_rec(canvas, x1 + BREADTH*1.5, y1+BREADTH, color, x2 = BREADTH, y2=BREADTH*0.5 )
    return top_obj
def letter_R(canvas, x1, y1, color):
    # one loop, one angular
    # top_obj = loop(canvas, x1, y1, x1+HEIGHT, y1+ BREADTH*1.5, color)
    
    right_angular(canvas, x1, y1+BREADTH*1, color, y2 = BREADTH*2)
    top_obj = letter_P(canvas, x1, y1, color)
    return top_obj

def letter_N(canvas, x1, y1, color):
    top_obj = vertical_rec(canvas, x1, y1, color)
    right_angular(canvas, x1, y1, color)
    vertical_rec(canvas, x1+WIDTH, y1, color)
    return top_obj

def letter_O(canvas, x1, y1, color):
    top_obj = canvas.create_oval(
        x1, y1, 
        x1+HEIGHT, y1+HEIGHT, color
    )
    diff = (BREADTH/1.2)
    canvas.create_oval(
        x1+diff, y1+diff, 
        x1+HEIGHT-diff, y1+HEIGHT-diff, "white"
    )
    return top_obj

def letter_B(canvas, x1, y1, color):
    # two loops
    bottom_loop = loop(canvas, x1, y1 + BREADTH*1.5, x1 + HEIGHT, y1 + HEIGHT, BREADTH*0.5, color)
    canvas.delete(bottom_loop)
    top_obj = loop(canvas, x1, y1, x1 + HEIGHT, y1 + BREADTH*1.5, BREADTH*0.5, color)  
    return top_obj

def letter_D(canvas, x1, y1, color):
    # one vertical of varied thickness, one O
    top_obj = loop(canvas, x1, y1, x1 + HEIGHT, y1 + HEIGHT, BREADTH*0.5, color)
    return top_obj
    
def letter_P(canvas, x1, y1, color):
    top_obj = loop(canvas, x1, y1, x1 + HEIGHT, y1 + WIDTH, BREADTH*0.5, color)
    return top_obj

def letter_E(canvas, x1, y1, color):
    # three horrizontal, one vertical
    top_obj = vertical_rec(canvas, x1, y1, color)
    horiz_rec(canvas, x1, y1, color, y2 = BREADTH*0.6)
    horiz_rec(canvas, x1, y1+BREADTH, color, y2= BREADTH*0.8)
    horiz_rec(canvas, x1, y1+BREADTH*2.2,color, y2=0.8*BREADTH)
    return top_obj

def letter_L(canvas, x1, y1, color):
    top_obj = vertical_rec(canvas, x1, y1, color)
    horiz_rec(canvas, x1, y1+BREADTH*2.2,color, y2=0.8*BREADTH)
    return top_obj

def letter_F(canvas, x1, y1, color):
    top_obj = vertical_rec(canvas, x1, y1, color)
    horiz_rec(canvas, x1, y1, color, y2 = BREADTH*0.6)
    horiz_rec(canvas, x1, y1+BREADTH, color, y2= BREADTH*0.8)
    
    return top_obj

def letter_I(canvas, x1, y1, color):
    # one long rectangle, two hor rectangles (for consistency)
    vertical_rec(canvas, x1+BREADTH, y1, color)
    top_obj = horiz_rec(canvas, x1, y1, color)
    horiz_rec(canvas, x1, y1+WIDTH, color)
    return top_obj

def letter_H(canvas, x1, y1, color):
    # two long rectangles, one horizontal. 
    top_obj = vertical_rec(canvas, x1, y1, color)
    horiz_rec(canvas, x1, y1+BREADTH, color)
    vertical_rec(canvas, x1+WIDTH, y1, color)
    return top_obj


def letter_C(canvas, x1, y1, color):
    # two horizontal, one ver
    top_obj = horiz_rec(canvas, x1, y1, color)
    vertical_rec(canvas, x1, y1, color)
    horiz_rec(canvas, x1, y1+WIDTH, color)
    return top_obj

if __name__ == '__main__':
    main()