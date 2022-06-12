import pygame,random
import pygame, sys, random
from pygame.locals import *

class particle:
    def __init__(self,screen) -> None:
        self.screen=screen;
        self.particles=[]
    def show(self,mx,my):
        self.particles.append([[mx, my], [random.randint(-40, 40) / 10, random.randint(-40, 40) / 10], random.randint(5, 7)])
 
        for particle in self.particles:
            particle[0][0] -= particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            pygame.draw.circle(self.screen, (247, 236, 79), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)