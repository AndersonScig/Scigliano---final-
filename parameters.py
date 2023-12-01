import pygame

#screen dimentions
BUFFER = 5
WIDTH = 600
HEIGHT = 633
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bank = (pygame.transform.scale(pygame.image.load('../Scigliano-final/asset/bank.png'), (130,70))) #get robber png


#collectables
coin = (pygame.transform.scale(pygame.image.load("../Scigliano-final/asset/coin.png"), (15, 15))).convert()
coin.set_colorkey((0, 0, 0))
money_bag = (pygame.transform.scale(pygame.image.load("../Scigliano-final/asset/money_bag.png"), (25, 25))).convert()
money_bag.set_colorkey((0, 0, 0))

#enemy
helicopter = (pygame.transform.scale(pygame.image.load("../Scigliano-final/asset/helicopter.png"), (40, 40))).convert()
helicopter.set_colorkey((0,0,0))
#
# run = True
# while run:
#     timer.tick(fps)
#     screen.fill('black')
#     screen.fill((170, 170, 170))
#     draw_board()
#     draw_rand()
#     screen.blit(bank, (235, 240))
#     my_helicopter.draw(screen)
#     draw_player()
#     center_x = player_x + 15
#     center_y = player_y + 18
#     turns_allowed = check_position(center_x, center_y)
#     player_x, player_y = move_player(player_x, player_y)
#     score, powerup, power_counter = check_collisions(score, powerup, power_counter)
#     center_helo_x = my_helicopter.x + my_helicopter.width / 2
#     center_helo_y = my_helicopter.y + my_helicopter.height / 2
#     # Calculate the angle between the helicopter and the robber
#     direction_helo = atan2(player_y - center_helo_y, player_x - center_helo_x)
#     # Update the helicopter's movement based on the calculated angle
#     my_helicopter.update(direction_helo)
#
#     if not game_over:
#         remaining_time -= 1 / fps
#     time_text = font.render(f'Time {remaining_time:.0f}', True, 'white')
#     screen.blit(time_text, (220, HEIGHT - 35))
#
#     if (my_helicopter.x - BUFFER < center_x < my_helicopter.x + my_helicopter.width + BUFFER) \
#             and (my_helicopter.y - BUFFER < center_y < my_helicopter.y + my_helicopter.height + BUFFER):
#         lives -= 1
#         my_helicopter = Helicopter(random.randint(0, WIDTH - helicopter.get_width()), random.randint(0, 100))
#         player_x = 285  # start pos x
#         player_y = 425  # start pos y
#         direction = 0
#         direction_command = 0
#         power_counter = 0
#
#     if powerup and power_counter < 300:
#         power_counter += 1
#         player_speed = 3
#     elif powerup and power_counter >= 300:
#         power_counter = 0
#         player_speed = 2
#         powerup = False
#
#     if score == total_coins or lives <= 0 or remaining_time <= 0:
#         game_over = True
#
#     if game_over == True and score == total_coins:
#         game_won = True
#
#     if game_over == True and score != total_coins:
#         game_lost = True
#
#     if game_won:
#         final_score = score + remaining_time
#         display_win_screen(screen, welcome_font, final_score)
#         pygame.display.flip()
#         waiting_for_key = True
#
#     if game_lost:
#         final_score = score + remaining_time
#         display_lose_screen(screen, welcome_font, final_score)
#         pygame.display.flip()
#         waiting_for_key = True
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#         if waiting_for_key:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_r:  # Restart the game
#                     # Reset game variables to their initial state
#                     score = 0
#                     lives = 3
#                     remaining_time = game_time
#                     player_x = 285
#                     player_y = 425
#                     direction = 0
#                     direction_command = 0
#                     game_over = False
#                     game_won = False
#                     game_lost = False
#                     waiting_for_key = False  # Add this line to exit the waiting state
#
#                 elif event.key == pygame.K_q:  # Quit the game
#                     run = False
#
#         elif event.type == pygame.KEYDOWN:  # first very simple like fish game
#             if event.key == pygame.K_RIGHT:  # change to be more similar to joystick commands
#                 direction_command = 0
#             if event.key == pygame.K_LEFT:
#                 direction_command = 1
#             if event.key == pygame.K_UP:
#                 direction_command = 2
#             if event.key == pygame.K_DOWN:
#                 direction_command = 3
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.KEYUP:  # inorder to keep moving while key up
#             if event.key == pygame.K_RIGHT and direction_command == 0:
#                 direction_command = direction
#             if event.key == pygame.K_LEFT and direction_command == 1:
#                 direction_command = direction
#             if event.key == pygame.K_UP and direction_command == 2:
#                 direction_command = direction
#             if event.key == pygame.K_DOWN and direction_command == 3:
#                 direction_command = direction
#
#         for x in range(4):
#             if direction_command == x and turns_allowed[x]:
#                 direction = x


