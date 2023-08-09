import sys, pygame

class Tic_Tac_Toe:
    square = [0] * 9

    def make_move(self, number, value):
        """
        Function to write down a move inside a list.
        """
        self.square[number] = value

    def check_win(self):
        """
        This function checks if there is a winner, who is a winner and what line it's on.
        It returns the line number and the winner number.
        """
        line = None
        victory = None
        for i in range(0, 7, 3):
            if self.square[i] + self.square[i+1] + self.square[i+2] == 3:
                line = i / 3
                victory = 0
            if self.square[i] + self.square[i+1] + self.square[i+2] == 12:
                line = i / 3
                victory = 1
        for i in range(3):
            if self.square[i] + self.square[i+3] + self.square[i+6] == 3:
                line = i + 3
                victory = 0
            if self.square[i] + self.square[i+3] + self.square[i+6] == 12:
                line = i + 3
                victory = 1
        if self.square[0] + self.square[4] + self.square[8] == 3:
                line = 6
                victory = 0
        if self.square[0] + self.square[4] + self.square[8] == 12:
                line = 6
                victory = 1
        if self.square[2] + self.square[4] + self.square[6] == 3:
                line = 7
                victory = 0
        if self.square[2] + self.square[4] + self.square[6] == 12:
                line = 7
                victory = 1
        return line, victory

def draw_grid():
    """
    Function that draws a grid.
    """
    rects = []
    square_size = 200
    for y in range(3):
        for x in range(3): 
            rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
            rects.append(rect)
            pygame.draw.rect(screen, black, rect, 3)
    return rects 

pygame.init()

size = width, height = 600, 600
red = 255, 0, 0
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
# What does this do?
clock = pygame.time.Clock()

screen.fill(white)
move = True
board = Tic_Tac_Toe()


while True:
    tiles = draw_grid()
    x = y = -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
    # First square
    if tiles[0].collidepoint(x, y) and board.square[0] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width / 30, height / 30), (width * 9 / 30, height * 9 / 30), 9)
            pygame.draw.line(screen, black, (width / 30, height * 9 / 30), (width * 9 / 30, height / 30), 9)
            board.make_move(0, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 6, height / 6), 85, 6)
            board.make_move(0, 4)
        move = not move
    # Second square
    if tiles[1].collidepoint(x, y) and board.square[1] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width * 11 / 30, height / 30), (width * 19 / 30, height * 9 / 30), 9)
            pygame.draw.line(screen, black, (width * 11 / 30, height * 9 / 30), (width * 19 / 30, height / 30), 9)
            board.make_move(1, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 2, height / 6), 85, 6)
            board.make_move(1, 4)
        move = not move
    # Third square
    if tiles[2].collidepoint(x, y) and board.square[2] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width * 21 / 30, height / 30), (width * 29 / 30, height * 9 / 30), 9)
            pygame.draw.line(screen, black, (width * 21 / 30, height * 9 / 30), (width * 29 / 30, height / 30), 9)
            board.make_move(2, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width * 5 / 6, height / 6), 85, 6)
            board.make_move(2, 4)
        move = not move
    # Forth square
    if tiles[3].collidepoint(x, y) and board.square[3] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width / 30, height * 11 / 30), (width * 9 / 30, height * 19 / 30), 9)
            pygame.draw.line(screen, black, (width / 30, height * 19 / 30), (width * 9 / 30, height * 11 / 30), 9)
            board.make_move(3, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 6, height / 2), 85, 6)
            board.make_move(3, 4)
        move = not move
    # Fifth square
    if tiles[4].collidepoint(x, y) and board.square[4] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width * 11 / 30, height * 11 / 30), (width * 19 / 30, height * 19 / 30), 9)
            pygame.draw.line(screen, black, (width * 11 / 30, height * 19 / 30), (width * 19 / 30, height * 11 / 30), 9)
            board.make_move(4, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 2, height / 2), 85, 6)
            board.make_move(4, 4)
        move = not move  
    # Sixth square
    if tiles[5].collidepoint(x, y) and board.square[5] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width * 21 / 30, height * 11 / 30), (width * 29 / 30, height * 19 / 30), 9)
            pygame.draw.line(screen, black, (width * 21 / 30, height * 19 / 30), (width * 29 / 30, height * 11 / 30), 9)
            board.make_move(5, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width * 5 / 6, height / 2), 85, 6)
            board.make_move(5, 4)
        move = not move 
    # Seventh square
    if tiles[6].collidepoint(x, y) and board.square[6] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width / 30, height * 21 / 30), (width * 9 / 30, height * 29 / 30), 9)
            pygame.draw.line(screen, black, (width / 30, height * 29 / 30), (width * 9 / 30, height * 21 / 30), 9)
            board.make_move(6, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 6, height * 5 / 6), 85, 6)
            board.make_move(6, 4)
        move = not move
    # Eighth square
    if tiles[7].collidepoint(x, y) and board.square[7] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width * 11 / 30, height * 21 / 30), (width * 19 / 30, height * 29 / 30), 9)
            pygame.draw.line(screen, black, (width * 11 / 30, height * 29 / 30), (width * 19 / 30, height * 21/ 30), 9)
            board.make_move(7, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width / 2, height * 5 / 6), 85, 6)
            board.make_move(7, 4)
        move = not move
    # Ninth square
    if tiles[8].collidepoint(x, y) and board.square[8] == 0:
        if move == True:
            # If it's a first player's move, draw a cross
            pygame.draw.line(screen, black, (width * 21 / 30, height * 21 / 30), (width * 29 / 30, height * 29 / 30), 9)
            pygame.draw.line(screen, black, (width * 21 / 30, height * 29 / 30), (width * 29 / 30, height * 21/ 30), 9)
            board.make_move(8, 1)
        if move == False:
            # Otherwise draw a circle
            pygame.draw.circle(screen, black, (width * 5 / 6, height * 5 / 6), 85, 6)
            board.make_move(8, 4)
        move = not move
    # Check if there's a winner and what line it's on
    line, victory = board.check_win()
    # Draw a winning line.
    match line:
        case 0:
            pygame.draw.line(screen, red, (width / 30, height / 6), (width * 29 / 30, height / 6), 9)
        case 1:
            pygame.draw.line(screen, red, (width / 30, height / 2), (width * 29 / 30, height / 2), 9)
        case 2:
            pygame.draw.line(screen, red, (width / 30, height * 5 / 6), (width * 29 / 30, height * 5 / 6), 9)
        case 3:
            pygame.draw.line(screen, red, (width / 6, height / 30), (width / 6, height * 29 / 30), 9)
        case 4:
            pygame.draw.line(screen, red, (width / 2, height / 30), (width / 2, height * 29 / 30), 9)
        case 5:
            pygame.draw.line(screen, red, (width * 5 / 6, height / 30), (width * 5 / 6, height * 29 / 30), 9)
        case 6:
            pygame.draw.line(screen, red, (width / 30, height / 30), (width * 29 / 30, height * 29 / 30), 9)
        case 7:
            pygame.draw.line(screen, red, (width / 30, height * 29 / 30), (width * 29 / 30, height / 30), 9)
    pygame.display.flip()





