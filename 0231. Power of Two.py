"""   
Key : log function is in math library of python, there is an difference between log2(n) and loge(n,2) 
	  function because of how computer store value in memory.
	  https://www.geeksforgeeks.org/log-functions-python/
	  if no of set bit is 1 then the number is power of 2.
	  **IMPORTANT**


"""

"""
Problem Name   : Power of Two
Problem Url    : https://leetcode.com/problems/power-of-two/
Solution Video : https://www.youtube.com/watch?v=4cqHahxFTYw
                 

Learning:

	Brute: **IMPORTANT**
		divide the number by 2 until you reach an odd number, iff that final odd no is 1, then its an 
		power of 2, else the number is not powere of 2.
		 
	Better: **IMPORTANT**
		if an number is power of 2, then it has only one setbit.

	Optimal: **IMPORTANT**
		Approach -> take log2(number), you will get the 2^x=n that x value. check if that value is whole
					no if yes then return True else return False
"""	

import math
from collections import Counter
class Solution:
	#Better Method
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return(False)
        c=Counter(bin(n))
        if c['1']==1:
            return(True)
        return(False)

	#Optimal Method
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return(False) #**IMPORTANT**
        temp=math.log2(n) #log2(n) and log(n,2) both will give differnet answer in fractional part due 
        				  #to division happening inside computer this error occur so please use log2(n) 
        				  #not log(n,2)(ie, loge(n,2))
        return(int(temp)==temp)

        