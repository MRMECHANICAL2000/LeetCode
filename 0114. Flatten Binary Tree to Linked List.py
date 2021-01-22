"""   
Key : in the optimal approach you taught of using many return node and making it point to 
	  another node. lot of stuff. but the CP coder easily solved it. with just 4 lines of code.
	  **IMPORTANT**
"""

"""
Problem Name   : Flatten Binary Tree to Linked List
Problem Url    : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Solution Video : 
				 https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)
				 #Look the comments for explanation -> Optimally soved person Code 
				 **IMPORTANT** Must see for explanation
				 

Learning:
	Brute:

	Better:
		do preorder traversal, store all nodes in array. then make them into linkedList.

	Optimal: **IMPORTANT**
		Approach -> we do an reverse preoderd like recursion, there we store the last visited
					node data, then when we look a new node we points curNode.right=prev
					make its curNode.left=None and make the prev=curNode.

					Make sure to first flattern the right side node. then come to left side.
"""	


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Better Appraoch -> Using PreOrder Traversal
    def flatten(self, root):

        def preorder(root):  #Preorder Traversal Code
            preOrderEle=[]
            if not root:
                return([])
            preOrderEle.append(root)

            if root.left:
                preOrderEle.extend(preorder(root.left))            
            
            if root.right:
                preOrderEle.extend(preorder(root.right))
            
            return(preOrderEle)

        traversal=preorder(root)
        for idx in range(0,len(traversal)-1):		#Connecting nodes to linkedList
            traversal[idx].right=traversal[idx+1]
            traversal[idx].left=None

        return(root)

    #Optimal Approach -> reverse preOrder in recursive Manner
    def flatten(self, root):
        self.prev=None  #To store the last visited Node

        def helper(root):
            if root==None:
                return()

            helper(root.right) #1st need to look right node to solve this question **IMPORTANT**
            helper(root.left)

            root.right=self.prev
            root.left=None
            self.prev=root

        helper(root)
        return(root)