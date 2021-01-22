"""   
Key : you may think of many approaches like how we solved the previous questoin of path Sum I,II
	  but it wont be solved. we can use the knowledge we gained from previous solving of question
	  called subArray sum equal to K, to sove it.
	  **IMPORTANT**
"""

"""
Problem Name   : Path Sum III
Problem Url    : https://leetcode.com/problems/path-sum-iii/
Solution Video : 
				 **IMPORTANT** 

Learning:
	Brute:
		finding all paths in tree and validate their sum. O(N^3) can be optimized to O(N^2)
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> similair to question subArray sum equal K. here we are doing paths whoes
					sum equal to k. we use an hashTable. we find prefix sum at each node we
					go, then we check if prefixSum-k in hashTabel if its there it means there
					is atleast hashTabel[prefixSum-k] number of path in hashTable which has an
					path sum of k. we inerst the prefixSum into the HashTable and recurse on
					the left,right child of tree with that prefix sum. after completing the left
					and right child traversal we pop the prefixSum from the table then we move to
					the previous called function. if you draw a small tree and dry run it you will
					understand why we do the last step. **IMPORTANT**
"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def pathSum(self, root, k):
        self.pathCount=0
        
        self.hashTable=defaultdict(int)
        self.hashTable[0]=1
        
        
        def helper(root,prefixSum):
            if root in [None]:		#same code as root==None or not root. but this runs 98% faster
                return(0)
            
            prefixSum+=root.val
             
            if self.hashTable[prefixSum-k]>=1:		#checking if prefixSum-k exist in HashTable
                self.pathCount+=self.hashTable[prefixSum-k]
                
            self.hashTable[prefixSum]+=1	#inserting cur PrefixSum in hashTable

            left=helper(root.left,prefixSum)
            right=helper(root.right,prefixSum)
            
            self.hashTable[prefixSum]-=1	#Deleting cur PrefixSum from hashTable **IMPORTANT**
            								#**IMPORATANT** try to understand it clearely we
            								#are using tree not array, so after completing
            								#everything in leftTree we need to delete the data
            								#added from left tree then only we can recurse on
            								#right tree
        
        helper(root,0)
        return(self.pathCount)