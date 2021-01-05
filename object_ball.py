import pygame
from random import randint
from pygame.sprite import Sprite
class Ball(Sprite):
    def __init__(self, tela, confg):
            super().__init__()
            self.image = pygame.image.load("Basket.bmp")
            self.tela = tela
            self.rect = self.image.get_rect()
            self.tela_rect = self.tela.get_rect()
            self.rect.x = randint(1, confg.tela_largura - 50)
    def draw(self):
        self.tela.blit(self.image, self.rect)
    def update(self):
        self.rect.y += 1
