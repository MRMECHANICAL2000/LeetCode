"""   
Key : It seems like easy greedy problem but you must try this out the heart of code is totally
	  different than you think , your code has edge case look this code.
	  **IMPORTANT** **IMPORTANT** similair to N meeting in one room but differnt condition

"""

"""
Problem Name   : Maximum Length of Pair Chain
Problem Url    : https://leetcode.com/problems/maximum-length-of-pair-chain/
Solution Video : https://youtu.be/poWB2UCuozA 


Learning:
	Brute:
		use two loop. find no of Activity that did overlap for each interval then return the max.
		O(n^2) solution **IMPORTANT** you dont even know how to think brute force method?
		
	Optimal: 
		Approach -> Sort the Activity wrt end time. now the Activity that finish first will be at beginnig
					select Activity that starts after 1 Activity ends. repeat until all Activity processed.
					this will give us optimal solution.
"""	

class Solution:

	#Optimal Solution- Greedy
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        chain=0
        curPair=float('-inf')  #Dont put 0th index of pair here and compare it become edge case always
        					   #try putting infinite and work **IMPORTANT** **IMPORTANT**
        for i in pairs:
            if curPair<i[0]:   #Heart of code try to understand **IMPORTAN**
                curPair=i[1]
                chain+=1

        return(chain)