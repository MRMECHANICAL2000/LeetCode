"""   
Key : if you did not chose an proper pivot then you will end up with an skewed Tree(linked list)
	  **IMPORTANT**
	  Whenever you are given an sorted array binary search would be what solution for it.
""" 

"""

Problem Name   : Convert Sorted Array to Binary Search Tree
Problem Url    : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Solution Video : https://youtu.be/12omz-VAyRk

Learning:
	Brute:
		take the first node as root and then insert the remaining by comparing it with the
		root node. if you do this you will end up with an Binary Tree skewed on left/right side
		(like linked list).
		
	Better: 


	Optimal: **IMPORTANT**
		Approach -> Recursive Binary Search Method, **IMPORTANT**

					Take the mid element as root, split the sorted into left(until mid) and
					right(after mid), then call the same function with this two array 
					recursively until the array gets empty.  

"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        root=TreeNode()
        if nums==[]:
            return(None)
        
        if len(nums)==1:
            root.val=nums[0]
            return(root)

        root.val=nums[(len(nums)-1)//2]

        root.left=self.sortedArrayToBST(nums[:(len(nums)-1)//2])

        root.right=self.sortedArrayToBST(nums[((len(nums)-1)//2)+1:])

        return(root)