


def create_board(cols=7, rows=6):
    """initializes the board"""
    mat = []
    for row in range(rows):
        mat_row = []
        for col in range(cols):
            mat_row.append('*')


def column_is_full(board, col):
    """returns whether the whole column is full"""
    return board[0][col] != '*'

def drop_disc(board, col, mark):
    """drops the disk if the column is not full"""
    if not column_is_full(board, col):
        for row in reversed(board):

            if row[col] == '*':
                row[col] = mark
                return
