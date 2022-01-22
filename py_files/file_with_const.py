import os
import pygame
from load_img import load_image


def get_size(filename) -> tuple:
    with open(filename, 'r') as file:
        size_r = list(line.split() for line in file)
    size_r = list(map(int, size_r[0]))
    return tuple(size_r)


pygame.init()

size = WIDTH, HEIGHT = get_size(os.path.join('py_files', 'window_size.txt'))
FPS = 60
pers_size = pers_width, pers_height = (WIDTH // 22, HEIGHT // 10)
enemy_size = enemy_width, enemy_height = (WIDTH // 13, HEIGHT // 10)
tile_size = tile_width, tile_height = (WIDTH // 12, WIDTH // 12)

clock = pygame.time.Clock()

IS_PRODUCT = False

menu_running = True

screen = pygame.display.set_mode(size)

levels = {
    1: os.path.join('levels', 'level_1.txt'),
    2: os.path.join('levels', 'level_2.txt'),
    3: os.path.join('levels', 'level_3.txt'),
    4: os.path.join('levels', 'level_4.txt'),
    5: os.path.join('levels', 'level_5.txt'),
    6: os.path.join('levels', 'level_6.txt'),
    7: os.path.join('levels', 'level_7.txt'),
    8: os.path.join('levels', 'level_8.txt')
}

tile_images = {
    '0': pygame.transform.scale(load_image('TEXTURE_0.jpg', papka='texture'), tile_size),
    '1': pygame.transform.scale(load_image('TEXTURE_1.jpg', papka='texture'), tile_size),
    '2': pygame.transform.scale(load_image('TEXTURE_2.jpg', papka='texture'), tile_size),
    '3': pygame.transform.scale(load_image('TEXTURE_3.jpg', papka='texture'), tile_size),
    '#': pygame.transform.scale(load_image('TEXTURE_wall.jpg', papka='texture'), tile_size),
    'empty': pygame.transform.scale(load_image('TEXTURE_pol.jpg', papka='texture'), tile_size),
    'exit': pygame.transform.scale(load_image('exit.jpg', papka='texture'), tile_size)
}

player_k_image = pygame.transform.scale(load_image('PERS_K.png', color_key=None, papka='pers'), pers_size)
player_d_image = pygame.transform.scale(load_image('PERS_D.png', color_key=None, papka='pers'), pers_size)