"""   
Key : Dont forget stack are LIFO(Last In First Out) Data Structure 
	  Make sure to return -1 whent the stack is empty

"""

"""
Problem Name   : Implement stack using array
Problem Url    : https://practice.geeksforgeeks.org/problems/implement-stack-using-array/1#
Solution Video :   
                 

Learning:
	Brute:
		Using inbuild append and pop method create a stack. make sure to return -1 when the pop is
		called on empty stack.
	
"""	

class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Adds element to the Stack
    def push(self,data):
        self.arr.append(data)
    
    #Removes element from the stack
    def pop(self):
        if self.arr:
            return(self.arr.pop())
        return(-1)                     #**IMPORTANT** Make sure to return -1 when the stack is empty
   

#{ 
#  Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyStack()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends

