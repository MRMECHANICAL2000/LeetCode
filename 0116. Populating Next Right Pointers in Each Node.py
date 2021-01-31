"""   
Key : In question its said given tree is full tree so,there wont be any gap in our tree.
"""

"""
Problem Name   : Populating Next Right Pointers in Each Node
Problem Url    : https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
Solution Video : https://youtu.be/vy2mnT3TEXQ

Learning:
	Brute:
		do level order traversal and connect all nodes in each level
		
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> we go to a node and check if the parent node of this node has a right
					child if it has a right child it means it is our next right pointer. if there
					is no parent node we point our node to none and if there is a parent node
					but we are its right child or no right child for it , then we point to the 
					left child of parents next right pointer node. **IMPORTANT**
"""	

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def populateNxtRightPointer(node,parent):
            if node is None:
                return()
            if parent is None:
                node.next=None
            elif parent.right!=node:
                node.next=parent.right
            elif parent.next and parent.next.left:
                node.next=parent.next.left
            else:
                node.next=None

            if node.right:
                populateNxtRightPointer(node.right,node)                
            
            if node.left:
                populateNxtRightPointer(node.left,node)



        populateNxtRightPointer(root,None)
        return(root)