# catching_raindrops.py  08/03/2016  D.J.Whale

from microbit import *
import math

# Game parameters
CUP_CAPACITY = 5
SPEED = 6
MAX_MISSES = 3
AUTO_EMPTY = False
SENSITIVITY = 400

# Images
BLANK      = Image('00000:00000:00000:00000:00000')
BLINK      = Image('00000:09090:00000:00000:00000')
CUP        = Image('00000:00000:00000:09090:09990')
CUP_FULL   = Image('00000:00000:00000:09990:09990')
CUP_BLINK  = Image('00000:09090:00000:09090:09990')

CUP_CATCH1 = Image('00000:00000:00000:09990:09990')
CUP_CATCH2 = Image('00000:00000:00000:90909:99999')

CUP_JUMP1  = Image('00000:09090:09990:00000:00900')
CUP_JUMP2  = Image('00000:00000:09090:09990:00000')

CUP_DRAIN1 = Image('00000:00000:00900:09090:09990')
CUP_DRAIN2 = Image('00000:00900:00000:09090:09990')
CUP_DRAIN3 = Image('00900:00000:00000:09090:09990')

CUP_OVER1  = Image('00000:00000:09990:09990:09990')
CUP_OVER2  = Image('00000:00000:09090:99999:09990')
CUP_OVER3  = Image('00000:00000:00000:99999:09990')
CUP_OVER4  = Image('00000:00000:00000:09990:99999')

CUP_FLOAT1 = Image('00000:00000:00000:00000:99999')
CUP_FLOAT2 = Image('00000:00000:00000:09990:09090')
CUP_FLOAT3 = Image('00000:00000:00000:99999:00000')
CUP_FLOAT4 = Image('00000:00000:09990:09090:00000')
CUP_FLOAT5 = Image('00000:00000:99999:00000:00000')
CUP_FLOAT6 = Image('00000:09990:09090:00000:00000')
CUP_FLOAT7 = Image('00000:99999:00000:00000:00000')
CUP_FLOAT8 = Image('09990:09090:00000:00000:00000')
CUP_FLOAT9 = Image('99999:00000:00000:00000:00000')

# Animations
SPLASH     = [CUP, CUP_BLINK]
CUP_CANVAS = [BLANK, CUP, BLANK]
DROPPED    = [CUP, CUP_JUMP1, CUP_JUMP2, CUP]
CAUGHT     = [CUP_CATCH1, CUP_CATCH2, CUP]
DRAINING   = [CUP_FULL, CUP_DRAIN1, CUP_DRAIN2, CUP_DRAIN3, CUP]
OVERFLOW   = [CUP_FULL, CUP_OVER1, CUP_OVER2, CUP_OVER3, CUP_OVER4, CUP_FULL]
HEAVEN     = [CUP, CUP_FLOAT1, CUP_FLOAT2, CUP_FLOAT3, CUP_FLOAT4, CUP_FLOAT5, CUP_FLOAT6, CUP_FLOAT7, CUP_FLOAT8, 
              CUP_FLOAT9, BLANK, BLINK, BLANK]

def show_splash_screen():
    button_a.reset_presses()
    button_b.reset_presses()
    
    while not button_a.was_pressed() and not button_b.was_pressed():
        display.show(SPLASH, delay=250)

    button_a.reset_presses()
    button_b.reset_presses()

def get_cup_position():
    acc = accelerometer.get_x()/SENSITIVITY
    acc += 2
    if acc > 4:
        acc = 4
    elif acc < 0:
        acc = 0
    return int(acc)

def test_movement():
    while not button_b.was_pressed():
        x = get_cup_position()
        display.clear()
        display.set_pixel(x, 2, 9)
        sleep(200)
    button_b.reset_presses()
    
def show_number(n):
    for i in range(4):
        display.show(str(n))
        sleep(500)
        display.clear()
        sleep(500)
        
    display.show(str(n))
       
def play_game(): #TODO
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
            ## draw cup CUP
            ## draw drop plot
            ## if cup full:
            #    ## draw full cup CUP_FULL
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
            ## show dropped animation DROPPED
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
            ## show animation FULL??
            #    state = "NEWDROP"
            pass
            
        elif state == "EMPTYING":
            # show animation: draining     DRAINING
            ## zero drops in cup
            ## if speed > 1
            #    ## take one off of speed
            #state = "NEWDROP"
            pass
            
        elif state == "OVERFLOW":
            ## show animation: overflowing    OVERFLOW
            #state = "GAMEOVER"
            pass
            
        elif state == "GAMEOVER":
            ## show animation: float to heaven    HEAVEN
            #break
            pass
            
    return score
        
def run(): #TO TEST
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

    
    
