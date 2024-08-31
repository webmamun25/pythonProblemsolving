# import ctypes 

# class Mylist:

#     def __init__(self):
#         self.size=1 
#         self.n=0 
#         self.A=self.__make_array(self.size)
    

#     def __len__(self):
#         return self.n 

#     def append(self,item):
#         if self.n==self.size:
#             # resize 

#             self.__resize((self.size*2))

        
#         self.A[self.n]=item 
#         self.n+=1
    
#     def __resize(self,new_capacity):

#         B=self.__make_array(new_capacity)
#         self.size=new_capacity 
#         # copy the content of A to B 
#         for i in range(self.n):
#             B[i]=self.A[i]
#             self.A=B

#     def __str__(self):
#         result=''
#         for i in range(self.n):
#             result+=str(self.A[i])+','
        
#         return '['+result[:-1]+']'


#     def __make_array(self,capacity):

#         return (capacity*ctypes.py_object)()
    


# Myobj=Mylist()

# Myobj.append('hello')
# Myobj.append(2)
# print(Myobj)

import ctypes 

class My_Dynamic:

    def __init__(self) -> None:
        self.size=1
        self.n=0 
        self.A=self.__make_array(2*self.size)


    def __len__(self):
        return self.n

    def append(self,item):

        if self.n==self.size:
            
            self.__resize_array(self.size*2)
        

        self.A[self.n]=item
        self.n+=1
    

    def __resize_array(self,new_capacity):
        B=self.__make_array(new_capacity)

        for i in range (self.n):
            B[i]=self.A[i]
            self.A=B
    
    def __str__(self):
        result=''
        for i in range(self.n):
            result+=str(self.A[i])+','

        return '['+result[:-1]+']'
        

    


    def __make_array(self,capacity):

        return (capacity*ctypes.py_object)()
    

Myobj=My_Dynamic()
print(len(Myobj))
Myobj.append('hello')
Myobj.append(2)
print(Myobj)
