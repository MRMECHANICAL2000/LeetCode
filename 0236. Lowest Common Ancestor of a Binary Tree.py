"""   
Key : LCA means lowest common Ancestor not longest ... look the code for optimization.
	  Node that are above the CurNode are ancestor of curNode
	  Node that are below the CurNode are descendant of curNode
	  **IMPORTANT**
"""

"""
Problem Name   : Lowest Common Ancestor of a Binary Tree
Problem Url    : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Solution Video : https://youtu.be/py3R23aAPCA

Learning:
	Brute:

	Better:
		Traverse the tree and find the path to node p,q. store the path in a list. compare
		both the list and return the lowest common ancestor.

	Optimal: **IMPORTANT**
		Approach ->  using Recursion, we just traverse the tree ordinarely. we have 3 choice
					 we either find the p or q or we end up at leaf node None. if we reach
					 any of this case we return them. other than that we recurse on leftTree
					 and rightTree , call the same function with sameparameter in the left,right
					 subTrees. eventually the recursive call ends are in both left,right subTree
					 we get return values if both are None it means no where the required node is
					 found and curNode cant be the ancestor. if any one of them has return values
					 it means the curNode is in the path of ancestor so we again push the node
					 we get true up in the recursive call. if both left,right call has return value
					 it means the curNode is the ancestor (1st time we are meeting it), so we return
					 the curNode instead of left,rightTree Node. finally the curNode get pushed up
					 in the recursive call and we get it as output.

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
    	#Code runs 18% Faster My Code
        '''
        if root==None or root==p or root==q:
            return(root)
        
        leftTree=self.lowestCommonAncestor(root.left,p,q)
        rightTree=self.lowestCommonAncestor(root.right,p,q)
        
        if leftTree and rightTree:
            return(root)
        else:
            return(leftTree if leftTree else rightTree)
        '''

        #Highly Effective and Faster code
        #Both are same code by this code runs 100% Faster CP Code **IMPORTANT**
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right

