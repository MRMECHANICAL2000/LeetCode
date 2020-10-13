"""
Key : changing pointer of linked list to make it sort. Make sure to point temp to l2
	  at last. "temp.next=l2"  then only last node points to other list. dont do some other 
	  stupid things like l1 to l2 or l2 to l1 **IMPORTANT**
"""

"""
Problem Name   : Merge two sorted Linked List
Problem Url    : https://leetcode.com/problems/merge-two-sorted-lists/
Solution Video : https://youtu.be/Xb4slcp1U38   **IMPORTANT** 

Learning:
	Brute:
		Take two pointer to two list, check which is small and insert it to an new linked list.
		Takes O(N+M) space

	Optimal: **IMPORTAT**
		Approach 1-> swaping the pointer in two linked list. In place swap. O(1) space
		Approach 2-> Always keep l1 as smaller value, so code is reduced into half. Must watch 
					 video to understand this. **IMPORTANT**

"""	

class Solution:
	#Optimal Approach 2
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:                #Taking care of Edge Case
            return(l2)
        elif l2==None:
            return(l1)
                                                       #Always keep small element in l1 **IMPORTANT**
        l1,l2=[l1,l2] if l1.val<l2.val else [l2,l1]    #Toppers trick Most optimized **IMPORTAT**
        head=l1
        temp=l1

        while l1!=None and l2!=None:
            
            if l1.val<=l2.val:
                temp=l1
                l1=l1.next
                continue

            temp.next=l2
            l1,l2=[l1,l2] if l1.val<l2.val else [l2,l1]

            							#**IMPORTANT** think carefully to understand why we do it
        temp.next=l2                    #At last remaining is take the temp node and point to max node
        return(head)