"""   
Key : 
"""

"""
Problem Name   : N-ary Tree Level Order Traversal
Problem Url    : https://leetcode.com/problems/n-ary-tree-level-order-traversal/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as ordinary binary tree Level order traversal , instead of having
					two chields we have a child array here.
"""	


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return([])
        queue=deque()
        queue.append(root)
        ans=[]
        
        while queue:
            tempQue=deque()
            tempAns=[]
            while queue:
                popNode=queue.popleft()
                							#**IMPORTANT**
                if popNode.children:		#Only this line varies instead of left,right child
                    tempQue.extend(popNode.children)
                
                tempAns.append(popNode.val)

            queue=tempQue
            if tempAns:
                ans.append(tempAns) 
        return(ans)