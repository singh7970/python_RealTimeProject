# sum =0
# for i in range(0,6):
#     n=int(input("Enter the item price :"))
#     sum=sum+n

#     print("Total price",'$',sum) 
sum=0
while(True):
    user=input("Enter the item price or CLICK 'q' to quit:")
    if (user!='q'):
        sum=sum+int(user)
        print(f"Order total so far:{sum}")
    else:
        print(f"Your Bill total is {sum} thanks for shoping us")    
        break

   

   

