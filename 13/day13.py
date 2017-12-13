def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()

	layersdata = inputdata.split("\n")
	layers = []

	for x in range(0,len(layersdata)):
		gg = layersdata[x].split(": ")
		gg.append(0)
		gg.append(-1)
		layers.append(gg)

	severity = 0
	position = 0
	lastLayer = int(layers[len(layers)-1][0])
	while(position < lastLayer):
		for layer in layers:
			if(int(layer[0]) == position):
				if(int(layer[2]) == 0):
					severity += int(layer[0])*int(layer[1])

		for layer in layers:
			if(int(layer[2]) == int(layer[1])-1 or int(layer[2] == 0)):
				layer[3] = -layer[3]

			layer[2] += int(layer[3])*1
		
		position +=1

	print "Task 1: severity " + str(severity)


main()

