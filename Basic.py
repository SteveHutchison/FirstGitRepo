import sys, pygame
import random
pygame.init()

speed = [(random.randrange(2) + 1), (random.randrange(2) + 1)]

black = 0, 0, 0

ball = pygame.image.load("ball.bmp")
ball2 = pygame.image.load("ball2.bmp")
ball3 = pygame.image.load("ball3.bmp")
background = pygame.image.load("BG.bmp")

ballrect = ball.get_rect()
ballrect2 = ball2.get_rect()
ballrect3 = ball3.get_rect()
backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

ballrect2 = ballrect2.move(100, 0)
b3x = 0
b3y = 0
movex = 0
movey = 0

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	#move ball 3 based on keyboard input	
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				movex =- 1
			elif event.key==pygame.K_RIGHT:
				movex =+ 1
			elif event.key==pygame.K_UP:
				movey =- 1
			elif event.key==pygame.K_DOWN:
				movey =+ 1
		
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT:
				movex = 0
			elif event.key==pygame.K_RIGHT:
				movex = 0
			elif event.key==pygame.K_UP:
				movey = 0
			elif event.key==pygame.K_DOWN:
				movey = 0
	
	if b3x + movex < 0 or b3x + ballrect3.width + movex > backgroundRect.width:
		movex = 0
		
	if b3y + movey < 0 or b3y + ballrect3.height + movey > backgroundRect.height:
		movey = 0

	b3x +=movex
	b3y += movey
	
	#move a ball randomly around the screen
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		
	#follow the mouse with a ball	
	b2x,b2y = pygame.mouse.get_pos()
	b2x -= ballrect2.width / 2
	b2y -= ballrect2.height/ 2
	
	screen.blit(background, backgroundRect)
	screen.blit(ball, ballrect)
	screen.blit(ball2,(b2x,b2y))
	screen.blit(ball3,(b3x,b3y))
	
	pygame.display.flip()