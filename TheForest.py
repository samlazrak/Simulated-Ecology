import pygame
import settings
pygame.init()

gameDisplay = pygame.display.set_mode((settings.display_width,settings.display_height))
pygame.display.set_caption('The Forest')

clock = pygame.time.Clock()

empty = False
while not empty:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            empty = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()