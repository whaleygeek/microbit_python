# catching_raindrops.py  08/03/2016  D.J.Whale

# game parameters

CUP_CAPACITY = 5
SPEED = 6
MAX_MISSES = 3
AUTO_EMPTY = False
SENSITIVITY = 400

def get_cup_position():
    acc = accelerometer.get_x()/SENSITIVITY
    return math.clamp(0, 4, acc+2)
    
def show_splash_screen():
    pass # TODO show an animation until any button pressed
    
def play_game():
    score = 0
    drops_in_cup = 0
    misses = 0
    drop_x = 0
    drop_y = 0
    cup_x = 2
    state = "NEWDROP"
    ##start_game
    while True:
        if state == "NEWDROP":
            pass
            
        elif state == "RAINING":
            pass
            
        elif state == "ATCUP":
            pass
            
        elif state == "MISS":
            pass
            
        elif state == "CATCH":
            pass
            
        elif state == "FULL":
            pass
            
        elif state == "EMPTYING"
            pass
            
        elif state == "OVERFLOW":
            pass
            
        elif state == "GAMEOVER":
            pass
        

def test_movement():
    button_b.reset_presses()
    while not button_b.was_pressed():
        x = get_cup_position()
        display.clear()
        display.set_pixel(x, 2)
        sleep(200)
    
def show_number(n):
    pass # TODO flash digit 4 times then leave it solid
       
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

    
    
