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
RED = (255, 0, 0)

# Set up the square
square_size = 80
square_color = WHITE
square_position_x = 0
square_position_y = 0

# player
player_x = 120
player_y = 120
player_speed = 2
player = pygame.image.load('player.png').convert_alpha()
player = pygame.transform.rotozoom(player, 0, 0.1)

def drawLevel():
    count = 0
    for row in range(9):
        for col in range(16):
            if level_map[count] == 1:
                x = col * (square_size)
                y = row * (square_size)
                pygame.draw.rect(screen, WHITE, (x, y, square_size - 5, square_size - 5))
            count += 1

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
        keys = pygame.key.get_pressed()

    # Update player position based on keys
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    screen.fill((0,0,0))
    drawLevel()
    # pygame.draw.circle(screen, RED, (500, 500), 25)
    player_rect = player.get_rect(midbottom = (player_x, player_y))
    screen.blit(player, player_rect)
    pygame.display.update()
    pygame.time.Clock().tick(60)
