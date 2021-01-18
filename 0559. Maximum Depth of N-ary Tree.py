"""   
Key :
"""

"""
Problem Name   : Maximum Depth of N-ary Tree
Problem Url    : https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> similair to max depth of binary tree, here we recurse on all children
					and take max of all of them

"""	

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return(0)
        
        childTreeDepth=[0]
        if root.children:
            childTreeDepth=[self.maxDepth(child) for child in root.children]

            
        return(1+max(childTreeDepth))