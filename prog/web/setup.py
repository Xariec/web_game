import pymongo
import random
import datetime
import math
import time

# Some rules to use... Everything has an Object, class, type, but we will call them Item type and name. Now for every item, there will be different things for each. but the key here is that every item I call from the database will have these three values. That will make it easier for me to keep track and safely call anything I want without having to wonder what key I used for the value.

# Item - Object
# Type - Type of object
# Title	- Specialization of object
# Name	- Name of object



# Common Names
	# u_id = user ID
		# - used to track what the user owns. all items has a user id, this gets updated if item changes hands
	
	# p_id = parent ID 
		# - used to track what the item is dependent on. So an power core has the p_id of the ship its in. Used during fights to figure out what to dmg
		
	# a_id = Attached to ID
		# - used to track what item is attached to specific key.
	



db = pymongo.Connection('localhost', 27017).game

# Global values/variables
now = datetime.datetime.now()  # Gets the current time.
day_of_year = datetime.datetime.now().timetuple().tm_yday
# convert the time to an integer we can use for checking how much time has passed.
days = (now.year * 365) + day_of_year + (now.year/4)
hours = days * 24 + now.hour
minutes = hours *60 + now.minute
seconds = minutes * 60 + now.second


def names():
	female_names = [' Sophia' , ' Emma' , ' Olivia' , ' Isabella' , ' Ava' , ' Lily' , ' Zoe' , ' Chloe' , ' Mia' , ' Madison' , ' Emily' , ' Ella' , ' Madelyn' , ' Abigail' , ' Aubrey' , ' Addison' , 'Avery' , ' Layla' , ' Hailey' , ' Amelia' , ' Hannah' , ' Charlotte' , ' Kaitlyn' , ' Harper' , ' Kaylee' , ' Sophie' , ' Mackenzie' , ' Peyton' , ' Riley' , ' Grace' , ' Brooklyn' , 'Sarah' , ' Aaliyah' , ' Anna' , ' Arianna' , ' Ellie' , ' Natalie' , ' Isabelle' , ' Lillian' , ' Evelyn' , ' Elizabeth' , ' Lyla' , ' Lucy' , ' Claire' , ' Makayla' , ' Kylie' , ' Audrey',' Maya' , ' Leah' , ' Gabriella' , ' Annabelle' , ' Savannah' , ' Nora' , ' Reagan' , ' Scarlett' , ' Samantha' , ' Alyssa' , ' Allison' , ' Elena' , ' Stella' , ' Alexis' , ' Victoria' , ' Aria' , ' Molly' , ' Maria' , ' Bailey' , ' Sydney' , ' Bella' , ' Mila' , ' Taylor' , ' Kayla' , ' Eva' , ' Jasmine' , ' Gianna' , ' Alexandra' , ' Julia' , ' Eliana' , ' Kennedy' , ' Brianna' , ' Ruby' , ' Lauren' , ' Alice' , ' Violet' , ' Kendall' , ' Morgan' , ' Caroline' , ' Piper' , ' Brooke' , ' Elise' , ' Alexa' , ' Sienna' , ' Reese' , ' Clara' , 'Paige' , ' Kate' , ' Nevaeh' , ' Sadie' , ' Quinn' , ' Isla' , ' Eleanor']
	male_names = ['Aiden' , ' Jackson' , ' Ethan' , ' Liam' , ' Mason' , ' Noah' , ' Lucas' , ' Jacob' , ' Jayden' , ' Jack' , ' Logan' , ' Ryan' , ' Caleb' , ' Benjamin' , ' William' , ' Michael' , 'Alexander' , ' Elijah' , ' Matthew' , ' Dylan' , ' James' , ' Owen' , ' Connor' , ' Brayden' , ' Carter' , ' Landon' , ' Joshua' , ' Luke' , ' Daniel' , ' Gabriel' , ' Nicholas' , ' Nathan' , ' Oliver' , ' Henry' , ' Andrew' , ' Gavin' , ' Cameron' , ' Eli' , ' Max' , ' Isaac' , ' Evan' , ' Samuel' , ' Grayson' , ' Tyler' , ' Zachary' , ' Wyatt' , ' Joseph' , ' Charlie' , 'Hunter' , ' David' , ' Anthony' , ' Christian' , ' Colton' , ' Thomas' , ' Dominic' , ' Austin' , ' John' , ' Sebastian' , ' Cooper' , ' Levi' , ' Parker' , ' Isaiah' , ' Chase' , ' Blake',' Aaron' , ' Alex' , ' Adam' , ' Tristan' , ' Julian' , ' Jonathan' , ' Christopher' , ' Jace' , ' Nolan' , ' Miles' , ' Jordan' , ' Carson' , ' Colin' , ' Ian' , ' Riley' , ' Xavier', ' Hudson' , ' Adrian' , ' Cole' , ' Brody' , ' Leo' , ' Jake' , ' Bentley' , ' Sean' , ' Jeremiah' , ' Asher' , ' Nathaniel' , ' Micah' , ' Jason' , ' Ryder' , ' Declan' , ' Hayden', ' Brandon' , ' Easton' , ' Lincoln' , ' Harrison']
	gender = ['M', 'F']
	gender = random.choice(gender)
	if gender == "M":
		name = random.choice(male_names)
	else:
		name = random.choice(female_names)		

	return gender, name

	
