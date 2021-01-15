"""   
Key :  Code looks little bit confusing, but think twise you will understand. each bit of 
	   code is important

"""

"""
Problem Name   : Delete Node in a BST
Problem Url    : https://leetcode.com/problems/delete-node-in-a-bst/
Solution Video : https://youtu.be/gcULXE7ViZw  #Explanation on how to delted
				 https://youtu.be/wMyWHO9F1OM  #Python code Tutorial
                 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> at first we check if the value exist in tree, if its less than curRoot
					then it in left subTree ,if its greater than curRoot its in right subTree
					if its equal to root, means the element to be delelted is found now we 
					have 3 options,

					1. Deleting node has no children -> just delete that node
					2. Deleting node has one children -> just delete the node and make the 
					   one child of deleting node to point to the parent of deleting node
					3. Deleting node has two children -> we find the minimum element on right
					   subTree or maximum element on left subTree and swap it with value of
					   node to be deleted. and delete that node which we used to swap.

					we can just delete the node we find but we do this stuff in order to maintain
					the property of the binary search tree.		
"""	

class Solution:
	#Optimal Solution
    def deleteNode(self, root, key):
        if root==None:		#Base Case if the given tree is empty or 
            return(None)	#node to be deleted does not exist  **IMPORTANT**

        if root.val<key:    #Value in right subTree
            if root.right:
                root.right=self.deleteNode(root.right,key)
        
        elif root.val>key:  #Value in left subTree
            if root.left:
                root.left=self.deleteNode(root.left,key)
                #Must put "root.left =" , its hard to understand why but if you think it
                #twise you will understand **IMPORTANT**
        
        else:				#Value found in current Node
            if root.left==None and root.right==None:     #If current node has No child
                return(None)
            elif root.left==None:						 #If current node has one child
                return(root.right)
            elif root.right==None:
                return(root.left)
            
            else:										 #If current Node has two child
                maxLeft=root.left.val
                temp=root.left
                while temp:				#Swaping with max on left subTree we can also swap
                    maxLeft=temp.val 	#it with min on right subTree
                    temp=temp.right
                root.val=maxLeft                    
                root.left=self.deleteNode(root.left,maxLeft)
        
        return(root)
        
        