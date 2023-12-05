import pygame
import random
import time
import sys
from math import atan2

#the modules I created with functions and classes that I am importing:
from game_parameters import *
from bullets import Bullet, bullets, bullets2
from monster import monsters
from zombie import zombies, Zombie
from player import Player
from player2 import Player2
from hearts import hearts, Heart
from utilities import draw_background, add_monsters, add_zombies, add_bullets, add_bullets2

# initialize Pygame, it starts all of the game
pygame.init()

#display a caption on the game's display at the top
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shootas The Game")

#load the sound effects
music = pygame.mixer.Sound("../assets/sounds/FOREVER (ROUGH EXTENDED).mp3")
pew = pygame.mixer.Sound("../assets/sounds/esert-eagle-gunshot.mp3")
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
ow = pygame.mixer.Sound("../assets/sounds/Kill Confirmed Sound Effect -Free Sound Effect Download.mp3")
gameover = pygame.mixer.Sound("../assets/sounds/game_over_voice___sound_effect_hd-sbz13HBSgxY-192k-1700518998.mp3")
sad = pygame.mixer.Sound("../assets/sounds/[Emotional Music] Ghibli Epic Songs Collection (128kbps).mp3")

#background music
pygame.mixer.Sound.play(music)

#set up the timer #from CHATGPT and initalizing pygame clock
clock = pygame.time.Clock()

# make a copy of the screen #what does this do???
bg = pygame.image.load("../assets/sprites/bg.png").convert()
bg2 = pygame.image.load("../assets/sprites/Individual Tiles/wood.png").convert()
background = screen.copy()
draw_background(background)

#buttons
play_button = pygame.image.load("../assets/sprites/start_btn.png").convert()
quit_button = pygame.image.load("../assets/sprites/exit_btn.png").convert()

new_size_play_button = pygame.transform.scale(play_button, (209.25,94.5))
new_size_quit_button = pygame.transform.scale(quit_button, (209.25,94.5))

play_button_rect = new_size_play_button.get_rect(center=(screen_width/2 , screen_height/2 -60))
quit_button_rect = new_size_quit_button.get_rect(center=(screen_width/2, screen_height/2 +60))

#heart stuff
life_icon = pygame.image.load("../assets/sprites/Individual Icons and Particles/minceraftheart.png")
life_icon.set_colorkey((0,0,0))
life2_icon = pygame.image.load("../assets/sprites/Individual Icons and Particles/minceraftheart - Copy.png")
life2_icon.set_colorkey((0,0,0))

#initialize score and a custom font to display it
main_menu_font = pygame.font.Font("../assets/fonts/Minecraft-Regular.otf", 60)
gameover_font = pygame.font.Font("../assets/fonts/Minecraft-Regular.otf", 60)
score_font = pygame.font.Font("../assets/fonts/Minecraft-Regular.otf", 48)
time_font = pygame.font.Font("../assets/fonts/Minecraft-Regular.otf", 36)
angle = 0
angle2 = 0
score = 0

def draw_welcome(screen):
    game_font = pygame.font.Font("../assets/fonts/Minecraft-Regular.otf",64)
    welcome_text = game_font.render("Welcome to Shootas", True, (255,255,255))
    screen.blit(welcome_text, (screen_width/ 2 - welcome_text.get_width() /2, screen_height/2 - welcome_text.get_height()/2))

    instructions_font = pygame.font.Font("../assets/fonts/Minecraft-Regular.otf", 30)
    instructions_text = instructions_font.render(f"Objective: Survive.", True, (255,255,255))
    screen.blit(instructions_text, (screen_width / 2 - 100, screen_height - 200))

draw_mess = True

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_button_rect.collidepoint(mouse_pos):
                        return
                    elif quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

        for x in range(0, screen_width, bg.get_width()):
            for y in range(0, screen_height, bg.get_height()):
                screen.blit(bg, (x, y))

        screen.blit(new_size_play_button, play_button_rect)
        screen.blit(new_size_quit_button, quit_button_rect)

        custom_font = pygame.font.Font("../assets/fonts/Minecraft-Regular.otf", 180)
        text = custom_font.render("Shoota", True, (255, 255, 240))
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, 0))

        pygame.display.flip()

main_menu()

