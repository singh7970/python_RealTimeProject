with open("/home/priyanshu/Documents/python_realTimeProject/currency_conerter/data.txt") as f:
    lines=f.readlines()
currDict={}    
for line in lines:
    parsed=line.split("\t")
    currDict[parsed[0]]=parsed[1]
# print(currDict)    
amount=int(input("enter the ammount:\n"))
print("Enterh the currency")
print("Available: \n")
[print(item) for item in currDict.keys()]
currency=input("Enter the only upper values ")
print(f"{amount} INR is equl to {amount*float(currDict[currency])}{currency}")



