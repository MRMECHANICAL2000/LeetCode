"""
Key : use merge sort so that you can ease count inversino question
"""
"""
Problem Name   : Sort an Array
Problem Url    : https://leetcode.com/problems/sort-an-array/
Solution Video : 

Learning:
	Brute: 
		use buble sort , selection or insertion sort. ->O(N^2) time and O(1) space complexity

	Better:
		use Merge sort -> O(NlogN) time and O(N) space compleixty
		

	Optimal: **IMPORTANT**
		Approach -> use quick sort , O(NlogN) time and O(1) space compleixty
"""	

class Solution:
	#Better
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSubRoutine(A,B):
            if not A:
                return(B)
            if not B:
                return(A)
            result=[]
            Aidx=0
            Bidx=0
            while Aidx<len(A) and Bidx<len(B):
                if A[Aidx]<B[Bidx]:
                    result.append(A[Aidx])
                    Aidx+=1
                else:
                    result.append(B[Bidx])
                    Bidx+=1
            #All the slicing will take O(N) time in python **IMPORTANT**
            result.extend(A[Aidx:]) #if A is not empty add it
            result.extend(B[Bidx:]) #if B is not empty add it
            		                #becuase the while looop breaks if atleast one of them is empty
            return(result)
        def splitSubRoutine(arr):
            if not arr:
                return([])
            if len(arr)==1:
                return(arr)
            splitLen=len(arr)//2
            #All the slicing will take O(N) time in python **IMPORTANT**            
            leftSplit=splitSubRoutine(arr[:splitLen])
            rightSplit=splitSubRoutine(arr[splitLen:])
            return(mergeSubRoutine(leftSplit,rightSplit))
        return(splitSubRoutine(nums))

	#Optimal
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return(nums)
        
