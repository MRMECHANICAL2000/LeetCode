"""   
Key : 
"""

"""
Problem Name   : Maximum Sum BST in Binary Tree
Problem Url    : https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
Solution Video : 

Learning:
	Brute:

	Better: 

	Optimal: **IMPORTANT** 
		Approach -> same as largest BST in BT question , instead of returning the size of 
                    binary tree we return sum of the BST nodes. at each time we find a BST
                    we store its sum inside an array. finally we return the sum of largest BST

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:

        Max=float('inf')
        Min=-float('inf')
        SumOfPossibleBST=[0]
        def BSTfinder(root):
            if not root:
                return(True,0,Min,Max)

            leftTree=[True,0,Min,Max] #we use min,max to pass condition on line 64 for leaf Node
            rightTree=[True,0,Min,Max]

            if root.left:
                leftTree=BSTfinder(root.left)

            if root.right:
                rightTree=BSTfinder(root.right)

            overAllMax=max(rightTree[2],root.val) #**IMPORTANT** Edge Case, if we did not do it
            overAllMin=min(leftTree[3],root.val)  #then 'inf' will be passed up the recurse call
            
            if leftTree[0] and rightTree[0]:
                if leftTree[2]<root.val<rightTree[3]:
                    #Heart of the question **IMPORTANT** Only change from prev question
                    SumOfPossibleBST.append(root.val+leftTree[1]+rightTree[1])
                    return(True,root.val+leftTree[1]+rightTree[1],overAllMax,overAllMin)
            return(False,max(leftTree[1],rightTree[1]),overAllMax,overAllMin)

        result=BSTfinder(root)
        return(max(SumOfPossibleBST))
