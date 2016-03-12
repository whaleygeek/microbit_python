# paintroller.py  12/03/2016  D.J.Whale

# Game parameters
MAX_GAME_TIME = 60000

def splash_screen(): # TODO
    pass
    # while not button pressed
        # show animation
        
def play_game(): # TODO
    count_dots = 0
    x = 2
    y = 2
    xdir = True
    # create blank canvas
    # sample start time
    while count_dots < 25 and running_time - start_time < MAX_GAME_TIME:
        if was_shake:
            # show roller animation
            # get random
            if xdir:
                # if pixel not set
                    # set pixel
                    # inc score
            else: # must be ydir
                # if pixel not set
                    # set pixel
                    # inc score
        if (compass - prev_compass) > 60:
            xdir = not xdir
            prev_compas = get compass
            if xdir:
                x = random
            else:
                y = random

def dots_to_score(dots):
    #TODO: use mathematical division
    if dots == 25: return 9
    if dots >= 22: return 8
    if dots >= 19: return 7
    if dots >= 16: return 6
    if dots >= 13: return 5
    if dots >= 10: return 4
    if dots >= 7:  return 3
    if dots >= 4:  return 2
    if dots >= 1:  return 1
    return 0

def flash_digit(digit, times):
    for i in range(times):
        display.show(digit)
        sleep(500)
        display.clear()
        sleep(500)
    display.show(digit)
    
def wait_button_b():
    button_b.reset_presses()
    while not button_b.was_pressed():
        pass
    
def run(): # TODO
    calibrate compass
    while True:
        splash_screen()
        #TODO: show start animation
        score = play_game()
        flash_digit(score)
        wait_button_b()
        #TODO: show end animation
    
# run()
