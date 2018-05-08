import pygame
import os
from global_inst import *
from button import Button


def Menu(score_list):
    pygame.init()
    pygame.mixer.init()
    menu = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Carrot Time")
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    menu_image = pygame.image.load(os.path.join(IMG_FOLDER, "menu.png")).convert()
    menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
    menu.fill(WHITE)
    menu.blit(menu_image, (0, 0))

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
        pygame.display.update()

        # create three buttons
        Button(score_list, menu, "Start", YELLOW, ORANGE, 50, 310, 100, 50, action='1')
        Button(score_list, menu, "High Scores", YELLOW, ORANGE, 50, 370, 100, 50, action='2')
        Button(score_list, menu, "Quit", RED, ORANGE, 50, 430, 100, 50, action='3')
    pygame.quit()


