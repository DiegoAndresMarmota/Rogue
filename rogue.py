import pygame
from settings.configuration import configurations
from settings.functions import check_controller, updated_screen
from warrior import Warrior


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
    
    # Create a warrior object.
    warrior = Warrior(screen)
    
    # Start the main loop for the game.
    while True:
        #Import the []functions from the functions.py file
        check_controller()
        updated_screen(init_configuration, screen, warrior)


# Execute the main function(Rogue)
open_game()