def personnel(u_id, p_id, type, lvl, location): # This will hold the rules for all personnel assigned to the ship. If they are not assigned, they have three locations they can be in, the Media Room, the Mess Hall, and Dorms. Pilots have an extra called the Pilots lounge. (This will have a purpose later)
	item = "personnel"
	# type = ""
	health = 15
	indiscretion = 0.25 * random.uniform(1,3)
	luck = random.uniform(.125, .75)
	skill = 0
	assigned = 0
	age = random.randint(20, 60)
	# personnel = {1: "Physician", 2 : "Engineer", 3 : "Scientist", 4 : "Mechanic", 5 : "Instructor", '6' : "Pilot"}
	# This will be a way to import a personnel and use this later for adding more as needed, but needs more work and the rest of the other parts need to come together before I know how I'm going to call the right information.
	# The type of personnel will be included when calling this function, the following uses the lvl associated with type to determine what their title is.
	if type == "Physician":
		title = {1: "Nurse", 2 : "Registered Nurse", 3 : "Doctor", 4 : "Surgeon", 5 : "Chief Surgeon"}
	
	elif type == "Engineer":
		title = {1: "Assistant Engineer", 2 : "Associate Engineer", 3 : "Engineer", 4 : "Senior Engineer", 5 : "Chief Engineer"}
	elif type == "Scientist":
		title = {1: "Lab Tech", 2 : "Lab Professor", 3 : "Scientist", 4 : "Senior Scientist", 5 : "Chief Scientist"}
	elif type == "Instructor":
		title = {1: "Instructor", 2 : "Lecturer", 3 : "Teacher", 4 : "Senior Teacher", 5 : "Professor"}
	elif type == "Mechanic":
		title = {1: "Apprentice", 2 : "Journeyman", 3 : "Mechanic", 4 : "Senior Mechanic", 5 : "Chief Mechanic"}
	else:
		title = {1: "First Lieutenant", 2 : "Second Lieutenant", 3 : "Captain", 4 : "Major", 5 : "Lieutenant Colonel"}
	if location == "None":
		location = ['media_room', 'mess_hall', 'dorm']
		location = random.choice(location)
	else:
		location = location
	personnel_id = db.player_items.insert({'name' : names()[1], 'item' : item, 'type' : type, 'title' : title[lvl], 'gender' : names()[0], 'indiscretion' : indiscretion, 'health' : health, 'u_id' : u_id, 'p_id' : p_id, 'skill' : skill,'timestamp' : now, 'created' : seconds, 'location' : location, 'luck' : luck, 'assigned' : assigned, 'age' : age})
	if type == "Pilot":
		assign_pilots = db.player_items.update({'u_id' : u_id, 'pilot' : "Unassigned", 'type' : "Fighter"}, {"$set" : { 'pilot' : personnel_id}})
	
