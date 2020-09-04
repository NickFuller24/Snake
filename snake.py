import pygame
import random

pygame.init()
random.seed()

#constants
BLACK = (0,0,0)
WHITE = (255,255,255)
WHITE_BLOCK = 0
RED = (255,0,0)
GREEN = (0,255,0)
GREEN_BLOCK = 1
WIN_H = 500
ROWS = 25
WIN_W = 500
COLS = 25
BLOCK_W = 20
BLOCK_H = 20
MARGIN = 1
SNAKE_BLOCK = 2


#Setting up the window
board = pygame.display.set_mode((WIN_H,WIN_W))
pygame.display.set_caption("Snake")
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)

#Snake class
class Snake:
    def __init__(self,grid):
        self.length = 1
        self.x_coord = COLS // 2
        self.y_coord = ROWS // 2
        grid[ROWS // 2][COLS // 2] = SNAKE_BLOCK
        pygame.draw.rect(board, RED, (self.x_coord*BLOCK_W,self.y_coord*BLOCK_H,BLOCK_W,BLOCK_H))


#draw the grid lines
def draw_board():
    for row in range(ROWS):
        #horizontal line for each row
        pygame.draw.line(board, BLACK, (0,row*BLOCK_H), (WIN_W-1,row*BLOCK_H))
        #vertical line for each column
        pygame.draw.line(board, BLACK, (row*BLOCK_H,0), (row*BLOCK_H, WIN_H-1), MARGIN)
        #for col in range(COLS):
            #vertical line for each column
            #pygame.draw.line(board, BLACK, (col*BLOCK_W,0), (col*BLOCK_W,WIN_H-1), MARGIN)

#populate grid with all zeros
def clear_grid(grid):
    for row in range(ROWS):
        grid.append([])
        for col in range(COLS):
            #assign each grid cell the value of 0
            grid[row].append([])
            grid[row][col] = WHITE_BLOCK

def green_square(grid):
    #get random coordinates
    randx = random.randint(0,COLS-1)
    randy = random.randint(0,ROWS-1)

    #draw green rectangle at the random coordinates
    pygame.draw.rect(board, GREEN, (randx*BLOCK_W,randy*BLOCK_H,BLOCK_W,BLOCK_H))

    #set grid value to green
    grid[randx][randy] = GREEN_BLOCK

    grid[randx][randy] = GREEN_BLOCK

#Running the game
def main():
    #fill grid with white
    board.fill(WHITE)

    #empty grid
    grid_vals = []

    #seed random generator
    random.seed()

    #clear grid values(set all to zero)
    clear_grid(grid_vals)

    #for row in range(ROWS - 1):
        #for col in range(COLS - 1):
            #print(grid_vals[row][col])
        #print('\n')
    green_square(grid_vals)
    s = Snake(grid_vals)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_board()
        pygame.display.update()

main()
pygame.quit()
