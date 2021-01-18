"""   
Key : we put -1 in final code because here they are asking edge count not vertex count.

"""

"""
Problem Name   : Diameter of Binary Tree
Problem Url    : https://leetcode.com/problems/diameter-of-binary-tree/
Solution Video : https://youtu.be/9bCqmaIY2as   ->#Watch it if you have confusion understanding
												  #the code

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> using Recursion. there are 3 possiblility 
					1.left+root+right -> max dia pass throught left tree then root then right tree
					2.left+root       -> max dia pass only through left tree and root alone
					3.root+right 	  -> max dia pass only through root and right tree alone
					4.left or right   -> either left or right tree has max dia no need to root
					we take the max of all 4 cases.

					here only case 2,3 can be extende 1,4 is already found dia and it cant be
					extended further. max(max(2,3) , max(1,4))-> max(canExtend,untilNow)
					we will take the max of this two possibility

				Case 1: [4,2,1,3] or [5,2,1,3]

			          1
			         / \
			        2   3
			       / \
			      4   5 

				Case 2: [6,4,2,1] or [5,4,2,1]

			          1
			         / 
			        2  
			       /     
			      4   
			     / \
			    6   5

				Case 3: [1,3,5,7] or [1,3,5,4]

			          1
			           \
			            3
			       	     \
			       	      5
			      	  	 / \
			      	  	4   7  

				Case 4: [4,2,1,3,7,6]

			          	8
			           / \
			          1   9
			         / \
			        2   3
			       /     \
			      4       7
			      		   \
			      		   	6

"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        def diameter(root):
            if not root:
                return(0,0)          #(max(left+root,root+right),left+root+right)

            #**IMPORTANT**
            leftExtend=0   #To check if maxDia is by extending root+left subTree
            leftDia=0	   #To check if max is already found in leftSub Tree
            rightExtend=0  #To check if maxDia is by extending root+right subTree
            rightDia=0     #To check if max is already found in rightSub Tree

            if root.left:
                leftExtend,leftDia=diameter(root.left)

            if root.right:
                rightExtend,rightDia=diameter(root.right)  

            #print("root:",root.val,"leftExtend:",leftExtend,"RightExtend",rightExtend ,"leftDia:",leftDia,"rightDia:",rightDia)
            return(1+max(leftExtend,rightExtend),max(leftDia,rightDia,leftExtend+1+rightExtend))
        	#**IMPORTANT** Heat of the question **IMPORTANT**

        if not root:	#Base Case if there is no Tree
            return(0)
            						  #**IMPORTANT**
        return(max(diameter(root))-1) #we put -1 because here they are asking edge count not vertex
