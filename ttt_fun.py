'''
Matt Myers
09/LW/2021
Tic Tac Toe Functions
'''
import pygame as pg

pg.init()

def draw_lines(S, LC,LW):
    pg.draw.rect(S, LC, pg.Rect(192,0,LW,600),8,LW)
    pg.draw.rect(S, LC, pg.Rect(392,0,LW,600),8,LW)
    pg.draw.rect(S, LC, pg.Rect(0,192,600,LW),8,LW)
    pg.draw.rect(S, LC, pg.Rect(0,392,600,LW),8,LW)

def mark_square(board, row, col, player):
    board[row][col] = player

def available_spot(board, row, col):
    return board[row][col] == 0

def available_board(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True
