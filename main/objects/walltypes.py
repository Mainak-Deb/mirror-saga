import math
from re import M
import pygame,sys
from pygame.locals import *
from objects.pictureline import picline
from objects.straightline import straightline,angleline



class plainwall:
    def __init__(self,screen,startpos,endpos) -> None:
        self.screen=screen;
        self.startpos=startpos
        self.endpos=endpos
        self.reflector= straightline(self.screen,self.startpos,self.endpos,"wall")

    def update(self):
        pass
    def show(self):
        pygame.draw.line(self.screen,(255, 233, 255),self.startpos,self.endpos,2)

    def setState(self):
        pass
    


class mirrorwall:
    def __init__(self,screen,startpos,endpos) -> None:
        self.screen=screen;
        self.startpos=startpos
        self.endpos=endpos
        self.reflector= straightline(self.screen,self.startpos,self.endpos,"mirror")
        self.pic=picline(screen,"./assets/images/linemirror.png")


    def update(self):
        pass
    def show(self):
        self.pic.show(self.startpos,self.endpos)

    def setState(self):
        pass
    
