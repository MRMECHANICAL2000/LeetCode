"""   
Key : 
	  **IMPORTANT**
"""

"""
Problem Name   : Serialize and Deserialize Binary Tree
Problem Url    : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Solution Video : https://youtu.be/suj1ro8TIVY
				 **IMPORTANT** Must watch the video to know where it is used **IMPORTANT**

Learning:
	Brute:
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> converte the given tree into string by BFS (you can also do dfs) order for
					serilized function, for each value we convert it into a string for each None
					we convert it inot an empty space all of them were seperated by ","

					now this data can be transmitted and deserilized in other function, there we
					split the string with "," first then make " " as 'null', convert this array
					to tree in reverse level order fashion.

"""	
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        if root is None:
            return([])
        queue=deque([root])
        outputQueue=deque([root.val])
        
        while queue:
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
                outputQueue.append(node.left.val)
            else:
                outputQueue.append('null')

            if node.right:
                queue.append(node.right)
                outputQueue.append(node.right.val)
            else:
                outputQueue.append('null')
        return(outputQueue)

    def deserialize(self, data):
        
        if not data:
            return(None)
                
        root=TreeNode(data.popleft())
        queue=deque([root])
        
        while queue:
            node=queue.popleft()

            if data:                
                node.left=TreeNode(data.popleft())
                queue.append(node.left)
                
            if data:
                node.right=TreeNode(data.popleft())
                queue.append(node.right)
            
            
        return(root)
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))