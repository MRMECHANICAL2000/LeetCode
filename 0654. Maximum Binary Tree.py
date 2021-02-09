"""   
Key :
	  **IMPORTANT**
"""

"""
Problem Name   : Maximum Binary Tree
Problem Url    : https://leetcode.com/problems/maximum-binary-tree/
Solution Video :                  

Learning:
	Brute:
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> each time find the max value, make it as a node then recure the left half
					of the array for node.left and right half of array for node.right. instead
					of splitting list each time you may use pointer to increase the code speed.

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return(None)

        maxVal=max(nums)
        root=TreeNode(maxVal)
        root.left=self.constructMaximumBinaryTree(nums[:nums.index(maxVal)])
        root.right=self.constructMaximumBinaryTree(nums[nums.index(maxVal)+1:])
        return(root)