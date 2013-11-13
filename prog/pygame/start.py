import sys, pygame
from pygame.locals import *
import pymongo


#	Pymongo values
db = pymongo.Connection('localhost', 27017).game
u_id = db.users.find_one()['_id']

#	Pygame values
pygame.init()
size = width, height, = 1024,786
color = (0,0,255)
screen = pygame.display.set_mode(size)
x_transform = 500
y_transform = 393
black = 0, 0, 0

# objects_name = []
# objects_type = []
# objects_location = []
# objects_color = []
# objects_size = []
# player_ship = []

# def find_player(u_id):
	# main_ship = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
	# lvl = 15000000000
	# scale = lvl/1500
	# x = int(main_ship['x'])/scale-x_transform
	# y = int(main_ship['y'])/scale-y_transform
	# print x, y
	# if x <= 0:
		# x = x*-1
		# player_ship.append(x)
	# else:
		# player_ship.append(x)
	# if y<= 0:
		# y = y*-1
		# player_ship.append(y)
	# else:
		# player_ship.append(y)
	# position = db.universe.find({"x_pos": {"$gte": x - lvl , "$lte": x + lvl},"y_pos": {"$gte": y - lvl, "$lte": y + lvl}})
	# for a in position:
		# # print a['name']
		# objects_name.append(a['name'])
		# objects_type.append(a['item'])
		# x = (int(a['x_pos']))/scale-x_transform
		# y = (int(a['y_pos']))/scale-y_transform
		# if x <= 0:
			# x = x*-1
			# if y <= 0:
				# y = y*-1
				# objects_location.append((x,y))
			# else:
				# objects_location.append((x,y))
		# if a['item'] == "planet":
			# objects_size.append(1)
			# objects_color.append((0,255,0))
		# elif a['item'] == "star":
			# # objects_size.append(x['diameter']/lvl)
			# objects_size.append(3)
			# objects_color.append((255,255,0))
		# else:
			# objects_size.append(1)
			# objects_color.append((255,0,0))
	









def map(u_id):
	objects_name = []
	objects_type = []
	objects_location = []
	objects_color = []
	objects_size = []
	main_ship = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
	lvl = 15000000000
	scale = lvl/300
	x = int(main_ship['x'])
	y = int(main_ship['y'])
	print x, y
	position = db.universe.find({"x_pos": {"$gte": x - lvl , "$lte": x + lvl},"y_pos": {"$gte": y - lvl, "$lte": y + lvl}})
	for a in position:
		# print a['name']
		objects_name.append(a['name'])
		objects_type.append(a['item'])
		x = (int(a['x_pos']-x))/scale-x_transform
		y = (int(a['y_pos']-y))/scale-y_transform
		
		if x <= 0:
			x = x*-1
			if y <= 0:
				y = y*-1
				objects_location.append((x,y))
				# print "Objects X and Y :", x,y
			else:
				objects_location.append((x,y))
				# print "Objects X and Y :", x,y
		if a['item'] == "planet":
			objects_size.append(1)
			objects_color.append((0,255,0))
		elif a['item'] == "star":
			# objects_size.append(x['diameter']/lvl)
			objects_size.append(3)
			objects_color.append((255,255,0))
		else:
			objects_size.append(1)
			objects_color.append((255,0,0))
	# print objects_location
	screen.fill(black)
	x = x_transform
	y = y_transform
	radius = 5
	color = (0,0,255)
	thickness = 1
	pygame.draw.circle(screen, color, (x,y), radius, thickness)
	pygame.display.flip()
	
	x = 20
	y = 20
	radius = 15
	color = (0,0,255)
	thickness = 1
	pygame.draw.circle(screen, color, (x,y), radius, thickness)
	pygame.display.flip()
	
	for a in range(len(objects_location)):
		position = objects_location[a]
		x = position[0]
		y = position[1]
		radius = objects_size[a]
		color = objects_color[a]
		thickness = 1
		pygame.draw.circle(screen, color, (x,y), radius, thickness)
		pygame.display.flip()


map(u_id)
while True:


	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			mouse_down = pygame.mouse.get_pos()
			print mouse_down
			my_location = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
			x = (mouse_down[0]-500)*10000000-my_location['x']
			y = (mouse_down[1]-500)*10000000-my_location['y']
			print x, y
			# print x, y
			# db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : x*10000000, 'y' : y*10000000}})
			map(u_id)
			# x = mouse_down[0]-5
			# y = mouse_down[1]-5
		if event.type == KEYDOWN:
			key = pygame.key.get_pressed()
			movement = 100000000
			if key[pygame.K_LEFT]:
				x = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})['x']
				print x
				db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : x+movement}})
				print "moved_left"
				map(u_id)
			elif key[pygame.K_RIGHT]:
				x = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})['x']
				print x
				db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : x-movement}})	
				print "moved_right"
				map(u_id)
			elif key[pygame.K_UP]:
				y = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})['y']
				print y
				db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'y' : y-movement}})
				print "moved_up"
				map(u_id)
			elif key[pygame.K_DOWN]:
				y = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})['y']
				print y
				db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'y' : y+movement}})
				print "moved_down"
				map(u_id)
			else: 
				break

		
		
	