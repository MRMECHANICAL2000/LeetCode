"""
Key : Flyord Cycle 2 pointer Turtle and Hare Algorithm
	  Algorithm name is Flyord cycle algo not kargers **IMPORTANT**
"""

"""
Problem Name   : Remove a cycle in Linked List
Problem Url    : https://leetcode.com/problems/linked-list-cycle-ii/
Solution Video : https://youtu.be/32Ll35mhWg0     **IMPORTANT** Look video for proof of Floyd's cycle algorithm
				 https://youtu.be/FkBm3NeWqak	  **IMPORTANT** 

Learning:
	Brute:
		using a hashtable to store previous visited node, if curNode in Table return Node

	Optimal: **IMPORTAT**
		Approach -> Floyd’s Cycle-Finding Algorithm or Floyd’s 2 pointer Algorithm or 
					Turtle and Hare algorithm

"""	

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	#Optimal 
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=head
        fast=head
        while True:
            if fast==None or fast.next==None:
                return(None)
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        fast=head
        
        while fast!=slow:
            fast=fast.next
            slow=slow.next
        return(slow)
 
        
        