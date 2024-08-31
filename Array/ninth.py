#subarray with given num 
L=[1,22,13,7,9,11,10]
s=16
for i in range(0,len(L)):
    subarray=[]
    for j in range(i,len(L)):
        subarray.append(L[j])
        if(sum(subarray)==s):
            print("Found",subarray)

