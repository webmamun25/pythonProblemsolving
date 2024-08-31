
def main(L):
    for i in range(1,len(L)-1):
        flag=True

        for j in range(0,i):
            if(L[j]>L[i]):
                flag=False 
        
        for k in range(i+1,len(L)):
            if(L[k]<L[i]):
                flag=False 
        
        if flag:
            print(L[i])



def second_solution(L):
    for i in range(1,len(L)-1):
        if(max(L[:i])<L[i]<min(L[i+1:])):
            print(L[i])


def third_sol(L):
    max_arr=[]
    max_val=L[0]
    min_arr=[]
    min_val=L[-1]
    for i in L:
        if i>max_val:
            max_val=i 
        max_arr.append(max_val)
    
    for i in range(len(L)-1,-1,-1):
        if L[i]<min_val:
            min_val=L[i]
        min_arr.insert(0,min_val)
   
    for i in range(1,len(L)-1):
        if max_arr[i-1]<L[i]<min_arr[i+1]:
            print(L[i])


L=[3,1,2,5,8,7,9]
second_solution(L)
third_sol(L)
main(L)




