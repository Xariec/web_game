import pymongo
import math
import time
import datetime
import random
from db_items import *



db = pymongo.Connection('localhost', 27017).game

class Battleship(object):
	
	def __init__(self):
		self.now = datetime.datetime.now()  # Gets the current time.
		self.day_of_year = datetime.datetime.now().timetuple().tm_yday
		# convert the time to an integer we can use for checking how much time has passed.
		self.days = (self.now.year * 365) + self.day_of_year + (self.now.year/4)
		self.hours = self.days * 24 + self.now.hour
		self.minutes = self.hours *60 + self.now.minute
		self.seconds = self.minutes * 60 + self.now.second
		self.name = "GCBS-371"
		self.item = "Ship"
		self.type = "Battleship"
		self.primary_support = ""
		self.secondary_support = ""
		self.min_support = 1
		self.max_persons = 5
		self.health = 1500
		self.project_slot = ""
		self.timestamp = datetime.datetime.now()
		self.created = self.seconds

	def engineRoomBattleship(self, p_id, u_id):
		self.engine = DbItems()
		self.name = "Engine Room"
		self.item = "Compartment"
		self.type = "Engine Compartment"
		self.primary_support = "Engineer"
		self.secondary_support = "Mechanic"
		self.primary_engine = self.engine.engine(u_id, p_id, 4)
		self.aux1_engine = self.engine.engine(u_id, p_id, 1)
		self.aux2_engine = self.engine.engine(u_id, p_id, 1)
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot, 'primary_engine' : self.primary_engine, 'aux1_engine' : self.aux1_engine, 'aux2_engine' : self.aux2_engine, 'max_persons' : self.max_persons})
		return self.db_insert
		
	def powerRoomBattleship(self, p_id, u_id):
		self.power = DbItems()
		self.name = "Power Room"
		self.item = "Compartment"
		self.type = "Engine Compartment"
		self.primary_support = "Engineer"
		self.secondary_support = "Mechanic"
		self.reactor = self.power.reactor(u_id, p_id, 1)
		self.warp_drive = self.power.warpDrive(u_id, p_id, 1)
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot, 'reactor' : self.reactor, 'warp_drive' : self.warp_drive, 'max_persons' : self.max_persons})
		return self.db_insert
		
	def mechanicsBayBattleship(self, p_id, u_id):
		self.name = "Mechanics Bay"
		self.item = "Compartment"
		self.type = "Mechanics Compartment"
		self.primary_support = "Mechanic"
		self.secondary_support = "Mechanic"
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert

	def pilotsLoungeBattleship(self, p_id, u_id):
		self.name = "Pilots Lounge"
		self.item = "Compartment"
		self.type = "Lounge Compartment"
		self.min_support = 0
		self.max_persons = 25		
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
		
	def rightHangerBattleship(self, p_id, u_id):
		self.name = "Right Hanger"
		self.item = "Compartment"
		self.type = "Hanger Compartment"
		self.primary_support = "Mechanic"
		self.secondary_support = "Mechanic"
		self.min_support = 2
		self.max_persons = 10
		self.small_bays = 20
		self.medium_bays = 5
		self.large_bays = 1
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons, 'small_bays' : self.small_bays, 'medium_bays' : self.medium_bays, 'large_bays' : self.large_bays})
		return self.db_insert

	def leftHangerBattleship(self, p_id, u_id):
		self.name = "Left Hanger"
		self.item = "Compartment"
		self.type = "Hanger Compartment"
		self.primary_support = "Mechanic"
		self.secondary_support = "Mechanic"
		self.min_support = 2
		self.max_persons = 10
		self.small_bays = 20
		self.medium_bays = 5
		self.large_bays = 1	
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons, 'small_bays' : self.small_bays, 'medium_bays' : self.medium_bays, 'large_bays' : self.large_bays})
		return self.db_insert
		
	def cargoBayBattleship(self, p_id, u_id):
		self.name = "Cargo Bay"
		self.item = "Compartment"
		self.type = "Cargo Compartment"
		self.primary_support = "Mechanic"
		self.secondary_support = "Mechanic"
		self.min_support = 2
		self.max_persons = 10
		self.small_bays = 100
		self.medium_bays = 50
		self.large_bays = 10			
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons, 'small_bays' : self.small_bays, 'medium_bays' : self.medium_bays, 'large_bays' : self.large_bays})
		return self.db_insert		
			
	def communicationsCenterBattleship(self, p_id, u_id):
		self.name = "Communications Center"
		self.item = "Compartment"
		self.type = "Comm Compartment"
		self.primary_support = "Scientist"
		self.secondary_support = "Engineer"
		self.min_support = 5
		self.max_persons = 10
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
		
	def operationsCenterBattleship(self, p_id, u_id):
		self.name = "Operations Center"
		self.item = "Compartment"
		self.type = "Operations Compartment"
		self.primary_support = "Scientist"
		self.secondary_support = "Engineer"
		self.min_support = 5
		self.max_persons = 10
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
		
	def battleCenterBattleship(self, p_id, u_id):
		self.name = "Battle Center"
		self.item = "Compartment"
		self.type = "Battle Compartment"
		self.primary_support = "Engineer"
		self.secondary_support = "Engineer"
		self.min_support = 5
		self.max_persons = 10
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert

	def weaponsCenterBattleship(self, p_id, u_id):
		self.name = "Weapons Center"
		self.item = "Compartment"
		self.type = "Weapon Compartment"
		self.primary_support = "Engineer"
		self.secondary_support = "Engineer"
		self.min_support = 5
		self.max_persons = 10
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
		
	def mediaLoungeBattleship(self, p_id, u_id):
		self.name = "Media Lounge"
		self.item = "Compartment"
		self.type = "Lounge Compartment"
		self.min_support = 0
		self.max_persons = 25	
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
		
	def messHallBattleship(self, p_id, u_id):
		self.name = "Mess Hall"
		self.item = "Compartment"
		self.type = "Lounge Compartment"
		self.primary_support = "Scientist"
		self.max_persons = 25
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert	
		
	def dormsBattleship(self, p_id, u_id):
		self.name = "Dorms"
		self.item = "Compartment"
		self.type = "Lounge Compartment"
		self.min_support = 0
		self.max_persons = 50
		self.db_insert = db.player_items.insert({'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
		
	def sickBayBattleship(self, p_id, u_id):
		self.name = "Sick Bay"
		self.item = "Compartment"
		self.type = "Medical Compartment"
		self.primary_support = "Scientist"
		self.secondary_support = "Scientist"
		self.min_support = 0
		self.max_persons = 10
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
		
	def researchLabBattleship(self, p_id, u_id):
		self.name = "Research Lab"
		self.item = "Compartment"
		self.type = "Science Compartment"
		self.primary_support = "Scientist"
		self.secondary_support = "Scientist"
		self.min_support = 0
		self.max_persons = 10
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
		
	def engineeringLabBattleship(self, p_id, u_id):
		self.name = "Engineering Lab"
		self.item = "Compartment"
		self.type = "Science Compartment"
		self.primary_support = "Engineer"
		self.secondary_support = "Engineer"
		self.min_support = 0
		self.max_persons = 10
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
		
	def techLabBattleship(self, p_id, u_id):
		self.name = "Tech Lab"
		self.item = "Compartment"
		self.type = "Science Compartment"
		self.primary_support = "Instructor"
		self.secondary_support = "Instructor"
		self.min_support = 0
		self.max_persons = 25
		self.db_insert = db.player_items.insert({'u_id' : u_id, 'p_id' : p_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'project_slot' : self.project_slot,  'max_persons' : self.max_persons})
		return self.db_insert
	
	def createBattleship(self, u_id):
		self.p_id = db.player_items.insert({'u_id' : u_id, 'p_id' : u_id, 'name' : self.name, 'item' : self.item, 'type' : self.type, 'primary_support' : self.primary_support, 'secondary_support' : self.secondary_support, 'min_support' : self.min_support, 'health' : self.health, 'created' : self.seconds, 'timestamp' : self.timestamp})
		
		self.all = {'Engine Room' : self.engineRoomBattleship(self.p_id, u_id), 'Power Room' : self.powerRoomBattleship(self.p_id, u_id), 'Mechanics Bay' : self.mechanicsBayBattleship(self.p_id, u_id), 'Pilots Lounge': self.pilotsLoungeBattleship(self.p_id, u_id), 'Right Hanger' : self.rightHangerBattleship(self.p_id, u_id), 'Left Hanger' : self.leftHangerBattleship(self.p_id, u_id), 'Cargo Bay' : self.cargoBayBattleship(self.p_id, u_id), 'Communications Center' : self.communicationsCenterBattleship(self.p_id, u_id), 'Operations Center' : self.operationsCenterBattleship(self.p_id, u_id), 'Battle Center' : self.battleCenterBattleship(self.p_id, u_id),'Weapons Center' : self.weaponsCenterBattleship(self.p_id, u_id), 'Media Lounge' : self.mediaLoungeBattleship(self.p_id, u_id), 'Mess Hall' : self.messHallBattleship(self.p_id, u_id), 'Dorms' : self.dormsBattleship(self.p_id, u_id), 'Sick Bay' : self.sickBayBattleship(self.p_id, u_id), 'Research Lab': self.researchLabBattleship(self.p_id, u_id), 'Engineering Lab' : self.engineeringLabBattleship(self.p_id, u_id), 'Tech Lab' : self.techLabBattleship(self.p_id, u_id)}
		
		for key, value in self.all.iteritems():
			db.player_items.update({'_id' : self.p_id}, {"$set" : { key : value}})
			
		return self.p_id
			
			

			
			
			
			
			
			
			
if __name__ == '__main__' :
	battleship = Battleship()
	newBattleship = battleship.createBattleship("Abc123")
	test = db.player_items.find_one({'_id' : newBattleship})
	print test
	for key,value in test.iteritems():
		print key, value
	
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		