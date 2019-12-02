import pygame
from pygame.sprite import *
#from pygame.locals import *
from pygame import *

WHITE = (255,255,255)

class Car(Sprite):
    #this class will be creating a car that gets it from a Sprite class in pygame

    def __init__(self,x,y):
        #this wll be calling the parent class sprites constructor
        Sprite.__init__(self)

        self.image = image.load('images_png/car1.png')
        #variable position of the car
        self.x = int(x)
        #y position of car
        self.y = int(y)
        #this will be placing the car
        self.rect = self.image.get_rect(center =(x,y))
        
    def move(self, xp, sgn, a):
        #new place for the car
        xp = self.x+xp
        
        if xp > 1200:
            xp = xp - 1200
        distance = xp - a.x
        
        if sgn == 0 or sgn == 1:
            #move the car
            self.rect.left = xp
            #update the cars position
            self.x = xp
        elif sgn == 2:
            if self.x > 700:
                self.rect.left = xp
                self.x = xp
            elif self.x >= 700 and self.x <= 750:
                pass
            elif distance > -200 and distance < 200: #checks nearby cars
                pass
            else :
                self.rect.left = xp
                self.x = xp
            
        
        
  
