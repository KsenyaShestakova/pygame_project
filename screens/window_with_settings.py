import os.path

import pygame

from classes.buttons import Buttons
from py_files.file_with_const import WIDTH, HEIGHT, clock, FPS, get_size
from py_files.file_with_sprite_groups import settings_spr, all_sprites
from load_img import load_image
from terminate import terminate


def window_with_settings(surface):
    surface.blit(pygame.transform.scale(load_image('fon_change.png'), (WIDTH, HEIGHT)), (0, 0))
    save_btn = Buttons('razr_btn.png', WIDTH // 4.28, HEIGHT // 1.52, WIDTH // 4, HEIGHT // 12, text='Сохранить')
    return_btn = Buttons('razr_btn.png', WIDTH // 1.97, HEIGHT // 1.52, WIDTH // 4, HEIGHT // 12, text='Отмена')
    save_btn.add(settings_spr)
    return_btn.add(settings_spr)

    btn_1200_900 = Buttons('razr_btn.png', WIDTH // 4.28, HEIGHT // 3.31, WIDTH // 4, HEIGHT // 12, text='1200*900')
    btn_1000_750 = Buttons('razr_btn.png', WIDTH // 4.28, HEIGHT // 2.41, WIDTH // 4, HEIGHT // 12, text='1000*750')
    btn_800_600 = Buttons('razr_btn.png', WIDTH // 4.28, HEIGHT // 1.89, WIDTH // 4, HEIGHT // 12, text='800*600')
    btn_1200_900.add(settings_spr)
    btn_1000_750.add(settings_spr)
    btn_800_600.add(settings_spr)

    fon = pygame.transform.scale(load_image('settings.png'), (WIDTH // 5 * 3, HEIGHT // 5 * 3))
    surface.blit(fon, (WIDTH // 5, HEIGHT // 5))

    OLD_SIZE = str(' '.join(map(str, get_size(os.path.join('py_files', 'window_size.txt')))))

    while True:
        for event in pygame.event.get():
            settings_spr.update(event)
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    for el in settings_spr:
                        el.kill()
                    return

                elif event.key == pygame.K_KP_ENTER:
                    for el in settings_spr:
                        if el.is_clicked:
                            el.is_clicked = False
                            save(el.text, 'window_size.txt', 'py_files')

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_btn.is_clicked:
                    save(OLD_SIZE, 'window_size.txt', 'py_files')
                    for el in settings_spr:
                        if el.is_clicked:
                            el.is_clicked = False

                if save_btn.is_clicked:
                    save_btn.is_clicked = False
                    for el in settings_spr:
                        if el.is_clicked:
                            el.is_clicked = False
                            save(el.text, 'window_size.txt', 'py_files')

        settings_spr.draw(surface)
        print_text(surface)
        for el in settings_spr:
            el.draw_text(surface, 'white', size_sh=HEIGHT // 20)
        pygame.display.flip()
        clock.tick(FPS)


def save(size: str, filename, papka=None):
    size = size.replace('*', ' ')
    if papka:
        print(size)
        filename = os.path.join(papka, filename)
    with open(filename, 'w') as file:
        file.write(size)


def print_text(surface):
    intro_text = ["После",
                  'поддтверждения',
                  'о сохранении',
                  'перезайдите',
                  'в игру']

    font = pygame.font.SysFont('arial', 30)
    text_coord = 200
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 500
        text_coord += intro_rect.height
        surface.blit(string_rendered, intro_rect)
