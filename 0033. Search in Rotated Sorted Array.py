"""   
Key : pivot element can be either overall max or overall min element in the array. lot of edge cases in
	  this question, what if given array is not rotated, what if pivot is last element what if pivot is
	  1st element, what is seraching elemtn is 1st , last ,pivot elment or not in array?
	  **IMPORTANT**  **IMPORTANT**

"""

"""
Problem Name   : Search in Rotated Sorted Array
Problem Url    : https://leetcode.com/problems/search-in-rotated-sorted-array/
Solution Video : https://www.youtube.com/watch?v=GU7DpgHINWQ

				 **IMPORTANT** Must watch this erricto Binary search to think like an CP **IMPORTANT**                 
  			     you should need to think Array like T,F then only we can applay Binary Search
Learning:
	Brute:
		Using Linear serach.


	Optimal: 
		Approach -> using binary search, find the pivot element like how CP think. then from pivot
					element check if target > or < than 1st elemnt  accordingly start searching from
					[:pivot] or [pivot:]
					**IMPORTANT**
"""	



class Solution:
	#Optimal solution - Using Binary Search
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        pivot=0

        #Findling Pivot
        if nums[0]>nums[-1]:   #To check if the array is rotated **IMPORTANT**
            while start<=end:
                mid=start+(end-start)//2
                if nums[mid]>nums[mid+1]: #pivot is an element which is greater than its next element
                    pivot=mid
                    break

                elif nums[mid]>=nums[0]:
                    start=mid+1
                else:
                    end=mid-1

            if target<nums[0]:  #finding where the target may occur
                start=pivot+1
                end=len(nums)-1
            else:
                start=0
                end=pivot

        else:                #iff array not rotated its an oridinary binary search
            start=0
            end=len(nums)-1
        

        #Finding Target
        ans=-1              #both if array roted or not , we just need to find start and end of where
        					#the target may occur and do binary search on there.
        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]==target:
                ans=mid
                break
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1

        return(ans)