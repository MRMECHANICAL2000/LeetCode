"""
Key : usign reverse approach is important
	  **IMPORTANT**
"""

"""
Problem Name   : Rotate Array
Problem Url    : https://leetcode.com/problems/rotate-array/
Solution Video : https://youtu.be/gmu0RA5_zxs

Learning:
	Brute:
		Rotate the list for give no of times and produce output

	Optimal: **IMPORTAT**
	   Approach 1 ->  find length of list , join tail of list to head and break (len-k)th node and 
					  return (len-k)+1th Node **IMPORTANT**

                      **IMPORTANT** **IMPORTANT**
       Approach 2 -> using Reversing, 1st reverse entire list. then reverse 1st k element alone then 
                     reverse all element after k. just think why it works you will get this eventurally.
"""	

class Solution:

    #Optimal 1 -> using cycle replacement
    def rotate(self, nums, k):       
        if k>=len(nums):
            k=k%len(nums)
        x=len(nums)-k
        print(k,nums[x:]+nums[:x])
        nums[:]=nums[x:]+nums[:x]
        
    #Optimal 2 -> using Reversing
    def rotate(self, nums, k):
        if k>=len(nums):
            k=k%len(nums)

        nums[:]=nums[::-1]          #Reverse entire array
        nums[:k]=nums[:k][::-1]     #Reverse 1st K elemtent seperately
        nums[k:]=nums[k:][::-1]     #Reverse last k element seperately