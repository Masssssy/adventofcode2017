def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()
	
	lengths = []
	for char in inputdata:
		lengths.append(ord(char))
	lengths.append(17)
	lengths.append(31)
	lengths.append(73)
	lengths.append(47)
	lengths.append(23)


	list = range(0,256)
	currentPos = 0
	skipSize = 0

	passes = 0
	while(passes < 64):
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
		passes += 1

	#print list

	dense = []
	for b in range(0,16):
		blist = list[b*16: (b*16)+16]
		#print blist
		res = blist[0] ^ blist[1]
		for block in range(2,16):
			res = res ^ blist[block]
		dense.append(res)

	print [hex(x) for x in dense]



	#print "Task 1: " + str(list[0] * list[1])



main()