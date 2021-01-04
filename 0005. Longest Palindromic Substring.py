"""   
Key : finding an odd palindrome is easy but finding an even palindrome is tough but we have an trick 
	  to convert an even palindrome to odd palindrome to insert an "#" in between each character,

	  "abba"  -> "a#b#b#a"    (even palindrome now become odd)
	  "abcba" -> "a#b#c#b#a"   (odd palindrome is still odd palindrome)

	  oftern think of changing the order of doing some operations because may be then the solution will
	  be easy. here we can take a string and check 1st and last char, 2nd and 2nd last char..... until
	  we reach center of palindrome. Another way is to expand form middle, from each character expand to
	  our left and right and check if its palindrome. if we can think of this thinking DP will be easy
	  **IMPORTANT**
"""

"""
Problem Name   : Longest Palindromic Substring
Problem Url    : https://leetcode.com/problems/longest-palindromic-substring/
Solution Video : https://youtu.be/UflHuQj6MVA -> DP solution **IMPORTANT* Must Must Watch
				 https://youtu.be/y2BD4MJqV20 -> Expand from center **IMPORTANT**
				 https://youtu.be/V-sEwsca1ak -> Manichers Algorithm
				 **IMPORTANT**Must watch to know Manichers O(N) linear time Approach **IMPORTANT**
                 

Learning:
	Brute:
		use two loop find all the substring and check if they are palindrome. O(N^3)
		
	Better: **IMPORTANT**
		using Dynamic Programming, O(N^2) time and space
		just look the video you will get the intutuion and how data filled in the table. 
		the idea is to check if a string of size n is palindrome , we check if 1st and last
		char are same , if yes we check if 2nd and 2nd last char is same, then 3rd and 3rd last char....
		until we reach single character or no character.(top down approach). we solve the DP by bottom
		up approach. we 1st know all single char are palindrome so we put 1 for them in DP table , then
		we check 2 char alone and store its result. after than using this we solve other. we start
		checking from 3 char, we check if 1st and last char are same if yes we go table and see if 2nd and
		2nd last char are same.... then start checking for 4 char, 5 char.... Unlike other DP problem we
		cant trace the output from table so we store the max palindrome each time we find a new one.


	Optimal: **IMPORTANT**
		Approach 1 -> Expand from center , Takes O(N^2) time and O(1) space. for each index check max 
					  odd palindrome and max even palindrome that can be formed from that index

		Approach 2 -> using Manachers Algorithm, Takes O(N) linear time only. highly used in 
					  competative programming. Must Watch video to learn it
					  We have not implemented it yet

"""	

class Solution:
    #Brute Force Method 
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return(s)
        ans=""
        for i in range(0,len(s)-1):
            for j in range(i,len(s)):
                temp=s[i:j+1]
                											  #**IMPORTANT**
                #if temp==temp[::-1] and len(ans)<len(temp):  #both this condition are same but below
                if len(ans)<len(temp) and temp==temp[::-1]:   #condition runs faster because c,c++,python
                    ans=temp[:]							  	  #uses lazy if consition, if it finds 1st 
                        									  #condition is fase then it wont execute the
                        									  #second condition because anyhow it gona fail
        return(ans)
        

    #Better Approach -> DP Based
    def longestPalindrome(self, s: str) -> str:
        DP=[[0 for i in range(len(s))]for j in range(len(s))] #creating 2D DP table of size len(s)*len(s)

        maxLenPalindrome=0							#In this question we cant backTrack the DP table
        											#to get the max palindrome, so we store the start
        											#and end of max palindrome ones we found it
        palinStart,palinEnd=0,0

        for i in range(len(s)):			#Making diagonal as 1 because single char is always palindrome        
            DP[i][i]=1
            							#**IMPORTANT**
        for i in range(len(s)-1):       #checking all consecutive 2 char if they are palindrome we put 1
            if s[i]==s[i+1]:
                DP[i][i+1]=1 
                if ((i+1)-i)>=maxLenPalindrome:
                    maxLenPalindrome=(i+1)-i
                    palinStart=i
                    palinEnd=i+1            
        y=2
        for i in range(len(s)-2):       #Checking all characters from size 3 to n. **IMPORTANT**
            for x in range(len(s)-y):
                if s[x]==s[x+y] and DP[x+1][x+y-1]==1: #check if 1st(i) & last(j) char of curString is
                									   # same,if yes then check if s[i+1:j-1] is palindrome
                									   #to check that we use DP table
                    DP[x][x+y]=1

                    if ((x+y)-x)>=maxLenPalindrome:     #keeping track of biggest palindrome each time we
                        maxLenPalindrome=(x+y)-x		#Encounter an new palindrome **IMPORTANT**
                        palinStart=x
                        palinEnd=x+y
            y+=1

        return(s[palinStart:palinEnd+1])   #Returning the longest palindrome
        


    #Optimal Approach -> Expand from center
    def longestPalindrome(self, s: str) -> str:
        def possiblePalindrome(left,right):
            #print(left,right)
            if left<0 or right>=len(s):	#**IMPORTANT**
                return(0)               #if limit get out of bound no more palindrome can be created

            if s[left]==s[right]:
                left-=1
                right+=1								  #**IMPORTANT**
                return(2+possiblePalindrome(left,right))  #No need to return the left,right value at 
                										  #which we got palindrome,just return max size
                										  #of palindrome from that we can know where it
                										  #starts and ends. make it simple not complicated
            else:
                return(0)               #if left,right dont match no more palindrome can be created

        ans=""
        maxPalin=0
        palLeft=0
        palRight=0
        for idx in range(len(s)-1):					 #**IMPORTANT**
            oddPalin=possiblePalindrome(idx,idx)-1   #to get max odd palin that can be formed from this idx
            evenPalin=possiblePalindrome(idx,idx+1)  #to get max even palin that can be formed from this idx

            #storing the maxPalin drome
            if oddPalin>maxPalin:
                maxPalin=oddPalin
                palLeft=idx-oddPalin//2
                palRight=idx+oddPalin//2
            if evenPalin>maxPalin:
                maxPalin=evenPalin
                palLeft=idx-(evenPalin-1)//2
                palRight=idx+(evenPalin)//2
                
        return(s[palLeft:palRight+1])
