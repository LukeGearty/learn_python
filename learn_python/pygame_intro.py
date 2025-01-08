import pygame
import sys

window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pygame Intro")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    window.fill('white')
    pygame.display.flip()
    clock.tick(60)