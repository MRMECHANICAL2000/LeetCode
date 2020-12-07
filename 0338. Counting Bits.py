"""   
Key : learn the intution of DP solutin
	  **IMPORTANT**


"""

"""
Problem Name   : Counting Bits
Problem Url    : https://leetcode.com/problems/counting-bits/
Solution Video : https://www.youtube.com/watch?v=awxaRgUB4Kw
                 

Learning:

	Brute: 
		count no of set bits using "&" operator
		 
	Better: 
		use bin() function convert int to binary,then to string and count no of set bits using 
		count("1") method

	Optimal: **IMPORTANT**
		Approach -> using Dynamic Programming, if a no is odd then it has "+1" more set bit than i//2 th
					element. if the no is even, then it has same no of set bit as i//2the element
					**IMPORTANT** 
"""	

class Solution:
	#Brute Force Approach
    def countBits(self, num: int) -> List[int]:
        if num<=0:         #Edge Case
            return([0])

        return([bin(i).count("1") for i in range(0,num+1)]) #Counting set bit for all element and storing

class Solution:
	#Optimal DP Approach
    def countBits(self, num: int) -> List[int]:
        if num<=0:              #Edge Case
            return([0])
        if num==1:              #Edge Case
            return([0,1])

        DP=[0,1]+[0 for i in range(num-1)]

        for i in range(1,len(DP)):                     #heart of the code
            DP[i]=DP[i//2] if i%2==0 else DP[i//2]+1
        return(DP)