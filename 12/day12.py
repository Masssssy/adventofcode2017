def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()

	connections = inputdata.split("\n")

	idToConnection = dict()

	for connection in connections:
		connection = connection.split(" <-> ")
		leadsTo = connection[1:]
		leadsTo = leadsTo[0].split(", ")
		idToConnection[connection[0]] = leadsTo

	inGroup = dict()

	currentItems = ['0']
	while(len(currentItems) > 0):
		linkedItems = idToConnection.get(currentItems.pop())
		for linkedItem in linkedItems:
			print linkedItem
			if(not inGroup.has_key(linkedItem)):
				currentItems.append(linkedItem)
				inGroup[linkedItem] = 1

	print len(inGroup)

main()