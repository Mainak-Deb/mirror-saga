from re import L
import pygame,sys
from pygame.locals import *
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


pygame.init()
width=1320
height=690;
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Line rotate")


def home():
    print("home")


def gamelevel(screen,level,size):
    width,height=size
    mirrorsize=60;
    f = open(level,"r")
    data = json.load(f)
    arr=data["gamemap"]
    mirrorarray=data["mirrorarr"]
    startpoint=data["leaser"]
    endpoint=data["target"]
    wallarr=data["wallarr"]
    mirrorcount=3
    laserang=0
    f.close()
    box=30;
    brick=tile(screen,"./assets/images/brick.png",box)
    stone=pygame.image.load("./assets/images/yellowtile.png")
    stone=pygame.transform.scale(stone,(30,30))
    
    update=Updater()

    backbutton=button(screen,(1150,100),(150,50),"./assets/images/back.png")
    addbutton=button(screen,(1150,200),(150,50),"./assets/images/add.png")
    shootbutton=button(screen,(1150,300),(150,50),"./assets/images/shoot.png")

    #adding all walls
    for i in wallarr:
        update.add(plainwall(screen,(i[0][0],i[0][1]),(i[1][0],i[1][1])))
    for i in mirrorarray:
        update.add(mirrorwall(screen,(i[0][0],i[0][1]),(i[1][0],i[1][1])))

    
    leaser=angleline(screen,startpoint,laserang,(0,255,0))
    shooter=gun(screen,startpoint,laserang)
    
    sprite=alien(screen,"./assets/images/alien.png",80,endpoint,90)
    update.add(sprite)

    # update.add(Drag(screen,(200,200),mirrorsize))

    update.update()
    isshoot=False

    
    running=True
    while running:
        screen.fill((0,0,0))       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break;
            if event.type == KEYDOWN:
                    if event.key==K_RIGHT:
                        leaser.updateAngle("decr")
                    elif event.key==K_LEFT:
                        leaser.updateAngle("incr")
        
       
        sprite.show()
        

        blast,iskill=intersect.check(screen,leaser,update.arr,isshoot)
        if(isshoot):
            if(iskill):
                sprite.killed()
        isshoot=False
        if(len(blast)==2):
            pygame.draw.circle(screen,(255, 0,0),blast,10)
        
        shooter.show()
        

        for i in range(len(arr)): 
            for j in range(len(arr[0])):
                if(arr[i][j]==1):
                    #pygame.draw.rect(screen,(0,255,0),(j*box,i*box,box,box))
                    brick.show((j*box,i*box,box,box))          
        for i in range(1140,1320,30):
            for j in range(0,690,30):
                screen.blit(stone,(i,j))


        if(backbutton.show()):
            print("back")
        if(addbutton.show()):
            addbutton.click()
            print("add")
            if(mirrorcount>0):
                update.add(Drag(screen,(200,100),mirrorsize))
                mirrorcount-=1
        if(shootbutton.show()):
            shootbutton.click()
            print("shoot")
            isshoot=True
    
        update.update()
        
        
        
        pygame.display.update() 


