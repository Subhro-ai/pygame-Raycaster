import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Raycaster")
clock = pygame.time.Clock()

while True:
    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((255,255,255))
    pygame.display.update()