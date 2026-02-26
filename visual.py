import pygame
import sys
from connect4classes import Board, Game
pygame.init()

rows = 5
cols = 5

cell_size = 100

width = cell_size * cols
height = cell_size * rows

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('connect4')

black = (0, 0, 0)
blue = (0 ,0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
game  = Game()

def draw_board(board):
    for row in range(board.rows):
        for col in range(board.cols):
            pygame.draw.rect(screen, blue, (col * cell_size, row*cell_size, cell_size, cell_size))
            x = col*cell_size + cell_size / 2
            y = row*cell_size + cell_size / 2
            if board.grid[row][col] == ' ':
                color = 'black'
            elif board.grid[row][col] == 'X':
                color = 'red'
            elif board.grid[row][col] == 'O':
                color = 'yellow'
            pygame.draw.circle(screen, color, (x,y), cell_size / 2)

# game starts

running = True
winner = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and winner == None:
            x_pos = event.pos[0]
            col = x_pos//cell_size
            row = game.board.drop_piece(game.board, col, game.current_player)
            if row != None:
                if game.board.check_win(row, col, game.current_player):
                    winner = game.current_player
                    print(f'player {winner} wins!')
                elif game.board.grid[0][0] != ' ' and game.board.grid[0][1] != ' ' and game.board.grid[0][2] != ' ' and game.board.grid[0][3] != ' ' and game.board.grid[0][4] != ' ':
                    print('it is a tie')
                else:
                    game.switch_player()

    screen.fill(black)
    draw_board(game.board)
    pygame.display.update()

pygame.quit()
sys.exit()