"""    
Key : you dont even realize we can use KMP string matching algorithm for this question. thats the level
	  week you are actually.
""" 

"""
Problem Name   : Shortest Palindrome
Problem Url    : https://leetcode.com/problems/shortest-palindrome/
Solution Video : https://youtu.be/c4akpqTwE5g


Learning:
	Brute:
		insert all character at begining and check which is minimum. O(e^n) exponential time
		
	Better:
		solving it by using two pointer technique like how we solve min insertion to make palindrome.
		we check last and 1st character if they dont match we insert character at first and we recurese
		here.finally return no of character inserted. in that quetsion we insert on both side and check
		in this question we insert only in begining.

	Optimal: **IMPORTANT** **IMPORTANT**
	  Approach -> by using KMP string matching algorithm.(we are using z function here). we create a 
	  			  new string as   string+'$'+revSting and in this new string we find largest prefix
	  			  which is also a suffix. in the lps array the last element is the max prefix which
	  			  is also a suffix. ie.the max possible palindrome inside the string. if we subtract
	  			  it with the total size we will get the minimum insersion to at begining needed.

	  			  aabaac ->  aabaac$caabaa
	  			  			     a a b a a c $ c a a b a a
				  lps Array ->[0 0 1 0 1 2 0 0 0 1 2 3 4 5]

				  so, max palindrome can be of size 5, we need 6-5=1 one character to be inserted at
				  begining to make it full palindrome
"""	
class Solution:
    def shortestPalindrome(self, s):
        tempString=s+'$'+s[::-1]                          #Creating a new string
        lps=[0]+[0 for i in range(len(tempString))]       #LPS array
        start=0
        idx=1

        while idx<len(tempString):                        #finding longest prefix which is also a suffix
        												  #this will give us the max match at front to
        												  #rear and from that we can know how much
        												  #we need to insert at front. **IMPORTATN**
            if tempString[idx]==tempString[start]:
                lps[idx+1]=start+1
                idx+=1
                start+=1

            elif start!=0:
                start=lps[start]

            else:
                lps[idx+1]=0
                idx+=1

        #return(len(s)-lps[-1])			#no of character need to be inserted at begining
        return(s[lps[-1]:][::-1]+s)     #newely created palindrome. **IMPORTANT**
