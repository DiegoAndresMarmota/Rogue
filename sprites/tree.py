import pygame
from settings import *

class Tree(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../design/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)