import pygame
import sys
from confg_13_5 import Configuration
from personagem import Personagem
import funcoes_perso as fp
from object_ball import Ball
from pygame.sprite import Group
def run_game():
    pygame.init()
    confg = Configuration()
    tela = pygame.display.set_mode((confg.tela_largura, confg.tela_altura))
    pygame.display.set_caption("Exercicio 13.5")


    ball = Ball(tela, confg)
    personagem = Personagem(tela, confg)

    ball_s = Group(ball)
    persons = Group(personagem)
    while True:
        tela.fill((255, 255, 255))
        persons.draw(tela)
        ball_s.draw(tela)
        fp.check_events(personagem)
        personagem.update()
        ball_s.update()
        fp.check_collision(tela, confg, ball_s, persons)
        pygame.display.flip()
run_game()