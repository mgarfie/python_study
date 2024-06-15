import pygame
import random
from math import *


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 9
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, width):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

    '''def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 9
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
        self.change_long, self.chang_short = self.rect.width, self.rect.height

    def move(self, width):
        self.rect.top -= self.speed
        self.change_long += 2
        self.chang_short += 2
        self.image = pygame.transform.scale(self.image, (self.change_long, self.chang_short))
        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.change_long, self.chang_short = self.rect.width, self.rect.height'''


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 10
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, width):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class Bullet3(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 5
        self.x_speed = 0
        self.x = 0
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, width):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False
        else:
            self.x_speed += 8
            if self.x_speed > 360:
                self.x_speed = 0
            self.rect.left = self.x + 150 * sin(self.x_speed * pi / 180)

    def reset(self, position):
        self.x, self.rect.top = position
        self.active = True
        self.x_speed = 0


class Bullet4(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 5
        self.x_speed = 0
        self.x = 0
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, width):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False
        else:
            self.x_speed += 8
            if self.x_speed > 360:
                self.x_speed = 0
            self.rect.left = self.x - 150 * sin(self.x_speed * pi / 180)

    def reset(self, position):
        self.x, self.rect.top = position
        self.active = True
        self.x_speed = 0