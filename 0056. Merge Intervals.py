"""
**IMPORTANT**  Ask the interviewer wheather the i/p array is sorted or not because in example it 
looks like the array are sorted so HR checks wheather we ask this question or not """

"""
Problem Name   : Merge Overlapping Subintervals
Problem Url    : https://leetcode.com/problems/merge-intervals/
Solution Video : https://youtu.be/2JzRBPFYbKE

Learning:
	Brute: 
		Take an interval loop to entire list and find its overlap and put in new list

	Better:
		approach -> Using two array of interval and try merging

	Optimal: 
		Approach -> Sort at first so overlap interval becomes consecutive, then merge them in linear time
"""	

class Solution:
    #optimal
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newInterval=[intervals[0]] if intervals else []
        for i in intervals[1:]:
            current=newInterval[-1]
            if current[1]>=i[0]:    #**IMPORTANT** must put >= not just > , overlap interval can also be equal
                newInterval.pop()
                newInterval.append([current[0],max(current[1],i[1])])
            else:
                newInterval.append(i)
        print(newInterval)
        return(newInterval)
                
            
        