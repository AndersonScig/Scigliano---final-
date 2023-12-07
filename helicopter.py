from parameters import *
from math import cos, sin


class Helicopter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = (pygame.transform.scale(pygame.image.load('asset/helicopter.png'), (75, 75)))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 1.15
        self.rect.center = (x, y)
        self.width = self.rect.width
        self.height = self.rect.height

    def update(self, direction_helo):
        self.x += self.speed * cos(direction_helo)
        self.rect.x = self.x
        self.y += self.speed * sin(direction_helo)
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


helicopters = pygame.sprite.Group()