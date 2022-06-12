import math
import pygame

class picline:
    def __init__(self,screen,pic,width=10) -> None:
        self.screen=screen
        self.pic=pic
        self.bg=pygame.image.load(pic)
        self.width=width
        self.ang=0
        
    def show(self,startpos,endpos):
        self.length=math.dist(startpos,endpos)
        nbg=pygame.transform.scale(self.bg,(self.length,self.width))
        center=((startpos[0]+endpos[0])//2,(startpos[1]+endpos[1])//2)
        angle=((math.atan2((-1)*(startpos[1]-endpos[1]),startpos[0]-endpos[0])/math.pi)*180);
        rotated_image = pygame.transform.rotate(nbg,angle)
        new_rect = rotated_image.get_rect(center =center)
        self.screen.blit(rotated_image, new_rect)
        # pygame.draw.circle(self.screen,(3, 202, 252),tuple(startpos),6)
        # pygame.draw.circle(self.screen,(3, 202, 252),tuple(endpos),6)

