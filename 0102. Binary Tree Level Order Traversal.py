"""   
Key : Iterative Appraoch is easy, just look how the recursive work from code.
	  level order traversal is an BFS technique.
"""

"""
Problem Name   : Binary Tree Level Order Traversal
Problem Url    : https://leetcode.com/problems/binary-tree-level-order-traversal/
Solution Video : https://youtu.be/MBZ-gBkjdMc ->iterative Appraoch

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> do either recursive or iterative approach.
					Recursive:
						have an array, when you reach a node just insert the node in appropriate
						array[level] index.

					Iterative:
						using queue, like how we usually do BFS. have a queue append the root
						inside it. loop until queue is empty. each time pop the left element.
						take its child and append to queue. continue. this is general bfs.
						for this question to store the levels instead of appending the child
						to the queue , we have a tempQueue and append the element to it
						then finally we make the original queue as tempQueue.

"""	


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    #iterative Approach
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return(ans) 
            
    #Recursive Approach
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(root,level,ans):
            if not root:
                return root

            if len(ans)<level+1:       #Understand this condition clearely **IMPORTANT**
                ans.append([])	       #if we get into a level we check we have space in ans
                					   #for this level if not we create it

            ans[level].append(root.val)
            dfs(root.left,level+1,ans)
            dfs(root.right,level+1,ans)

        ans=[]
        level=0
        dfs(root,level,ans)
        return(ans)
        
