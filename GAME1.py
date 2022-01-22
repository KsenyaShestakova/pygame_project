import os.path

import pygame

from classes.CLASS_product import Product
from classes.CLASS_enemy import Enemy
from classes.CLASS_exit_lvl import ExitLevel
from screens.SCREEN_menu import new_game, game
from screens.SCREEN_redactor import redactor
from py_files.file_with_sprite_groups import tiles_group, levels_sprites, player_group
from screens.SCREEN_game import play
from py_files.file_with_const import HEIGHT, WIDTH, menu_running, levels, \
    tile_width, tile_height, tile_images, screen, player_d_image, \
    player_k_image
from screens.SCREEN_menu import menu
from screens.SCREEN_start import start_screen
from screens.SCREEN_story import story
from py_files.file_new import LEVEL_NOW


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, levels_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, levels_sprites)
        if LEVEL_NOW % 2 == 0:
            self.image = player_d_image
        else:
            self.image = player_k_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + WIDTH // 80, tile_height * pos_y + HEIGHT // 180)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (pos_x, pos_y)
        self.product = False
        camera.dx = pos_x
        camera.dy = pos_y

    def move(self, x, y):
        camera.dx -= tile_width * (x - self.pos[0])
        camera.dy -= tile_width * (y - self.pos[1])

        level_map[self.pos[1]][self.pos[0]] = '.'
        self.pos = (x, y)
        level_map[self.pos[1]][self.pos[0]] = '?'


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = 0
        self.dy = 0


def generate_level(level, lvl_now):
    new_player, x, y, enemies, product = None, None, None, [], None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] in '.':
                Tile('empty', x, y)
            elif level[y][x] in '1230#':
                Tile(str(level[y][x]), x, y)
            elif level[y][x] == '?':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] in '+-|/':
                Tile('empty', x, y)
                new_enemy = Enemy(str(level[y][x]), x, y)
                enemies.append(new_enemy)
            elif level[y][x] == '@':
                Tile('exit', x, y)
                exit_new = ExitLevel(x, y)
            elif level[y][x] == '*':
                Tile('empty', x, y)
                product = Product(x, y, lvl_now)

    return new_player, x, y, enemies, product, exit_new


pygame.init()

pygame.display.set_caption('Pizza')
camera = Camera()

if start_screen(screen) == 'new game':
    new_game(os.path.join('game_func', 'open_levels.txt'))
    story(screen)

while menu_running:
    game(os.path.join('game_func', 'open_levels.txt'))

    level = menu(screen)

    if type(level) == int:
        LEVEL_NOW = level
        level_map = load_level(levels[level])
        player, max_x, max_y, enemies, product, exit_new = generate_level(level_map, LEVEL_NOW)
        play(screen, (1200, 900), player,
             camera, level_map, (max_x, max_y),
             enemies, product, exit_new, LEVEL_NOW)

    else:
        redactor(screen, (1200, 900))


pygame.display.quit()
pygame.quit()