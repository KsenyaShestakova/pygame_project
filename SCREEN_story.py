import pygame

from file_with_const import WIDTH, HEIGHT, clock, FPS
from load_img import load_image
from terminate import terminate


def story(surface):
    story = pygame.transform.scale(load_image('story.png'), (WIDTH, HEIGHT))
    surface.blit(story, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)