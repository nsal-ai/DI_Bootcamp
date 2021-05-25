import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,play):
        '''initialize alien and set the starting position'''
        super().__init__()
        self.screen = play.screen 

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #horizontal position of alien
        self.x = float(self.rect.x)