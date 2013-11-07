import pymongo
import math
import time
import datetime
import random


db = pymongo.Connection('localhost', 27017).game

now = datetime.datetime.now()  # Gets the current time.
day_of_year = datetime.datetime.now().timetuple().tm_yday
# convert the time to an integer we can use for checking how much time has passed.
days = (now.year * 365) + day_of_year + (now.year/4)
hours = days * 24 + now.hour
minutes = hours *60 + now.minute
seconds = minutes * 60 + now.second # Seconds, fairly accurate depiction of time since the year of 0001





star = db.universe.find({'item' : "star"}).limit(100)
print "Item Name X-POS Y-POS System-Size"
for a in star:
	print a['item'], a['name'], a['x_pos'], a['y_pos'], a['system_size']
	planet = db.universe.find({'p_id' : a['_id']})
	for b in planet:
		print b['item'], b['name'], b['x_pos'], b['y_pos']
		

		





# print attacker_id
# count = 0
# for a in a_ship_id:
	# count +=1
	# print a_name[a], a_lvl[a], a_health[a], a_cannon[a], a_missile[a]
# print count


# count = 0
# for b in d_ship_id:
	# count +=1
	# print d_name[b], d_lvl[b], d_health[b], d_cannon[b], d_missile[b]
# print count






















# p = 2*math.pi


# u_id = db.users.find_one({'username' : "test"})['_id']

# p_id= db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})

# # lvl = 100000000000


# planets = db.universe.find({"x_pos": {"$gte": int(p_id['x']) - lvl , "$lte": int(p_id['x']) + lvl},"y_pos": {"$gte": int(p_id['y']) - lvl, "$lte": int(p_id['y']) + lvl}}) # position is passed from the command class of app.py.

# planets = db.universe.find({'item' : "planet"})

# count = 0

# for a in planets:
	# t = seconds - a['created'] #subtract current seconds from seconds of the moment it was created
	# op = a['op'] # orbital period
	# r = a['distance'] * 1000 # distance is saved in km, we need meters for this calulation.
	# # Note, add in accordance to the star, as that is the center in this case.
	# star = db.universe.find_one({'_id' : a['p_id']})
	# new_x = round(r*math.sin(math.fmod(t,op)/op*p))/1000
	# new_y = round(r*math.cos(math.fmod(t,op)/op*p))/1000
	# new_x = new_x + star['x_pos']
	# new_y = new_y + star['y_pos']
	# db.universe.update({'_id' : a['_id']}, {"$set": {'x_pos' : int(new_x), 'y_pos' : int(new_y)}})
	# count +=1
	



# print count




# 795,432,085,189

# alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# numeric = ['0','1','2','3','4','5','6','7','8','9']


# x_min = -795500000000
# x_max = 795500000000
# y_min = -795500000000
# y_max = 795500000000

# incrament = 1500000000

# first = 0
# second = 0
# third = 0
# fourth = 0

# count = 0
# print x_min
# print x_min + incrament

# def sector_creation():
	# first = 0
	# second = 0
	# third = 0
	# fourth = 0
	# x_min = -795500000000
	# x_max = 795500000000
	# y_min = -795500000000
	# y_max = 795500000000
	# while x_min <= x_max:
		# v = 0
		# for a in range(26):	
			# n = 0
			# for b in range(99):
				# digits = 2
				# ns = str(n).zfill(digits)
				# sector = alpha[v]+ns
				# n +=1
				# x_min += incrament
				# print sector
			# v +=1
		
		# print "X :",x_min
		
	# print x_min
# sector_creation()

# print x_max


# while i < 26:

	
# first += 1	





		# if y_min < y_max:
			# sector = sector+numeric[start]
			# y_range = db.universe.find({"y_pos" : {"$gte": y_min, "$lte" : y_min+incrament}})
			# y_min 
	















# x_min = db.universe.find().sort("x_pos" , 1).limit(1)
# for a in x_min:
	# x_min = a['x_pos']
	
# x_max = db.universe.find().sort("x_pos" , -1).limit(1)
# for a in x_max:
	# x_max = a['x_pos']
	
# y_max = db.universe.find().sort("y_pos" , -1).limit(1)
# for a in y_max:
	# y_max = a['y_pos']

# y_min = db.universe.find().sort("y_pos" , 1).limit(1)
# for a in y_min:
	# y_min = a['y_pos']
	
# print x_min
# print x_max
# print y_min
# print y_max

	
	
	
	# x_max = db.universe.find().sort({'x_pos' : 1}).limit(1)['x_pos']
# y_min = db.universe.find().sort({'y_pos' : -1}).limit(1)['y_pos']
# y_max = db.universe.find().sort({'y_pos' : 1}).limit(1)['y_pos']













# track = 0
# e = math.e
# a = 5000
# static_b = .4 #Controls the spiral 
# deg = 0

# numtails = 5 # number of tails originating from the same point.
# offset = 360/numtails

