"""
Key : smaller version of 4 sum problem , basically we used more optimal code than 4sum problem here.
	  look when to increment left,right for duplicate in this code.  **IMPORTANT**
	  while seeing this question your first intution should be of sorting it dont forget
"""

"""
Problem Name   : 3Sum
Problem Url    : https://leetcode.com/problems/3sum/
Solution Video : https://youtu.be/Ca7k53qcTic

				 Optimal code link Must see this guys code   **IMPORTANT** 
                 https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time).


Learning:
	Brute:
		using 3 Loop's 
	Better: 
		use two loop and binary search

	Optimal: **IMPORTAT**
		Approach -> similair to 4 sum problem, one loop and two pointer. but this code is more optimal in 
					skipping duplicates.
					**IMPORTANT**

"""	

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	#Brute
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        hashTable=set()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp=[nums[i],nums[j],nums[k]]
                        temp.sort()
                        temp=tuple(temp)
                        if temp not in hashTable:
                            hashTable.add(temp)
                            output.append(temp)
        return(output)

    #Optimal
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums.sort()
        previ=None
        for i in range(len(nums)-2):            
            if nums[i]==previ:
                continue
            previ=nums[i]

            j=i+1
            k=len(nums)-1

            while j<k:

                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                	
                	#only check for duplicates if we found a match else leave it  key for simple code
                	#in this problem.                                 **IMPORTANT**
                    while j<k and nums[j]==nums[j-1]:
                        j+=1

                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                    
        return(output)
