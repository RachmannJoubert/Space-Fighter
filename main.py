import pygame
import os

pygame.display.set_caption("Space Pong")
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER =pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
VEL = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join(
    'Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join(
    'Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow):
    
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    pygame.display.update()

def handle_red_movement(keys_pressed, red):
        if keys_pressed[pygame.K_a]: # LEFT
            red.x -= VEL
        if keys_pressed[pygame.K_d]: # RIGHT
            red.x += VEL
        if keys_pressed[pygame.K_w]: # UP
            red.y -= VEL
        if keys_pressed[pygame.K_s]: # DOWN
            red.y += VEL

def handle_yellow_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_LEFT]: # LEFT
            yellow.x -= VEL
        if keys_pressed[pygame.K_RIGHT]: # RIGHT
            yellow.x += VEL
        if keys_pressed[pygame.K_UP]: # UP
            yellow.y -= VEL
        if keys_pressed[pygame.K_DOWN]: # DOWN
            yellow.y += VEL

def main():

    red = pygame.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_red_movement(keys_pressed, red)
        handle_yellow_movement(keys_pressed, yellow)
         
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
           
