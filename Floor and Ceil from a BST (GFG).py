"""   
Key : 
"""

"""
Problem Name   : Floor and Ceil from a BST
Problem Url    : https://www.geeksforgeeks.org/floor-and-ceil-from-a-bst/
Solution Video : 

Learning:
	Brute:
		

	Better:


	Optimal: **IMPORTANT**
		Approach -> similair to finding next greater element approach.

"""	

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def floorAndCeil(self, root,Target):

        floor=-1
        ceil=-1
        if not root:
            return(floor,ceil)
        
        while root:
            if root.val==Target:
                floor=root.val
                ceil=root.val
                break
            if root.val<Target:
            	floor=root.val
            	root=root.right
            elif:
            	ceil=root.val
            	root=root.left

        return(floor,ceil)
        
        
