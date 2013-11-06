import pymongo
import datetime
import time
import random


db = pymongo.Connection('localhost', 27017).game

now = datetime.datetime.now()  # Gets the current time.
day_of_year = datetime.datetime.now().timetuple().tm_yday
# convert the time to an integer we can use for checking how much time has passed.
days = (now.year * 365) + day_of_year + (now.year/4)
hours = days * 24 + now.hour
minutes = hours *60 + now.minute
seconds = minutes * 60 + now.second

u_id = db.users.find_one({'username' : "test"})['_id']

ship = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
engine = db.player_items.find_one({'u_id' : u_id, 'object' : "Engine", 'p_id': ship['_id']})

print engine

print "The engine has been operational for the following seconds %r" %((engine['life']+engine['created'])-seconds)

value =  float((engine['life']+engine['created'])-seconds)/float(engine['life'])*100

if value > 75:
	print "Green"
	print round(value)
elif value > 50 and value < 75:
	print "Yellow"
	print value
elif value > 25 and value < 50:
	print "Orange"
	print value
else:
	print "Red"
	print value


# warp_health = seconds - (warp['created'] + warp['life'])
# print warp_health





# percentage = float(warp_health) / float(warp['life'])
# print warp['created']
# print warp['life']
# print seconds
# print warp_health
# print "The total life of the warp drive is %r" %warp['life']
# print "But I want to know the left over amount of health my warp drive has."
# print
# print "So, lets look at doing some math about it."

# print percentage*100










































# uname = "Xariec"

# u_id = db.users.find_one({'username' : uname})['_id']
# p_id = db.player_items.find_one({'u_id' : u_id, 'type' : "Battleship"})['_id']

# engine = db.player_items.find_one({'u_id' : u_id, 'object' : "Engine"})

# battleship = db.player_items.find({'p_id' : p_id})

# name = []
# count = 0
# for x in battleship:
	# count += 1
	# name.append(x['name'])

# print p_id
# print name
# print 
# print count


# print now
# print seconds









# effiency = {1 : .4, 2 : .5, 3 : .65, 4 : .7, 5 : .85, 6 : .95}

# lvl = 1

# print effiency[lvl]











# def names():
	# title = {'1': "Nurse", '2' : "Registered Nurse", '3' : "Doctor", '4' : "Surgeon", '5' : "Cheif Surgeon"}
	#female_names = [' Sophia' , ' Emma' , ' Olivia' , ' Isabella' , ' Ava' , ' Lily' , ' Zoe' , ' Chloe' , ' Mia' , ' Madison' , ' Emily' , ' Ella' , ' Madelyn' , ' Abigail' , ' Aubrey' , ' Addison' , 'Avery' , ' Layla' , ' Hailey' , ' Amelia' , ' Hannah' , ' Charlotte' , ' Kaitlyn' , ' Harper' , ' Kaylee' , ' Sophie' , ' Mackenzie' , ' Peyton' , ' Riley' , ' Grace' , ' Brooklyn' , 'Sarah' , ' Aaliyah' , ' Anna' , ' Arianna' , ' Ellie' , ' Natalie' , ' Isabelle' , ' Lillian' , ' Evelyn' , ' Elizabeth' , ' Lyla' , ' Lucy' , ' Claire' , ' Makayla' , ' Kylie' , ' Audrey',' Maya' , ' Leah' , ' Gabriella' , ' Annabelle' , ' Savannah' , ' Nora' , ' Reagan' , ' Scarlett' , ' Samantha' , ' Alyssa' , ' Allison' , ' Elena' , ' Stella' , ' Alexis' , ' Victoria' , ' Aria' , ' Molly' , ' Maria' , ' Bailey' , ' Sydney' , ' Bella' , ' Mila' , ' Taylor' , ' Kayla' , ' Eva' , ' Jasmine' , ' Gianna' , ' Alexandra' , ' Julia' , ' Eliana' , ' Kennedy' , ' Brianna' , ' Ruby' , ' Lauren' , ' Alice' , ' Violet' , ' Kendall' , ' Morgan' , ' Caroline' , ' Piper' , ' Brooke' , ' Elise' , ' Alexa' , ' Sienna' , ' Reese' , ' Clara' , 'Paige' , ' Kate' , ' Nevaeh' , ' Sadie' , ' Quinn' , ' Isla' , ' Eleanor']
	#male_names = ['Aiden' , ' Jackson' , ' Ethan' , ' Liam' , ' Mason' , ' Noah' , ' Lucas' , ' Jacob' , ' Jayden' , ' Jack' , ' Logan' , ' Ryan' , ' Caleb' , ' Benjamin' , ' William' , ' Michael' , 'Alexander' , ' Elijah' , ' Matthew' , ' Dylan' , ' James' , ' Owen' , ' Connor' , ' Brayden' , ' Carter' , ' Landon' , ' Joshua' , ' Luke' , ' Daniel' , ' Gabriel' , ' Nicholas' , ' Nathan' , ' Oliver' , ' Henry' , ' Andrew' , ' Gavin' , ' Cameron' , ' Eli' , ' Max' , ' Isaac' , ' Evan' , ' Samuel' , ' Grayson' , ' Tyler' , ' Zachary' , ' Wyatt' , ' Joseph' , ' Charlie' , 'Hunter' , ' David' , ' Anthony' , ' Christian' , ' Colton' , ' Thomas' , ' Dominic' , ' Austin' , ' John' , ' Sebastian' , ' Cooper' , ' Levi' , ' Parker' , ' Isaiah' , ' Chase' , ' Blake',' Aaron' , ' Alex' , ' Adam' , ' Tristan' , ' Julian' , ' Jonathan' , ' Christopher' , ' Jace' , ' Nolan' , ' Miles' , ' Jordan' , ' Carson' , ' Colin' , ' Ian' , ' Riley' , ' Xavier', ' Hudson' , ' Adrian' , ' Cole' , ' Brody' , ' Leo' , ' Jake' , ' Bentley' , ' Sean' , ' Jeremiah' , ' Asher' , ' Nathaniel' , ' Micah' , ' Jason' , ' Ryder' , ' Declan' , ' Hayden', ' Brandon' , ' Easton' , ' Lincoln' , ' Harrison']
	# gender = ['M', 'F']


	# gender = random.choice(gender)

	# if gender == "M":
		# name = random.choice(male_names)
	# else:
		# name = random.choice(female_names)
		
	# return gender, name

