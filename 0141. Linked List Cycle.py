"""
Key : Flyord Cycle 2 pointer Turtle and Hare Algorithm
	  Know how to implement Do_while loop in python **IMPORTANT**
"""

"""
Problem Name   : Detect a cycle
Problem Url    : https://leetcode.com/problems/linked-list-cycle/submissions/ 
Solution Video : https://youtu.be/32Ll35mhWg0     **IMPORTANT** Look video for proof of Floyd's cycle algorithm
				 https://youtu.be/FkBm3NeWqak	  **IMPORTANT** 

Learning:
	Brute:
		using a hashtable to store previous visited node, if curNode in Table return Fasle

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
    def hasCycle(self, head: ListNode) -> bool:
        slow=head
        fast=head

        #This is how you implement do while loop in python **IMPORTANT**
        while True:

        	#if slow==None or slow.next==None or fast==None or fast.next==None: #Waste of Time

            if fast==None or fast.next==None:     #No need to check both slow and fast  **IMPORTANT**
                return(False)                     #check only fast because he is the 1st person to reach None
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        return(True)
        
        