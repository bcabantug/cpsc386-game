import os
import pygame



WIDTH = 480
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, "img")
SOUND_FOLDER = os.path.join(GAME_FOLDER, "sound")
# sprite group
ALL_SPRITES = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()
ENEMIES = pygame.sprite.Group()

#test
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
shoot_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "launch.wav"))
shoot_sound.set_volume(1)

bgm = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "bensound-cute.wav"))
bgm.set_volume(1)

# feed_sound = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "carrotchew.wav"))
# feed_sound.set_volume(1)
#
