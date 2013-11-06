import random
import pymongo
import time
import string
import datetime
import math


db = pymongo.Connection('localhost', 27017).game


#                    Global Variables

# Set the time variables
now = datetime.datetime.now()  # Gets the current time.
day_of_year = datetime.datetime.now().timetuple().tm_yday
# convert the time to an integer we can use for checking how much time has passed.
days = (now.year * 365) + day_of_year + (now.year/4)
hours = days * 24 + now.hour
minutes = hours *60 + now.minute
# seconds = minutes * 60 + now.second # Seconds, fairly accurate depiction of time since the year of 0001
seconds = 0

# Solar unites for measurements 
g = 6.674 * math.pow(10,-11) # Gravitational constant
su = 1.989 * math.pow(10, 30) # Mass of our Sun, using this as a reference for other stars of different sizes.
au = 149597871
planet_diameter = random.randrange(2000,140000)
sr = 6.955 * math.pow(10,8) #Solar Radii in meters, Don't forget that this number needs to be divided by 1000 for our scale.







em = 6.972*math.pow(10,24) # Earth's mass, in kg

planet_classes = ('Terrestrial', 'Desert', 'Gas', 'Ice', 'Iron', 'Ocean')


iron_ore = {'Iron' : random.randint(10,100), 'Terrestrial' : random.randint(10,100), 'Gas' : random.randint(1, 2), 'Ice' : random.randint(5,30), 'Desert' : random.randint(10,50), 'Ocean' : random.randint(1,20)}

carbon_ore = {'Iron' : random.randint(10,100), 'Terrestrial' : random.randint(10,100), 'Gas' : random.randint(1, 2), 'Ice' : random.randint(5,30), 'Desert' : random.randint(10,50), 'Ocean' : random.randint(1,20)}

oxygen_ore = {'Iron' : random.randint(10,100), 'Terrestrial' : random.randint(10,100), 'Gas' : random.randint(1, 2), 'Ice' : random.randint(5,30), 'Desert' : random.randint(10,50), 'Ocean' : random.randint(1,20)}

h2o_ore = {'Iron' : random.randint(10,100), 'Terrestrial' : random.randint(10,100), 'Gas' : random.randint(1, 2), 'Ice' : random.randint(5,30), 'Desert' : random.randint(10,50), 'Ocean' : random.randint(1,20)}

deuterium_ore = {'Iron' : random.randint(10,100), 'Terrestrial' : random.randint(10,100), 'Gas' : random.randint(1, 2), 'Ice' : random.randint(5,30), 'Desert' : random.randint(10,50), 'Ocean' : random.randint(1,20)}

def zeus():
        name = "Sun"
        item = "star"
        x = 2629742
        y = 2629742
        solar_system_size = 590000
        star_type = "O"
        star_color = "Yellow White"
        diameter = sr*2
        s_mass = su
        p_id = db.universe.insert({'name' : name, 'item' : item , 'x_pos' : x, 'y_pos' : y, 'size' : solar_system_size, 'type' : star_type, 'color' : star_color, 'diameter' : diameter, 'mass' : s_mass, 'created' : seconds})

        for planet in ((580 , "Mercury", 4879, planet_classes[4],1, .05),
                                        (1080,"Venus",12100, planet_classes[1],1, .815),
                                        (1500,"Earth", 12742, planet_classes[0],1, 1),
                                        (2280,"Mars", 6792, planet_classes[1],1, .107),
                                        (7785,"Jupiter", 142981, planet_classes[2],0,318),
                                        (14300,"Saturn", 120536, planet_classes[2],0, 95),
                                        (28800,"Uranus", 51118, planet_classes[0],1, 14),
                                        (45000,"Neptune", 49500, planet_classes[0],1, 17),
                                        (59000,"Pluto", 2630, planet_classes[3],1, .022)):

                distance = planet[0] # This is sector based, 1 sector is 100,000Km
                name = planet[1]
                planet_diameter = planet[2]
                planet_type = planet[3]
                r = distance * 100000000 # Need actual distance for mapping orbits, this converts it into meters.
                v = math.sqrt((g*s_mass)/r)
		p_mass = planet[5]*em
                op = 2*math.pi*math.sqrt(math.pow(r,3)/(g*s_mass))
                iron = planet_diameter*iron_ore[planet_type]
                carbon = planet_diameter*carbon_ore[planet_type]
                oxygen = planet_diameter*oxygen_ore[planet_type]
                h2o = planet_diameter*h2o_ore[planet_type]
                deuterium = planet_diameter*deuterium_ore[planet_type]
                area = (planet_diameter/random.randint(5,10))*planet[4]
                db.universe.insert({'name' : name, 'x_pos' : x+distance, 'y_pos' : y, 'area' : area, 'item' : "planet", 'p_id' : p_id, 'iron' : iron, 'carbon' : carbon, 'oxygen' : oxygen, 'h2o' : h2o, 'deuterium' : deuterium, 'type' : planet_type, 'diameter' : planet_diameter, 'velocity' : v, 'created' : seconds, 'distance' : distance, 'op' : op, 'mass' : p_mass})



zeus()

test = db.universe.find({'item' : "planet"})

for b in test:
        print b['name']
        print b['velocity']



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))





star_classes = ('O', 'B', 'A', 'F', 'G', 'K', 'M')

star_color = {'O' : "Blue", 'B' : "Blue White", 'A' : "White", 'F' : "Yellow White", 'G' : "Yello", 'K' : "Orange", 'M' : "Red"}

star_solar_mass = {'O' : "16,150", 'B' : "2.1,16", 'A' : "1.4,2.1", 'F' : "1.04,1.4", 'G' : "0.8,1.4", 'K' : ".45,.8", 'M' : ".075,.45"}

star_solar_radii = {'O' : "6.6,20", 'B' : "1.8,6.6", 'A' : "1.4,1.8", 'F' : "1.15,1.4", 'G' : ".96,1.15", 'K' : ".7,.96", 'M' : ".05,.7"}


star_solar_luminosity = {'O' : "30000,500000", 'B' : "25,30000", 'A' : "5,25", 'F' : "1..5,5", 'G' : ".6,1.5", 'K' : ".08,.6", 'M' : ".0001,.08"}

planet_classes = ('Terrestrial', 'Desert', 'Gass', 'Ice', 'Iron', 'Ocean')

planet_mass = random.uniform(.25,350)

em = 6.972*math.pow(10,24) # Earth's mass, in kg



def create_galaxy():
        for d in range(50):
        #The following is a control structure to keep the probability of specific types of stars accurate.
                choose_star = random.randrange(1,100)
                if choose_star <= 75:
                        star_class = star_classes[6]
                        color = star_color[star_class]
                        solar_mass = star_solar_mass[star_class].split(',')
                        star_mass = random.uniform(float(solar_mass[0]),float(solar_mass[1]))*su
                        solar_radii = star_solar_radii[star_class].split(',')
                        star_radii = random.uniform(float(solar_radii[0]),float(solar_radii[1]))*sr
                        solar_luminosity = star_solar_luminosity[star_class].split(',')
                        star_luminosity = random.uniform(float(solar_luminosity[0]),float(solar_luminosity[1]))
                        star_habbital_zone_min = au*star_luminosity*.75
                        star_habbital_zone_max = au*star_luminosity*1.25

                        planet_count = random.randrange(2,15)
                        for a in range(planet_count):
                                distance = random.uniform(.25, 10)*au
