"""
Key : using Shell sort 2 Gap Method
      During Interview ,They wont ask to sort without extra space,but you should do it in 
      optimization step
"""


"""
Problem Name   : Merge two sorted Arrays without extra space
Problem Url    : https://leetcode.com/problems/merge-sorted-array/
Solution Video : https://youtu.be/hVl2b3bLzBw
                 https://youtu.be/ddeLSDsYVp8

Learning:
	Brute: 
		put two array in another array then sort it again 

	Better:

       1st Approach -> if you cant insert array2 into array1 , then we do like insertion sort take array2 
                       element and put in array1 then pop last element of it and put in it last of array2 then 
                       take array2 1st element and repeat until all element in array2 is bigger than array1    
	   2nd Approach -> take 2nd array element use binary search(bisect) then insert on 1st array

	Optimal: **IMPORTANT**
		Approach -> Using 2 Gap Algorithm (Shell Sort Algorithm)
"""	

class Solution:
    #Better 2nd Approach
    from bisect import bisect_left
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        beg=0
        end=m
        for i in nums2:
            j=bisect_left(nums1,i,beg,end)
            nums1.insert(j,i)
            nums1.pop()
            end+=1

    #optimal Approach
    from math import ceil
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        gap=(len(nums1)+len(nums2))//2
        nums1[len(nums1)-len(nums2):]=nums2 #**IMPORTANT**
                                            #1st we put nums2 in nums1, slice index and put value this 
                                            #is the easy way to change value inplace dont do any other
                                            #stupid thing to change value,we cant do it other way
        
        while gap>=1:
            i=0
            j=i+gap
            while j<len(nums1):
                if nums1[i]>nums1[j]:
                    nums1[i],nums1[j]=nums1[j],nums1[i]
                i+=1
                j=i+gap #**IMPORTANT** don't put j+=gap, we need to have gap from i not from j
            
            if gap/2<1:
                break
            gap=ceil(gap/2) #**IMPORTANT** we need to put ceil, if gap<1 break dont ceil. 