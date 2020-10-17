"""   **IMPORTANT** **IMPORTANT**
Key : Look logic of the question ,  
	  Not simpler as you think, just try solving without looking the code.
	  dont thik of swap uniue element because it makes duplicate to travel from one point to other
	  try this question ones. **IMPORTANT**

"""

"""
Problem Name   : Remove Duplicate from Sorted array with k duplicates allowed
Problem Url    : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Solution Video : https://youtu.be/-jHoA0e-IJ0  **IMPORTANT**
                 

Learning:
	Brute:
		Creating an seperate array and putting unique elements out there
		
	Better:
		pop elements from the same array

	Optimal: **IMPORTAT**
		Approach -> same as previous question ,just note small changes always 1st to element 
					obeys our rules.		**IMPORTANT**
"""	

class Solution:
	#Optimal Solution

    def removeDuplicates(self, nums: List[int]) -> int:
        j=2  #1st two  element will be non duplicate always

        							  #**IMPORTANT** **IMPORTANT** **IMPORTANT** **IMPORTANT**
        for i in range(2,len(nums)):  #Always loop and check i,j-2 not i,i+2 because we cant generalize
            if nums[j-2]!=nums[i]:    #i,i+2 comparison but can do i,j-k(wher k is allowed duplicates)
                nums[j]=nums[i]             #**IMPORTANT** swapping wont solves the problem
                j+=1   						#Replace the index with that unique values.
                             
        return(j)