import pygame

class button:
    def __init__(self,screen,pos,size,pic) -> None:
        self.screen=screen
        self.pos=pos
        self.size=size
        self.bg=pygame.image.load(pic)
        self.bg=pygame.transform.scale(self.bg,(self.size[0],self.size[1]))
        self.state=True
        self.count=0

    def show(self):
        self.count+=1
        if(self.count>15):
            self.state=True
        self.screen.blit(self.bg,self.pos)
        mx,my=pygame.mouse.get_pos()
        if(self.state):
            if((self.pos[0]<=mx<=self.pos[0]+self.size[0]) and
                (self.pos[1]<=my<=self.pos[1]+self.size[1]) ):
                mouse_state=pygame.mouse.get_pressed()
                if(mouse_state[0]):
                    return True
        return False

    def click(self):
        self.state=False
        self.count=0

    