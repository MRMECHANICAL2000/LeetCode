"""   
Key : easy question but base case is important. if both nodes are None return True else Fasle
"""

"""
Problem Name   : Same Tree
Problem Url    : https://leetcode.com/problems/same-tree/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> using recursion, at each node check if both are same, if yes check if
					both their left, right child are same if yes return True else False.


"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p==None and q==None:   #Base Case
            return(True)

        elif p==None or q==None:
            return(False)
        
        if p.val==q.val: #If both node values are same
            left=True
            right=True
            
            if p.left and q.left:  #if both of them have left node
                left=self.isSameTree(p.left,q.left)

            elif p.left or q.left: #if any one dont have left node return False
                return(False)
            
            if p.right and q.right: #If both of them have right node
                right=self.isSameTree(p.right,q.right)

            elif p.right or q.right: #If any one dont have right node return False
                return(False)

            return(left and right)
        else:
            return(False)
        