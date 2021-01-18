"""   
Key : 
"""

"""
Problem Name   : Binary Tree Zigzag Level Order Traversal
Problem Url    : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as level order traversal, here we have a variable to keep track of the 
					level we are at, just reverse at odd leves and append or while inserting 
					itself appendleft() if its even level.

"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return([])
        queue=deque()
        queue.append(root)
        ans=[[root.val]]
        level=1
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
                ans.append(tempAns if level%2==0 else tempAns[::-1]) #Only change **IMPORTANT**
            level+=1
        return(ans)