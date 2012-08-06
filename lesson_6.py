import pygame , item

screen = pygame.display.set_mode( (800,600) )

pygame.key.set_repeat(200, 1)
		
bg=item.Item("Sky.png")
bg.update(screen)

bob = item.Item("MR_bob.png")
bob.place(300, 250)
bob.update(screen)

wall = item.Item("Blocking_cloud.png")

pygame.display.flip()

def processTick():
	bg.update(screen)
	wall.update(screen)
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
			bob.moveIn(bg, 0,-3 )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_DOWN:
			bob.moveIn(bg, 0,3 )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			bob.moveIn(bg, 3,0 )
			processTick()
		if event.type==pygame.KEYDOWN and event.key == pygame.K_LEFT:
			bob.moveIn(bg, -3,0 )
			processTick()

		if event.type==pygame.MOUSEBUTTONDOWN:
			mouseClicked()
		

	pygame.time.delay(10)

	




