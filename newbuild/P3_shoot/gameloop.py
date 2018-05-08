import pygame
from player import Player
from enemy import Enemy
from global_inst import *
import copy #for use with calculating score



def GameLoop():
    score = 0
    acc = 0
    ltime = 0  # last time that there before the next tick of ms since start of game
    #font
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans", 30)
    #load game elements
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Carrot Time!")
    clock = pygame.time.Clock()
    bgm = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "bensound-cute.wav"))
    bgm.set_volume(1)
    feed_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "carrotchew.wav"))
    feed_sound.set_volume(1)
    shoot_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "launch.wav"))
    shoot_sound.set_volume(0.5)
    background = pygame.image.load(os.path.join(IMG_FOLDER, "tmpback.png")).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_position_y = 0
    screen.blit(background, (0, 0))
    #creat player sprite
    player = Player()
    ALL_SPRITES.add(player)
    #create bunny sprites
    for i in range(8):
        enemy = Enemy(acc)
        ALL_SPRITES.add(enemy)
        ENEMIES.add(enemy)

    #game main loop
    running = True
    bgm.play(-1)
    while running:
        clock.tick_busy_loop(FPS) #gets the total ms since init

        ms = int(pygame.time.get_ticks()/1000) #get total amount of seconds passed since init

        if(ms-ltime>=1): #if a second has passed
            score = score + 1 #add 1 to the score
            SCORE = score
            print("Score: ", score)

        ltime = copy.deepcopy(ms) #copys the ms that has passed so that it can keep track of seconds passed
        MS = ms
        # Events:
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot_sound.play()
                    player.shoot()

        # Update:
        ALL_SPRITES.update()

        # check hit between ENEMIES and BULLETS groups
        hit1 = pygame.sprite.groupcollide(ENEMIES, BULLETS, True, True)
        # if hit,
        for hit in hit1:
            feed_sound.play()
            # bunnies will accelerate their speeds when getting more scores
            score += 10
            SCORE = score
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
            bgm.stop()
            running = False
            print("end out of game")
        # Draw updates:
        screen.fill(WHITE)

        #scrolling background
        check_y = background_position_y % background.get_rect().height
        screen.blit(background, (0, check_y - background.get_rect().height))
        if check_y < HEIGHT:
            screen.blit(background, (0, check_y))
        background_position_y += 1

        ALL_SPRITES.draw(screen)

        #score
        scoretext = myfont.render("Score: " + str(score), False, ORANGE)
        screen.blit(scoretext, (20, 20))

        pygame.display.flip()
    print("quit game loop")

