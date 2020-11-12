"""
Key : Same as No of meeting requied. but code is this question code so look mistake in it and learn
	  Remember the brute force method you dont even know how to think **IMPORTANT**
      for Meeting Room 1 sort wrt end time , here sort wrt start time then only we can know how
      many rooms need.Know how to implement heap with heapq liberary. you cant optimise the 
      problem without heap/priority queue. 
      Must understand 2 pointer technique for this sum. **IMPORTANT** Must Must
"""

"""
Problem Name   : Minimum Platform Needed in Railway Station
Problem Url    : https://practice.geeksforgeeks.org/problems/minimum-platforms/0#
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

#Optimal Approach 2
for _ in range(int(input())):
    n=int(input())
    
    start=[int(i) for i in input().split()]
    end=[int(i) for i in input().split()]

    start.sort()
    end.sort()
    
    maxPlatform=1
    platform=1
    i,j=1,0
    while i<n and j<n: # dont put <= like stupid **IMPORTANT**
    						 #**IMPORTANT**
        if start[i]<=end[j]: #Read question carefully arrival == dept also we need new platform
            platform+=1
            i+=1            
        else:
            platform-=1
            j+=1
        maxPlatform=max(maxPlatform,platform)
    print(maxPlatform)
