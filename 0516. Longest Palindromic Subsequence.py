"""    
Key : make sure to see the loop condition carefully, its very curcial

"""  

"""
Problem Name   : Longest Palindromic Subsequence
Problem Url    : https://leetcode.com/problems/longest-palindromic-subsequence/
Solution Video : https://youtu.be/_nCsPn7_OgI 
				 **IMPORTANT** Have a look if you cant understand notes

Learning:
	Brute:
		
	Better: 
		
	Optimal: **IMPORTANT** **IMPORTANT**
	  Approach -> same as min insersion question, just small variation in code. first we write all
	  			  data we know. single char can make longest palindromic sequence of size 1. if two
	  			  char are same it can make longest palindromic sequence of size 2 if different size 1.
	  			  for all other subString if 1st and last char are same it can make 2+longest palindrome
	  			  inside that substring. else 1 + max of two possibel palindrome subsequence


"""	

class Solution:
    #Optimal Approach 
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

                    
        return(DP[0][-1])