## -*- coding: utf-8 -*-

import web
import hashlib
import pymongo

db = pymongo.Connection('localhost', 27017).cc

def update_gate(x, y):
	player = db.gate.find_one({'x_origin' : x, 'y_origin' : y})
	if player != None:
		db.gate.update({'_id' : player['_id']}, {"$set": {'player' : player}})
	else:
		return None
	# return player if player else None
 