import sys, pygame
from copy import deepcopy
from random import randrange

class Tic_Tac_Toe:
    def __init__(self):
        self.square = [0] * 9

    def try_move(self, i, move):
        """
        Function that tries a move for a computer. (To see if it's winning etc)
        """
        if self.square[i] == 0:
            if move == True:
                self.square[i] = 1
            else:
                self.square[i] = 4
    
    def try_opp_move(self, i, move):
        """
        Function that tries a move for a computer's opponent (human). 
        (To see if it's winning etc and react accordingly)
        """
        if self.square[i] == 0:
            if move == True:
                self.square[i] = 4
            else:
                self.square[i] = 1

    def make_move_comp(self, i, move, player_move):
        """
        Function that makes a move for computer.
        """
        if self.square[i] == 0:
            if move == True:
                self.square[i] = 1
            else:
                self.square[i] = 4
        move = not move
        player_move = not player_move
        return move, player_move

    def make_winning_move(self, move, player_move):
        for i in range(9):
            board_comp = deepcopy(self)
            board_comp.try_move(i, move)
            _, game_over = board_comp.check_win()
            if game_over:
                move, player_move = board.make_move_comp(i, move, player_move)
                pygame.time.wait(500)
                break
        return move, player_move
    
    def make_fork(self, move, player_move):
        """
        Computer makes a fork move if possible (guaranteed win in the next move).

        Try one move (A) (using a copy of an object). Then try all possible moves (B, C, D ...) with that move. 
        If there's more than one winning move after the move A: (B or C or D e t.c. ...), make the move A.
        """
        for i in range(9):
            board_comp = deepcopy(self)
            board_comp.try_move(i, move)
            find = False
            count = 0
            for j in range(9):
                board_comp_2 = deepcopy(board_comp)
                board_comp_2.try_move(j, move)
                _, game_over = board_comp_2.check_win()
                if game_over:
                    count += 1
                if count > 1:
                    print("Fork")
                    move, player_move = board.make_move_comp(i, move, player_move)
                    pygame.time.wait(500)
                    find = True
                    break
            if find:
                break
        return move, player_move
    
    def block_fork(self, move, player_move):
        """
        Defending against a fork (if there's only one fork).
        In progress: multiple forks defence or counter-attack.
        """
        fork_count = 0
        forks = []
        for i in range(9):
            board_comp = deepcopy(self)
            board_comp.try_opp_move(i, move)
            find = False
            count = 0
            for j in range(9):
                board_comp_2 = deepcopy(board_comp)
                board_comp_2.try_opp_move(j, move)
                _, game_over = board_comp_2.check_win()
                if game_over:
                    count += 1
                if count > 1:
                    fork_count += 1
                    forks.append(i)
                    print(fork_count)
                    print(f"Fork alert:{i}")
                    break
        if fork_count == 1:
            move, player_move = board.make_move_comp(forks[0], move, player_move)
            pygame.time.wait(500)
        return move, player_move

    def make_random_move(self, move, player_move):
        """
        Function to make a random move
        """
        while True:
            i = randrange(9)
            if self.square[i] == 0:
                if move == True:
                    self.square[i] = 1
                    break
                else:
                    self.square[i] = 4
                    break
        move = not move
        player_move = not player_move
        return move, player_move

    def make_move(self, tiles, move, player_move):
        """
        Function to write down a move inside a list.
        """
        # i-th square
        for i in range(9):
            if tiles[i].collidepoint(x, y) and self.square[i] == 0:
                if move == True and player_move == True:
                    # Add first player's move to the list.
                    self.square[i] = 1
                if move == False and player_move == True:
                    # Add second player's move to the list.
                    self.square[i] = 4
                if game_state == "game_comp_x" or game_state == "game_comp_o":
                    player_move = not player_move
                move = not move
        return move, player_move

    def check_win(self):
        """
        This function checks if there is a winner, who is a winner and what line it's on.
        It returns the line number and the winner number.
        """
        line = None
        game_over = False
        for i in range(0, 7, 3):
            if self.square[i] + self.square[i+1] + self.square[i+2] == 3:
                line = i / 3
                game_over = True
            elif self.square[i] + self.square[i+1] + self.square[i+2] == 12:
                line = i / 3
                game_over = True
        for i in range(3):
            if self.square[i] + self.square[i+3] + self.square[i+6] == 3:
                line = i + 3
                game_over = True
            elif self.square[i] + self.square[i+3] + self.square[i+6] == 12:
                line = i + 3
                game_over = True
        if self.square[0] + self.square[4] + self.square[8] == 3:
            line = 6
            game_over = True
        elif self.square[0] + self.square[4] + self.square[8] == 12:
            line = 6
            game_over = True
        if self.square[2] + self.square[4] + self.square[6] == 3:
            line = 7
            game_over = True
        elif self.square[2] + self.square[4] + self.square[6] == 12:
            line = 7
            game_over = True
        return line, game_over


