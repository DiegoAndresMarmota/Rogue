import sys
import pygame
from warrior import Warrior


def check_controller(Warrior):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #If the user press any arrow keys, set the moving_right, moving_left, moving_up or moving_down flag to True.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Warrior.moving_right = True
            elif event.key == pygame.K_LEFT:
                Warrior.moving_left = True
            elif event.key == pygame.K_UP:
                Warrior.moving_up = True
            elif event.key == pygame.K_DOWN:
                Warrior.moving_down = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Warrior.moving_right = False
            elif event.key == pygame.K_LEFT:
                Warrior.moving_left = False
            elif event.key == pygame.K_UP:
                Warrior.moving_up = False
            elif event.key == pygame.K_DOWN:
                Warrior.moving_down = False


def updated_screen(configuration, screen, warrior):
    # Update the screen during each pass through the loop.
    
    # Redraw the screen during each pass through the loop with the function bg_screen() with the warrior.bmp
    screen.fill(configuration.bg_screen)
    warrior.start_on_screen()

    # Make the most recently drawn screen visible. 
    pygame.display.flip()
