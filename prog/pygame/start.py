import sys, pygame, random





# Game Parameters


size = width, height = 400, 400



pygame.init()

screen = pygame.display.set_mode(size)


	
while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
