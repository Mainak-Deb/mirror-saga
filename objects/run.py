import pygame,sys
from pygame.locals import *
import math
from Updater import Updater
from drag import Drag
from straightline import angleline 
import intersect
from pictureline import picline
from walltypes import mirrorwall, plainwall


pygame.init()
width=1200
height=690;
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("game tests")
update=Updater()

mirrorsize=60;

update.add(Drag(screen,(200,200),mirrorsize))
update.add(Drag(screen,(400,500),mirrorsize))
update.add(Drag(screen,(300,200),mirrorsize))
update.add(Drag(screen,(500,500),mirrorsize))
update.add(Drag(screen,(200,500),mirrorsize))
update.add(Drag(screen,(400,600),mirrorsize))

update.add(plainwall(screen,(200,600),(60,30)))
update.add(plainwall(screen,(400,600),(600,530)))
update.add(mirrorwall(screen,(100,200),(600,300)))
update.add(mirrorwall(screen,(500,700),(100,500)))

leaser=angleline(screen,(0,0),-45,(0,255,0))

#leaser=angleline(screen,(0,height),45,(0,255,0))
# leaser=angleline(screen,(width//2,height),90,(0,255,0))
# leaser=angleline(screen,(width//2,0),-90,(0,255,0))

running=True
 
update.update()
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
    
    #update.update()
    intersect.check(screen,leaser,update.arr)
    update.update()
    
    
    pygame.display.update() 