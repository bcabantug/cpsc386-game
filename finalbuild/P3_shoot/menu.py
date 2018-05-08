import pygame
import os
from global_inst import *
from button import Button
from gameloop import GameLoop


# game menu
def Menu(score_list):
    pygame.init()
    pygame.mixer.init()
    menu = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Carrot Time")
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    menu_image = pygame.image.load(os.path.join(IMG_FOLDER, "menu.png")).convert()
    menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
    click_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "click.wav"))
    click_sound.set_volume(1)
    big_font = pygame.font.SysFont("Arial", 30, False, False)
    mini_font = pygame.font.SysFont("Arial", 15, False, False)
    menu.fill(WHITE)
    menu.blit(menu_image, (0, 0))

    # create three buttons
    Button(menu, "Start", YELLOW, 50, 310, 100, 50)
    Button(menu, "High Scores", YELLOW, 50, 370, 100, 50)
    Button(menu, "Quit", RED, 50, 430, 100, 50)

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cur = pygame.mouse.get_pos()
                # button 1
                if 50 < cur[0] < 150 and 310 < cur[1] < 360:
                    click_sound.play()
                    Button(menu,  "Start", ORANGE, 50, 310, 100, 50)
                    pygame.display.update()
                    GameLoop(score_list)
                # button 2
                if 50 < cur[0] < 150 and 370 < cur[1] < 420:
                    click_sound.play()
                    Button(menu, "High Scores", ORANGE, 50, 370, 100, 50)
                    pygame.display.update()
                    # get the first 10 high scores
                    leng = len(score_list)
                    if leng < 10:
                        while len(score_list) < 10:
                            score_list.append(0)
                        for s in score_list:
                            print(s)
                    if leng >= 10:
                        for i in range(10):
                            print(score_list[i])
                    # display 10 high scores
                    e = True
                    while e:
                        pygame.draw.rect(menu, ORANGE, (0, 200, WIDTH, 200))
                        title = big_font.render("High Scores", False, BLACK)
                        rect = title.get_rect()
                        rect.center = (WIDTH / 2 - 10, 220)
                        menu.blit(title, rect)
                        text = mini_font.render("Back? Y/N", False, BLACK)
                        rect = text.get_rect()
                        rect.center = (WIDTH / 2 - 10, 380)
                        menu.blit(text, rect)

                        t1 = mini_font.render(str(score_list[0]), False, BLACK)
                        rect = t1.get_rect()
                        rect.center = (200, 250)
                        menu.blit(t1, rect)

                        t2 = mini_font.render(str(score_list[1]), False, BLACK)
                        rect = t2.get_rect()
                        rect.center = (200, 270)
                        menu.blit(t2, rect)

                        t3 = mini_font.render(str(score_list[2]), False, BLACK)
                        rect = t3.get_rect()
                        rect.center = (200, 290)
                        menu.blit(t3, rect)

                        t4 = mini_font.render(str(score_list[3]), False, BLACK)
                        rect = t4.get_rect()
                        rect.center = (200, 310)
                        menu.blit(t4, rect)

                        t5 = mini_font.render(str(score_list[4]), False, BLACK)
                        rect = t5.get_rect()
                        rect.center = (200, 330)
                        menu.blit(t5, rect)

                        t6 = mini_font.render(str(score_list[5]), False, BLACK)
                        rect = t6.get_rect()
                        rect.center = (270, 250)
                        menu.blit(t6, rect)

                        t7 = mini_font.render(str(score_list[6]), False, BLACK)
                        rect = t7.get_rect()
                        rect.center = (270, 270)
                        menu.blit(t7, rect)

                        t8 = mini_font.render(str(score_list[7]), False, BLACK)
                        rect = t8.get_rect()
                        rect.center = (270, 290)
                        menu.blit(t8, rect)

                        t9 = mini_font.render(str(score_list[8]), False, BLACK)
                        rect = t9.get_rect()
                        rect.center = (270, 310)
                        menu.blit(t9, rect)

                        t10 = mini_font.render(str(score_list[9]), False, BLACK)
                        rect = t10.get_rect()
                        rect.center = (270, 330)
                        menu.blit(t10, rect)

                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    Menu(score_list)
                                if event.key == pygame.K_n:
                                    e = False
                # button 3
                if 50 < cur[0] < 150 and 430 < cur[1] < 480:
                    click_sound.play()
                    Button(menu, "Quit", ORANGE, 50, 430, 100, 50)
                    pygame.display.update()
                    pygame.quit()
        pygame.display.update()
    pygame.quit()