def compartments(u_id, p_id):
	names = {1: "Engine Room" , 2 : "Mechanics Bay", 3 : "Pilots Lounge", 4 : "Right Hanger", 5 : "Left Hanger", 6 : "Cargo Bay", 7 : "Communications Center", 8 : "Weapons Center", 9 : "Media Room", 10 : "Mess Hall", 11 : "Dorms", 12 : "Sick Bay", 13 : "Research Lab", 14 : "Engineering Room", 15 : "Tech Center"}
	
	compartments = {'Engine Room' : 3 , 'Mechanics Bay' : 15 , 'Pilots Lounge' : 60 ,'Right Hanger' : 25 , 'Left Hanger' : 25 , 'Cargo Bay' : 150 , 'Communications Center' : 5, 'Weapons Center' : 5 , 'Media Room' :  30 , 'Mess Hall' : 75 , 'Dorms' : 150 , 'Sick Bay' : 15 , 'Research Lab' :  15 , 'Engineering Room' :  15 , 'Tech Center' : 15 }
	
	min_support = {'Engine Room' : 1 , 'Mechanics Bay' : 1 , 'Pilots Lounge' : 0 ,'Right Hanger' : 2 , 'Left Hanger' : 2 , 'Cargo Bay' : 1 , 'Communications Center' : 1, 'Weapons Center' : 1 , 'Media Room' :  1 , 'Mess Hall' : 1 , 'Dorms' : 1 , 'Sick Bay' :  1, 'Research Lab' :  1 , 'Engineering Room' :  1 , 'Tech Center' : 1 }
	
	type = {'Engine Room' : "Engineer" , 'Mechanics Bay' : "Mechanic" , 'Pilots Lounge' : "Military" ,'Right Hanger' : "Mechanic" , 'Left Hanger' : "Mechanic" , 'Cargo Bay' : "Military" , 'Communications Center' : "Military", 'Weapons Center' : "Military" , 'Media Room' :  "Personnel" , 'Mess Hall' : "Personnel" , 'Dorms' : "Personnel" , 'Sick Bay' : "Physician" , 'Research Lab' :  "Scientist" , 'Engineering Room' :  "Engineer"	, 'Tech Center' : "Instructor" }
	
	primary_support = {'Engine Room' : "Engineer" , 'Mechanics Bay' : "Mechanic" , 'Pilots Lounge' : "Pilot" ,'Right Hanger' : "Mechanic" , 'Left Hanger' : "Mechanic" , 'Cargo Bay' : "Mechanic" , 'Communications Center' : "Engineer", 'Weapons Center' : "Engineer" , 'Media Room' :  "Engineer" , 'Mess Hall' : "Scientist" , 'Dorms' : "" , 'Sick Bay' : "Physician" , 'Research Lab' :  "Scientist" , 'Engineering Room' :  "Engineer" , 'Tech Center' : "Instructor" }

	secondary_support = {'Engine Room' : "Mechanic" , 'Mechanics Bay' : "Scientist" , 'Pilots Lounge' : "" ,'Right Hanger' : "Engineer" , 'Left Hanger' : "Engineer" , 'Cargo Bay' : "Scientist" , 'Communications Center' : "Scientist", 'Weapons Center' : "Mechanic" , 'Media Room' :  "" , 'Mess Hall' : "" , 'Dorms' : "" , 'Sick Bay' : "Scientist" , 'Research Lab' :  "Physician" , 'Engineering Room' :  "Scientist" , 'Tech Center' : "" }
	

	item = "compartment"
	health = 10000
	for a in range(15):
		a = a+1
		name = names[a]
		compartment_id = db.player_items.insert({'name' : name, 'item' : item, 'type' : type[name], 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : now, 'created' : seconds, 'health' : health, 'primary_support' : primary_support[name], 'secondary_support' : secondary_support[name], 'compartments' : compartments[name] })
		db.player_items.update({'_id' : p_id},{"$set": {name : compartment_id}})
		min = min_support[name]
		for x in range(min):
			personnel(u_id, p_id, type[name], 1, name)
			
			
		

		
