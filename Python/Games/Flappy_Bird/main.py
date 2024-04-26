import pygame
import sys 

pygame.init()

# Einstellungen für den Bildschirm
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800

# Spieler Startposition
player_x = WINDOW_WIDTH // 2
player_y = WINDOW_HEIGHT // 2

movex = 0
movey = 0
gravity = 0.25
player_speed = 5

# Bildschirm und Hintergrund
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_image = pygame.image.load("D:/Projects/Python/Games/Flappy_Bird/assets/background-day.png").convert()
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Spieler Sprite
player_image = pygame.image.load("D:/Projects/Python/Games/Flappy_Bird/assets/redbird-downflap.png").convert()

clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Bewegung des Spielers
    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_d] - keys[pygame.K_a]) * player_speed
    player_y += (keys[pygame.K_s] - keys[pygame.K_w]) * player_speed 

    # Begrenzung der Spielerposition auf dem Bildschirm
    player_x = max(0, min(WINDOW_WIDTH - player_image.get_width(), player_x))
    player_y = max(0, min(WINDOW_HEIGHT - player_image.get_height(), player_y))
            
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))


    pygame.display.update()
    clock.tick(60)
