import pygame

screen = pygame.display.set_mode( (800,600) )

background = pygame.image.load("Sky.png")
backgroundRect = background.get_rect()

screen.blit(background,backgroundRect)


person = pygame.image.load("MR_bob.png")
personRect = person.get_rect()

screen.blit(person,personRect)



pygame.display.flip()

def processTick():

	screen.blit(background,backgroundRect)
	screen.blit(person,personRect)
	pygame.display.flip()

while 1==1:
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN and event.key == pygame.K_q:
			exit()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_UP:
			personRect.move_ip( [0,-10] )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_DOWN:
			personRect.move_ip( [0,10] )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			personRect.move_ip( [10,0] )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_LEFT:
			personRect.move_ip( [-10,0] )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
			personRect.move_ip( [4,4] )
			processTick()

	

	pygame.time.delay(100)




