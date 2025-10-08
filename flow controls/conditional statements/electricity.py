units=int(input("enter the units: "))
if units>100:
    if 100<units<200:
        total=(units-100)*5
        print("the bill amount is",total)
    else:
        total=500+((units-200)*10)
        print("the bill amount is",total)
else:
    print("bill amount is 0")
