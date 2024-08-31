n=int(input("Enter the rows:"))
counter=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print("{} ".format(counter) ,end="")
        counter+=1
    print()
