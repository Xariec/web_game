import datetime
import time


now = datetime.datetime.now()
day_of_year = now.timetuple().tm_yday
# convert the time to an integer we can use for checking how much time has passed.
days = (now.year * 365) + day_of_year + (now.year/4)
hours = days * 24 + now.hour
minutes = hours *60 + now.minute
seconds = minutes * 60 + now.second





compartments = ['Engine Room', 'Mechanics Bay', 'Pilots Lounge', 'Right Hanger', 'Left Hanger', 'Cargo Bay', 'Communications Center', 'Operations Center', 'Battle Center','Weapons Center', 'Media Room', 'Mess Hall', 'Dorms', 'Sick Bay', 'Research Lab', 'Engineering Lab', 'Tech Lab']

for x in range(len(compartments)):
	print "'"+compartments[x]+"'"

	
def aFunction():
	test = 1
	return test

test = [(aFunction())]


print test