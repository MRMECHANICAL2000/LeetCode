"""   
Key : 
	  **IMPORTANT**
"""

"""
Problem Name   : Peeking Iterator
Problem Url    : https://leetcode.com/problems/peeking-iterator/submissions/
Solution Video : 

Learning:
	Brute:
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as BST Iterator question with small function added, here they
					are asking to implemet a function called peek when returns the 
					next element but wont move the pointer.

					simpely have a variable self.peekEle initlize it to next element
					whenever they ask peek return it, when they ask hasNext return true
					if element in peek when they next() return the value in peek and 
					again initilize the self.peekEle to next element

"""	
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def initilizePeek(self):
        self.peekEle=self.iterator.next() if self.iterator.hasNext() else None
        
    def __init__(self, iterator):
        self.iterator=iterator
        self.peekEle=None
        self.initilizePeek()
        
    def peek(self):
        if self.peekEle:
            return(self.peekEle)
        return(-1)
        

    def next(self):
        if self.peekEle:
            temp=self.peekEle
            self.initilizePeek()
            return(temp)
        

    def hasNext(self):
        if self.peekEle:
            return(True)
        return(False)
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].