import pygame

from py_files.file_with_const import WIDTH, HEIGHT, clock, FPS
from load_img import load_image
from terminate import terminate


def instruction(surface):
    intro_text = ['Esc - для выхода',
                  '',
                  'Enter - для подтверждения',
                  '',
                  '    W  ',
                  'A  S  D - для движения',
                  '(или используйте стрелочки)',
                  '',
                  'Q - быстрое прохождение уровня']

    font = pygame.font.SysFont('arial', HEIGHT // 15)
    text_coord = HEIGHT // 12
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = WIDTH // 12
        text_coord += intro_rect.height
        surface.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.flip()
        clock.tick(FPS)