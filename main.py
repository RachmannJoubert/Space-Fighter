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
PROJECTILE_VEL = 10
MAX_PROJECTILES = 5

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

def main():

    red = pygame.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_projectiles = []
    yellow_projectiles = []
    
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_projectiles) < MAX_PROJECTILES:
                    projectile = pygame.Rect(red.x + red.width, red.y + red.height/2 - 2.5, 10, 5)
                    red_projectiles.append(projectile)

                if event.key == pygame.K_RCTRL and len(yellow_projectiles) < MAX_PROJECTILES:
                    projectile = pygame.Rect(yellow.x, yellow.y + yellow.height/2 - 2.5, 10, 5)
                    yellow_projectiles.append(projectile)
        print(red_projectiles, yellow_projectiles)
        keys_pressed = pygame.key.get_pressed()
        handle_red_movement(keys_pressed, red)
        handle_yellow_movement(keys_pressed, yellow)
         
        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
           
