"""   
Key : 

"""

"""
Problem Name   : Lowest Common Ancestor of a Binary Search Tree
Problem Url    : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Solution Video : https://youtu.be/TIoCCStdiFo

Learning:
	Brute:
		find path to node p and q store them in an array, compare the array and find the node
		at which two path diverges it its the LCA.
		
	Better: **IMPORTANT**
		doing the same appraoch as how we did with LCA of Binary Tree, just push the node upward
		if you find p,q or None push them upward in the recursion. see that question for this 
		approach.


	Optimal: **IMPORTANT**
		Approach ->  we can do same optimal approach we did for LCA of BT, but BST has an special
					 property right? we are going to utalize it,
					 if root>p,q -> LCA is in left Tree
					 if root<p,q -> LCA is in right Tree
					 if p<=root<=q or q<=root<=p -> 1st node that satisfies this condition is LCA

					 Easy question, look condition twise you will eventually understand it.

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return(None)
        
        if root.val>p.val and root.val>q.val:
            return(self.lowestCommonAncestor(root.left,p,q))
        
        elif root.val<p.val and root.val<q.val:
            return(self.lowestCommonAncestor(root.right,p,q))

        else:
            return(root)
