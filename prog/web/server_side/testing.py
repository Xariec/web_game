import pymongo

db = pymongo.Connection('localhost', 27017).bbarnes_test



# find = db.universe.find()

print """
<canvas id="myCanvas" width="5000" height="5000" style="border:1px solid #EFFFFF;" onmousemove="myMouse(event)">
Your browser does not support the HTML5 canvas tag. Please open in Google Chrome.
</canvas>

<script>

var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d")
"""



stars = db.universe.find({'object' : "star"})

for star in stars:
	x = star['x_pos']
	y = star['y_pos']
	size = star['size']
	print 'ctx.beginPath();ctx.arc(%d,%d,%d,0,2*Math.PI);	ctx.fillStyle = "#00FF00";ctx.fill();ctx.stroke();ctx.closePath();' %(x/10,y/10,size/10)
	












# distance = 29742
# x_pos = 29742
# y_pos = 29742
# front = y_pos + distance
# back = y_pos - distance
# left = x_pos - distance
# right = x_pos + distance
# position = db.universe.find({"x_pos": {"$gte": left, "$lte": right},"y_pos": {"$gte": back, "$lte": front}})





# for system in position:
	# x = system['x_pos']
	# y = system['y_pos']
	# name = system['name']
	# object = system['object']
	# if object == "star":	
		# print 'ctx.save();ctx.translate(500,500);ctx.beginPath();ctx.arc(%d,%d,10,0,2*Math.PI);	ctx.fillStyle = "#00FF00";ctx.fill();ctx.stroke();ctx.closePath();ctx.restore();' %(x-x_pos,y-y_pos)
	# elif object == "planet":
		# print 'ctx.save();ctx.translate(500,500);ctx.beginPath();ctx.arc(%d,%d,2,0,2*Math.PI);	ctx.fillStyle = "#00FF00";ctx.fill();ctx.stroke();ctx.closePath();cts.restore();' %(x-x_pos,y-y_pos)
		



print """
</script>

</center>
</div>
"""

