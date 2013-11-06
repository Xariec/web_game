import pymongo

db = pymongo.Connection('localhost', 27017).bbarnes_test





print """
<canvas id="myCanvas" width="10000" height="10000" style="border:1px solid #EFFFFF;" onmousemove="myMouse(event)">
Your browser does not support the HTML5 canvas tag. Please open in Google Chrome.
</canvas>

<script>

var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d")
"""



# stars = db.universe.find({'object' : "star"})

# for star in stars:
	# x = star['x_pos']/10
	# y = star['y_pos']/10
	# size = star['star_size']
	# name = star['name']
	# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,%d,0,2*Math.PI);	ctx.fillStyle = "#FF0000";ctx.fill();ctx.stroke();ctx.font="12px Arial";ctx.fillStyle = "#FFFFFF";ctx.fillText("%s",%d,%d);ctx.closePath();ctx.restore();' %(x,y,size,name, x+10,y+10)

stars = db.universe.find({'object' : "star"})

for star in stars:
	x = star['x_pos']/10
	y = star['y_pos']/10
	size = star['size']/10
	name = star['name']
	print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,%d,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %(x,y,size)

	
planets = db.universe.find({'object' : "planet"})

for planet in planets:
	x = planet['x_pos']/10
	y = planet['y_pos']/10
	name = planet['name']
	print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,1,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.font="12px Arial";ctx.fillStyle = "#000000";ctx.fillText("%s",%d,%d);ctx.closePath();ctx.restore();' %(x,y,name,x+10,y+10)
		

# planets = db.universe.find({'object' : "star_circumference"})

# for planet in planets:
	# x = planet['x_pos']
	# y = planet['y_pos']
	# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,1,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %(x/10,y/10)
		
# planets = db.universe.find({'object' : "planet_circumference"})

# for planet in planets:
	# x = planet['x_pos']
	# y = planet['y_pos']
	# print 'ctx.save();ctx.translate(2500,2500);ctx.beginPath();ctx.arc(%d,%d,1,0,2*Math.PI);	ctx.fillStyle = "#0000FF";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %(x/10,y/10)


print """
</script>

</center>
</div>
"""
