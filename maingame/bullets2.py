import pygame
from game_parameters import *

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        # uploading the png picture of orange fish as forward image
        self.forward_image = pygame.image.load("../assets/sprites/Individual Icons and Particles/Bullet.png").convert()
        self.forward_image.set_colorkey((0, 0, 0))

        # makes orange fish to move opposite direction
        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.up_image = pygame.transform.rotate(self.forward_image, 90)
        self.down_image = pygame.transform.rotate(self.forward_image, -90)

        size = self.forward_image.get_size()
        new_size = (size[0] * .02, size[1] * .02)
        self.forward_image = pygame.transform.scale(self.forward_image, new_size)

        #create a bullet rect at (0,0) and then set correct position

        self.x = x
        self.y = y
        self.angle = angle #chatGPT

    def update(self):

        self.x =x
        self.y = y

        #update the rect position
        self.forward_image.x, self.forward_image.y = self.x,self.y ##maybe its in this??

    def shoot_right(self):
        self.x += bullet_speed

    def shoot_left(self):
        self.x += - bullet_speed

    def shoot_up(self):
        self.y +=bullet_speed

    def shoot_down(self):
        self.y += - bullet_speed

    def draw_bullet(self, screen):
        screen.blit(self.forward_image, self.rect)

bullets2 = pygame.sprite.Group()