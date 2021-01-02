"""
Key : Take care of edge cases , use math . split base not power (x)^n = (x/2 * x/2)^(n/2) not as
       (x)^(n/2) . (x)^(n/2)    **IMPORTANT**
"""
"""
Problem Name   : Pow(x, n)
Problem Url    : https://leetcode.com/problems/powx-n/
Solution Video : https://youtu.be/l0YC3876qxg   **IMPORTANT** Must wath video

Learning:
	Brute: 
		Trivial using ** operator 

	Optimal: **IMPORTANT**
		Approach -> using math and recursion. if pow=0 return 1 ,if pow=-ve return (1/result)
		            if power is even (x)^n = (x/2 * x/2)^(n/2)
		            if power is odd  (x)^n = (x)^n . x = (x/2 * x/2)^((n-1)/2) . x
			    
			    **IMPORTANT** Dont forget (x)^n = (x/2 * x/2)^(n/2) not x^(n/2) * x^(n/2)
			    same mistake while teaching Zoho anna and Ece students. prepare this well
"""	

class Solution:
	#Optimal
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n==0:                        #Edge Case if pow is zero **IMPORTANT**
                return(1)
            if n==1:
                return(x)
            elif n%2==0:
                return(pow(x*x,n//2))
            else:
                return(pow(x*x,n//2)*x)

        if n<0:                            #Edge Case if pow is negative *IMPORTANT**
            return(1/pow(x,-n))
        
        return(pow(x,n))
    
