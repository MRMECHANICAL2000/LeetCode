"""   
Key : 
	  **IMPORTANT**
"""

"""
Problem Name   : Symmetric Tree
Problem Url    : https://leetcode.com/problems/symmetric-tree/
Solution Video : https://www.youtube.com/watch?v=XV7Sg2hJO3Q
				 

Learning:
	Brute:
		using level order traversal, at each level divide the level array and compare both
		the pieces if all the array in all level are symmertic then the tree is symmetric.
		O(n) space for making level array
	Better:


	Optimal: **IMPORTANT**
		Approach -> 1st check if given L,R is same.if yes we check if (L.left,R.right) are same
					and (L.right,R.left) are same. we do it recursively. if we get true at all
					places the given tree is symmetric, else not.
"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symChec(L,R):
            if not L and not R:
                return(True)
            elif not L or not R:
                return(False)
            
            
            if L.val==R.val:
                return(symChec(L.left,R.right) and symChec(L.right,R.left))
                											#Heart of the code **IMPORTNAT**

            return(False)
        
        if not root:
            return(True)
        return(symChec(root.left,root.right))