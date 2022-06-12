import pygame,sys
from pygame.locals import *
import objects.home as home



pygame.init()
width=1320
height=690;
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Line rotate")

home.home(screen,(width,height))