size = width, height = 600, 600
red = 255, 0, 0
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 128
# These are the colors for the menu, they get changed on mouseover
color_button_1 = white
color_button_2 = white

screen = pygame.display.set_mode(size)
# What does this do?
clock = pygame.time.Clock()

# move = True is for crosses, move = False for zeros.
move = True
board = Tic_Tac_Toe()
game_state = "start_menu"
game_over = False
player_move = True

def draw_menu():
    """
    Function that draws a start/choice menu.
    """
    if game_state == "start_menu":
        string_1, string_2 = "Play against the computer", "Play against each other"
    else:
        string_1, string_2 = "X", "O"
    screen.fill(black)
    font = pygame.font.SysFont('arial', 40)
    title = font.render("Tic Tac Toe", True, white)
    start_comp = font.render(string_1, True, color_button_1, black)
    start_human = font.render(string_2, True, color_button_2, black)
    rect_comp = start_comp.get_rect(topleft=(width / 2 - start_comp.get_width() / 2, height / 2))
    rect_human = start_human.get_rect(topleft=(width / 2 - start_human.get_width() / 2, 
                                               height / 2 + title.get_height() * 2))
    screen.blit(title, (width / 2 - title.get_width() / 2, height / 2 - title.get_height() * 2))
    screen.blit(start_comp, rect_comp)
    screen.blit(start_human, rect_human)
    pygame.display.update()
    return rect_comp, rect_human

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

def draw_moves():
        # Draw cross or circle depending on what's in the moves list.
    if board.square[0] == 1:
        pygame.draw.line(screen, black, (width / 30, height / 30), (width * 9 / 30, height * 9 / 30), 9)
        pygame.draw.line(screen, black, (width / 30, height * 9 / 30), (width * 9 / 30, height / 30), 9)
    elif board.square[0] == 4:                
        pygame.draw.circle(screen, black, (width / 6, height / 6), 85, 6)
    if board.square[1] == 1:
        pygame.draw.line(screen, black, (width * 11 / 30, height / 30), (width * 19 / 30, height * 9 / 30), 9)
        pygame.draw.line(screen, black, (width * 11 / 30, height * 9 / 30), (width * 19 / 30, height / 30), 9)
    elif board.square[1] == 4:
        pygame.draw.circle(screen, black, (width / 2, height / 6), 85, 6)
    if board.square[2] == 1:
        pygame.draw.line(screen, black, (width * 21 / 30, height / 30), (width * 29 / 30, height * 9 / 30), 9)
        pygame.draw.line(screen, black, (width * 21 / 30, height * 9 / 30), (width * 29 / 30, height / 30), 9)
    elif board.square[2] == 4:
        pygame.draw.circle(screen, black, (width * 5 / 6, height / 6), 85, 6)
    if board.square[3] == 1:
        pygame.draw.line(screen, black, (width / 30, height * 11 / 30), (width * 9 / 30, height * 19 / 30), 9)
        pygame.draw.line(screen, black, (width / 30, height * 19 / 30), (width * 9 / 30, height * 11 / 30), 9)
    elif board.square[3] == 4:
        pygame.draw.circle(screen, black, (width / 6, height / 2), 85, 6)
    if board.square[4] == 1:
        pygame.draw.line(screen, black, (width * 11 / 30, height * 11 / 30), (width * 19 / 30, height * 19 / 30), 9)
        pygame.draw.line(screen, black, (width * 11 / 30, height * 19 / 30), (width * 19 / 30, height * 11 / 30), 9)
    elif board.square[4] == 4:
        pygame.draw.circle(screen, black, (width / 2, height / 2), 85, 6)
    if board.square[5] == 1:
        pygame.draw.line(screen, black, (width * 21 / 30, height * 11 / 30), (width * 29 / 30, height * 19 / 30), 9)
        pygame.draw.line(screen, black, (width * 21 / 30, height * 19 / 30), (width * 29 / 30, height * 11 / 30), 9)
    elif board.square[5] == 4:
        pygame.draw.circle(screen, black, (width * 5 / 6, height / 2), 85, 6)
    if board.square[6] == 1:
        pygame.draw.line(screen, black, (width / 30, height * 21 / 30), (width * 9 / 30, height * 29 / 30), 9)
        pygame.draw.line(screen, black, (width / 30, height * 29 / 30), (width * 9 / 30, height * 21 / 30), 9)
    elif board.square[6] == 4:
        pygame.draw.circle(screen, black, (width / 6, height * 5 / 6), 85, 6)
    if board.square[7] == 1:
        pygame.draw.line(screen, black, (width * 11 / 30, height * 21 / 30), (width * 19 / 30, height * 29 / 30), 9)
        pygame.draw.line(screen, black, (width * 11 / 30, height * 29 / 30), (width * 19 / 30, height * 21/ 30), 9)
    elif board.square[7] == 4:
        pygame.draw.circle(screen, black, (width / 2, height * 5 / 6), 85, 6)
    if board.square[8] == 1:
        pygame.draw.line(screen, black, (width * 21 / 30, height * 21 / 30), (width * 29 / 30, height * 29 / 30), 9)
        pygame.draw.line(screen, black, (width * 21 / 30, height * 29 / 30), (width * 29 / 30, height * 21/ 30), 9)
    elif board.square[8] == 4:
        pygame.draw.circle(screen, black, (width * 5 / 6, height * 5 / 6), 85, 6)

