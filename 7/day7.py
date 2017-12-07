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
	for disc in splitdata:
		disc[0] = [x.strip(' ') for x in disc[0].split(' ')]
		disc[1] = [x.strip(' ') for x in disc[1].split(",")]
		for child in disc[1]:
			if(child != ''):
				childrenDict[child] = 1

	for disc in splitdata:
		if childrenDict.has_key(disc[0][0]):
			continue
		else:
			print disc[0]
main()