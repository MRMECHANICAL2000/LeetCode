"""   
Key : really simple question although it seems realy hard, have no idea to solve at first.
	  while explaining this questoin to team mates you messed up a lot. look the question 
	  properly. must learn the taught process behind this question.
	  **IMOPRTANT**
"""

"""
Problem Name   : Subarrays with K Different Integers
Problem Url    : https://leetcode.com/problems/subarrays-with-k-different-integers/
Solution Video : https://youtu.be/88mGJqbnPVw
				 **IMPORTANT** watch the video if you cant understand the description

Learning:
	Brute:
		take window of size k and check how many k distinct element window accurs. then 
		take window of size k+1,k+2... until k+x=n, add all distinct element window finally
		return the count.
		
	Better: 
		
	Optimal: **IMPORTANT** **IMPORTANT** **IMPORTANT**
		Approach -> write the code to find the window with k distinct integre, and at each
					iteration we include all the subArray possible with the curWindow.ie,

					for window=[1,2,3] => [1],[1,2],[1,3]
					total 3 subArray possible. for each window of k and <k distinct integeres
					we store total subArray possible.


					then the main idea is,
					for window k distinct integer we have sub array of size with 1,2,3,4....,k-1,k
					for winodw k-1 distinct integre we have sub array of size 1,2,3,4...k-1

					if we subtract both the count we get subArray with k distinct integer.
					(1,2,3,4...k-1,k)-(1,2,3,4...k-1)=k


"""	

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        def slidingWindow(arr,k):
            hashTable={}
            allPossibleSubArrCount=0  #**IMPORTANT**
            uniqueCount=0
            start=0
            for idx,val in enumerate(arr):
                if val not in hashTable:
                    uniqueCount+=1
                hashTable[val]=idx

                while start<len(arr) and uniqueCount>k:
                    if hashTable[arr[start]]==start:
                        hashTable.pop(arr[start])
                        uniqueCount-=1
                    start+=1
                    
                allPossibleSubArrCount+=idx-start+1  #**IMPORTANT** Heart of the code.
            return(allPossibleSubArrCount)
        
        return(slidingWindow(A,K)-slidingWindow(A,K-1))  #Trick to solve this question 
        												 #**IMPORTANT**    