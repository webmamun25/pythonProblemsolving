# second largest element 

L=[1,4,6,3,2]

first_large=L[0]
second_large=None 

if(len(L)<=1):
    second_large=None

for i in L[1:]:
    if(i>first_large):
        second_large=first_large
        first_large=i
    elif(i!=first_large):
        if second_large==None or second_large<i:
            second_large=i 

print(second_large)