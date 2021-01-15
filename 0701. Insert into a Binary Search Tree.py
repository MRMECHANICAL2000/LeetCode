"""   
Key : 

"""

"""
Problem Name   : Insert into a Binary Search Tree
Problem Url    : https://leetcode.com/problems/insert-into-a-binary-search-tree/
Solution Video :                  

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> do similair to searching and find the position where it can be place and
					insert it in that location. ie, search until you find a empty node , and 
					insert the value in that empty node.
"""	


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	#Optimal Approach
    def insertIntoBST(self, root, val):
        if root==None:
            root=TreeNode(val)
            return(root)
        
        elif root.val<val:
            root.right=self.insertIntoBST(root.right,val)
            
        else:
            root.left=self.insertIntoBST(root.left,val)
        return(root)