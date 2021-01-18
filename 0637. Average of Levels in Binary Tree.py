"""   
Key : 
"""

"""
Problem Name   : Average of Levels in Binary Tree
Problem Url    : https://leetcode.com/problems/average-of-levels-in-binary-tree/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as level order traversal,just find the sum at each level
					and append it to the final answer.

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return([])
        queue=deque()
        queue.append(root)
        ans=[root.val]
        
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
                ans.append(sum(tempAns)/len(tempAns)) 
        return(ans)