insertion_array=[5,4,3,2,1]

for i in range(1,len(insertion_array)):
    curr=insertion_array[i]
    prev=i-1 

    while(prev>=0 and insertion_array[prev]>curr):
        insertion_array[prev+1]=insertion_array[prev]
        prev-=1
    
    insertion_array[prev+1]=curr

print(insertion_array)