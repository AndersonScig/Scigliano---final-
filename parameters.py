import pygame

#screen dimentions
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
