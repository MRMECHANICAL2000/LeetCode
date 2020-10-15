"""
Key : Updating pointer is tough in this question **IMPORTANT**
	  need 5 pointer, 3 for reverse , 2 to keep track of tail of curNode and head of nextNode.
"""

"""
Problem Name   : Reverse a LinkedList in groups
Problem Url    : https://leetcode.com/problems/reverse-nodes-in-k-group/
Solution Video : https://youtu.be/BfQeP6XEXEc   **IMPORTANT** 

Learning:
	Brute:
		Create a new linked list and insert elements in k groups of reversed order

	Optimal: **IMPORTAT**
		Approach -> Playing with pointer, 1st find len of linkedlist then divide by k to find the
					number of group, you should need to remember tail,head of each group because tail of
					1st group need to be connected to head of 2nd group.||| for other groups
					**IMPORTANT**

"""	

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	#Optimal 
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseList(tail,k):
            prev=None
            cur=tail
            nxt=None
            while k>0:
                nxt=cur.next
                cur.next=prev
                prev=cur
                cur=nxt
                k-=1
            return(prev,tail,nxt)      #prev-> head of revList 
            						   #tail-> tail of revList
            						   #nxt -> head of next list to be reverse
        
        count=0                        #Counting the length of the list, 
        dummy=head                     #Donot use head to count , if we do we loose the entire list
        while dummy!=None:             #because when we update head for counting after counting head
            count+=1                   #will be pinting to None       **IMPORTANT**
            dummy=dummy.next

        if count<=1 or k<=1 or count<k:   #if k==1 or len==1 or len<k no need to reverse, base case
            return(head)
        
        iterCount=count//k             #No of Iteration Needed
        prevTail=head
        cur=head
        nxt=None

        while iterCount>0:               #cur->current head of non-reverse list
        								 #prevTail-> tail of pre-revlist
            prev,tail,nxt=reverseList(cur,k)
            prevTail.next=prev        #Pointing previous tail to head of current reversed node
            if iterCount==count//k:   #for 1st iteratioin alone we need to update head **IMPORTANT**
                head=prev
            prevTail=tail
            cur=nxt
            iterCount-=1
        prevTail.next=nxt
        return(head)
        