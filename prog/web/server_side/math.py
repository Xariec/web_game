import pymongo
import time
import math
import datetime
from datetime import datetime


t = 0

op = 792

r = 92

p = 2*math.pi

planet_diameter = 4878
volume = 1.33*math.pi*math.pow(planet_diameter/2,3)

print volume




for d in range(20):
	t +=50
	x = round(r*math.sin(math.fmod(t,op)/op*p))
	y = round(r*math.cos(math.fmod(t,op)/op*p))
	print t
	print x,y
	print "\n"
