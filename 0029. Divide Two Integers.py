"""   
Key : 
	  **IMPORTANT**


"""

"""
Problem Name   : Divide Two Integers without / operator
Problem Url    : 
Solution Video :  

Learning:

	Brute: 

		 
	Better: 


	Optimal: **IMPORTANT**
		Approach ->
					**IMPORTANT** 
"""	

class Solution:
	#Brute Approach
    def divide(self, dividend: int, divisor: int) -> int:
        
        ans=0
        isNegative=1 if dividend<0 or divisor<0 else 0
        isNegative=0 if dividend<0 and divisor<0 or dividend>0 and divisor>0 else 1
        
        dividend=abs(dividend)
        divisor=abs(divisor)
        while dividend>=divisor:
            ans+=1
            dividend-=divisor

        return(-ans if isNegative==1 else  ans)

	#Optimal Approach
    def divide(self, dividend: int, divisor: int) -> int:        
        ans=0
        isNegative=1 if dividend<0 or divisor<0 else 0
        isNegative=0 if dividend<0 and divisor<0 or dividend>0 and divisor>0 else 1
        
        dividend=abs(dividend)
        divisor=abs(divisor)
        while dividend-divisor>=0:
            temp=0
            while dividend-(divisor<<1<<temp) >=0:
                temp+=1
            ans+=1<<temp
            dividend-=divisor<<temp
            
        res=-ans if isNegative==1 else  ans
        return min(max(-2147483648, res), 2147483647)
