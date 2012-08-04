import pygame , sys

screen = pygame.display.set_mode( (800,600) )

background = pygame.image.load("Sky.png")
backgroundRect = background.get_rect()
screen.blit(background,backgroundRect)

pygame.key.set_repeat(200, 1)


person = pygame.image.load("MR_bob.png")
personRect = person.get_rect()
screen.blit(person,personRect)

wall = pygame.image.load("Blocking_cloud.png")
wallRect = wall.get_rect()
# screen.blit(wall,wallRect)

pygame.mixer.init()
smack = pygame.mixer.Sound("Smack.ogg")

pygame.display.flip()

def Moveit():
	i = 0
	while (i < 20):
		personMove(1,1)
		processTick()
		i = i + 1

def processTick():
	screen.blit(background,backgroundRect)
	screen.blit(wall,wallRect)
	screen.blit(person,personRect)
	pygame.display.flip()

def mouseClicked():
	pos = pygame.mouse.get_pos()
	wallRect.x = pos[0]
	wallRect.y = pos[1]
	processTick()
	
def personMove(x,y):
	if backgroundRect.contains(personRect):
		personRect.move_ip( [x,y] )
		if  not backgroundRect.contains(personRect):
			personRect.move_ip( [-x,-y])
			smack.play()
		if personRect.colliderect(wallRect):
			personRect.move_ip( [-x,-y])
			smack.play()
			
		   
	
while 1==1:
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN and event.key == pygame.K_q:
			exit()
		if event.type==pygame.QUIT:
			exit()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_UP:
			personMove( 0,-3 )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_DOWN:
			personMove( 0,3 )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			personMove( 3,0 )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_LEFT:
			personMove( -3,0 )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
			Moveit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			mouseClicked()
		

	pygame.time.delay(10)

	




