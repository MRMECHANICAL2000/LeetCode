"""   
Key : very very very confusing problem, you took 4 days to understand this. if there is an small change 
	  in the code written then the program wont run. simple questoin dont forget even an single piece
	  of code. then you will suffer.
	  **IMPORTANT**

"""

"""
Problem Name   : K-th element of two sorted Arrays
Problem Url    : https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array/0#
Solution Video : https://www.youtube.com/watch?v=tmu50Fs4v54&t=701s
				 **IMPORTANT** Must watch the video to get the intution **IMPORTANT**                 

Learning:
	Brute:
		join both array into single array sort and find the required value
		
	Better:
		to join use merge step of merge sort. so another time we dont need to sort

	Optimal: 
		Approach -> By using Divide conquer Approach. look the video and memorise the code to get
					the intution of the problem and thats the only way
"""	

def findKth(A,B,k):

    if len(A)>len(B): #Best programming practice, always keep A as small size array
        A,B=B,A 	  #**IMPORTANT**
        
    if A==[] and B!=[]:  #recursion end Here
        return(B[k-1]) #if the element we are searching is k, then it will be present in k-1th index
        			   #**IMPORTANT***

    if k==1:				   #**IMPORTANT**
        return(min(A[0],B[0])) #1st element is the element in 0th index not in 1st index Think Twise dont put max() there. **IMPORTANT**

    i=min(len(A),k//2) #**IMPORTANT**
    j=min(len(B),k//2) #since we have 0 based indexing and the element is kth so 
                       #we take len(A) or  k//2 here and on next line we take A[i-1]th index
    
    if A[i-1]<B[j-1]:
        return(findKth(A[i:],B,k-i)) #we are eliminating one part of array alone , another array we take it
        							 #fully. since we eliminate i elment from 1st array , the kth element
        							 #will be in (k-i)th index now **IMPORTANT** **IMPORTANT**
    else:
        return(findKth(A,B[j:],k-j))                
            

for _ in range(int(input())):
    N,M,K=list(map(int,input().split()))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    print(findKth(A,B,K))