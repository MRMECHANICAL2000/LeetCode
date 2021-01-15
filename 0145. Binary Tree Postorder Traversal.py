"""   
Key : Iterative approach of postOrder Traversal differs from both the preOrder and InOrder
	  Traversal techniques
"""

"""
Problem Name   : Binary Tree Postorder Traversal
Problem Url    : https://leetcode.com/problems/binary-tree-postorder-traversal/
Solution Video : https://youtu.be/k21VKEM8OFY  -> Iterative Approach
				 **IMPORTANT** 
Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> do either recursive or iterative approach.
					Recursive:
						[funCall(left)]+[funCall(right)]+[root]

					Iterative: **IMPORTANT**
						using 2 stacks. take the root and insert it on 1st stack. we loop
						until stack1 is empty. pop the last element of stack1, append it to 
						stack2. Append the left and right child of popElement to stack1.
						continue the process. fially reverse the values in stack2 you will get
						the post order traversal


"""	


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	#Optimal Approach
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #Iterative Approach
        if not root:		#Base Case
            return([])

        stack1=[root]
        stack2=[]
        while stack1:
            popNode=stack1.pop()
            stack2.append(popNode.val)
            if popNode.left:
                stack1.append(popNode.left)
            if popNode.right:
                stack1.append(popNode.right)
        return(stack2[::-1])                  #Reversing stack2 gives post order traversal
        									  #**IMPORTATN** 
        
        #Recursive Approach
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val] if root!=None else []