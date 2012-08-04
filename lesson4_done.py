import pygame , sys

screen = pygame.display.set_mode( (800,600) )


class Character(Item):
	def move(self, x,y):
		self.rec.move_ip( [x,y] )

pygame.key.set_repeat(200, 1)



bgItem = Item("Sky.png")
bgItem.update(screen)

pygame.key.set_repeat(1, 1)

bob = Character("MR_bob.png")
bob.update(screen)

pygame.display.flip()

def Moveit():
	i = 0
	while (i < 20):
		personRect.move_ip( [1,1] )
		processTick()
		i = i + 1

def processTick():
	bgItem.update(screen)
	bob.update(screen)
	pygame.display.flip()

while 1==1:
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN and event.key == pygame.K_q:
			exit()
		if event.type==pygame.QUIT:
			exit()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_UP:
			bob.move(0,-20);
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_DOWN:
			bob.move(0,20);
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			bob.move(20,0);
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_LEFT:
			bob.move(-20,0);
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
			Moveit()

	

	pygame.time.delay(100)



