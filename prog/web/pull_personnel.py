import pymongo
import math
import time
import datetime
import random
import setup


db = pymongo.Connection('localhost', 27017).game

now = datetime.datetime.now()  # Gets the current time.
day_of_year = datetime.datetime.now().timetuple().tm_yday
# convert the time to an integer we can use for checking how much time has passed.
days = (now.year * 365) + day_of_year + (now.year/4)
hours = days * 24 + now.hour
minutes = hours *60 + now.minute
seconds = minutes * 60 + now.second # Seconds, fairly accurate depiction of time since the year of 0001





u_id = db.users.find_one({'username' : "test"})['_id']

class Personnel(object):


	def getPersonnel(self, u_id):
		self.personnel = db.player_items.find({'u_id' : u_id, 'item' : "personnel"})
		
		self.physician = []
		self.pilot = []
		
		
		for x in self.personnel:
			# print x['type']
			if x['type'] == "Physician":
				self.physician.append((x['name'], x['title'], x['gender'], x['location'], x['assigned']))
			elif x['type'] == "Pilot":
				self.pilot.append((x['name'], x['title'], x['gender'], x['location'], x['assigned']))
				
		
		return ({"pilot" :self.pilot, "physician" :self.physician})
		
		# for b in range(len(self.pilot)):
			# x = self.pilot[b]
			# for c in range(len(x)):
				# print x[c]
			
		


a =Personnel()
pilots = a.getPersonnel(u_id)
list = a.getPersonnel(u_id)
pilots = list['pilot']
physician = list['physician']
for x in range(len(pilots)):
	print pilots[x]
	


# physician = []
# instructor = []
# personnel = []
# scientist = []
# mechanic = []
# military = []
# pilot = []
# engineer = []


# for x in personnel:
	# print x
	# print x['type']
	# if x['type'] == "Physician":
		# physician.append((x['name'], x['title']))
	# name.append(x['name'])
	# title.append(x['title'])
	# skill.append(x['skill'])
	# health.append(x['health'])
	# gender.append(x['gender'])
	# position[(x['type'])] = ""
	# location.append(x['location'])
	
	
# print physician