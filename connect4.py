# from colorama import Fore

rows = 8
cols = 8
current_player = 'X'
# board = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", "X", " ", " ", " "]]
board = [[" " for i in range(cols)] for j in range(rows)]

def print_board():
    for row in board:
        print('| ', end = '')
        for cell in row:
            if cell == ' ':
                print('. ', end = '')
            else:
                print(cell + ' ', end = '')
        print('|')
    print("  0 1 2 3 4 5 6 7")

def drop_piece(board, col, piece):
    for row in reversed(range(rows)):
        if board[row][col] == ' ':
            board[row][col] = piece
            return row
    return None

def piece_counter(start_row, start_col, row_change, col_change, piece):
    counter = 0
    row = start_row
    col = start_col
    while row >= 0 and row < rows and col >= 0 and col < cols and board[row][col] == piece:
        counter += 1
        col += col_change
        row += row_change
    return counter

def check_win(row, col, piece):
    # horizontal
    total = (piece_counter(row, col, 0, 1, piece) + piece_counter(row, col, 0, -1, piece))-1
    if total >= 4:
        return True
    total = (piece_counter(row, col, 1, 0, piece) + piece_counter(row, col, -1, 0, piece))-1
    if total >= 4:
        return True
    total = (piece_counter(row, col, 1, 1, piece) + piece_counter(row, col, -1, -1, piece))-1
    if total >= 4:
        return True
    total = (piece_counter(row, col, 1, -1, piece) + piece_counter(row, col, -1, 1, piece))-1
    if total >= 4:
        return True
    return False

while True:
    print_board()
    print(f'it is the turn of player {current_player}')
    try:
        col = int(input('which column do you want to place the piece in? '))
    except  ValueError:
        print('that is not EVEN a number!')
        continue
    if col > cols or col < 0:
        print(f'invalid number, please choose an input between 0 and {cols}')
        continue
    row = drop_piece(board, col, current_player)
    if row == None:
        print('that column is full, try a different number')
        continue
    if check_win(row, col, current_player):
        print('player ' + current_player + ' Wins!')
        break
    if board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[0][3] != ' ' and board[0][4] != ' ':
        print_board()
        print('it is a tie')
        break
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'