def main():
	stepSize = 382
	currentPosition = 0
	buffer = [0]

	for x in range(0,2017):
		insertIndex = 1 + (currentPosition + stepSize) % len(buffer)
		buffer = buffer[:insertIndex] + [x+1] + buffer[insertIndex:]
		currentPosition = insertIndex

	print "Task 1: " + str(buffer[buffer.index(2017)+1])


main()