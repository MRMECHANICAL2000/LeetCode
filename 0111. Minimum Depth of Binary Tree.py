"""   
Key : 
"""

"""
Problem Name   : Minimum Depth of Binary Tree
Problem Url    : https://leetcode.com/problems/minimum-depth-of-binary-tree/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as max depth,just we take min of left and right tree and +1 to it if
                    both left and right subTree exist. if only one exist we move by that path.

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return(0)
        
        leftTreeDepth=0
        rightTreeDepth=0
        if root.left:
            leftTreeDepth=self.minDepth(root.left)
        if root.right:
            rightTreeDepth=self.minDepth(root.right)
            
        #Only Change Code
        return((1+min(leftTreeDepth,rightTreeDepth)) if leftTreeDepth and rightTreeDepth else 1+leftTreeDepth+rightTreeDepth)