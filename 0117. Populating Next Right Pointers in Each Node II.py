"""   
Key : same as previous question but not easy as you think , here it is said that the Tree is not
	  an complete tree so each level may or may not be fully filled.

      May look simple but lot of edge cases you must do post order traversal not inorder
      here because after fixing all the right side node only you can fix your left side node
      Eg :[1,2,3,4,5,null,6,7,null,null,null,null,8] in this test case if you do preorder 
      traversal/inorder traversal you will 1st go to 7, but still we did not made connection 
      for 5->6 so 7 will point to None

      **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Populating Next Right Pointers in Each Node II
Problem Url    : https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Solution Video : https://youtu.be/vy2mnT3TEXQ

Learning:
	Brute:
		do level order traversal and connect all nodes in each level
		
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> since the given tree is not full tree, here we find the next right
					pointer by traversing through all the next pointer of the parent until
					we reach None or find the next right node
					**IMPORTANT**
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
            elif parent.right and parent.right!=node:
                node.next=parent.right

                				#**IMPORTANT** **IMPORTANT**
                				#not just single next pointer we go and check for all the next
                				#pointer of parent until we find next right node or null
            elif parent.next:
                parent=parent.next
                while parent:

                    if parent.left:
                        node.next=parent.left
                        break
                    if parent.right:
                        node.next=parent.right
                        break
                    parent=parent.next
                if parent==None:
                    node.next=None
 
            else:
                node.next=None
            
                				   #Edge Case
            if node.right:         #first right side then only left side **IMPORTANT** 
                populateNxtRightPointer(node.right,node)                
            
            if node.left:
                populateNxtRightPointer(node.left,node)


        populateNxtRightPointer(root,None)
        return(root)