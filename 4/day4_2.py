import hashlib
def main():
    inputfile = open("input")
    inputdata = inputfile.read()
    inputfile.close()
    splitdata = inputdata.split("\n")


    valid = 0

    for phrase in splitdata:
        words = phrase.split(" ")
        dict = {}
        failed = False
        for word in words:
            alphabet = [0]*26
            for letter in word:
                alphabet[ord(letter) - 97] += 1
            wordhash = hashlib.sha256(str(alphabet).encode('utf-8','ignore')).hexdigest()

            if(not dict.has_key(wordhash)):
                dict[wordhash] = 1
            else:
                failed = True
                break;
        if(not failed):
            valid += 1

        dict.clear()

    print valid


main()