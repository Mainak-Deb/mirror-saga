import imp
from re import L
from tracemalloc import start
import pygame,sys
from pygame.locals import *
from pygame import mixer
import math
import copy
import json
from os.path import exists

from objects.alien import alien
from objects.button import button

from objects.drag import Drag
from objects.gun import gun
from objects.straightline import angleline,straightline 
import objects.intersect as intersect
from objects.pictureline import picline
from objects.walltypes import mirrorwall, plainwall

from objects.tile import tile
from objects.drag import Drag
from objects.Updater import Updater
from objects.gun import gun
from objects.button import button
import objects.maingame as game
import objects.levelmap as levelmap




def home(screen,size):
    width,height=size
    startbutton=button(screen,((width//2)-100-150,550),(150,50),"./assets/images/start.png")  
    quitbutton=button(screen,((width//2)+100,550),(150,50),"./assets/images/quit.png")  
    lens=pygame.image.load('./assets/images/Eye-Lens-PNG-Picture.png')
    lens=pygame.transform.scale(lens,(100,100))
    font3=pygame.font.Font('freesansbold.ttf',45)
        
    welcome=font3.render("WELCOME TO THE WORLD OF MIRRORS",True,(255,255,255))
    saga=font3.render("MIRROR SAGA",True,(4, 146, 201))
    stss=mixer.Sound("./assets/sounds/start.mp3")
    stss.play()
    
    x=int(width/2)
    y=int(height/2)
    od=40
    ind=20
    a=int(height*2/3)
    r=300
    ex=0
    m=2
    ea=0
    ma=0
    eye_height=80

    prev_x=x

    def polar_elipse(a,b,t):
        x1=a*math.cos(t*math.pi/180)
        y1=b*math.sin(t*math.pi/180)
        return (x+x1,y+y1)
        
    def polar_circle(r,t):
        x1=r*math.cos(t*math.pi/180)
        y1=r*math.sin(t*math.pi/180)
        return (x+x1,y+y1)

    def elipse_height(lx,posy):
        try:
            h=math.sqrt((1-(lx/a)**2)*(eye_height)**2)
            ly=((posy-y)*(h-(lens.get_width()/2))/y)
            return ly
        except:
            return a
        
    def mod(x):
        if x<0:return (-1*x)
        else: return x
        
    screenlenth=height

        
    running=True
    while running:
        screen.fill((0,0,0))       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break;
        
        mice=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        posx=mice[0] 
        if(x-screenlenth/3 <posx<x+screenlenth/3):
            posx=mice[0]    
        else:
            posx=x
        posy=mice[1]   

        if(mod(prev_x-posx)>30):colour=(255,0,0)
        else:colour=(255,255,255)
        pygame.draw.circle(screen,colour,(x,y),int(screenlenth/3))
        lens_radius=int(130-(mod(posx-x)/10))

        lens_copy=pygame.transform.scale(lens,(lens_radius,lens_radius))
        lx=((posx-x)*(x-a/4-(lens_copy.get_width()/2))/x)

        
        p=mod(elipse_height(lx,posy))+(lens_copy.get_width()/4)
       
        screen.blit(lens_copy,(int(x-(lens_copy.get_width()/2)+lx),int(y-(lens_copy.get_height()/2)+elipse_height(lx,posy))))
        
      
        b=((screenlenth/3)-p)/ind
        
        for i in range(0,90):
            pygame.draw.polygon(screen,(0,0,0),[polar_elipse(a/2,p,i),polar_elipse(a/2,p,i+1),polar_circle(int(screenlenth/3),i+1),polar_circle(int(screenlenth/3),i)])       
            j=i+270
            pygame.draw.polygon(screen,(0,0,0),[polar_elipse(a/2,p,j),polar_elipse(a/2,p,j+1),polar_circle(int(screenlenth/3),j+1),polar_circle(int(screenlenth/3),j)])       
            j=i+90
            pygame.draw.polygon(screen,(0,0,0),[polar_elipse(a/2,p,j),polar_elipse(a/2,p,j+1),polar_circle(int(screenlenth/3),j+1),polar_circle(int(screenlenth/3),j)])       
            j=i+180
            pygame.draw.polygon(screen,(0,0,0),[polar_elipse(a/2,p,j),polar_elipse(a/2,p,j+1),polar_circle(int(screenlenth/3),j+1),polar_circle(int(screenlenth/3),j)])       

            
        
        
        for i in range(od):
              pygame.draw.circle(screen,(255,255,255),(x,y),int((screenlenth/3)+((i*((screenlenth*(1/(2**(.5))-(1/3)))/od)+ex)%((screenlenth*(1/(2**(.5))-(1/3)))))),1)
              if(i<ind):
                  if((p+i*b)>2):pygame.draw.ellipse(screen,(255,255,255),(x-a/2,y-((p+(i*b))),a,2*(p+(i*b))),1)
                  else:pygame.draw.ellipse(screen,(255,255,255),(x-a/2,y-2,a,4))
        
        for i in range(50):
              pygame.draw.circle(screen,(255,255,255),(x,y),int((screenlenth*4/5)+(i*6))-64,1)
        ex+=0.4
        prev_x=posx

        screen.blit(welcome,(220,20))

        if(startbutton.show()):
            levelmap.levelmap(screen,size)
            #game.gamelevel(screen,"./assets/levels/lev1.json",(width,height))
        if(quitbutton.show()):
            pygame.quit()
            sys.exit()
            break;

        screen.blit(saga,(500,620))

        pygame.display.update() 


