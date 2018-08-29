import string

firstAndMiddle = ["Margaux","Nova","Winter","Takchee","River","Clementine", "Simone","Vega", "Maude", "Marikit"]
lastNames = ["Verlin","Gong","Verlingong","Verlong","Verlin-Gong","Vergong","Gong-Verlin","Gongverlin"]

def main():
    
    f = open('names.csv', 'a')

    for first in sorted(firstAndMiddle):
        for middle in sorted(firstAndMiddle):
            if first == middle:
                continue
            else:
                for last in sorted(lastNames):
                    name = "{}.{}.{}., {} {} {}".format(first[:1], middle[:1], last[:1], first, middle, last)
                    print(name)
                    name = name + "\n"
                    f.write(name)
    
    f.close()
    return

if __name__ == "__main__":
    main()