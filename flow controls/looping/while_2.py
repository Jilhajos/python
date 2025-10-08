# # print all the digits of a given number
# # ex: 234
#
# num=int(input("enter the number"))
# while num!=0:
#     n=num%10
#     print(n)
#     num=num//10
#-------------------------------------------------------------------------------------------------------------------#

# find sum of digits
#
# num=int(input("enter the number:"))
# digit_sum=0
# while num!=0:
#     digit=num%10
#     digit_sum+=digit
#     num//=10
# print(digit_sum)

#--------------------------------------------------------------------------------------------------------------------#

# find the sum of numbers from lower to upper range

lower=int(input("enter the lower range: "))
upper=int(input("enter the upper range: "))
s=0
while lower<=upper:
    s+=lower
    lower+=1
print(s)