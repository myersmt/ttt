'''
Matt Myers
09/16/2021
Tic Tac Toe
'''
import pygame as pg
import numpy as np
import sys
import ttt_fun as tf

def main():
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

    def restart():
        screen.fill( BG_COLOR )
        tf.draw_lines(screen, LINE_COLOR, LINE_WIDTH)
        for row in range(3):
            for col in range(3):
                board[row][col]=0

    # Mainloop
    def ttt():
        player =1
        game_won = False
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
                        tf.mark_square( board, crow, ccol, player )
                        if tf.results(screen, board,player, CIRCLE_COLOR, X_COLOR, HEIGHT):
                            game_won = True
                        player = player % 2 + 1
                            
                        draw_symbols()
                        
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        restart()
                        player = 1
                        game_won = False
                        
            pg.display.update()
    ttt()


if __name__ == '__main__':
    main()
