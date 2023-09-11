#Create configuration class to load the game configurations
class Configurations():
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_screen = (230,230,230)
        
        #Speed warrior
        self.warrior_speed = 0.2
        
        #configurations of the blaster
        self.blaster_speed = 1
        self.blaster_width = 5
        self.blaster_height = 10
        self.blaster_color = 60,60,60