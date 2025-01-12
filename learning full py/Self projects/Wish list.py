list = []


Heading = print("\033Wish List")
Info = print("Type 'r' to remove any item \nType 'e' to get the final list" )
H = input("Press enter to start making: ")

if H == "":
    no = 1
    while True:
        Thing = input(f"{no}. Thing :")
        if Thing.lower() == "r":
            Ritem = input("Thing to remove : ")
            if Ritem in list :
                list.remove(Ritem)
            else:
                print(Ritem , "is not in the list")
        elif (Thing.lower() == "e"):
            print("here is your final list\n",list)
            break
        else:
            list.append(Thing)
            no = no + 1
else:
    print("Sorry invalid action")