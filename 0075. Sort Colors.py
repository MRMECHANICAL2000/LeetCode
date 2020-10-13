"""
Key : using Dutch National Flag Algorithm
"""
"""
Problem Name   : Sort an array of 0’s 1’s 2’s without using extra space or sorting algo
Problem Url    : https://leetcode.com/problems/sort-colors/
Solution Video : https://youtu.be/oaVa-9wmpns   

Learning:
	Brute: 
		use any n^2 sorting algorithm

	Better:
	1st approach -> using any O(n log n) sorting algorithm
	2nd approach -> Using counting sort ,which is like Frequency Array **IMPORTANT** (dont forget the name)

	Optimal: **IMPORTANT**
		Approach -> using 3 pointer , "Dutch National Flag Algorithm"
"""	

class Solution:
	#Better 1st approach
	def sortColors(self, nums: List[int]) -> None:
		nums.sort()

	#optimal
	def sortColors(self, nums: List[int]) -> None:
		p1=0
			   #**IMPORTANT**
		p2=0   #this is iterator loosu mari innoru variable increment panitu itha p1 to p2 to store 1
			   #nu kevalama yosikathey

		p3=len(nums)-1   
		while p2<=p3:
			if nums[p2]==2:
				nums[p2],nums[p3]=nums[p3],nums[p2]
				p3-=1
			elif nums[p2]==1:			#**IMPORTANT**
				p2+=1					#only increament p2 in case value is 0 or 1 , yosiche paru purium
			elif nums[p2]==0:
				nums[p1],nums[p2]=nums[p2],nums[p1]
				p1+=1
				p2+=1