# #nested if loop ---- type 1
# # if cond:
#       if cond:
#           print()
#       else:
#           statement
#   else:
#      statement

# -----type 2
# ---type 3    refer note

# num=int(input("enter the number: "))
# if num>0:
#     print("postive")
# else:
#     if num<0:
#         print("negative")
#     else:
#         print("zero")


num=int(input("enter the number: "))
if num!=0:
    if num<0:
        print("negative")
    else:
        print("positive")
else:
    print("zero")