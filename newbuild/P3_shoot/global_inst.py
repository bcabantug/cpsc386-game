import os
import pygame

REPLAY = True
SCORE = 0
MS = 0
WIDTH = 480
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, "img")
SOUND_FOLDER = os.path.join(GAME_FOLDER, "sound")
# sprite group
ALL_SPRITES = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()
ENEMIES = pygame.sprite.Group()
