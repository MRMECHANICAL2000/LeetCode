"""
Key : Do like simple math. Take care of edge case must loop until carry!=0  **IMPORTANT**
"""

"""
Problem Name   : Add two numbers as LinkedList  
Problem Url    : https://leetcode.com/problems/add-two-numbers/
Solution Video : https://youtu.be/LBVsXSMOIk4   

Learning:
	Brute:
        iterate entirely, make it as a number sum both, then store individual char in linked list
        but this method wont work if length is more than 20. you cant add a no of length more than 20

	Optimal: **IMPORTAT**
		Approach 1-> To be noted that it is given no are in reversed order, so just add add two number 
                     store carry in variable and remaining in newlist and move to next number.repeat 
                     do like what how we add a two number in elementry school

"""	

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #Optimal 
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curSum=0
        curCarry=0
        head=ListNode()
        temp=head                                  #**IMPORTANT**
        while l1!=None or l2!=None or curCarry!=0: #Edge Case Must loop until carry also become 0 **IMPORTANT**
            curSum=0
            curSum+=l1.val if l1!=None else (0) 
            curSum+=l2.val if l2!=None else (0) 
            curSum+=curCarry
            curCarry=curSum//10
            curSum%=10
            l1=l1.next if l1!=None else None
            l2=l2.next if l2!=None else None
            temp.val=curSum
            newNode=ListNode() if l1!=None or l2!=None or curCarry!=0 else None
            temp.next=newNode
            temp=newNode
            
        return(head)