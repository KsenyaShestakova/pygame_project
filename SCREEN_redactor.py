import pygame

import file_new
from buttons import Buttons
from file_with_const import WIDTH, HEIGHT, clock, FPS
from file_with_sprite_groups import redactor_sprites, all_sprites
from load_img import load_image
from SCREEN_menu import FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, \
    FOURTH_LEVEL, FIFTH_LEVEL, SIXTH_LEVEL, SEVENTH_LEVEL, EIGHT_LEVEL

from terminate import terminate

pygame.init()


def redactor(surface):
    fon = pygame.transform.scale(load_image('red.png'), (WIDTH, HEIGHT))
    surface.blit(fon, (0, 0))

    if FIRST_LEVEL:
        pastry = Buttons('1_red.png', WIDTH // 60, HEIGHT // 5.2941, WIDTH // 2.1938,
                         HEIGHT // 1.6453)
    if SECOND_LEVEL:
        cheese = Buttons('2_red.jpg', WIDTH // 1.6, HEIGHT // 1.2295, WIDTH // 7.5949,
                         HEIGHT // 14.2857)
    if THIRD_LEVEL:
        sauce = Buttons('3_red.jpg', WIDTH // 1.6 + WIDTH // 7.5949, HEIGHT // 1.2295 + HEIGHT // 14.2857,
                        WIDTH // 7.5949, HEIGHT // 14.2857)
    if FOURTH_LEVEL:
        tomato = Buttons('4_red.png', WIDTH // 1.9261, HEIGHT // 22.5, WIDTH // 4.3796,
                         HEIGHT // 2.6163)
    if FIFTH_LEVEL:
        pepperoni = Buttons('5_red.png', WIDTH // 1.9261 + WIDTH // 4.3796, HEIGHT // 22.5 + HEIGHT // 2.6163,
                            WIDTH // 4.3796, HEIGHT // 2.6163)
    if SIXTH_LEVEL:
        pass
        #  pepper = Buttons()
    if SEVENTH_LEVEL:
        pass
        #  onion = Buttons()
    if EIGHT_LEVEL:
        pass
        #  olive = Buttons()
    all_sprites.draw(surface)

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN:


        pygame.display.flip()
        clock.tick(FPS)


