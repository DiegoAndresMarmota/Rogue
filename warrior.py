import pygame

#Create a class for the warrior
class Warrior():
    #Iniciate the warrior and establish him position on the screen
    def __init__(self, screen, Configurations):
        self.screen = screen
        
        self.configurations = Configurations()
        
        #Upload the image of the warrior and manipulate the image on the screen
        self.image = pygame.image.load('images/warrior.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new warrior at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        #Center the warrior with float value
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
    
    #Update the movement of the warrior
    def init_translation_movement(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.configurations.warrior_speed
        
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.configurations.warrior_speed
            
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.configurations.warrior_speed
            
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.configurations.warrior_speed
        
        #Update the rect object from self.center_x, self.center_y
        self.rect.center = self.center_x, self.center_y
    
    def start_on_screen(self):
        #Draw the warrior on the screen
        self.screen.blit(self.image, self.rect)