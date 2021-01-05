import pygame
import sys
from object_ball import Ball


def check_events(perso):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, perso)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, perso)
        elif event.type == pygame.QUIT:
            sys.exit()


def check_keyup_events(event, perso):
    """Responde a solturas de tecla"""
    if event.key == pygame.K_RIGHT:
        perso.moving_right = False
    elif event.key == pygame.K_LEFT:
        perso.moving_left = False


def check_keydown_events(event, perso):
    """Responde a pressionamentos de tecla."""
    if event.key == pygame.K_RIGHT:
        perso.moving_right = True
    elif event.key == pygame.K_LEFT:
        perso.moving_left = True


def check_collision(tela, confg, ball, person):
    collisions = pygame.sprite.groupcollide(ball, person, True, False)
    if not ball:
        new_ball = Ball(tela,confg)
        ball.add(new_ball)


