import pygame
from item import *

screen = pygame.display.set_mode( (800,600) )

pygame.key.set_repeat(200, 1)
		
bg=Item("Sky.png")
bg.update(screen)

bob = Character("MR_bob.png")
bob.place(300, 250)
bob.update(screen)
bob.container=bg

music.play()

sheller = Character("sheller.png")
sheller.place(400, 400)
sheller.update(screen)
sheller.container=bg
bob.enemy=sheller

wall = Item("Blocking_cloud.png")

pygame.display.flip()

def processTick():
	bg.update(screen)
	wall.update(screen)
	sheller.update(screen)
	bob.update(screen)
	pygame.display.flip()

def mouseClicked():
	pos = pygame.mouse.get_pos()
	wall.rec.x = pos[0]
	wall.rec.y = pos[1]
	processTick()
	
while 1==1:
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN and event.key == pygame.K_q:
			exit()
		if event.type==pygame.QUIT:
			exit()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_UP:
			bob.ySpeed-=1
		if event.type==pygame.KEYDOWN and event.key == pygame.K_DOWN:
			bob.ySpeed+=1
		if event.type==pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			bob.xSpeed+=1
		if event.type==pygame.KEYDOWN and event.key == pygame.K_LEFT:
			bob.xSpeed-=1
		if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
			bob.jump()
		if event.type==pygame.MOUSEBUTTONDOWN:
			mouseClicked()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_v:
			bob.visible=False
		if event.type==pygame.KEYDOWN and event.key == pygame.K_r:
			bob.visible=True
		
	processTick()
	pygame.time.delay(10)

	




