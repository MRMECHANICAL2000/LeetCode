"""   
Key :  Look what they are asking in question carefully.you dont even know how to think brute force method?
	   Know how to sort wrt 2nd element using "" Key=lambda x: x[1] "" in sort function **IMPORTANT**
	   **IMPORTANT**
	   #sorting wrt 2nd element
	   https://stackoverflow.com/questions/20099669/python-sort-multidimensional-array-based-on-2nd-element-of-subarray

"""

"""
Problem Name   : N meetings in one room
Problem Url    : https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0#
Solution Video : https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/   **IMPORTANT**
				 https://youtu.be/zbImSGug-oc
                 

Learning:
	Brute:
		use two loop. find no of meeting that did overlap for each interval then return the max.
		O(n^2) solution **IMPORTANT** you dont even know how to think brute force method?
		
	Optimal: 
		Approach -> Sort the meeting wrt end time. now the meeting that finish first will be at beginnig
					select meetin that starts after 1 meeting ends. repeat until all meeting processed.
					this will give us optimal solution.		
"""	

class Solution:
	#Optimal Solution
	for _ in range(int(input())):
	    n=int(input())                                  #Getting Input
	    start=[int(i) for i in input().split()]
	    end=[int(i) for i in input().split()]          

	    Time=[(start[i],end[i]) for i in range(n)]      #Making Time slots

	    HashTable=dict()                                #Remembering the slots position **IMPORTANT**
	    for i,v in enumerate(Time,1):
	        HashTable[v]=i

	    Time=sorted(Time,key=lambda x:x[1])            #Sorting wrt end time **IMPORTANT**

	    possibleMeeting=[Time[0]]                      #selecting interval that do not merge with prev end time
	    for i  in Time[1:]:
	        if possibleMeeting[-1][1]<=i[0]:
	            possibleMeeting.append(i)
                                                       #Printing the position of slots
	    [print(HashTable[v],end=" ") for v in possibleMeeting]
	    print()

