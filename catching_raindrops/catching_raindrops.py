# catching_raindrops.py  08/03/2016  D.J.Whale

# game parameters

CUP_CAPACITY = 5
SPEED = 6
MAX_MISSES = 3
AUTO_EMPTY = False
MOVEMENT = True
SENSITIVITY = 400

def show_splash_screen():
    pass
    
def play_game():
    pass

def test_movement():
    pass
    
def show_number(n):
    pass
       
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

    
    
