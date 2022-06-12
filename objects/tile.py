import pygame

class tile:
    def __init__(self,screen,pic,size) -> None:
        self.screen=screen
        self.pic=pic
        self.size=size
        self.bg=pygame.image.load(pic)
        self.bg=pygame.transform.scale(self.bg,(self.size,self.size))

    def show(self,pos):
        self.screen.blit(self.bg,pos)
