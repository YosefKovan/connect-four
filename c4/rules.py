
def in_bounds(board, row, col):
    """returns if the row and col are in the bounds of the board"""
    return 0 <= row < len(board) and 0<= col < len(board[0])

def check_direction(board, row, col, direction, mark):
    """checks every direction """
    #this will make sure that we don't start from the current piece
    row += direction[0]
    col += direction[1]

    count = 0
    while in_bounds(board, row, col):
          if board[row][col] == mark:
             count += 1
             row += direction[0]
             col += direction[1]
          else:
              break

    return count

def check_all_directions(board, row, col, mark):
    """checks all four directions if there is a - connect 4"""

    #this will check horizontal direction
    if check_direction(board, row, col, (0, 1), mark) + check_direction(board, row, col, (0, -1), mark) + 1 >= 4:
        return True
    #this will check vertical direction
    if check_direction(board, row, col, (1, 0), mark) + check_direction(board, row, col, (-1, 0), mark) + 1 >= 4:
        return True
    #this will check the slant going from top left to bottom right
    if check_direction(board, row, col, (-1, -1), mark) + check_direction(board, row, col, (1, 1), mark) + 1 >= 4:
        return True
    #this will check the slant going from bottom left to top right
    if check_direction(board, row, col, (1, -1), mark) + check_direction(board, row, col, (-1, 1), mark) + 1 >= 4:
        return True

def has_winner(board):
    """returns if there is a winner"""
    for row_index, row in enumerate(board):
        for col_index in range(len(row)):
            print(row_index, col_index)
            if board[row_index][col_index] == '*':
              continue

            if check_all_directions(board, row_index, col_index, board[row_index][col_index]):
                return True

    return False

def if_full(board):
    """return if the board is full and there is nowhere else to go"""
    for row_index, row in enumerate(board):
        for col_index in range(len(row)):
            if board[row_index][col_index] == '*':
                return False

    return True