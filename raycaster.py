import pygame
from sys import exit

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Raycaster")
clock = pygame.time.Clock()

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the square
square_size = 80
square_color = WHITE
square_position_x = 0
square_position_y = 0

level_map = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
             1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

while True:
    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))
    count = 0
    for row in range(9):
        for col in range(16):
            if level_map[count] == 1:
                x = col * (square_size)
                y = row * (square_size)
                pygame.draw.rect(screen, WHITE, (x, y, square_size - 5, square_size - 5))
            count += 1
        
    pygame.display.update()