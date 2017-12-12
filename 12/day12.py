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
			if(not inGroup.has_key(linkedItem)):
				currentItems.append(linkedItem)
				inGroup[linkedItem] = 1

	print "Task 1: " + str(len(inGroup))

	groups = 0
	while(findfirst(connections, inGroup) != None):
		first = findfirst(connections, inGroup)
		localGroup = dict()
		currentItems = [str(first)]
		inGroup[str(first)] = 1
		localGroup[str(first)] = 1

		while(len(currentItems) > 0):
			currentItem = currentItems.pop()
			linkedItems = idToConnection.get(currentItem)

			for linkedItem in linkedItems:
				if(not localGroup.has_key(linkedItem)):
					currentItems.append(linkedItem)
					localGroup[linkedItem] = 1
					inGroup[linkedItem] = 1
		groups += 1
	print "Task 2: " + str(groups+1)


def findfirst(connections, inGroup):
	for x in range(0,len(connections)):
		if(not inGroup.has_key(str(x))):
			return x
	return None

main()