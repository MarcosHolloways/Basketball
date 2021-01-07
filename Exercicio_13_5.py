import pygame
import sys
from confg_13_5 import Configuration
from personagem import Personagem
import funcoes_perso as fp
from object_ball import Ball
from pygame.sprite import Group
from Game_Stats import Game_Stats
def run_game():
    pygame.init()
    confg = Configuration()
    tela = pygame.display.set_mode((confg.tela_largura, confg.tela_altura))
    pygame.display.set_caption("Exercicio 13.5")
    stats = Game_Stats(confg)
    ball = Ball(tela, confg)
    personagem = Personagem(tela, confg)

    ball_s = Group(ball)
    persons = Group(personagem)
    while True:
        #rodar
        if stats.game_active:
            tela.fill((255, 255, 255))
            personagem.update()
            fp.check_borda_bola(stats,ball_s)
            fp.update_tela(stats, tela, confg, ball_s, persons)
            ball_s.update()
        persons.draw(tela)
        ball_s.draw(tela)
        fp.check_events(personagem)
        fp.check_collision(stats,tela, confg, ball_s)
        pygame.display.flip()
run_game()