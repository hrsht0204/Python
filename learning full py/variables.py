A = int(input("A :"))
G = input("M/F :")

if (A == 1 or A ==2 and G.lower() == "m"):
    print("fee is 100")
elif(A == 3 or A == 4 and G.lower() == "f"):
    print("fee is 200")
elif(A == 5 and G.lower() == "m"):
    print("fee is 300")
else:
    print("no fee")