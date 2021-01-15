"""   
Key : understand the iterative approach as well. recursive just look code all will be clear

The order in which we traverse the root node given rise to this traversals, all these 3 traversal
comes under DFS(Depth First Search)

InOrder   -> [left,root,right]
preOrder  -> [root,left,right]
postOrder -> [left,right,root]
"""

"""
Problem Name   : Binary Tree Preorder Traversal
Problem Url    : https://leetcode.com/problems/binary-tree-preorder-traversal/
Solution Video : https://youtu.be/K2ybI-GEHSY  -> Iterative Approach
				 **IMPORTANT**
Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> do either recursive or iterative approach.
					Recursive:
						[root]+[funCall(left)]+[funCall(right)]
					Iterative:
						same code as inorder only one line varies

						using stack, take root node and put it in stack,let curNode=root
						we loop until both stack empty and curNode is None. at each iter
						we check if curNode==None if not we add it to answer we loop to its left
						node we append this node to the stack, if yes we pop the last node from 
						stack and make curNode point to right node of popNode. this will
						give us preOrder Traversal

"""	


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	#Optimal Approach
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #Iterative Approach
        preorderTraversal=[]
        stack=[]
        curNode=root
        while curNode!=None or stack:
            if curNode!=None:
                preorderTraversal.append(curNode.val)
                stack.append(curNode)
                curNode=curNode.left
            else:
                popNode=stack.pop()
                curNode=popNode.right
            
        return(preorderTraversal)

                
        #Recursive Approach
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right) if root!=None else []