# for o in range(numtails):

	# for s in range(5):
		# b = static_b + (0.05*s)  #controls the angle of the spiral arms, 

		# deg = 0
		# while deg < 720:
			
			# r = a*math.pow(e,b*math.radians(deg))
			# x = r*math.cos(math.radians(deg-(o*offset)))*-1
			# y = r*math.sin(math.radians(deg-(o*offset)))*-1
			# deg +=14.4
			# print int(x),int(y)


			
			# track +=1
			
			
		# while deg > 720:
			
			# r = a*math.pow(e,b*math.radians(deg))
			# x = r*math.cos(math.radians(deg-(o*offset)))
			# y = r*math.sin(math.radians(deg-(o*offset)))
			# deg -=14.4
			# print int(x),int(y)

		#The following is a control structure to keep the probability of specific types of stars accurate.

			
			# track +=1
		




































# db = pymongo.Connection('localhost', 27017).game








# su = 1.989 * math.pow(10, 30) # Solar Unit
# sr = 6.955 * math.pow(10,8) #Solar Radii In meters
# au = 149597871



# star_classes = ('O', 'B', 'A', 'F', 'G', 'K', 'M')

# star_color = {'O' : "Blue", 'B' : "Blue White", 'A' : "White", 'F' : "Yellow White", 'G' : "Yello", 'K' : "Orange", 'M' : "Red"}

# star_solar_mass = {'O' : "16,150", 'B' : "2.1,16", 'A' : "1.4,2.1", 'F' : "1.04,1.4", 'G' : "0.8,1.4", 'K' : ".45,.8", 'M' : ".075,.45"}

# star_solar_radii = {'O' : "6.6,20", 'B' : "1.8,6.6", 'A' : "1.4,1.8", 'F' : "1.15,1.4", 'G' : ".96,1.15", 'K' : ".7,.96", 'M' : ".05,.7"}

	
# star_solar_luminosity = {'O' : "30000,500000", 'B' : "25,30000", 'A' : "5,25", 'F' : "1..5,5", 'G' : ".6,1.5", 'K' : ".08,.6", 'M' : ".0001,.08"}


	

	

# for d in range(50):
	# choose_star = random.randrange(1,100)
	# if choose_star <= 75:
		# star_class = star_classes[6]
		# color = star_color[star_class]
		# solar_mass = star_solar_mass[star_class].split(',')
		# star_mass = random.uniform(float(solar_mass[0]),float(solar_mass[1]))*su
		# solar_radii = star_solar_radii[star_class].split(',')
		# star_radii = random.uniform(float(solar_radii[0]),float(solar_radii[1]))*sr
		# solar_luminosity = star_solar_luminosity[star_class].split(',')
		# star_luminosity = random.uniform(float(solar_luminosity[0]),float(solar_luminosity[1]))
		# star_habbital_zone_min = au*star_luminosity*.75
		# star_habbital_zone_max = au*star_luminosity*1.25

		
		
		# print star_mass
		# print star_radii
		# print star_luminosity
		# print
		# print star_habbital_zone_min
		# print star_habbital_zone_max
		# print






# for x in range(20):
	# a = random.uniform(.25,10)
	# print round(a,2)




















# now = datetime.datetime.now()  # Gets the current time.
# day_of_year = datetime.datetime.now().timetuple().tm_yday
# # convert the time to an integer we can use for checking how much time has passed.
# days = (now.year * 365) + day_of_year + (now.year/4)
# hours = days * 24 + now.hour
# minutes = hours *60 + now.minute
# seconds = minutes * 60 + now.second



# # Let's try to figure out gravity.


# M = 1.989 * math.pow(10, 30) #mass in KG of the sun

# g = 6.674 * math.pow(10,-11) # Gravitational constant

# r = 149600000 * 1000  # Multiplied by 1000 to convert from km to meters


# v = math.sqrt((g*M)/r)  # Velocity is the square-root of the gravitational constant * Mass of large body / radius of orbit.

# print "Current Velocity for Earth is", round(v/1000,1), "km per second"



	
# # and now for the orbital period

# T = 2*math.pi*math.sqrt(math.pow(r,3)/(g*M))

# print "Orbital period in seconds: ", T

# print "Current time is : ", seconds

# print "The planet has completed ", seconds/T, " orbits around the sun"













# planet = db.universe.find_one({'item' : "planet"})

# print planet['created']

# now = datetime.datetime.now()  # Gets the current time.
# day_of_year = datetime.datetime.now().timetuple().tm_yday
# # convert the time to an integer we can use for checking how much time has passed.
# days = (now.year * 365) + day_of_year + (now.year/4)
# hours = days * 24 + now.hour
# minutes = hours *60 + now.minute
# seconds = minutes * 60 + now.second

# t = ((seconds) - planet['created'])



# r = 580

# v = 986

# op = r*v

# p = 2*math.pi


# # now = round(radius*math.sin(t%orbital_period/orbital_period)*p)

# # now = datetime.now().time()
# x_pos = 2630322
# y_pos = 2629742




# for d in range(500):
	# t +=50
	# x = round(r*math.sin(math.fmod(t,op)/op*p))+x_pos
	# y = round(r*math.cos(math.fmod(t,op)/op*p))+y_pos
	# print t
	# print v
	# print x,y
	# print
	# time.sleep(.5)

	
	