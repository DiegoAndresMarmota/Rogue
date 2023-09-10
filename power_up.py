import pygame
from pygame.sprite import Sprite


class PowerUp(Sprite):
    """Create a sprite Skill with the ability of warrior named
    Power_up:
        Sprite (blaster_width, blaster_height):
            blaster_width: width of the blaster
            blaster_height: height of the blaster
    """
    def __init__(self, configurations, screen, warrior):
        super(PowerUp, self).__init__()
        self.screen = screen
        
        #Create a blaster object in the position of warrior
        self.rect = pygame.Rect(
            0, 0, configurations.blaster_width, configurations.blaster_height)
        self.rect.centerx = warrior.rect.centerx
        self.rect.top = warrior.rect.top

        #Guard the position of the blaster
        self.y = float(self.rect.y)
        
        #Set the color of the blaster
        self.color = configurations.blaster_color
        self.speed = configurations.blaster_speed


    def update(self):
        """Move the blaster upward"""
        #Update the position of the blaster
        self.y -= self.speed
        #Update the rect position of the blaster
        self.rect.y = self.y
        
        
    def release_power_up(self):
        """Draw the blaster on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
