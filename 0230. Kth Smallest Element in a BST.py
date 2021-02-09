"""   
Key : similair to doing inorder traversal but its a bit tricky on how and when you will decerement
	  the k value. what if the tree become dynamic
	  **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Kth Smallest Element in a BST
Problem Url    : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Solution Video : https://youtu.be/KqMm81Y7j9M      
				 **IMPORTANT** Must watch 3rd appraoch to know the optimal appraoch **IMPORTANT**           

Learning:
	Brute:
		do inorder travesal and store all the element in an array.then return kth index element
		takes O(N) time and O(N) space.
		
	Better: **IMPORTANT** **IMPORTANT**
		instead of storing all element in array then finding kth index, while doing the inorder
		traversal itself we will do the kth element checking.(a bit tricky one). 
		Takes O(N) time no matter how balanced your tree is


	Optimal: **IMPORTANT** **IMPORTANT** **IMPORTANT**
		Approach -> what if the tree become dynamic, what if they alter the tree by adding and
					removing some element oftern and you are asked to find the different kth
					smallest element always 

					here instead of moving entire tree and solving at each node we will have
					a count of how many nodes are there in its left side, so that when you go
					to a node you will know wheather your kth node will exist there on left side
					or you need to go to right subTree. this method requires to change the values
					in the tree but it runs in O(Log N) time in average.

					**IMPORTANT** we have not implemented it yet. look the video 3rd appraoch

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	#Better Appraoch
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans=-1
        self.k=k

        def inorder(root): #Always try writing seperate function for finding inorder traversal
        				   #dont use the given function itself. **IMPORTANT**
            if not root:
                return()
                					#**IMOPORTANT** ones you find the kth smalles element	
            if self.k>0:            #we wont make further calls 
                if root.left:
                    inorder(root.left)
                    
                self.k-=1
                if self.k==0:
                    self.ans=root.val
                    
                if root.right:
                    inorder(root.right)

        inorder(root)
        return(self.ans)
        
