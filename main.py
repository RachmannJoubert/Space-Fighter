import pygame

pygame.display.set_caption("Space Pong")
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)

def draw_window():
    
    WIN.fill(WHITE)
    pygame.display.update()


def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
           
