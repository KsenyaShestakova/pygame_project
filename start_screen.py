import pygame

from buttons import Buttons
from file_with_const import WIDTH, HEIGHT, btns, all_sprites, clock, FPS
from load_img import load_image
from terminate import terminate
from window_with_settings import window_with_settings


def start_screen(surface):
    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    surface.blit(fon, (0, 0))
    settings = Buttons('BUTTON_settings.png', 0, 0, 50, 50)
    new_game = Buttons('BUTTON_new_game.png', 700, 200, 350, 250)
    old_game = Buttons('BUTTON_old_game.png', 700, 500, 350, 250)
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

                if new_game.is_clicked and settings.is_clicked is False:
                    # нужно сделать окошко точно ли хочет начать новую игру если есть старая
                    return 'new game'

                if old_game.is_clicked and settings.is_clicked is False:
                    # нужно сделать проверку есть старая игра или нет
                    return 'old game'

        pygame.display.flip()
        clock.tick(FPS)
