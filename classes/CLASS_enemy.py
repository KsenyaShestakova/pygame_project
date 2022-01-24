import pygame

from py_files.file_with_const import tile_width, WIDTH, tile_height, HEIGHT, enemy_size
from py_files.file_with_sprite_groups import enemy_group, levels_sprites
from load_img import load_image


class Enemy(pygame.sprite.Sprite):
    enemy1_image = pygame.transform.scale(load_image('bake1.png', color_key=-1, papka='enemy'), enemy_size)
    enemy2_image = pygame.transform.scale(load_image('bake2.png', color_key=-1, papka='enemy'), enemy_size)
    """"enemy3_image = pygame.transform.scale(load_image('bake3.png', color_key=-1), enemy_size)
    enemy4_image = pygame.transform.scale(load_image('bake4.png', color_key=-1), enemy_size)"""

    def __init__(self, type: str, pos_x, pos_y):
        super().__init__(enemy_group, levels_sprites)
        self.type = type
        self.image = Enemy.enemy1_image

        self.rect = self.image.get_rect().move(
            tile_width * pos_x + WIDTH // 240, tile_height * pos_y + HEIGHT // 180)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (pos_x, pos_y)
        self.n = 0
        self.speed_x = 1
        self.speed_y = 1

    def update(self, *args):
        if args:
            pass

    def kill_player(self, player):
        if player.pos == self.pos:
            print(1)
            return False
        return True

    def run(self, level_map):
        self.n += 1
        if self.n % 60 == 0:
            if self.type == '-':
                if level_map[self.pos[1] + self.speed_y][self.pos[0]] in '1230#':
                    self.speed_y *= -1
                level_map[self.pos[1]][self.pos[0]] = '.'
                level_map[self.pos[1] + self.speed_y][self.pos[0]] = '-'
                self.pos = self.pos[0], self.pos[1] + self.speed_y
                self.rect = self.image.get_rect().move(
                    self.rect.x, self.rect.y + tile_height * self.speed_y)
                if self.speed_y < 0:
                    self.image = Enemy.enemy2_image
                else:
                    self.image = Enemy.enemy1_image

            elif self.type == '+':
                if level_map[self.pos[1]][self.pos[0] + self.speed_x] in '1230#':
                    self.speed_x *= -1
                level_map[self.pos[1]][self.pos[0]] = '.'
                level_map[self.pos[1]][self.pos[0] + self.speed_x] = '-'
                self.pos = self.pos[0] + self.speed_x, self.pos[1]
                self.rect = self.image.get_rect().move(
                    self.rect.x + tile_width * self.speed_x, self.rect.y)
                if self.speed_x < 0:
                    self.image = Enemy.enemy1_image
                else:
                    self.image = Enemy.enemy2_image
