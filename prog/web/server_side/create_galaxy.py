import pymongo
import time
import string
import random
import math

db = pymongo.Connection('localhost', 27017).bbarnes_test

main_sizes = ('Extra Small', 'Small', 'Medium', 'Large', 'Extra Large')

type = {'Extra Small' : "Red Dwarf" , 'Small' : "Yellow Dwarf" , 'Medium' : "Yellow Star" , 'Large' : "Giant Star" , 'Extra Large' : "Super Giant"}

size = {'Extra Small' : 2 , 'Small' : 4 , 'Medium' : 8 , 'Large' : 16 , 'Extra Large' : 32}


def zeus():
	name = "Sun"
	find = db.universe.find_one({'name' : name})
	if find == None:
		x = 0
		y = 0
		solar_system_size = 3700
		star_type = type['Medium']
		db.universe.insert({'name' : name, 'object' : "star" , 'x_pos' : x, 'y_pos' : y, 'size' : solar_system_size, 'type' : star_type})
		id = db.universe.find_one({'name' : name})
		parent_id =  "object_id("+ id['_id'].__str__()+ ")"
		for x in range(100):
			x = random.randint(-solar_system_size, solar_system_size)
			new_x = math.pow(x,2)
			radius = math.pow(solar_system_size,2)
			y = math.sqrt(radius-new_x)
			db.universe.insert({'x_pos' : round(x), 'y_pos' : round(y), 'object' : "circumference"})
			db.universe.insert({'x_pos' : -round(x), 'y_pos' : -round(y), 'object' : "circumference"})
		for y in range(100):
			y = random.randint(-solar_system_size, solar_system_size)
			new_y = math.pow(y,2)
			radius = math.pow(solar_system_size,2)
			x = math.sqrt(radius-new_y)
			db.universe.insert({'x_pos' : round(x), 'y_pos' : round(y), 'object' : "circumference"})
			db.universe.insert({'x_pos' : -round(x), 'y_pos' : -round(y), 'object' : "circumference"})
		for distance in ((36 , "Mercury"), (67,"Venus"), (92,"Earth"), (141,"Mars"), (483,"Jupiter"), (886,"Saturn"), (1782,"Uranus"), (2794,"Neptune"), (3666,"Pluto")):
			r = distance[0]
			print " %s is %d away from the sun" %(distance[1],r)
			x = random.randint(-r,r)
			new_x = math.pow(round(x),2)
			radius = math.pow(r,2)
			y = math.sqrt(radius-round(new_x))
			y = round(y)
			print y
			if distance[1] == "Mercury":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 3031
				planet_type = "mineral"
				iron = planet_diameter*random.randint(10,100)
				carbon = planet_diameter*random.randint(5,50)
				oxygen = planet_diameter*random.randint(0,0)
				h2o = planet_diameter*random.randint(0,1)
				deuterium = planet_diameter*random.randint(0,5)
				helium_3 = planet_diameter*random.randint(0,2)
				print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
			elif distance[1] == "Venus":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 7518
				planet_type = "mineral"
				iron = planet_diameter*random.randint(10,100)
				carbon = planet_diameter*random.randint(5,50)
				oxygen = planet_diameter*random.randint(0,0)
				h2o = planet_diameter*random.randint(0,1)
				deuterium = planet_diameter*random.randint(0,5)
				helium_3 = planet_diameter*random.randint(0,2)
				print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
			elif distance[1] == "Earth":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 7918
				planet_type = "organic"
				iron = planet_diameter*random.randint(10,100)
				carbon = planet_diameter*random.randint(5,50)
				oxygen = planet_diameter*random.randint(40,100)
				h2o = planet_diameter*random.randint(30,100)
				deuterium = planet_diameter*random.randint(0,5)
				helium_3 = planet_diameter*random.randint(0,2)
				print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
			elif distance[1] == "Mars":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 4222
				planet_type = "mineral"
				iron = planet_diameter*random.randint(10,100)
				carbon = planet_diameter*random.randint(5,50)
				oxygen = planet_diameter*random.randint(0,0)
				h2o = planet_diameter*random.randint(0,1)
				deuterium = planet_diameter*random.randint(0,5)
				helium_3 = planet_diameter*random.randint(0,2)
				print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
			elif distance[1] == "Jupiter":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 88844
				planet_type = "gas"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(1,10)
				oxygen = planet_diameter*random.randint(0,5)
				h2o = planet_diameter*random.randint(0,10)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,5)
				print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
			elif distance[1] == "Saturn":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 74898
				planet_type = "gas"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(1,10)
				oxygen = planet_diameter*random.randint(0,5)
				h2o = planet_diameter*random.randint(0,10)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,5)
				print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
			elif distance[1] == "Uranus":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 31763
				planet_type = "gas"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(1,10)
				oxygen = planet_diameter*random.randint(0,5)
				h2o = planet_diameter*random.randint(0,10)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,5)
				print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3

				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
			elif distance[1] == "Neptune":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 30758
				planet_type = "gas"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(1,10)
				oxygen = planet_diameter*random.randint(0,5)
				h2o = planet_diameter*random.randint(0,10)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,5)
				print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
			elif distance[1] == "Pluto":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 1466
				planet_type = "ice"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(0,0)
				oxygen = planet_diameter*random.randint(0,20)
				h2o = planet_diameter*random.randint(0,30)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,0)
				print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3

				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
		# break
	else:
		print "Zeus already exists."
		print find
