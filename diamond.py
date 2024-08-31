n=int(input("Enter the rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,(2*i-1)+1):
        print("*",end="")
    print()

    # odd representation with 2x+1 or 2x-1