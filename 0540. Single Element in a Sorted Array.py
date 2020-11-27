"""   
Key : Must watch the video to get the intution. dont forget the edge cases. the key to the question is on
	  knowing when to do binary serach on left and when on right.
	  **IMPORTANT**

"""

"""
Problem Name   : 540. Single Element in a Sorted Array
Problem Url    : https://leetcode.com/problems/single-element-in-a-sorted-array/
Solution Video : https://www.youtube.com/watch?v=nMGL2vlyJk0
				 **IMPORTANT** Must watch the video to get the intution **IMPORTANT**                 

Learning:
	Brute:
		do linear search and find that element that appears only ones.

	Optimal: 
		Approach -> using binary search, to get the intution you need to have an observation in the 
					input. note that if we are in even index(i) then value in index i,i+1 both 
					will be same. if not then single element have appeared before.
					**IMPORTANT**
"""	



class Solution:
	#Optimal solution - Using Binary Search
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if len(nums)==1 or nums[-1]!=nums[-2]:   #Edge Case ,if last element is the single element
            return(nums[-1])
        
        elif nums[0]!=nums[1]:  #Edge Case, if 1st element is the single element
            return(nums[0])
        
        start=0
        end=len(nums)-1
        ans=0

        #Binary search wrt index not wrt numbers in array **IMPORTANT**
        while start<end:
            mid=start+(end-start)//2

            if mid%2==0:                     #Heart of the Program **IMPORTANT**
                if nums[mid]!=nums[mid+1]:
                    ans=nums[mid]
                    end=mid
                else:
                    start=mid+1
            else:
                if nums[mid]!=nums[mid-1]:
                    ans=nums[mid]
                    end=mid
                else:
                    start=mid+1
        return(ans)
                
        
        