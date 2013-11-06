#!/usr/bin/env python
import pymongo
import random
import time
import bson
from bson.objectid import ObjectId
from sys import exit

db = pymongo.Connection('192.168.4.19', 27017).bbarnes_test

print "Welcome to Total Galaxy Anniliation!\n"
print "Please type in your User Name:"
# name = "Xariec"
name = raw_input("> ")
user = db.users.find_one({'name' : name})

def Intro():
	if user == None:
		print "It would appear %s, that we havent seen your face around here before. \nWould you like to start a new account? Y or N" %name
		new_user = raw_input("> ")
		if new_user == "Y":
			print "Thank you %s for creating an account with us. Now lets see if we cant get you set up." %name
			db.users.insert({'name' : name})
		elif new_user == "N":
			print "Thank you %s for stopping by" %name
			exit(0)
		else:
			print "I'm sorry but I don't understand that character. Please try again."
	else:
		print "Hello %s, Nice to see you again. Please wait while we pull up your your stats.\n" %name
		time.sleep(2)
		print "It will only be a minute.\n " 
		time.sleep(2)

Intro()		

		
		

	
user = db.users.find_one({'name' : name})	

id = "Object_id("+ user['_id'].__str__()+ ")"
time.sleep(2)
print "Good News %s,\nWe found your account.\nYour player ID is '%s'. \nWe will now look for your ship." %(user['name'],user['_id'].__str__())
time.sleep(2)


# print (user['name']+ ", "+ user['_id'].__str__())

location = db.universe.find_one({'player_id' : id})

start_planet = db.universe.find_one({'name' : "Earth"})
# print location

if location == None:
	print "It appears you where never assigned a ship."
	print "Please wait while we assign you a ship."
	time.sleep(2)
	db.universe.insert({'name' : user['name'], 'x_pos' : start_planet['x_pos']+1, 'y_pos' : start_planet['y_pos']+1, 'player_id' : id})
	time.sleep(2)
	location = db.universe.find_one({'player_id' : id})
	print "Thank you for your patience %s, your ship is located at... %d, %d "%(user['name'],location['x_pos'],location['y_pos'])
	print """
	A little bit about the area you are in... You where started out at a planet called Earth.
	Now while this might sound wonderfull as you are probably familiar with the archives state about Earth, remember that the fourth World War pretty much destroyed its surface. Life as you know it no longer lives on the planet, but instead in space stations that are orbiting the planet.
	
	The Ship we assigned you is a lvl 1 class BattelShip located in the docs of ISS AC-1997. As of now she isn't much, but i'm sure with a little TLC on your part you can have here surfing the galaxies in no time.
	
	Please follow me and I'll deliver you to your ship.:
	"""
	
else:
	print "You are located at... %d, %d " %(location['x_pos'],location['y_pos'])

location = db.universe.find_one({'player_id' : id})

x_pos = location['x_pos']
y_pos = location['y_pos']

config = {"close": 2500, "medium" : 36000, "far" : 100000}

def view_area(distance):
	front = y_pos + distance
	back = y_pos - distance
	left = x_pos - distance
	right = x_pos + distance
	position = db.universe.find({"x_pos": {"$gte": left, "$lte": right},"y_pos": {"$gte": back, "$lte": front}})

	for i in position:
		print i['name']+","+ i['x_pos'].__str__()+","+ i['y_pos'].__str__()	


print "What would you like to do?"
# action = "Scan"
action = raw_input("> ")

if action == "Scan":
	print "What level of a scan would you like to do?"
	print """
	A local scan is lvl 1
	A solar system scan is lvl 2
	A Galaxy scan is lvl 3
	"""
	print "Remember %s, each lvl of scan takes considerbly longer." %name
	lvl = raw_input("> ")
	if lvl == "1":
		time.sleep(2)
		view_area(config['close'])
	elif lvl == "2":
		time.sleep(5)
		view_area(config['medium'])
	elif lvl == "3":
		time.sleep(10)
		view_area(config['far'])
	else:
		print "You must select a scan lvl!"

