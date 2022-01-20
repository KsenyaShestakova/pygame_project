import pygame

from file_with_const import WIDTH, HEIGHT, clock, FPS
from load_img import load_image
from terminate import terminate


def you_dead(surface):
    """fon = pygame.transform.scale(load_image('dead_pechkoy.jpg'), (WIDTH, HEIGHT))
    surface.blit(fon, (0, 0))

    font = pygame.font.SysFont('arial', HEIGHT // 25)
    text = font.render('*НАЖМИТЕ НА ЛЮБУЮ КЛАВИШУ ДЛЯ ПРОДОЛЖЕНИЯ*', True, 'dark red')
    text_x = WIDTH * 0.1
    text_y = HEIGHT * 0.8"""

    fon = pygame.transform.scale(load_image('killing_window.png'), (WIDTH, HEIGHT))
    surface.blit(fon, (0, 0))
    while True:

        """surface.blit(text, (text_x, text_y))"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.flip()
        clock.tick(FPS)