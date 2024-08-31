num1=60 
num2=24 

result=[]
while num2/2>=2:
    bag=num2//2
    print(bag)
    result.append(bag)
    num2=bag 

while num1/2>=2:
    bag=num1//2
    print(bag)
    num1=bag 
    result.append(bag)

print(result)

    
