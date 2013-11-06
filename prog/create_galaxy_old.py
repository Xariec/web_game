import random
import pymongo
import time
import string

db = pymongo.Connection('localhost', 27017).game

main_sizes = ('Extra Small', 'Small', 'Medium', 'Large', 'Extra Large')

type = {'Extra Small' : "Red Dwarf" , 'Small' : "Yellow Dwarf" , 'Medium' : "Yellow Star" , 'Large' : "Giant Star" , 'Extra Large' : "Super Giant"}

size = {'Extra Small' : 2 , 'Small' : 4 , 'Medium' : 8 , 'Large' : 16 , 'Extra Large' : 32}


def zeus():
	name = "Zeus"
	x = 2629742
	y = 2629742
	solar_system_size = 37000
	star_type = type['Medium']
	print "x - ",x
	print "y - ",y
	print "Star type is" , star_type
	print "Solar system size is" , solar_system_size
	db.universe.insert({'name' : name, 'object' : "star" , 'x_pos' : x, 'y_pos' : y, 'size' : solar_system_size, 'type' : star_type})
	id = db.universe.find_one({'name' : name})
	parent_id =  "object_id("+ id['_id'].__str__()+ ")"
	
	for distance in ((580 , "Mercury"), (1080,"Venus"), (1500,"Earth"), (2280,"Mars"), (7785,"Jupiter"), (14300,"Saturn"), (28800,"Uranus"), (45000,"Neptune"), (59000,"Pluto")):

		while True:
			random_x = random.randrange(-distance[0],distance[0],1)
			random_y = random.randrange(-distance[0],distance[0],1)

			if(random_x <distance[0] and random_x >-distance[0] and random_y <distance[0] and random_y >-distance[0]):
				continue

			else:
				# print distance[0],distance[1], random_x+x, random_y+y
				if distance[1] == "Mercury":
					name = distance[1]
					distance = distance[0]
					velocity = round(random.uniform(1,2),1)*distance
					planet_diameter = 4879
					planet_type = "mineral"
					iron = planet_diameter*random.randint(10,100)
					carbon = planet_diameter*random.randint(5,50)
					oxygen = planet_diameter*random.randint(0,0)
					h2o = planet_diameter*random.randint(0,1)
					deuterium = planet_diameter*random.randint(0,5)
					helium_3 = planet_diameter*random.randint(0,2)
					print name, distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
					db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
				elif distance[1] == "Venus":
					name = distance[1]
					distance = distance[0]
					velocity = round(random.uniform(1,2),1)*distance
					planet_diameter = 12100
					planet_type = "mineral"
					iron = planet_diameter*random.randint(10,100)
					carbon = planet_diameter*random.randint(5,50)
					oxygen = planet_diameter*random.randint(0,0)
					h2o = planet_diameter*random.randint(0,1)
					deuterium = planet_diameter*random.randint(0,5)
					helium_3 = planet_diameter*random.randint(0,2)
					print name, distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
					db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
				elif distance[1] == "Earth":
					name = distance[1]
					distance = distance[0]
					velocity = round(random.uniform(1,2),1)*distance
					planet_diameter = 12742
					planet_type = "organic"
					iron = planet_diameter*random.randint(10,100)
					carbon = planet_diameter*random.randint(5,50)
					oxygen = planet_diameter*random.randint(40,100)
					h2o = planet_diameter*random.randint(30,100)
					deuterium = planet_diameter*random.randint(0,5)
					helium_3 = planet_diameter*random.randint(0,2)
					print name, distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
					db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
				elif distance[1] == "Mars":
					name = distance[1]
					distance = distance[0]
					velocity = round(random.uniform(1,2),1)*distance
					planet_diameter = 6792
					planet_type = "mineral"
					iron = planet_diameter*random.randint(10,100)
					carbon = planet_diameter*random.randint(5,50)
					oxygen = planet_diameter*random.randint(0,0)
					h2o = planet_diameter*random.randint(0,1)
					deuterium = planet_diameter*random.randint(0,5)
					helium_3 = planet_diameter*random.randint(0,2)
					print name, distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
					db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
				elif distance[1] == "Jupiter":
					name = distance[1]
					distance = distance[0]
					velocity = round(random.uniform(1,2),1)*distance
					planet_diameter = 142981
					planet_type = "gas"
					iron = planet_diameter*random.randint(0,0)
					carbon = planet_diameter*random.randint(1,10)
					oxygen = planet_diameter*random.randint(0,5)
					h2o = planet_diameter*random.randint(0,10)
					deuterium = planet_diameter*random.randint(0,0)
					helium_3 = planet_diameter*random.randint(0,5)
					print name, distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
					db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
				elif distance[1] == "Saturn":
					name = distance[1]
					distance = distance[0]
					velocity = round(random.uniform(1,2),1)*distance
					planet_diameter = 120536
					planet_type = "gas"
					iron = planet_diameter*random.randint(0,0)
					carbon = planet_diameter*random.randint(1,10)
					oxygen = planet_diameter*random.randint(0,5)
					h2o = planet_diameter*random.randint(0,10)
					deuterium = planet_diameter*random.randint(0,0)
					helium_3 = planet_diameter*random.randint(0,5)
					print name, distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
					db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
				elif distance[1] == "Uranus":
					name = distance[1]
					distance = distance[0]
					velocity = round(random.uniform(1,2),1)*distance
					planet_diameter = 51118
					planet_type = "gas"
					iron = planet_diameter*random.randint(0,0)
					carbon = planet_diameter*random.randint(1,10)
					oxygen = planet_diameter*random.randint(0,5)
					h2o = planet_diameter*random.randint(0,10)
					deuterium = planet_diameter*random.randint(0,0)
					helium_3 = planet_diameter*random.randint(0,5)
					print name, distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
					db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
				elif distance[1] == "Neptune":
					name = distance[1]
					distance = distance[0]
					velocity = round(random.uniform(1,2),1)*distance
					planet_diameter = 49500
					planet_type = "gas"
					iron = planet_diameter*random.randint(0,0)
					carbon = planet_diameter*random.randint(1,10)
					oxygen = planet_diameter*random.randint(0,5)
					h2o = planet_diameter*random.randint(0,10)
					deuterium = planet_diameter*random.randint(0,0)
					helium_3 = planet_diameter*random.randint(0,5)
					print name, distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
					db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
				elif distance[1] == "Pluto":
					name = distance[1]
					distance = distance[0]
					velocity = round(random.uniform(1,2),1)*distance
					planet_diameter = 2360
					planet_type = "ice"
					iron = planet_diameter*random.randint(0,0)
					carbon = planet_diameter*random.randint(0,0)
					oxygen = planet_diameter*random.randint(0,20)
					h2o = planet_diameter*random.randint(0,30)
					deuterium = planet_diameter*random.randint(0,0)
					helium_3 = planet_diameter*random.randint(0,0)
					print name, distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
					db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
			break

