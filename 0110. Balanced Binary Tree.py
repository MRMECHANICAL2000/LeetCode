"""   
Key : To check if a Tree is height balanced, we need to find the height of left,right subTree
	  if both are eual or differ by only 1 then its an balanced Tree. **IMPORTANT**
"""

"""
Problem Name   : Balanced Binary Tree
Problem Url    : https://leetcode.com/problems/balanced-binary-tree/
Solution Video : https://youtu.be/LU4fGD-fgJQ

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> Same as height/depth of binary tree code, while recursion back the height
					we also send the if abs(left-right)<=1.if this condition is True then the 
					Tree is balanced.

"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        def heightFind(root):
            if not root:
                return(0,True)		#Small Fitting in Height of Binary Tree Code

            leftHeight=0
            rightHeight=0
            isLeftBalance=True
            isRightBalance=True

            if root.left:
                leftHeight,isLeftBalance=heightFind(root.left)

            if root.right:
                rightHeight,isRightBalance=heightFind(root.right)

            return(1+max(leftHeight,rightHeight),isLeftBalance and isRightBalance and abs(leftHeight-rightHeight)<=1)
        
        return(heightFind(root)[1])