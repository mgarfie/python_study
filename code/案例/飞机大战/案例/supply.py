import pygame
from random import *


class BulletSupply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        self.image = pygame.image.load("images/bullet_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 5
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self. rect.top = randint(0, self.width - self.rect.width), \
                                        -100
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
        self.choice = "bullet"

    def move(self):
        if self.rect.height < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self. rect.top = randint(0, self.width - self.rect.width), \
                                        -100
        if choice([True, False]):
            self.image = pygame.image.load("images/bullet_supply.png").convert_alpha()
            self.choice = "bullet"
        else:
            self.image = pygame.image.load("images/bullet3_supply.png").convert_alpha()
            self.choice = "bullet3"


class BombSupply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        self.image = pygame.image.load("images/bomb_supply.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 5
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        -100
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.height < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        -100

