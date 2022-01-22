import pygame

import py_files.file_new
from classes.buttons import Buttons
from py_files.file_with_const import WIDTH, HEIGHT, clock, FPS
from py_files.file_with_sprite_groups import redactor_sprites, all_sprites
from load_img import load_image
from screens.SCREEN_menu import FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, \
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
    tomato = pygame.transform.scale(load_image('tomato_on.png'), (WIDTH // 15, HEIGHT // 15))
    pepperoni = pygame.transform.scale(load_image('pepperoni_on.png'), (WIDTH // 15, HEIGHT // 15))
    centre = (WIDTH // 60 + (WIDTH // 2.087) // 2, HEIGHT // 5 + (HEIGHT // 1.6981) // 2)
    radius = WIDTH // 4.1667
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
                if (WIDTH // 1.3483) <= event.pos[0] <= (WIDTH // 1.0327) and \
                        (HEIGHT // 3.0508) <= event.pos[1] <= (HEIGHT // 1.7613) and FOURTH_LEVEL:
                    new_running = True
                    while new_running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                terminate()

                            if event.type == pygame.MOUSEBUTTONDOWN and \
                                    (event.pos[0] - centre[0]) ** 2 + (event.pos[1] - centre[1]) <= radius ** 2:
                                surface.blit(tomato, event.pos)
                                new_running = False
                if (WIDTH // 1.9512) <= event.pos[0] <= (WIDTH // 1.3825) and \
                        (HEIGHT // 2.8754) <= event.pos[1] <= (HEIGHT // 1.7893) and FIFTH_LEVEL:
                    new_running = True
                    while new_running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                terminate()

                            if event.type == pygame.MOUSEBUTTONDOWN and \
                                    (event.pos[0] - centre[0]) ** 2 + (event.pos[1] - centre[1]) <= radius ** 2:
                                surface.blit(pepperoni, event.pos)
                                new_running = False


        pygame.display.flip()
        clock.tick(FPS)

