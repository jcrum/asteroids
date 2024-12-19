import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: 1280")
    print(f"Screen height: 720")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()




if __name__ == "__main__":
    main()


