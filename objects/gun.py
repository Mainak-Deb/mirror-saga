import pygame
import math
from objects.pictureline import picline


class gun:
    def __init__(self,screen,pos,ang) -> None:
        self.screen=screen;
        self.pos=pos;
        self.size=50
        self.neck=120
        self.topleft=(self.pos[0]-self.size//2,self.pos[1]-self.size//2)
        self.ang=ang;
        self.fulcrum=pygame.image.load("./assets/images/fulcrum.png")
        self.fulcrum=pygame.transform.scale(self.fulcrum,(self.size,self.size))
        self.nosel=picline(self.screen,"./assets/images/gunnoesel.png",40)
        self.uppos=( self.pos[0]+int(self.neck*math.cos(self.ang/180*math.pi)),
                 self.pos[1]-int(self.neck*math.sin(self.ang/180*math.pi)))
        
    def show(self):   
        self.nosel.show(self.uppos,self.pos)
        self.screen.blit(self.fulcrum,self.topleft)

   