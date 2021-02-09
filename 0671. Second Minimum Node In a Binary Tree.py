"""   
Key : try to learn this taught process behind the optimal approach since they are asking the
	  2nd smallest the author used 2 variable and constantly updated them when new values
	  are found . think like a good cp. dont do some complicated computation
	  **IMPORTANT**
"""

"""
Problem Name   : Second Minimum Node In a Binary Tree
Problem Url    : https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
Solution Video :                  

Learning:
	Brute:
		do inorder traversal and store element in a set, sort the set and return 2nd
		smallest element. takes O(N) space
		
	Better:


	Optimal: **IMPORTANT** **IMPORTANT**
		Approach -> instead of using an set to cach all the data use two variable and
		   			store only 1st two caches.

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
	#Optimal Solution
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        self.first=root.val
        self.second=float('inf')
        def inorder(root):
            if not root:
                return()
            
            if self.first<root.val<self.second:  #**IMPORTANT** Heart of the Trick
                self.second=root.val
            
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        return(self.second if self.second!=float('inf') else -1)

