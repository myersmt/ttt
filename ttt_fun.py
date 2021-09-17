'''
Matt Myers
09/LW/2021
Tic Tac Toe Functions
'''
import pygame as pg

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

def results(s, board, player, cc, xc, h):
    # Vert check
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vert_win(s, col, player, cc, xc, h)
            return True
    
    # Hor check
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            hor_win(s, row, player, cc, xc, h)
            return True
    
    # down diag check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        down_diag_win(s, player, cc, xc, h)
        return True
        
    # up diag check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        up_diag_win(s, player, cc, xc, h)
        return True
    
    return False

def vert_win(s, col, player, cc, xc, h):
    x = col *200 +100
    
    if player ==1:
        c = cc
    elif player == 2:
        c = xc
    
    pg.draw.line(s, c, (x,15), (x, h-15), 15)

def hor_win(s, row, player, cc, xc, h):
    y = row *200+100
    
    if player == 1:
        c = cc
    elif player == 2:
        c = xc
    
    pg.draw.line(s,c, (15,y), (h-15,y), 15)

def up_diag_win(s, player, cc, xc, h):
    if player == 1:
        c = cc
    elif player == 2:
        c = xc
    
    pg.draw.line( s, c, (15,h-15), (h-15,15), 15)

def down_diag_win(s, player, cc, xc, h):
    if player == 1:
        c = cc
    elif player == 2:
        c = xc
    
    pg.draw.line( s, c, (15,15), (h-15,h-15), 15)

def restart():
    pass