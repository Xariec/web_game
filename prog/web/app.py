import web
import pymongo
import time
import math
import users
import db_updates
import session
import mongo_utils
from session import MongoStore
import templates
from templates import render
import lang.en as lang
import forms
import pprint
import datetime
import db_actions
import random
from bson.objectid import ObjectId
import web_actions


web.config.debug = False

db = pymongo.Connection('localhost', 27017).game

# render = web.template.render('templates/')

urls = (
	'/','Index',
	'/login/','Login',
	'/logout/','Logout',
    '/register/', 'Register',
	'/default/','default',
	'/command/','command',
	'/personnel/','personnel',
	'/fleet/','fleet',
	'/operations/', 'Operations',
	)
  
app = web.application(urls, globals())
session = web.session.Session(app, MongoStore(db, 'sessions'))
users.collection = db.users
users.session = session


now = datetime.datetime.now()  # Gets the current time.
day_of_year = datetime.datetime.now().timetuple().tm_yday
# convert the time to an integer we can use for checking how much time has passed.
days = (now.year * 365) + day_of_year + (now.year/4)
hours = days * 24 + now.hour
minutes = hours *60 + now.minute
seconds = minutes * 60 + now.second
p = 2*math.pi	

current_user = "blah"

class Index(object): 
    def GET(self): 
		return render('home.html')


class Login(object):
	def GET(self):
		next = web.input(_method='GET').get(' next' , '/default/' )
		return render('login.html', next=next)
		
	def POST(self):
		post = web.input(_method='POST')
		errors = {}
		try:
			user = users.authenticate(post['username'], post['password'])
			if user:
				users.login(user)
			else:
				errors['__all__'] = lang.AUTH_FAILURE
		except KeyError:
			errors['__all__'] = lang.AUTH_FAILURE
			
		if errors:
			return render('login.html', errors=errors, next=post.get('next'))
		else:
			# current_user = user
			return web.seeother(post.get('next' , '/default/' ))
			
			
class Register(object):
    def GET(self):
        return render('register.html')

    def POST(self):
        post = web.input(_method='POST')
        errors = {}
        username = forms.get_or_add_error(post, 'username', errors, lang.NO_FIELD_SUPPLIED('username'))
        password = forms.get_or_add_error(post, 'password', errors, lang.NO_FIELD_SUPPLIED('password'))
        password_again = forms.get_or_add_error(post, 'password_again', errors, lang.NO_FIELD_SUPPLIED('password again'))

        forms.validate(errors, 'password_again', lang.PASSWORDS_DONT_MATCH, lambda p,p2: p == p2, (password, password_again))

        if username is not None:
            forms.validate(errors, 'username', lang.FIELD_MUST_BE_LEN('Username', 3), lambda u: len(u) >= 3, (username,))
            forms.validate(errors, 'username', lang.USERNAME_TAKEN, lambda u: not bool(db.users.find_one({'username':u})), (username,))
        if password is not None:
            forms.validate(errors, 'password', lang.FIELD_MUST_BE_LEN('Password', 5), lambda p: len(p) >= 5, (password,))            
            
        if errors:
			return render('register.html', errors=errors)
        else:
            users.register(username=username, password=users.pswd(password))
            web.seeother('/login/')            

class Logout(object):
    def GET(self):
        users.logout()
        return web.seeother('/')




class default(object):
	@users.login_required
	def GET(self):
		u_id = users.get_user()['_id'] # Lets find out who we are
		ship = db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
		return render('default.html', ship=ship)

