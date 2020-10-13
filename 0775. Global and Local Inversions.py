"""
Key : NO are from 0 to n, so no Merge Sort need , index-Val gives inversion **IMPORTANT**
"""
"""
Problem Name   : Global and Local Inversions
Problem Url    : https://leetcode.com/problems/global-and-local-inversions/
Solution Video : https://leetcode.com/problems/global-and-local-inversions/discuss/859083/My-2-Line-Java-Solution-or-Accepted-or-With-Explanation-or-Beats-100

Learning:
	Brute: 
		use Merge sort to count Global Inversion

	Optimal: **IMPORTANT**
		Approach -> find for each element index-value if it is >1 it means , there is a global inversion
                    Every Local Inversion is a global inversion, so if a LI is encountered LI will still 
                    be equal to GI. But if a new GI is encountered then return false
"""	

class Solution:
	#Optimal
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i,v in enumerate(A):
            if abs(i-v)>1:      #using Absolute value is must **IMPORTANT**
                return(False)
        return(True)
            
