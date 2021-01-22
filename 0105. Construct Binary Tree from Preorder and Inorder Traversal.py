"""   
Key : closely watch the clues in the question.
	  **IMPORTANT**
"""

"""
Problem Name   : Construct Binary Tree from Preorder and Inorder Traversal
Problem Url    : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Solution Video : https://youtu.be/9sw8RRsBw6s				 

Learning:
	Brute:

	Better:

	Optimal: **IMPORTANT**
		Approach -> two clues to solve this question
					1. 1st element in preorder is the root element
					2. find the position of root element in inorder, element to its left are
					   the element in the left subTree and element to its right are the element
					   in the right subTree
					we find the curRoot val and recurse on left,right subTree with the splited
					inorder,preorder array. continue until the array become empty

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if preorder==[] or inorder==[]:
            return(None)

        newNode=TreeNode(preorder[0])
        
        leftInorder=inorder[:inorder.index(preorder[0])]
        leftPreorder=preorder[1:len(leftInorder)+1]
        newNode.left=self.buildTree(leftPreorder,leftInorder)
        
        rightInorder=inorder[inorder.index(preorder[0])+1:]
        rightPreorder=preorder[len(preorder)-len(rightInorder):]=
        newNode.right=self.buildTree(rightPreorder,rightInorder)
                
        return(newNode)