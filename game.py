# Create flappy bird game with pygame

import pygame

def main():
    screen = pygame.display.set_mode((800, 600)) # näytön koko
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("sky blue") # taustaväri

        pygame.display.flip()

        clock.tick(60) # Odota niin kauan, että ruudun päivitysnopeus on 60fps

if __name__ == '__main__':
    main()
    