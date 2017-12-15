def main():
	genAmul = 16807
	genBmul = 48271
	modulo = 2147483647
	aVal = 679
	bVal = 771

	count = 0
	for x in range(0,40000000):
		aVal = (aVal * genAmul) % modulo
		a = bin(aVal)[-16:].strip("b")
		a = int(a,2)
		bVal = (bVal * genBmul) % modulo
		b = bin(bVal)[-16:].strip("b")
		b = int(b,2)

		if(a == b):
			count +=1
			print "+1  at " + str(x) + "val a: " + str(a) + " val b: " + str(b)
	print count

main()