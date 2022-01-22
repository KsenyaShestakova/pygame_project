import pygame

from py_files.file_with_const import tile_width, tile_height, enemy_size
from py_files.file_with_sprite_groups import products_group, levels_sprites
from load_img import load_image


class Product(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, level):
        super().__init__(products_group, levels_sprites)
        self.image = pygame.transform.scale(load_image(f'{level}.png', color_key=-1, papka='product_lvl'), enemy_size)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (pos_x, pos_y)

    def update(self, player):
        if player.pos == self.pos:
            player.product = True
            return True
