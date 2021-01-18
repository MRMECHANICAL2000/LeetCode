"""   
Key : 
"""

"""
Problem Name   : Find Bottom Left Tree Value
Problem Url    : https://leetcode.com/problems/find-bottom-left-tree-value/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> do level order traversal and return last level 1st node


"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        
        leftTree=root.val
        queue=deque()
        queue.append(root)
        while queue:
            tempQueue=deque()
            while queue:
                popNode=queue.popleft()
                if popNode.left:
                    tempQueue.append(popNode.left)
                if popNode.right:
                    tempQueue.append(popNode.right)
            queue=tempQueue

            if tempQueue:
                leftTree=tempQueue[0].val #Only change in code **IMPORTANT**
        return(leftTree)