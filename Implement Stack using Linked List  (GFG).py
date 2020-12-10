"""   
Key : Stacks are LIFO(Last in First Out) Data Structure
	  they to implement push, pop in O(1) time is to use do it in front side of list rather than back 
	  side. return -1 when the list is empty.
"""

"""
Problem Name   : Implement stack using Linked List
Problem Url    : https://practice.geeksforgeeks.org/problems/implement-stack-using-linked-list/1#
Solution Video : https://www.youtube.com/watch?v=T_UXDTy23DQ
                 

Learning:
	Brute: **IMPORTANT**
		dont use usual way to create an Linked list (bottom up). you may think of having a head node and end node
		and we can push element in O(1) time using end node. but you cant pop it because ones you pop
		one element you loose connection to previous list. you may think of having an variable Prev 
		and store prev node but even it fails after you pop you wont have link to node before prev.
		it takes O(N) to traverse from head to tail and to pop tail element no matter what you do

		Push:O(1)
		head --> None
		head --> |_Node1_| -->None
		head --> |_Node1_| --> |_Node2_| -->None
		head --> |_Node1_| --> |_Node2_| --> |_Node3_| -->None
		head --> |_Node1_| --> |_Node2_| --> |_Node3_| --> |_Node4_| -->None

		Pop:O(n)
		head --> |_Node1_| --> |_Node2_| --> |_Node3_| -->None
		head --> |_Node1_| --> |_Node2_| -->None
		head --> |_Node1_| -->None
		head --> None

	Optimal:
		the optimal approach is to build LL by top down. add or remove element on top side.

		Push:O(1)
		head --> None
		head --> |_Node1_| -->None
		head --> |_Node2_| --> |_Node1_| -->None
		head --> |_Node3_| --> |_Node2_| --> |_Node1_| -->None
		head --> |_Node4_| --> |_Node3_| --> |_Node2_| --> |_Node1_| -->None

		Pop:O(1)
		head --> |_Node3_| --> |_Node2_| --> |_Node1_| -->None
		head --> |_Node2_| --> |_Node1_| -->None
		head --> |_Node1_| -->None
		head --> None



	
"""	


# Class to represent a node
class StackNode:
	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
    def __init__(self):
        self.top=None

    # The method push to push element into the stack
    def push(self, data):
        newNode=StackNode(data)
        newNode.next=self.top
        self.top=newNode

    def pop(self):
        val=-1
        if self.top!=None:
            val=self.top.data
            self.top=self.top.next
        return(val)


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = Stack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends