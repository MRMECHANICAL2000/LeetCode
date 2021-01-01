"""   
Key : key to solve the question is to catsh the min value in each position
""" 

"""
Problem Name   : Min Stack
Problem Url    : https://leetcode.com/problems/min-stack/
Solution Video : https://www.youtube.com/watch?v=nGwn8_-6e7w
				 **IMPORTANT** Must watch the video to know API,ADT **IMPORTANT**
                 
Learning:
	Brute:
		check the min() of entire stack each time to find min. takes O(n) for each getMin() operation
.

	Optimal: **IMPORTANT**
		Approach -> the key to unlock the getmin() in O(1) time, is to store the min value in each
					location. ie,we know what is min on each location just cash the minimum value
					in each location and return it in O(1) time. but it takes O(n) space. 
					we can optimize it by using seperate array to store the minVal which reduce
					space drastically in best case scenaior.
"""	



class MinStack:
	#Optimal Approach
    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        prevMin=self.getMin()
        self.stack.append([x,min(prevMin,x)])  #Cashing the min value at each index

    def pop(self) -> None:
        return(self.stack.pop()[0] if self.stack else -1)
        
    def top(self) -> int:
        return(self.stack[-1][0] if self.stack else -1)

    def getMin(self) -> int:
        return(self.stack[-1][1] if self.stack else float('inf'))
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()