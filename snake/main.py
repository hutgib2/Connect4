import pygame
import sys
import random

cell_size = 32
rows = 32
cols = 32
width = cols * cell_size
height = rows * cell_size
snake = [(5,5),(5,4),(5,3)]
direction = (0, 1)

def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

pygame.init()
font = pygame.font.SysFont(None, 64)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('snake')
clock = pygame.time.Clock()
running = True
food = (random.randint(0, rows-1), random.randint(0, cols-1))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = (-1, 0)
            if event.key == pygame.K_s:
                direction = (1, 0)
            if event.key == pygame.K_a:
                direction = (0, -1)
            if event.key == pygame.K_d:
                direction = (0, 1)
    head_row, head_col = snake[0]
    d_row, d_col = direction
    new_head = (head_row+d_row, head_col+d_col)

    # wall_collision
    if new_head == food:
        food = (random.randint(0, rows-1), random.randint(0, cols-1))
    else:
        snake.pop()
    
    if not (0 <= new_head[0] < rows and 0 <= new_head[1] < cols):
        print('WASTED')
        running = False
    # snake_collision
    elif new_head in snake:
        print('WASTED')
        running = False
    snake.insert(0, new_head)

    screen.fill((0,0,0))
    for row, col in snake:
        pygame.draw.rect(screen, (0, 255, 0),
        (col*cell_size, row*cell_size, cell_size, cell_size))
    f_row, f_col = food
    pygame.draw.rect(screen, (255, 128, 0), (f_col*cell_size, f_row*cell_size, cell_size, cell_size))
    score = len(snake) - 3
    draw_text(f'Score: {score}', (255, 255, 255), 10, 10)
    pygame.display.update()
    clock.tick(10)
pygame.quit()
sys.exit()