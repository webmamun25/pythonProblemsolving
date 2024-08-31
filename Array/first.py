# Maximum sum subarray

# L=[-2,4,7,-1,6,-11,14,3,-1,-6]

# d={}

# for i in range(0,len(L)):
#     subarray=[]
#     for j in range(i,len(L)):
#        subarray.append(L[j])
#        print(subarray)
#        d[sum(subarray)]=subarray

# max_val=max(d.keys())
# for i in d:
#     if i== max_val:
#         print(d[i])

# time complexity o(n^2)

# Kadens algo 
# import sys
L=[-2,4,7,-1,6,-11,14,3,-1,-6]

curr_sum=0
curr_seq=[]
# best_sum=-sys.maxsize-1
best_sum=0
best_seq=[]

for i in L:
    if i+curr_sum>i:

        curr_sum+=i 
        curr_seq.append(i)
    else:
        curr_sum=i
        curr_seq.clear()
        curr_seq.append(i)
    if curr_sum>best_sum:
        best_sum=curr_sum
        best_seq=curr_seq 
print(best_sum,best_seq)