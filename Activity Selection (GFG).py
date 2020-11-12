"""   
Key : Greedy Method. Similair to N meeting in one room problem.just go through code ones.

"""

"""
Problem Name   : Activity Selection
Problem Url    : https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1#
Solution Video : https://youtu.be/poWB2UCuozA 

				 Weighted Job Sequencing / Job sequencing with deadline 
				 https://youtu.be/zPtI8q9gvX8  **IMPORTANT** Must Watch **IMPORTANT**
                 
Learning:
	Brute:
		use two loop. find no of Activity that did overlap for each interval then return the max.
		O(n^2) solution **IMPORTANT** you dont even know how to think brute force method?
		
	Optimal: 
		Approach -> Sort the Activity wrt end time. now the Activity that finish first will be at beginnig
					select Activity that starts after 1 Activity ends. repeat until all Activity processed.
					this will give us optimal solution.		
"""	

class Solution:
	#Optimal Solution
	def maximumActivities(n,start,end):
	    Time=[(start[i],end[i]) for i in range(n)]
	    Time.sort(key=lambda x:x[1])
	    count,finish=0,-float('inf')  #if infintiy not used then we put count=1,finish=0 and start **IMPORTANT**
	    for i in Time:
	        if i[0]>=finish: #it is said start and end time can collide
	            count+=1
	            finish=i[1]
	    return(count)