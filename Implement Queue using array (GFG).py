"""   
Key : Dont forget Queue are FIFO(First In First Out) Data Structure 
	  Make sure to return -1 when the queue is empty

"""

"""
Problem Name   : Implement queue using array
Problem Url    : https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1
Solution Video :   
                 

Learning:
	Brute:
		dont need to remove element just have an variable that points to which element are yet in arr.
		use append to push to last. use an variable top to pop from front and increment that variable
	
"""	

class MyQueue:
    def __init__(self):
        self.arr=[]
        self.top=0  #Key to solve this question **IMPORTANT**
        
    def push(self, x):
        self.arr.append(x)
         
    def pop(self):
        val=-1
        if self.top<len(self.arr):
             val=self.arr[self.top]
             self.top+=1
        return(val)


#{ 
#  Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
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