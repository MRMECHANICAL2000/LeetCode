"""
Key : remember how brute force works, and must watch the video to know how optimal approach works 
	  using lower envelop technique
      **IMPORTANT**

"""

"""
Problem Name   : Trapping rainwater
Problem Url    : https://leetcode.com/problems/trapping-rain-water/
Solution Video : https://youtu.be/XqTBrQYYUcc  **IMPORTANT** Must Must Must Must watch video
                 

Learning:
	Brute: **IMPORTANT** Remember the brute method
		from (1)st to (n-1)th find max value to left and right , sub min of(leftMax,rightMax) to curVal
		to find amount of water can be stored in each coloum. O(1) space and O(n^2) time 
		
	Better: 
		Instead of moving left,right for each coloum each time, just use two array to store left and right
		value. takes O(2n) Space and O(n) time

	Optimal: **IMPORTAT**
		Approach -> Using Lower Enveloper Technique , an 2 pointer technique 
		 			Must watch video to learn more
					**IMPORTANT**

"""	

class Solution:
	#Better Approach
    def trap(self, height: List[int]) -> int:
        totalWater=0

        curMax=0                  #O(n) space to store prefix max from left to right
        ltor=[]
        for i in height:
            if i>curMax:
                curMax=i
            ltor.append(curMax)

        curMax=0                  #O(n) space to store prefix max from right to left
        rtol=[]
        for i in height[::-1]:
            if i>curMax:
                curMax=i
            rtol.append(curMax)
        rtol=rtol[::-1]

        for i in range(len(height)):    #look it twise to understand, logic of question
            if height[i]<ltor[i] and height[i]<rtol[i]:
                totalWater+=min(ltor[i],rtol[i])-height[i]
        return(totalWater)

	#Optimal Approach
    def trap(self, height: List[int]) -> int:
    									   #Edge case
        if len(height)<3:                  #We could do noting if we have less than 3 walls
            return(0)
			
        totalWater=0
        leftMax=0
        rightMax=0
        left=0
        right=len(height)-1
        while left<=right: 
            leftMax=max(leftMax,height[left])            #Updating leftMax and rightMax at each step
            rightMax=max(rightMax,height[right])
            										   #**IMPORTANT**
            if leftMax<rightMax:                       #dont check lefMax and height[left] like fool does
                totalWater+=leftMax-height[left]       #if leftMax<rightMax we can store at most 
                left+=1                                #leftMax-height[left] amount of water only since we
                									   #already know lefMax is greater than height[left]
            elif leftMax>=rightMax:                   
                totalWater+=rightMax-height[right]
                right-=1
        return(totalWater)