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
		lvl = 100000000
		u_id = users.get_user()['_id']
		p_id= db.player_items.find_one({'u_id' : u_id, 'name' : "GCBS-371"})
		x = int(p_id['x'])
		y = int(p_id['y'])
		warp_drive = db_actions.display_health("warp_drive", p_id['_id'])
		engine = db_actions.display_health("engine", p_id['_id'])
		reactor = db_actions.display_health("reactor", p_id['_id'])
		# for a in db.universe.find({"x_pos": {"$gte": int(p_id['x']) - lvl , "$lte": int(p_id['x']) + lvl},"y_pos": {"$gte": int(p_id['y']) - lvl, "$lte": int(p_id['y']) + lvl}}):
			# if a['item'] == "planet":
				# print a['name']
				# # t = seconds - a['created'] #subtract current seconds from seconds of the moment it was created
				# # t = seconds - a['created']
				# t = random.randrange(13546985622,63546985622)
				# print t
				# op = a['op'] # orbital period
				# r = a['distance'] * 100000000
				# # Note, add in accordance to the star, as that is the center in this case.
				# star = db.universe.find_one({'_id' : a['p_id']})
				# new_x = round(r*math.sin(math.fmod(t,op)/op*p))/100000000
				# new_y = round(r*math.cos(math.fmod(t,op)/op*p))/100000000
				# new_x = new_x + star['x_pos']
				# new_y = new_y + star['y_pos']
				# print new_x, new_y
				# db.universe.update({'_id' : a['_id']}, {"$set": {'x_pos' : int(new_x), 'y_pos' : int(new_y)}})
				
		# position = db.universe.find({"x_pos": {"$gte": x - lvl , "$lte": x + lvl},"y_pos": {"$gte": y - lvl, "$lte": y + lvl}})
		position = db.universe.find().limit(1000)
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
			objects_x.append((x['x_pos']-int(p_id['x']))/lvl)
			objects_y.append((x['y_pos']-int(p_id['y']))/lvl-65)
			objects_lable_x.append((x['x_pos']-int(p_id['x']))/lvl+10)
			objects_lable_y.append((x['y_pos']-int(p_id['y']))/lvl-70)
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
		print post['x'], post['y']
		new_position = db.universe.find({"x_pos": {"$gte": int(post['x']) - safe , "$lte": int(post['x']) + safe},"y_pos": {"$gte": int(post['y']) - safe, "$lte": int(post['y']) + safe}})
		if new_position == None:
			status = "Computer cant calculate Warp, please try a different destination"
			return web.seeother('/command/')
		else:
			db.player_items.update({'u_id' : u_id, 'name' : "GCBS-371"}, {"$set": {'x' : post['x'], 'y' : post['y']}})
			return web.seeother('/command/')
		
class personnel(object):
	@users.login_required
	def GET(self):
		u_id = users.get_user()['_id']
		personnel = db.player_items.find({'u_id' : u_id, 'item' : "personnel"})
		
		name = []
		title = []
		skill = []
		health = []
		gender = []
		position = []
		location = []
		count = 0
		for x in personnel:
			name.append(x['name'])
			title.append(x['title'])
			skill.append(x['skill'])
			health.append(x['health'])
			gender.append(x['gender'])
			position.append(x['type'])
			location.append(x['location'])
			count += 1
		
		return render('personnel.html', name=name, position=position, location=location, count=count, title = title, skill = skill, health = health, gender = gender)

		


class fleet(object):
	@users.login_required
	def GET(self):
		u_id = users.get_user()['_id']
		fleet = db.player_items.find({'u_id' : u_id, 'item' : "Ship"})
		name = []
		health = []
		type = []
		ship_fleet = []
		list_fleet = []
		count = 0
		list = 0
		for x in fleet:
			name.append(x['name'])
			type.append(x['type'])
			health.append(x['health'])
			ship_fleet.append(x['fleet'])
			if (x['fleet'] in list_fleet) == False:
				list_fleet.append(x['fleet'])
				list +=1
			count += 1
		return render('fleet.html', name=name, type=type, health = health, count=count, list = list, list_fleet = list_fleet, ship_fleet = ship_fleet)

	def POST(self):
		post = web.input(_method='POST')
		submit = post['submit']
		# fleet_selected = post['list_fleets']
		# find_fleet = db.warps.find({'fleet' : fleet_selected})
		# name = []
		# health = []
		# type = []
		# list_fleet = []
		# count = 0
		# for x in find_fleet:
			# name.append(x['name'])
			# type.append(x['type'])
			# health.append(x['health'])
			# if (x['fleet'] in list_fleet) == False:
				# list_fleet.append(x['fleet'])
				# list +=1
			# count += 1
			

		# update_fleet = post['fleet']
		
		print "submit :", submit
		print "post :", post
		# print "fleet selected :", fleet_selected
		# print "update fleet :", update_fleet
		
		# list = 0	
		# list_x = []
		# list_y = []
		# gates = db.warps.find().sort(u'x_origin', -1)
		# for b in gates:
			# if ((b['x_origin'] in list_x) and (b['y_origin'] in list_y)) == False:
				# list_x.append(b['x_origin'])
				# list_y.append(b['y_origin'])
				# list +=1
				
		# return render('warps.html', x_origin = x, y_origin = y, x_dest = warped_x_dest, y_dest = warped_y_dest, count = count_warped, list_x = list_x, list_y = list_y, list = list)		

		
# class fleet(object):
	# @users.login_required
	# def GET(self):
		# u_id = users.get_user()['_id']
		# fleet = db.player_items.find({'u_id' : u_id, 'item' : "Ship"})
		# name = []
		# health = []
		# lvl = []
		# type = []
		# count = 0
		# for x in fleet:
			# name.append(x['name'])
			# type.append(x['type'])
			# health.append(x['health'])
			# lvl.append(x['lvl'])
			# count += 1
		
		# return render('fleet.html', name=name, type=type, health = health, count=count, lvl = lvl)


	# def POST(self):
		# post = web.input(_method='POST')
		# name = post['player']
		# x = post['x']
		# y = post['y']
		# search = db.gate.find_one({'x_origin' : int(x), 'y_origin' : int(y)})
		# if search is not None:
			# db.gate.update({'_id' : search['_id']}, {"$set": {'player' : name}})
			# return render('warp_gates.html')
		# else:
			# return search, name, x, y

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
