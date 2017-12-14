import binascii
def main():

	grid = [[None for x in range(128)] for y in range(128)] 


	for x in range(0,128):
		input = "ffayrhll"
		input+= "-" + str(x)
		knotHash = knot_hash(input)

		#print knotHash

		binStr = ""
		for hexVal in knotHash:
			test = str(hexVal.split("x")[1])
			if(len(test) < 2):
				test = "0"+test
			binStr += toBinary(str(binascii.unhexlify(test)))

		ind=0
		for char in binStr:
			grid[x][ind] = int(char)
			ind += 1

	used = 0
	for x in range(0,128):
		for y in range(0,128):
			if(grid[x][y] == 1):
				used += 1

	print "Task 1: " + str(used)


	inGroup = dict()

	groups = 0
	for x in range(0,128):
		for y in range(0,128):
			if(grid[x][y] == 1):
				if(not inGroup.has_key((x,y))):
					startOfGroup = (x,y)
					groups += 1
					inGroup[(x,y)] = 1

					#process the group
					currentCoord = startOfGroup
					groupDone = False
					neighbours = []
					while(not groupDone):
						if(currentCoord[0] > 0):
							if(grid[currentCoord[0]-1][currentCoord[1]] == 1 and (not inGroup.has_key((currentCoord[0]-1,currentCoord[1])))):
								neighbours.append( (currentCoord[0]-1, currentCoord[1]))
								inGroup[(currentCoord[0]-1, currentCoord[1])] = 1
						if(currentCoord[0] < 127):
							if(grid[currentCoord[0]+1][currentCoord[1]] == 1 and (not inGroup.has_key( (currentCoord[0]+1,currentCoord[1])))):
								neighbours.append((currentCoord[0]+1, currentCoord[1]))
								inGroup[(currentCoord[0]+1, currentCoord[1])] = 1
							

						if(currentCoord[1] > 0):
							if(grid[currentCoord[0]][currentCoord[1]-1] == 1 and (not inGroup.has_key( (currentCoord[0],currentCoord[1]-1) ))):
								neighbours.append( (currentCoord[0], currentCoord[1]-1) )
								inGroup[(currentCoord[0], currentCoord[1]-1)] = 1
							
						if(currentCoord[1] < 127):
							if(grid[currentCoord[0]][currentCoord[1]+1] == 1 and (not inGroup.has_key( (currentCoord[0],currentCoord[1]+1)))):
								neighbours.append( (currentCoord[0], currentCoord[1]+1) )
								inGroup[(currentCoord[0], currentCoord[1]+1)] = 1

						if(len(neighbours) > 0):
							currentCoord = neighbours.pop()
						else:
							groupDone = True

	print "Task 2: " + str(groups)










def toBinary(string):
    return "".join([format(ord(char),'#010b')[2:] for char in string])

def knot_hash(input):

	lengths = []
	for char in input:
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

	return [hex(x) for x in dense]

main()