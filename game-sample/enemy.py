import pygame
import os
from global_inst import YELLOW, WIDTH, HEIGHT, IMG_FOLDER
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER, "bunny.png")).convert()
        #self.image = pygame.Surface((50, 40))
        # self.image.x = random.randrange(WIDTH-self.image.width)
        # self.image.y = random.randrange(-100, -100)
        # self.speedx = random.randrange(-3, 3)
        # self.speedy = random.randrange(1, 8)
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 8)




    def update(self):
        # self.image.x += self.speedx
        # self.image.y += self.speedy
        # if self.image.top > HEIGHT + 10 or self.image.left < -25 or self.image.right > WIDTH + 20:
        #     self.image.x = random.randrange(WIDTH - self.image.width)
        #     self.image.y = random.randrange(-100, -40)
        #     self.speedy = random.randrange(1, 8)
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
