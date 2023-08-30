import pygame

#Create a class for the warrior
class Warrior():
    #Iniciate the warrior and establish him position on the screen
    def __init__(self, screen):
        self.screen = screen
        #Upload the image of the warrior and manipulate the image on the screen
        self.image = pygame.image.load('images/warrior.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new warrior at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def start_on_screen(self):
        #Draw the warrior on the screen
        self.screen.blit(self.image, self.rect)