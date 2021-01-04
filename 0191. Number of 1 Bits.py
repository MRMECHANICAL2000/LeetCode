"""   
Key :

"""

"""
Problem Name   : Number of 1 Bits
Problem Url    : https://leetcode.com/problems/number-of-1-bits/
Solution Video : 
                 

Learning:

	Brute: 

		 
	Better: 


	Optimal: 
		Approach -> use bin() function convert int to binary,then to string and count no of set bits
					using count("1") method
					 
"""	


class Solution:
	#Optimal DP Approach
    def hammingWeight(self, n: str):
        return(str(bin(n)).count('1'))
        