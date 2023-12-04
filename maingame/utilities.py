import pygame
import random
from game_parameters import *
from monster import Monster, monsters
from zombie import Zombie, zombies
from bullets import Bullet, bullets
from bullets2 import Bullet2
from hearts import Heart, hearts

def draw_background(screen):
    # load the tiles from assets folder into surfaces
    background_tile = pygame.image.load("../assets/sprites/Individual Tiles/grass.jpg").convert()
    background_tile.set_colorkey((0, 0, 0))

    # fill the screen with background_tile
    for x in range(0, screen_width, background_tile.get_width()):
        for y in range(0, screen_height, background_tile.get_height()):
            screen.blit(background_tile, (x, y))

    # load game font
    custom_font = pygame.font.Font("../assets/fonts/Minecraft-Regular.otf", 80)
    text = custom_font.render("Shoota", True, (255, 255, 240))
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, 0))

def add_monsters(num_monsters):
    for _ in range(num_monsters):
        monsters.add(Monster(random.randint(screen_width, screen_width * 2),
                          random.randint(tile_size, screen_height - tile_size)))

def add_zombies(num_zombies):
    for _ in range(num_zombies):
        zombies.add(Zombie(random.randint(-screen_width*2,screen_width),
                           random.randint(tile_size,screen_height -tile_size)))

def add_bullets(num_bullets, pos, angle):
    for _ in range(num_bullets):
        bullets.add(Bullet(pos[0],pos[1], angle))

def add_bullets2(num_bullets,pos):
    for _ in range(num_bullets):
        bullets2.add(Bullet2(pos[0],pos[1]))

def add_hearts(num_hearts):
    for _ in range(num_hearts):
        hearts.add(Heart(random.randint(-screen_width*2,screen_width),
                           random.randint(tile_size,screen_height -tile_size)))