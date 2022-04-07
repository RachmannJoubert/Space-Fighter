import pygame
from global_var import *

def handle_red_movement(keys_pressed, red):
        if keys_pressed[pygame.K_a] and red.x - VEL > 0 -5: # LEFT
            red.x -= VEL
        if keys_pressed[pygame.K_d] and red.x + VEL < BORDER.x - SPACESHIP_WIDTH + 15: # RIGHT
            red.x += VEL
        if keys_pressed[pygame.K_w] and red.y - VEL > 0: # UP
            red.y -= VEL
        if keys_pressed[pygame.K_s] and red.y + VEL < HEIGHT - SPACESHIP_HEIGHT - 5: # DOWN
            red.y += VEL

def handle_yellow_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > BORDER.x + BORDER.width - 5: # LEFT
            yellow.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and yellow.x - VEL < WIDTH - SPACESHIP_WIDTH + 5: # RIGHT
            yellow.x += VEL
        if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: # UP
            yellow.y -= VEL
        if keys_pressed[pygame.K_DOWN] and yellow.y + VEL < HEIGHT - SPACESHIP_HEIGHT - 5: # DOWN
            yellow.y += VEL