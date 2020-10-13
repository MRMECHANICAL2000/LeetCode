"""
Key : Flyord Cycle 2 pointer Turtle and Hare Algorithm
"""
"""
Problem Name   : Find the duplicate in an array of N+1 integers
Problem Url    : https://leetcode.com/problems/find-the-duplicate-number/
Solution Video : https://youtu.be/32Ll35mhWg0     **IMPORTANT** Look video for proof of Floyd's cycle algorithm
				 https://youtu.be/FkBm3NeWqak	  **IMPORTANT** 

Learning:
	Brute: 
		Having two loop and look for each element entire array to know duplicate of that element exists

	Better:
	1st approach -> sort the array then linear serch through it. O(n log n)
	2nd approach -> store unseen element in Frequency array **IMPORTANT** (look video to know what it is) or Dictionary , second occurance can be found easily
		Frequency Array:
			we use dictionary when we need key to be other values, since here keys are numbers and we gonna store their frequency
			we just use an array and store 0 in all index if an element of index found we add 1 to it , if already 
			1 is there in that index then it is our repeating value.

	Optimal: **IMPORTANT**
		Approach -> using cycle in Linked list , Floyd’s Cycle-Finding Algorithm or Floyd’s 2 pointer Algorithm or 
					Turtle and Hare algorithm
"""	

class Solution:
	#Better 2nd Approach
    def findDuplicate(self, nums: List[int]) -> int:
        seen={}
        for i in nums:
            if i in seen:
                return(i)
            seen[i]=1

    #optimal
    def findDuplicate(self, nums: List[int]) -> int:
    	hair=tort=nums[0]        #no need to convert the list to linked list, iniside the list we 
    							 #can use loop via element and index only for this sum. because
    							 # we have n element in order and n index.
    	hair= nums[nums[hair]]   
    	tort= nums[tort]
    	while hair!= tort:
    		hair= nums[nums[hair]]
    		tort= nums[tort]

    	hair=nums[0]
    	while hair!=tort:
    		hair= nums[hair]
    		tort= nums[tort]

    	return(hair)
