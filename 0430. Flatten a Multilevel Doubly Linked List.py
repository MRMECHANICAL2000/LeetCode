"""
Key : Note that it is an doubly linked list, can solve this problem recursively.
	  Must do it and see, because it has lot of edge cases **IMPORTANT**
"""

"""
Problem Name   : Flatten a Multilevel Doubly Linked List
Problem Url    : https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
Solution Video : https://youtu.be/RIyPgR7AF7M  

Learning:
	Brute:
		creating a new linked List


	Optimal: **IMPORTAT**
		Approach -> playing with pointer, using an recursive approach, if we find an child recurse on it
					and find end of it, return the end of it. then take that end and point to current
					nodes next node. **IMPORTANT**

"""	

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	#Optimal 
    def flatten(self, head: 'Node') -> 'Node':
        def flatList(head):            
            prev=None
            cur=head
            nxt=None
            while cur!=None:
                nxt=cur.next
                if cur.child:                    #If child found recursre and find the end of the list
                    temp=flatList(cur.child)
                    if temp==None:               #If child is None break and return prev pointer
                        break
                    cur.next=cur.child
                    cur.child.prev=cur
                    cur.child=None
                    temp.next=nxt
                    if nxt==None:               #if next pointer None continue to change prev to cur point
                        continue                #and return the current pointer
                    nxt.prev=temp

                prev=cur
                cur=nxt

            return(prev)                         #Return end of the list

        temp=flatList(head)                      #head of the recursive function
        return(head)
