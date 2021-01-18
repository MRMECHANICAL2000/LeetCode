"""   
Key : n-array tree only has preorder and postorder not inorder because we are not having
	  binary tree, we have children array. think twise to understand. 
	  **IMPORTANT**
"""

"""
Problem Name   : N-ary Tree Preorder Traversal
Problem Url    : https://leetcode.com/problems/n-ary-tree-preorder-traversal/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as binary tree preorder traversal, instead of left,right child
					we recurse on each children.

"""	


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:     
        if not root:
            return([])
        element=[]
        element.append(root.val)

        if root.children:
            for child in root.children:
                element.extend(self.preorder(child))
        return(element)