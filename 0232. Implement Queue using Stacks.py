"""   
Key : The key is to use two stack. one to push element and other to pop last element. 
	  int, float, string --> Data Types
	  stack, queue --> Abstract Data Types ie,we know this function like push, pop, top will take O(1)
	  				   time but we dont know how it is implemented inside. it can implemented using
	  				   linkedlist or array or stack for queue or queue for stack
""" 

"""
Problem Name   : Implement Queue using Stacks
Problem Url    : https://leetcode.com/problems/implement-queue-using-stacks/
Solution Video : https://www.youtube.com/watch?v=Wg8IiY1LbII **IMPORTANT**
                 
Learning:
	Better:
		push is same as queue takes O(1), but while pop we take all element of stack to reach last
		element and return that last element and put all element back to stack. takes O(n) for
		each operation


	Optimal: 
		Approach -> use two stack, one is to push elemet to stack and other to pop element out of
					stack in O(1) time. push element to pushStack in O(1) time. to pop an element
					pop all element from push stack and append it to pop stack now pop element from
					popStack you will get FIFO in O(1) Amortised time
"""	



class MyQueue:

    def __init__(self):
        self.pushStack=[]
        self.popStack=[]        #**IMPORTANT** key to get O(1) pop time

    def push(self, x: int) -> None:
        self.pushStack.append(x)
        
    def pop(self) -> int:
        val=-1
        if self.popStack==[]:     #if no element in popStack pop element from pushStack append to popStack
            while self.pushStack: #then pop form pop stack. **IMPORTANT**
                self.popStack.append(self.pushStack.pop())

        if self.popStack:
            val=self.popStack.pop()
        return(val)

    def peek(self) -> int:
        val=-1
        if self.popStack==[]:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        if self.popStack:
            val=self.popStack[-1]
        return(val)        

    def empty(self) -> bool:
        return(not (self.pushStack!=[] or self.popStack!=[])) 
        
