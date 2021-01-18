"""   
Key : Height means bottom to up(like how we measure human height), depth means top to bottom
	  (like how we see a well).
"""

"""
Problem Name   : Maximum Depth of Binary Tree
Problem Url    : https://leetcode.com/problems/maximum-depth-of-binary-tree/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> to find depth of root, we just need to find the depth of left subTree then
					depth of right subTree and add +1 to max of them. just use this logic
					recursively.

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return(0)
        
        leftTreeDepth=0
        rightTreeDepth=0

        if root.left:          #Depth of left subTree
            leftTreeDepth=self.maxDepth(root.left)

        if root.right:		  #Depth of right subTree
            rightTreeDepth=self.maxDepth(root.right)
            				  #1+max(leftDepth,rightDepth) gives depth of root
        return(1+max(leftTreeDepth,rightTreeDepth))  