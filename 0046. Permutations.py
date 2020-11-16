"""
Key : Permutation are in Pyramid pattern , increase to a point then decreases
"""

"""
Problem Name   : Permutation
Problem Url    : https://leetcode.com/problems/permutations/
Solution Video : https://youtu.be/1Rox5gt51b0
				 **IMPORTANT** Must Must Watch to know optimal implementation in library  **IMPORTANT**

Learning:
	Brute: 
	    look from back , find i-1<i ,swap that value with 1st value > than i-1 and reversre everything 
	    in range [i:]. use this next permutation finding method call it n! times to generate all 
	    permutation.


	Optimal: **IMPORTANT**
		Approach 1-> create Entire permutation from assending to decending using Inbuild Library
		Approach 2-> Look the video to know it. just keep all character at position 1 and then call the
					 function on remaining array.
"""	

from itertools import permutations
class Solution:
	#Optimal Approach 1
    def permute(self, arr: List[int]) -> List[List[int]]:
        return(permutations(arr))
