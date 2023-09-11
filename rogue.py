import pygame
from settings.configurations import Configurations
from settings.functions import check_controller, updated_screen
from warrior import Warrior
from pygame.sprite import Group


def open_game():
    # Initialize "Rogue" with settings.configuration
    
    # Open game and create a screen object.
    pygame.init()
    
    # Import the configurations class to get the screen width, height, bg_screen
    configurations = Configurations()
    
    # Create a screen object with the width and height of the screen.
    screen = pygame.display.set_mode((
        configurations.screen_width,
        configurations.screen_height))
    
    # Set the caption of the window
    pygame.display.set_caption("Rogue")
    
    # Create a warrior object.
    warrior = Warrior(screen, configurations)
    
    # Create instance of Group class to store the blaster_skills
    skills = Group()
    
    # Start the main loop for the game.
    while True:
        #Import the []functions from the functions.py file
        check_controller(configurations, screen, warrior, skills)
        # Update the screen during pressing the arrow keys
        warrior.walk()
        skills.update()
        updated_screen(configurations, screen, warrior, skills)


# Execute the main function(Rogue)
open_game()