zeus()


# Full galaxy values
# x_min = -5259485
# y_min = -5259485
# x_max = 5259485
# y_max = 5259485
# margin = 5000

# Single quadrant values
x_min = -29742
y_min = -29742
x_max = 29742
y_max = 29742
margin = 3700



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))


def solar_system():
	for d in range(500000):
		print "d is ", d
		# Define a random x and y value that is between the min and max and includes a 5000 sector distance from the edge of the map so the star isn't on the edge.
		x = random.randint(x_min+margin,x_max-margin)
		y = random.randint(y_min+margin,y_max-margin)
		# Randomly choose on solar system size
		decide = random.choice(main_sizes)
		# Sets the randomly chosen star size and type.
		star_size = size[decide]
		star_type = type[decide]
		# multiplies the star size to the initial vales to create the solar system sizes
		# Solar systems around anywhere from 900 sectors to 19200 depending on the size of the star.
		solar_system_size = random.randint(900,4250)
		# Check to see if the position chosen has any solar systems nearby that it would collide with.
		position = db.universe.find_one({"x_pos": {"$gte": x-solar_system_size*2 , "$lte": x+solar_system_size*2},"y_pos": {"$gte": y-solar_system_size*2, "$lte": y+solar_system_size*2}})
		# time.sleep(2)
		
		# If it doesn't then create the star. We will create the planets later.
		if position == None:
			print star_size
			#time.sleep(1)
			# Create random name for the star.
			name = id_generator()
			#Insert the star into the database with its information
			db.universe.insert({'name' : name, 'object' : "star" , 'x_pos' : x, 'y_pos' : y, 'size' : solar_system_size, 'type' : star_type})
			#Query the database for the start we just created. We need this to create the planets around it.
			id = db.universe.find_one({'name' : name})
			# Pull the ObjectId from the star to assign to the planets so we can query the star and find the planets.
			parent_id =  "object_id("+ id['_id'].__str__()+ ")"
			# time.sleep(2)
			#new function for creating planets. Built inside the main one to pass the varbiles forward.
			def system():
				# First planet is at least 70 sectors away from the star. Otherwise it would be crispy fried. :-) Of course this says 50, but that is because the random number that gets added later starts at a minimum of 100.
				a = {}
				planet = 50
				k = 0
				i = random.randint(1,4)*star_size
				while k < i:
					distance_between = random.randrange(30,300,1)
					planet += distance_between
					if planet <= solar_system_size:
						key = planet
						name = id_generator()
						a[key] = name
						k += 1
					else:
						break
				def planets():
					for distance in (a):
						while True:
							random_x = random.randint(-distance,distance)
							random_y = random.randint(-distance,distance)

							if(random_x <distance and random_x >-distance and random_y <distance and random_y >-distance):
								continue

							else:
								if star_size*10 >= distance:
									possible_planet_type = ('mineral' , 'gas')
									planet_type = random.choice(possible_planet_type)
									if planet_type =="mineral":
										planet_diameter = random.randint(3000,8000)
										iron = planet_diameter*random.randint(10,100)	
										carbon = planet_diameter*random.randint(5,50)
										oxygen = planet_diameter*random.randint(0,0)
										h2o = planet_diameter*random.randint(0,1)
										deuterium = planet_diameter*random.randint(0,5)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="organic":
										planet_diameter = random.randint(8000,10000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="terraform":
										planet_diameter = random.randint(8000,10000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="gas":
										planet_diameter = random.randint(20000,90000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,0)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="ice":
										planet_diameter = random.randint(2000,6000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,1)
										helium_3 = planet_diameter*random.randint(0,1)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									
								elif distance <= 15*star_size and distance >= 11*star_size:
									possible_planet_type = ('organic', 'terraform')
									planet_type = random.choice(possible_planet_type)
									if planet_type =="mineral":
										planet_diameter = random.randint(3000,8000)
										iron = planet_diameter*random.randint(10,100)	
										carbon = planet_diameter*random.randint(5,50)
										oxygen = planet_diameter*random.randint(0,0)
										h2o = planet_diameter*random.randint(0,1)
										deuterium = planet_diameter*random.randint(0,5)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="organic":
										planet_diameter = random.randint(8000,10000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="terraform":
										planet_diameter = random.randint(8000,10000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="gas":
										planet_diameter = random.randint(20000,90000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,0)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="ice":
										planet_diameter = random.randint(2000,6000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,1)
										helium_3 = planet_diameter*random.randint(0,1)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									
									
								elif distance <= 30*star_size and distance >=  16*star_size:
									possible_planet_type = ('mineral' , 'gas', 'ice')
									planet_type = random.choice(possible_planet_type)
									if planet_type =="mineral":
										planet_diameter = random.randint(3000,8000)
										iron = planet_diameter*random.randint(10,100)	
										carbon = planet_diameter*random.randint(5,50)
										oxygen = planet_diameter*random.randint(0,0)
										h2o = planet_diameter*random.randint(0,1)
										deuterium = planet_diameter*random.randint(0,5)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="organic":
										planet_diameter = random.randint(8000,10000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="terraform":
										planet_diameter = random.randint(8000,10000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="gas":
										planet_diameter = random.randint(20000,90000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,0)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="ice":
										planet_diameter = random.randint(2000,6000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,1)
										helium_3 = planet_diameter*random.randint(0,1)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									
								elif distance >=  31*star_size:
									possible_planet_type = ('gas', 'ice')
									planet_type = random.choice(possible_planet_type)
									if planet_type =="mineral":
										planet_diameter = random.randint(3000,8000)
										iron = planet_diameter*random.randint(10,100)	
										carbon = planet_diameter*random.randint(5,50)
										oxygen = planet_diameter*random.randint(0,0)
										h2o = planet_diameter*random.randint(0,1)
										deuterium = planet_diameter*random.randint(0,5)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="organic":
										planet_diameter = random.randint(8000,10000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="terraform":
										planet_diameter = random.randint(8000,10000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="gas":
										planet_diameter = random.randint(20000,90000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,0)
										helium_3 = planet_diameter*random.randint(0,2)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									elif planet_type =="ice":
										planet_diameter = random.randint(2000,6000)
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,1)
										helium_3 = planet_diameter*random.randint(0,1)
										# print planet_type, planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type})
									
							break
							
				planets()

			system()
		else:
			print "found a solar system at %d,%d" %(position['x_pos'],position['y_pos'])

solar_system()

