"""
Key : know how to add element and check present of element in an set.
      https://www.geeksforgeeks.org/python-sets/
      Must watch the video to know the intution on how to approach the problem
      **IMPORTANT** **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Word Break
Problem Url    : https://leetcode.com/problems/word-break/
Solution Video : https://youtu.be/hLQYQ4zj0qg
				 https://youtu.be/WepWFGxiwRs
				 **IMPORTANT** Must Must Must Must Must Watch both the video **IMPORTANT**  
				 To know the intution as well as two different DP table method.
Learning:
    Brute:  **IMPORTANT**
    	using Recursive DFS Approach.just check all possible splits in the string.

	Better: **IMPORTANT**
		using same Recursive DFS Approach just memoise and catch some solutions in between


    Optimal: **IMPORTANT**
        Approach -> using Bottom up approach in the DP table. must watch the video to get intution of
        			all the 3 methods
        		    **IMPORTANT**

"""	

class Solution:

    #Brute - Recursive DFS Approach
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)  #**IMPORTANT** Know how to use set in python
        def DFS(s):
            if s=="":
                return(True)    #Base Case
            if s in wordDict: 
                return(True)    #Base Case

            for i in range(0,len(s)):
                if s[:i+1] in wordDict:
                    result=DFS(s[i+1:])
                    if result==True:    #if any one split is True its enough. if not then contuniue next iter
                        return(result)  #**IMPORTANT**

            return(False)
        return(DFS(s))
    
    #Better -Memoised Recursive DFS Approach
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        memoTable={}
        def DFS(s):
            try:                          #Memoization of the Result
                return(memoTable[s])
            except:
                pass

            if s=="":                     #Base case
                return(True)
            if s in wordDict:
                return(True)

            for i in range(0,len(s)):
                if s[:i+1] in wordDict:
                    memoTable[s[:i+1]]=True
                    result=DFS(s[i+1:])       #Recursion Code
                    memoTable[s[i+1:]]=result
                    if result==True:          #if atleast one split is possible return True
                        return(result)
                        
            memoTable[s]=False                #If No split possible then for that sub string s put False
            return(False)
        return(DFS(s))

    #Optimal - Bottom UP DP Table Approach
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        DP=[True]+[False for i in range(len(s))] #ie,DP[0]=True **IMPORTANT**

        for i in range(len(s)+1):
            for j in range(0,i):
                if DP[j] and s[j:i] in wordDict:  #Carefully learn where to put i,j,j:i dont memorise
                    DP[i]=True					  #Think twise to know how it works
                    break
        return(DP[-1])
        
