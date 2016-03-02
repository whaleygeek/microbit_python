# connect4x4  02/03/2016  D.J.Whale
#
# A 4x4 grid of connect 4 with full gameplay

from microbit import *

# two player boards
# 16 bit binary encoded raster for player 1[0] and player 2[1]
boards = [0x0000, 0x0000]

# winning masks for win signatures, 10 in all for a 4x4 board
# can be applied to any player board
# xy coords,       lay bits out left to right MSB to LSB for a board
# 00 01 02 03      15 14 13 12
# 10 11 12 13      11 10 09 08
# 20 21 22 23      07 06 05 04
# 30 31 32 33      03 02 01 00

win = [
#horizontal wins (4)
# 15,14,13,12 = 1111 0000 0000 0000
0xF000,
# 11,10,09,08 = 0000 1111 0000 0000
0x0F00,
# 07,06,05,04 = 0000 0000 1111 0000
0x00F0,
# 03,02,01,00 = 0000 0000 0000 1111
0x000F,
#vertical wins (4)
# 15,11,07,03 = 1000 1000 1000 1000
0x8888,
# 14,10,06,02 = 0100 0100 0100 0100
0x4444,
# 13,09,05,01 = 0010 0010 0010 0010
0x2222,
# 12,08,04,00 = 0001 0001 0001 0001
0x1111,
#diagonal wins (2)
# 15,10,05,00 = 1000 0100 0010 0001
0x8421,
# 12,09,06,03 = 0001 0010 0100 1000
0x1248
]

def splash_screen():
    pass
    # show a splash screen until any button is pressed
    
# move a piece
def move(player):
    pass
    # button A moves left, until leftmost position
    # button B moves right, until rightmost position
    # button A+B requests a drop
    # draws a dot at top row
    # intensity is bright for player 1, dim for player 2
    # returns column selected (0..3)
    
# work out how far to drop a piece until it stops
def get_depth(col):
    pass
    # scans down the column finding the first full piece for any player
    # returns 0 if the column is full
    # returns 1 if there is 1 space left, 2, 3.
    # OR together both boards to get occupancy signature
    # highest 3-(set bit number in nibble) (3210) is depth of that col
    # i.e. could count how many right shifts of number until it is zero
    # or could pre-compute a depth table for each column and just compare?
    # col0 0x8888
    # col1 0x4444
    # col2 0x2222
    # col3 0x1111
    
# drop a piece
def drop(player, col, depth):
    pass
    # animates dropping a piece for a player
    #   draw the player dot in the correct intensity
    #   animate from top down to depth (0 is top, 3 is bottom)
    # must set appropriate bit in board for that player at end
    #   col is index into nibble (how many shifts of 4bits)
    #   row is bit number in nibble (how many shifts)
    
# work out if there is a winner
def get_winner():
    pass
    # -1: stalemate
    # 0 : no winner
    # 1 : player 1 wins
    # 2 : player 2 wins
    # compare board[0] against 10 masks, any match, player 1 wins
    # compare board[1] against 10 masks, any match, player 2 wins
    # no player wins (0)
    
# show winner or stalemate annimation
def winner(player):
    pass
    # show a flashing player number then solid at end
    # note player 0 means stale mate
    # at end, wait for any button press to exit
    
# run forever
while True:
    game_over = False
    player = 1
    clear_board()
    
    # show splash screen and wait for start
    splash_screen()

    # main game loop
    while not game_over:
        # get a move
        while True:
            col = move()
            depth = get_depth(col)
            if depth > 0:
                break

        # action the move
        drop(player, col, depth)
        
        # work out if the game is over
        win = get_winner()
        if win == -1:
            winner(0)
            
        else if win != 0:
            winner(win)
            game_over = True
            
        else:
            # swap to other player
            if player == 1:
                player = 2
            else:
                player = 1