class command(object):
	@users.login_required
	def GET(self):
		now = datetime.datetime.now()
		# lvl = 1500000000
		lvl = 15000000000
		scale = lvl/1500
		u_id = users.get_user()['_id']
		p_id= db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
		x = int(p_id['x'])
		y = int(p_id['y'])
		warp_drive = db_actions.display_health("warp_drive", p_id['_id'])
		engine = db_actions.display_health("engine", p_id['_id'])
		reactor = db_actions.display_health("reactor", p_id['_id'])
		position = db.universe.find({"x_pos": {"$gte": x - lvl , "$lte": x + lvl},"y_pos": {"$gte": y - lvl, "$lte": y + lvl}})
		# position = db.universe.find().limit(1000)
		objects_name = []
		objects_type = []
		objects_x = []
		objects_y = []
		objects_lable_x = []
		objects_lable_y = []
		objects_color = []
		objects_size = []
		count = 0
		for x in position:
			print x['name']
			objects_name.append(x['name'])
			objects_type.append(x['item'])
			objects_x.append((x['x_pos']-int(p_id['x']))/scale)
			objects_y.append((x['y_pos']-int(p_id['y']))/scale-65)
			objects_lable_x.append((x['x_pos']-int(p_id['x']))/scale+10)
			objects_lable_y.append((x['y_pos']-int(p_id['y']))/scale-70)
			if x['item'] == "planet":
				objects_size.append(1)
				objects_color.append('green')
			elif x['item'] == "star":
				# objects_size.append(x['diameter']/lvl)
				objects_size.append(5)
				objects_color.append('yellow')
			else:
				objects_size.append(1)
				objects_color.append('red')
			count += 1
			
		return render('command.html', warp_drive = warp_drive, engine = engine, ship = p_id, name = objects_name, item = objects_type, x = objects_x, y = objects_y, count = count, lable_x = objects_lable_x, lable_y = objects_lable_y, reactor = reactor, now = now, color = objects_color, objects_size = objects_size)

	
	def POST(self):
		safe = 500
		now = datetime.datetime.now()
		u_id = users.get_user()['_id']
		p_id= db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})	
		post = web.input(_method='POST')
		movement = 100000000
		if post['submit'] == "Warp":
			print post['x'], post['y']
			new_position = db.universe.find({"x_pos": {"$gte": int(post['x']) - safe , "$lte": int(post['x']) + safe},"y_pos": {"$gte": int(post['y']) - safe, "$lte": int(post['y']) + safe}})
			if new_position == None:
				status = "Computer cant calculate Warp, please try a different destination"
				return web.seeother('/command/')
			else:
				db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : post['x'], 'y' : post['y']}})
				return web.seeother('/command/')
		elif post['submit'] == "Down":
			y = int(p_id['y'])-movement
			db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'y' : y}})
			return web.seeother('/command/')
		elif post['submit'] == "Up":
			y = int(p_id['y'])+movement
			db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'y' : y}})
			return web.seeother('/command/')
		elif post['submit'] == "Left":
			x = int(p_id['x'])-movement
			db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : x}})
			return web.seeother('/command/')
		elif post['submit'] == "Right":
			x = int(p_id['x'])+movement
			db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : x}})
			return web.seeother('/command/')
				

class personnel(object):
	@users.login_required
	def GET(self):
		u_id = users.get_user()['_id']
		people = web_actions.Population()
		list = people.getAllPersonnel(u_id)[0]
		button = people.getAllPersonnel(u_id)[1]
		return render('all_personnel.html', list = list, button = button)

		
	def POST(self):
		u_id = users.get_user()['_id']
		post = web.input(_method='POST')
		try:
			button = post['button']
		except:
			print post
		if button:
			people = web_actions.Population()
			single = people.getOnePersonnel(button, u_id)
			button = people.getAllPersonnel(u_id)[1]
			print single
			return render('personnel.html', button = button, single = single)
		

		
class Operations(object):
	@users.login_required
	def GET(self):
		return render('operations.html')
		
		
		
		
class fleet(object):
	@users.login_required
	def GET(self):
		u_id = users.get_user()['_id']
		print u_id
		fleet = db.player_items.find({'u_id' : u_id, 'item' : "Ship"})
		ship_id = []
		name = []
		health = []
		type = []
		ship_fleet = []
		list_fleet = []
		count = 0
		list = 0
		for x in fleet:
			ship_id.append(x['_id'])
			name.append(x['name'])
			type.append(x['type'])
			health.append(x['health'])
			ship_fleet.append(x['fleet'])
			if (x['fleet'] in list_fleet) == False:
				list_fleet.append(x['fleet'])
				list +=1
			count += 1
		return render('fleet.html', name=name, type=type, health = health, count=count, list = list, list_fleet = list_fleet, ship_fleet = ship_fleet, ship_id = ship_id)

	def POST(self):
		post = web.input(_method='POST')
		submit = post['submit']
		if submit == "select":
			print submit
		elif submit == "update":
			ship_id = post['id']
			print ship_id
			ship_id = ObjectId(ship_id)
			fleet = post['fleet']
			# fleet_update = db.player_items.find_one({'_id' : ship_id})
			fleet_update = db.player_items.update({'_id' : ship_id}, {"$set" :{'fleet' : "Blah"}})
			if fleet_update:
				print fleet_update
			else:
				print "Didn't work.... sooo sorry!"
				print fleet_update, ship_id


class warps(object):
	@users.login_required
	def GET(self):
		query = "Unknown"
		return render('warps.html', query=query)
			
			
	def POST(self):
		post = web.input(_method='POST')
		name = post['list']
		cord = name.split(',')
		x = cord[0]
		y = cord[1]
		test = db.warps.find_one({'x_origin' : int(x), 'y_origin' : int(y)})
		query = test['player']
		# query = x
		return render('warps.html', query=query)
		
		


if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
