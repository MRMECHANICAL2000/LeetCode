"""   
Key : looking from right side what are the nodes you can see is the right side view question.
	  similarely we have left side view, left&right side view that can be solved by this
	  question
"""

"""
Problem Name   : Binary Tree Right Side View
Problem Url    : https://leetcode.com/problems/binary-tree-right-side-view/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> do level order traversal and save last node at each level.


"""	


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return([])
        queue=deque()
        queue.append(root)
        ans=[root.val]

        while queue:
            tempQue=deque()
            while queue:
                popNode=queue.popleft()
                if popNode.left:
                    tempQue.append(popNode.left)
                if popNode.right:
                    tempQue.append(popNode.right)     
                    
            queue=tempQue
            if tempQue:
                ans.append(tempQue[-1].val)

        return(ans)