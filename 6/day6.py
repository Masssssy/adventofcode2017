import hashlib
def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()
	splitdata = inputdata.split("\t")

	banks = map(int, splitdata)
	seenBefore = dict()

	done = False
	iterations = 0
	while(not done):
		highest = [0,None]
		seenBeforeHash = hashlib.sha256(str(banks).encode('utf-8','ignore')).hexdigest()
		if(seenBefore.has_key(seenBeforeHash)):
			print iterations
			print "Since last: " + str(iterations - seenBefore.get(seenBeforeHash))
			done = True
		else:
			seenBefore[seenBeforeHash] = iterations
		iterations += 1
		for n in range(0,len(banks)):
			if(banks[n] > highest[0]):
				highest = (banks[n], n)



		banks[highest[1]] = 0

		ind = 1
		while(highest[0] > 0):
			highest = [highest[0]-1, highest[1]]
			banks[(highest[1] + ind) % len(banks)] += 1
			ind += 1


main()