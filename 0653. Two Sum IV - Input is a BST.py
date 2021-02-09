"""   
Key : 
"""

"""
Problem Name   : Two Sum IV - Input is a BST
Problem Url    : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Solution Video :                  

Learning:
	Brute:
		
		
	Better:
		insert all element into an array and do how we did two sum for arrays.

	Optimal: **IMPORTANT**
		Approach -> same as two sum question we solved in array, we use HashTable here also
					to optimize it. do DFS or BFS + HashTable to solve this question.
					we go to a node and check if k-node.val already in table if yes you
					found the two sum
"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        queue=[root]
        
        HashTable={}
        
        while queue:
            tempRoot=queue.pop()
            
            try:
                return(HashTable[k-tempRoot.val])
                
            except:
                HashTable[tempRoot.val]=True
                
            if tempRoot.left:
                queue.append(tempRoot.left)
            if tempRoot.right:
                queue.append(tempRoot.right)
                
        return(False)