def reactor(u_id, p_id,lvl): # All details for all reactors. We need the User ID, the battle_ship ID, and the lvl of the item.
	name = {1: "DD-FG-40", 2 : "DD-FG-50", 3 : "DD-FG-65", 4 : "DD-FG-700", 5 : "DD-FG-850", 6 : "DD-FG-950"}
	item = "reactor"
	type = "fusion"
	primary_support = "Engineer"
	secondary_support = "Mechanic"
	effiency = {1 : .4, 2 : .5, 3 : .65, 4 : .7, 5 : .85, 6 : .95}
	max_deuterium = {1 : 450, 2 : 450, 3 : 600, 4 : 600, 5 : 750, 6 : 750}
	life = {1 : 48384000, 2 : 157248000, 3 : 4838400, 4 : 15724800, 5 : 4838400, 6 : 15724800}
	iron_cost = {1 : 10000, 2 : 20000, 3 : 25000, 4 : 40000, 5 : 80000, 6 : 120000}
	carbon_cost = {1 : 1000, 2 : 2500, 3 : 3000, 4 : 8000, 5 : 20000, 6 : 40000}
	build_time = {1 : 1800, 2 : 1800, 3 : 2400, 4 : 2400, 5 : 3600, 6 : 3600}
	health = 2500
	#That should be most of the variables 
	#Lets start some inserts :-)
	if p_id:
		reactor_id = db.player_items.insert({'name' : name[lvl], 'item' : item, 'type' : type, 'effiency' : effiency[lvl], 'max_deuterium' : max_deuterium[lvl], 'life' : life[lvl], 'iron_cost' : iron_cost[lvl], 'carbon_cost' : carbon_cost[lvl], 'build_time' : build_time[lvl], 'lvl' : lvl, 'health' : health, 'maxx' : health, 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : now, 'created' : seconds, 'primary_support' : primary_support, 'secondary_support' : secondary_support})
		db.player_items.update({'_id' : p_id},{"$set": {'reactor' : reactor_id}})
		personnel(u_id, p_id, primary_support, 1, "Engineering Room")
	else:
		reactor_id = db.player_items.insert({'name' : name[lvl], 'item' : item, 'type' : type, 'effiency' : effiency[lvl], 'max_deuterium' : max_deuterium[lvl], 'life' : life[lvl], 'iron_cost' : iron_cost[lvl], 'carbon_cost' : carbon_cost[lvl], 'build_time' : build_time[lvl], 'lvl' : lvl, 'health' : health, 'maxx' : health, 'u_id' : u_id, 'p_id' : "", 'timestamp' : now, 'created' : seconds, 'primary_support' : primary_support, 'secondary_support' : secondary_support})
		db.player_items.update({'_id' : cargo_bay_id},{"$set": {'cargo_bay_%d' %a : reactor_id}})
		

def engines(u_id, p_id,lvl): # All details for all engines. We need the User ID, the battle_ship ID, and the lvl of the item.
	name = {1: "Electrostatic Ion Thruster", 2 : "Xenon Hall Thruster", 3 : "Helicon Double Layer Thruster", 4 : "Magnetoplasmadynamic Thruster", 5 : "Variable Magnetoplasma Rocket"}
	item = "engine"
	primary_support = "Engineer"
	secondary_support = "Mechanic"
	thrust = {1: 20000, 2 : 25000, 3 : 50000, 4 : 100000, 5 : 125000}
	type = {1: "aux", 2 : "aux", 3 : "aux", 4 : "main", 5 : "main"}
	life = {1: 3600000, 2 : 2520000, 3 : 2160000, 4 : 3000000, 5 : 1800000}
	iron_cost = {1: 5000, 2 : 7000, 3 : 12000, 4 : 30000, 5 : 90000}
	carbon_cost = {1: 2000, 2 : 3000, 3 : 5000, 4 : 10000, 5 : 20000}
	build_time = {1: 1800, 2 : 1800, 3 : 2400, 4 : 2400, 5 : 3600}
	health = 2500
	#That should be most of the variables 
	#Lets start some inserts :-)
	if p_id:
		engine_id = db.player_items.insert({'name' : name[lvl], 'item' : item, 'thrust' : thrust[lvl], 'type' : type[lvl], 'life' : life[lvl], 'iron_cost' : iron_cost[lvl], 'carbon_cost' : carbon_cost[lvl], 'build_time' : build_time[lvl], 'lvl' : lvl, 'health' : health, 'maxx' : health, 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : now, 'created' : seconds, 'primary_support' : primary_support, 'secondary_support' : secondary_support})
		db.player_items.update({'_id' : p_id},{"$set": {'reactor' : engine_id}})
		personnel(u_id, p_id, primary_support, 1, "Engine Room")
	else:
		engine_id = db.player_items.insert({'name' : name[lvl], 'item' : item, 'thrust' : thrust[lvl], 'type' : type[lvl], 'life' : life[lvl], 'iron_cost' : iron_cost[lvl], 'carbon_cost' : carbon_cost[lvl], 'build_time' : build_time[lvl], 'lvl' : lvl, 'health' : health, 'maxx' : health, 'u_id' : u_id, 'p_id' : "", 'timestamp' : now, 'created' : seconds, 'primary_support' : primary_support, 'secondary_support' : secondary_support})
		db.player_items.update({'_id' : cargo_bay_id},{"$set": {'cargo_bay_%d' %a : engine_id}})
		
		
