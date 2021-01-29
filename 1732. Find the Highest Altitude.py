"""   
Key :  

"""

"""
Problem Name   : Find the Highest Altitude
Problem Url    : https://leetcode.com/problems/find-the-highest-altitude/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT** **IMPORTANT**
		Approach -> just find prefix sum and store the max value, then return it at last.

"""	

class Solution:
	#Optimal Solution
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum=0
        maxGain=0
        for i in gain:
            prefixSum+=i
            maxGain=max(maxGain,prefixSum)
        return(maxGain)