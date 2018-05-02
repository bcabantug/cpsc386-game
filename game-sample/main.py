import pygame
from global_inst import *
from player import Player
from enemy import Enemy


def GameLoop():
    score = 0
    acc = 0
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My game")
    clock = pygame.time.Clock()
    # NEED A BACKGROUND IMAGE
    background = pygame.image.load(os.path.join(IMG_FOLDER, "background.png")).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_position_y = 0

    player = Player()
    ALL_SPRITES.add(player)

    for i in range(8):
        enemy = Enemy(acc)
        ALL_SPRITES.add(enemy)
        ENEMIES.add(enemy)

    running = True
    while running:
        clock.tick(FPS)
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
        # if hit,
        for hit in hit1:
            # bunnies will accelerate their speeds when getting more scores
            score += 1
            print("Score: ", score)
            if 5 <= score < 10:
                acc = 1
            if 10 <= score < 15:
                acc = 2
            if 15 <= score < 20:
                acc = 3
            if score >= 20:
                acc = 4
            # create a new bunny
            enemy = Enemy(acc)
            ALL_SPRITES.add(enemy)
            ENEMIES.add(enemy)

        # check hit between player and ENEMIES
        hit2 = pygame.sprite.spritecollide(player, ENEMIES, False)
        if hit2:
            pass
            #print("GAME OVER")
            #running = False

        # Draw updates:
        screen.fill(WHITE)
        # scrolling background
        check_y = background_position_y % background.get_rect().height
        screen.blit(background, (0, check_y - background.get_rect().height))
        if check_y < HEIGHT:
            screen.blit(background, (0, check_y))
        background_position_y += 1

        ALL_SPRITES.draw(screen)


        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    GameLoop()
    quit()
