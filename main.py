import pygame
import os
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Space Pong")

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
                    PROJECTILE_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(yellow_projectiles) < MAX_PROJECTILES:
                    projectile = pygame.Rect(yellow.x, yellow.y + yellow.height/2 + 2.5, 10, 5)
                    yellow_projectiles.append(projectile)
                    PROJECTILE_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                SHIP_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                SHIP_HIT_SOUND.play()

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
           
