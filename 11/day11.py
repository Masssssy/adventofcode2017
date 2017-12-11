def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()
	directions = inputdata.split(",")

	position = (0,0)
	maxDist = 0

	for direc in directions:
		if(direc == "s"):
			position = (position[0], position[1]-1)
		if(direc == "n"):
			position = (position[0], position[1]+1)
		if(direc == "sw"):
			position = (position[0]-1, position[1]-1)
		if(direc == "nw"):
			position = (position[0]-1, position[1]+1)
		if(direc == "se"):
			position = (position[0]+1, position[1]-1)
		if(direc == "ne"):
			position = (position[0]+1, position[1]+1)

		dist = max(abs(position[0]), abs(position[1])) 
		if(dist > maxDist):
			maxDist = dist

	position = (abs(position[0]), abs(position[1])) 
	print "Task 1: " + str(max(position))
	print "Task 2: " + str(maxDist)


main()