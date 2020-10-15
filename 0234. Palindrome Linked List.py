"""
Key : Multiple concept inherited. find Mid,odd or even length,reverse,compare  
	  Take care of edge case, during finding Mid if len==even ok , len==odd means Mid=Mid.next use
	  to skip middle element while reversing  **IMPORTANT**
"""

"""
Problem Name   : Check if a LinkedList is palindrome or not.
Problem Url    : https://leetcode.com/problems/palindrome-linked-list/
Solution Video : https://youtu.be/oZuR2-AKkXE   **IMPORTANT** 

Learning:
	Brute:
		create another linked list in reverse manner and compare. takes O(N) space

	Optimal: **IMPORTAT**
		Approach -> find Mid , break into two linked list, reverse send part after mid
					then compare both list and return result. Make sure to take care of edge case
					like odd,even,one,zero length of list. 		**IMPORTANT**

"""	

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	#Optimal 
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseList(head):             #Code to reverse second Part
            prev=None
            cur=head
            nxt=None
            while cur!=None:
                nxt=cur.next
                cur.next=prev
                prev=cur
                cur=nxt
            return(prev)
        
        def findMid(head):				  #Code to find mid of list
            fast=head
            slow=head

            while fast!=None and fast.next!=None:
                fast=fast.next.next
                temp=slow
                slow=slow.next
            else:
                temp.next=None                   #Breaking int two linked list **IMPORTANT**
                if fast!=None:                   #if len=odd skip mid pointer  **IMPORTANT**
                    slow=slow.next
            return(slow)

        #Program Begins
        if head==None or head.next==None:
            return(True)

        mid=findMid(head)
        head1=head
        head2=reverseList(mid)        
        
        #Comparing two Linked List ie,checking if it is palindrome
        while head2!=None:
            if head2.val!=head1.val:
                return(False)
            head2=head2.next
            head1=head1.next
        else:
            return(True)