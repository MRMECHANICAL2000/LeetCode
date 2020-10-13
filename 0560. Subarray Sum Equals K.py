"""
Key : always sum of subarray means make sure you use PrefixSum method 
	  for this sum HashTable intution is important  remember that **IMPORTANT**
"""

"""
Problem Name   : Subarray Sum Equals K
Problem Url    : https://leetcode.com/problems/subarray-sum-equals-k/
Solution Video : https://www.youtube.com/watch?v=HbbYPQc-Oo4           **IMPORTANT** Must Must Must Watch

Learning:
	Brute: 
		Using 2 loops and find sum of all element in each subarray compare with K , O(1) space, O(n^3) time

	Better:
		Approach 1 -> using 2 loop and instead of sum each time use an Prefix sum array takes 
					  O(n) space , O(n^2) time    **IMPORTANT**
		Approach 2 -> using 2 loop and variable to keep sum track. O(1) space and O(n^2) time


	Optimal: **IMPORTANT**
		Approach -> Using HashTable , store curSum in HashMap, check if curSum-k exist in HashTable
					if exist means there is an array from exist index to current Index summing up to k
 					Watch video for explanation **IMPORTANT**

"""	

from collections import defaultdict            #**IMPORTANT** Collection's' spelling don't forget
class Solution:
	#Optimal
    def subarraySum(self, nums: List[int], k: int) -> int:
        HashMap=defaultdict(bool)
        HashMap[0]=1
        curSum=0
        count=0
        for i in nums:
            curSum+=i

            if HashMap[curSum-k]:
                count+=HashMap[curSum-k]
            HashMap[curSum]+=1            

        return(count)