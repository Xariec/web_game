import pymongo


db = pymongo.Connection('localhost', 27017).game





print """
<html>
<head>
<title> </title>
</head>


<body>
<center>
<canvas id="myCanvas" width="10000" height="10000" style="background-color: #000000";>
Your browser does not support the HTML5 canvas tag. Please open in Google Chrome.

<script>
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.translate(c.width /2, c.height /2);
"""
scale = 100000000

stars = db.universe.find({'item' : "star"})
for a in stars:
	x = a['x_pos']/scale
	y = a['y_pos']/scale
	size = int(a['system_size']/scale)
	print "ctx.beginPath();	ctx.arc(%r,%r,%r,0,2*Math.PI);	ctx.strokeStyle = 'yellow';	ctx.stroke();" %(int(x),int(y),size)
	
planets = db.universe.find({'item' : "planet"})
for a in planets:
	x = a['x_pos']/scale
	y = a['y_pos']/scale
	size = 1
	print "ctx.beginPath();	ctx.arc(%r,%r,%r,0,2*Math.PI);	ctx.strokeStyle = 'green';	ctx.stroke();" %(int(x),int(y),size)
	
	
print """
</script>
</body>
</html>
"""
