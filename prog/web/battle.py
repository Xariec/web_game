import pymongo
import math
import time
import datetime
import random
import test_setup


db = pymongo.Connection('localhost', 27017).game

now = datetime.datetime.now()  # Gets the current time.
day_of_year = datetime.datetime.now().timetuple().tm_yday
# convert the time to an integer we can use for checking how much time has passed.
days = (now.year * 365) + day_of_year + (now.year/4)
hours = days * 24 + now.hour
minutes = hours *60 + now.minute
seconds = minutes * 60 + now.second # Seconds, fairly accurate depiction of time since the year of 0001







def battle(attacker_id, defender_id):
	rounds = 3
	for a in range(rounds):
		time.sleep(1)
		# A list of all the attributes of the attacking fleet. Everything from them will be predominated with an a_
		a_ship_id = []
		a_health = {}
		a_name = {}
		a_cannon = {}
		a_missile = {}
		# A list of all the attributes of the defending fleet. Everything from them will be predominated with a d_
		d_ship_id = []
		d_health = {}
		d_name = {}
		d_cannon = {}
		d_missile = {}
		
		a_ships = db.player_items.find({'u_id' : attacker_id, 'item' : "Ship"})
		for a in a_ships: # Collects all the data about the attackers fleet
			if a['type'] == "Fighter":
				p_id = a['_id']
				a_ship_id.append(p_id)
				a_health[a['_id']] = a['health']
				a_name[a['_id']] = a['name']
				cannons = db.player_items.find({'item' : "Artillery", 'type' : "Cannon" , 'p_id' : a['_id']})
				cannon_dmg = 0
				for b in cannons:
					dmg = int(b['caliber']*b['rps']*random.uniform((b['accuracy']-.25), (b['accuracy']+.125)))
					luck = random.uniform(.125,.75)
					dmg = int(dmg*luck)
					cannon_dmg += dmg
				missiles = db.player_items.find({'item' : "Artillery", 'type' : "Missile" , 'p_id' : a['_id']}).limit(2)
				missile_dmg = 0
				for c in missiles:
					dmg = int(c['warhead']*random.uniform((b['accuracy']-.125), (b['accuracy']+.125)))
					missile_dmg += dmg
					db.player_items.remove({'_id' : c['_id']})
				a_cannon[a['_id']] = cannon_dmg
				a_missile[a['_id']] = missile_dmg
				
		d_ships = db.player_items.find({'u_id' : defender_id, 'item' : "Ship"})
		for a in d_ships: # Collects all the data about the defenders fleet
			if a['type'] == "Fighter":
				p_id = a['_id']
				d_ship_id.append(p_id)
				d_health[a['_id']] = a['health']
				d_name[a['_id']] = a['name']
				cannons = db.player_items.find({'item' : "Artillery", 'type' : "Cannon" , 'p_id' : a['_id']})
				cannon_dmg = 0
				for b in cannons:
					dmg = int(b['caliber']*b['rps']*random.uniform((b['accuracy']-.25), (b['accuracy']+.125)))
					luck = random.uniform(.125,.75)
					dmg = int(dmg*luck)
					cannon_dmg += dmg
				missiles = db.player_items.find({'item' : "Artillery", 'type' : "Missile" , 'p_id' : a['_id']}).limit(2)
				missile_dmg = 0
				for c in missiles:
					dmg = int(c['warhead']*random.uniform((b['accuracy']-.125), (b['accuracy']+.125)))
					missile_dmg += dmg
					db.player_items.remove({'_id' : c['_id']})
					
				d_cannon[a['_id']] = cannon_dmg
				d_missile[a['_id']] = missile_dmg		
		
		
		a_vs = [] # ObjectID's of all the attacking ships
		d_vs = [] # ObjectID's of all the defending ships
		attack_fleet_size = len(a_ship_id)
		defend_fleet_size = len(d_ship_id)
		print "Attack_fleet =", attack_fleet_size
		print "Defend_fleet =", defend_fleet_size
		count = 0
		a_kill_count = 0
		d_kill_count = 0
		if attack_fleet_size > 0 and defend_fleet_size > 0:
			if attack_fleet_size > defend_fleet_size:
				left_over = attack_fleet_size-defend_fleet_size
				# print "There are %d additional targets for the attack fleet to find" %left_over
				for b in range(defend_fleet_size):
					a_vs.append(a_ship_id[b])
					d_vs.append(d_ship_id[b])
					count +=1
				for c in range(left_over):
					index_adjustment = defend_fleet_size+c
					# print index_adjustment
					random_selection = random.randint(0,defend_fleet_size-1)
					# print "Random defense ship chosen = ", random_selection
					a_vs.append(a_ship_id[index_adjustment])
					d_vs.append(d_ship_id[random_selection])
					count +=1
					
			elif attack_fleet_size < defend_fleet_size:
				left_over = defend_fleet_size - attack_fleet_size
				# print "There are %d additional targets for the defend fleet to find" %left_over 
				for b in range(attack_fleet_size):
					a_vs.append(a_ship_id[b])
					d_vs.append(d_ship_id[b])
					count +=1
				for c in range(left_over):
					index_adjustment = attack_fleet_size+c
					# print index_adjustment
					random_selection = random.randint(0,attack_fleet_size-1)
					# print "Random defense ship chosen = ", random_selection
					a_vs.append(a_ship_id[random_selection])
					d_vs.append(d_ship_id[index_adjustment])
			else:
				for b in range(attack_fleet_size):
					a_vs.append(a_ship_id[b])
					d_vs.append(d_ship_id[b])
					count +=1
					
			print "Attacker, Defender, attack damage, defender's health"
			for n in range(attack_fleet_size):
				attacker_damage = a_cannon[a_vs[n]]+a_missile[a_vs[n]]
				defender_health = d_health[d_vs[n]]-attacker_damage
				print "%r , %r , %r, %r"%(a_vs[n], d_vs[n], attacker_damage, defender_health)
				# print attacker_damage, defender_health
				if defender_health <= 0:
					db.player_items.remove({'_id' : d_vs[n]})
					del d_vs[n]
					defend_fleet_size = len(d_vs)
					a_kill_count +=1
					# print "%r was lost in battle while defending!"%d_vs[n]
				else:
					db.player_items.update({'_id' : d_vs[n]}, {"$set" : {'health' : defender_health}})
			

			
			# for n in range(defend_fleet_size):	
			print "Defender, Attacker, defend damage, attacker's health"
			for n in range(defend_fleet_size):
				defender_damage = d_cannon[d_vs[n]]+d_missile[d_vs[n]]
				attacker_health = a_health[a_vs[n]]-defender_damage
				print "%r , %r , %r, %r"%(d_vs[n], a_vs[n], defender_damage, attacker_health)
				# print defender_damage, attacker_health
				if attacker_health <= 0:
					db.player_items.remove({'_id' : a_vs[n]})
					d_kill_count +=1
					# print "%r was lost in battle while attacking!" %a_vs[n]
				else:
					db.player_items.update({'_id' : a_vs[n]}, {"$set" : {'health' : attacker_health}})
				
		else:
			print "Battle Over"
		# print a_vs
		print "Attacker Kill Count: ", a_kill_count
		print "Defender Kill Count: ",d_kill_count
		print
		# print 
		# print d_vs

		
		
i = 1
x = 0
while x < i:
	test_setup.clear_db()
	test_setup.test("attacker")
	test_setup.test("defender")
	attacker_id = db.users.find_one({'username' : "attacker"})['_id']
	defender_id = db.users.find_one({'username' : "defender"})['_id']
	battle(attacker_id, defender_id)
	x +=1







