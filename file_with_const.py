import os
import sys

import pygame

USERNAME = os.environ.get("USERNAME")
size = WIDTH, HEIGHT = 1200, 900
FPS = 60

clock = pygame.time.Clock()
tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
settings_spr = pygame.sprite.Group()
btns = pygame.sprite.Group()


def terminate():
    pygame.quit()
    sys.exit()