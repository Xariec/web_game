import pymongo
import random
import datetime
import math
import time



db = pymongo.Connection('localhost', 27017).game






# Lets start creating some Items for the database..... this will only take all night :-)



# The following will be all items in db.items()



def engines():
	db.items.insert({'name' : "Electrostatic Ion Thruster", 'object' : "Engine", 'thrust' : 20000, 'kw' : 60, 'life' : 3600000, 'seconds_used' : 0, 'iron_cost' : 5000, 'carbon_cost' : 2000, 'build_time' : 1800, 'lvl' : 1, 'health' : 1000})
	db.items.insert({'name' : "Xenon Hall Thruster", 'object' : "Engine", 'thrust' : 25000, 'kw' : 80, 'life' : 2520000, 'seconds_used' : 0, 'iron_cost' : 7000, 'carbon_cost' : 3000, 'build_time' : 1800, 'lvl' : 2, 'health' : 1000})
	db.items.insert({'name' : "Helicon Double Layer Thruster", 'object' : "Engine", 'thrust' : 50000, 'kw' : 100, 'life' : 2160000, 'seconds_used' : 0, 'iron_cost' : 12000, 'carbon_cost' : 5000, 'build_time' : 2600, 'lvl' : 3, 'health' : 1000})
	db.items.insert({'name' : "Magnetoplasmadynamic Thruster", 'object' : "Engine", 'thrust' : 100000, 'kw' : 200, 'life' : 3000000, 'seconds_used' : 0, 'iron_cost' : 30000, 'carbon_cost' : 10000, 'build_time' : 3600, 'lvl' : 4, 'health' : 10000})
	db.items.insert({'name' : "Verible Magnetoplasma Rocket", 'object' : "Engine", 'thrust' : 125000, 'kw' : 200, 'life' : 3000000, 'seconds_used' : 0, 'iron_cost' : 90000, 'carbon_cost' : 20000, 'build_time' : 4800, 'lvl' : 5, 'health' : 10000})

	
engines()

def warp_drives():
	db.items.insert({'name' : "WDE-120", 'object' : "Warp_drive", 'kw_ly' : 0.015, 'recharge_time' : 60, 'life' : 8000, 'times_used' : 0, 'iron_cost' : 30000, 'carbon_cost' : 10000, 'build_time' : 1800, 'lvl' : 1, 'health' : 10000})
	db.items.insert({'name' : "WDE-240", 'object' : "Warp_drive", 'kw_ly' : 0.01, 'recharge_time' : 30, 'life' : 7000, 'times_used' : 0, 'iron_cost' : 45000, 'carbon_cost' : 16000, 'build_time' : 1800, 'lvl' : 2, 'health' : 10000})
	db.items.insert({'name' : "WDE-480", 'object' : "Warp_drive", 'kw_ly' : 0.02, 'recharge_time' : 15, 'life' : 5000, 'times_used' : 0, 'iron_cost' : 45000, 'carbon_cost' : 20000, 'build_time' : 1800, 'lvl' : 2, 'health' : 10000})
	db.items.insert({'name' : "WDE-1000", 'object' : "Warp_drive", 'kw_ly' : 0.01, 'recharge_time' : 90, 'life' : 4500, 'times_used' : 0, 'iron_cost' : 70000, 'carbon_cost' : 30000, 'build_time' : 1800, 'lvl' : 3, 'health' : 10000})
	db.items.insert({'name' : "WDE-2000", 'object' : "Warp_drive", 'kw_ly' : 0.01, 'recharge_time' : 60, 'life' : 4000, 'times_used' : 0, 'iron_cost' : 80000, 'carbon_cost' : 42000, 'build_time' : 1800, 'lvl' : 4, 'health' : 10000})
	db.items.insert({'name' : "WDE-1000-V2", 'object' : "Warp_drive", 'kw_ly' : 0.005, 'recharge_time' : 60, 'life' : 3000, 'times_used' : 0, 'iron_cost' : 125000, 'carbon_cost' : 60000, 'build_time' : 1800, 'lvl' : 5, 'health' : 10000})
	db.items.insert({'name' : "WDE-2000-V2", 'object' : "Warp_drive", 'kw_ly' : 0.005, 'recharge_time' : 90, 'life' : 2500, 'times_used' : 0, 'iron_cost' : 172000, 'carbon_cost' : 72000, 'build_time' : 1800, 'lvl' : 5, 'health' : 10000})


warp_drives()	
def reactors():
	db.items.insert({'name' : "DD-FG-40", 'object' : "Reactor", 'effiency' : .4, 'max_deuterium' : 450, 'life' : 31536000, 'seconds_used' : 0, 'iron_cost' : 10000, 'carbon_cost' : 1000, 'build_time' : 1800, 'lvl' : 1, 'health' : 25000})
	db.items.insert({'name' : "DD-FG-50", 'object' : "Reactor", 'effiency' : .5, 'max_deuterium' : 450, 'life' : 31536000, 'seconds_used' : 0, 'iron_cost' : 20000, 'carbon_cost' : 2500, 'build_time' : 1800, 'lvl' : 2, 'health' : 25000})
	db.items.insert({'name' : "DD-FG-65", 'object' : "Reactor", 'effiency' : .65, 'max_deuterium' : 600, 'life' : 31536000, 'seconds_used' : 0, 'iron_cost' : 25000, 'carbon_cost' : 3000, 'build_time' : 1800, 'lvl' : 3, 'health' : 25000})
	db.items.insert({'name' : "DD-FG-700", 'object' : "Reactor", 'effiency' : .7, 'max_deuterium' : 600, 'life' : 31536000, 'seconds_used' : 0, 'iron_cost' : 40000, 'carbon_cost' : 8000, 'build_time' : 1800, 'lvl' : 4, 'health' : 25000})
	db.items.insert({'name' : "DD-FG-850", 'object' : "Reactor", 'effiency' : .85, 'max_deuterium' : 750, 'life' : 31536000, 'seconds_used' : 0, 'iron_cost' : 80000, 'carbon_cost' : 20000, 'build_time' : 1800, 'lvl' : 5, 'health' : 25000})
	db.items.insert({'name' : "DD-FG-950", 'object' : "Reactor", 'effiency' : .95, 'max_deuterium' : 750, 'life' : 31536000, 'seconds_used' : 0, 'iron_cost' : 120000, 'carbon_cost' : 40000, 'build_time' : 1800, 'lvl' : 5, 'health' : 25000})


