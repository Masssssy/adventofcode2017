import sys
def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()

	layersdata = inputdata.split("\n")
	lastLayer = layersdata[len(layersdata)-1].split(": ")[0]

	layers = [0] * (int(lastLayer)+1)

	for x in range(0,len(layersdata)):
		gg = layersdata[x].split(": ")
		layers[int(gg[0])] = int(gg[1])


	severity = 1
	delay = 0
	while(severity != 0):
		severity = 0
		position = 0
		delay += 1
		time = delay

		while(position < int(lastLayer) +1 ):
			if(layers[position] != 0):
				if((time % (2 * (int(layers[position]) - 1))) == 0):
						severity += 1
						break
			position += 1
			time +=1

	print "Task 2: Delay  " + str(delay)

main()

