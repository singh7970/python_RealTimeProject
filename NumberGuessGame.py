import random
# user=int(input("Enter the number"))
# comp=random.randint(1,10)
# if user>comp:
#     print(f"computer output is  {comp}")
#     print("your guess in hiegh")
# elif (user==comp)   :
#     print(f"computer output is  {comp}")
#     print("You are correct")
# elif(user<comp):
#     print(f"computer output is  {comp}")

#     print("you guess is to low ")    
# else:
#     print("try nwxt time ")    
n=5
for i in range (n):
    user=int(input("Enter the number"))
    comp=random.randint(1,10)
    if user>comp:
        print(f"computer output is  {comp}")
        print("your guess in hiegh")
    elif (user==comp)   :
        print(f"computer output is  {comp}")
        print("You are correct")
    elif(user<comp):
        print(f"computer output is  {comp}")

        print("you guess is to low ")    
    else:
        print("try nwxt time ")    