# object = "personnel"
# location = ['media_room', 'mess_hall', 'dorm']
# location = random.choice(location)
# health = 15
# indiscretion = 0.25 * random.uniform(1,3)
# skill = 0
# type = {'1': "Physician", '2' : "Engineer", '3' : "Scientist", '4' : "Mechanic", '5' : "Instructor", '6' : "Pilot"}


# if type == "Physician":
	# title = {'1': "Nurse", '2' : "Registered Nurse", '3' : "Doctor", '4' : "Surgeon", '5' : "Chief Surgeon"}
# else if type == "Engineer":
	# title = {'1': "Assistant Engineer", '2' : "Associate Engineer", '3' : "Engineer", '4' : "Senior Engineer", '5' : "Chief Engineer"}
# else if type == "Scientist":
	# title = {'1': "Lab Tech", '2' : "Lab Professor", '3' : "Scientist", '4' : "Senior Scientist", '5' : "Chief Scientist"}
# else if type == "Mechanic":
	# title = {'1': "Apprentice", '2' : "Journeyman", '3' : "Mechanic", '4' : "Senior Mechanic", '5' : "Chief Mechanic"}
# else:
	# title = {'1': "Nurse", '2' : "Registered Nurse", '3' : "Doctor", '4' : "Surgeon", '5' : "Chief Surgeon"}
	
# print 
# personell_id = db.player_items.insert({'name' : names()[1], 'object' : object, 'type' : type, 'title' : title['1'], 'gender' : names()[0], 'indiscretion' : indiscretion, 'health' : health, 'u_id' : u_id, 'p_id' : battle_ship, 'skill' : skill,'timestamp' : now, 'created' : seconds, 'location' : location})




# Time for some Time, managing time and what not.

# now = datetime.datetime.now()  # Gets the current time.
# day_of_year = datetime.datetime.now().timetuple().tm_yday

# days = (now.year * 365) + day_of_year + (now.year/4)
# hours = days * 24 + now.hour
# minutes = hours *60 + now.minute
# seconds = minutes * 60 + now.second

# test = db.player_items.find_one({'name' : "DD-FG-40"})
# time_created = test['created']*1.0
# life = test['life']*1.0
# seconds = seconds * 1.0

# print time_created
# print life
# print seconds






# now = datetime.datetime.now()

# print now
# print repr(now)
# print type(now)
# print now.year, now.month, now.day
# print now.hour, now.minute, now.second
# print now.microsecond
# day_of_year = datetime.datetime.now().timetuple().tm_yday
# print "Day of year", day_of_year

# # Ok, now I know how to seperate everything, lets do some math so it makes sense...
# days = (now.year * 365) + day_of_year + (now.year/4)
# hours = days * 24 + now.hour
# minutes = hours *60 + now.minute
# seconds = minutes * 60 + now.second




# print "Total seconds up till now is", seconds

# alternate = 63542677310


# test = seconds - alternate

# print test








# test = db.test.insert({'name' : "Brian"})

# print test





# Testing how the artillery compartments look and work.

# weapons = db.player_items.find_one({'name' : "Weapons Center"})
# compartments = db.player_items.find_one({'name' : "GCBS-371"}) # Find out how many there really should be.

# for a in range(compartments['cannon_slots']):
	# slot = weapons['cannon_slot_%d' %a]
	# if slot:
		# print "Somethings there"
	# else:
		# print "Didn't fight naught"






















# db.data.insert({'data' : "This is data"})

# db.data.update({'data' : "This is data"}, {'$set': {'data' : "This is how you change the data"}}, True)

# db.data.insert({'array' : "This is an array", 'cargo' : ['13245615','3567489131','81618916313','49813165165']})

# find = db.data.find()

# for a in find:
	# print a
	
	
# one = db.data.find_one()

# print "using finid One", one
	
