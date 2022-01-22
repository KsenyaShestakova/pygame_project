import pygame

from screens.SCREEN_dead import you_dead
from screens.SCREEN_menu import change_is_open
from game_func.end_level import end_lvl
from py_files.file_with_const import clock, FPS
from py_files.file_with_sprite_groups import tiles_group, enemy_group, products_group, player_group
from game_func.go_player import go
from game_func.run_player import run
from terminate import terminate


def play(surface, size: (int, int), player, camera, level_map, max_s: (int, int), enemies, product, exit_new, lvl_now):
    running = True
    n = 0
    while running:
        n += 1
        is_pressed = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN:
                is_pressed = go(event, player, level_map, max_s[0], max_s[1])
                n -= n % 20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end_lvl(camera, player)
                    return

                elif event.key == pygame.K_q:
                    change_is_open('../game_func/open_levels.txt', lvl_now)
                    end_lvl(camera, player)
                    return

        if is_pressed:
            run(player, n, level_map, max_s[0], max_s[1])

        for sprite in tiles_group:
            camera.apply(sprite)
        for sprite in enemy_group:
            camera.apply(sprite)
        for sprite in products_group:
            camera.apply(sprite)

        for el in enemies:
            el.run(level_map)
            if not el.kill_player(player):
                you_dead(surface)
                end_lvl(camera, player)
                return

        if exit_new.exit(player):
            end_lvl(camera, player)
            return

        if product.update(player):
            product.kill()

        surface.fill((149, 66, 110))
        camera.update(player)
        tiles_group.draw(surface)
        player_group.draw(surface)
        enemy_group.draw(surface)
        products_group.draw(surface)
        pygame.display.flip()
        clock.tick(FPS)