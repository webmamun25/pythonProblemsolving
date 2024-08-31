Selection_Array=[5,4,1,3,2]

for i in range(0,len(Selection_Array)-1):
    minPos=i 

    for j in range(i+1,len(Selection_Array)):
        if(Selection_Array[minPos]>Selection_Array[j]):
            minPos=j
    
    Selection_Array[minPos],Selection_Array[i]=Selection_Array[i],Selection_Array[minPos]

print(Selection_Array)