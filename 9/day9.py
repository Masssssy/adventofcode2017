def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()

	char = 0
	groupLevel = 0
	inGarbage = False
	score = 0
	garbageCount = 0
	while(char < len(inputdata)-1):
		c = inputdata[char] 

		if(inGarbage and c != ">" and c != "!"):
			garbageCount += 1

		if(c == "<"):
			inGarbage = True
		elif(c == ">"):
			inGarbage = False

		if(c == "{" and not inGarbage):
			groupLevel += 1
		elif(c == "}" and groupLevel > 0 and not inGarbage):
			score += groupLevel
			groupLevel -=1

		if(c == "!"):
			char += 2
		else:
			char += 1

	print "Score: " + str(score + 1) + " Garbage count: " + str(garbageCount)


main()