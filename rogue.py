import sys
import pygame
from settings.configuration import configurations


def open_game():
    # Initialize "Rogue" with settings.configuration
    
    # Open game and create a screen object.
    pygame.init()
    
    # Import the configurations class to get the screen width, height, bg_screen
    init_configuration = configurations()
    
    # Create a screen object with the width and height of the screen.
    screen = pygame.display.set_mode((
        init_configuration.screen_width,
        init_configuration.screen_height))
    
    # Set the caption of the window
    pygame.display.set_caption("Rogue")
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop with the function bg_screen()
        screen.fill(init_configuration.bg_screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
        
# Execute the main function(Rogue)
open_game()