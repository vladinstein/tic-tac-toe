import sys, pygame

class Tic_Tac_Toe:
    square = [0] * 9

    def make_move(self, number, value):
        self.square[number] = value

def draw_grid():
    square_size = 200
    for x in range(3):
        for y in range(3):
            rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
            pygame.draw.rect(screen, black, rect, 3)

#game.make_move(3, 1)
#print(board.square)
#if game.check_win():
#    print('Victory!')

pygame.init()

size = width, height = 600, 600
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
# What does this do?
clock = pygame.time.Clock()

screen.fill(white)
move = True
board = Tic_Tac_Toe()


while True:
    print(board.square)
    draw_grid()
    x = y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
    # First square 
    if x > 0 and x < width / 3 and y > 0 and y < height/3 and board.square[0] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width / 30, height / 30), (width * 9 / 30, height * 9 / 30), 9)
            pygame.draw.line(screen, black, (width / 30, height * 9 / 30), (width * 9 / 30, height / 30), 9)
            board.make_move(0, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 6, height / 6), 85, 6)
            board.make_move(0, 2)
        move = not move
    # Second square
    if x > width / 3 and x < width * 2 / 3 and y > 0 and y < height / 3 and board.square[1] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width * 11 / 30, height / 30), (width * 19 / 30, height * 9 / 30), 9)
            pygame.draw.line(screen, black, (width * 11 / 30, height * 9 / 30), (width * 19 / 30, height / 30), 9)
            board.make_move(1, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 2, height / 6), 85, 6)
            board.make_move(1, 2)
        move = not move
    # Third square
    if x > width * 2 / 3 and x < width and y > 0 and y < height / 3 and board.square[2] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width * 21 / 30, height / 30), (width * 29 / 30, height * 9 / 30), 9)
            pygame.draw.line(screen, black, (width * 21 / 30, height * 9 / 30), (width * 29 / 30, height / 30), 9)
            board.make_move(2, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width * 5 / 6, height / 6), 85, 6)
            board.make_move(2, 2)
        move = not move
    # Forth square
    if x > 0 and x < width / 3 and y > height / 3 and y < height * 2 / 3 and board.square[3] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width / 30, height * 11 / 30), (width * 9 / 30, height * 19 / 30), 9)
            pygame.draw.line(screen, black, (width / 30, height * 19 / 30), (width * 9 / 30, height * 11 / 30), 9)
            board.make_move(3, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 6, height / 2), 85, 6)
            board.make_move(3, 2)
        move = not move
    # Fifth square
    if x > width / 3 and x < width * 2 / 3 and y > height / 3 and y < height * 2 / 3 and board.square[4] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width * 11 / 30, height * 11 / 30), (width * 19 / 30, height * 19 / 30), 9)
            pygame.draw.line(screen, black, (width * 11 / 30, height * 19 / 30), (width * 19 / 30, height * 11 / 30), 9)
            board.make_move(4, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 2, height / 2), 85, 6)
            board.make_move(4, 2)
        move = not move  
    # Sixth square
    if x > width * 2 / 3 and x < width and y > height / 3 and y < height * 2 / 3:
        pygame.draw.circle(screen, black, (width * 5 / 6, height / 2), 85, 6)
    # Seventh square
    if x > 0 and x < width / 3 and y > height * 2 / 3 and y < height:
        pygame.draw.circle(screen, black, (width / 6, height * 5 / 6), 85, 6)
    # Eighth square
    if x > width / 3 and x < width * 2 / 3 and y > height * 2 / 3 and y < height:
        pygame.draw.circle(screen, black, (width / 2, height * 5 / 6), 85, 6)
    # Ninth square
    if x > width * 2 / 3 and x < width and y > height * 2 / 3 and y < height:
        pygame.draw.circle(screen, black, (width * 5 / 6, height * 5 / 6), 85, 6)

    pygame.display.flip()





