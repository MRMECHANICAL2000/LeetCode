"""   
Key : Queue are FIFO(First in First Out) Data Structure
	  add value to back and remove value from front
"""

"""
Problem Name   : Implement Queue using Linked List
Problem Url    : https://practice.geeksforgeeks.org/problems/implement-queue-using-linked-list/1
Solution Video :                

Learning:
	Brute: **IMPORTANT**
		use end variable to add element to end and use top variable to remove element from top

		Push:O(1)
		head --> None
		head --> |_Node1_| -->None
		head --> |_Node1_| --> |_Node2_| -->None
		head --> |_Node1_| --> |_Node2_| --> |_Node3_| -->None
		head --> |_Node1_| --> |_Node2_| --> |_Node3_| --> |_Node4_| -->None

		Pop:O(1)
		head --> |_Node2_| --> |_Node3_| --> |_Node4_| -->None
		head --> |_Node3_| --> |_Node4_| -->None
		head --> |_Node4_| -->None
		head --> None

"""	
# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head=None      #**IMPORTANT** Key to solve this question is to use this two variable
        self.tail=None
    
     # Method to add an item to the queue
    def push(self, item): 
        newNode=Node(item)
        if self.head==None:
            self.head=newNode
        else:
            self.tail.next=newNode

        self.tail=newNode
         
    # Method to remove an item from queue
    def pop(self):
        val=-1
        if self.head!=None:
            val=self.head.data
            self.head=self.head.next
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