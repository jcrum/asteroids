import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: 1280")
    print(f"Screen height: 720")

    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()

        time_passed = clock.tick(60)
        dt = time_passed / 1000



if __name__ == "__main__":
    main()


