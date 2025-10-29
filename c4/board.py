
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
        for row_index, row in enumerate(reversed(board)):

            if row[col] == '*':
                row[col] = mark
                return row_index, col

def legal_moves(board):
    """return a list with all the legal columns"""
    legal_moves_arr = []
    for col_index, val in enumerate(board[0]):
        if val == '*':
            legal_moves_arr.append(col_index)

def create_col_numbers(num):
    """this will create the column numbers on the top"""
    row_numbers = ""
    for i in range(num):
        row_numbers += f"{i} "

    row_numbers += '\n'
    return row_numbers

def render(board):
    """returns a string of the board"""
    row_numbers = create_col_numbers(len(board[0]))

    render_str = ""
    for row in board:
        for val in row:
            render_str += f"{val} "

    render_str += '\n'

    return row_numbers + render_str