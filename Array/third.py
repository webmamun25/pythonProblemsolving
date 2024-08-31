
import sys 

def largest_number(L):
    largest_number=L[0]

    for i in L:
        if(largest_number<i):
            largest_number=i
            return largest_number

def smallest_number(L):
    smallest_number=L[0]

    for i in L:
        if(smallest_number>=i):
            smallest_number=i
            return smallest_number

L=[3,42,33,4,5]
print(largest_number(L))
print(smallest_number(L))