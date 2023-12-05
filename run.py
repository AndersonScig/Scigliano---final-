#get the board back tp
#credit
import sys
import pygame
from board import boards
from math import pi
from parameters import *
from math import atan2
import random
from helicopter import helicopters, Helicopter

pygame.init()
welcome_font = pygame.font.Font('../Scigliano-final/asset/blox/blox2.ttf', 40)


def start_game():
    global draw_message
    draw_message = False

#draw the directions and objective
def draw_intro(screen):
    font = pygame.font.Font('../Scigliano-final/asset/blox/blox2.ttf', 20)
    # Font for the "Welcome to RUN!!" text with a larger size

    welcome = "Welcome to RUN"
    paragraph1 = "Objective     collect as many coins as you can"
    paragraph2 = "Escape the police helicopter before time runs out"
    paragraph3 = "Instructions     use the arrow keys"
    paragraph4 = "to move the robber around the map"
    paragraph5 = "Tip     Collecting the money bags will"
    paragraph6 = "give you a short speed boost and more points"
    paragraph7 = "extra time is added to your score"
    start = "press space to start"

    # Render each paragraph separately
    intro_text = welcome_font.render(welcome, True, 'blue')
    intro_text1 = font.render(paragraph1, True, 'white')
    intro_text2 = font.render(paragraph2, True, 'white')
    intro_text3 = font.render(paragraph3, True, 'white')
    intro_text4 = font.render(paragraph4, True, 'white')
    intro_text5 = font.render(paragraph5, True, 'white')
    intro_text6 = font.render(paragraph6, True, 'white')
    intro_text7 = font.render(paragraph7, True, 'white')
    start_text = font.render(start, True, 'red')

    # Blit each rendered paragraph to the screen
    screen.blit(intro_text, (160, 50))
    screen.blit(intro_text1, (50, 140))
    screen.blit(intro_text2, (50, 180))
    screen.blit(intro_text3, (50, 300))
    screen.blit(intro_text4, (50, 350))
    screen.blit(intro_text5, (50, 450))
    screen.blit(intro_text6, (50, 500))
    screen.blit(intro_text7, (50, 550))
    screen.blit(start_text, (360, 575))


draw_message = True
background = screen.copy()
draw_intro(background)

if draw_message:
    screen.blit(background, (0, 0))
    draw_intro(screen)
    pygame.display.flip()

while draw_message:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_game()

screen.blit(background, (0, 0))
draw_intro(screen)
pygame.display.flip()

#blit the score, lives, and other
def draw_rand():
    score_text = font.render(f'Score {score}', True, 'white')
    screen.blit(score_text, (10, HEIGHT - 35))
    lives_text = font.render('lives', True, 'white')
    screen.blit(lives_text, (400, HEIGHT - 35))
    for x in range(lives):
        pygame.draw.circle(screen, 'green', (475 + x * 30, HEIGHT - 25), 10)

#collect coins and power up
def check_collisions(score, power, power_count):
    numh = (HEIGHT - 50) // 32
    numw = WIDTH // 30
    if 0 < player_x < WIDTH:
        if level[center_y // numh][center_x // numw] == 1:
            level[center_y // numh][center_x // numw] = 0
            score += 1
        elif level[center_y // numh][center_x // numw] == 2:
            level[center_y // numh][center_x // numw] = 0
            pygame.mixer.Sound.play(money_bag_sound)
            score += 10
            power = True
            power_count = 0
    return score, power, power_count

#all board 1-8
def draw_board():
    numh = ((HEIGHT - 50) // 32)  # height of block
    numw = (WIDTH // 30)  # width of block
    for i in range(len(level)):  # column
        for j in range(len(level[i])):  # row
            if level[i][j] == 1:
                screen.blit(coin, (
                j * numw + (.5 * numw) - 7, i * numh + (.5 * numh) - 5))  # left
            if level[i][j] == 2:
                screen.blit(money_bag, (
                j * numw + (.5 * numw) - 10, i * numh + (.5 * numh) - 14))  # left
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * numw + (.5 * numw), i * numh),
                                 (j * numw + (.5 * numw), i * numh + numh), 3)  # start and end point of the line
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * numw, i * numh + (.5 * numh)),
                                 (j * numw + numw, i * numh + .5 * numh), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * numw - (numw * .5)), (i * numh + (.5 * numh)), numw, numh], 0,
                                pi / 2, 3)  # draw square that you want your curve to be in
            if level[i][j] == 6:  # start and end on a radian
                pygame.draw.arc(screen, color, [(j * numw + (numw * .5)), (i * numh + (.5 * numh)), numw, numh], pi / 2,
                                pi, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * numw + (numw * .5)), (i * numh - (.5 * numh)), numw, numh], pi,
                                3 * pi / 2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j * numw - (numw * .5)), (i * numh - (.5 * numh)), numw, numh],
                                3 * pi / 2, 2 * pi, 3)


