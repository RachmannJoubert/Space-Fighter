import pygame
import os
pygame.font.init()

pygame.display.set_caption("Space Pong")
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER =pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('ubuntu', 100)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60
VEL = 5
PROJECTILE_VEL = 10
MAX_PROJECTILES = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join(
    'Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join(
    'Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

BACKGROUND_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

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

def winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():

    red = pygame.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_projectiles = []
    yellow_projectiles = []

    red_health = int(10)
    yellow_health = int(10)
    
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_projectiles) < MAX_PROJECTILES:
                    projectile = pygame.Rect(red.x + red.width, red.y + red.height/2 + 2.5, 10, 5)
                    red_projectiles.append(projectile)

                if event.key == pygame.K_RCTRL and len(yellow_projectiles) < MAX_PROJECTILES:
                    projectile = pygame.Rect(yellow.x, yellow.y + yellow.height/2 + 2.5, 10, 5)
                    yellow_projectiles.append(projectile)

            if event.type == RED_HIT:
                red_health -= 1

            if event.type == YELLOW_HIT:
                yellow_health -= 1

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        handle_red_movement(keys_pressed, red)
        handle_yellow_movement(keys_pressed, yellow)

        handle_projeciles(red_projectiles, yellow_projectiles, red, yellow)
         
        draw_window(red, yellow, red_projectiles, yellow_projectiles, red_health, yellow_health)

    main()

if __name__ == "__main__":
    main()
           
