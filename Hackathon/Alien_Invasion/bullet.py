import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,play):
        super().__init__()
        self.screen = play.screen
        self.settings = play.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = play.ship.rect.midtop
        
        self.y = float(self.rect.y)

    def update(self):
        '''move bullet up the screen'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''draws bullet at the screen co-ordinate with y-coord decreasing 
        incrementally from the top
        '''
        pygame.draw.rect(self.screen, self.color, self.rect)