import pygame

from game_func.move import move


def go(event, obj, level_map, max_x, max_y):
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        move(obj, 'up', level_map, max_x, max_y)
        return False
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        move(obj, "down", level_map, max_x, max_y)
        return False
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        move(obj, "left", level_map, max_x, max_y)
        return False
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        move(obj, "right", level_map, max_x, max_y)
        return False
