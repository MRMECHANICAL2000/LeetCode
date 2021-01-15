"""   
Key : Make sure you cover the base case properly

"""

"""
Problem Name   : Search in a Binary Search Tree
Problem Url    : https://leetcode.com/problems/search-in-a-binary-search-tree/
Solution Video :                  

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> using the property of binary tree. simialir to binary search, check the
					if root==val same return True, if root<val, recurse on left subTree		
					if root>val recurse on right subTree. 
"""	


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	#Optimal Solution
    def searchBST(self, root, val):
        if root==None: 			#Base Case if value not found or Tree is empty
            return(None)
        
        if root.val==val:
            return(root)
        
        elif root.val<val:
            return(self.searchBST(root.right,val))
        
        else:
            return(self.searchBST(root.left,val))