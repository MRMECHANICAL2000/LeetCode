"""   
Key : same as serilize and deserialize binary tree
	  **IMPORTANT**
"""

"""
Problem Name   : Serialize and Deserialize BST
Problem Url    : https://leetcode.com/problems/serialize-and-deserialize-bst/
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
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return("")
        
        queue=deque([root])
        outputQueue=str(root.val)
        
        while queue:
            node=queue.popleft()

            outputQueue+=","
            if node.left:
                queue.append(node.left)
                outputQueue+=str(node.left.val)
            else:
                outputQueue+=" "

            outputQueue+=","
            if node.right:
                queue.append(node.right)
                outputQueue+=str(node.right.val)
            else:
                outputQueue+=" "
       
        return(outputQueue)        

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return(None)

        data=deque([int(i) if i!=" " else 'null' for i in data.split(",")])
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
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans