"""   
Key : dont get afraid of this question and think how to solve it, its an very easy question.
	  Here they are only asking if there is any path from root to leaf, with a given sum. if yes
	  return True else False. the important thing is that we are required to return the sum in 
	  path from root to leaf, if you find the path some where in internal node that sums up to
	  givenSum then also we need to return False.
	  **IMPORTANT**
"""

"""
Problem Name   : Path Sum
Problem Url    : https://leetcode.com/problems/path-sum/
Solution Video : 
				 **IMPORTANT** 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> if root is not None, subTract it with given sum and recurse with the
					subtracted sum on leftTree and rightTree. we resurse until we reach the leaf
					node at leaf node we check if givenSum-leafNode==0 if yes a path exist else
					no path exist.
					you may think we can break if givenSum-root becomes -ve in internal nodes,
					but this tree is not binary search tree also there are -ve values in the tree
					so we go until leaf ones we reach the leaf alone we check the condition.

"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, givenSum):

        if root is None:
            return(False)

		#In question its stated that only root to left path sum is asked not root to any 
		#internal node or just root alone, so if we reach a path which has our required sum 
		#we also need to make sure its the root node        
        if root.left==None and root.right==None and givenSum==root.val: 
            return(True)
        
        #No need to check if givenSum<root.val and return false its good but it fails if input 
        #is -ve. here we are asked if there is a root to leaf path.so we just subtract 
        #givenSum-root.val until leaf and at the leaf we check if its equal to givenSum 
        #ie, givenSum become 0 if yes we return True else False

        givenSum-=root.val 
        leftTree=self.hasPathSum(root.left,givenSum)
        rightTree=self.hasPathSum(root.right,givenSum)        

        return(leftTree or rightTree) #we return True if we found a path in either of the Tree
