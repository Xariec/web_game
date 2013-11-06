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



def a_favor_vs(a_vs, d_vs):
	a_kill_count = 0
	d_kill_count = 0
	for d in range(len(a_vs)):
		dmg = 0
		cannons = db.player_items.find({'item' : "Artillery", 'type' : "Cannon" , 'p_id' : a_vs[d]})
		missiles = db.player_items.find({'item' : "Artillery", 'type' : "Missile" , 'p_id' : a_vs[d]}).limit(random.randint(0,2))
		for a in cannons:
			dmg += int(a['caliber']*a['rps']*random.uniform((a['accuracy']-.25), (a['accuracy']+.25))*random.uniform(.125,.75))/5
		for b in missiles:
			dmg += int(b['warhead']*random.uniform((b['accuracy']-.125), (b['accuracy']+.125))*random.uniform(.125,.75))
			missile_fired = db.player_items.remove({'_id': b['_id']})
			print "Attacker fired missile"
		try:
			defender_health = db.player_items.find_one({'_id' : d_vs[d]})['health']
			d_new_health = defender_health - dmg
			if d_new_health <= 0:
				db.player_items.remove({'_id' : d_vs[d]})
				print "removed Defender:", d_vs[d]
				a_kill_count +=1
			else:
				db.player_items.update({'_id' : d_vs[d]}, {"$set" : {'health' : d_new_health}})
				print "defender %r health updated to %d" %(d_vs[d], d_new_health)
				dmg = 0
				cannons = db.player_items.find({'item' : "Artillery", 'type' : "Cannon" , 'p_id' : d_vs[d]})
				missiles = db.player_items.find({'item' : "Artillery", 'type' : "Missile" , 'p_id' : d_vs[d]}).limit(random.randint(0,2))
				for a in cannons:
					dmg += int((a['caliber']*a['rps']*random.uniform((a['accuracy']-.25), (a['accuracy']+.25))*random.uniform(.125,.75)))
				for b in missiles:
					dmg += int(b['warhead']*random.uniform((b['accuracy']-.125), (b['accuracy']+.125))*random.uniform(.125,.75))
					missile_fired = db.player_items.remove({'_id': b['_id']})
					print "Defender fired missile"
				try:
					attacker_health = db.player_items.find_one({'_id' : a_vs[d]})['health']
					a_new_health = attacker_health - dmg
					if a_new_health <= 0:
						db.player_items.remove({'_id' : a_vs[d]})
						print "removed Attacker:", a_vs[d]
						d_kill_count +=1
					else:
						db.player_items.update({'_id' : a_vs[d]}, {"$set" : {'health' : a_new_health}})
						print "attacker %r health updated to %d" %(a_vs[d], a_new_health)
				except:
					continue
		except:
			continue 
	
	print "Attackers kill count : " , a_kill_count
	print "Defenders kill count : " , d_kill_count

def d_favor_vs(a_vs, d_vs):
	a_kill_count = 0
	d_kill_count = 0
	for d in range(len(d_vs)):
		dmg = 0
		cannons = db.player_items.find({'item' : "Artillery", 'type' : "Cannon" , 'p_id' : d_vs[d]})
		missiles = db.player_items.find({'item' : "Artillery", 'type' : "Missile" , 'p_id' : d_vs[d]}).limit(random.randint(0,2))
		for a in cannons:
			dmg += int(a['caliber']*a['rps']*random.uniform((a['accuracy']-.25), (a['accuracy']+.25))*random.uniform(.125,.75))/5
		for b in missiles:
			dmg += int(b['warhead']*random.uniform((b['accuracy']-.125), (b['accuracy']+.125))*random.uniform(.125,.75))
			missile_fired = db.player_items.remove({'_id': b['_id']})
			print "Defender fired missile"
		try:
			attacker_health = db.player_items.find_one({'_id' : a_vs[d]})['health']
			a_new_health = attacker_health - dmg
			if a_new_health <= 0:
				db.player_items.remove({'_id' : a_vs[d]})
				print "removed Attacker:", a_vs[d]
				d_kill_count +=1
			else:
				db.player_items.update({'_id' : a_vs[d]}, {"$set" : {'health' : a_new_health}})
				print "Attacker %r health updated to %d" %(a_vs[d], a_new_health)
				dmg = 0
				cannons = db.player_items.find({'item' : "Artillery", 'type' : "Cannon" , 'p_id' : a_vs[d]})
				missiles = db.player_items.find({'item' : "Artillery", 'type' : "Missile" , 'p_id' : a_vs[d]}).limit(random.randint(0,2))
				for a in cannons:
					dmg += int((a['caliber']*a['rps']*random.uniform((a['accuracy']-.25), (a['accuracy']+.25))*random.uniform(.125,.75)))
				for b in missiles:
					dmg += int(b['warhead']*random.uniform((b['accuracy']-.125), (b['accuracy']+.125))*random.uniform(.125,.75))
					missile_fired = db.player_items.remove({'_id': b['_id']})
					print "Attacker fired missile"
				try:
					defender_health = db.player_items.find_one({'_id' : d_vs[d]})['health']
					d_new_health = defender_health - dmg
					if d_new_health <= 0:
						db.player_items.remove({'_id' : d_vs[d]})
						print "removed Defender:", d_vs[d]
						a_kill_count +=1
					else:
						db.player_items.update({'_id' : d_vs[d]}, {"$set" : {'health' : d_new_health}})
						print "Defender %r health updated to %d" %(d_vs[d], d_new_health)
				except:
					continue
		except:
			continue
					
	print "Attackers kill count : " , a_kill_count
	print "Defenders kill count : " , d_kill_count


