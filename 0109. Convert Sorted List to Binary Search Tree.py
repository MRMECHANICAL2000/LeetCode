"""   
Key : Dont think much, think simple your first taught is that find the mid then for that mid
	  put all the value in left side as skewed left tree and all the value in right as skewed 
	  right subTree. but this wont give an height balanced tree. you started the question right
	  but ended in wrong approach.
	  **IMPORTANT**
""" 

"""

Problem Name   : Convert Sorted List to Binary Search Tree
Problem Url    : https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
Solution Video : https://youtu.be/5IQF13nNq6A

Learning:
	Brute:

		
	Better: 


	Optimal: **IMPORTANT**
		Approach -> find mid , its our root, now split the list into two list at the mid
					recursively call it for left,right child. this is similair to binary search
					in linked list.

"""	

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return(None)
        if not head.next:
            return(TreeNode(head.val))
        
        slow=head 				#slow->points to Mid finally **IMPORTANT**
        fast=head.next
        leftTreeEnd=slow 		#End of 1st Linked List , head is the begining of 1st Linked List
        rightTreeStart=slow 	#Begining of 2nd Linked List

        while fast!=None and fast.next!=None:  
            leftTreeStart=slow
            slow=slow.next
            fast=fast.next.next

        #Splitting at the middle and making two Linked List **IMPORTANT**
        rightTreeStart=slow.next
        leftTreeStart.next=None
        slow.next=None
        
        newNode=TreeNode(slow.val) #Creating a BST with mid as root

        if head!=slow:			   #only recurse if head and mid or different **IMPORTNAT**
        						   #if the len(list) is 2 , both slow and head will be same.
            newNode.left=self.sortedListToBST(head) 

        newNode.right=self.sortedListToBST(rightTreeStart) 
               
        return(newNode)