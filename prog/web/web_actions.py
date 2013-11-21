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





# u_id = db.users.find_one({'username' : "test"})['_id']

class Population(object):


	def getAllPersonnel(self, u_id):
		self.personnel = db.player_items.find({'u_id' : u_id, 'item' : "personnel"})
		
		
		self.type = []
		self.physician = []
		self.pilot = []
		self.engineer = []
		self.scientist = []
		self.instructor = []
		self.mechanic = []
		self.military = []
		self.personnell = []
		
		for x in self.personnel:
			if x['type'] not in self.type:
				self.type.append(x['type'])
			if x['type'] == "Physician":
				self.physician.append((x['name'], x['title'], x['gender'], x['location'], x['assigned'], x['age']))
			elif x['type'] == "Pilot":
				self.pilot.append((x['name'], x['title'], x['gender'], x['location'], x['assigned'], x['age']))
			elif x['type'] == "Engineer":
				self.engineer.append((x['name'], x['title'], x['gender'], x['location'], x['assigned'], x['age']))
			elif x['type'] == "Scientist":
				self.scientist.append((x['name'], x['title'], x['gender'], x['location'], x['assigned'], x['age']))
			elif x['type'] == "Instructor":
				self.instructor.append((x['name'], x['title'], x['gender'], x['location'], x['assigned'], x['age']))
			elif x['type'] == "Mechanic":
				self.mechanic.append((x['name'], x['title'], x['gender'], x['location'], x['assigned'], x['age']))
			elif x['type'] == "Military":
				self.military.append((x['name'], x['title'], x['gender'], x['location'], x['assigned'], x['age']))	
			elif x['type'] == "Personnel":
				self.personnell.append((x['name'], x['title'], x['gender'], x['location'], x['assigned'], x['age']))
				
				
		return ({"Pilot" :self.pilot, "Physician" :self.physician, "Engineer" : self.engineer, "Scientist" : self.scientist, "Instructor" : self.instructor, "Mechanic" : self.mechanic, "Military" : self.military, "Personnel" : self.personnell}, {"type" :self.type})
		
	def getOnePersonnel(self, type, u_id):
		self.personnel = db.player_items.find({'u_id' : u_id, 'item' : "personnel", 'type' : type})
		p = []
		for x in self.personnel:
			p.append((x['name'], x['title'], x['gender'], x['location'], x['assigned'], x['age']))
			
		return(p)
		
		
		
		
		

		
		
		
		
if __name__ == '__main__':
	u_id = db.users.find_one({'username' : "test"})['_id']
	populate = Population()
	list = populate.getAllPersonnel(u_id)[0]
	buttons = populate.getAllPersonnel(u_id)[1]
	print buttons
	for key in list.keys():
		print key

		
		
		
		
		
		
		