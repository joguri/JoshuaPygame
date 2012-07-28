import pygame , sys

screen = pygame.display.set_mode( (800,600) )

background = pygame.image.load("Sky.png")
backgroundRect = background.get_rect()

screen.blit(background,backgroundRect)

pygame.key.set_repeat(200, 1)


person = pygame.image.load("MR_bob.png")
personRect = person.get_rect()

screen.blit(person,personRect)



pygame.display.flip()

def Moveit():
	i = 0
	while (i < 20):
		personRect.move_ip( [1,1] )
		processTick()
		i = i + 1

def processTick():

	screen.blit(background,backgroundRect)
	screen.blit(person,personRect)
	pygame.display.flip()

while 1==1:
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN and event.key == pygame.K_q:
			exit()
		if event.type==pygame.QUIT:
			exit()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_UP:
			personRect.move_ip( [0,-20] )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_DOWN:
			personRect.move_ip( [0,20] )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			personRect.move_ip( [20,0] )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_LEFT:
			personRect.move_ip( [-20,0] )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
			Moveit()

	

	pygame.time.delay(100)




