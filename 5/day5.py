def main():
    inputfile = open("input")
    inputdata = inputfile.read()
    inputfile.close()
    splitdata = inputdata.split("\n")

    index = 0
    steps = 0 
    while(index < len(splitdata)):
        jump = int(splitdata[index])
        splitdata[index] = int(splitdata[index]) + 1
        index = index + jump
        steps += 1

    print steps
main()