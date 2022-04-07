import pygame
from global_var import *

def handle_projeciles(red_projectiles, yellow_projectiles, red, yellow):

    for projectile in red_projectiles:
        projectile.x += PROJECTILE_VEL
       
        if yellow.colliderect(projectile):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_projectiles.remove(projectile)
        elif projectile.x > WIDTH:
            red_projectiles.remove(projectile)


    for projectile in yellow_projectiles:
        projectile.x -= PROJECTILE_VEL
       
        if red.colliderect(projectile):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_projectiles.remove(projectile)
        elif projectile.x < 0:
            yellow_projectiles.remove(projectile)