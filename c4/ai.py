import random
from c4.board import drop_disc

def choose_move_random(board):
    """chooses a column for the computer"""
    col = random.randrange(len(board[0]))

    while not drop_disc(board, col, 'X'):
        col = random.randrange(len(board[0]))

    return col
