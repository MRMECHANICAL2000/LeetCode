"""   
Key : they are asking kth largest element which means kth element from right not from left this 
	  looks like an simple things but you even made mistakes in it. 
	  **IMORTANT**
	  quick select is really easy but you made lot of mistake in implementing it. in this question
	  they ask kth largest element which means without considering duplicates you need to output
	  kth largest element.
	  **IMORTANT** **IMPORTANT**

	  look how to implement heap in python
	  https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
"""

"""
Problem Name   : Kth Largest Element in an Array
Problem Url    : https://leetcode.com/problems/kth-largest-element-in-an-array/
Solution Video :                  

Learning:
	Brute:
		sort and pick the kth element. O(nlogn) time
		
	Better:
		use heap, insert the element inside heap and pop until you reach kth element.
		O(nlogn) time to heapify & pop in worst case, since same space used so O(1) space alone
		
	Optimal: **IMPORTANT**
		Approach -> using Quick select algorithm, brother of quick sort. takes O(logn) time in
					average.

"""	

import heapq
class Solution:
	#Optimal Solution -> Quick Select
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return(nums[0])
        pivot=nums[0]
        left=[]
        equal=[]
        right=[]
        for val in nums:
            if val<pivot:
                left.append(val)
            elif val==pivot:
                equal.append(val)
            else:
                right.append(val)
        
        if k<=len(right):
            return(self.findKthLargest(right,k))
        elif k<=len(equal)+len(right):
            return(equal[0])
        else:
            return(self.findKthLargest(left,k-len(right)-len(equal)))
                
    #Better -> using heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heappop(nums)
        return(heappop(nums))

    #Brute -> using sorting
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return(nums[len(nums)-k])