reactors()	
def artillery():
	# Cannons
	db.items.insert({'name' : "GRC20M", 'object' : "Cannon", 'rounds_per_second' : 100, 'caliber' : 20, 'accuracy' : .45, 'capacity' : 1000, 'iron_cost' : 1, 'carbon_cost' : 2, 'build_time' : 3, 'lvl' : 1})
	db.items.insert({'name' : "GRC25M", 'object' : "Cannon", 'rounds_per_second' : 30, 'caliber' : 25, 'accuracy' : .8, 'capacity' : 700,  'iron_cost' : 1, 'carbon_cost' : 2, 'build_time' : 3, 'lvl' : 3})
	db.items.insert({'name' : "GRC30M", 'object' : "Cannon", 'rounds_per_second' : 70, 'caliber' : 30, 'accuracy' : .65, 'capacity' : 500,  'iron_cost' : 1, 'carbon_cost' : 2, 'build_time' : 3, 'lvl' : 5})
	# Missiles
	db.items.insert({'name' : "AAM-4 Stinger", 'object' : "Missile", 'guidance' : "Radar", 'thrust' : 270000, 'warhead' : 75, 'range' : 30, 'accuracy' : .7, 'iron_cost' : 500, 'carbon_cost' : 100, 'build_time' : 300, 'lvl' : 1})
	db.items.insert({'name' : "AAM-8 Stryker", 'object' : "Missile", 'guidance' : "Radar", 'thrust' : 290000, 'warhead' : 88, 'range' : 25, 'accuracy' : .5, 'iron_cost' : 700, 'carbon_cost' : 300, 'build_time' : 450, 'lvl' : 2})
	db.items.insert({'name' : "AAM-12", 'object' : "Missile", 'guidance' : "Infrared", 'thrust' : 270000, 'warhead' : 20, 'range' : 100, 'accuracy' : .9, 'iron_cost' : 850, 'carbon_cost' : 400, 'build_time' : 600, 'lvl' : 3})
	db.items.insert({'name' : "AAM-100-R", 'object' : "Missile", 'guidance' : "Radar", 'thrust' : 75000, 'warhead' : 100, 'range' : 150, 'accuracy' : .8, 'iron_cost' : 1050, 'carbon_cost' : 800, 'build_time' : 900, 'lvl' : 4})
	db.items.insert({'name' : "AAM-100-I", 'object' : "Missile", 'guidance' : "Infrared", 'thrust' : 75000, 'warhead' : 100, 'range' : 150, 'accuracy' : .85, 'iron_cost' : 1050, 'carbon_cost' : 800, 'build_time' : 900, 'lvl' : 4})
	db.items.insert({'name' : "AANM-5-Destroyer", 'object' : "Missile", 'guidance' : "Laser", 'thrust' : 25000, 'warhead' : 5000, 'range' : 500, 'accuracy' : .95, 'iron_cost' : 30050, 'carbon_cost' : 8000, 'build_time' : 1800, 'lvl' : 5})
	db.items.insert({'name' : "AAEMP-Stunner", 'object' : "Missile", 'guidance' : "Radar", 'thrust' : 270000, 'warhead' : 0, 'range' : 500, 'accuracy' : .8, 'iron_cost' : 3050, 'carbon_cost' : 800, 'build_time' : 900, 'lvl' : 5})


artillery()	
def ships():
	db.items.insert({'name' : "GCBS-371", 'object' : "Battleship", 'cannon_slots' : 10, 'missile_slots' : 12, 'bomb_slots' : 0, 'bomb_missle_slots' : 0})
	db.items.insert({'name' : "GD-971", 'object' : "Destoryer", 'cannon_slots' : 6, 'missile_slots' : 10, 'bomb_slots' : 0, 'bomb_missle_slots' : 0})
	db.items.insert({'name' : "GF-37 Falcon", 'object' : "Fighter", 'cannon_slots' : 2, 'missile_slots' : 4, 'bomb_slots' : 0, 'bomb_missle_slots' : 2})
	db.items.insert({'name' : "GB-3", 'object' : "Bomber", 'cannon_slots' : 1, 'missile_slots' : 2, 'bomb_slots' : 6, 'bomb_missle_slots' : 2})
	db.items.insert({'name' : "GGCS-71", 'object' : "Cargo", 'cannon_slots' : 10, 'missile_slots' : 4, 'bomb_slots' : 6, 'bomb_missle_slots' : 2})
	

ships()
	
	