#
def draw_player():
    if direction == 0:
        screen.blit(pygame.transform.flip(player, True, False), (player_x, player_y))  # right
    elif direction == 1:
        screen.blit(player, (player_x, player_y))  # left
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player, -90), (player_x, player_y))  # Up
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player, 90), (player_x, player_y))  # down


def check_position(centerx, centery):
    turns = [False, False, False, False]
    numh = (HEIGHT - 50) // 32
    numw = (WIDTH // 30)
    nume = 10

    def is_wall_collision(x, y):
        numh = (HEIGHT - 50) // 32
        numw = (WIDTH // 30)
        return level[y // numh][x // numw] >= 3

    # check collisions based on center x and center y of player +/- error acceptance
    if centerx // 30 < 29:
        if direction == 0:
            if (level[centery // numh][(centerx - nume) // numw]) < 3 and not is_wall_collision(centerx - nume, centery):
                turns[1] = True
        if direction == 1:
            if level[centery // numh][(centerx + nume) // numw] < 3 and not is_wall_collision(centerx + nume, centery):
                turns[0] = True
        if direction == 2:
            if level[(centery + nume) // numh][centerx // numw] < 3 and not is_wall_collision(centerx, centery + nume):
                turns[3] = True
        if direction == 3:
            if level[(centery - nume) // numh][centerx // numw] < 3 and not is_wall_collision(centerx, centery - nume):
                turns[2] = True

        if direction == 2 or direction == 3:
            if 5 <= centerx % numw <= 25:
                if level[(centery + nume) // numh][centerx // numw] < 3 and not is_wall_collision(centerx, centery + nume):
                    turns[3] = True
                if level[(centery - nume) // numh][centerx // numw] < 3 and not is_wall_collision(centerx, centery - nume):
                    turns[2] = True
            if 5 <= centery % numh <= 25:
                if level[centery // numh][(centerx - numw) // numw] < 3 and not is_wall_collision(centerx - numw, centery):
                    turns[1] = True
                if level[centery // numh][(centerx + numw) // numw] < 3 and not is_wall_collision(centerx + numw, centery):
                    turns[0] = True
        if direction == 0 or direction == 1:
            if 5 <= centerx % numw <= 25:
                if level[(centery + numh) // numh][centerx // numw] < 3 and not is_wall_collision(centerx, centery + numh):
                    turns[3] = True
                if level[(centery - numh) // numh][centerx // numw] < 3 and not is_wall_collision(centerx, centery - numh):
                    turns[2] = True
            if 5 <= centery % numh <= 25:
                if level[centery // numh][(centerx - nume) // numw] < 3 and not is_wall_collision(centerx - nume, centery):
                    turns[1] = True
                if level[centery // numh][(centerx + nume) // numw] < 3 and not is_wall_collision(centerx + nume, centery):
                    turns[0] = True
    return turns


def move_player(play_x, play_y):
    turns_allowed = check_position(play_x + 15, play_y + 18)
    if direction == 0 and play_x < WIDTH - 60 and turns_allowed[0]:
        play_x += player_speed
    elif direction == 1 and play_x > 40 and turns_allowed[1]:
        play_x -= player_speed
    if direction == 2 and play_y > 35 and turns_allowed[2]:
        play_y -= player_speed
    elif direction == 3 and play_y < HEIGHT - 98 and turns_allowed[3]:
        play_y += player_speed
    return play_x, play_y


def display_win_screen(screen, welcome_font, score):
    screen.fill('black')
    win_text1 = welcome_font.render(f"Congratulations   You won", True, 'green')
    win_text2 = welcome_font.render(f"score {score:.0f}", True, 'green')
    try_again_text = font.render(f"press r to try again", True, 'green')
    quit_text = font.render(f"press q to quit", True, 'green')
    screen.blit(win_text1, (WIDTH // 2 - win_text1.get_width() // 2, HEIGHT/2-100))
    screen.blit(win_text2, (WIDTH // 2 - win_text2.get_width() // 2, (HEIGHT/2)))
    screen.blit(try_again_text, (360, 500))
    screen.blit(quit_text, (90, 500))
    pygame.display.flip()

def display_lose_screen(screen, welcome_font, score):
    screen.fill('black')
    lose_text1 = welcome_font.render(f"Game over   try again", True, 'red')
    lose_text2 = welcome_font.render(f"score {score:.0f}", True, 'red')
    try_again_text = font.render(f"press r to try again", True, 'green')
    quit_text = font.render(f"press q to quit", True, 'green')
    screen.blit(lose_text1, (WIDTH // 2 - lose_text1.get_width() // 2, (HEIGHT/2-100)))
    screen.blit(lose_text2, (WIDTH // 2 - lose_text2.get_width() // 2, (HEIGHT/2)))
    screen.blit(try_again_text, (330, 500))
    screen.blit(quit_text, (90, 500))
    pygame.display.flip()


timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('../Scigliano-final/asset/blox/blox2.ttf', 20)
level = boards
color = 'black'
player_x = 285  # start pos x
player_y = 425  # start pos y
direction = 0
direction_command = 0
score = 0
center_helo_x = 0
center_helo_y = 0
power_counter = 0
player_speed = 2
total_coins = 183
lives = 3
game_time = 180
remaining_time = game_time
powerup = False
game_over = False
game_lost = False
game_won = False
waiting_for_key = False
turns_allowed = [False, False, False, False]  # RLUD
player = (pygame.transform.scale(pygame.image.load('../Scigliano-final/asset/robber.png'), (30, 30)))  # get robber png
background_sound = pygame.mixer.Sound("../Scigliano-final/asset/background.mp3")
pygame.mixer.Sound.play(background_sound)
# Set the volume level (e.g., 0.5 for half volume)
background_sound.set_volume(0.2)
money_bag_sound = pygame.mixer.Sound("../Scigliano-final/asset/money_sound.wav")
my_helicopter = Helicopter(random.randint(0, WIDTH - helicopter.get_width()), random.randint(0, 100))

#main loop
run = True
while run:
    timer.tick(fps)
    screen.fill((170, 170, 170))
    draw_board()
    draw_rand()
    screen.blit(bank, (235, 240))
    my_helicopter.draw(screen)
    draw_player()
    center_x = player_x + 15
    center_y = player_y + 18
    turns_allowed = check_position(center_x, center_y)
    player_x, player_y = move_player(player_x, player_y)
    score, powerup, power_counter = check_collisions(score, powerup, power_counter)
    center_helo_x = my_helicopter.x + my_helicopter.width / 2
    center_helo_y = my_helicopter.y + my_helicopter.height / 2
    # Calculate the angle between the helicopter and the robber
    direction_helo = atan2(player_y - center_helo_y, player_x - center_helo_x)
    # Update the helicopter's movement based on the calculated angle
    my_helicopter.update(direction_helo)

    if not game_over:
        remaining_time -= 1/fps
        time_text = font.render(f'Time {remaining_time:.0f}', True, 'white')
        screen.blit(time_text, (220, HEIGHT - 35))

    if (my_helicopter.x - BUFFER < center_x < my_helicopter.x + my_helicopter.width + BUFFER) \
            and (my_helicopter.y - BUFFER < center_y < my_helicopter.y + my_helicopter.height + BUFFER):
        lives -= 1
        my_helicopter = Helicopter(random.randint(0, WIDTH - helicopter.get_width()), random.randint(0, 100))
        player_x = 285  # start pos x
        player_y = 425  # start pos y
        direction = 0
        direction_command = 0
        power_counter = 0


    if powerup and power_counter < 300:
        power_counter += 1
        player_speed = 3
    elif powerup and power_counter >= 300:
        power_counter = 0
        player_speed = 2
        powerup = False

    if score == total_coins or lives <= 0 or remaining_time <= 0:
        player_speed = 0
        game_over = True

    if game_over == True and score == total_coins:
        game_won = True

    if game_over == True and score != total_coins:
        game_lost = True

    if game_won:
        final_score = score + remaining_time
        display_win_screen(screen, welcome_font, final_score)
        pygame.display.flip()
        waiting_for_key = True

    if game_lost:
        final_score = score + remaining_time
        display_lose_screen(screen, welcome_font, final_score)
        pygame.display.flip()
        waiting_for_key = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if waiting_for_key:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    # #Reset game variables to their initial state
                    score = 0
                    lives = 3
                    remaining_time = game_time
                    player_x = 285
                    player_y = 425
                    player_speed = 2
                    direction = 0
                    direction_command = 0
                    game_over = False
                    game_won = False
                    game_lost = False
                    waiting_for_key = False  # Add this line to exit the waiting state
                    my_helicopter = Helicopter(random.randint(0, WIDTH - helicopter.get_width()),
                                               random.randint(0, 100))
                elif event.key == pygame.K_q:  # Quit the game
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

        for x in range(4):
            if direction_command == x and turns_allowed[x]:
                direction = x

    pygame.display.flip()
pygame.quit()
sys.exit()
