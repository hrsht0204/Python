Num = int(input("Number for the table : "))
Till = int(input("Till which num : "))
multiplier = 1
while multiplier <= Till:
    multiple = Num * multiplier
    print(Num , "x" , multiplier ,"=" , multiple)
    multiplier += 1
