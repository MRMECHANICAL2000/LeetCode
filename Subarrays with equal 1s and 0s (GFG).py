"""
Key : Question is similair to count subarray with given sum. just convert all the zero to -1 and 
	  find the subarray with sum 0. you will get all subarrya with equal no of 0 and 1. only a good 
	  programmer will get thaughts like this. you did not even get this intution that this is simialir
	  to question we already solved and we can use that approach. a good programmer will understand and
	  relate questions to each other.
	  **IMPORTANT**
"""

"""
Problem Name   : Subarrays with equal 1s and 0s
Problem Url    : https://practice.geeksforgeeks.org/problems/count-subarrays-with-equal-number-of-1s-and-0s-1587115620/1#
Solution Video : https://youtu.be/lV48UiSRaNM

Learning:
	Brute: 
		Using 2 loops and find count of 1,2 in subArray each time , O(1) space, O(n^3) time

	Better:
		Approach 1 ->using 2 loop and variable to keep count track. O(1) space and O(n^2) time
		Approach 2 ->using a sliding window, create a sliding window of size 2, slide entire array
					 and check if one 0 and one 1 in any subarray, again create an sliding window of 
					 size 4 check if two 0 and two 1 in any subarray. again create an sliding window
					 of size 6,8,10 until you reach size>len(array).

	Optimal: **IMPORTANT**
		Approach -> convert all the 0 to -1 and count all subarry with sum 0. you will get all subarry
					with equal no of 0 and 1. think you will understand why

"""	

from collections import defaultdict            #**IMPORTANT** Collection's' spelling don't forget
#Optimal
def subArrayWithGivenCount(nums,k):             #SubArray Sum equal to k question **IMPORTANT**
    HashMap=defaultdict(bool)
    HashMap[0]=1
    curSum=0
    count=0
    for i in nums:
        curSum+=i
        if HashMap[curSum-k]:
            count+=HashMap[curSum-k]
        HashMap[curSum]+=1            
    return(count)


def countSubarrWithEqualZeroAndOne(arr, N):
    for idx,val in enumerate(arr):              #Convert all zero to -1 **IMPORTANT**
        if val==0:
            arr[idx]=-1

    return(subArrayWithGivenCount(arr,0))

        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]      
        print(countSubarrWithEqualZeroAndOne(arr, n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends