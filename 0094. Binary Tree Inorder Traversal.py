"""   
Key : understand the iterative approach as well. recursive just look code all will be clear

The order in which we traverse the root node given rise to this traversals, all these 3 traversal
comes under DFS(Depth First Search)

InOrder   -> [left,root,right]
preOrder  -> [root,left,right]
postOrder -> [left,right,root]
"""

"""
Problem Name   : Binary Tree Inorder Traversal
Problem Url    : https://leetcode.com/problems/binary-tree-inorder-traversal/
Solution Video : https://youtu.be/5y_j0OqD7v8  -> Iterative Approach
				 **IMPORTANT**
Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> do either recursive or iterative approach.
					Recursive:
						[funCall(left)]+[root]+[funCall(right)]
					Iterative:
						same code as preOder only one line varies

						using stack, take root node and put it in stack,let curNode=root
						we loop until both stack empty and curNode is None. at each iter
						we check if curNode==None if not we loop to its left
						node we append this node to the stack, if yes we pop the last node from 
						stack we add it to answer and make curNode point to right node of popNode.
						this will give us inOrder Traversal

"""	


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        #Iterative Approach
        inorderTraversal=[]
        stack=[]
        curNode=root
        while curNode!=None or stack:
            if curNode!=None:
                stack.append(curNode)
                curNode=curNode.left
            else:
                popNode=stack.pop()
                inorderTraversal.append(popNode.val)  #Same code as preOrder this one line alone
                									  #changed **IMPORTANT**
                curNode=popNode.right
        return(inorderTraversal)
        
        
        #Recursive Approach
        if root==None:
            return(None)
        element=[]
        
        if root.left:
            element.extend(self.inorderTraversal(root.left))
            
        element.append(root.val)
        
        if root.right:
            element.extend(self.inorderTraversal(root.right))
            
        return(element)

        #Recursive Approach -> One Liner
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root!=None else []
        
