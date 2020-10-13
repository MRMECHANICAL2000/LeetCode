"""
Key : Permutation are in Pyramid pattern , increase to a point then decreases
"""

"""
Problem Name   : Next Permutation
Problem Url    : https://leetcode.com/problems/next-permutation/
Solution Video : https://youtu.be/LuLCLgMElus

Learning:
	Brute: 
		create Entire permutation from assending to decending

	Optimal: **IMPORTANT**
		Approach -> look from back , find i-1<i ,swap that value with 1st value > than i-1 
		and reversre everything in range [i:]
"""	

class Solution:
	#Optimal
    def nextPermutation(self, nums: List[int]) -> None:
        y=0
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:	
                for j in range(len(nums)-1,i-1,-1):
                    if nums[i-1]<nums[j]:
                        nums[i-1],nums[j]=nums[j],nums[i-1]
                        y=i
                        break
                break
        
        nums[y:]=nums[y:][::-1]  #Reverse a slice of an array in-place **IMPORTANT** Dont forget this