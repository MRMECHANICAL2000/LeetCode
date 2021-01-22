"""   
Key : 
	  **IMPORTANT**
"""

"""
Problem Name   : Construct Binary Search Tree from Preorder Traversal
Problem Url    : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
Solution Video : 

Learning:
	Brute:

	Better:

	Optimal: **IMPORTANT**
		Approach -> we know 1st element in preOrder is the root element. after that we travese
					the preorder array to find the pivot element ie,1st element to the right
					which is greater than the root element. now the element to the left of 
					pivot element are the preorder of the left subTree and the element to the 
					right of pivot are preorder of right subTree. 

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder==[]:
            return(None)

        newNode=TreeNode(preorder[0])
        pivot=len(preorder)

        for i in range(1,len(preorder)):
            if preorder[i]>preorder[0]:
                pivot=i
                break

        leftPreorder=preorder[1:pivot]
        newNode.left=self.bstFromPreorder(leftPreorder)
        rightPreorder=preorder[pivot:]
        newNode.right=self.bstFromPreorder(rightPreorder)        
        
        return(newNode)