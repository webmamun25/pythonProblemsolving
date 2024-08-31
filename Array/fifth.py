def Binary_search(L,key):
    start=0
    end=len(L)
    
    while(start<=end):
        mid=(start+end)//2
        if(L[mid]==key):
            print("{} is Found ".format(key))
        if(L[mid]<key):
            start=mid+1
        else:
            end=mid-1
    return -1


Binary_search([2,3,4,51,1,9],3)