from re import L
from tracemalloc import start
import time
import pygame,sys,random
from pygame.locals import *
import math
import copy
import json
from os.path import exists
from pygame import mixer

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
from objects.button import button,levelbutton
import objects.maingame as game
import objects.home as home






def levelmap(screen,size):
    width,height=size
    backbutton=button(screen,((width//2)-75,500),(150,50),"./assets/images/back.png")
    f = open("./assets/db/player.json","r")
    data = json.load(f)
    passed=data["passed"]
    levelcount=9
    row=3
    levelocc=[]
    buz=mixer.Sound("./assets/sounds/buzzer.mp3")

    for i in range(levelcount):
        if(i<passed):
            levelocc.append(levelbutton(screen,(490+140*(i%row),100+140*(i//row)),(80,80),i,False))
        else:
            levelocc.append(levelbutton(screen,(490+140*(i%row),100+140*(i//row)),(80,80),i,True))


    #background part
        
    bitsarr=[]
    for i in range(0,width,10):
        x=i
        y=random.randint(int(-1*height),0)
        speed=random.randint(1,4)
        bitsarr.append([x,y,speed])

    bit_length=20
    l=20
    font5=pygame.font.Font('freesansbold.ttf',bit_length)
    font3=pygame.font.Font('freesansbold.ttf',36)
    font3=font3.render("CHOOSE AN UNLOCKED LEVEL",True,(186, 186, 0))

    def rain(x,y):
        for i in range(l):
                bits=font5.render(str(random.randint(0,1)),True,(0, int((255/l)*(l-i)),0))
                screen.blit(bits,(x,y-(i*bit_length)))
        
        
        
    line_length=10


    running=True

    while running:
        screen.fill((0,0,0))       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break;
        for i in range(len(bitsarr)):
            rain(bitsarr[i][0],bitsarr[i][1])
            bitsarr[i][1]+=bitsarr[i][2]
            if(bitsarr[i][1]>=height+(l*bit_length)):
                bitsarr[i][1]=random.randint(int(-1*height),0)

        for i in range(levelcount):
            if((levelocc[i].show()) and (i<passed)):
                game.gamelevel(screen,i+1,(width,height))
            else:
                if(levelocc[i].show()):
                    buz.play()
                    continue
        if(backbutton.show()):
            home.home(screen,(width,height))
        screen.blit(font3,(400,20))

        pygame.display.update() 


