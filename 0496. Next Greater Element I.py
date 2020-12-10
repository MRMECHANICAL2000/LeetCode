"""   
Key : cataching the intermediate result at each of the location/index. to solve an question we can check
	  for what we want by looping each time on entire array or loop the array ones and cach all the result
	  In question they are diverting us by saying fancy words like nums1 subset of nums2
""" 

"""
Problem Name   : Next Greater Element I
Problem Url    : https://leetcode.com/problems/next-greater-element-i/
Solution Video : https://www.youtube.com/watch?v=sDKpIO2HGq0
                 
Learning:
	Brute:
		Using 2 loops and finding next Greater each time. O(N^2) time

	Optimal: **IMPORTANT**
		Approach -> store greater element on each index. just loop through nums2, if the element is
					less <= top of stack push that element to stack, else curElment is the next
					greater element for top of stack. store "top:curElemnet" in hashTable
"""	

class Solution:
	#Optimal Approach
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        HashTable={}
        stack=[]
        answer=[]
        
        for i in nums2:                #To cash all next greater element
            if not stack:
                stack.append(i)
                continue
                
            if i<=stack[-1]:
                stack.append(i)   
            else:
                while stack and i>stack[-1]:           #found the next greater element
                    HashTable[stack.pop()]=i           #cashing the result. key of question **IMPORTNAT**
                stack.append(i)
                
        for i in nums1:               #To get result
            try:
                answer.append(HashTable[i]) #if the element not in hash table it means it has no 
            except:							#next greater element so append -1 to answer **IMPORTNAT**
                answer.append(-1)
        return(answer)