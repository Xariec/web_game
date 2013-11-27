import pymongo
import math
import time
import datetime
import random



db = pymongo.Connection('localhost', 27017).game

item_categories = ['engines', 'weapons', 'communication', 'warp drives', 'reactors', 'surveillance', 'artillery']
list_items_levels = {'engine' : 5, 'reactor' : 6, 'warpDrive' : 5}


class DbItems(object):
	
	def __init__(self):
		self.now = datetime.datetime.now()  # Gets the current time.
		self.day_of_year = datetime.datetime.now().timetuple().tm_yday
		# convert the time to an integer we can use for checking how much time has passed.
		self.days = (self.now.year * 365) + self.day_of_year + (self.now.year/4)
		self.hours = self.days * 24 + self.now.hour
		self.minutes = self.hours *60 + self.now.minute
		self.seconds = self.minutes * 60 + self.now.second
		self.timestamp = datetime.datetime.now()
		self.created = self.seconds
		self.engine_levels = 5
		self.reactor_levels = 6
		self.warpdrive_levels = 5

	def engine(self, u_id, p_id, lvl):
		self.name = {1: "Electrostatic Ion Thruster", 2 : "Xenon Hall Thruster", 3 : "Helicon Double Layer Thruster", 4 : "Magnetoplasmadynamic Thruster", 5 : "Variable Magnetoplasma Rocket"}
		self.item = "Engine"
		self.type = {1: "Auxiliary", 2 : "Auxiliary", 3 : "Auxiliary", 4 : "Primary", 5 : "Primary"}
		self.primary_support = "Engineer"
		self.secondary_support = "Mechanic"
		self.thrust = {1: 20000, 2 : 25000, 3 : 50000, 4 : 100000, 5 : 125000}
		self.life = {1: 3600000, 2 : 2520000, 3 : 2160000, 4 : 3000000, 5 : 1800000}
		self.iron_cost = {1: 5000, 2 : 7000, 3 : 12000, 4 : 30000, 5 : 90000}
		self.carbon_cost = {1: 2000, 2 : 3000, 3 : 5000, 4 : 10000, 5 : 20000}
		self.build_time = {1: 1800, 2 : 1800, 3 : 2400, 4 : 2400, 5 : 3600}
		self.health = 2500
		self.engine_id = db.player_items.insert({'name' : self.name[lvl], 'item' : self.item, 'thrust' : self.thrust[lvl], 'type' : self.type[lvl], 'life' : self.life[lvl], 'iron_cost' : self.iron_cost[lvl], 'carbon_cost' : self.carbon_cost[lvl], 'build_time' : self.build_time[lvl], 'lvl' : lvl, 'health' : self.health, 'max_health' : self.health, 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : self.now, 'created' : self.seconds, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support})
		
		return self.engine_id
		
	def reactor(self, u_id, p_id, lvl):
		self.name = {1: "DD-FG-40", 2 : "DD-FG-50", 3 : "DD-FG-65", 4 : "DD-FG-700", 5 : "DD-FG-850", 6 : "DD-FG-950"}
		self.item = "Reactor"
		self.type = "Fusion"
		self.primary_support = "Engineer"
		self.secondary_support = "Mechanic"
		self.effiency = {1 : .4, 2 : .5, 3 : .65, 4 : .7, 5 : .85, 6 : .95}
		self.max_deuterium = {1 : 450, 2 : 450, 3 : 600, 4 : 600, 5 : 750, 6 : 750}
		self.life = {1 : 48384000, 2 : 157248000, 3 : 4838400, 4 : 15724800, 5 : 4838400, 6 : 15724800}
		self.iron_cost = {1 : 10000, 2 : 20000, 3 : 25000, 4 : 40000, 5 : 80000, 6 : 120000}
		self.carbon_cost = {1 : 1000, 2 : 2500, 3 : 3000, 4 : 8000, 5 : 20000, 6 : 40000}
		self.build_time = {1 : 1800, 2 : 1800, 3 : 2400, 4 : 2400, 5 : 3600, 6 : 3600}
		self.health = 2500
		self.reactor_id = db.player_items.insert({'name' : self.name[lvl], 'item' : self.item, 'type' : self.type, 'life' : self.life[lvl], 'iron_cost' : self.iron_cost[lvl], 'carbon_cost' : self.carbon_cost[lvl], 'deuterium_cost' : self.max_deuterium[lvl], 'max_deurtium' : self.max_deuterium[lvl], 'build_time' : self.build_time[lvl], 'lvl' : lvl, 'health' : self.health, 'max_health' : self.health, 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : self.now,'created' : self.seconds, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'effiency' : self.effiency[lvl]})
		
		return self.reactor_id
		
	def warpDrive(self, u_id, p_id, lvl):
		self.name = {1: "WDE-120", 2 : "WDE-240", 3 : "WDE-480", 4 : "WDE-1000", 5 : "WDE2000"}
		self.item = "Warp Drive"
		self.type = "Warp Drive Engine"
		self.primary_support = "Engineer"
		self.secondary_support = "Mechanic"
		self.kw_ly = {1: .015, 2 : .01, 3 : .02, 4 : .01, 5 : .005}
		self.recharge = {1: 60, 2 : 30, 3 : 15, 4 : 90, 5 : 45}
		self.iron_cost = {1: 30000, 2 : 45000, 3 : 50000, 4 : 70000, 5 : 90000}
		self.carbon_cost = {1: 10000, 2 : 16000, 3 : 20000, 4 : 30000, 5 : 42000}
		self.build_time = {1: 1800, 2 : 1800, 3 : 2400, 4 : 2400, 5 : 3600}
		self.life = {1: 3600000, 2 : 2520000, 3 : 2160000, 4 : 3000000, 5 : 1800000}
		self.health = 2500
		self.warp_drive_id = db.player_items.insert({'name' : self.name[lvl], 'item' : self.item, 'type' : self.type, 'life' : self.life[lvl], 'iron_cost' : self.iron_cost[lvl], 'carbon_cost' : self.carbon_cost[lvl], 'build_time' : self.build_time[lvl], 'lvl' : lvl, 'health' : self.health, 'max_health' : self.health, 'u_id' : u_id, 'p_id' : p_id, 'timestamp' : self.now,'created' : self.seconds, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'kw_ly' : self.kw_ly[lvl], 'reacharch_time' : self.recharge[lvl]})
		
		return self.warp_drive_id
	
	def listItems(self, item, lvl):
		for key,value in list_items_levels.iteritems():
			print key, value
			test = key.object()
			print test
			print type(test)

			
		
	
	
if __name__ == '__main__':
	C = DbItems()
	items = C.listItems("test", 1)
	
	
	