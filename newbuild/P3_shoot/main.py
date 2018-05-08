import pygame
import os
from global_inst import *
import datetime
from gameloop import GameLoop


def Menu():
    intro = True
    while intro:
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()

        # create three buttons
        var1 = Button("Start", YELLOW, ORANGE, 50, 310, 100, 50, action="1")
        Button("High Scores", YELLOW, ORANGE, 50, 370, 100, 50, action="2")
        Button("Quit", RED, ORANGE, 50, 430, 100, 50, action="3")

        if var1 == False:
            intro = False

        pygame.display.flip()
    print("quit menu")
    pygame.quit()


def Result(score, time):
    time = str(datetime.timedelta(seconds=time))
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, 300))
    pygame.display.set_caption("Game Over")
    result_font = pygame.font.SysFont("Arial", 20, False, False)
    screen.fill(WHITE)

    text1 = result_font.render("GAME OVER", True, BLACK)
    rect1 = text1.get_rect()
    rect1.center = (WIDTH / 2, 220)
    text2 = result_font.render("Score: " + str(score), False, BLACK)
    text3 = result_font.render("Time: " + time, False, BLACK)

    stay = True
    while stay:
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                stay = False
                pygame.quit()
        print("aaa")
        screen.blit(text1, rect1)
        screen.blit(text2, (100, 240))
        screen.blit(text3, (100, 270))
        #Button("Play Again", YELLOW, ORANGE, 50, 310, 100, 50, action="4")
        #Button("Quit", RED, ORANGE, 50, 430, 100, 50, action="3")

        pygame.display.flip()
    print("quit result")
    pygame.quit()


# create buttons
def Button(text, inactive_color, active_color, x, y, w, h, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    click_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "click.wav"))
    click_sound.set_volume(1)

    if x + w > cur[0] > x and y + h > cur[1] > y:
        pygame.draw.rect(menu, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "1":
                click_sound.play()
                pygame.time.wait(300)
                GameLoop()
                print("quit button")
                return False
            if action == "2":
                click_sound.play()
                pygame.time.wait(300)

            if action == "3":
                click_sound.play()
                pygame.time.wait(300)
                pygame.quit()

    else:
        pygame.draw.rect(menu, inactive_color, (x, y, w, h))
    text_to_button(text, BLACK, x, y, w, h)



# print the text on the buttons
def text_to_button(text, color, x, y, w, h, ):
    small_font = pygame.font.SysFont("Arial", 20, False, False)
    button_text = small_font.render(text, False, color)
    rect = button_text.get_rect()
    rect.center = (x + w / 2, y + h / 2)
    menu.blit(button_text, rect)


if __name__ == "__main__":
    while REPLAY:
        pygame.init()
        pygame.mixer.init()
        menu = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Carrot Time")
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        # set menu background
        menu.fill(WHITE)
        menu_image = pygame.image.load(os.path.join(IMG_FOLDER, "menu.png")).convert()
        menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
        menu.blit(menu_image, (0, 0))
        Menu()
        print("going to result")
        Result(SCORE, MS)

    exit()
