import os
import pygame
from load_img import load_image

pygame.init()

USERNAME = os.environ.get("USERNAME")
size = WIDTH, HEIGHT = 800, 600
FPS = 60
pers_size = pers_width, pers_height = (WIDTH // 22, HEIGHT // 10)

tile_size = tile_width, tile_height = (WIDTH // 12, WIDTH // 12)

clock = pygame.time.Clock()
tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
settings_spr = pygame.sprite.Group()
enemy_group = pygame.sprite.Sprite()
btns = pygame.sprite.Group()
lvl_btn = pygame.sprite.Group()

menu_running = True

screen = pygame.display.set_mode(size)

levels = {
    1: 'level_1.txt',
    2: 'level_2.txt',
    3: 'level_3.txt',
    4: 'level_4.txt',
    5: 'level_5.txt',
    6: 'level_6.txt',
    7: 'level_7.txt',
    8: 'level_8.txt'
}

tile_images = {
    '0': pygame.transform.scale(load_image('TEXTURE_0.jpg'), tile_size),
    '1': pygame.transform.scale(load_image('TEXTURE_1.jpg'), tile_size),
    '2': pygame.transform.scale(load_image('TEXTURE_2.jpg'), tile_size),
    '3': pygame.transform.scale(load_image('TEXTURE_3.jpg'), tile_size),
    '#': pygame.transform.scale(load_image('TEXTURE_wall.jpg'), tile_size),
    'empty': pygame.transform.scale(load_image('TEXTURE_pol.jpg'), tile_size)
}