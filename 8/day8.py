import operator
def main():
	inputfile = open("input")
	inputdata = inputfile.read()
	inputfile.close()
	splitdata = inputdata.split("\n")

	registers = dict()
	highest = 0

	for instruction in splitdata:
		instargs = instruction.split(' ')
		checkOk = False

		checkReg = instargs[4]
		checkOp = instargs[5]
		checkVal = int(instargs[6])

		if(registers.has_key(checkReg)):
			checkRegVal = registers.get(checkReg)
		else:
			registers[checkReg] = 0
			checkRegVal = 0

		if(checkOp == "<"):
			if(checkRegVal < checkVal):
				checkOk = True

		elif(checkOp == "<="):
			if(checkRegVal <= checkVal):
				checkOk = True
		elif(checkOp == ">"):
			if(checkRegVal > checkVal):
				checkOk = True
		elif(checkOp == ">="):
			if(checkRegVal >= checkVal):
				checkOk = True
		elif(checkOp == "=="):
			if(checkRegVal == checkVal):
				checkOk = True
		elif(checkOp == "!="):
			if(checkRegVal != checkVal):
				checkOk = True

		if(checkOk):
			changeReg = instargs[0]
			operation = instargs[1]
			amount = int(instargs[2])

			if(registers.has_key(checkReg) and registers.get(changeReg) != None):
				changeRegVal = registers.get(changeReg)
			else:
				registers[changeReg] = 0
				changeRegVal = 0

			if(operation == "dec"):
				changeRegVal -= amount
				registers[changeReg] = changeRegVal
				if(changeRegVal > highest):
					highest = changeRegVal

			elif(operation == "inc"):
				changeRegVal += amount
				registers[changeReg] = changeRegVal
				if(changeRegVal > highest):
					highest = changeRegVal

	print registers.get(max(registers.iteritems(), key=operator.itemgetter(1))[0])
	print highest

main()