import pygame
from global_inst import *
from bunny import Bunny
from enemy import Enemy
import copy


def GameLoop():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My game")
    clock = pygame.time.Clock()

    my_font = pygame.font.SysFont("Calibri", 50, True, False)
    score = 0;

    # score = 0;
    # scoretext = small_font.render("Score: " + str(score), 1, RED)

    player = Bunny()
    ALL_SPRITES.add(player)
    for i in range(8):
        enemy = Enemy()
        ALL_SPRITES.add(enemy)
        ENEMIES.add(enemy)

    text_player_name = my_font.render("YOU", False, RED)

    ltime=0

    running = True
    while running:

        clock.tick_busy_loop(FPS)
        #clock.tick(FPS)
        #ms = clock.get_time()
        ms = int(pygame.time.get_ticks()/1000)

        #print (ms-ltime)

        if (ms-ltime >=1):
            score = score + 1
            print(score)

        ltime = copy.deepcopy(ms)

        # screen.blit(scoretext, (5, 10));
        # Events:
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Update:
        ALL_SPRITES.update()
        # check hit between ENEMIES and BULLETS groups
        hit1 = pygame.sprite.groupcollide(ENEMIES, BULLETS, True, True)
        # if hit, create a new enemy
        for hit in hit1:
            score = score + 10
            print("score:"+ str(score))
            enemy = Enemy()
            ALL_SPRITES.add(enemy)
            ENEMIES.add(enemy)

        # check hit between player and ENEMIES
        hit2 = pygame.sprite.spritecollide(player, ENEMIES, False)
        if hit2:
            print("GAME OVER")
            running = False

        # Draw updates:
        screen.fill(WHITE)
        ALL_SPRITES.draw(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    GameLoop()
    quit()
