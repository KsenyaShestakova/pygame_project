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
    levels = [FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, FOURTH_LEVEL, FIFTH_LEVEL,
              SIXTH_LEVEL, SEVENTH_LEVEL, EIGHT_LEVEL]
    n = levels.count(True)
    fon = pygame.transform.scale(load_image(f'red{n}.png'), (WIDTH, HEIGHT))
    sauce = pygame.transform.scale(load_image('sauce_on.png'), (WIDTH, HEIGHT))
    cheese = pygame.transform.scale(load_image('cheese_on.png'), (WIDTH, HEIGHT))
    surface.blit(fon, (0, 0))

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN and FIRST_LEVEL:
                if (WIDTH // 1.9355) <= event.pos[0] <= (WIDTH // 1.4052) and \
                        (HEIGHT // 45) <= event.pos[1] <= (HEIGHT // 3.169) and THIRD_LEVEL:
                    surface.blit(sauce, (0, 0))
                if (WIDTH // 1.362) <= event.pos[0] <= (WIDTH // 1.0345) and \
                        (HEIGHT // 37.5) <= event.pos[1] <= (HEIGHT // 3.3582) and SECOND_LEVEL:
                    surface.blit(cheese, (0, 0))


        pygame.display.flip()
        clock.tick(FPS)


