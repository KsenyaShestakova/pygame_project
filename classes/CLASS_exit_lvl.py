import pygame

from screens.SCREEN_menu import change_is_open
from py_files.file_with_const import tile_size, tile_width, tile_height
from py_files.file_with_sprite_groups import exit_sprite, levels_sprites
from load_img import load_image


class ExitLevel(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, level_now):
        super().__init__(exit_sprite, levels_sprites)
        self.image = pygame.transform.scale(load_image('exit.jpg', papka='texture'), tile_size)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.pos = (pos_x, pos_y)
        self.level = level_now

    def exit(self, player):
        if player.pos == self.pos and player.product:
            change_is_open('open_levels.txt', self.level)
            return True
