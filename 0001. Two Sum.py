"""
Key : Store index along with value in Hash Table.
"""
"""
Problem Name   : Two Sum
Problem Url    : https://leetcode.com/problems/two-sum/
Solution Video : https://youtu.be/dRUpbt8vHpo

Learning:
	Brute: 
		Using Two Loops 

	Optimal: 
		Approach -> use HashTable to store, an element along with index. check an element req-i present in
		            Table if present then return that index. Look constrain of the question it is said
		            there will be only one such pair.
"""	

class Solution:
	#Optimal
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashTable={}
        for i,v in enumerate(nums):
            try:
                j=HashTable[target-v]
                return([i,j])
            except Exception:
                HashTable[v]=i
