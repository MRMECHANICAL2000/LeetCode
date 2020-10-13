"""
Key : Look for edge cases, problem cant be solved until 1st pointer used is an dummy node 
      Must watch video to know edge case **IMPORTANT**
"""

"""
Problem Name   : Remove N-th node from back of LinkedList
Problem Url    : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Solution Video : https://youtu.be/Lhu3MsXZy-Q   **IMPORTANT** Must watch to know edge case

Learning:
	Brute:
		Count the length of list and delete (l-n)th node from begining
		
	Better:
		finding mid and proceding from there

	Optimal: **IMPORTAT**
		Approach 1-> use two pointer, take 1st pointer move to n distance from there start moving 2nd
					 pointer from begining and 1st pointer from there simultaneously until the 1st
					 pointer reach None. the position of 2nd pointer is node to be deleted.
					 **IMPORTANT** Must take care of the edge cases 

"""	

class Solution:
	#Optimal 
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0,head)        #if we are not using dummy node and pointing p1,p2 to it
        							  #the program fails if node to be deleted is last node,1st node
        							  #has only one node and more edge case **IMPORTANT** **IMPORTANT**
        p1=dummy
        p2=dummy
        temp=p2
        i=0

        while i<n:
            p1=p1.next
            i+=1

        while p1!=None:
            p1=p1.next
            temp=p2
            p2=p2.next

        if temp.next==head:           #if the element to be removed is head Edge Case **IMPORTANT**
            head=head.next
        else:
            temp.next=temp.next.next
        return(head)
        
        