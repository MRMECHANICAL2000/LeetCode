"""   **IMPORTANT**
Key : Dirty trick must watch video. check if random pointer pointing to None even 1st node can point to 
	  None. even random Node can point to None check both newNode and randNode !=None before doing other
	  stuff. here take care of empty of one head, if it is one head it's random can point to None or it
	  can also point to itself.
	  Must do it and see, because it has lot of edge cases **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Clone a Linked List with random and next pointer
Problem Url    : https://leetcode.com/problems/copy-list-with-random-pointer/
Solution Video : https://youtu.be/xbpUHSKoALg     **IMPORTANT** Must Watch

Learning:
	Brute:
		use Hash Table to store the Node position and randomNode postion. use it while creating new
		node to point to that specific random node in new list

	Optimal: **IMPORTAT**
		Approach -> inserting new node in original linked list, do some dirty trick then remove our
					inserted Node. look video for dirty trick **IMPORTANT**

"""	

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	#Optimal 
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head==None:              #Edge Case when head is None
            newNode=None
            return(newNode)

        if head.next==None:          #Edge Case if there is one head
            newNode=Node(head.val,None,None)     #if head random points to None
            newNode.random=None if head.random!=head else newNode  #if head random points to itself
            return(newNode)

        #Inserting dummy Node next to each Node
        dummy=head
        while dummy!=None:
            nxt=dummy.next
            newNode=Node(dummy.val,dummy.next)
            dummy.next=newNode
            newNode.next=nxt
            dummy=dummy.next.next

        #Making inserNode node random points to its position  has lot of edge cases hear           
        real=head
        while real!=None:
            inserNode=real.next
            if real.random!=None:                 #if real node random is not None point next of real Node
                inserNode.random=real.random.next #random to insertedNode random
            else:
                inserNode.random=None
            real=real.next.next
        
        #Seperating the inserted Node from the real Node
        newHead=head.next
        real=head
        while real!=None:
            inserNode=real.next
            real=real.next.next
            if inserNode.next!=None:
                inserNode.next=inserNode.next.next
            else:
                inserNode.next=None
                
        return(newHead)