import pygame
import os
from global_inst import BLACK, SOUND_FOLDER
from gameloop import GameLoop
#from test import test
#from menu import Menu


# create buttons
def Button(score_list, windows, text, inactive_color, active_color, x, y, w, h, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    click_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "click.wav"))
    click_sound.set_volume(1)
    if x + w > cur[0] > x and y + h > cur[1] > y:
        pygame.draw.rect(windows, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "1":
                click_sound.play()
                GameLoop(score_list)
                #Menu(score_list)
            if action == "2":
                click_sound.play()
                #test(score_list)
                '''leng = len(score_list)
                if leng < 10:
                    while len(score_list) < 10:
                        score_list.append(0)
                    for s in score_list:
                        print(s)
                if leng >= 10:
                    for i in range(10):
                        print(score_list[i])'''
            if action == "3":
                click_sound.play()
                pygame.quit()
    else:
        pygame.draw.rect(windows, inactive_color, (x, y, w, h))
    text_to_button(windows, text, BLACK, x, y, w, h)


# print the text on the buttons
def text_to_button(windows, text, color, x, y, w, h):
    small_font = pygame.font.SysFont("comicsansms", 15, False, False)
    button_text = small_font.render(text, False, color)
    rect = button_text.get_rect()
    rect.center = (x + w / 2, y + h / 2)
    windows.blit(button_text, rect)


