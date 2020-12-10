"""   
Key : we cant solve this question like how we did in next greater element I, dont think that do similair
	  to prev question  and for last element alone we can check from front. that approach fails
	  Eg: 4 3 2 1 -> your above approach will give -1 -1 -1 4 but correct ans is -1 4 4 4

	  In question they did not say the input will only have unique element. so dont store the element
	  store its index in stack. no need to use hashTable as how we used in next greater element I
""" 

"""
Problem Name   : Next Greater Element II
Problem Url    : https://leetcode.com/problems/next-greater-element-ii/
Solution Video : https://www.youtube.com/watch?v=_t_GfZ5QBUY  **IMPORTANT**
				 **IMPORTANT** Must watch the video to get the optimal approach 1 intution **IMPORTANT**

                 https://www.youtube.com/watch?v=ARkl69eBzhY&t=348s **IMPORTANT**
				 **IMPORTANT** Must watch the video to get the optimal approach 2 intution **IMPORTANT**
Learning:
	Brute:
		for each element we check for next greater element to  its left then to its right. for each 
		element we use two for loop. takes O(n^2) time

	Optimal: **IMPORTANT**
		Approach 1 -> do the same as process as next greater element I but do it twise on the input.
					  in 1st iteration you will find greater element for some index in 2nd iteration
					  you will find greater element for remaining index.

		Approach 2 -> Nailded it solution.extending the approach we already know to an different question
					  to solve this question.Consider two string, str1= "aeiou"   str2="iouae" , 
					  if we want to check if str1 is an rotation of str2, all we have to do is to 
					  duplicate the str2 by just modify the str2 as "iouae"+"ioua"="iouaeioua" add the 
					  same string on the end of it and we can just look through the whole string. if it
					  was in addition of the two string then str1 is an rotation of str1.
"""	

class Solution:
	#Optimal Approach 1
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        answer=[-1 for i in nums]        

        for idx,val in enumerate(nums):    #1st Iteration
            if not stack:
                stack.append(idx)
                continue
                
            if val<=nums[stack[-1]]:
                stack.append(idx)   
            else:
                while stack and val>nums[stack[-1]]:
                    answer[stack.pop()]=val           
                stack.append(idx)

        for idx,val in enumerate(nums):  #2nd Iteration
            if not stack:
                stack.append(idx)
                continue
                
            if val<=nums[stack[-1]]:
                stack.append(idx)   
            else:
                while stack and val>nums[stack[-1]]:
                    answer[stack.pop()]=val           
                stack.append(idx)

        return(answer)



	#Optimal Approach 2
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        tempNums=nums[:]+nums[:-1]         #Extending the solution we already know to solve this question
        answer=[-1 for i in tempNums]        
        for idx,val in enumerate(tempNums):           #To cash all next greater element

            if not stack:
                stack.append(idx)  					  #since input may contain duplicate we store the 
                continue							  #index instead of value **IMPORTANT**
                                
            if val<=tempNums[stack[-1]]:
                stack.append(idx)   
            else:
                while stack and val>tempNums[stack[-1]]:#found the next greater element cashing the result
                    answer[stack.pop()]=val             #key of question **IMPORTNAT**
                stack.append(idx)
        return(answer[:len(nums)])