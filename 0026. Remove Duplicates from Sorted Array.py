"""   **IMPORTANT** **IMPORTANT**
Key : Look logic of the question , look code of remove duplicates in sorted array 2 to understand 
	  Not simpler as you think, just try solving without looking the code.
	  dont thik of swap uniue element because it makes duplicate to travel from one point to other
	  try this question ones. **IMPORTANT**

"""

"""
Problem Name   : Remove Duplicate from Sorted array
Problem Url    : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Solution Video : https://youtu.be/MVcNRKr93uQ  **IMPORTANT**
                 

Learning:
	Brute:
		Creating an seperate array and putting unique elements out there
		
	Better:
		pop elements from the same array

	Optimal: **IMPORTAT**
		Approach -> In the quetoin it is said to do inplace, have an index j pointing to index 1 of array
					because we can be sure that index 0 is always uniques elements. if you find i!=i+1
					make nums[j]=i+1 and increament j+1. swapping wont makes the problem solve dry run to
					look for it.		**IMPORTANT**
"""	

class Solution:
	#Optimal Solution

    def removeDuplicates(self, nums: List[int]) -> int:
        j=1  #1st  element will be non duplicate always

        							  #**IMPORTANT** **IMPORTANT** **IMPORTANT** **IMPORTANT**
        for i in range(1,len(nums)):  #Always loop and check i,j-1 not i,i+1 because we cant generalize
            if nums[j-1]!=nums[i]:    #i,i+1 comparison but can do i,j-k(wher k is allowed duplicates)
                nums[j]=nums[i]             #**IMPORTANT** swapping wont solves the problem
                j+=1   						#Replace the index with that unique values.
                             
        return(j)