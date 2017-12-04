def main():
	input = 361527

	w, h = 1000, 1000;
	Matrix = [[0 for x in range(w)] for y in range(h)] 

	Matrix[0][0] = 1
	
	horizontal = 2
	vertical = 1

	coordX=1
	coordY=0
	Matrix[coordX][coordY] = 1
	vSteps=0
	hSteps=0
	direction = 0
	skip = False

	for n in range(3, 361528):
		if(skip):
			skip = False
			continue
		if(vSteps < vertical and direction == 0):
			coordY += 1
			vSteps += 1
			print "Place1 " + str(n) + " at " + str(coordX) + ", " + str(coordY)
			if(vSteps == vertical):
				direction +=1
				vSteps = 0
		elif(hSteps < horizontal and direction == 1):
			coordX -= 1
			hSteps +=1
			print "Place2 " + str(n) + " at " + str(coordX) + ", " + str(coordY)
			if(hSteps == horizontal):
				direction +=1
				hSteps = 0
		elif(vSteps < vertical+1 and direction == 2):
			coordY -=1
			vSteps +=1
			print "Place3 " + str(n) + " at " + str(coordX) + ", " + str(coordY)
			if(vSteps == vertical+1):
				direction += 1 
				vSteps = 0
		elif(hSteps < horizontal and direction == 3):
			coordX+=1
			hSteps+=1
			print "Place4 " + str(n) + " at " + str(coordX) + ", " + str(coordY)
			if(hSteps == horizontal):
				print "layer done"
				coordX +=1
				vertical = vertical + 2
				horizontal = horizontal + 2
				hSteps = 0
				direction = 0
				skip = True
				print "first element of next is " + str(n+1) + " at " + str(coordX) + " , " + str(coordY)

	print "Distance is " + str(abs(coordX)+abs(coordY)) 




main()

