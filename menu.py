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
    levels_is_open = [FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, FOURTH_LEVEL,
              FIFTH_LEVEL, SIXTH_LEVEL, SEVENTH_LEVEL, EIGHT_LEVEL]
    coords = []
    for i in range(8):
        coords.append(COORDS[i + 1])
    levels = []
    for coord, i, lvl_is_op in zip(coords, range(1, 9), levels_is_open):
        levels.append(LevelBtn(coord, (WIDTH / 6, WIDTH / 6), i, lvl_is_op))

    lvl_btn.draw(surface)
    for el in lvl_btn:
        el.draw_text(surface)
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:

                pass
            lvl_btn.update(event)
        pygame.display.flip()
        clock.tick(FPS)
"""     lvl1 = LevelBtn(COORDS[1], (WIDTH / 6, WIDTH / 6), 1, FIRST_LEVEL)
        lvl2 = LevelBtn(COORDS[2], (WIDTH / 6, WIDTH / 6), 2, SECOND_LEVEL)
        lvl3 = LevelBtn(COORDS[3], (WIDTH / 6, WIDTH / 6), 3, THIRD_LEVEL)
        lvl4 = LevelBtn(COORDS[4], (WIDTH / 6, WIDTH / 6), 4, FOURTH_LEVEL)
        lvl5 = LevelBtn(COORDS[5], (WIDTH / 6, WIDTH / 6), 5, FIFTH_LEVEL)
        lvl6 = LevelBtn(COORDS[6], (WIDTH / 6, WIDTH / 6), 6, SIXTH_LEVEL)
        lvl7 = LevelBtn(COORDS[7], (WIDTH / 6, WIDTH / 6), 7, SEVENTH_LEVEL)
        lvl8 = LevelBtn(COORDS[8], (WIDTH / 6, WIDTH / 6), 8, EIGHT_LEVEL)
    """

def render_coords():
    global COORDS
    for i in range(4):
        x, y = int(WIDTH / 12 + WIDTH / 6 * i + WIDTH // 18 * i), int(WIDTH / 10)
        COORDS[i + 1] = (x, y)
        y += int(WIDTH * 5 / 24)
        COORDS[i + 5] = (x, y)


class LevelBtn(Buttons):
    level_img_otkr = 'open_level.png'

    def __init__(self, coords: tuple, transform: tuple, lvl_number, is_open):
        Buttons.__init__(self, name=LevelBtn.level_img_otkr, pos_x=coords[0],
                         pos_y=coords[1], transform_width=transform[0],
                         transform_height=transform[1], text=str(lvl_number))
        pygame.sprite.Sprite.__init__(self, lvl_btn, all_sprites)

        self.number = lvl_number
        self.is_open = is_open

COORDS = {}
render_coords()
menu(screen)