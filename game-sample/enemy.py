import pygame
import os
from global_inst import BLACK, WIDTH, HEIGHT, IMG_FOLDER
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, acc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER, "bunny.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-1000, -100)
        self.acc = acc
        self.speedy = 3 + self.acc

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = 3 + self.acc

