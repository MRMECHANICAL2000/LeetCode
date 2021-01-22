"""   
Key : look sys.maxsize is used to get max integer in python there is no such thing called
	  sys.maxint in python. you can also use float('inf')
	  **IMPORTANT**
"""

"""
Problem Name   : Binary Tree Maximum Path Sum
Problem Url    : https://leetcode.com/problems/binary-tree-maximum-path-sum/
Solution Video : https://youtu.be/TO5zsKtc1Ic
				 **IMPORTANT** Must watch the video

Learning:
	Brute:

		
	Better:
		same code as diameter code but lot of edge cases to be covered.

	Optimal: **IMPORTANT**
		Approach -> similair to diameter question, there we find max length between two
					nodes here we find the max sum between two nodes. we make small changes in 
					code here because not like diameter here there are lot of edge cases the 
					node may contain -ve values all node may contain -ve values... 

					so here instead of poping by maxValues of left/right +root , left+root+right
					and .... we have a variable pathSum which we initilize by -ve value.for
					every question we take

					self.pathSum=max(self.pathSum, leftExtend+root.val+rightExtend, root.val)

					we just add this code with small modification in height finding code,
					you may think that we are taking into account only curNode,left+curNode+right
					case not left+curNode, right+curNode extending case even that case will be
					taken into account in next line where we pass the height back

					return(max(root.val+max(leftExtend,rightExtend),0)), we take max(extending,0)
					because in some case extending value will be -ve so when we push this -ve value
					up, self.pathSum wont be getting max value.

					lot of things to absorb in this code.
					**IMPORTANT**

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys 
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.pathSum=-sys.maxsize  #or use -float('inf')  **IMPORTANT**
            
        def diameter(root):
            if root is None:  #this line is more effective than if not root:
                return(0)          

			#**IMPORTANT**            
            #if root.left: #No need to check this condition because we have None as base case
            leftExtend=diameter(root.left)

            #if root.right:
            rightExtend=diameter(root.right)  
                
            #**IMPORTANT**
            self.pathSum=max(self.pathSum,leftExtend+root.val+rightExtend,root.val)
            #max of already found path or cur left+root+right or root alone
            
            return(max(root.val+max(leftExtend,rightExtend),0))
            #max of extending or nothing at all  **IMPORTANT**
            #Extending happens here

        diameter(root)
        return(self.pathSum)
