def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()

	char = 0
	groupLevel = 0
	inGarbage = False
	score = 0
	while(char < len(inputdata)-1):

		if(inputdata[char] == "<"):
			inGarbage = True
		elif(inputdata[char] == ">"):
			inGarbage = False

		if(inputdata[char] == "{" and not inGarbage):
			groupLevel += 1
		elif(inputdata[char] == "}" and groupLevel > 0 and not inGarbage):
			score += groupLevel
			groupLevel -=1

		if(inputdata[char] == "!"):
			char += 2
		else:
			char += 1

	print "Score: " + str(score + 1)


main()