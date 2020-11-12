"""
Key : Remember the brute force method you dont even know how to think **IMPORTANT**
      for Meeting Room 1 sort wrt end time , here sort wrt start time then only we can know how
      many rooms need.Know how to implement heap with heapq liberary. you cant optimise the 
      problem without heap/priority queue. 
      Must understand 2 pointer technique for this sum. **IMPORTANT** Must Must
"""

"""
Problem Name   : Meeting Rooms 2
Problem Url    : https://www.lintcode.com/problem/meeting-rooms-ii/description
Solution Video : https://youtu.be/xLbXbG6uK-A     **IMPORTANT** Must Watch **IMPORTANT**
                 https://youtu.be/38JLfQGVlkw    **IMPORTANT** Must Must Must Must Watch **IMPORTANT**

Learning:
    Brute:  **IMPORTANT**
        Using two loops and check no of rooms required for each iteration. return the max of all.
        max no of intersion is equal to max rooms. O(N^2)

    Better:  **IMPORTANT**
        if we need N meeting in 1 room we sort wrt end time and store all meeting that do not overlap. but 
        here we need No of rooms to accomodate all rooms. so sort wrt start time. store meeting in an array
        if current meeting start time does not match with any of the meeting end time in array create an new
        room in array. O(N^2) we take quadratic time to check if an  room with less ending time exist


    Optimal: **IMPORTANT**
        Approach 1 -> instead of check room with less ending time each time we can just use an priority 
                      queue or MinHeap to store meeting that gonna end soon so that each time we can check
                      if the meeting that **IMPORTANT**
        
                      **IMPORTANT** **IMPORTANT** **IMPORTANT**
        Approach 2 -> two pointer approach. highly space and time effective **IMPORTANT** **IMPORTANT**
                      watch Video to understand same as min platform sum. if i<=j increment j and room-=1
                      if i>j increment i and rooms+=1. ie, if i>j means 2nd meeting starts before 1st end
                      so we need a new rooms if i<=j means use same room so reduce room-=1.return max rooms
"""	

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq      #To get optimal Solution **IMPORTANT**

class Solution:
    #Optimal Approach 1
    def minMeetingRooms(self, intervals):
        
        Time=[(i.start,i.end) for i in intervals]   #Creating Time Array from interval object
        Time.sort()                                 #Sorting wrt start time **IMPORTANT**

                                                    #**IMPORTANT**
        EndTime=[Time[0][1]]                        #creating 1 room for 1st meeting
        heapq.heapify(EndTime)                      #Heapify to get room with quick endind time in O(1) time


        for i in Time[1:]:                          #**IMPORTANT**
            if i[0]>=EndTime[0]:                    #if min end time is <= cur start time then we can use
                heapq.heappop(EndTime)              #the same room. pop that meeting and put cur meeting 
            heapq.heappush(EndTime,i[1])            #end time else create new meeting room by pushing into heap
        
        return(len(EndTime))     #Length of heap is the no of rooms required.


    #Optimal Approach 2
    def minMeetingRooms(self, intervals):
        # Write your code here
        startTime=[i.start for i in intervals]
        endTime=[i.end for i in intervals]
                                                  #**IMPORTANT**
        startTime.sort()                          #starting both start and end time
        endTime.sort()

        Rooms=1
        maxRooms=1                                 #**IMPORTANT**
        i=1                                        #since already one room alloted for 1st meeting
        j=0
                                                   #**IMPORTANT**
        while i<len(startTime) and j<len(endTime): #if either i,j became out of bound break

            if endTime[j]<=startTime[i]:  #**IMPORTANT**
                j+=1
                Rooms-=1               #Existing room utilized, 2nd meeting starts after 1st meeting ends
            else:
                i+=1 
                Rooms+=1               #New room created, 2nd meeting starts before 1st meeting ends
            maxRooms=max(maxRooms,Rooms)
        return(maxRooms)
