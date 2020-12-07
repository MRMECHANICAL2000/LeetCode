"""   
Key : 
	  **IMPORTANT**

"""

"""
Problem Name   : Most significant set bit
Problem Url    : 
Solution Video : https://www.geeksforgeeks.org/find-significant-set-bit-number/ 

Learning:

	Brute: 
		find the index of 1st "1", it is the MSB, find 2^(index) it is the answer

"""	

class Solution:
	#Brute Force Approach
    def findMSB(self, num: int):
    	temp=str(bin(num)[2:])
    	return(2^(len(temp)-temp.index("1")))

