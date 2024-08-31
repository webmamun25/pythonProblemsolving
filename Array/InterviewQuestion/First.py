class Max_subArray:
    def __init__(self,L):
        self.L=L
        self.naive_function()
        self.kadanes_algo()
        
    
    def naive_function(self):
        
        self.d={}
        for i in range(0,len(self.L)):
            subarray=[]
            for j in range(i,len(self.L)):
                subarray.append((self.L[j]))
                self.d[sum(subarray)]=subarray
            
        max_val=(max(self.d.keys()))  

        for i in self.d:
            if i==max_val:
                print(self.d[i])


        
    def kadanes_algo(self):
        self.sum=0
        self.max_val=self.L[0]

        for i in range(0,len(self.L)):
            self.sum=self.sum+self.L[i]
            self.max_val=max(self.sum,self.max_val)
            if(self.sum<0):
                self.sum=0
        print(self.max_val)


naive_obj=Max_subArray([-2,4,7,-1,6,-11,14,3,-1,-6])
