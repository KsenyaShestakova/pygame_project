import pygame

from classes.buttons import Buttons
from py_files.file_with_const import WIDTH, HEIGHT, clock, FPS
from py_files.file_with_sprite_groups import btns, all_sprites
from load_img import load_image
from terminate import terminate
from screens.window_with_settings import window_with_settings


def start_screen(surface):
    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    surface.blit(fon, (0, 0))
    settings = Buttons('BUTTON_settings.png', 0, 0, WIDTH // 24, WIDTH // 24, is_pr=-1)
    new_game = Buttons('BUTTON_new_game.png', WIDTH // 1.714, HEIGHT // 4.5, WIDTH // 3.43, HEIGHT // 3.6)
    old_game = Buttons('BUTTON_old_game.png', WIDTH // 1.714, HEIGHT // 1.8, WIDTH // 3.43, HEIGHT // 3.6)
    btns.draw(surface)
    while True:
        for event in pygame.event.get():
            all_sprites.update(event)

            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:

                if settings.is_clicked:
                    print('settings')
                    window_with_settings(surface)

                    settings.is_clicked = False

                if new_game.is_clicked:
                    for el in all_sprites:
                        el.kill()
                    return 'new game'

                if old_game.is_clicked:
                    for el in all_sprites:
                        el.kill()
                    return 'old game'

        surface.blit(fon, (0, 0))
        btns.draw(surface)
        pygame.display.flip()
        clock.tick(FPS)
