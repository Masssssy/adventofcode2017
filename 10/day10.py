def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()
	lengths = inputdata.split(",")

	list = range(0,256)
	currentPos = 0
	skipSize = 0

	for length in lengths:
		if(currentPos + int(length) > 256):
			gg = list[currentPos:256]
			gg.extend(list[0:(currentPos + int(length)) % 256])
			reverse = gg[::-1]
			for b in range(0, int(length)):
				list[(currentPos+b)%256] = reverse[b]

		else:
			gg = list[currentPos:currentPos+int(length)]
			reverse = gg[::-1]
			list[currentPos:currentPos+int(length)] = reverse

		currentPos = (currentPos + (int(length) + skipSize)) % 256
		skipSize +=1

	print "Task 1: " + str(list[0] * list[1])


main()