<<<<<<< HEAD
# import pygame
# from global_inst import *
# #from player_ai import Player_vs_AI
# #from player_player import Player_vs_Player
#
#
# # print the text on the buttons
# def text_to_button(text, color, x, y, w, h, ):
#     small_font = pygame.font.SysFont("Arial", 20, False, False)
#     button_text = small_font.render(text, False, color)
#     rect = button_text.get_rect()
#     rect.center = (x + w / 2, y + h / 2)
#     menu.blit(button_text, rect)
#
#
# # create buttons
# def button(text, inactive_color, active_color, x, y, w, h, action=None):
#     cur = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     if x + w > cur[0] > x and y + h > cur[1] > y:
#         pygame.draw.rect(menu, active_color, (x, y, w, h))
#         if click[0] == 1 and action != None:
#             if action == "1":
#                 bgm.stop()
#                 click_sound.play()
#                 pygame.time.wait(300)
#                 Player_vs_AI()
#             if action == "2":
#                 bgm.stop()
#                 click_sound.play()
#                 pygame.time.wait(300)
#                 Player_vs_Player()
#             if action == "3":
#                 bgm.stop()
#                 click_sound.play()
#                 pygame.time.wait(300)
#                 pygame.quit()
#     else:
#         pygame.draw.rect(menu, inactive_color, (x, y, w, h))
#     text_to_button(text, black, x, y, w, h)
#
#
# def main():
#     # load texts
#     large_font = pygame.font.SysFont("Arial", 60, False, False)
#     menu_text = large_font.render("BUNNY RUN", True, black)
#     menu_text_rect = menu_text.get_rect()
#     menu_text_rect.center = (width / 2, 100)
#     menu.blit(menu_text, menu_text_rect)
#
#     intro = True
#     while intro:
#         # process input (events)
#         for event in pygame.event.get():
#             # check for closing the window
#             if event.type == pygame.QUIT:
#                 intro = False
#                 pygame.quit()
#
#         # create three buttons
#         button("Play Game", yellow, dark_yellow, 300, 200, 200, 80, action="1")
#         button("High Scores", yellow, dark_yellow, 300, 320, 200, 80, action="2")
#         button("Quit", red, dark_red, 300, 440, 200, 80, action="3")
#
#         pygame.display.flip()
#
#
# if __name__ == "__main__":
#     pygame.init()
#     pygame.mixer.init()
#     menu = pygame.display.set_mode((width, height))
#     pygame.display.set_caption("Menu")
#     pygame.event.set_blocked(pygame.MOUSEMOTION)
#     # set menu background
#     menu.fill(white)
#     background = pygame.image.load(os.path.join(img_folder, "background.png")).convert()
#     background = pygame.transform.scale(background, (width, height))
#     bg_rect = background.get_rect()
#     bg_rect.center = (width / 2, height / 2)
#     menu.blit(background, bg_rect)
#     click_sound = pygame.mixer.Sound(os.path.join(sound_folder, "click.wav"))
#     click_sound.set_volume(1)
#     bgm = pygame.mixer.Sound(os.path.join(sound_folder, "bgm.wav"))
#     bgm.play(-1)
#     main()
#     quit()
=======
import pygame
import os
from global_inst import *
from main import *
from highscores import *

menu = pygame.display.set_mode((WIDTH, HEIGHT))


# print the text on the buttons
def text_to_button(text, color, x, y, w, h):
    small_font = pygame.font.SysFont("Arial", 20, False, False)
    button_text = small_font.render(text, False, color)
    rect = button_text.get_rect()
    rect.center = (x + w / 2, y + h / 2)
    menu.blit(button_text, rect)

def Menu(scores):
    pygame.display.set_caption("Menu")
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    # set menu background
    menu.fill(WHITE)
    background = pygame.image.load(os.path.join(IMG_FOLDER, "background.png")).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    bg_rect = background.get_rect()
    bg_rect.center = (WIDTH / 2, HEIGHT / 2)
    menu.blit(background, bg_rect)
    bgm.play(-1)
    MenuDisplay(scores)
    # main()
    # quit()

# create buttons
def button(scores, text, inactive_color, active_color, x, y, w, h, action=None):

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > cur[0] > x and y + h > cur[1] > y:
        pygame.draw.rect(menu, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "1":
                bgm.stop()
                # click_sound.play()
                pygame.time.wait(300)
                GameLoop(scores)
            if action == "2":
                bgm.stop()
                # click_sound.play()
                pygame.time.wait(300)
                # Player_vs_Player()
            if action == "3":
                bgm.stop()
                # click_sound.play()
                pygame.time.wait(300)
                pygame.quit()
    else:
        pygame.draw.rect(menu, inactive_color, (x, y, w, h))
    text_to_button(text, BLACK, x, y, w, h)

def MenuDisplay(scores):
    # load texts
    large_font = pygame.font.SysFont("Arial", 30, False, False)
    menu_text = large_font.render("CARROT TIME!", True, BLACK)
    menu_text_rect = menu_text.get_rect()
    menu_text_rect.center = (WIDTH / 2, 100)
    menu.blit(menu_text, menu_text_rect)

    intro = True
    while intro:
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()

        # create three buttons
        button(scores, "Start", YELLOW, ORANGE, 100, 200, 200, 80, action="1")
        button(scores, "High Scores", YELLOW, ORANGE, 100, 320, 200, 80, action="2")
        button(scores, "Quit", RED, ORANGE, 100, 440, 200, 80, action="3")

        pygame.display.flip()
>>>>>>> e38f955888740a3d5ac362a988f9ad473189f953
