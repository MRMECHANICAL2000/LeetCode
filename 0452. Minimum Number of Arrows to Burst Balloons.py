"""   
Key :  similair to meeting room 2 but there if two meeting overlap we create a room here if two meeting
	   did not overlap we create a arrow. just sort wrt end time then count no of non overlapping 
	   intervals. Must try this question
	   **IMPORTANT** This question is an differnt interval problem Must Must try this. need to think a bit
	   carefully we cant use previous interval problems here.


"""

"""
Problem Name   : Minimum Number of Arrows to Burst Balloons
Problem Url    : https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
Solution Video : https://youtu.be/uC0aDIhwGdE   
				 **IMPORTANT**
				 https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/93719/Greedy-Python-(132-ms)
				 
                 

Learning:
	Brute:
		use two loop. find no of meeting that did ''not overlap'' for each interval then return the max.
		O(n^2) solution **IMPORTANT** you dont even know how to think brute force method?
		
	Optimal: 
		Approach -> Sort the meeting wrt end time. now the meeting that finish first will be at beginnig
					if a meeting did not overlap increament arrow and store curEnd time.		
"""	

class Solution:
	#Optimal Solution
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        end,arrow= -float('inf') ,0           #How to put infinity in python **IMPORTANT**
        for i in points:
            if i[0]>end:     #if interval did not overlap we need another arrow
                arrow+=1
                end=i[1]
        return(arrow)