def warp_drive(u_id, p_id,lvl): # All details for all Warp Drives. We need the User ID, the battle_ship ID, and the lvl of the item.
	name = {1: "WDE-120", 2 : "WDE-240", 3 : "WDE-480", 4 : "WDE-1000", 5 : "WDE2000"}
	item = "warp_drive"
	type = "Warp Drive Engine"
	primary_support = "Engineer"
	secondary_support = "Mechanic"
	kw_ly = {1: .015, 2 : .01, 3 : .02, 4 : .01, 5 : .005}
	recharge = {1: 60, 2 : 30, 3 : 15, 4 : 90, 5 : 45}
	iron_cost = {1: 30000, 2 : 45000, 3 : 50000, 4 : 70000, 5 : 90000}
	carbon_cost = {1: 10000, 2 : 16000, 3 : 20000, 4 : 30000, 5 : 42000}
	build_time = {1: 1800, 2 : 1800, 3 : 2400, 4 : 2400, 5 : 3600}
	life = {1: 3600000, 2 : 2520000, 3 : 2160000, 4 : 3000000, 5 : 1800000}
	health = 2500
	#That should be most of the variables 
	#Lets start some inserts :-)
	if p_id:
		warp_drive_id = db.player_items.insert({'name' : name[lvl], 'item' : item, 'type' : type, 'kw_ly' : kw_ly[lvl], 'recharge' : recharge[lvl], 'iron_cost' : iron_cost[lvl], 'carbon_cost' : carbon_cost[lvl], 'build_time' : build_time[lvl], 'lvl' : lvl, 'health' : health, 'maxx' : health, 'life' : life[lvl], 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : now, 'created' : seconds, 'primary_support' : primary_support, 'secondary_support' : secondary_support})
	else:
		warp_drive_id = db.player_items.insert({'name' : name[lvl], 'item' : item, 'type' : type, 'kw_ly' : kw_ly[lvl], 'recharge' : recharge[lvl], 'iron_cost' : iron_cost[lvl], 'carbon_cost' : carbon_cost[lvl], 'build_time' : build_time[lvl], 'lvl' : lvl, 'health' : health, 'maxx' : health, 'life' : life, 'u_id' : u_id, 'p_id' : "", 'timestamp' : now, 'created' : seconds, 'primary_support' : primary_support, 'secondary_support' : secondary_support})


def cannon(u_id, p_id,lvl): # All details for all reactors. We need the User ID, the battle_ship ID, and the lvl of the item.
	name = {1: "GRC20M", 2 : "GRC25M", 3 : "GRC30M"}
	item = "Artillery"
	type = "Cannon"
	primary_support = "Mechanic"
	secondary_support = ""
	rps = {1 : 100, 2 : 30, 3 : 70}
	capacity = {1: 10000, 2 : 5000, 3 : 10000}
	caliber = {1 : 20, 2 : 25, 3 : 30}
	accuracy = {1 : .5, 2 : .7, 3 : .8}
	life = {1 : 48384000, 2 : 157248000, 3 : 4838400}
	iron_cost = {1 : 1, 2 : 2, 3 : 3}
	carbon_cost = {1 : 2, 2 : 1, 3 :5}
	build_time = {1 : 180, 2 : 180, 3 : 180}
	health = 50
	#That should be most of the variables 
	#Lets start some inserts :-)
	cannon_id = db.player_items.insert({'name' : name[lvl], 'item' : item, 'rps' : rps[lvl], 'capacity' : capacity[lvl], 'caliber' : caliber[lvl], 'accuracy' : accuracy[lvl], 'life' : life[lvl], 'iron_cost' : iron_cost[lvl], 'carbon_cost' : carbon_cost[lvl], 'build_time' : build_time[lvl], 'lvl' : lvl, 'health' : health, 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : now, 'created' : seconds, 'primary_support' : primary_support, 'secondary_support' : secondary_support, 'type' : type})
	
	# slot_name = "cannon_slot"
	# cannon_slot = db.player_items.update({'u_id' : u_id, '_id' : p_id}, {"$set": {slot_name : cannon_id}})

	
