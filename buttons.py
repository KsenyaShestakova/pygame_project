import pygame
from file_with_const import btns, all_sprites
from load_img import load_image


class Buttons(pygame.sprite.Sprite):
    def __init__(self, name, pos_x, pos_y, transform_width, transform_height, text=''):
        super().__init__(btns, all_sprites)
        self.image_load = load_image(name)
        self.change_img = load_image(name.split('.')[0] + '_change.' + name.split('.')[1])
        self.text = text
        self.width = transform_width
        self.height = transform_height
        self.x = pos_x
        self.y = pos_y
        self.image = pygame.transform.scale(self.image_load, (transform_width, transform_height))
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.is_clicked = False

    def draw(self, surface, color='black', x=None, y=None):
        if self.text != '':
            font = pygame.font.Font(None, 50)
            text = font.render(self.text, True, color)
            if x and y:
                surface.blit(text, (x, y))
            else:
                text_x = self.x + self.width // 2
                text_y = self.y + self.width // 2
                surface.blit(text, (text_x, text_y))

    def update(self, *args):
        try:
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):
                self.is_clicked = True
            elif args and self.rect.collidepoint(args[0].pos):
                self.image = pygame.transform.scale(self.change_img, (self.width, self.height))
                print(1)
            else:
                self.image = pygame.transform.scale(self.image_load, (self.width, self.height))
                print(2)
        except AttributeError:
            return
