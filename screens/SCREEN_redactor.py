import os
import pygame
from py_files.file_with_const import clock, FPS
from load_img import load_image
from terminate import terminate
from classes.buttons import Buttons
from py_files.file_with_sprite_groups import btns, all_sprites

pygame.init()
red_group = pygame.sprite.Group()


def redactor(surface, size: (int, int)):
    with open(os.path.join('game_func', 'open_levels.txt'), 'r') as file:
        levels = list(line.split() for line in file)
    levels = list(map(int, levels[0]))

    FIRST_LEVEL = levels[0]
    SECOND_LEVEL = levels[1]
    THIRD_LEVEL = levels[2]
    FOURTH_LEVEL = levels[3]
    FIFTH_LEVEL = levels[4]
    SIXTH_LEVEL = levels[5]
    SEVENTH_LEVEL = levels[6]
    EIGHT_LEVEL = levels[7]
    levels = [FIRST_LEVEL, SECOND_LEVEL, THIRD_LEVEL, FOURTH_LEVEL, FIFTH_LEVEL,
              SIXTH_LEVEL, SEVENTH_LEVEL, EIGHT_LEVEL]
    n = levels.count(True)
    WIDTH, HEIGHT = size
    fon = pygame.transform.scale(load_image(f'red{n}.png'), (WIDTH, HEIGHT))
    sauce = pygame.transform.scale(load_image('sauce_on.png'), (WIDTH, HEIGHT))
    cheese = pygame.transform.scale(load_image('cheese_on.png'), (WIDTH, HEIGHT))
    tomato = pygame.transform.scale(load_image('tomato_on.png'), (WIDTH // 15, HEIGHT // 11.25))
    pepper = pygame.transform.scale(load_image('pepper_on.png'), (WIDTH // 15, HEIGHT // 11.25))
    onion = pygame.transform.scale(load_image('onion_on.png'), (WIDTH // 15, HEIGHT // 11.25))
    masl = pygame.transform.scale(load_image('masl_on.png'), (WIDTH // 15, HEIGHT // 11.25))
    pepperoni = pygame.transform.scale(load_image('pepperoni_on.png'), (WIDTH // 15, HEIGHT // 11.25))
    bake = pygame.transform.scale(load_image('baking.png'), (WIDTH, HEIGHT))

    centre = (WIDTH // 60 + (WIDTH // 2.087) // 2, HEIGHT // 5 + (HEIGHT // 1.6981) // 2)
    radius = WIDTH // 4.1667
    surface.blit(fon, (0, 0))

    btn_bake = Buttons('baking.jpg', WIDTH // 1.96, HEIGHT // 1.22, WIDTH // 8.96, HEIGHT // 6.72)
    btn_go_menu = Buttons('go_to_menu.jpg', WIDTH // 40, HEIGHT // 30, WIDTH // 2.08, HEIGHT // 7.03)
    btn_clean = Buttons('clean.jpg', WIDTH // 40, HEIGHT // 1.22, WIDTH // 2.08, HEIGHT // 6.72)
    btn_clean.add(red_group)
    btn_bake.add(red_group)
    btn_go_menu.add(red_group)

    while True:

        red_group.draw(surface)
        for event in pygame.event.get():
            red_group.update(event)
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN and btn_go_menu.is_clicked:
                for el in red_group:
                    el.kill()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and btn_clean.is_clicked:
                surface.blit(fon, (0, 0))
                btn_clean.is_clicked = False

            if event.type == pygame.MOUSEBUTTONDOWN and btn_bake.is_clicked:
                surface.blit(bake, (0, 0))
                btn_bake.is_clicked = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    for el in red_group:
                        el.kill()
                    return

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
                                surface.blit(tomato, (event.pos[0] - WIDTH // 30, event.pos[1] - HEIGHT // 22.5))
                                new_running = False

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    return

                if (WIDTH // 1.9512) <= event.pos[0] <= (WIDTH // 1.3825) and \
                        (HEIGHT // 2.8754) <= event.pos[1] <= (HEIGHT // 1.7893) and FIFTH_LEVEL:
                    new_running = True
                    while new_running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                terminate()

                            if event.type == pygame.MOUSEBUTTONDOWN and \
                                    (event.pos[0] - centre[0]) ** 2 + (event.pos[1] - centre[1]) <= radius ** 2:
                                surface.blit(pepperoni, (event.pos[0] - WIDTH // 30, event.pos[1] - HEIGHT // 22.5))
                                new_running = False

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    return

                if (WIDTH // 1.3544) <= event.pos[0] <= (WIDTH // 1.0309) and \
                        (HEIGHT // 1.7045) <= event.pos[1] <= (HEIGHT // 1.2712) and SIXTH_LEVEL:
                    new_running = True
                    while new_running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                terminate()

                            if event.type == pygame.MOUSEBUTTONDOWN and \
                                    (event.pos[0] - centre[0]) ** 2 + (event.pos[1] - centre[1]) <= radius ** 2:
                                surface.blit(pepper, (event.pos[0] - WIDTH // 30, event.pos[1] - HEIGHT // 22.5))
                                new_running = False

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    return

                if (WIDTH // 1.9449) <= event.pos[0] <= (WIDTH // 1.3793) and \
                        (HEIGHT // 1.7408) <= event.pos[1] <= (HEIGHT // 1.257) and SEVENTH_LEVEL:
                    new_running = True
                    while new_running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                terminate()

                            if event.type == pygame.MOUSEBUTTONDOWN and \
                                    (event.pos[0] - centre[0]) ** 2 + (event.pos[1] - centre[1]) <= radius ** 2:
                                surface.blit(onion, (event.pos[0] - WIDTH // 30, event.pos[1] - HEIGHT // 22.5))
                                new_running = False

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    return

                if (WIDTH // 1.5769) <= event.pos[0] <= (WIDTH // 1.0283) and \
                        (HEIGHT // 1.2346) <= event.pos[1] <= (HEIGHT // 1.0477) and EIGHT_LEVEL:
                    new_running = True
                    while new_running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                terminate()

                            if event.type == pygame.MOUSEBUTTONDOWN and \
                                    (event.pos[0] - centre[0]) ** 2 + (event.pos[1] - centre[1]) <= radius ** 2:
                                surface.blit(masl, (event.pos[0] - WIDTH // 30, event.pos[1] - HEIGHT // 22.5))
                                new_running = False

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    return


        pygame.display.flip()
        clock.tick(FPS)
