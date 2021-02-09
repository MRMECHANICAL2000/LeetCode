"""   
Key : must read about the bisect library. both bisect_left,bisect_right returns where the 
	  element to be inserted in the sorted array but they differs when target element already 
	  exist in the array. bisect_left will return the index where the target exist bisect_right
	  returns the index+1 where the target exist.
	  
	   0 1 2 3 4 5
	  [0,1,2,2,2,3] -> bisect_left returns "2" , bisect_right returns "5" 
	  **IMPORTANT** **IMPORTANT**

	  https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
"""

"""
Problem Name   : Find First and Last Position of Element in Sorted Array
Problem Url    : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Solution Video :                  

Learning:
	Brute:
		linear search
		
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> using binary search

"""	

import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:   #Dont forgot the edge case
            return([-1,-1])

        start=0
        end=0
        start=bisect.bisect_left(nums,target)
        end=bisect.bisect_right(nums,target)-1

        if start<len(nums) and nums[start]==target:
            return([start,end])
        else:
            return([-1,-1])