import pygame
from pygame.sprite import *
from pygame import *

class Signal(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.image = image.load('images_png/green.png')
        self.rect = self.image.get_rect(center = (x,y))
    def change_sign(self,color):
        self.image = image.load(color)

