# implementation of card game - Memory

import simplegui
import random

# initialize global variables

# randomly creates the deck of cards
deck_a = range(8)
deck_b = range(8)
deck = deck_a + deck_b
random.shuffle(deck)


# Creates a list called exposed which will 
# record whether the card is exposed or not
exposed = range(16)
for i in range(16):
    exposed[i] = False

card = 0
counter = 0
flip1 = 0
flip2 = 0

# helper function to initialize globals
def new_game():
    global card
    global state
    global counter
    global flip1
    global flip2
    for i in range(16):
        exposed[i] = False
    state = 0
    card = 0
    counter = 0
    flip1 = 0
    flip2 = 0
    random.shuffle(deck)
    label.set_text("Turns = " + str(counter))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global card
    global state
    global counter
    global flip1
    global flip2
    
    #checks for which card is clicked
    card_number = pos[0]//50 
       
    #defines the state of the game
    if exposed[card_number] == False:
        if state == 0:
            state = 1
            flip1 = card_number
        elif state == 1:
            state = 2
            flip2 = card_number
            counter += 1
            label.set_text("Turns = " + str(counter))
        else:
            state = 1
            if deck[flip1] == deck[flip2]:
                exposed[flip1] = True
                exposed[flip2] = True
                flip1 = card_number
            else:
                exposed[flip1] = False
                exposed[flip2] = False
                flip1 = card_number
    else:
        pass
    #exposes the card which was clicked
    exposed[card_number] = True
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    for i in range(16):
        canvas.draw_text(str(deck[i]), (20 + 50*i , 60), 40, 'White')
        if exposed[i] == False:
            canvas.draw_polygon([[0 + 50*i, 0], [50 + 50*i, 0], [50 + 50*i, 100], [0+50*i, 100]], 1, 'Black', 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric