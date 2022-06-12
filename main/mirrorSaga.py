import pygame,sys
from pygame.locals import *
import objects.maingame as game



pygame.init()
width=1320
height=690;
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Line rotate")

print("ok")
game.gamelevel(screen,"./assets/levels/lev2.json",(width,height))