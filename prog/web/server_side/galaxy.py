import pymongo
import string
import random
import math
import datetime


now = datetime.datetime.now()


db = pymongo.Connection('localhost', 27017).game

main_sizes = ('Extra Small', 'Small', 'Medium', 'Large', 'Extra Large')

type = {'Extra Small' : "Red Dwarf" , 'Small' : "Yellow Dwarf" , 'Medium' : "Yellow Star" , 'Large' : "Giant Star" , 'Extra Large' : "Super Giant"}

size = {'Extra Small' : 2 , 'Small' : 4 , 'Medium' : 8 , 'Large' : 16 , 'Extra Large' : 32}


def zeus():
	name = "Zeus"
	find = db.universe.find_one({'name' : name})
	if find == None:
		star_x = 15000
		star_y = 15000
		solar_system_size = 6000
		star_size = size['Medium']
		star_type = type['Medium']
		db.universe.insert({'name' : name, 'object' : "star" , 'x_pos' : star_x, 'y_pos' : star_y, 'size' : solar_system_size, 'type' : star_type, 'star_size' : star_size})
		id = db.universe.find_one({'name' : name})
		# parent_id =  "object_id("+ id['_id'].__str__()+ ")"
		parent_id =  id['_id']
		for x in range(100):
			x = random.randint(-solar_system_size, solar_system_size)
			new_x = math.pow(x,2)
			radius = math.pow(solar_system_size,2)
			y = math.sqrt(radius-new_x)
			db.universe.insert({'x_pos' : round(x)+star_x, 'y_pos' : round(y)+star_y, 'object' : "star_circumference", 'parent_id' : parent_id})
			db.universe.insert({'x_pos' : -round(x)+star_x, 'y_pos' : -round(y)+star_y, 'object' : "star_circumference", 'parent_id' : parent_id})
		for y in range(100):
			y = random.randint(-solar_system_size, solar_system_size)
			new_y = math.pow(y,2)
			radius = math.pow(solar_system_size,2)
			x = math.sqrt(radius-new_y)
			# print "planet circumference is ", round(x)+star_x
			db.universe.insert({'x_pos' : round(x)+star_x, 'y_pos' : round(y)+star_y, 'object' : "star_circumference", 'parent_id' : parent_id})
			db.universe.insert({'x_pos' : -round(x)+star_x, 'y_pos' : -round(y)+star_y, 'object' : "star_circumference", 'parent_id' : parent_id})
		for distance in ((58, "Hades"), (108,"Athena"), (149,"Apollo"), (228,"Ares"), (779,"Dionysus"), (1430,"Poseidon"), (2880,"Hermes"), (4500,"Hestia"), (5900,"Hera")):
			r = distance[0]
			print " %s is %d away from the sun" %(distance[1],r)
			x = star_x
			y = r+star_y
			for h in range(100):
				r = distance[0]
				h = random.randint(-r, r)
				new_h = math.pow(h,2)
				radius = math.pow(r,2)
				i = math.sqrt(radius-new_h)
				db.universe.insert({'x_pos' : round(h)+star_x, 'y_pos' : round(i)+star_y, 'object' : "planet_circumference", 'parent_id' : parent_id})
				db.universe.insert({'x_pos' : -round(h)+star_x, 'y_pos' : -round(i)+star_y, 'object' : "planet_circumference", 'parent_id' : parent_id})
			for i in range(100):
				r = distance[0]
				i = random.randint(-r, r)
				new_i = math.pow(i,2)
				radius = math.pow(r,2)
				h = math.sqrt(radius-new_i)
				db.universe.insert({'x_pos' : round(h)+star_x, 'y_pos' : round(i)+star_y, 'object' : "planet_circumference", 'parent_id' : parent_id})
				db.universe.insert({'x_pos' : -round(h)+star_x, 'y_pos' : -round(i)+star_y, 'object' : "planet_circumference", 'parent_id' : parent_id})
			if distance[1] == "Hades":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 4878
				volum = 1.33*math.pi*math.pow(planet_diameter/2,3)
				planet_type = "mineral"
				iron = planet_diameter*random.randint(10,100)
				carbon = planet_diameter*random.randint(5,50)
				oxygen = planet_diameter*random.randint(0,0)
				h2o = planet_diameter*random.randint(0,1)
				deuterium = planet_diameter*random.randint(0,5)
				helium_3 = planet_diameter*random.randint(0,2)
				# print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' : planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
			elif distance[1] == "Athena":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 12100
				planet_type = "mineral"
				iron = planet_diameter*random.randint(10,100)
				carbon = planet_diameter*random.randint(5,50)
				oxygen = planet_diameter*random.randint(0,0)
				h2o = planet_diameter*random.randint(0,1)
				deuterium = planet_diameter*random.randint(0,5)
				helium_3 = planet_diameter*random.randint(0,2)
				# print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
			elif distance[1] == "Apollo":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 12742
				planet_type = "organic"
				iron = planet_diameter*random.randint(10,100)
				carbon = planet_diameter*random.randint(5,50)
				oxygen = planet_diameter*random.randint(40,100)
				h2o = planet_diameter*random.randint(30,100)
				deuterium = planet_diameter*random.randint(0,5)
				helium_3 = planet_diameter*random.randint(0,2)
				# print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
			elif distance[1] == "Ares":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 6794
				planet_type = "mineral"
				iron = planet_diameter*random.randint(10,100)
				carbon = planet_diameter*random.randint(5,50)
				oxygen = planet_diameter*random.randint(0,0)
				h2o = planet_diameter*random.randint(0,1)
				deuterium = planet_diameter*random.randint(0,5)
				helium_3 = planet_diameter*random.randint(0,2)
				# print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
			elif distance[1] == "Dionysus":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 142981
				planet_type = "gas"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(1,10)
				oxygen = planet_diameter*random.randint(0,5)
				h2o = planet_diameter*random.randint(0,10)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,5)
				# print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
			elif distance[1] == "Poseidon":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 120536
				planet_type = "gas"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(1,10)
				oxygen = planet_diameter*random.randint(0,5)
				h2o = planet_diameter*random.randint(0,10)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,5)
				# print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
			elif distance[1] == "Hermes":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 51118
				planet_type = "gas"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(1,10)
				oxygen = planet_diameter*random.randint(0,5)
				h2o = planet_diameter*random.randint(0,10)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,5)
				# print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3

				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
			elif distance[1] == "Hestia":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 49500
				planet_type = "gas"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(1,10)
				oxygen = planet_diameter*random.randint(0,5)
				h2o = planet_diameter*random.randint(0,10)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,5)
				# print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3
				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
			elif distance[1] == "Hera":
				name = distance[1]
				distance = distance[0]
				planet_diameter = 2360
				planet_type = "ice"
				iron = planet_diameter*random.randint(0,0)
				carbon = planet_diameter*random.randint(0,0)
				oxygen = planet_diameter*random.randint(0,20)
				h2o = planet_diameter*random.randint(0,30)
				deuterium = planet_diameter*random.randint(0,0)
				helium_3 = planet_diameter*random.randint(0,0)
				# print name, x, y,distance, planet_diameter, planet_type, iron, carbon, oxygen, h2o, deuterium, helium_3

				db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' :y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
		# break
	else:
		print "Zeus already exists."
