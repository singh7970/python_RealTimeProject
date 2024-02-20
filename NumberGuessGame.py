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


n=7
print("Range of guessing game is 1-20")
comp=random.randint(1,20)
chances=n

for i in range (n):
    
    print(f"you have  {chances} chances")
    chances -= 1
    user=int(input("Enter the number :"))
    
    if(user==comp)   :
        print(f"computer number is  {comp}")
        print("You are correct 🤩")
        print(" You won 😎") 
        break
    elif(user<comp):
        print("Try Again! You guessed too small 🙄 ")    
    elif user>comp:
        print("Try Again! You guessed too high 😵")
if user != comp:
    print(f"Sorry, you could not  guess the number. The correct number was {comp}.")
        
        
