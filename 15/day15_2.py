def main():
	genAmul = 16807
	genBmul = 48271
	modulo = 2147483647
	aVal = 679
	bVal = 771

	count = 0
	for x in range(0,5000000):
		adata = generate(aVal, genAmul, 4, modulo)
		a = adata[1]
		aVal = adata[0]
		bdata = generate(bVal, genBmul, 8, modulo)
		b = bdata[1]
		bVal = bdata[0]

		if(a == b):
			count +=1
			print "+1  at " + str(x) + "val a: " + str(a) + " val b: " + str(b)
	print count


def generate(val, mul, mulToFind, modulo):
	done = False
	while(not done):
		fval = (val * mul) % modulo
		if(fval % mulToFind == 0):
			#ok fval
			f = bin(fval)[-16:].strip("b")
			f = int(f,2)
			done = True
		else:
			val = fval

	return [fval, f]


main()