def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()
	splitdata = inputdata.split("\n")
	splitdata = [x.split('->') for x in splitdata]
	for b in splitdata:
		if(len(b) < 2):
			b.append('')

	childrenDict = dict()
	idToList = dict()
	for disc in splitdata:
		disc[0] = [x.strip(' ') for x in disc[0].split(' ')]
		disc[1] = [x.strip(' ') for x in disc[1].split(",")]
		for child in disc[1]:
			if(child != ''):
				childrenDict[child] = 1
		idToList[disc[0][0]] = disc

	for disc in splitdata:
		if childrenDict.has_key(disc[0][0]):
			continue
		else:
			root = disc[0][0]
			print "Task 1: " + str(root)

	rootChildren = idToList.get(root)[1]
	print rootChildren

	a = 0
	lastLayer =[]
	while(a<4):
		balance = []
		for child in rootChildren:
			balance.append(weightOf(child,idToList))
		print balance
		if(len(set(balance)) == 1):
			print str(lastWrong[0][0][0]) + " needs to be " + str(lastWrong[1]) + " less than " + str(lastWrong[0][0][1]) 
			break

		wrongIndex = None
		for n in range(len(balance)): 
			amount = balance.count(balance[n])	#Slow but w/e
			if(amount == 1):
				wrongIndex = n
		a+=1 
		lastWrong = [idToList.get(rootChildren[wrongIndex]), balance[wrongIndex] - balance[wrongIndex-1]]
		rootChildren = idToList.get(rootChildren[wrongIndex])[1]
		print rootChildren
			
def weightOf(name,idToList):
	weight = int(idToList.get(name)[0][1].strip("(").strip(")"))
	childList = idToList.get(name)[1]

	if(childList[0] == ''):
		return int(idToList.get(name)[0][1].strip("(").strip(")"))

	for child in childList:
		weight += weightOf(child, idToList)
	return weight
main()