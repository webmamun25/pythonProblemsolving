# find element with left side smaller/right side greater in an array

L=[3,1,2,5,8,7,9]

# for i in range(1,len(L)-1):
#     flag=True 

#     for j in range(0,i):
#         if L[j]>L[i]:
#             flag=False 
#     for k in range(i+1,len(L)):
#         if L[k]<L[i]:
#             flag=False 
#     if flag:
#         print(L[i])
        

# new

# for i in range(1,len(L)-1):
#     if(max(L[:i])<L[i]< min(L[i+1:])):
#         print(L[i])

# new2

max_array=[]
max_val=L[0]
min_array=[]
min_val=L[-1]

for i in L:
    if(i>max_val):
        max_val=i
    max_array.append(max_val)
print(max_array)

for i in range(len(L)-1,-1,-1):
    if L[i]<min_val:
        min_val=L[i]

    min_array.insert(0,min_val)
print(min_array)

for i in range(1,len(L)-1):
    if max_array[i-1]<L[i]<min_array[i+1]:
        print(L[i])