def missile(u_id, p_id,lvl): # All details for all reactors. We need the User ID, the battle_ship ID, and the lvl of the item.
	name = {1: "AAM-4 Stinger", 2 : "AAM-8 Stryker", 3 : "AAM-12"}
	item = "Artillery"
	type = "Missile"
	primary_support = "Mechanic"
	secondary_support = "Engineer"
	guidance = {1 : "Radar", 2 : "Radar", 3 : "Infrared"}
	thrust = {1 : 270000, 2 : 290000, 3 : 270000}
	limit = {1 : 30, 2 : 25, 3 : 100}
	accuracy = {1 : .7, 2 : .5, 3 : .9}
	warhead = {1 : 75, 2 : 88, 3 : 20}
	iron_cost = {1 : 100, 2 : 200, 3 : 300}
	carbon_cost = {1 : 200, 2 : 100, 3 :500}
	build_time = {1 : 1800, 2 : 1800, 3 : 1800}
	#That should be most of the variables 
	#Lets start some inserts :-)
	missile_id = db.player_items.insert({'name' : name[lvl], 'item' : item, 'guidance' : guidance[lvl], 'thrust' : thrust[lvl], 'accuracy' : accuracy[lvl], 'warhead' : warhead[lvl], 'range' : limit[lvl], 'iron_cost' : iron_cost[lvl], 'carbon_cost' : carbon_cost[lvl], 'build_time' : build_time[lvl], 'lvl' : lvl, 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : now, 'created' : seconds, 'primary_support' : primary_support, 'secondary_support' : secondary_support, 'type' : type})
	slot_name = "missile_slot"
	# missile_slot = db.player_items.update({'u_id' : u_id, '_id' : p_id, 'item' : "Ship"}, {"$set": {slot_name : missile_id}})
	# if missile_slot:
		# print "Updated missile slot"
	

def fighter(u_id, p_id, lvl, hanger_id): # At this moment I'm thinking each ship will be declared.
	name = "GF-37 Falcon"
	type = "Fighter"
	item = "Ship"
	fleet = "Base"
	primary_support = "Pilot"
	secondary_support = "Mechanic"
	limit = {1: 10000, 2 : 12000, 3 : 18000, 4 : 29500, 5 : 32000}
	cannons = 2
	missiles = 6
	bomb_missile_slots = 4
	life = {1: 8000, 2 : 7000, 3 : 5000, 4 : 4500, 5 : 4000}
	iron_cost = {1: 30000, 2 : 45000, 3 : 50000, 4 : 70000, 5 : 90000}
	carbon_cost = {1: 10000, 2 : 16000, 3 : 20000, 4 : 30000, 5 : 42000}
	build_time = {1: 43200, 2 : 54300, 3 : 65400, 4 : 76500, 5 : 87600}
	health = 1500
	pilot = "Unassigned"
	#That should be most of the variables 
	#Lets start some inserts :-)
	p_id = db.player_items.insert({'name' : name, 'item' : item, 'type' : type, 'range' : limit[lvl], 'life' : life[lvl], 'iron_cost' : iron_cost[lvl], 'carbon_cost' : carbon_cost[lvl], 'build_time' : build_time[lvl], 'lvl' : lvl, 'health' : health, 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : now, 'created' : seconds, 'primary_support' : primary_support, 'secondary_support' : secondary_support, 'fleet' : fleet, 'cannons' : cannons, 'missiles' : missiles, 'pilot' : pilot})
	
	for k in range(cannons):
		cannon(u_id, p_id,lvl)
	
	for d in range(missiles):
		missile(u_id, p_id,lvl)


	
