import pygame
from global_var import *

def draw_window(red, yellow, red_projectiles, yellow_prjectiles, red_health, yellow_health):

    WIN.blit(BACKGROUND_IMG, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("HEALTH: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("HEALTH: " + str(yellow_health), 1, WHITE)

    WIN.blit(red_health_text, (10, 10))
    WIN.blit(yellow_health_text, (WIDTH - yellow_health_text.get_width() -15, 10))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    for projectile in red_projectiles: 
        pygame.draw.rect(WIN, RED, projectile)

    for projectile in yellow_prjectiles:
        pygame.draw.rect(WIN, YELLOW, projectile)

    pygame.display.update()