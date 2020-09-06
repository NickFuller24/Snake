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
UP = 1
DOWN = 2 
LEFT = 3
RIGHT = 4


#Setting up the window
board = pygame.display.set_mode((WIN_H,WIN_W))
pygame.display.set_caption("Snake")
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)

#Snake class
class Snake():
#This class contains the variables associated with a snake

    length = 1

    #start the snake in the middle of the grid
    x_coord = COLS // 2
    y_coord = ROWS // 2

    #initialize the corresponding grid value
    def __init__(self, grid):
        grid[ROWS // 2][COLS // 2] = SNAKE_BLOCK
        pygame.draw.rect(board, RED, (self.x_coord*BLOCK_W,self.y_coord*BLOCK_H,BLOCK_W,BLOCK_H))

    direction = RIGHT

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

    #draw grid lines
    draw_board()

    #empty grid
    grid_vals = []

    #seed random generator
    random.seed()

    #clear grid values(set all to zero)
    clear_grid(grid_vals)

    green_square(grid_vals)

    #create the snake character
    s = Snake(grid_vals)
    
    run = True
    while run:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #get all key values
        keys = pygame.key.get_pressed()
        
        #determine direction that the snake should move
        if keys[pygame.K_UP]:
            s.direction = UP
            s.y_coord -= 1                  #rows count top to bottom
        if keys[pygame.K_DOWN]:
            s.direction = DOWN
            s.y_coord += 1
        if keys[pygame.K_LEFT]:
            s.direction = LEFT
            s.x_coord -= 1
        if keys[pygame.K_RIGHT]:
            s.direction = RIGHT
            s.x_coord += 1
        
        pygame.draw.rect(board, RED, (s.x_coord*BLOCK_W,s.y_coord*BLOCK_H,BLOCK_W,BLOCK_H))
        pygame.display.update()

main()
pygame.quit()
