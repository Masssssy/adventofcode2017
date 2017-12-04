import sys
def main():
	input = 361527

	w, h = 500, 500;
	matrix = [[0 for x in range(w)] for y in range(h)] 

	coordX=1
	coordY=0

	matrix[0][0] = 1
	matrix[coordX][coordY] = 1
	
	horizontal = 2
	vertical = 1


	vSteps=0
	hSteps=0
	direction = 0
	skip = False

	for n in range(3, input+1):
		if(skip):
			skip = False
			continue
		if(vSteps < vertical and direction == 0):
			coordY += 1
			vSteps += 1
			matrix[coordX][coordY] = neighbourSum(coordX, coordY, matrix, input)
			if(vSteps == vertical):
				direction +=1
				vSteps = 0
		elif(hSteps < horizontal and direction == 1):
			coordX -= 1
			hSteps +=1
			matrix[coordX][coordY] = neighbourSum(coordX, coordY, matrix, input)
			if(hSteps == horizontal):
				direction +=1
				hSteps = 0
		elif(vSteps < vertical+1 and direction == 2):
			coordY -=1
			vSteps +=1
			matrix[coordX][coordY] = neighbourSum(coordX, coordY, matrix, input)
			if(vSteps == vertical+1):
				direction += 1 
				vSteps = 0
		elif(hSteps < horizontal and direction == 3):
			coordX+=1
			hSteps+=1
			matrix[coordX][coordY] = neighbourSum(coordX, coordY, matrix, input)
			if(hSteps == horizontal):
				coordX +=1
				vertical = vertical + 2
				horizontal = horizontal + 2
				hSteps = 0
				direction = 0
				skip = True
				matrix[coordX][coordY] = neighbourSum(coordX, coordY, matrix, input)

	print "Task1: Distance to " + str(n) + " is " + str(abs(coordX)+abs(coordY)) 

def neighbourSum(x,y,matrix,inp):
	numberlist = []
	numberlist.append(matrix[x][y-1])
	numberlist.append(matrix[x][y+1])
	numberlist.append(matrix[x-1][y])
	numberlist.append(matrix[x+1][y])
	numberlist.append(matrix[x+1][y+1])
	numberlist.append(matrix[x+1][y-1])
	numberlist.append(matrix[x-1][y+1])
	numberlist.append(matrix[x-1][y-1])
	if(sum(numberlist) > inp):
		print "Task2: " + str(sum(numberlist))
		sys.exit(0)
	return sum(numberlist)

main()