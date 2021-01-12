"""    
Key : for palindromic sequence only we do s+'$'+s.reverse() not here. this is an simple kmp 
      implementation question

"""  

"""
Problem Name   : Longest Happy Prefix
Problem Url    : https://leetcode.com/problems/longest-happy-prefix/
Solution Video : 

Learning:
	Brute:
		
	Better: 
		
	Optimal: **IMPORTANT**
	  Approach -> using KMP string matching algorithm

"""	

class Solution:
    #Optimal Approach 
    def longestPrefix(self, s: str) -> str:
        newString=s
        lps=[0]+[0 for i in range(len(newString))]
        
        start=0
        idx=1
        
        while idx<len(newString):
            if newString[idx]==newString[start]:
                lps[idx+1]=start+1
                start+=1
                idx+=1
            elif start!=0:
                start=lps[start]
            else:
                lps[idx+1]=0
                idx+=1

                
        return(s[:lps[-1]])
