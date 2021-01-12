"""    
Key : Must learn about function tools lru_cache. similair to implementing an hashTable, it stores both
	  function name argument passed and value returned for that arugment by the function. when next time
	  same argument passed it returns the value instead of recalculating it again.
	  https://www.geeksforgeeks.org/python-functools-lru_cache/
	
	  **IMPORTANT** **IMPORTAT**
		
	  lru_cache + Recursion = 157 MB
	  DP Table  + looping   = 16.7 MB


"""  

"""
Problem Name   : Minimum Insertion Steps to Make a String Palindrome
Problem Url    : https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
Solution Video : https://youtu.be/rSEoN6qnb8Q


Learning:
	Brute:
		compare last two index, if they are same means increment the 1st index and decrement the last 
		index. if they are different means we have two choice either we can insert a character at front
		which is same as last character or we can insert a character at back which is same as front
		character to make the given string palindrome. we try both and take which ever step gives
		palindrome in minimum steps.

	Better: **IMPORTANT**  **IMPORTANT**
		instead of inserting a character we can just increase the left or right pointer. think twise
		you will understand.
		  
		  L   R
		0 1 2 3 4
		a b c d a -> two choice 
						inserting at L : 0 1 1 2 3 4		0 1 1 2 3 4
										 a d b c d a 	 -> a d b c d a         (Next Step)
										   L     R       	    L R

						inserting at R : 0 1 2 3 3 4	    0 1 2 3 3 4
										 a b c d b a 	->  a b c d b a
										   L     R 		   	    L R

		In both inserting at left and right you see after the insesion step either R index reduce by 1
		or L index increased by 1 no more effect of insersion. so instead of wasting time on inserting
		we can just increase the index that is how a good programmer will think.

		finally we should need to cach some result inbetween so that we do not recompute same things
		again and again. we may use an HashTable for memoization but here for easiness we use lru_cache
		from python functools library.

	Optimal: **IMPORTANT** **IMPORTANT**
	  Approach 1 -> Using DP Table, if we use recursion + memoization we need extra space. create 
	  			   a DP table fill all detail we know first, single char need 0 insersion to become
	  			   palindrom. substring of size 2 requires 0 or 1 insersion to make given string as
 	  			   palindrome. for remaining substring of size 3 and more. if last two char same
 	  			   it requires 0 insersion + no of insersion required to make substring i+1,j-1 as a 
	  			   palindrome. if last two char not same 1 inserion + min(insersion to make two of
	  			   its substing palindrome (i,j-1) or (i+1,j))

	  Approach 2 -> write DP code to find longest palindromic subSequence , subtract that from total
	  				length you will get the minimum no of character to be inserted to make the string 
	  				palindrome
"""	

from functools import lru_cache
class Solution:
	#Better Solution
    def minInsertions(self, s):            
        left=0										#Initilizing Left,Right Pointers
        right=len(s)-1
        
        @lru_cache(None) 							#Cach the intermediate results **IMPORTATN**
        def palInsersion_Optimal(left,right):
            if left-right==0 or left-right==1:		#base case if no string or single char they are
                return(0)							#already palindrome no more insersion required

            if s[left]==s[right]:					#if both left and right are same, no insersion
            										#required just increase the pointer to next position
                return(palInsersion_Optimal(left+1,right-1))

            else:									#if left, right not same two choise either increase
            										#left or decrease right,take min of both
                lInsersion=palInsersion_Optimal(left,right-1) 
                rInsersion=palInsersion_Optimal(left+1,right)
                return(1+min(lInsersion,rInsersion)) #'+1' must put because it is to indicate we are 
                									 #inserting an character            
        return(palInsersion_Optimal(left,right))
            
            
    #Optimal 1  
    def minInsertions(self, s):
    	#Creating DP Table            
        DP=[[0 for i in range(len(s))] for j in range(len(s))]
        
        #for i in range(len(s)):	#this step not need because we alredy know for single character no
        #    DP[i][i]=0				#insersion is required , they are already palindrome **IMPORTANT**

        for i in range(len(s)-1):   #checking if 2 char are palindrome, if not we need min 1 insersion
        							#to make them palindrome
            if s[i]!=s[i+1]:
                DP[i][i+1]=1

        for i in range(len(s)-2,-1,-1): #checking for remaining size substring **IMPORTANT** **IMPORTANT**
        								#looping for back size is easy, memorize the loop condition 
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    DP[i][j]=DP[i+1][j-1] #if both are same, 0 insersion + insersion to make substring palindrome

                else:					  #if both are different, 1 insersin + min(two choices)
                    DP[i][j]=1+min(DP[i+1][j],DP[i][j-1])
        
        return(DP[0][-1])

    #Optimal Approach 2 -> (lenth-longest palindromic Subsequence)
    def longestPalindromeSubseq(self, s: str) -> int:
        DP=[[0 for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(s)): 		#all char are longest sequence of size 1
            DP[i][i]=1

            
        for i in range(len(s)-1):		#if two char same they are longes sequence of size 2 else 1
            if s[i]!=s[i+1]:
                DP[i][i+1]=1
            else:
                DP[i][i+1]=2

                
        for i in range(len(s)-3,-1,-1):
            for j in range(i+2,len(s)):
                if s[i]==s[j]:				 #if last two char same means they are longest sequence
                							 #with size 2+ longest sequence exist in substring
                    DP[i][j]=2+DP[i+1][j-1]
                else:
                    DP[i][j]=max(DP[i+1][j],DP[i][j-1])
                    						 #if last two char diff means they are longest sequence
                							 #with size 1+ longest sequence exist in either of 2 substring

                    
        return(len(s)-DP[0][-1])