def draw_win():
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

pygame.init()

while True:
    x = y = -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
    if game_state == "start_menu" or game_state == "choose_menu":
        button_1, button_2 = draw_menu()
        # Change the color of the menu buttons on mouseover.
        if button_2.collidepoint(pygame.mouse.get_pos()):
            color_button_2 = blue
        else:
            color_button_2 = white
        if button_1.collidepoint(pygame.mouse.get_pos()):
            color_button_1 = blue
        else:
            color_button_1 = white
        # Action if the button is pressed.
        if button_2.collidepoint(x, y) and game_state == "start_menu":
            game_state = "game"
            x = y = -1
        if button_1.collidepoint(x, y) and game_state == "start_menu":
            game_state = "choose_menu"
            x = y = -1
        if button_1.collidepoint(x, y) and game_state == "choose_menu":
            game_state = "game_comp_x"
            x = y = -1
        if button_2.collidepoint(x, y) and game_state == "choose_menu":
            game_state = "game_comp_o"
            x = y = -1
            player_move = False
    # Playing with each other.
    if game_state == "game":
        screen.fill(white)
        tiles = draw_grid()
        if not game_over:
            move, _ = board.make_move(tiles, move, player_move)
        draw_moves()
        # Check if there's a winner and what line it's on
        line, game_over = board.check_win()
        draw_win()
    # This is for playing against computer
    if game_state == "game_comp_x" or game_state == "game_comp_o":
        screen.fill(white)
        tiles = draw_grid()
        # Player's move
        if not game_over and player_move:
            move, player_move = board.make_move(tiles, move, player_move)
        elif not game_over and not player_move:
            # Winning move (computer) if there is one.
            move, player_move = board.make_winning_move(move, player_move)
            # A move to prevent human from winning (if he can win in the next move).
            if not player_move:
                for i in range(9):
                    board_comp = deepcopy(board)
                    board_comp.try_opp_move(i, move)
                    _, game_over = board_comp.check_win()
                    if game_over:
                        move, player_move = board.make_move_comp(i, move, player_move)
                        pygame.time.wait(500)
                        break
            # Fork move if there is one.
            if not player_move:
                    move, player_move = board.make_fork(move, player_move)
            # Defend against fork move if there is one.
            if not player_move:
                    move, player_move = board.block_fork(move, player_move)
            # Random move
            if not player_move:
                print('random')
                move, player_move = board.make_random_move(move, player_move)
                pygame.time.wait(500)
        draw_moves()
        # Check if there's a winner and what line it's on
        line, game_over = board.check_win()
        draw_win()

    pygame.display.flip()





