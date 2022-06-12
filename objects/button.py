import pygame
from pygame import mixer


class button:
    def __init__(self,screen,pos,size,pic) -> None:
        self.screen=screen
        self.pos=pos
        self.size=size
        self.bg=pygame.image.load(pic)
        self.bg=pygame.transform.scale(self.bg,(self.size[0],self.size[1]))
        self.state=True
        self.count=0
        self.sound=mixer.Sound("./assets/sounds/button.mp3")


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
                    self.sound.play()
                    return True
        return False

    def click(self):
        self.state=False
        self.count=0

class levelbutton(button):
    def __init__(self,screen,pos,size,num,lock) -> None:
        self.num=num
        self.lock=lock
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(str(self.num+1), True, (0,0,0))
        self.sound=mixer.Sound("./assets/sounds/button.mp3")
        if(not self.lock):
            super().__init__(screen,pos,size,"./assets/images/levels.png")
        else:
            super().__init__(screen,pos,size,"./assets/images/lockedlevel.png")
    
    def show(self):    
        self.count+=1
        if(self.count>15):
            self.state=True
        self.screen.blit(self.bg,self.pos)
        if(not self.lock):
            self.screen.blit(self.text,(self.pos[0]+25, self.pos[1]+self.size[1]//2))
            # textRect = self.text.get_rect()
            # textRect.center = (self.pos[0], self.pos[1]+self.size[1]//2)
        mx,my=pygame.mouse.get_pos()
        if(self.state):
            if((self.pos[0]<=mx<=self.pos[0]+self.size[0]) and
                (self.pos[1]<=my<=self.pos[1]+self.size[1]) ):
                mouse_state=pygame.mouse.get_pressed()
                if(mouse_state[0]):
                    self.sound.play()
                    return True
        return False
        


