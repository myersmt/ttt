'''
Matt Myers
09/16/2021
Tic Tac Toe
'''
import pygame as pg
import numpy as np
import sys, random
import ttt_fun as tf

#Initializing pygame
pg.init()

#Creating Background
# * Contants
WIDTH = HEIGHT = 600
BG_COLOR = (40,40,45)
CIRCLE_COLOR = (10,10,15)
X_COLOR = (200,200,210)
LINE_COLOR = (60,60,70)
LINE_WIDTH  = 16
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_WIDTH = 25
X_SPACE = 50

# * Variables
screen = pg.display.set_mode( (WIDTH, HEIGHT) )
pg.display.set_caption('Tic Tac Toe')
screen.fill( BG_COLOR )

#Board
board = np.zeros((3, 3))
tf.draw_lines(screen, LINE_COLOR, LINE_WIDTH)

#Drawing symbols
def draw_symbols():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pg.draw.circle( screen, CIRCLE_COLOR, (int(col * 200+100), int(row * 200+100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pg.draw.line( screen, X_COLOR, (col *200+X_SPACE,row*200+200-X_SPACE), (col*200+200-X_SPACE,row*200+X_SPACE), X_WIDTH)
                pg.draw.line( screen, X_COLOR, (col *200+X_SPACE,row*200+X_SPACE), (col*200+200-X_SPACE,row*200+200-X_SPACE), X_WIDTH)

player = 1
game_won = False

# Mainloop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type ==pg.MOUSEBUTTONDOWN and not game_won:
            mx = event.pos[0]
            my = event.pos[1]
            
            crow = int(my // 200)
            ccol = int(mx // 200)
            
            if tf.available_spot( board, crow, ccol ):
                if player == 1:
                    tf.mark_square( board, crow, ccol, player )
                    if tf.results(screen, board,player, CIRCLE_COLOR, X_COLOR, HEIGHT):
                        game_won = True
                    player = 2
                elif player == 2:
                    tf.mark_square( board, crow, ccol, player )
                    if tf.results(screen, board,player, CIRCLE_COLOR, X_COLOR, HEIGHT):
                        game_won = True
                    player = 1
                    
                draw_symbols()
                
    pg.display.update()

