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

    length = 0

    #start the snake in the middle of the grid
    x_coord = COLS // 2
    y_coord = ROWS // 2

    #(row = y, column = x)
    coords = [[y_coord,x_coord]]

    #initialize the corresponding grid value
    def __init__(self, grid):
        grid[ROWS // 2][COLS // 2] = SNAKE_BLOCK
        pygame.draw.rect(board, RED, (self.x_coord*BLOCK_W+MARGIN,self.y_coord*BLOCK_H+MARGIN,BLOCK_W-MARGIN,BLOCK_H-MARGIN))

    direction = RIGHT

#draw the grid lines
def draw_board():
    for row in range(ROWS):
        #horizontal line for each row
        pygame.draw.line(board, BLACK, (0,row*BLOCK_H), (WIN_W-1,row*BLOCK_H))
        #vertical line for each column
        pygame.draw.line(board, BLACK, (row*BLOCK_H,0), (row*BLOCK_H, WIN_H-1), MARGIN)

#populate grid with all zeros
def clear_grid(grid):
    for row in range(ROWS):
        grid.append([])
        for col in range(COLS):
            #assign each grid cell the value of 0
            grid[row].append([])
            grid[row][col] = WHITE_BLOCK

#draw a random green square and set corresponding grid value
def green_square(grid):
    #get random coordinates
    randx = random.randint(0,COLS-1)
    randy = random.randint(0,ROWS-1)
    #repeat until the grid space is not part of the snake
    while grid[randy][randx] == SNAKE_BLOCK:
        randx = random.randint(0,COLS-1)
        randy = random.randint(0,ROWS-1)

    #draw green rectangle at the random coordinates
    pygame.draw.rect(board, GREEN, (randx*BLOCK_W+MARGIN,randy*BLOCK_H+MARGIN,BLOCK_W-MARGIN,BLOCK_H-MARGIN))

    #set grid value to green
    grid[randy][randx] = GREEN_BLOCK

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

    #initial green square
    green_square(grid_vals)

    #create the snake character
    s = Snake(grid_vals)
    
    run = True
    while run:
        pygame.time.delay(80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #get all key values
        keys = pygame.key.get_pressed()
        
        #determine direction that the snake should move
        if keys[pygame.K_UP]:
            s.direction = UP
        if keys[pygame.K_DOWN]:
            s.direction = DOWN
        if keys[pygame.K_LEFT]:
            s.direction = LEFT
        if keys[pygame.K_RIGHT]:
            s.direction = RIGHT
        
        #clear board
        #deal with edge cases. Pacman effect(continued on line 175)
        for num in range(0,s.length + 1):
            if s.coords[num][0] == ROWS-1 and s.direction == UP:
                grid_vals[0][s.coords[num][1]] = WHITE_BLOCK
                pygame.draw.rect(board, WHITE, (s.coords[num][1]*BLOCK_W+MARGIN,0*BLOCK_H+MARGIN,BLOCK_W-MARGIN,BLOCK_H-MARGIN))
            elif s.coords[num][0] == 0 and s.direction == DOWN:
                grid_vals[ROWS-1][s.coords[num][1]] = WHITE_BLOCK
                pygame.draw.rect(board, WHITE, (s.coords[num][1]*BLOCK_W+MARGIN,(ROWS-1)*BLOCK_H+MARGIN,BLOCK_W-MARGIN,BLOCK_H-MARGIN))
            elif s.coords[num][1] == ROWS and s.direction == LEFT:
                grid_vals[s.coords[num][0]][0] = WHITE_BLOCK
                pygame.draw.rect(board, WHITE, (0*BLOCK_W+MARGIN,s.coords[num][0]*BLOCK_H+MARGIN,BLOCK_W-MARGIN,BLOCK_H-MARGIN))
            elif s.coords[num][1] == 0 and s.direction == RIGHT:
                grid_vals[s.coords[num][0]][ROWS-1] = WHITE_BLOCK
                pygame.draw.rect(board, WHITE, ((ROWS-1)*BLOCK_W+MARGIN,s.coords[num][0]*BLOCK_H+MARGIN,BLOCK_W-MARGIN,BLOCK_H-MARGIN))
        
            #clear board at previous coordinates
            grid_vals[s.coords[num][0]][s.coords[num][1]] = WHITE_BLOCK
            pygame.draw.rect(board, WHITE, (s.coords[num][1]*BLOCK_W+MARGIN,s.coords[num][0]*BLOCK_H+MARGIN,BLOCK_W-MARGIN,BLOCK_H-MARGIN))

        #Change coordinates
        if s.direction == UP:
            s.y_coord -= 1
        elif s.direction == DOWN:
            s.y_coord += 1
        elif s.direction == LEFT:
            s.x_coord -= 1
        else:
            s.x_coord += 1

        #move snake block
        #deal with edge cases. Pacman effect
        if s.y_coord == ROWS:
            s.y_coord = 0
        elif s.y_coord == -1:
            s.y_coord = ROWS - 1
        if s.x_coord == ROWS:
            s.x_coord = 0
        elif s.x_coord == -1:
            s.x_coord = ROWS - 1

        #check for green square and add to length if the snake found green square. Also generate
        #a new green square
        if grid_vals[s.y_coord][s.x_coord] == GREEN_BLOCK:
            s.length += 1
            s.coords.append([])
            green_square(grid_vals)
        
        #body blocks
        if s.length > 0:
            for num in range(s.length,0,-1):
                #This saves the previous coordinates(since the body blocks tail the head)
                s.coords[num] = s.coords[num-1]

                #draw the block and set the corresponding grid value (row = y,column = x)
                grid_vals[s.coords[num][0]][s.coords[num][1]] = SNAKE_BLOCK
                pygame.draw.rect(board, RED, (s.coords[num][1]*BLOCK_W+MARGIN,s.coords[num][0]*BLOCK_H+MARGIN,BLOCK_W-MARGIN,BLOCK_H-MARGIN))
        
        #if snake ran into itself
        if grid_vals[s.y_coord][s.x_coord] == SNAKE_BLOCK:
            run = False

        #head block
        s.coords[0] = [s.y_coord,s.x_coord]
        grid_vals[s.y_coord][s.x_coord] = SNAKE_BLOCK
        pygame.draw.rect(board, RED, (s.x_coord*BLOCK_W+MARGIN,s.y_coord*BLOCK_H+MARGIN,BLOCK_W-MARGIN,BLOCK_H-MARGIN))

        pygame.display.update()

main()
pygame.quit()
