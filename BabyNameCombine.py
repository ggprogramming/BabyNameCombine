import string

firstAndMiddle = ["Margaux","Nova","Winter","Takchee","River","Clementine","Rainer","Alice","Nico","Simone","Vega"]
lastNames = ["Verlin","Gong","VerlinGong","Verlong","Verlin-Gong","Vergong","Gong-Verlin","Gongverlin"]

def main():
    #print(firstAndMiddle)
    #print(lastNames)
    for first in firstAndMiddle:
        for middle in firstAndMiddle:
            if first == middle:
                continue
            else:
                for last in lastNames:
                    name = "{} {} {}".format(first, middle, last)
                    print(name)
    return

if __name__ == "__main__":
    main()