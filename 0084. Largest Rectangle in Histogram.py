"""   
Key : if we can extend area of histogram we append it to stack if we cant extend the area of histogram 
	  we calculate its area. formula to calculate area is important. must append 0 to end of histogram.
	  look code to check edge case.
""" 

"""
Problem Name   : Largest Rectangle in Histogram
Problem Url    : https://leetcode.com/problems/largest-rectangle-in-histogram/
Solution Video : https://www.youtube.com/watch?v=zx5Sw9130L0
				 **IMPORTANT** Must watch the video to get intution and know how to expain this
				 question in the interview **IMPORTANT**
                 
Learning:
	Brute:
		using two loop, calculate the Area each time. takes O(n^2) time.

	Optimal: **IMPORTANT**
		Approach 1 -> combination of two sums we have already solved. trapping rain water and next smaller
					  element, find next small element from L to R and R to L. store it in two array. so
					  now at each index now using this 2 array value we can find max area that can be
					  created with that index value. indexVal*(smallRightIndex-smallLeftIndex)


	   Approach 2 ->using stack based approach. loop i through the histogram. if i is less than stack[-1]
				    it means we cant extend that histogram at stack any further, so we calculate its are
					by using "Val*(CurIdx-Idx)" , if i>stack[-1] we can extend the histogram area even
					further so we append i to stack. since we have appende 0 to histogram end, all the
					histogram left in stack will be evaluvated defenitely 

					we can go with DP for this question but it will take more space and time than
					this easy stack based approach.
"""	


class Solution:
	#Optimal Approach 2
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        heights.append(0)                   #Must append 0 at last then only we can make sure all the
        maxArea=0							#Histogram are taken into account **IMPORTANT**
        for idx,val in enumerate(heights):
            if not stack:
                stack.append([idx,val])
                continue

            if val>=stack[-1][1]:
                stack.append([idx,val])

            else:
                while stack and val<stack[-1][1]:
                    tempIdx,tempVal=stack.pop()
                    area=tempVal*(idx-tempIdx)  #This Formula is the Key **IMPORTNAT**
                    maxArea=max(maxArea,area)
                    
                stack.append([tempIdx,val]) #**IMPORTANT** must append tempIdx not current index because 
                							#[2,1,2] here largest rect is 3, if you add curIdx you will 
                							#end with large rect as 2. **IMPORTANT** Edge Case
        return(maxArea)