import pygame

from buttons import Buttons
from file_with_const import WIDTH, HEIGHT, btns, all_sprites, terminate, clock, FPS
from load_img import load_image
from file_new import FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, FIFTH_LEVEL,\
    FOURTH_LEVEL, SIXTH_LEVEL, SEVENTH_LEVEL, EIGHT_LEVEL

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
lvl_btn = pygame.sprite.Group()


def menu(surface):
    fon = pygame.transform.scale(load_image('menu_of_lvls.png'), (WIDTH, HEIGHT))
    surface.blit(fon, (0, 0))
    do_buttons(surface)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                """"if event.key == pygame.K_ESCAPE:
                    terminate()"""
                pass
            for el in lvl_btn:
                lvl = el.update(event)
                if lvl:
                    return lvl
        pygame.display.flip()
        clock.tick(FPS)


def render_coords():
    COORDS = {}
    for i in range(4):
        x, y = int(WIDTH / 12 + WIDTH / 6 * i + WIDTH // 18 * i), int(WIDTH / 10)
        COORDS[i + 1] = (x, y)
        y += int(WIDTH * 5 / 24)
        COORDS[i + 5] = (x, y)
    return COORDS


def do_buttons(surface):
    levels_is_open = [True, FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, FOURTH_LEVEL,
                      FIFTH_LEVEL, SIXTH_LEVEL, SEVENTH_LEVEL]
    coords = []
    COORDS = render_coords()
    size_button = (WIDTH / 6, WIDTH / 6)
    for i in range(8):
        coords.append(COORDS[i + 1])
    levels = []
    for coord, i, lvl_is_op in zip(coords, range(1, 9), levels_is_open):
        levels.append(LevelBtn(coord, size_button, i, lvl_is_op))

    lvl_btn.draw(surface)
    for el in lvl_btn:
        if el.is_open:
            el.draw_text(surface, (223, 93, 71))


class LevelBtn(Buttons):
    level_img_otkr = 'open_level.png'
    level_img_not_otkr = "close_level.png"

    def __init__(self, coords: tuple, transform: tuple, lvl_number, is_open):
        if is_open:
            img = LevelBtn.level_img_otkr
        else:
            img = LevelBtn.level_img_not_otkr

        Buttons.__init__(self, name=img, pos_x=coords[0],
                         pos_y=coords[1], transform_width=transform[0],
                         transform_height=transform[1], text=str(lvl_number))
        pygame.sprite.Sprite.__init__(self, lvl_btn, all_sprites)

        self.number = lvl_number
        self.is_open = is_open

    def update(self, *args):
        try:
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos) and self.is_open:
                print(self.number)
                return self.number
            elif args and self.x <= pygame.mouse.get_pos()[0] <= self.x + self.width and \
                    self.y <= pygame.mouse.get_pos()[1] <= self.y + self.height:
                self.image = self.change_img
            else:
                self.image = self.old_img
        except AttributeError:
            return

    def get_level_number(self):
        return self.number

