class Board:
    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        self.grid = [[" " for i in range(cols)] for j in range(rows)]

    def print_board(self):
        for row in self.grid:
            print('| ', end = '')
            for cell in row:
                if cell == ' ':
                    print('. ', end = '')
                else:
                    print(cell + ' ', end = '')
            print('|')
        print("  0 1 2 3 4")

    def drop_piece(self, board, col, piece):
        for row in reversed(range(self.rows)):
            if self.grid[row][col] == ' ':
                self.grid[row][col] = piece
                return row
        return None

    def piece_counter(self, start_row, start_col, row_change, col_change, piece):
        counter = 0
        row = start_row
        col = start_col
        while row >= 0 and row < self.rows and col >= 0 and col < self.cols and self.grid[row][col] == piece:
            counter += 1
            col += col_change
            row += row_change
        return counter

    def check_win(self, row, col, piece):
        # horizontal
        total = (self.piece_counter(row, col, 0, 1, piece) + self.piece_counter(row, col, 0, -1, piece))-1
        if total >= 4:
            return True
        total = (self.piece_counter(row, col, 1, 0, piece) + self.piece_counter(row, col, -1, 0, piece))-1
        if total >= 4:
            return True
        total = (self.piece_counter(row, col, 1, 1, piece) + self.piece_counter(row, col, -1, -1, piece))-1
        if total >= 4:
            return True
        total = (self.piece_counter(row, col, 1, -1, piece) + self.piece_counter(row, col, -1, 1, piece))-1
        if total >= 4:
            return True
        return False

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def run(self):
        while True:
            self.board.print_board()
            print(f'it is the turn of player {self.current_player}')
            try:
                col = int(input('which column do you want to place the piece in? '))
            except  ValueError:
                print('that is not even a number')
                continue
            if col > 4 or col < 0:
                print('invalid number, please choose an input between 0 and 4')
                continue
            row = self.board.drop_piece(self.board.grid, col, self.current_player)
            if row == None:
                print('that column is full, try a different number')
                continue
            if self.board.check_win(row, col, self.current_player):
                self.board.print_board()
                print('player ' + self.current_player + ' Wins!')
                break
            if self.board.grid[0][0] != ' ' and self.board.grid[0][1] != ' ' and self.board.grid[0][2] != ' ' and self.board.grid[0][3] != ' ' and self.board.grid[0][4] != ' ':
                self.board.print_board()
                print('it is a tie')
                break
            self.switch_player()
if __name__ == '__main__':
    game = Game()
    game.run()