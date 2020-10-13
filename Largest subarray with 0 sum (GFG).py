"""
Key : They are asking us to find the length of largest subarray with zero sum not to count the
      number of subarray with sum 0. dont confuse with previous problem count subarray with sum k
      Dont forget if curSum=0 means entire array length up to current index sum up to 0 **IMPORTANT**
"""

"""
Problem Name   : Largest subarray with 0 sum
Problem Url    : https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
Solution Video : https://youtu.be/xmguZ6GbatA     **IMPORTANT**

Learning:
	Brute: 
		Using two loop 

	Optimal: **IMPORTANT**
		Approach -> Using HashTable , store curSum in HashMap, check if curSum exist in HashTable
					if exist means there is an array from exist index to current Index summing up to 0
					if curSum is 0 means entire array sum until that index is 0
 					Watch video for explanation **IMPORTANT**

"""	

def maxLen(n, arr):
    HashMap={}
    curSum=0
    count=0

    for i,v in enumerate(arr,1):
        curSum+=v
        					# **IMPORTAT**
        if curSum==0:       # Dont forget this step , if curSum=0 means entire array sum=0 **IMPORTANT**
            count=i
            continue

        try:
            if HashMap[curSum]:
                count=max(count,i-HashMap[curSum])
        except Exception:
            HashMap[curSum]=i

    return(count)  


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends