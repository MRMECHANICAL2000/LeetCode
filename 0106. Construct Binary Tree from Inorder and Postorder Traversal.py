"""   
Key : same as inorder and preorder question, here the root element is the last element in 
	  postorder array
	  **IMPORTANT**
"""

"""
Problem Name   : Construct Binary Tree from Inorder and Postorder Traversal
Problem Url    : https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Solution Video : https://youtu.be/s5XRtcud35E

Learning:
	Brute:

	Better:

	Optimal: **IMPORTANT**
		Approach -> two clues to solve this question
					1. last element in postorder is the root element
					2. find the position of root element in inorder, element to its left are
					   the element in the left subTree and element to its right are the element
					   in the right subTree
					we find the curRoot val and recurse on left,right subTree with the splited
					inorder,postorder array. continue until the array become empty

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if postorder==[] or inorder==[]:
            return(None)
        
        root=postorder.pop()
        newNode=TreeNode(root)
        
        leftInorder=inorder[:inorder.index(root)]
        leftPostorder=postorder[:len(leftInorder)]        
        newNode.left=self.buildTree(leftInorder,leftPostorder)
        
        rightInorder=inorder[inorder.index(root)+1:]
        rightPostorder=postorder[len(leftInorder):]
        newNode.right=self.buildTree(rightInorder,rightPostorder)
        
        
        return(newNode)