import pygame
from file_with_const import btns, all_sprites
from load_img import load_image


class Buttons(pygame.sprite.Sprite):
    def __init__(self, name, pos_x, pos_y, transform_width, transform_height, text=''):
        super().__init__(btns, all_sprites)
        self.change_img = load_image(name.split('.')[0] + '_change.' + name.split('.')[1])
        self.image_load = load_image(name)

        self.text = text
        self.width = transform_width
        self.height = transform_height
        self.x = pos_x
        self.y = pos_y
        self.image = pygame.transform.scale(self.image_load, (transform_width, transform_height))
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.is_clicked = False
        self.change_img = pygame.transform.scale(self.change_img, (self.width, self.height))
        self.old_img = pygame.transform.scale(self.image_load, (self.width, self.height))

    def draw_text(self, surface, color='black', x=None, y=None):
        if self.text != '':
            font = pygame.font.SysFont('arial', int(self.width // 3))
            text = font.render(self.text, True, color)
            if x and y:
                surface.blit(text, (x, y))
            else:
                text_x = self.x + self.width // 2 - self.width // 13
                text_y = self.y + self.width // 2 - self.height // 7
                surface.blit(text, (text_x, text_y))

    def update(self, *args):
        try:
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):
                self.is_clicked = True
            elif args and self.x <= pygame.mouse.get_pos()[0] <= self.x + self.width and \
                    self.y <= pygame.mouse.get_pos()[1] <= self.y + self.height:
                self.image = self.change_img
            else:
                self.image = self.old_img
        except AttributeError:
            return
