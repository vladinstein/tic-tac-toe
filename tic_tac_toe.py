import sys, pygame

class Tic_Tac_Toe:
    a = [0] * 9
    A1 = A2 = 'O'
    #def check_win(self):
    #    if self.a1 + self.a2 + self.a3 == 3:
    #        return True
        
    def make_move(self, field, value):
        self.a[field] = value

game = Tic_Tac_Toe()

def draw_grid():
    square_size = 200
    for x in range(3):
        for y in range(3):
            rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
            pygame.draw.rect(screen, black, rect, 3)

#game.make_move(3, 1)
#print(game.a)
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

while True:
    draw_grid()
    x = y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
    # First square 
    if x > 0 and x < width / 3 and y > 0 and y < height/3:
        pygame.draw.circle(screen, black, (width / 6, width / 6), 85, 6)
    # Second square
    if x > width / 3 and x < width * 2 / 3 and y > 0 and y < height / 3:
        pygame.draw.circle(screen, black, (width / 2, width / 6), 85, 6)
    # Third square
    if x > width * 2 / 3 and x < width and y > 0 and y < height / 3:
        pygame.draw.circle(screen, black, (width * 5 / 6, width / 6), 85, 6)
    # Forth square
    if x > 0 and x < width / 3 and y > height / 3 and y < height * 2 / 3:
        pygame.draw.circle(screen, black, (width / 6, width / 2), 85, 6)
    # Fifth square
    if x > width / 3 and x < width * 2 / 3 and y > height / 3 and y < height * 2 / 3:
        pygame.draw.circle(screen, black, (width / 2, width / 2), 85, 6)
    # Sixth square
    if x > width * 2 / 3 and x < width and y > height / 3 and y < height * 2 / 3:
        pygame.draw.circle(screen, black, (width * 5 / 6, width / 2), 85, 6)
    # Seventh square
    if x > 0 and x < width / 3 and y > height * 2 / 3 and y < height:
        pygame.draw.circle(screen, black, (width / 6, width * 5 / 6), 85, 6)
    # Eighth square
    if x > width / 3 and x < width * 2 / 3 and y > height * 2 / 3 and y < height:
        pygame.draw.circle(screen, black, (width / 2, width * 5 / 6), 85, 6)
    # Ninth square
    if x > width * 2 / 3 and x < width and y > height * 2 / 3 and y < height:
        pygame.draw.circle(screen, black, (width * 5 / 6, width * 5 / 6), 85, 6)

    pygame.display.flip()





