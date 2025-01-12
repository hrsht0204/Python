while True:
    Info = input("press enter to start, or enter 's' for Available shapes: ")
    if Info.lower() == "s":
        print("Available shapes are:\nRectangle\nSquare\nTriangle\nCircle")
    elif Info == "":
        Shape = input("What is the shape: ")

        if Shape.lower() in ["rectangle", "r"]:
            lenR = float(input("Length: "))
            BreR = float(input("Breadth: "))
            while True:
                area_or_peri = input("Area or Perimeter: ")
                if area_or_peri.lower() in ["area", "a"]:
                    areaR = lenR * BreR
                    print("Area is", areaR)
                elif area_or_peri.lower() in ["perimeter", "p"]:
                    periR = 2 * (lenR + BreR)
                    print("Perimeter is", periR)
                elif area_or_peri.lower() in ["e", ""]:
                    break
                else:
                    print("Wrong input")

        elif Shape.lower() in ["square", "s"]:
            sideS = float(input("Side length: "))
            while True:
                area_or_peri = input("Area or Perimeter: ")
                if area_or_peri.lower() in ["area", "a"]:
                    areaS = sideS * sideS
                    print("Area is", areaS)
                elif area_or_peri.lower() in ["perimeter", "p"]:
                    periS = 4 * sideS
                    print("Perimeter is", periS)
                elif area_or_peri.lower() in ["e", ""]:
                    break
                else:
                    print("Wrong input")

        elif Shape.lower() in ["triangle", "t"]:
            baseT = float(input("Base length: "))
            while True:
                area_or_peri = input("Area or Perimeter: ")
                if area_or_peri.lower() in ["area", "a"]:
                    heiT = float(input("Height from base: "))
                    areaT = (heiT * baseT) / 2
                    print("Area is", areaT)
                elif area_or_peri.lower() in ["perimeter", "p"]:
                    side1 = float(input("Length of side 1: "))
                    side2 = float(input("Length of side 2: "))
                    side3 = float(input("Length of side 3: "))
                    periT = side1 + side2 + side3
                    print("Perimeter is", periT)
                elif area_or_peri.lower() in ["e", ""]:
                    break
                else:
                    print("Wrong input")

        elif Shape.lower() in ["circle", "c"]:
            RadiC = float(input("Radius: "))
            pi = 3.14
            while True:
                area_or_peri = input("Area or Circumference: ")
                if area_or_peri.lower() in ["area", "a"]:
                    areaC = pi * (RadiC ** 2)
                    print("Area is", areaC)
                elif area_or_peri.lower() in ["circumference", "c"]:
                    CircumC = 2 * (pi * RadiC)
                    print("Circumference is", CircumC)
                elif area_or_peri.lower() in ["e", ""]:
                    break
                else:
                    print("Wrong input")

        else:
            print("The shape is either not available or invalid")
    else:
        print("Invalid input. Please try again.")
