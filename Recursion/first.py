
def backtrack(n):

    if n==1:
        print(1)
      
    
    print(n)
    backtrack(n-1)




if __name__ == "__main__":
    

    n=10

    backtrack(n)