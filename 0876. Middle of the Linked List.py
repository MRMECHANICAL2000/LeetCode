"""
Key : Tortoise Two pointer Method  EDGE case: when len is even, mid pointer be at left or right?
	  Look video for it ,just an small change in code required**IMPORTANT**
"""

"""
Problem Name   : Middle of the Linked List
Problem Url    : https://leetcode.com/problems/middle-of-the-linked-list/
Solution Video : https://youtu.be/sGdwSH8RK-o **IMPORTANT** 

Learning:
	Brute: 
		Traverse the list to entire length. find length of it .then again traverse to find mid.
		O(N+N/2) runtime
		

	Optimal: **IMPORTAT**
		Approach -> Using Tortoise two pointer method. move slow 1 step , fast two step, when fast or
					fast.next is None break. return slow pointer, it will be at mid.

"""	

class Solution:
	#Optimal
    def middleNode(self, head: ListNode) -> ListNode:
        slow=head                                #Initially point both to head, not to None or other stuff
        fast=head
        while fast!=None and fast.next!=None: #**IMPORTAT** both fast & fast.next should not be None
            fast=fast.next.next               #because fast!=None to take care if len()=[] and len()=even
            slow=slow.next                    #fast.next!=None to take care if len()=odd
        return(slow)
            