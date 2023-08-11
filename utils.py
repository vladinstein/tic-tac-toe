import sys, pygame

def draw_start_menu():
    """
    Function that draws a start menu.
    """
    screen.fill(black)
    font = pygame.font.SysFont('arial', 40)
    title = font.render("Tic Tac Toe", True, white)
    start_comp = font.render("Play against the computer", True, color_comp, black)
    start_human = font.render("Play against each other", True, color_human, black)
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