zeus()


# Full galaxy values
# x_min = -5259485
# y_min = -5259485
# x_max = 5259485
# y_max = 5259485
# margin = 5000

# Single quadrant values
x_min = -0
y_min = 0
x_max = 5259485
y_max = 5259485
margin = 37000




def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))


def solar_system():
	for d in range(5000):
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
		solar_system_size = random.randint(900,19200)
		# Check to see if the position chosen has any solar systems nearby that it would collide with.
		position = db.universe.find_one({"x_pos": {"$gte": x-solar_system_size , "$lte": x+solar_system_size},"y_pos": {"$gte": y-solar_system_size, "$lte": y+solar_system_size}})
		time.sleep(2)
		
		# If it doesn't then create the star. We will create the planets later.
		if position == None:
			# Create random name for the star.
			name = id_generator()
			#Insert the star into the database with its information
			db.universe.insert({'name' : name, 'object' : "star" , 'x_pos' : x, 'y_pos' : y, 'size' : solar_system_size, 'type' : star_type})
			#Query the database for the start we just created. We need this to create the planets around it.
			id = db.universe.find_one({'name' : name})
			# Pull the ObjectId from the star to assign to the planets so we can query the star and find the planets.
			parent_id =  "object_id("+ id['_id'].__str__()+ ")"
			time.sleep(2)
			#new function for creating planets. Built inside the main one to pass the varbiles forward.
			def system():
				# First planet is at least 200 away from the star. Otherwise it would be crispy fried. :-) Of course this says 100, but that is because the random number that gets added later starts at a minimum of 100.
				time.sleep(.5)
				a = {}
				planet = 100
				k = 0
				i = random.randint(3,5)*star_size
				while k < i:
					distance_between = random.randrange(50,300,1)
					planet += distance_between
					if planet <= solar_system:
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

								if distance <= 100*star_size:
									possible_planet_type = ('mineral' , 'gas')
									planet_type = random.choice(possible_planet_type)
									if planet_type is "mineral":
										planet_diameter = random.randint(3000,8000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,100)	
										carbon = planet_diameter*random.randint(5,50)
										oxygen = planet_diameter*random.randint(0,0)
										h2o = planet_diameter*random.randint(0,1)
										deuterium = planet_diameter*random.randint(0,5)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "organic":
										planet_diameter = random.randint(8000,10000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "terraform":
										planet_diameter = random.randint(8000,10000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "gas":
										planet_diameter = random.randint(20000,90000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,0)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "ice":
										planet_diameter = random.randint(2000,6000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,1)
										helium_3 = planet_diameter*random.randint(0,1)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									
								elif distance <= 150*star_size and distance >= 101*star_size:
									possible_planet_type = ('organic' , 'teriform')
									planet_type = random.choice(possible_planet_type)
									if planet_type is "mineral":
										planet_diameter = random.randint(3000,8000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,100)	
										carbon = planet_diameter*random.randint(5,50)
										oxygen = planet_diameter*random.randint(0,0)
										h2o = planet_diameter*random.randint(0,3)
										deuterium = planet_diameter*random.randint(0,5)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "organic":
										planet_diameter = random.randint(8000,10000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "terraform":
										planet_diameter = random.randint(8000,10000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "gas":
										planet_diameter = random.randint(20000,90000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,0)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "ice":
										planet_diameter = random.randint(2000,6000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,1)
										helium_3 = planet_diameter*random.randint(0,1)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									
									
								elif distance <= 300*star_size and distance >=  151*star_size:
									possible_planet_type = ('mineral' , 'gas', 'ice')
									planet_type = random.choice(possible_planet_type)
									if planet_type is "mineral":
										planet_diameter = random.randint(3000,8000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,100)	
										carbon = planet_diameter*random.randint(5,50)
										oxygen = planet_diameter*random.randint(0,0)
										h2o = planet_diameter*random.randint(0,3)
										deuterium = planet_diameter*random.randint(0,5)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "organic":
										planet_diameter = random.randint(8000,10000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "terraform":
										planet_diameter = random.randint(8000,10000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "gas":
										planet_diameter = random.randint(20000,90000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,0)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "ice":
										planet_diameter = random.randint(2000,6000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,1)
										helium_3 = planet_diameter*random.randint(0,1)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									
									
								elif distance <= 500*star_size and distance >=  301*star_size:
									possible_planet_type = ('mineral' , 'gas' , 'ice')
									planet_type = random.choice(possible_planet_type)
									if planet_type is "mineral":
										planet_diameter = random.randint(3000,8000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,100)	
										carbon = planet_diameter*random.randint(5,50)
										oxygen = planet_diameter*random.randint(0,0)
										h2o = planet_diameter*random.randint(0,3)
										deuterium = planet_diameter*random.randint(0,5)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "organic":
										planet_diameter = random.randint(8000,10000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "terraform":
										planet_diameter = random.randint(8000,10000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,3)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "gas":
										planet_diameter = random.randint(20000,90000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,0)
										helium_3 = planet_diameter*random.randint(0,2)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									elif planet_type is "ice":
										planet_diameter = random.randint(2000,6000)
										velocity = round(random.uniform(1,2),1)*distance
										iron = planet_diameter*random.randint(10,20)
										carbon = planet_diameter*random.randint(5,10)
										oxygen = planet_diameter*random.randint(40,100)
										h2o = planet_diameter*random.randint(30,100)
										deuterium = planet_diameter*random.randint(0,1)
										helium_3 = planet_diameter*random.randint(0,1)
										name = a[distance]
										db.universe.insert({'name' : name, 'x_pos' : random_x+x, 'y_pos' : random_y+y, 'diameter' : planet_diameter, 'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'velocity' : velocity})
									
							break
							
				planets()

			system()
		else:
			print "found a solar system at %d,%d" %(position['x_pos'],position['y_pos'])

solar_system()
