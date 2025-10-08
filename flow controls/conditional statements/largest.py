# # num1=int(input("enter the number1:"))
# # num2=int(input("enter the number2:"))
# # num3=int(input("enter the number3:"))
# # if num1==num2==num3:
# #     print("all are same")
# # elif num1>num2 and num1>num3:
# #     print("number 1 is greater")
# # elif num2>num1 and num2>num3:
# #     print("number 2 is greater")
# # else:
# #     print("number 3 is greater")
#
#
# # Input three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# #
# # # Find the second largest using if-else
# # if (a > b and a < c) or (a > c and a < b):
# #     second_largest = a
# # elif (b > a and b < c) or (b > c and b < a):
# #     second_largest = b
# # else:
# #     second_largest = c
# #
# # print("The second largest number is:", second_largest)
# #



#using nested if

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2:
    if num1 >= num3:
        print("num1 is the largest")
    else:
        print("num3 is the largest")
else:
    if num2 >= num3:
        print("num2 is the largest")
    else:
        print("num3 is the largest")
