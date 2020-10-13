"""
Key : using sorting at 1st is an good idea ,since order does not matters. Look the implementation
      of jumping over the duplicates be carefull in it. **IMPORTANT**
"""

"""
Problem Name   : 4 Sum problem
Problem Url    : https://leetcode.com/problems/4sum/
Solution Video : https://youtu.be/4ggF3tXIAp0 **IMPORTANT**

Learning:
	Brute: 
		Using 4 loops(i,j,k,l) ,sum all and find

	Better:
		Sort the array at 1st, use 3 loops(i,j,k) and one binary search(mid) , sum all and find  **IMPORTANT**

	Optimal: 
		Approach -> Sort the array 1st, use 2 loops(i,j) and 2 pointer (left,right), sum all if less than 
		            target increase left, if greater increase right. Make sure to jump over duplicate
		            element to make algorithm more faster.    **IMPORTANT**

"""	

class Solution:
	#Optimal
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()                             #Preprocessor sorting Step
        output=[]

        prevI=None                              #To skip over duplicates
        prevJ=None
        prevLeft=None
        prevRight=None


        for i in range(len(nums)):
            if nums[i]==prevI:                 #To Jump i duplicate
                continue
            prevI=nums[i]

            prevJ=None       #**IMPORTANT** on each new iter prevJ should need to be made None, 
            				 #similarely left and right as well

            for j in range(i+1,len(nums)-1):
                if nums[j]==prevJ:             #To Jump j duplicates
                    continue
                prevJ=nums[j]

                left=j+1
                right=len(nums)-1

                firstAttempt="Yes"            #1st try prevLeft,PrevRight no need to check
                                
                while left<right:

                    if firstAttempt=="Yes":
                        prevLeft=left
                        prevRight=right
                        firstAttempt="No"
                        
                    else:                     #Jumping Left and right duplicates
                        if nums[left]==nums[prevLeft] and left!=prevLeft:
                            left+=1
                            continue
                        prevLeft=left
                    
                        if nums[right]==nums[prevRight] and right!=prevRight:
                            right-=1
                            continue
                        prevRight=right
                    

                                              #Checking Target and taking other dicission
                    add=nums[i]+nums[j]+nums[left]+nums[right]
                    if add==target:
                        output.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                    elif add<target:
                        left+=1
                    else:
                        right-=1

        return(output)               