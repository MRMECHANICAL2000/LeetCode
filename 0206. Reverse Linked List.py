"""
Key : Not simple as you think, try both recursive and iterative approach **IMPORTANT**
"""

"""
Problem Name   : Reverse a Linked List
Problem Url    : https://leetcode.com/problems/reverse-linked-list/
Solution Video : https://youtu.be/O0By4Zq0OFc **IMPORTANT** Must Watch

Learning:
	Brute: 
		create a new linked list and put element from here to there. Takes O(N) extra space

	Optimal: **IMPORTAT**
		Approach -> No need to create a new Linked list , just reverse all the pointers  **IMPORTANT**
					Must use 3 pointers, prev,cur,nxt. 

"""	

class Solution:
	#Optimal Iterative
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:              # Edge Case what if list is empty=[] dont forget this **IMPORTANT**
            return(head)

        prev=None                   # Use these 3 different pointers, dont use head as one pointer it 
        cur=head                    # become confusing
        nxt=None

        while cur!=None:
            nxt=cur.next            
            cur.next=prev
            prev=cur
            cur=nxt
        return(prev)               #Return Previous pointer because cur,nxt both in None **IMPORTAT**


    #Optimal Recursive
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(head):                      #**REMEMBER** each piece of code is important
            if head==None or head.next==None:   #Both head and head.next should not be None **IMPORTANT**
                return(head)
            else:
                CurFinal=reverse(head.next)
                head.next.next=head
                head.next=None
                return(CurFinal)
        return(reverse(head))
