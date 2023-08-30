import sys
import pygame


def check_controller():
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def updated_screen(configuration, screen, warrior):
    # Update the screen during each pass through the loop.
    
    # Redraw the screen during each pass through the loop with the function bg_screen() with the warrior.bmp
    screen.fill(configuration.bg_screen)
    warrior.start_on_screen()

    # Make the most recently drawn screen visible. 
    pygame.display.flip()
