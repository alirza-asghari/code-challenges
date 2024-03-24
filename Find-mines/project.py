
def find_mines(board, row, column):
    # checking if it is mine or not
    if board[row][column] == 1:
        return 9
    mine_counter = 0
    for i in range(row - 1, row + 2):
        if i < 0: continue
        for j in range(column - 1, column + 2):
            # first check the shitty terms
            if j < 0: continue
            if i == row and j == column: continue
            try:
                if board[i][j] == 1:
                    mine_counter += 1
            except IndexError:
                pass
    return mine_counter

    
def number_of_neighbouring_mines(board):
    num_rows = len(board)
    num_cols = len(board[0])
    mines = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    # new list with board size created
    for i in range(len(board)):
        for j in range(len(board[i])):
            mines[i][j] = find_mines(board, i, j)
    return mines
            
board = [
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 0]
]

print(number_of_neighbouring_mines(board))

