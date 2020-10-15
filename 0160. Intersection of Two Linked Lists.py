"""
Key : Take care of Edge case, what if No intersection , empty list , Infinity Loop **IMPORTANT**
"""

"""
Problem Name   : Find intersection point of Y LinkedList
Problem Url    : https://leetcode.com/problems/intersection-of-two-linked-lists/
Solution Video : https://youtu.be/IpBfg9d4dmQ   **IMPORTANT** 

Learning:
	Brute:
		store all node of one list in Hash table , traverse through another list, there if you find 
		an node in Hash table then thats the intersecting node. O(N) Space

	Better:
		run through entire list and find their length. biglen-smallen , start bignode from that point 
		now return the 1st node in which both intersects. O(2N) time
		

	Optimal: **IMPORTAT**
		Approach -> just iterate through the listA and listB, if you reach end of listA take its pointer
					and point to listB, |||ly if you reach end of listB take its pointer and point to 
					listA. break when both nodeA and nodeB are same it happens if there is intersection 
					or both list become None. In better approach we manually make both to come to start
					point hear automatically they come to same starting point. See Video for clarity
					**IMPORTANT**

"""	

class Solution:
	#Optimal 
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if headA==None or headB==None:            #Edge Case : Empty list  **IMPORTANT**
            return(None)
        
        tempA=headA
        tempB=headB
        while headA!=headB:   
            headA=headA.next    #if they both not same first go to next node then check for None
            headB=headB.next    #else it become an infinite loop. Edge Case **IMPORTANT**
        
            if headA==None and headB==None:       #Edge Case : No Intersection **IMPORTANT**
                return(None)
        
            elif headA==None:
                headA=tempB
            elif headB==None:
                headB=tempA

        return(headA)