zeus()


# Full galaxy values
# x_min = -5259485
# y_min = -5259485
# x_max = 5259485
# y_max = 5259485
# margin = 5000

# Single quadrant values
x_min = -30000
y_min = -30000
x_max = 30000
y_max = 30000



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))


def solar_system():
	for d in range(500):
		print "d is ", d
		# Define a random x and y value that is between the min and max and includes a 3700 sector distance from the edge of the map so the star isn't on the edge.
		star_x = random.randint(x_min,x_max)
		star_y = random.randint(y_min,y_max)
		# Randomly choose on solar system size
		decide = random.choice(main_sizes)
		# Sets the randomly chosen star size and type.
		star_size = size[decide]
		star_type = type[decide]
		# multiplies the star size to the initial vales to create the solar system sizes
		# Solar systems around anywhere from 900 sectors to 19200 depending on the size of the star.
		solar_system_size = random.randint(900,4250)
		# Check to see if the position chosen has any solar systems nearby that it would collide with.
		position = db.universe.find_one({"x_pos": {"$gte": star_x-solar_system_size , "$lte": star_x+solar_system_size},"y_pos": {"$gte": star_y-solar_system_size, "$lte": star_y+solar_system_size}})
		
		# If it doesn't then create the star. We will create the planets later.
		if position == None:
			# print "star size is ",star_size
			# print "Solar system size is ",solar_system_size
			# print "system is located at", x,y
			
			# 
			# Create random name for the star.
			name = id_generator()
			# Insert the star into the database with its information
			db.universe.insert({'name' : name, 'object' : "star" , 'x_pos' : star_x, 'y_pos' : star_y, 'size' : solar_system_size, 'type' : star_type, 'star_size' : star_size})
			# Query the database for the start we just created. We need this to create the planets around it.
			id = db.universe.find_one({'name' : name})
			# Pull the ObjectId from the star to assign to the planets so we can query the star and find the planets.
			parent_id =  "object_id("+ id['_id'].__str__()+ ")"
			for a in range(100):
				cir_x = random.randint(-solar_system_size, solar_system_size)
				new_x = math.pow(cir_x,2)
				radius = math.pow(solar_system_size,2)
				cir_y = math.sqrt(radius-new_x)
				# print "x_pos is %d, y_pos is %d" %(round(cir_x)+x,round(cir_y)+y)
				db.universe.insert({'x_pos' : round(cir_x)+star_x, 'y_pos' : round(cir_y)+star_y, 'object' : "star_circumference", 'parent_id' : parent_id})
				db.universe.insert({'x_pos' : -round(cir_x)+star_x, 'y_pos' : -round(cir_y)+star_y, 'object' : "star_circumference", 'parent_id' : parent_id})
			for b in range(100):
				cir_y = random.randint(-solar_system_size, solar_system_size)
				new_y = math.pow(cir_y,2)
				radius = math.pow(solar_system_size,2)
				cir_x = math.sqrt(radius-new_y)
				# print "x_pos is %d, y_pos is %d" %(round(cir_x)+x,round(cir_y)+y)
				db.universe.insert({'x_pos' : round(cir_x)+star_x, 'y_pos' : round(cir_y)+star_y, 'object' : "star_circumference", 'parent_id' : parent_id})
				db.universe.insert({'x_pos' : -round(cir_x)+star_x, 'y_pos' : -round(cir_y)+star_y, 'object' : "star_circumference", 'parent_id' : parent_id})

			# new function for creating planets. Built inside the main one to pass the varbiles forward.
			def system():
				# First planet is at least 70 sectors away from the star. Otherwise it would be crispy fried. :-) Of course this says 50, but that is because the random number that gets added later starts at a minimum of 100.
				a = {}
				planet = 50+star_size
				k = 0
				i = random.randint(1,4)*solar_system_size/10
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
						# print "distance is ",distance
						x = star_x
						random_x = random.randint(-distance,distance)
						new_x = math.pow(random_x,2)
						radius = math.pow(distance,2)
						random_y = math.sqrt(radius-new_x)
						y = distance+star_y
						# print " planet is located at", random_x,random_y
						for h in range(100):
							h = random.randint(-distance, distance)
							new_h = math.pow(h,2)
							radius = math.pow(distance,2)
							i = math.sqrt(radius-new_h)
							db.universe.insert({'x_pos' : round(h)+star_x, 'y_pos' : round(i)+star_y, 'object' : "planet_circumference", 'parent_id' : parent_id})
							db.universe.insert({'x_pos' : -round(h)+star_x, 'y_pos' : -round(i)+star_y, 'object' : "planet_circumference", 'parent_id' : parent_id})
						for i in range(100):
							i = random.randint(-distance, distance)
							new_i = math.pow(i,2)
							radius = math.pow(distance,2)
							h = math.sqrt(radius-new_i)
							db.universe.insert({'x_pos' : round(h)+star_x, 'y_pos' : round(i)+star_y, 'object' : "planet_circumference", 'parent_id' : parent_id})
							db.universe.insert({'x_pos' : -round(h)+star_x, 'y_pos' : -round(i)+star_y, 'object' : "planet_circumference", 'parent_id' : parent_id})
						# x = random_x
						# y = round(random_y)
						if distance <= star_size*10:
							possible_planet_type = ('mineral' , 'gas')
							planet_type = random.choice(possible_planet_type)
							if planet_type =="mineral":
								planet_diameter = random.randint(4000,12000)
								iron = planet_diameter*random.randint(10,100)	
								carbon = planet_diameter*random.randint(5,50)
								oxygen = planet_diameter*random.randint(0,0)
								h2o = planet_diameter*random.randint(0,1)
								deuterium = planet_diameter*random.randint(0,5)
								helium_3 = planet_diameter*random.randint(0,2)
								#  print planet_type, x, y,  planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3								
								name = a[distance]
								db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' : y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
							
							elif planet_type =="gas":
								planet_diameter = random.randint(20000,90000)
								iron = planet_diameter*random.randint(10,20)
								carbon = planet_diameter*random.randint(5,10)
								oxygen = planet_diameter*random.randint(40,100)
								h2o = planet_diameter*random.randint(30,100)
								deuterium = planet_diameter*random.randint(0,0)
								helium_3 = planet_diameter*random.randint(0,2)
								#  print planet_type, x, y,  planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
								name = a[distance]
								db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' : y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
							
						elif distance <= 20*star_size and distance >= 11*star_size:
							possible_planet_type = ('organic', 'terraform')
							planet_type = random.choice(possible_planet_type)
							if planet_type =="organic":
								planet_diameter = random.randint(8000,14000)
								iron = planet_diameter*random.randint(10,20)
								carbon = planet_diameter*random.randint(5,10)
								oxygen = planet_diameter*random.randint(40,100)
								h2o = planet_diameter*random.randint(30,100)
								deuterium = planet_diameter*random.randint(0,3)
								helium_3 = planet_diameter*random.randint(0,2)
								#  print planet_type, x, y,  planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
								name = a[distance]
								db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' : y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
	
							elif planet_type =="terraform":
								planet_diameter = random.randint(8000,14000)
								iron = planet_diameter*random.randint(10,20)
								carbon = planet_diameter*random.randint(5,10)
								oxygen = planet_diameter*random.randint(40,100)
								h2o = planet_diameter*random.randint(30,100)
								deuterium = planet_diameter*random.randint(0,3)
								helium_3 = planet_diameter*random.randint(0,2)
								#  print planet_type, x, y,  planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
								name = a[distance]
								db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' : y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
							
							
						elif distance <= 30*star_size and distance >=  21*star_size:
							possible_planet_type = ('mineral' , 'gas', 'ice')
							planet_type = random.choice(possible_planet_type)
							if planet_type =="mineral":
								planet_diameter = random.randint(4000,12000)
								iron = planet_diameter*random.randint(10,100)	
								carbon = planet_diameter*random.randint(5,50)
								oxygen = planet_diameter*random.randint(0,0)
								h2o = planet_diameter*random.randint(0,1)
								deuterium = planet_diameter*random.randint(0,5)
								helium_3 = planet_diameter*random.randint(0,2)
								#  print planet_type, x, y,  planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
								name = a[distance]
								db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' : y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
							
							elif planet_type =="gas":
								planet_diameter = random.randint(20000,90000)
								iron = planet_diameter*random.randint(10,20)
								carbon = planet_diameter*random.randint(5,10)
								oxygen = planet_diameter*random.randint(40,100)
								h2o = planet_diameter*random.randint(30,100)
								deuterium = planet_diameter*random.randint(0,0)
								helium_3 = planet_diameter*random.randint(0,2)
								#  print planet_type, x, y,  planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
								name = a[distance]
								db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' : y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
							
							elif planet_type =="ice":
								planet_diameter = random.randint(500,6000)
								iron = planet_diameter*random.randint(10,20)
								carbon = planet_diameter*random.randint(5,10)
								oxygen = planet_diameter*random.randint(40,100)
								h2o = planet_diameter*random.randint(30,100)
								deuterium = planet_diameter*random.randint(0,1)
								helium_3 = planet_diameter*random.randint(0,1)
								#  print planet_type, x, y,  planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
								name = a[distance]
								db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' : y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
							
						elif distance >=  31*star_size:
							possible_planet_type = ('gas', 'ice')
							planet_type = random.choice(possible_planet_type)
							if planet_type =="gas":
								planet_diameter = random.randint(20000,90000)
								iron = planet_diameter*random.randint(10,20)
								carbon = planet_diameter*random.randint(5,10)
								oxygen = planet_diameter*random.randint(40,100)
								h2o = planet_diameter*random.randint(30,100)
								deuterium = planet_diameter*random.randint(0,0)
								helium_3 = planet_diameter*random.randint(0,2)
								#  print planet_type, x, y,  planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
								
								name = a[distance]
								db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' : y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
							elif planet_type =="ice":
								planet_diameter = random.randint(500,6000)
								iron = planet_diameter*random.randint(10,20)
								carbon = planet_diameter*random.randint(5,10)
								oxygen = planet_diameter*random.randint(40,100)
								h2o = planet_diameter*random.randint(30,100)
								deuterium = planet_diameter*random.randint(0,1)
								helium_3 = planet_diameter*random.randint(0,1)
								#  print planet_type, x, y,  planet_diameter, iron, carbon, oxygen, h2o, deuterium, helium_3
								
								name = a[distance]
								db.universe.insert({'name' : name, 'x_pos' : x, 'y_pos' : y, 'diameter' : planet_diameter, 'size' : 1,  'object' : "planet", 'parent_id' : parent_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'helium_3' : helium_3, 'distance_from_star' : distance, 'type' :planet_type, 'create_time' : now.strftime("%Y%m%d%H%M%S"), 'orbit' : []})
									
							
				planets()

			system()
		else:
			print "found a solar system at %d,%d" %(position['x_pos'],position['y_pos'])

# solar_system()


