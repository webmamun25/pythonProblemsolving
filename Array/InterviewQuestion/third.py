L=[1,22,13,7,9,11,10]
s=16
d={}
# first solution
# for i in range(0,len(L)):
#             subarray=[]
#             for j in range(i,len(L)):
#                 subarray.append((L[j]))
                
#                 if(sum(subarray)==s):
#                         print(subarray)

# second solution 

curr_sum=0 
for i in range(len(L)):
    curr_sum+=L[i]
    if(curr_sum-s) in d:
        print(d[curr_sum-s]+1,i)
        break 
    
    d[curr_sum]=i



