import sys
import pygame
from board import boards
from math import pi
from parameters import *
import time
from math import atan2
import random
from helicopter import helicopters, Helicopter
pygame.init()

# def draw_welcome(screen):
#     font = pygame.font.Font('../final/asset/blox/blox2.ttf', 64)
#     text = font.render("Welcome to RUN", True, (155,155,255))
#     screen.blit(text, ((WIDTH-text.get_width())//2, (HEIGHT-text.get_height())//2))
# draw_message = True
# background = screen.copy()
# draw_welcome(background)
#
# if draw_message:
#     screen.blit(background, (0,0))
#     draw_welcome(screen)
#     pygame.display.flip()
#     time.sleep(5)

def draw_rand():
    score_text = font.render(f'Score {score}', True, 'white')
    screen.blit(score_text, (10, HEIGHT-35))
    lives_text = font.render('lives', True, 'white')
    screen.blit(lives_text, (350, HEIGHT - 35))
    for x in range(lives):
        pygame.draw.circle(screen, 'green', (425 + x*30, HEIGHT-25), 10)
    # if game_over:
    #     pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
    #     pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
    #     gameover_text = font.render('Game over! Space bar to restart!', True, 'red')
    #     screen.blit(gameover_text, (100, 300))
    # if game_won:
    #     pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
    #     pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
    #     gameover_text = font.render('Victory! Space bar to restart!', True, 'green')
    #     screen.blit(gameover_text, (100, 300))
#
def check_collisions(score, power, power_count):
    numh = (HEIGHT - 50) // 32
    numw = WIDTH // 30
    if 0 < player_x < WIDTH:
        if level[center_y // numh][center_x // numw] == 1:
            level[center_y // numh][center_x // numw] = 0
            score += 1
        if level[center_y // numh][center_x // numw] == 2:
            level[center_y // numh][center_x // numw] = 0
            pygame.mixer.Sound.play(money_bag_sound)
            score += 10
            power = True
            power_count = 0
    return score, power, power_count
def draw_board():
    numh = ((HEIGHT - 50) // 32) #height of block
    numw = (WIDTH //30)   #width of block
    for i in range(len(level)): #column
        for j in range(len(level[i])): #row
            if level[i][j] == 1:
                screen.blit(coin, (j*numw+(.5*numw)-7, i *numh + (.5*numh)-5))  #left         if level [i][j]==2:
                # pygame.draw.circle(screen, 'white', (j*numw+(.5*numw), i *numh + (.5*numh)),4 )
            if level[i][j] == 2:
                screen.blit(money_bag, (j*numw+(.5*numw)-10, i *numh + (.5*numh)-14))  #left        if level [i][j]==2:
                # pygame.draw.circle(screen, 'white', (j*numw+(.5*numw), i *numh + (.5*numh)),8 )
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * numw + (.5 * numw), i*numh), (j * numw + (.5 * numw), i*numh+numh), 3)  #start and end point of the line
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * numw, i*numh + (.5*numh )), (j * numw + numw, i*numh+ .5* numh), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * numw - (numw * .5)), (i*numh + (.5*numh)), numw, numh], 0, pi/2, 3)  #draw square that you want your curve to be in
            if level[i][j] == 6:                                                                                                                  # start and end on a radian
                pygame.draw.arc(screen, color, [(j * numw + (numw * .5)), (i*numh + (.5*numh)), numw, numh],  pi/2, pi,  3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * numw + (numw * .5)), (i*numh - (.5*numh)), numw, numh], pi, 3*pi/2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j * numw - (numw * .5)), (i*numh - (.5*numh)), numw, numh],  3*pi/2,2*pi, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'blue', (j * numw, i * numh + (.5 * numh)),(j * numw + numw, i * numh + .5 * numh), 3)
#
def draw_player():
    if direction == 0:
        screen.blit(pygame.transform.flip(player,True,False), (player_x, player_y)) #right
    elif direction == 1:
        screen.blit(player, (player_x, player_y)) # left
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player,-90), (player_x, player_y)) #Up
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player, 90), (player_x, player_y)) #down

