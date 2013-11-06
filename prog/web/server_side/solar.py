a = {}
planet = 50
k = 0
i = random.randint(1,4)*star_size
while k < i:
	distance_between = random.randrange(30,300,1)
	planet += distance_between
	if planet <= solar_system_size:
		key = planet
		name = id_generator()
		a[key] = name
		k += 1
	else:
		break
def planets():
	for distance in (a):
		while True:
			random_x = random.randint(-distance,distance)
			random_y = random.randint(-distance,distance)

			if(random_x <distance and random_x >-distance and random_y <distance and random_y >-distance):
				continue
