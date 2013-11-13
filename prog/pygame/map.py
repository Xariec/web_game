import sys, pygame
from pygame.locals import *
import pymongo
import time


#	Pymongo values
db = pymongo.Connection('localhost', 27017).game
u_id = db.users.find_one({'username' : "defender"})['_id']
p_id= db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
#	Pygame values
pygame.init()
size = width, height, = 1280,720
color = (0,0,255)
screen = pygame.display.set_mode(size)
x_tf = 500
y_tf = height/2
black = 0, 0, 0

db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : 0, 'y' : 0}})
incrament = .25

def map(p_id, incrament):
	lvl = int(100000000*incrament)
	view = 500*lvl
	p_id= db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
	p_x = p_id['x']
	p_y = p_id['y']
	# print x, y
	player_x = player_y = 0
	radius = 5
	color = (0,0,255)
	thickness = 1
	pygame.draw.circle(screen, color, (player_x+x_tf,player_y+y_tf), radius, thickness)
	
	all = db.universe.find({"x_pos": {"$gte": p_x - view , "$lte": p_x + view},"y_pos": {"$gte": p_y - view, "$lte": p_y + view}})
	items = []
	for a in all:
		x = (a['x_pos']-p_x)/lvl+x_tf
		y = (a['y_pos']-p_y)/lvl+y_tf
		if x < 0 or y < 0 or x > width or y > height:
			continue
		else:

			
			items.append((x,y,a['name']))
			# print x,y, a['name']
		
	for b in range(len(items)):
		item = items[b]
		x = item[0]
		y = item[1]
		name = item[2]
		radius = 1
		color = (0,255,0)
		thickness = 1
		font = pygame.font.Font(None, 12)
		text = font.render(name,1, (255,0,0))
		screen.blit(text, (x,y))
		
		pygame.draw.circle(screen, color, (x,y), radius, thickness)
		
	
	pygame.display.flip()



x = y = 0
map(p_id,incrament)
while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			m_button = pygame.mouse.get_pressed()
			if m_button == (1,0,0):
				print incrament
				if incrament > .1:
					incrament = incrament - .05
					print incrament
				else:
					incrament = .05
			elif m_button == (0,0,1):
				print incrament
				if incrament < 2:
					incrament = incrament + .05
				else:
					incrament = 2
					
				print "Right"
			screen.fill(black)
			map(p_id,incrament)
		if event.type == KEYDOWN:
			move = 10000000*50
			p_id= db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
			x = p_id['x']
			y = p_id['y']
			key = pygame.key.get_pressed()
			if key:
				if key[pygame.K_UP]:
					print "Up was pressed"
					db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'y' : y-move}})
				elif key[pygame.K_DOWN]:
					db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'y' : y+move}})
					print "Down was pressed"
				elif key[pygame.K_LEFT]:
					db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : x-move}})
					print "Left was pressed"
				elif key[pygame.K_RIGHT]:
					db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : x+move}})
					print "Right was pressed"
				screen.fill(black)
				map(p_id,incrament)
				print " Done"
			
			# mouse_down = pygame.mouse.get_pos()
			# print mouse_down
			# x = x + (mouse_down[0]-500)*lvl
			# y = y +(mouse_down[1]-500)*lvl
			# print x,y
			# screen.fill(black)
			# map(x,y,lvl,view)