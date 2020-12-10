"""   
Key : you cant do it like how we do for implementing stack using queue. because Queue is FIFO, so even 
	  you take element from 1st queue and put on 2nd it remains the same.
	  know how to return 0th index element from deque wihtout poping it from array
	  There are two ways to do it, either we make push operation costlier and pop,top in O(1) time or we 
      make pop and top costlier and push in O(1) time. 

	  int, float, string --> Data Types
	  stack, queue --> Abstract Data Types ie,we know this function like push, pop, top will take O(1)
	  				   time but we dont know how it is implemented inside. it can implemented using
	  				   linkedlist or array or stack for queue or queue for stack
""" 

"""
Problem Name   : Implement Stack using Queues
Problem Url    : https://leetcode.com/problems/implement-stack-using-queues/
Solution Video : https://www.youtube.com/watch?v=nh1GCPB4j6g **IMPORTANT**
				 **IMPORTANT** Watch to know both approach **IMPORTANT**
                 
Learning:
	Better:
		Making both pop,top costlier and push in O(1) time. ie.each time pop all element from Queue1
		from beginning to Queue2 the last element we pop from Queue1 is the element we need to return.
		then just swap names for Queue1 and Queue2

	Optimal: **IMPORTANT**
		Approach -> Making push costlier and pop,top in O(1) time. if we take entire Queue1 and put on
					Queue2 both will look same but if you do the same from 1st element till last
					ie, evey time you insert a element take previous Queue 1 put on Queue 2, insert
					your new element in Queue1 and put all element back from Queue1 to Queue2.
					look the illustration to understand clearely 

						Queue1 -->  | |                  Queue2 --> | |
					Push1:
						Queue1 -->  |1|                  Queue2 --> | |
					Push2:
						Queue1 -->  |1|                  Queue2 --> | |					
						Queue1 -->  | |                  Queue2 --> |1|					
						Queue1 -->  |2|                  Queue2 --> |1|					
						Queue1 -->  |2,1|                Queue2 --> | |
					Push3:
						Queue1 -->  |2,1|                Queue2 --> | |
						Queue1 -->  | |                  Queue2 --> |2,1|
						Queue1 -->  |3|             	 Queue2 --> |2,1|
						Queue1 -->  |3,2,1|              Queue2 --> | |
					Now when you pop this Queue1 you will get output like stack 

"""	

from collections import deque
class MyStack:
	#Optimal Approach
    def __init__(self):        
        self.Queue1=deque()
        self.Queue2=deque()

    def push(self, x: int) -> None:
        while self.Queue1: 								#Making Push Costlier **IMPORTANT**
            self.Queue2.append(self.Queue1.popleft())
        self.Queue1.append(x)
        self.Queue1.extend(self.Queue2)
        self.Queue2=[]

        
    def pop(self) -> int:
        return(self.Queue1.popleft())        

    def top(self) -> int:
        for i in self.Queue1:   #**IMPORTANT** how to return element in 1st index  
            return(i)           #without poping it from array. just use an for loop
        return(-1)              #take 1st element and return it **IMPORTANT**
    
    def empty(self) -> bool:
        return(not self.Queue1)
        