def check_position(centerx, centery):
    turns = [False, False, False, False]
    numh = (HEIGHT - 50) // 32
    numw = (WIDTH // 30)
    nume = 15
    # check collisions based on center x and center y of player +/- error acceptance
    if centerx // 30 < 29:
        if direction == 0:
            if (level[centery // numh][(centerx - nume) // numw]) < 3:
                turns[1] = True
        if direction == 1:
            if level[centery // numh][(centerx + nume) // numw] < 3:
                turns[0] = True
        if direction == 2:
            if level[(centery + nume) // numh][centerx // numw] < 3:
                turns[3] = True
        if direction == 3:
            if level[(centery - nume) // numh][centerx // numw] < 3:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= centerx % numw <= 18:
                if level[(centery + nume) // numh][centerx // numw] < 3:
                    turns[3] = True
                if level[(centery - nume) // numh][centerx // numw] < 3:
                    turns[2] = True
            if 12 <= centery % numh <= 18:
                if level[centery // numh][(centerx - numw) // numw] < 3:
                    turns[1] = True
                if level[centery // numh][(centerx + numw) // numw] < 3:
                    turns[0] = True
        if direction == 0 or direction == 1:
            if 12 <= centerx % numw <= 18:
                if level[(centery + numh) // numh][centerx // numw] < 3:
                    turns[3] = True
                if level[(centery - numh) // numh][centerx // numw] < 3:
                    turns[2] = True
            if 12 <= centery % numh <= 18:
                if level[centery // numh][(centerx - nume) // numw] < 3:
                    turns[1] = True
                if level[centery // numh][(centerx + nume) // numw] < 3:
                    turns[0] = True
    # else:
    #     turns[0] = True
    #     turns[1] = True

    return turns

def move_player(play_x, play_y):
    if direction == 0:
        play_x += player_speed
    elif direction == 1:
        play_x -= player_speed
    if direction == 2:
        play_y -= player_speed
    elif direction == 3:
        play_y += player_speed
    return play_x, play_y


timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('../final/asset/blox/blox2.ttf', 20)
level = boards
color = 'black'
player = (pygame.transform.scale(pygame.image.load('asset/robber.png'), (30,30))) #get robber png
# helo = (pygame.transform.scale(pygame.image.load('asset/helicopter.png'), (30,30)))
player_x = 285 #start pos x
player_y = 425 #start pos y
direction = 0
direction_command = 0
turns_allowed = [False, False, False, False] #RLUD
player_speed = 2
background_sound = pygame.mixer.Sound("../final/asset/background.mp3")
pygame.mixer.Sound.play(background_sound)
#Set the volume level (e.g., 0.5 for half volume)
background_sound.set_volume(0.2)
money_bag_sound = pygame.mixer.Sound("../final/asset/money_sound.wav")
score = 0
powerup = False
power_counter = 0
lives = 3
for i in range(1):
    helicopters.add(Helicopter(random.randint(0, WIDTH-helicopter.get_width()), random.randint(0, 100)))
game_over = False
game_won = False


run = True
while run:
    timer.tick(fps)
    screen.fill((170,170,170))
    draw_board()
    # draw_player()
    draw_rand()
    center_x = player_x + 15
    center_y = player_y + 18
    turns_allowed = check_position(center_x, center_y)
    player_x, player_y = move_player(player_x, player_y)
    score, powerup, power_counter = check_collisions(score, powerup, power_counter)
    screen.blit(bank, (235, 240))
    for helicopter in helicopters:
        direction_helo = atan2(player_y - helicopter.y, player_x - helicopter.x)
        helicopter.update(direction_helo)
    helicopters.draw(screen)
    draw_player()
    if powerup and power_counter < 300:
        power_counter += 1
        player_speed = 3
    elif powerup and power_counter >= 300:
        power_counter = 0
        player_speed = 2
        powerup = False

    # result = pygame.sprite.spritecollide(player, helicopters, True)
    # if result:
    #     lives -= len(result)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  # first very simple like fish game
            if event.key == pygame.K_RIGHT:  # change to be more similar to joystick commands
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:  # inorder to keep moving while key up
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction

    for x in range(4):
        if direction_command == x and turns_allowed[x]:
            direction = x

    # if player_x > 600:
    #     player_x = - 50
    # elif player_x < -50:
    #     player_x = 600

    pygame.display.flip()
pygame.quit()
sys.exit()
