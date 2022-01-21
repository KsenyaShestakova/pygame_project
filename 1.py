import pygame

from SCREEN_dead import you_dead
from SCREEN_menu import new_game, game, change_is_open
from file_with_sprite_groups import tiles_group, levels_sprites, player_group, enemy_group, products_group, exit_sprite
from load_img import load_image
from file_with_const import size, HEIGHT, WIDTH, menu_running, FPS, levels, \
    pers_size, \
    tile_width, tile_height, tile_images, screen, clock, enemy_size,\
    tile_size, player_d_image, \
    player_k_image
from SCREEN_menu import menu
from SCREEN_start import start_screen
from SCREEN_story import story
from terminate import terminate
from file_new import LEVEL_NOW


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


class Enemy(pygame.sprite.Sprite):
    enemy1_image = pygame.transform.scale(load_image('bake1.png', color_key=-1, papka='enemy'), enemy_size)
    enemy2_image = pygame.transform.scale(load_image('bake2.png', color_key=-1, papka='enemy'), enemy_size)
    """"enemy3_image = pygame.transform.scale(load_image('bake3.png', color_key=-1), enemy_size)
    enemy4_image = pygame.transform.scale(load_image('bake4.png', color_key=-1), enemy_size)"""

    def __init__(self, type: str, pos_x, pos_y):
        super().__init__(enemy_group, levels_sprites)
        self.type = type
        if type == '-':
            self.image = Enemy.enemy2_image
        elif type == '+':
            self.image = Enemy.enemy1_image

        self.rect = self.image.get_rect().move(
            tile_width * pos_x + WIDTH // 120, tile_height * pos_y + HEIGHT // 90)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (pos_x, pos_y)
        self.n = 0
        self.speed_x = 1
        self.speed_y = 1

    def update(self, *args):
        if args:
            pass

    def kill_player(self):
        if player.pos == self.pos:
            print(1)
            return False
        return True

    def run(self):
        self.n += 1
        if self.n % 60 == 0:
            if self.type == '-':
                if level_map[self.pos[1] + self.speed_y][self.pos[0]] in '1234#':
                    self.speed_y *= -1
                level_map[self.pos[1]][self.pos[0]] = '.'
                level_map[self.pos[1] + self.speed_y][self.pos[0]] = '-'
                self.pos = self.pos[0], self.pos[1] + self.speed_y
                self.rect = self.image.get_rect().move(
                    self.rect.x, self.rect.y + tile_height * self.speed_y)

            elif self.type == '+':
                if level_map[self.pos[1]][self.pos[0] + self.speed_x] in '1234#':
                    self.speed_x *= -1
                level_map[self.pos[1]][self.pos[0]] = '.'
                level_map[self.pos[1]][self.pos[0] + self.speed_x] = '-'
                self.pos = self.pos[0] + self.speed_x, self.pos[1]
                self.rect = self.image.get_rect().move(
                    self.rect.x + tile_width * self.speed_x, self.rect.y)


class Product(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(products_group, levels_sprites)
        self.image = pygame.transform.scale(load_image(f'{LEVEL_NOW}.png', color_key=-1, papka='product_lvl'), enemy_size)
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
        super().__init__(exit_sprite, levels_sprites)
        self.image = pygame.transform.scale(load_image('exit.jpg', papka='texture'), tile_size)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.pos = (pos_x, pos_y)

    def update(self, player):
        if player.pos == self.pos and player.product:
            change_is_open('open_levels.txt', LEVEL_NOW)
            return True


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

    return new_player, x, y, enemies, product, exit_new


def move(player, movement):
    x, y = player.pos
    if movement == "up":
        if y > 0 and (level_map[y - 1][x] in ".@*+-|/"):
            player.move(x, y - 1)
    elif movement == "down":
        if y < max_y and (level_map[y + 1][x] in ".@*+-|/"):
            player.move(x, y + 1)
    elif movement == "left":
        if x > 0 and (level_map[y][x - 1] in ".@*+-|/"):
            player.move(x - 1, y)
    elif movement == "right":
        if x < max_x and (level_map[y][x + 1] in ".@*+-|/"):
            player.move(x + 1, y)


def end_lvl():
    global running, camera
    running = False
    camera.dx = 0
    camera.dy = 0
    player.kill()
    for el in levels_sprites:
        el.kill()


pygame.init()

pygame.display.set_caption('Pizza')
camera = Camera()


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
    n = 0
    while running:
        n += 1
        is_pressed = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move(player, 'up')
                    is_pressed = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move(player, "down")
                    is_pressed = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move(player, "left")
                    is_pressed = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move(player, "right")
                    is_pressed = False
                n -= n % 20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end_lvl()
                    continue

                elif event.key == pygame.K_q:
                    change_is_open('open_levels.txt', LEVEL_NOW)
                    end_lvl()
                    continue

        if is_pressed:
            if (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]) and n % 20 == 0:
                move(player, 'up')
            elif (pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]) and n % 20 == 0:
                move(player, "down")
            elif (pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]) and n % 20 == 0:
                move(player, "left")
            elif (pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]) and n % 20 == 0:
                move(player, "right")

        for sprite in tiles_group:
            camera.apply(sprite)
        for sprite in enemy_group:
            camera.apply(sprite)
        for sprite in products_group:
            camera.apply(sprite)

        for el in enemies:
            el.run()
            if not el.kill_player():
                you_dead(screen)
                end_lvl()
                continue

        if exit_new.update(player):

            end_lvl()
            continue

        if product.update(player):
            product.kill()

        screen.fill((149, 66, 110))
        camera.update(player)
        tiles_group.draw(screen)
        player_group.draw(screen)
        enemy_group.draw(screen)
        products_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


pygame.display.quit()
pygame.quit()