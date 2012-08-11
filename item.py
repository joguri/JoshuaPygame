import pygame

pygame.mixer.init()
smack = pygame.mixer.Sound("Smack.ogg")

class Item:
    def __init__ (self,fileName):
        self.img=pygame.image.load(fileName)
        self.rec=self.img.get_rect()
        self.xSpeed=0
        self.ySpeed=0
        self.inAir=True
        self.container=None
        self.visible=True
    
    def stop (self):
        self.xSpeed=0
        self.ySpeed=0 
        
    def update (self,screen):
        if self.visible==True:
            if self.inAir==True:
                self.ySpeed+=1
            screen.blit(self.img,self.rec)
        
    def place(self,x,y):
        self.rec.x=x
        self.rec.y=y


class Character(Item):
    def __init__(self, fileName):
        Item.__init__(self, fileName)
        self.wall = None
        
    def jump (self):
        self.ySpeed=-10
        self.inAir=True
        
    def update(self, screen):
        Item.update(self, screen)
        self.moveIn(self.container,self.xSpeed,self.ySpeed)

    def moveIn (self,container,x,y):
        if container and container.rec.contains(self.rec):
            self.rec.move_ip( [x,y] )
            if  not container.rec.contains(self.rec):
                self.rec.move_ip( [-x,-y])
                smack.play()
                self.stop()
                self.inAir=False
    
class Wall(Item):
    def update(self,screen):
        if self.visible==True:
            screen.blit(self.img,self.rec)
            