import pygame

from file_with_const import WIDTH, HEIGHT, clock, FPS
from terminate import terminate


def window_with_settings(surface):  # при закрытии is_s() возвращает False
    dr_set = pygame.draw.rect(surface, 'black', (WIDTH // 5, HEIGHT // 5, WIDTH // 5 * 3, HEIGHT // 5 * 3))
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(9)
                return

        pygame.display.flip()
        clock.tick(FPS)