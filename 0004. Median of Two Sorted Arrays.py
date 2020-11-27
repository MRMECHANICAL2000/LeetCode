"""   
Key : write the code to find k'th element in two sorted array and in kth place put l//2 if len(A)+len(B)
	  is odd. else find both l//2 and l//2+1 and return theire average

	  your simple min,max math idea wont works here because median is not average of min and max element 
	  its average of midlle two element or middle element itself
	  **IMPORTANT** **IMPORTANT** **IMPORTANT**

"""

"""
Problem Name   : Median of Two Sorted Arrays
Problem Url    : https://leetcode.com/problems/median-of-two-sorted-arrays/
Solution Video : https://www.youtube.com/watch?v=tmu50Fs4v54&t=701s

Learning:
	Brute:
		join both array into single array sort and find the required value
		
	Better:
		to join use merge step of merge sort. so another time we dont need to sort

	Optimal: 
		Approach -> By using Divide conquer Approach. look the video and memorise the code to get
					the intution of the problem and thats the only way
"""	

class Solution:

    def findMedianSortedArrays(self, A: List[int], B: List[int]):
        def findKth(A,B,k):
            if len(A)>len(B):
                A,B=B,A
                
            if A==[] and B!=[]:
                return(B[k-1])

            if k==1:
                return(min(A[0],B[0])) #1st element is the element in 0th index not in 1st index Think Twise dont put max() there. **IMPORTANT**

            i=min(len(A),k//2)
            j=min(len(B),k//2) #since we have 0 based indexing and the element is kth so 
                               #we take len(A) or  k//2 here and on next line we take A[i-1]th index
            
            if A[i-1]<B[j-1]:
                return(findKth(A[i:],B,k-i))
            else:
                return(findKth(A,B[j:],k-j))                
            
        l=len(A)+len(B)        
        if l%2==1:
            return(findKth(A,B,l//2+1))  #if length is odd median is middle element
        else:							 #else median is average of two elemet near middle element
            return(findKth(A,B,l//2) +findKth(A,B,(l//2)+1))/2
