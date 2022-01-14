import sys

import pygame

from SCREEN_menu import new_game, game, FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, FOURTH_LEVEL, \
    change_is_open
from load_img import load_image
from file_with_const import size, HEIGHT, WIDTH, \
    all_sprites, btns, settings_spr, tiles_group, player_group, menu_running, FPS, levels, \
    pers_size, \
    tile_width, tile_height, tile_images, screen, clock, enemy_size, enemy_group, products_group, \
    tile_size, exit_sprite
from SCREEN_menu import menu
from SCREEN_start import start_screen
from SCREEN_story import story
from terminate import terminate
from file_new import LEVEL_NOW


def load_level(filename):
    # filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        if LEVEL_NOW % 2 == 0:
            self.image = player_d_image
        else:
            self.image = player_k_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + WIDTH // 80, tile_height * pos_y + HEIGHT // 180)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (pos_x, pos_y)
        self.product = False

    def move(self, x, y):
        camera.dx -= tile_width * (x - self.pos[0])
        camera.dy -= tile_width * (y - self.pos[1])

        level_map[self.pos[1]][self.pos[0]] = '.'
        self.pos = (x, y)
        level_map[self.pos[1]][self.pos[0]] = '@'


class Enemy(pygame.sprite.Sprite):
    def __init__(self, type, pos_x, pos_y):
        super().__init__(enemy_group, all_sprites)
        self.type = type
        if type == '-':
            self.image = enemy2_image
        elif type == '+':
            self.image = enemy1_image
        elif type == "|":
            self.image = enemy3_image
        elif type == '/':
            self.image = enemy4_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (pos_x, pos_y)
        print("enemy init")


class Product(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(products_group, all_sprites)
        self.image = pygame.transform.scale(load_image(f'{LEVEL_NOW}.png', color_key=-1), enemy_size)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (pos_x, pos_y)

    def update(self, player):
        if player.pos == self.pos:
            player.product = True
            return True


class ExitLevel(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(exit_sprite)
        self.image = pygame.transform.scale(load_image('exit.jpg'), tile_size)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.pos = (pos_x, pos_y)

    def update(self, player):
        if player.pos == self.pos and player.product:
            change_is_open('open_levels.txt', LEVEL_NOW)
            return True

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = 0
        self.dy = 0


def generate_level(level):
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
                product = Product(x, y)
    print(enemies)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y, enemies, product, exit_new


def move(player, movement):
    x, y = player.pos
    if movement == "up":
        if y > 0 and (level_map[y - 1][x] == "." or level_map[y - 1][x] == "@" or level_map[y - 1][x] == '*'):
            player.move(x, y - 1)
    elif movement == "down":
        if y < max_y and (level_map[y + 1][x] == "." or level_map[y + 1][x] == "@" or level_map[y + 1][x] == '*'):
            player.move(x, y + 1)
    elif movement == "left":
        if x > 0 and (level_map[y][x - 1] == "." or level_map[y][x - 1] == "@" or level_map[y][x - 1] == '*'):
            player.move(x - 1, y)
    elif movement == "right":
        if x < max_x and (level_map[y][x + 1] == "." or level_map[y][x + 1] == "@" or level_map[y][x + 1] == '*'):
            player.move(x + 1, y)


pygame.init()

pygame.display.set_caption('Pizza')
camera = Camera()


player_k_image = pygame.transform.scale(load_image('PERS_K.png', color_key=None), pers_size)
player_d_image = pygame.transform.scale(load_image('PERS_D.png', color_key=None), pers_size)

enemy1_image = pygame.transform.scale(load_image('bake1.png', color_key=-1), enemy_size)
enemy2_image = pygame.transform.scale(load_image('bake2.png', color_key=-1), enemy_size)
enemy3_image = pygame.transform.scale(load_image('bake3.png', color_key=-1), enemy_size)
enemy4_image = pygame.transform.scale(load_image('bake4.png', color_key=-1), enemy_size)


if start_screen(screen) == 'new game':
    new_game('open_levels.txt')
    story(screen)

while menu_running:
    game('open_levels.txt')

    level = menu(screen)
    LEVEL_NOW = level
    level_map = load_level(levels[level])
    player, max_x, max_y, enemies, product, exit_new = generate_level(level_map)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move(player, 'up')
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move(player, "down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move(player, "left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move(player, "right")
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    player.kill()
                    for el in tiles_group:
                        el.kill()
        for sprite in tiles_group:
            camera.apply(sprite)
        for sprite in enemy_group:
            camera.apply(sprite)
        for sprite in products_group:
            camera.apply(sprite)
        if exit_new.update(player):
            running = False
            player.kill()
            for el in tiles_group:
                el.kill()
        if product.update(player):
            product.kill()

        screen.fill('black')
        camera.update(player)
        tiles_group.draw(screen)
        player_group.draw(screen)
        enemy_group.draw(screen)
        products_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


pygame.display.quit()
pygame.quit()