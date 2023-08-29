import sys
import pygame

def open_game():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Rogue")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
        
open_game()