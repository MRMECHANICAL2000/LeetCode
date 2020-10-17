"""   
Key :  Look Max consecutive ones part 3, it wont be easy as you think
	   **IMPORTANT**you can see the edge case of for Loop in this question **IMPORTANT**
		dry run the code by "return(overMax)" and "return(max(curMax,overMax))" seperately 
"""

"""
Problem Name   : Max continuous number of 1’s
Problem Url    : https://leetcode.com/problems/max-consecutive-ones/
Solution Video : https://youtu.be/PLa4tYQhqoU    
                 

Learning:
	Brute:
		Using 2 Loops
		
	Optimal: 
		Approach -> Using a variable to store curMax and overMax. compare curMax ,overMax each time and
					return the 	overMax at last
"""	

class Solution:
	#Optimal Solution
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        overMax=0
        curMax=0
        for i in nums:
            if i==0:
                overMax=max(curMax,overMax)
                curMax=0                
            else:
                curMax+=1            
        							 #**IMPORTANT**
        return(max(overMax,curMax))  #**IMPORTANT** Edge case: if we use for loop , i=0 to n-1 so n'th element
        							 #wont be upgraded , at last check who is max overMax or curMax and then return 
