import pygame
import turtle
import random
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from car import Car
from signal import Signal


pygame.init()

screen = pygame.display.set_mode((1050,950))

pygame.display.set_caption("Traffic Simulator")


x = 50
y = 50
width = 40
height = 60
velocity = 100


#Declaring all RGB colors
PURPLE = (255,0,255)
RED = (255,0,0)
WHITE = (255,255,255)
GREY = (210,210,210)
GREEN =(50,205,50)
BLACK = (0,0,0)

#this will be a list of all the sprites that we use for the animation
def traffic():
    xp = 100
    car1 = Car(xp+150,525)
    car2 = Car(xp+100,525)
    car3 = Car(xp+50,525)
    signal_east = Signal(380,520)
    #signal_north = Signal(510,350)

    #this will be aligning the cars into each other
    #also aligning the signal lights
    all_cars = pygame.sprite.Group(car1,car2,car3)
    all_signals = pygame.sprite.Group(signal_east)
    #This lets the user close the window
    #which means that we have to flag it once we hit the
    #close button
    run = True
    #responsible for the velocity and the intervals of the game
    clock=pygame.time.Clock()
    
    types_of_signals = ['images_png/green.png','images_png/yellow.png','images_png/red.png'];
    signal_counter = 0
    

    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        
        xp = 100
        car1.move(xp,signal_counter,car2)
        car2.move(xp,signal_counter,car3)
        car3.move(xp,signal_counter,car1)
        
        e = pygame.event.wait()
        
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                break
        if e.type == KEYUP:
            signal_counter += 1
            if signal_counter > 2:
                signal_counter = 0
            signal_east.change_sign(types_of_signals[signal_counter])
        #this will allow the cars to move on there own with ligh changes

        #this will be the color of the screen
        screen.fill(GREEN)
       
        
        
        #draw the road [moving position left or right, moving down and up, width of the rec, length of the rect]
        pygame.draw.rect(screen, GREY, [335,0,400,1050])
        pygame.draw.rect(screen,GREY, [0,300,1050,370])
        
        #this white lines for cross walk
        
        #this is for vertiacle lines
        pygame.draw.line(screen,BLACK, (530, 245), (530, 0),5)
        pygame.draw.line(screen,BLACK, (530, 725), (530,1050),5)
        pygame.draw.line(screen,WHITE, (773,667), (773,300),40)
        pygame.draw.line(screen,WHITE, (735,667),(735,300),5)
        pygame.draw.line(screen,WHITE, (295,667),(295,300),40)
        pygame.draw.line(screen,WHITE, (332,667),(332,300),5)
        
        #this will be for horizontal lines
        pygame.draw.line(screen,BLACK, (0, 500), (275, 500),5)
        pygame.draw.line(screen,BLACK, (1050, 500), (795,500),5)
        pygame.draw.line(screen,WHITE, (335, 673), (735,673),5)
        pygame.draw.line(screen,WHITE, (335, 705), (735,705),35)
        pygame.draw.line(screen,WHITE, (335, 298), (735,298),5)
        pygame.draw.line(screen,WHITE, (335, 265), (735,265),37)

        #this will be drawing cars into the screen
        all_cars.draw(screen)
        all_signals.draw(screen)
        #refresh screen
        pygame.display.flip()
        
        #Number of frames per second is 60 in this case we can change
        clock.tick(200)
    #this will allow the program no to crash
    pygame.quit()
    
#this will be displaying the
if __name__ =='__main__':
    traffic()
