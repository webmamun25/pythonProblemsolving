n=int(input("Enter the total rows:"))

for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end='')
    print()

