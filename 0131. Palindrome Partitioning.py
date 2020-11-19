"""
Key : this question is reallly simple if you see the video and follow the procedure you will defenitely
	  code it within seconds. but you wasted 6 hours stating you will do your own method and finally used
	  the same method as that of video. you need to make ceratain changes in your backTracking code to make 
	  correct answer. 
      **IMPORTANT** **IMPORTANT** 
"""

"""
Problem Name   : Palindrome Partitioning
Problem Url    : https://leetcode.com/problems/palindrome-partitioning/
Solution Video : https://www.youtube.com/watch?v=aFrM192tLWE
       			**IMPORTANT**Must Must  Must Must Must watch just 4 minutes video **IMPORTANT**
				 
Learning:
    Brute:  **IMPORTANT**
    	find all the partation and verify each if its palindromic partation then append it to the
    	solution

    Optimal: **IMPORTANT**
        Approach -> using BackTracking ,same brute force approach but if you find curPartition forms palindrom
        			then alone recurse on remaining part else skip it.
			
        			
"""	

class Solution:

    #Optimal Approach - BackTracking 
    def partition(self, s: str) -> List[List[str]]:
        global result
        result=[]  #**IMPORTANT**  **IMPORTANT**
        temp=[]    #Both result and temp(Temperary partation) should need to be declared as global
        def isPalindrome(curString):            #Seperate function must must be used to find palindrome/not
            return(curString==curString[::-1])  #else lot of confusion on question arrise since recursive
        
        def decomposeString(curString,temp):

            if curString=="":         #We should need to append the result if we reach the end of the string
                result.append(temp[:])#not when we find an palindrome or other stuff. **IMPORTNAT** **IMPORTANT**
                
            for i in range(1,len(curString)+1):
                if isPalindrome(curString[:i]): #if this split is palindrome add the split to temp and then
                    temp.append(curString[:i])  #then decompose the remaining to check if its palindrome 
                    decomposeString(curString[i:],temp)
                    temp.pop()                  #Must Must pop the previously added split then only we can 
                    							#go and check for new splits. this step is really realy important
                    							#you must need to understand it well
                
        decomposeString(s,temp)
        #print(result)
        return(result)
        