"""
Problem Name   : Kadane’s Algorithm
Problem Url    : https://leetcode.com/problems/maximum-subarray/
Solution Video : https://youtu.be/w_KEocd__20

Learning:
	Brute: 
		using two Loop Method

	Optimal: **IMPORTANT**
		Approach -> Kadane's Algorithm (Amazon intern question you failed in 2nd year)
"""	


import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        overallMax=-sys.maxsize
        currentMax=-sys.maxsize
        for i in nums:
            currentMax=max(currentMax+i,i)
            if currentMax>overallMax:
                overallMax=currentMax        
        return(overallMax)