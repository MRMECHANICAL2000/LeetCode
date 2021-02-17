"""   
Key : "".join(array) -> you can only convert an array of string into string by join not an 
	  array of integer into string.
	  **IMORTANT**
"""

"""
Problem Name   : Sum Root to Leaf Numbers
Problem Url    : https://leetcode.com/problems/sum-root-to-leaf-numbers/
Solution Video : 

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT**
        Approach -> first find all the root to leaf path using Dfs, then convert all path
        			into an number, then add all the number return

""" 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        allPaths=[]
        def rootToLeaf(root,path):
            if not root:
                return()

            path.append(str(root.val))
            if not root.left and not root.right:
                allPaths.append(path)
                return()
            if root.left:
                rootToLeaf(root.left,path[:])
            if root.right:
                rootToLeaf(root.right,path[:])
                
        rootToLeaf(root,[])
        return(sum([int("".join(i)) for i in allPaths]))