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

job_categories = ['Navigation', 'Artillery', 'Ships', 'Support Systems', 'Sensors']

female_names = [' Sophia' , ' Emma' , ' Olivia' , ' Isabella' , ' Ava' , ' Lily' , ' Zoe' , ' Chloe' , ' Mia' , ' Madison' , ' Emily' , ' Ella' , ' Madelyn' , ' Abigail' , ' Aubrey' , ' Addison' , 'Avery' , ' Layla' , ' Hailey' , ' Amelia' , ' Hannah' , ' Charlotte' , ' Kaitlyn' , ' Harper' , ' Kaylee' , ' Sophie' , ' Mackenzie' , ' Peyton' , ' Riley' , ' Grace' , ' Brooklyn' , 'Sarah' , ' Aaliyah' , ' Anna' , ' Arianna' , ' Ellie' , ' Natalie' , ' Isabelle' , ' Lillian' , ' Evelyn' , ' Elizabeth' , ' Lyla' , ' Lucy' , ' Claire' , ' Makayla' , ' Kylie' , ' Audrey',' Maya' , ' Leah' , ' Gabriella' , ' Annabelle' , ' Savannah' , ' Nora' , ' Reagan' , ' Scarlett' , ' Samantha' , ' Alyssa' , ' Allison' , ' Elena' , ' Stella' , ' Alexis' , ' Victoria' , ' Aria' , ' Molly' , ' Maria' , ' Bailey' , ' Sydney' , ' Bella' , ' Mila' , ' Taylor' , ' Kayla' , ' Eva' , ' Jasmine' , ' Gianna' , ' Alexandra' , ' Julia' , ' Eliana' , ' Kennedy' , ' Brianna' , ' Ruby' , ' Lauren' , ' Alice' , ' Violet' , ' Kendall' , ' Morgan' , ' Caroline' , ' Piper' , ' Brooke' , ' Elise' , ' Alexa' , ' Sienna' , ' Reese' , ' Clara' , 'Paige' , ' Kate' , ' Nevaeh' , ' Sadie' , ' Quinn' , ' Isla' , ' Eleanor']

male_names = ['Aiden' , ' Jackson' , ' Ethan' , ' Liam' , ' Mason' , ' Noah' , ' Lucas' , ' Jacob' , ' Jayden' , ' Jack' , ' Logan' , ' Ryan' , ' Caleb' , ' Benjamin' , ' William' , ' Michael' , 'Alexander' , ' Elijah' , ' Matthew' , ' Dylan' , ' James' , ' Owen' , ' Connor' , ' Brayden' , ' Carter' , ' Landon' , ' Joshua' , ' Luke' , ' Daniel' , ' Gabriel' , ' Nicholas' , ' Nathan' , ' Oliver' , ' Henry' , ' Andrew' , ' Gavin' , ' Cameron' , ' Eli' , ' Max' , ' Isaac' , ' Evan' , ' Samuel' , ' Grayson' , ' Tyler' , ' Zachary' , ' Wyatt' , ' Joseph' , ' Charlie' , 'Hunter' , ' David' , ' Anthony' , ' Christian' , ' Colton' , ' Thomas' , ' Dominic' , ' Austin' , ' John' , ' Sebastian' , ' Cooper' , ' Levi' , ' Parker' , ' Isaiah' , ' Chase' , ' Blake',' Aaron' , ' Alex' , ' Adam' , ' Tristan' , ' Julian' , ' Jonathan' , ' Christopher' , ' Jace' , ' Nolan' , ' Miles' , ' Jordan' , ' Carson' , ' Colin' , ' Ian' , ' Riley' , ' Xavier', ' Hudson' , ' Adrian' , ' Cole' , ' Brody' , ' Leo' , ' Jake' , ' Bentley' , ' Sean' , ' Jeremiah' , ' Asher' , ' Nathaniel' , ' Micah' , ' Jason' , ' Ryder' , ' Declan' , ' Hayden', ' Brandon' , ' Easton' , ' Lincoln' , ' Harrison']


personnel_types = {"Physician" : ('Nurse', 'Registered Nurse', 'Doctor', 'Surgeon', 'Cheif Surgeon'), "Engineer" : ('Assistant Engineer', 'Associate Engineer', 'Engineer', 'Senior Engineer', 'Cheif Engineer'), "Scientist" : ('Lab Tech',  'Lab Professor',  'Scientist', 'Senior Scientist', 'Chief Scientist'), "Instructor" : ('Instructor', 'Lecturer', 'Teacher', 'Senior Teacher', 'Professor'), "Mechanic" : ('Apprentice', 'Journeyman', 'Mechanic', 'Senior Mechanic', 'Chief Mechanic'), "Pilot" : ('First Lieutenant', 'Second Lieutenant', 'Captain', 'Major', 'Lieutenant Colonel')}


class CreatePersonnel(object):
	# Everything that can be created on a ship, or a planet, will be included in here.
	
	def __init__(self):
		self.item = "Personnel"
		self.health = 150
		self.indiscretion = 0.25 * random.uniform(1,3)
		self.luck = random.uniform(.125,.75)
		self.assigned = "Unassigned"
		self.age = random.randint(20,35)
		self.location = "None"
		
	def setPersonnelName(self):
		self.gender = ['M', 'F']
		self.gender = random.choice(self.gender)
		if self.gender == "M":
			self.name = random.choice(male_names)
		else:
			self.name = random.choice(female_names)
			
		return self.gender, self.name
	
		
	def setPersonnelType(self):
		self.chose_type = ['Physician', 'Engineer', 'Scientist', 'Instructor', 'Mechanic', 'Pilot']
		self.chosen_type = random.choice(self.chose_type)
		return self.chosen_type
		
	def setPersonnelLocation(self):
		self.location = ['media_room', 'mess_hall', 'dorm']
		self.location = random.choice(self.location)
		return self.location
		
	def setPersonnelLevel(self):
		self.level = random.randint(1,5)
		return self.level
		
	def setPersonnelSkill(self):
		self.personlevel = self.setPersonnelLevel()
		self.skill = int(random.uniform(0,1)*100*self.personlevel)
		return self.skill
		
	def createNewPersonnel(self, **kwargs):
		try:
			if u_id:
				pass
				
		except:
			self.u_id = ""
			self.type = self.setPersonnelType()
			self.level = self.setPersonnelLevel()
			self.title = personnel_types[self.type][self.level]
			self.name = self.setPersonnelName()[1]
			self.gender = self.setPersonnelName()[0]
			self.location = self.setPersonnelLocation()
			self.skill = self.setPersonnelSkill()
			
			self.insertToDb = db.player_items.insert({'name' : self.name, 'item' : self.item, 'type' : self.type, 'title' : self.title, 'gender' : self.gender, 'indiscretion' : self.indiscretion, 'health' : self.health, 'u_id' : self.u_id, 'skill' : self.skill,'timestamp' : now, 'created' : seconds, 'location' : self.location, 'luck' : self.luck, 'assigned' : self.assigned, 'age' : self.age})
			
			return self.insertToDb
		
		

		
		
		
	
		



		
if __name__ == '__main__':
	a = CreatePersonnel()
	test = a.createNewPersonnel()
	print test

