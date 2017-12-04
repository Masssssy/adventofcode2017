def main():
    inputfile = open("input")
    inputdata = inputfile.read()
    inputfile.close()
    splitdata = inputdata.split("\n")


    valid = 0

    for phrase in range(0, len(splitdata)):
        words = splitdata[phrase].split(" ")
        dict = {}
        failed = False
        for word in range(0, len(words)):
            if(not dict.has_key(words[word])):
                dict[words[word]] = 1
            else:
                print "failed phrase"
                failed = True
                break;
        if(not failed):
            valid += 1

        dict.clear()

    print valid


main()