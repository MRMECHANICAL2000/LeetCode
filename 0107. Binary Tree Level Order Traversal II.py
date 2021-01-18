"""   
Key : 
"""

"""
Problem Name   : Binary Tree Level Order Traversal II
Problem Url    : https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as level order traversal,just reverse the final solution and 
					return it or while appending the solution appendleft

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return([])
        queue=deque()
        queue.append(root)
        ans=[[root.val]]
        
        while queue:
            tempQue=deque()
            tempAns=[]
            while queue:
                popNode=queue.popleft()
                if popNode.left:
                    tempQue.append(popNode.left)
                    tempAns.append(popNode.left.val)
                if popNode.right:
                    tempQue.append(popNode.right)            
                    tempAns.append(popNode.right.val)
            queue=tempQue
            if tempAns:
                ans.append(tempAns) 
        return(ans[::-1])  #Only Change **IMPORTANT**