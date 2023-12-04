#this code will move a heart across the screen after every level

import pygame
import random
from game_parameters import *

class Heart(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/Individual Icons and Particles/minceraftheart.png").convert()

        # self.reverse_image = pygame.transform.flip(self.forward_image, True, False)

        # size = self.image.get_size()
        # new_size = (size[0] * .2, size[1] * .2)
        # self.image = pygame.transform.scale(self.image, new_size)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.x =x
        self.y = y
        self.speed = random.uniform(heart_speed_min,heart_speed_max)
        self.rect.center = (x,y)

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)


hearts = pygame.sprite.Group()