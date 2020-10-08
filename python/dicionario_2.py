alien={"x_position" : 0,"y_position" : 25,"speed":"medium"}

print("Original X position: " + str(alien["x_position"]))

if alien["speed"]=="slow":
	alien["x_position"]+=1

elif alien["speed"]=="medium":
	alien["x_position"]+=2

elif alien["speed"]=="fast":
	alien["x_position"]+=3
	
print("New X position: " + str(alien["x_position"]))

del alien["y_position"]
print(alien)
