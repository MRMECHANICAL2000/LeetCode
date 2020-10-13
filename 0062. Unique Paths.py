"""
Key : Using combination formula nCr=n!/((n-r)!*r!), 
      **IMPORTANT** where n=row+coloum r=row or coloum  **IMPORTANT**  
"""

"""
Problem Name   : Unique Paths
Problem Url    : https://leetcode.com/problems/unique-paths/
Solution Video : https://youtu.be/t_f0nwwdg5o   **IMPORTANT** Must wath video

Learning:
	Brute: 
		use recursion, at each cell two recursion one down other right
		find all path and count the unique paths 

	Better:
		using Dynamic Programming, create a matrix and find solution

	Optimal: **IMPORTANT**
		Approach -> using combination solution,

"""	

class Solution:
	#Optimal Approach    
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(val):
            output=1
            for i in range(1,val+1):
                output*=i
            print(output)
            return(output)
        n-=1   #Depending on question this step may or may not come
        m-=1
        return(factorial(m+n)//(factorial(m+n-m)*factorial(m)))	
