import pygame,random
import pygame, sys, random
from pygame.locals import *


class star:
    def __init__(self,screen,w,h) -> None:
        self.screen=screen;
        self.stars=[]
        self.w=w
        self.starcount=400
        for i in range(self.starcount):
            self.stars.append([[random.randint(0,w),random.randint(0,h)],(random.randint(1,4)*2)])
        
    def show(self):
        for i in range(self.starcount):
            pygame.draw.circle(self.screen,(255, 255,255),tuple(self.stars[i][0]),1)
            self.stars[i][0][0]=(self.stars[i][0][0]+self.stars[i][1])%self.w
