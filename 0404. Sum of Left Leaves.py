"""   
Key : 
"""

"""
Problem Name   : Sum of Left Leaves
Problem Url    : https://leetcode.com/problems/sum-of-left-leaves/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> Same code as BFS or DFS, just while storing node store wheather
                    it is left child or right child. finally when you reach a leaf node
                    check if its leftChild. if yes add it to the answer 

"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root :
            return(0)
        queue=deque()
        queue.append((root,False))    #**IMPORTANT** Storing if the node is leftChild
        ans=0

        while queue:
            tempQue=deque()
            while queue:
                popNode,is_left=queue.popleft()
                if popNode.left:
                    tempQue.append((popNode.left,True))
                if popNode.right:
                    tempQue.append((popNode.right,False))
                    
                if not popNode.left and not popNode.right:
                    if is_left:          #Adding the leaf node to final ans if its left leaf
                        ans+=popNode.val

            queue=tempQue
        return(ans)