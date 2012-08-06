import pygame

pygame.mixer.init()
smack = pygame.mixer.Sound("Smack.ogg")
class Item:
    def __init__ (self,fileName):
        self.img=pygame.image.load(fileName)
        self.rec=self.img.get_rect()
    def update (self,screen):
        screen.blit(self.img,self.rec)
    def moveIn (self,container,x,y):
        if container.rec.contains(self.rec):
            self.rec.move_ip( [x,y] )
            if  not container.rec.contains(self.rec):
                self.rec.move_ip( [-x,-y])
                smack.play()
    def place(self,x,y):
        self.rec.x=x
        self.rec.y=y