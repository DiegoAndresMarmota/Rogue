import pygame
from settings.settings import TILESIZE
from settings.map import MAP
from sprites.player import Player
from sprites.river import River
from sprites.rock import Rock
from sprites.tree import Tree


class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        
        self.animated_sprites = pygame.sprite.Group()
        self.static_sprites = pygame.sprite.Group()
        
        self.create_map()
        
    
    def create_map(self):
        for row_index, row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                
                if col == 'p':
                    Player((x, y),[self.animated_sprites])
                if col == 'r':
                    Rock((x, y),[self.animated_sprites, self.static_sprites])
                if col == 't':
                    Tree((x, y),[self.animated_sprites, self.static_sprites])
                if col == 'ri':
                    River((x, y),[self.animated_sprites, self.static_sprites])
        
        
    def run(self):
        self.animated_sprites.draw(self.display_surface)