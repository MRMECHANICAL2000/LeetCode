"""   
Key : same as kth largest element. but here if array has only two distinct element and you
	  need 3rd larger element you return the larger element in array. edge case in question.
	  **IMPORTANT**
"""

"""
Problem Name   : Third Maximum Number
Problem Url    : https://leetcode.com/problems/third-maximum-number/
Solution Video :                  

Learning:
	Brute:
		sort and pick the 3rd largest element. O(nlogn) time
		
	Better:
		use heap, insert the element inside heap and pop until you reach 3rd element.
		O(nlogn) time to heapify & pop in worst case, since same space used so O(1) space alone
		
	Optimal: **IMPORTANT**
		Approach -> using Quick select algorithm, brother of quick sort. takes O(logn) time in
					average.

"""	

import heapq
class Solution:
   #Better -> using heap
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        #**IMPORTANT**
        #Edge case what if the array size is less than 3 or array has only 3 unique element
        if len(nums)<3:
            return(max(nums)) 
        nums=[-i for i in nums]
        heapq.heapify(nums)
        heapq.heappop(nums)
        heapq.heappop(nums)
        return(-heapq.heappop(nums))
                        
 