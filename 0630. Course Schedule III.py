"""   
Key : in the first go you found that we can solve it using greedy question, similair to how
	  we solve the N meeting in one room question, but there is a slight change in this 
	  question. the given interval is not fixed , only end time is fixed start time is varaying
	  depending on which course we chose. so N meeting room appraoch fails.

	  N meeting in one Room -> both start and end time fixed
	  course schedule III -> only dedline given , start and end time can vary depending on how
	  						 we choose the course.
      **IMOPRTANT** **IMOPRTANT** **IMOPRTANT**
"""

"""
Problem Name   : Course Schedule III
Problem Url    : https://leetcode.com/problems/course-schedule-iii/
Solution Video : https://youtu.be/0DiBE3r1dHA

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT** **IMPORTANT**
        Approach -> sort the course wrt to end time, so that initilly we will chose the course
        			which ends quickly. we take a course and see if it crach with previous
        			course we have chosen if not we add this course to list, if it crash we 
        			see if there is any course that we have previously chosen has more duriation
        			than current course if yes, we pop that course and take the current course
        			because here our goal is to take as many course as possible. so we are
        			taking the course which ends faster and has less time to complete.

      				since we are searching each time wheather there any course that we have
      				previously chosen has maxTime than our current course. O(N^2) run time
      				in worst case. here we can optimize it by using an maxheap since each time
      				we are checking if there is any time greater than our curCourse time.


""" 
import heapq
class Solution:
	#Optimal Approach -> go Greedy
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        maxHeap=[]						#just writing maxHeap is not enough you need to store
        								#the element in max order, heapq() in python is minHeap
        								#so you need to use -val to make use the minHeap as
        								#maxheap **IMPORTANT**
        heapq.heapify(maxHeap)
        courses.sort(key=lambda x:x[1]) #sort wrt course ending time
        curTime=0
        for i in courses:
            if i[0]+curTime<=i[1]:
                curTime+=i[0]		    #if we can take that course we take it **IMPORTANT**
                heapq.heappush(maxHeap,[-i[0],-i[1]])

                						#if we cant we will see the last course we have taken
                						#and see wheather the time duriation of curCourse is
                						#smaller than previous chosen course is yes we pop
                						#the previous course and take the current course
                						#**IMPORTANT**
            elif maxHeap and i[0]<-maxHeap[0][0]:                
                temp=heapq.heappop(maxHeap)
                curTime-=-(temp[0])
                if i[0]+curTime<=i[1]:
                    curTime+=i[0]
                    heapq.heappush(maxHeap,[-i[0],-i[1]])
                    
        return(len(maxHeap))