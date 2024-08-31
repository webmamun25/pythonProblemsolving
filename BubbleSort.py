Bubble_Array=[5,4,1,3,2]

for i in range(0,len(Bubble_Array)):
    
    for j in range(0,len(Bubble_Array)-i-1):
        if Bubble_Array[j]>Bubble_Array[j+1]:
            Bubble_Array[j],Bubble_Array[j+1]=Bubble_Array[j+1],Bubble_Array[j]

print(Bubble_Array)
