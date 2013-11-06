import pymongo
import time
import math


db = pymongo.Connection('localhost',27017).bbarnes_test


earth = db.universe.find_one({'name' : "Earth"})

x = earth['x_pos']
y = earth['y_pos']
r = earth['distance_from_star']
name = earth['name']
id = earth['_id']
parent_id = earth['parent_id']

parent = db.universe.find_one({ '_id' : parent_id})

star_x = parent['x_pos']
star_y = parent['y_pos']


print "x is ",x
print "y is ",y
print "radius is ",r
print "planet in question is " ,name

print "its starting at " , x,y

def x_increase():

	earth = db.universe.find_one({'name' : "Earth"})

	x = earth['x_pos']
	y = earth['y_pos']
	r = earth['distance_from_star']
	name = earth['name']
	id = earth['_id']
	
	
	while True:

		if x == y and x > star_x or x > star_x  and -x < y and x > y:
			y -=1
			x = round(math.sqrt(math.pow(r,2)-math.pow(y,2)))
			db.universe.update({'_id' : id}, {"$set": {'x_pos' : x}})
			db.universe.update({'_id' : id}, {"$set": {'y_pos' : y}})
			# print x,y
			# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,1,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %( x, y)
			time.sleep(1)
			
		elif -x == y and x >= star_x or x> star_x and x > y or y< star_y and x > y: 
			x -=1
			y = round(math.sqrt(math.pow(r,2)-math.pow(x,2)))
			y = y*-1
			db.universe.update({'_id' : id}, {"$set": {'x_pos' : x}})
			db.universe.update({'_id' : id}, {"$set": {'y_pos' : y}})
			# print x,y
			# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,1,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %( x, y)
			time.sleep(1)
			
			
			
		elif x == y and y < star_y or x < y and x < star_x and x < -y:
			y +=1
			x = round(math.sqrt(math.pow(r,2)-math.pow(y,2)))
			x = x * -1
			db.universe.update({'_id' : id}, {"$set": {'x_pos' : x}})
			db.universe.update({'_id' : id}, {"$set": {'y_pos' : y}})
			# print x,y
			# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,1,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %( x, y)
			time.sleep(1)

			
		elif x == -y and x < star_x or x < y and x < star_x :
			x +=1
			y = round(math.sqrt(math.pow(r,2)-math.pow(x,2)))
			db.universe.update({'_id' : id}, {"$set": {'x_pos' : x}})
			db.universe.update({'_id' : id}, {"$set": {'y_pos' : y}})
			# x = x * -1
			# print  x,y
			# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,1,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %( x, y)
			time.sleep(1)
	
		elif x == star_x or x > star_x and x < y:
			x +=1
			y = round(math.sqrt(math.pow(r,2)-math.pow(x,2)))
			db.universe.update({'_id' : id}, {"$set": {'x_pos' : x}})
			db.universe.update({'_id' : id}, {"$set": {'y_pos' : y}})
			# print x,y
			# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,1,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %( x, y)
			time.sleep(1)
x_increase()

	
	


# for d in range(100):
	# if x < r and != y:
		# x +=1
		# y = round(math.sqrt(math.pow(r,2)-math.pow(x,2)))
		# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,1,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %( x, y)
	
	# elif x = y:


	
	# if x == r:
		# for e in range(-r,r):
			# x -=1
			# y = round(math.sqrt(math.pow(r,2)-math.pow(x,2)))
			# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,3,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %( x, y)
		
		# db.universe.update({'_id' : id}, {"$set": {'x_pos' : x}})
		# db.universe.update({'_id' : id}, {"$set": {'y_pos' : y}})
	