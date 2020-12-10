"""   
Key : This question has v.v.v.v important edge case, in question its stated if next greater element
	  is greater than 2^31 then  return -1, in python we can store 2^31 but here we need to output
	  -1. so we check if current permutaion is less than 2^31 by using "temp<=((1<<31)-1)"
	  **IMPORTANT** **IMPORTANT**
""" 

"""
Problem Name   : Next Greater Element III
Problem Url    : https://leetcode.com/problems/next-greater-element-iii/
Solution Video : 

Learning:
	Brute:


	Optimal: **IMPORTANT**
		Approach -> same as that of next permutaion question. find next permutation if its > than 
					current number "n" then return found permutaion if its lesser return -1.
"""	

class Solution:
	#Optimal Approach
    def nextGreaterElement(self, n: int) -> int:

        def nextPermutation(nums):
            y=0
            for i in range(len(nums)-1,0,-1):
                if nums[i]>nums[i-1]:	
                    for j in range(len(nums)-1,i-1,-1):
                        if nums[i-1]<nums[j]:
                            nums[i-1],nums[j]=nums[j],nums[i-1]
                            y=i
                            break
                    break

            nums[y:]=nums[y:][::-1]
            return(nums)
        
        nums=[int(i) for i in str(n)]                               #to find next permutaion we need to 
        															#convert the input as list of int's
        temp=int("".join([str(i) for i in nextPermutation(nums)]))  #finding next permutaion
        
        if temp>n and temp<=((1<<31)-1):  #**IMPORTANT** Edge case to solve this question **IMPORTANT**
            return(temp)
        return(-1)