import pygame
from global_inst import *
from player import Player
from enemy import Enemy
import copy #for use with calculating score
from menu import *
from highscores import *



def GameLoop(scores):
    score = 0
    acc = 0

    #font
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans", 30)
    scoretext = myfont.render("Score: " + str(score),False ,ORANGE)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Carrot Time!")
    clock = pygame.time.Clock()

    # NEED A BACKGROUND IMAGE
    background = pygame.image.load(os.path.join(IMG_FOLDER, "tmpback.png")).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_position_y = 0

    player = Player()
    ALL_SPRITES.add(player)

    for i in range(8):
        enemy = Enemy(acc)
        ALL_SPRITES.add(enemy)
        ENEMIES.add(enemy)

    ltime = 0 #last time that there before the next tick of ms since start of game
    bgm.play(-1)

    running = True
    while running:
        clock.tick_busy_loop(FPS) #gets the total ms since init

        ms = int(pygame.time.get_ticks()/1000) #get total amount of seconds passed since init

        if(ms-ltime>=1): #if a second has passed
            score += 1 #add 1 to the score
            print("Score: ", score)

        ltime = copy.deepcopy(ms) #copys the ms that has passed so that it can keep track of seconds passed


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
            #feed_sound.play()
            score += 10
            print("Score: ", score)
            if 250 <= score < 500:
                acc = 1
            if 500 <= score < 750:
                acc = 2
            if 750 <= score < 1250:
                acc = 3
            if score >= 1250 < 2250:
                acc = 4
            if score >= 2250 < 3500:
                acc = 5
            if score >= 3500 < 5000:
                acc = 6
            if score >= 5000 < 10000:
                acc = 7
            # create a new bunny
            enemy = Enemy(acc)
            ALL_SPRITES.add(enemy)
            ENEMIES.add(enemy)

        # check hit between player and ENEMIES
        hit2 = pygame.sprite.spritecollide(player, ENEMIES, False)
        if hit2:
            #pass
            print("GAME OVER")
            #print(score)
            # if not scoreslist:
            #     scoreslist  = [1,2,3]
            for i in scores:
                print(i)
            addScore(score, scores)
            saveScores(scores)
            bgm.stop()

            running = False


        # Draw updates:
        screen.fill(WHITE)

        # scrolling background
        check_y = background_position_y % background.get_rect().height
        screen.blit(background, (0, check_y - background.get_rect().height))
        if check_y < HEIGHT:
            screen.blit(background, (0, check_y))
        background_position_y += 1

        ALL_SPRITES.draw(screen)

        #score
        scoretext = myfont.render("Score: " + str(score),False ,ORANGE)
        screen.blit(scoretext, (20,20))

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    scoreslist = loadFile()
    for i in scoreslist:
        print(i)
    print("end read")
    menu = pygame.display.set_mode((WIDTH, HEIGHT))
    Menu(scoreslist)
    quit()
