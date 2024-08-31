# /*
# *   
#     *****
#     *   *
#     *   *
#     *****
    

# */

# solution 

# 1.First we have to think about how many lines we need to print 
# 2.think about inner loop condition how to achieve this 
# 3.Right now we see that first row and last row have all Star .In the other hand,row 2 and 3 only have 2 start their postion is j=1 and j=4 

n=int(input("Enter the total lines:"))
# for i in range(1,n+1):
#         for j in range(1,n+2):
#             if(i==1 or i==4 or j==1 or j==5):
#                 print("*",end='')
#             else:
#                 print(' ',end='')
#         print()
        

for i in range(1,n+1):
    if(i==1 or i==4):
        for j in range(1,n+2):
            
            print('*',end="")
        print()
    elif(i==2 or i==3):
        for j in range(1,n+2):
            if(j==1 or j==5):
            
                print('*',end="")
            else:
                print(" ",end="")
        print('',end='')

    

        print()
   