def create_player_items(u_id, race):
	# Global Values for a battle ship
	name = "GCBS-371"
	item = "ship"
	type = "Battleship"
	cannon_slots = 10
	missile_slots = 12
	if race == "Human":
		# location = db.universe.find_one({'name' : "Earth"})
		x = 0
		y = 0
		lvl = 1
		#Lets Make a ship. This is just the container for 
		battle_ship = db.player_items.insert({'name' : name, 'item' : item, 'type' : type, 'x' : x, 'y' : y, 'u_id' : u_id, 'timestamp' : now, 'created' : seconds })
		# By making it a variable, it will still insert, and the variable becomes the id for the item interred.
		#Adding the items/compartments to the ships
		compartments(u_id, battle_ship)
		#reactor, this is the power unit for the ship
		reactor(u_id, battle_ship, lvl)
		# Add an engine
		engines(u_id, battle_ship, lvl)
		# Add the warp drive
		warp_drive(u_id, battle_ship, lvl)
		# Now it's time to start populating the ship.
		# Now lets give her a mini-fleet
		left_hanger = db.player_items.find_one({'p_id' : battle_ship, 'name' : "Left Hanger"})['_id']
		for a in range(random.randint(5,30)):
			fighter(u_id, battle_ship, lvl, left_hanger)
			lvl = random.randint(1,3)
			personnel(u_id, battle_ship, "Pilot", lvl, "Pilots Lounge")

		right_hanger = db.player_items.find_one({'p_id' : battle_ship, 'name' : "Right Hanger"})['_id']
		for a in range(random.randint(5,30)):
			fighter(u_id, battle_ship, lvl, right_hanger)
			lvl = random.randint(1,3)
			personnel(u_id, battle_ship, "Pilot", lvl, "Pilots Lounge")
	
	
	elif race == "Delvarnian":
		location = db.universe.find_one({'name' : "Earth"})
		x = location['x_pos']
		y = location['y_pos']
		lvl = 1
		#Lets Make a ship. This is just the container for 
		battle_ship = db.player_items.insert({'name' : name, 'item' : item, 'type' : type, 'x' : x, 'y' : y, 'u_id' : u_id, 'timestamp' : now, 'created' : seconds })
		# By making it a variable, it will still insert, and the variable becomes the id for the item interred.
		#Adding the items/compartments to the ships
		compartments(u_id, battle_ship)
		#reactor, this is the power unit for the ship
		reactor(u_id, battle_ship, lvl)
		# Add an engine
		engines(u_id, battle_ship, lvl)
		# Add the warp drive
		warp_drive(u_id, battle_ship, lvl)
		# Now it's time to start populating the ship.
		# Now lets give her a mini-fleet
		left_hanger = db.player_items.find_one({'p_id' : battle_ship, 'name' : "Left Hanger"})['_id']
		for a in range(random.randint(5,15)):
			fighter(u_id, battle_ship, lvl, left_hanger)
			lvl = random.randint(1,3)
			personnel(u_id, battle_ship, "Pilot", lvl, "Pilots Lounge")

		right_hanger = db.player_items.find_one({'p_id' : battle_ship, 'name' : "Right Hanger"})['_id']
		for a in range(random.randint(5,15)):
			fighter(u_id, battle_ship, lvl, right_hanger)
			lvl = random.randint(1,3)
			personnel(u_id, battle_ship, "Pilot", lvl, "Pilots Lounge")


	
	# players_items = db.player_items.find({'u_id' : u_id})
	# for a in players_items:
		# print a['name'], a['item']
		


def player(u_id):
	race = "Human"
	start_date = datetime.datetime.now() #Need to know how long they have been around.
	strength = int(0) # Based on number of ships and ammo, a way for a player to know who to pick on and who not ot.
	experience = int(0) #starting at Zero. will grow through battles and events.
	#Lets insert everything into the db to get the user account created.
	db.users.update({'_id' : u_id},{"$set": {'race' : race, 'start_date' : start_date, 'strength' : strength, 'experience' : experience }})
	# print "Inserting %s, who is of the race %s. %s started on %r, and has a current strength of %d, and the experience of %d" %(username, race, username, start_date, strength, experience)
	create_player_items(u_id, race)




def test(username):
	password = "password"
	
	u_id = db.users.insert({'username' : username, 'password' : password})
	
	player(u_id)

def clear_db():
	

	db.users.drop()
	db.player_items.drop()	
	
	
