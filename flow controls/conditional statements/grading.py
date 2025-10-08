bio=int(input("enter the mark"))
maths=int(input("enter the mark"))
chem=int(input("enter the mark"))
phy=int(input("enter the mark"))
eng=int(input("enter the mark"))

total=500
sum1=bio+maths+phy+chem+eng

percentage=(sum1/total)*100
print(percentage)

if percentage>=80:
    print("grade is A+")
elif 70<=percentage<80:
    print("grade is A")
else:
    print("failed")