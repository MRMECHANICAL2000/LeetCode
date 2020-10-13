"""
Key : Moors Voting Algorithm   **IMPORTANT**
"""

"""
Problem Name   : Majority Element
Problem Url    : https://leetcode.com/problems/majority-element/
Solution Video : https://youtu.be/AoX3BPWNnoE   **IMPORTANT** Must wath video

Learning:
	Brute: 
		Use two loop and count each element , return max repeated element 

	Better:
		using hash table

	Optimal: **IMPORTANT**
		Approach -> Moores Voting Algorithm. since need to find element that occurs more than floor(n/2)
		            times. Note that there can be only one such element. so use two variable and store element
		            and their occurance in them. loop for i in list, if count=0 take i as maxelement and increase
		            count by 1. if i and maxelement are same increase count by 1. if i and current element  
		            are not same then decrement count by 1.

"""	

from collections import defaultdict
class Solution:
	#Better Approach
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return(None)
        hashTable=defaultdict(int)
        for i in nums:
            hashTable[i]+=1
        count=-1
        output=-1
        for i in hashTable.keys():
            if hashTable[i]>count:
                count=hashTable[i]
                output=i
        return(output)


	#Optimal Approach    
	def majorityElement(self, nums: List[int]) -> int:
        elemet=0
        count=0
        for i in nums:
            if count==0:
                element=i
                count+=1
            elif element==i:
                count+=1
            else:
                count-=1
        return(element)
        