#main game loop
running = True
while running:

    lives = num_lives
    lives2 = num_lives2
    score = 0
    add_monsters(1)
    add_zombies(5)
    player = Player(screen_width / 2, screen_height / 2)
    player2 = Player2(screen_width / 2, screen_height / 2 + 50)

    #lives loop
    while lives and lives2 > 0:
        # welcome screen
        if draw_mess:
            draw_mess = False

            # welcome message and background
            for x in range(0, screen_width, bg2.get_width()):
                for y in range(0, screen_height, bg2.get_height()):
                    screen.blit(bg2, (x, y))

            draw_welcome(screen)
            start_time = pygame.time.get_ticks()

            # update the display
            pygame.display.flip()
            time.sleep(5)

        #event handling

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_up()
                elif event.key == pygame.K_DOWN:
                    player.move_down()
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_w:
                    player2.move_up()
                elif event.key == pygame.K_s:
                    player2.move_down()
                elif event.key == pygame.K_a:
                    player2.move_left()
                elif event.key == pygame.K_d:
                    player2.move_right()
                elif event.key == pygame.K_w:
                    player2.move_up()
                    angle2 = pi / 2
                elif event.key == pygame.K_s:
                    player2.move_down()
                    angle2 = - pi / 2
                elif event.key == pygame.K_a:
                    player2.move_left()
                    angle2 = pi
                elif event.key == pygame.K_d:
                    player2.move_right()
                    angle2 = 0
