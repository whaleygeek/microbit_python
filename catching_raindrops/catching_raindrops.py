# catching_raindrops.py  08/03/2016  D.J.Whale

from microbit import *
import math

# game parameters

CUP_CAPACITY = 5
SPEED = 6
MAX_MISSES = 3
AUTO_EMPTY = False
SENSITIVITY = 400

SPLASH = [Image('00000:00000:00000:09090:09990:'),Image('00000:09090:00000:09090:09990:')]

def show_splash_screen():
    button_a.reset_presses()
    button_b.reset_presses()
    
    while not button_a.was_pressed() and not button_b.was_pressed():
        display.show(SPLASH, delay=250)

    button_a.reset_presses()
    button_b.reset_presses()

def get_cup_position():
    acc = accelerometer.get_x()/SENSITIVITY
    return math.clamp(0, 4, acc+2)

def test_movement():
    while not button_b.was_pressed():
        x = get_cup_position()
        display.clear()
        display.set_pixel(x, 2)
        sleep(200)
    button_b.reset_presses()
    
def show_number(n):
    for i in range(4):
        display.show(str(n))
        sleep(500)
        display.clear()
        sleep(500)
        
    display.show(str(n))
       
def play_game():
    score = 0
    drops_in_cup = 0
    misses = 0
    drop_x = 0
    drop_y = 0
    cup_x = 2
    state = "NEWDROP"
    
    while True:
        if state == "NEWDROP":
            ## create new drop at random position
            #state = "RAINING"
            pass
            
        elif state == "RAINING":
            ## draw cup
            ## draw drop
            ## if cup full:
            #    ## draw full cup
            ## if drop at cup
            #    state = "ATCUP"
            ## else
            #    ## move drop down
            ## if cup inverted and cup full
            #    state = "EMPTYING"
            pass
            
        elif state == "ATCUP":
            ## if drop at cup x
            #    state = "CATCH"
            ## else
            #    state = "MISS"
            pass
            
        elif state == "MISS":
            ## add one to misses
            ## show dropped animation
            ## if too many misses
            #    state = "GAMEOVER"
            ## else
            #    state = "NEWDROP"
            pass
            
        elif state == "CATCH":
            ## add one to drops in cup
            ## if cup is at capacity
            #    ## add one to score
            #    state = "FULL"
            ## else if over capacity
            #    state = "OVERFLOW"
            ## else
            #    ## add one to score
            #    state = "NEWDROP"
            pass
            
        elif state == "FULL":
            ## show animation 
            ## if AUTO EMPTY
            #    state = "EMPTYING"
            ## else
            #    state = "NEWDROP"
            pass
            
        elif state == "EMPTYING":
            ## if cup inverted
            #    ## show animation:draining
            ## else
            #    ## show animation: other?
            ## zero drops in cup
            ## if speed > 1
            #    ## take one off of speed
            #state = "NEWDROP"
            pass
            
        elif state == "OVERFLOW":
            ## show animation: overflowing
            #state = "GAMEOVER"
            pass
            
        elif state == "GAMEOVER":
            ## show animation: float to heaven
            #break
            pass
            
    return score
        
def run():
    high_score = 0
    
    while True:
        show_splash_screen()
        
        if button_a.was_pressed():
            button_a.reset_presses()
            score = play_game()
            if score > high_score:
                high_score = score
                show_number(high_score)
                
        elif button_b.was_pressed():
            button_b.reset_presses()
            test_movement()

# run()

    
    
