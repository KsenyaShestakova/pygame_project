import os
import sys

import pygame
from load_img import load_image
from file_with_const import size, HEIGHT, WIDTH


class Settings(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(settings_spr, all_sprites)
        self.image_load = load_image('BUTTON_settings.png')
        self.image = pygame.transform.scale(self.image_load, (50, 50))
        self.change_img = load_image('BUTTON_settings.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.is_set = False

    def update(self, *args):
        try:
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):
                self.is_set = True
                print(0)
            elif args and self.rect.collidepoint(args[0].pos):
                self.image = pygame.transform.scale(self.change_img, (50, 50))
                print(5)
            else:
                self.image = pygame.transform.scale(self.image_load, (50, 50))
        except AttributeError:
            print('Вот где была ошибка.....')  # ладно всё равно не работает так как надо

    def is_s(self):
        return self.is_set


class BtnStart(pygame.sprite.Sprite):
    def __init__(self, name, pos_x, pos_y):
        super().__init__(btns, all_sprites)
        self.image_load = load_image(name)
        self.change_img = load_image(name.split('.')[0] + '_change.' + name.split('.')[1])
        self.image = pygame.transform.scale(self.image_load, (350, 250))
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.is_st = False

    def update(self, *args):
        try:
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):
                self.is_st = True
                print(0)
            elif args and self.rect.collidepoint(args[0].pos):
                self.image = pygame.transform.scale(self.image_load, (350, 250))
                print(5)
            else:
                self.image = pygame.transform.scale(self.change_img, (350, 250))
        except AttributeError:
            print('Вот где была ошибка.....')

    def is_start(self):
        return self.is_st


def start_screen():

    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    settings = Settings(0, 0)
    new_game = BtnStart('BUTTON_new_game.png', 700, 200)
    old_game = BtnStart('BUTTON_old_game.png', 700, 500)
    settings_spr.draw(screen)
    btns.draw(screen)
    while True:
        for event in pygame.event.get():
            all_sprites.update(event)
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:

                if settings.is_s():
                    print('settings')
                    window_with_settings()
                    settings.is_set = False

                if new_game.is_start() and settings.is_s() is False:
                    return print('new game')

                if old_game.is_start() and settings.is_s() is False:
                    return print('old game')
        pygame.display.flip()
        clock.tick(FPS)


def window_with_settings():  # при закрытии is_s() возвращает False
    dr_set = pygame.draw.rect(screen, 'black', (WIDTH // 5, HEIGHT // 5, WIDTH // 5 * 3, HEIGHT // 5 * 3))
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(9)

                return
            """elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:

                if settings.is_s():
                    print('settings')
                    window_with_settings()
                    settings.is_set = False

                if new_game.is_start() and settings.is_s() is False:
                    return print('new game')

                if old_game.is_start() and settings.is_s() is False:
                    return print('old game')"""
        pygame.display.flip()
        clock.tick(FPS)


class SettingsWindow(pygame.sprite.Sprite):
    def __init__(self, name, pos_x, pos_y):
        super().__init__(settings_spr, all_sprites)
        self.image_load = load_image(name)
        tile_width, tile_height = self.image_load.get_width(), self.image_load.get_height()
        self.image = pygame.transform.scale(self.image_load, (100, 50))
        self.rect = self.image.get_rect().move(
            tile_width + pos_x, tile_height + pos_y)
        self.is_st = 0

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.is_st += 1
            print(1)


def terminate():
    pygame.quit()
    sys.exit()


def story():
    story = pygame.transform.scale(load_image('story.png'), (WIDTH, HEIGHT))
    screen.blit(story, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    # filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
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
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        camera.dx -= tile_width * (x - self.pos[0])
        camera.dy -= tile_width * (y - self.pos[1])

        level_map[self.pos[1]][self.pos[0]] = '.'
        self.pos = (x, y)
        level_map[self.pos[1]][self.pos[0]] = '@'
        for sprite in tiles_group:
            camera.apply(sprite)


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
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] in '.@':
                Tile('empty', x, y)
            elif level[y][x] in '1230#':
                Tile(str(level[y][x]), x, y)
            elif level[y][x] == '?':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def move(player, movement):
    x, y = player.pos
    if movement == "up":
        if y > 0 and (level_map[y - 1][x] == "." or level_map[y - 1][x] == "@"):
            player.move(x, y - 1)
    elif movement == "down":
        if y < level_y and (level_map[y + 1][x] == "." or level_map[y + 1][x] == "@"):
            player.move(x, y + 1)
    elif movement == "left":
        if x > 0 and (level_map[y][x - 1] == "." or level_map[y][x - 1] == "@"):
            player.move(x - 1, y)
    elif movement == "right":
        if x < level_y and (level_map[y][x + 1] == "." or level_map[y][x + 1] == "@"):
            player.move(x + 1, y)


pygame.init()

pygame.display.set_caption('Pizza')
screen = pygame.display.set_mode(size)
FPS = 50
clock = pygame.time.Clock()
camera = Camera()

tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
settings_spr = pygame.sprite.Group()
btns = pygame.sprite.Group()

tile_images = {
    '0': pygame.transform.scale(load_image('TEXTURE_0.jpg'), (100, 100)),
    '1': pygame.transform.scale(load_image('TEXTURE_1.jpg'), (100, 100)),
    '2': pygame.transform.scale(load_image('TEXTURE_2.jpg'), (100, 100)),
    '3': pygame.transform.scale(load_image('TEXTURE_3.jpg'), (100, 100)),
    '#': pygame.transform.scale(load_image('TEXTURE_wall.jpg'), (100, 100)),
    'empty': pygame.transform.scale(load_image('TEXTURE_pol.jpg'), (100, 100))
}
player_image = load_image('mar.png')

tile_width = tile_height = 100


start_screen()
story()
level_map = load_level('test_map_Dasha.txt')
player, level_x, level_y = generate_level(level_map)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move(player, 'up')
            elif event.key == pygame.K_s:
                move(player, "down")
            elif event.key == pygame.K_a:
                move(player, "left")
            elif event.key == pygame.K_d:
                move(player, "right")
    screen.fill('black')
    camera.update(player)
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.display.quit()
pygame.quit()