w
                elif event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(pew)
                    pos = player2.rect.midright
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    angle = - atan2(mouse_y - player2.y, mouse_x - player2.x)
                    add_bullets2(1, pos, angle2)

                # elif event.key == pygame.K_SPACE:
                #         bullet_sound.play()
                #         directionx = 1
                #         directiony = 0
                #         if player2.move_right() == player2.move_right():
                #             directionx = 1
                #             directiony = 0
                #         elif player2.move_left() == shooter.left_image:
                #             directionx = -1
                #             directiony = 0
                #         elif shooter.image == shooter.up_image:
                #             directiony = -1
                #             directionx = 0
                #         elif shooter.image == shooter.down_image:
                #             directiony = 1
                #             directionx = 0
                #         elif shooter.image == shooter.down_right_image:
                #             directionx = 1
                #             directiony = 1
                #         elif shooter.image == shooter.down_left_image:
                #             directionx = -1
                #             directiony = 1
                #         elif shooter.image == shooter.up_right_image:
                #             directionx = 1
                #             directiony = -1
                #         elif shooter.image == shooter.up_left_image:
                #             directionx = -1
                #             directiony = -1
                #
                #     bullets2.shoot_down()
                #     pos = player2.rect.midright
                #     add_bullets2(1, pos)
                #     pygame.mixer.Sound.play(pew)


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.stop_vertical_movement()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop_horizontal_movement()
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    player2.stop_vertical_movement()
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    player2.stop_horizontal_movement()

            elif event.type == pygame.MOUSEBUTTONDOWN:  # elif instead of if because this smoothens the code
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.Sound.play(pew)
                    pos = player.rect.midright
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    angle = - atan2(mouse_y - player.y, mouse_x - player.x)
                    add_bullets(1, pos, angle)

        #calculate time
        start_time = 0
        running_time = (pygame.time.get_ticks() - start_time) //1000 # in seconds

        #update each monster direction, do it individually so they all don't go the same way
        for monster in monsters:
            direction = atan2(player.y - monster.y, player.x - monster.x)
            monster.update(direction)

        #check for collisions between player and zombies
        result = pygame.sprite.spritecollide(player, zombies, True)
        if result:
            lives -= len(result)
            # play hurt sound
            pygame.mixer.Sound.play(hurt)
            # add new zombie
            add_zombies(len(result))

        #interaction with player2 and zombies
        result2 = pygame.sprite.spritecollide(player2,zombies,True)
        if result2:
            lives2 -= len(result2)
            pygame.mixer.Sound.play(hurt)
            add_zombies(len(result2))

        #check for collisions between player and monsters
        result = pygame.sprite.spritecollide(player, monsters, True)
        if result:
            lives -= len(result)
            #play hurt sound
            pygame.mixer.Sound.play(hurt)
            #add new monster
            add_monsters(len(result))

        #interaction with player2 and monsters
        result2 = pygame.sprite.spritecollide(player2, monsters, True)
        if result2:
            lives -= len(result2)
            pygame.mixer.Sound.play(hurt)
            add_monsters(len(result2))

        # result = pygame.sprite.spritecollide(player, hearts, True)
        #generating health every 10 kills
        # if score == 5:
        #     add_hearts(1)
        #
        #     result = pygame.sprite.spritecollide(player, hearts, True)
        #     if result:
        #         num_lives += len(result)
        #     elif score <= 5:
        #         continue


        #generating monsters
        for monster in monsters:
            if monster.rect.x < -monster.rect.width:
                monsters.remove(monster)
                add_monsters(1)

        #spawning in zombies
        for zombie in zombies:
            if zombie.rect.x > screen_width:
               zombies.remove(zombie)
               zombies.add(Zombie(random.randint(-screen_width, 0),
                                  random.randint(tile_size, screen_height - tile_size)))

        for bullet2 in bullets2:
            if bullet2.rect.x > screen_width:
                bullets2.remove(bullet2)

            for monster in monsters:
                bullet2_monster = pygame.sprite.spritecollide(bullet2,monsters,True)
                if bullet2_monster:
                    score += len(bullet2_monster)
                    monsters.remove(monster)
                    add_monsters(1)
                    bullet2.remove(bullet2)
                    pygame.mixer.Sound.play(ow)


            for zombie in zombies:
                bullet2_zombie = pygame.sprite.spritecollide(bullet2,zombies,True)
                if bullet2_zombie:
                    score += len(bullet2_zombie)
                    zombies.remove(zombie)
                    add_zombies(1)
                    bullets2.remove(bullet2)
                    pygame.mixer.Sound.play(ow)

        #bullet interaction with monsters and zombies
        for bullet in bullets:
            if bullet.rect.x > screen_width:
                bullets.remove(bullet)

            for monster in monsters:
                bullet_monster = pygame.sprite.spritecollide(bullet, monsters, True)
                if bullet_monster:
                    score += len(bullet_monster)
                    monsters.remove(monster)
                    add_monsters(1)
                    bullets.remove(bullet)
                    pygame.mixer.Sound.play(ow)

            for zombie in zombies:
                bullet_zombie = pygame.sprite.spritecollide(bullet, zombies, True)
                if bullet_zombie:
                    score += len(bullet_zombie)
                    zombies.remove(zombie)
                    add_zombies(1)
                    bullets.remove(bullet)
                    pygame.mixer.Sound.play(ow)

        # draw the background
        screen.blit(background, (0, 0))

        # draw the score in the upper left corner
        score_message = score_font.render(f"{score}", True, (255, 255, 240))
        screen.blit(score_message, (screen_width - score_message.get_width() - 10, 0))

        #draw the timer
        timer_text = time_font.render(f"{running_time}s", True, (255, 255, 240))
        screen.blit(timer_text, (10,10))

        # draw game objects
        player.draw(screen)
        player2.draw(screen)
        monsters.draw(screen)
        zombies.draw(screen)
        hearts.draw(screen)

        for bullet in bullets:
            bullet.draw_bullet(screen)

        for bullet2 in bullets2:
            bullet2.draw_bullet(screen)

        # draw the lives in the lower left corner
        for life in range(lives):
            screen.blit(life_icon, (life* tile_size, screen_height - tile_size))

        for life in range(lives2):
            screen.blit(life2_icon, (screen_width - (life* tile_size), screen_height-tile_size))

        #update display
        pygame.display.flip() #why do we put this here

        # update game objects
        player.update()
        player2.update()
        bullets.update()
        bullets2.update()
        zombies.update()
        hearts.update()

        # Limit the frame rate
        clock.tick(60)

    screen.blit(background, (0,0))

    #show a game over message
    gameover_message = gameover_font.render("Game Over", True, (139,0,0))
    screen.blit(gameover_message, (screen_width/ 2 - gameover_message.get_width() / 2,
                          screen_height/2 - gameover_message.get_height() / 2 ))

    #show the final score
    score_text = score_font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2,
                             screen_height / 2 + gameover_message.get_height()))
    #time survived
    time_text = time_font.render(f"Time survived: {running_time}", True, (0,0,0))
    screen.blit(time_text, (screen_width/2 - time_text.get_width()/2, screen_height / 2 + gameover_message.get_height() + score_text.get_height()))

    quit_font = pygame.font.Font("../assets/fonts/HUSKYSTA.TTF", 20)
    quit_text = quit_font.render(f"Press 'Q' to quit", True, (255, 255, 240))
    screen.blit(quit_text, (screen_width - quit_text.get_width(), screen_height - 20))

    pygame.display.flip()

    if lives and lives2 == 0:
        pygame.mixer.Sound.stop(music)
        pygame.mixer.Sound.play(gameover) and pygame.mixer.Sound.play(sad)

    #wait for user to exit the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # Quit Pygame
                    pygame.quit()
                    sys.exit()