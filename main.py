import sys
from street import Street, Streets, Point

# YOUR CODE GOES HERE
totalStreets = []
def main():
    # YOUR MAIN CODE GOES HERE
    myStreets = Streets()

    try:
        global totalStreets
        generated =0 

       
    # sample code to read from stdin.
    # make sure to remove all spurious print statements as required
    # by the assignment
        while True:
            print("Enter command: ")
            line = sys.stdin.readline()
            command = line[0]
            print(len(line))
            coords =[]
            if command=="a":
                print("Add Street")
                flagQ = False
                strName = ""
                for i in range(1, len(line)):
                    if (flagQ):
                        if(line[i]!="\""):
                            strName += line[i]
                    if line[i]=="\"":
                        if (flagQ):
                            flagQ = False
                        else:
                            flagQ = True
                    
                    coord = []
                    if(line[i]=="("):
                        coord.append(int(line[i+1]))
                        coord.append(int(line[i+3]))
                        coords.append(coord)
                myStreets.addStreet(name=strName, points=coords)
                myStreets.print()
                myStreets.checkIntersections()
                myStreets.printVertices()


            elif command=="c":
                    print("Change Street")
            elif command == "r":
                    print("Delete Street")
            elif command == "g":
                    print("Generate Graph")
            else:
                print("Invalid command.")
            
            #myStreet.streetName , myStreet.streetPath = su.parseInput(line)
        sys.exit(0)

    except Exception as e:
        print("Error : \n" + str(e), file=sys.stderr)



if __name__ == "__main__":
    main()

# print(command)

