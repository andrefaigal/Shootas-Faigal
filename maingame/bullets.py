import pygame
from math import cos, sin
from game_parameters import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, bullet_width, bullet_height) #want to make it into an image
        self.x = x
        self.y = y
        self.angle = angle

    def update(self):
        """Move the bullet up the screen."""
        # Update the position of the bullet.
        self.x += bullet_speed * cos(self.angle)
        self.y -= bullet_speed * sin(self.angle)

        # Update the rect position.
        self.rect.x, self.rect.y = self.x, self.y

    def draw_bullet(self, screen):
        """Draw the bullet to the screen."""
        # pygame.draw.rect(screen, BULLET_COLOR, self.rect)
        pygame.draw.circle(screen, bullet_color, self.rect.center, 10)


bullets = pygame.sprite.Group()