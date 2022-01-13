import sys

import pygame

from SCREEN_menu import new_game, game, FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, FOURTH_LEVEL
from load_img import load_image
from file_with_const import size, HEIGHT, WIDTH, \
    all_sprites, btns, settings_spr, tiles_group, player_group, menu_running, FPS, levels, pers_size, \
    tile_width, tile_height, tile_images, screen, clock
from SCREEN_menu import menu
from SCREEN_start import start_screen
from SCREEN_story import story
from terminate import terminate


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
        self.image = player_k_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.mask = pygame.mask.from_surface(self.image)
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
        if y < max_y and (level_map[y + 1][x] == "." or level_map[y + 1][x] == "@"):
            player.move(x, y + 1)
    elif movement == "left":
        if x > 0 and (level_map[y][x - 1] == "." or level_map[y][x - 1] == "@"):
            player.move(x - 1, y)
    elif movement == "right":
        if x < max_x and (level_map[y][x + 1] == "." or level_map[y][x + 1] == "@"):
            player.move(x + 1, y)


pygame.init()

pygame.display.set_caption('Pizza')
camera = Camera()


player_k_image = pygame.transform.scale(load_image('PERS_K.png', color_key=-1), pers_size)
player_d_image = pygame.transform.scale(load_image('PERS_D.png', color_key=-1), pers_size)


if start_screen(screen) == 'new game':
    new_game('open_levels.txt')
    story(screen)

while menu_running:
    game('open_levels.txt')
    print(FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, FOURTH_LEVEL)
    level = menu(screen)

    level_map = load_level(levels[level])
    player, max_x, max_y = generate_level(level_map)

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
        screen.fill('black')
        camera.update(player)
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


pygame.display.quit()
pygame.quit()