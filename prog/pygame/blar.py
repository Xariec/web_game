import pymongo
import math




db = pymongo.Connection('localhost', 27017).game




# all = db.universe.find().sort("x_pos" , -1).limit(500)
x = y = 0
lvl = 100000000
view = 500*lvl
all = db.universe.find({"x_pos": {"$gte": x - view , "$lte": x + view},"y_pos": {"$gte": y - view, "$lte": y + view}})



for a in all:
	x = a['x_pos']/lvl
	y = a['y_pos']/lvl

	print x+500, y+500
	



















































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
			
			
		# # while deg > 720:
			
			# # r = a*math.pow(e,b*math.radians(deg))
			# # x = r*math.cos(math.radians(deg-(o*offset)))
			# # y = r*math.sin(math.radians(deg-(o*offset)))
			# # deg -=14.4
			# # print int(x),int(y)

		# #The following is a control structure to keep the probability of specific types of stars accurate.

			
			# track +=1
		







































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

	
	