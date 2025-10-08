A1=int(input("enter angle 1: "))
A2= int(input("enter angle 2: "))
A3=int(input("enter angle 3: "))

total=A1+A2+A3
if total!=180:
    print("not a triangle")
else:
    if A1==A2==A3:
        print("equalateral triangle")
    elif A1==A2 or A1==A3 or A2==A3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")