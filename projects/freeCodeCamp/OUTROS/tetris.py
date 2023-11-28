import pygame
import random
 
pygame.font.init()
 
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CIANO = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
 
 
# SHAPE FORMATS
 
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
 

shapes = [S, Z, I, O, J, L, T]
shape_colors = [GREEN, RED, CIANO, YELLOW, ORANGE, BLUE, PURPLE]
# index 0 - 6 represent shape
 
 
class Piece(object):
    def __init__(self, x , y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0
 

def create_grid(locked_pos={}):
    grid = [[BLACK for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c

    return grid



def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
    
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    
    return positions
 


def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == BLACK] for i in range(20)] # - > [[(0,1)], [(2,3)]]
    accepted_pos = [j for sub in accepted_pos for j in sub] # - > [(0, 1), (2, 3)]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

 

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
 

def get_shape():
    return Piece(5, 0, random.choice(shapes))
 
 
def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsansn", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/2 - label.get_height()/2))


def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, GREY, (sx, sy + i * block_size), (sx + play_width, sy + i * block_size)) # horizontal lines
        for j in range(len(grid[i])):
            pygame.draw.line(surface, GREY, (sx + j * block_size, sy), (sx + j * block_size, sy + play_height)) # vertical lines
            
    
    
 
def clear_rows(grid, locked):

    inc = 0
    for i in range(len(grid) -1, -1, -1):
        row = grid[i]
        if BLACK not in row:
            inc += 1
            ind = 1
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    
    if inc > 0:
        for key in sorted(list(locked), key = lambda x : x[1])[::-1]:
            x, y = key
            if y < ind:
                newKew = (x, y + inc)
                locked[newKew] = locked.pop(key)
    
    return inc

 
 
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, WHITE)

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i , line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * block_size, sy + i * block_size, block_size, block_size), 0)
    
    surface.blit(label, (sx + 10, sy - 50))


 
def draw_window(surface, grid, score=0):
    surface.fill(BLACK)

    font = pygame.font.SysFont('comicsans', 60)
    label = font.render("Tetris", 1, WHITE)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))

    # current score
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render(f'Score: {score}', 1, WHITE)

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    surface.blit(label, (sx + 20, sy + 160))


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)
    
    draw_grid(surface,grid)
    pygame.draw.rect(surface, RED, (top_left_x, top_left_y, play_width, play_height), 5)
   

 
def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    currente_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time  = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 >5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005

        if fall_time/1000 >= fall_speed:
            fall_time = 0
            currente_piece.y += 1
            if not(valid_space(currente_piece, grid)) and currente_piece.y > 0:
                currente_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    currente_piece.x -= 1
                    if not valid_space(currente_piece, grid):
                        currente_piece.x += 1

                if event.key == pygame.K_RIGHT:
                    currente_piece.x += 1
                    if not valid_space(currente_piece, grid):
                        currente_piece.x -= 1

                if event.key == pygame.K_DOWN:
                    currente_piece.y += 1
                    if not valid_space(currente_piece, grid):
                        currente_piece.y -= 1

                if event.key == pygame.K_UP:
                    currente_piece.rotation += 1
                    if not valid_space(currente_piece, grid):
                        currente_piece.rotation -= 1
        
        shape_pos = convert_shape_format(currente_piece)

        for i in range(len(shape_pos)):
            x,y = shape_pos[i]
            if y > -1:
                grid[y][x] = currente_piece.color
        
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = currente_piece.color
            currente_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid, score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST!", 80, WHITE)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False

    
 
def main_menu(win):
    run = True
    while run:
        win.fill(BLACK)
        draw_text_middle(win,"Press Any Key To Play", 60, WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")

main_menu(win)  # start game