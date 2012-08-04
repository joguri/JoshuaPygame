import pygame , sys

screen = pygame.display.set_mode( (800,600) )

background = pygame.image.load("Sky.png")
backgroundRect = background.get_rect()

screen.blit(background,backgroundRect)

pygame.key.set_repeat(200, 1)


person = pygame.image.load("MR_bob.png")
personRect = person.get_rect()
screen.blit(person,personRect)

pygame.mixer.init()
smack = pygame.mixer.Sound("Smack.ogg")

pygame.display.flip()

walls = []

def Moveit():
	i = 0
	while (i < 20):
		personMove(1,1)
		processTick()
		i = i + 1

def processTick():
	screen.blit(background,backgroundRect)
	screen.blit(person,personRect)
	for wall in walls:
		screen.blit(wall[0], wall[1])
	pygame.display.flip()

def personMove(x,y):
	if backgroundRect.contains(personRect):
		personRect.move_ip( [x,y] )
		if  not backgroundRect.contains(personRect):
			personRect.move_ip( [-x,-y])
			smack.play()
def mouseClick(event):
	pos = pygame.mouse.get_pos()
	print(pos[0], pos[1])
	objx = pygame.image.load("Blocking_cloud.png")
	recx = objx.get_rect()
	walls.append( [objx, recx] )
	recx.x = pos[0]
	recx.y = pos[1]
	processTick()

while 1==1:
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN and event.key == pygame.K_q:
			exit()
		if event.type==pygame.QUIT:
			exit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			processTick()
			mouseClick(event)
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
	pygame.time.delay(10);

