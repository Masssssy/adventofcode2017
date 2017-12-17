def main():
	stepSize = 382
	currentPosition = 0
	buffer = [0]

	afterZero = None
	bufferLen = 1
	for x in range(0, 50000000):
		insertIndex = 1 + (currentPosition + stepSize) % bufferLen
		currentPosition = insertIndex
		bufferLen += 1

		if(insertIndex == 1):
			print "after zero"
			afterZero = x+1
	print afterZero

main()