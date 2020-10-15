"""
Key : Has lot of edge cases so try yourself onse. link tail to head and break at correct postion
	  **IMPORTANT**
"""

"""
Problem Name   : Rotate a LinkedList
Problem Url    : https://leetcode.com/problems/rotate-list/
Solution Video : https://youtu.be/Fh8BV3eMKzc

Learning:
	Brute:
		Rotate the list for give no of times and produce output

	Optimal: **IMPORTAT**
		Approach ->  find length of list , join tail of list to head and break (len-k)th node and 
					 return (len-k)+1th Node **IMPORTANT**
"""	

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	#Optimal
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None or head.next==None or k<=0:            #Edge Cases
            return(head)

        count=0                            #Counting the length of the linkedList
        dummy=head
        prev=dummy
        while dummy!=None:
            count+=1
            prev=dummy
            dummy=dummy.next
        else:
            prev.next=head                 #setting last node to point back to head

        
        if k>count:                        #All this this lines are **IMPORTANT** **IMPORTANT**
            k=k%count                       
        iterLen=count-k if count!=k else k #Edge Case: what to do iff k==count , break the kth Node
        								   #not the 0th Node. **IMPORTANT**
        prev=head
        while iterLen>0:
            prev=head
            head=head.next
            iterLen-=1
        else:
            prev.next=None
        return(head)