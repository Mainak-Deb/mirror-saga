from multiprocessing.spawn import is_forking
import pygame
import math
from objects.straightline import straightline,angleline


class alien:
    def __init__(self,screen,pic,size,pos,srange,speed=2,move="y") -> None:
        self.screen=screen;
        self.pic=pic;
        self.intial_pos=pos;
        self.pos=list(pos);
        self.endpos=(self.pos[0]+size,self.pos[1]+size)
        self.srange=srange;
        self.move=move
        self.ang=0;
        self.bg=pygame.image.load(pic)
        self.size=size
        self.speed=speed;
        self.bg=pygame.transform.scale(self.bg,(self.size,self.size))
        self.state=0
        self.reflector= straightline(self.screen,self.intial_pos,self.endpos,"sprite")
        self.iskilled=False
        pass

    def show(self):
        self.updateit()
        rotated_image = pygame.transform.rotate(self.bg, self.ang)
        new_rect = rotated_image.get_rect(center = self.bg.get_rect(topleft = self.pos).center)
        self.screen.blit(rotated_image, new_rect)

    def updateit(self):
        if(self.iskilled):
            return
        self.state=(self.state+1)%1800000
        self.ang=int(math.sin(self.state/180*math.pi)*25)
        if(self.move=="y"):
            self.pos[1]=self.intial_pos[1]+int(math.sin((self.state*self.speed)/180*math.pi)*self.srange/2)
        if(self.move=="x"):
            self.pos[0]=self.intial_pos[0]+int(math.sin((self.state*self.speed)/180*math.pi)*self.srange/2)
        self.endpos=(self.pos[0]+self.size,self.pos[1]+self.size)
        self.reflector= straightline(self.screen,self.pos,self.endpos,"sprite")

    def update(self):
        pass
    def setState(self):
        pass

    def killed(self):
        if(not self.iskilled):
            self.bg=pygame.image.load("./assets/images/smashed.png")
            self.bg=pygame.transform.scale(self.bg,(self.size,self.size))
            self.iskilled=True
            self.reflector= straightline(self.screen,(0,0),(0,0),"sprite")
    
