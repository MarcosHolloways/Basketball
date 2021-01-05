import pygame
from pygame.sprite import Sprite
class Personagem(Sprite):
    def __init__(self, tela, confg):
        super().__init__()
        self.image = pygame.image.load("Personagem.bmp")
        self.rect = self.image.get_rect()
        self.tela = tela
        self.confg = confg
        self.rect = self.image.get_rect()
        self.screen_rect = tela.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False



    def person_draw(self):
        self.tela.blit(self.image, self.rect)
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.confg.person_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.confg.person_speed