def battle(attacker_id, defender_id):
	rounds = 5
	for a in range(rounds):
		a_ship_id = []
		d_ship_id = []
		a_ships = db.player_items.find({'u_id' : attacker_id, 'item' : "Ship", 'type' : "Fighter"})
		d_ships = db.player_items.find({'u_id' : defender_id, 'item' : "Ship", 'type' : "Fighter"})
		for a in a_ships: # Collects all the data about the attackers fleet
			a_ship_id.append(a['_id'])
		for b in d_ships:
			d_ship_id.append(b['_id'])
		attack_fleet_size = len(a_ship_id)
		defend_fleet_size = len(d_ship_id)
		print "Attack_fleet =", attack_fleet_size
		print "Defend_fleet =", defend_fleet_size
		count = 0
		if attack_fleet_size > 0 and defend_fleet_size > 0:
			if attack_fleet_size > defend_fleet_size:
				a_vs = [] # ObjectID's of all the attacking ships
				d_vs = [] # ObjectID's of all the defending ships
				left_over = attack_fleet_size-defend_fleet_size
				for b in range(defend_fleet_size):
					a_vs.append(a_ship_id[b])
					d_vs.append(d_ship_id[b])
					count +=1
				for c in range(left_over):
					index_adjustment = defend_fleet_size+c
					random_selection = random.randint(0,defend_fleet_size-1)
					a_vs.append(a_ship_id[index_adjustment])
					d_vs.append(d_ship_id[random_selection])
					count +=1
				for x in range(attack_fleet_size):
					print a_vs[x], d_vs[x]
				a_favor_vs(a_vs, d_vs)
				time.sleep(1)

			elif attack_fleet_size < defend_fleet_size:
				a_vs = [] # ObjectID's of all the attacking ships
				d_vs = [] # ObjectID's of all the defending ships
				left_over = defend_fleet_size - attack_fleet_size
				for b in range(attack_fleet_size):
					a_vs.append(a_ship_id[b])
					d_vs.append(d_ship_id[b])
					count +=1
				for c in range(left_over):
					index_adjustment = attack_fleet_size+c
					random_selection = random.randint(0,attack_fleet_size-1)
					a_vs.append(a_ship_id[random_selection])
					d_vs.append(d_ship_id[index_adjustment])
				for x in range(defend_fleet_size):
					print a_vs[x], d_vs[x]
				d_favor_vs(a_vs, d_vs)
				time.sleep(1)
					
				
						
			else:
				a_vs = [] # ObjectID's of all the attacking ships
				d_vs = [] # ObjectID's of all the defending ships
				for b in range(attack_fleet_size):
					a_vs.append(a_ship_id[b])
					d_vs.append(d_ship_id[b])
					count +=1
				for x in range(defend_fleet_size):
					print a_vs[x], d_vs[x]
				if random.randrange(0,10) >= 5:
					print "A"
					a_favor_vs(a_vs, d_vs)
					time.sleep(1)
				else:
					print "D"
					d_favor_vs(a_vs, d_vs)
					time.sleep(1)
				
		else:
			print "Battle Over"
		# print a_vs

		print
		time.sleep(1)

		
		
i = 1
x = 0
while x < i:
	setup.clear_db()
	setup.test("attacker")
	setup.test("defender")
	attacker_id = db.users.find_one({'username' : "attacker"})['_id']
	defender_id = db.users.find_one({'username' : "defender"})['_id']
	battle(attacker_id, defender_id)
	x +=1







