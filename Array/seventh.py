# Pairs 



def Pairs(L):
    for i in range(0,len(L)+1):
        for j in range(i+1,len(L)):
            print( "({},{})".format(L[i],L[j]),end="")








numbers=[2,4,6,8,10]

Pairs(numbers)