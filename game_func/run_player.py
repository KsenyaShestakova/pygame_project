import pygame

from game_func.move import move


def run(player, n, level_map, max_x, max_y):
    if (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]) and n % 20 == 0:
        move(player, 'up', level_map, max_x, max_y)
    elif (pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]) and n % 20 == 0:
        move(player, "down", level_map, max_x, max_y)
    elif (pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]) and n % 20 == 0:
        move(player, "left", level_map, max_x, max_y)
    elif (pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]) and n % 20 == 0:
        move(player, "right", level_map, max_x, max_y)