"""   **IMPORTANT** **IMPORTANT**
Key : Using SLiding Window technique only topper will get this idea not fool like you
	  Not simple as you think , Edge case that occur in for loop can be seen here**IMPORTANT**

"""

"""
Problem Name   : Max Consecutive Ones III
Problem Url    : https://leetcode.com/problems/max-consecutive-ones-iii/
Solution Video : https://youtu.be/97oTiOCuxho  **IMPORTANT**  Must Must Watch 
                 

Learning:
	Brute:
		using two loop and counter

	Optimal: **IMPORTAT**
		Approach -> Using sliding window technique 	**IMPORTANT**
"""	

class Solution:
	#Optimal Solution using for loop
    def longestOnes(self, A: List[int], K: int) -> int:
        j=0
        for i in range(len(A)):
            if A[i]==0:
                K-=1
            if K<0:
                if A[j]==0:
                    K+=1
                j+=1         #**IMPORTANT**
        i+=1                 #for loop take us from 0 to n-1 , we need to keep i=n at last : Corner Case
        return(i-j)			 #i remains as i=n-1 we incremetn it to i=n


	#Optimal Solution using while loop
    def longestOnes(self, A: List[int], K: int) -> int:
        j=0
        while i<len(A):
            if A[i]==0:
                K-=1
            if K<0:
                if A[j]==0:
                    K+=1
                j+=1     
	        i+=1
	             #since we increment while loop ourself after reaching i=n-1, at end i become i=n
        return(i-j)