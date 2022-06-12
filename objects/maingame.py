import imp
from re import L
from attr import s
from matplotlib import collections
import pygame,sys
from pygame.locals import *
import math
import copy
import json
from os.path import exists
import time
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
from objects.button import button
import objects.home as home
import objects.levelmap as levelmap
from objects.particle import particle
from objects.star import star



def gamelevel(screen,levelid,size):
    width,height=size
    mirrorsize=60;
    level="./assets/levels/lev"+str(levelid)+".json"
    f = open(level,"r")
    data = json.load(f)
    arr=data["gamemap"]
    mirrorarray=data["mirrorarr"]
    startpoint=data["leaser"]
    endpoint=data["target"]
    wallarr=data["wallarr"]
    mirrorcount=data["mirrorcount"]
    laserang=data["leaserang"]
    duration=data["countdown"]
    spriterange=data["range"]
    spritespeed=data["speed"]
    spritemove=data["move"]
    f.close()

    blastsound=mixer.Sound("./assets/sounds/blast.mp3")
    clk=mixer.Sound("./assets/sounds/button.mp3")
    frc=mixer.Sound("./assets/sounds/friction.mp3")
    lss=mixer.Sound("./assets/sounds/laser.wav")
    buz=mixer.Sound("./assets/sounds/buzzer.mp3")
    gos=mixer.Sound("./assets/sounds/gameover.mp3")
    gws=mixer.Sound("./assets/sounds/gamewin.mp3")
    stss=mixer.Sound("./assets/sounds/start.mp3")
    stss.play()

    
    box=30;
    brick=tile(screen,"./assets/images/brick.png",box)
    stone=pygame.image.load("./assets/images/yellowtile.png")
    stone=pygame.transform.scale(stone,(box,box))

    font1 = pygame.font.Font('freesansbold.ttf', 24)
    font2 = pygame.font.Font('freesansbold.ttf', 32)
    yourtime = font1.render("TIME REMAIN", True, (0,0,0))
    yourmirrors = font1.render("MIRROR", True, (255,255,255))
    update=Updater()

    backbutton=button(screen,(1150,100),(150,50),"./assets/images/back.png")
    backbutton2=button(screen,(300,500),(150,50),"./assets/images/back.png")
    quitbutton=button(screen,(750,500),(150,50),"./assets/images/quit.png")  


    addbutton=button(screen,(1150,200),(150,50),"./assets/images/add.png")
    shootbutton=button(screen,(1150,300),(150,50),"./assets/images/shoot.png")

    gameoverimg=pygame.image.load("./assets/images/gameover.png")
    gameoverimg=pygame.transform.scale(gameoverimg,(800,500))

    wonimg=pygame.image.load("./assets/images/won.png")
    wonimg=pygame.transform.scale(wonimg,(800,500))


    #adding all walls
    for i in wallarr:
        update.add(plainwall(screen,(i[0][0],i[0][1]),(i[1][0],i[1][1])))
    for i in mirrorarray:
        update.add(mirrorwall(screen,(i[0][0],i[0][1]),(i[1][0],i[1][1])))

    
    leaser=angleline(screen,startpoint,laserang,(0,255,0))
    shooter=gun(screen,startpoint,laserang)
    
    sprite=alien(screen,"./assets/images/alien.png",80,endpoint,spriterange,spritespeed,spritemove)
    update.add(sprite)

    # update.add(Drag(screen,(200,200),mirrorsize))

    update.update()
    isshoot=False

    
    running=True
    gameover=False
    won=False

    collitions=particle(screen)
    galaxy=star(screen,width,height)

    stss.play()
    starttime = time.time()
    while running:
        screen.fill((0,0,0))       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break;
            
        galaxy.show()
        sprite.show()

        if(not gameover): 
            if(isshoot):
                for i in range(len(arr)): 
                    for j in range(len(arr[0])):
                        if(arr[i][j]==1):
                            #pygame.draw.rect(screen,(0,255,0),(j*box,i*box,box,box))
                            brick.show((j*box,i*box,box,box))          
                for i in range(1140,1320,30):
                    for j in range(0,690,30):
                        screen.blit(stone,(i,j))
            blast,iskill=intersect.check(screen,leaser,update.arr,isshoot,lss)
            if(isshoot):
                if(iskill):
                    sprite.killed()
                    blastsound.play()
                    won=True
                    gameover=True
                    pygame.time.wait(2000)
                    gws.play()
                    f = open("./assets/db/player.json","r")
                    data = json.load(f)
                    passed=data["passed"]

                    playerabout={
                        "passed":max(passed,levelid+1)
                    }
                    with open("./assets/db/player.json", "w") as outfile:
                        json.dump(playerabout, outfile)


            isshoot=False
            if(len(blast)==2):
                #pygame.draw.circle(screen,(255, 0,0),blast,10)
                collitions.show(blast[0],blast[1])
        
            
        shooter.show()
        

        for i in range(len(arr)): 
            for j in range(len(arr[0])):
                if(arr[i][j]==1):
                    #pygame.draw.rect(screen,(0,255,0),(j*box,i*box,box,box))
                    brick.show((j*box,i*box,box,box))          
        for i in range(1140,1320,30):
            for j in range(0,690,30):
                screen.blit(stone,(i,j))

        if(not gameover):
            if(backbutton.show()):
                levelmap.levelmap(screen,size)

            if(addbutton.show()):
                addbutton.click()
                # print("add")
                if(mirrorcount>0):
                    update.add(Drag(screen,(200,100),mirrorsize))
                    mirrorcount-=1
            if(shootbutton.show()):
                shootbutton.click()
                # print("shoot")
                isshoot=True

        pygame.draw.rect(screen,(0, 186, 31),(1150,380,167,120))
        pygame.draw.rect(screen,(0,0,0),(1150,520,167,120))

        screen.blit(yourtime,(1150,400))
        screen.blit(yourmirrors,(1180,540))


        currenttime=time.time()
        if(not gameover):
            difftime=int(currenttime-starttime)

        ctime = font2.render(str(duration-difftime), True, (255,0,0))
        screen.blit(ctime,(1200,440))
        if(duration-difftime==0):
            gos.play()
            gameover=True

        ymc = font2.render(str(mirrorcount), True, (255,0,255))
        screen.blit(ymc,(1220,590))


        
        if(not gameover):
            update.update()
        
        if(gameover):
            if(not won):
                screen.blit(gameoverimg,(200,100))
            else:
                screen.blit(wonimg,(200,100))
            if(backbutton2.show()):
                levelmap.levelmap(screen,size)
            if(quitbutton.show()):
                pygame.quit()
                sys.exit()
                break;

        
        
        
        pygame.display.update() 


