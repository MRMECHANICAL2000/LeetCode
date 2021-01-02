"""   
Key : s.strip().split() order is important dont put .split().strip() then the program raise error since 
	  we are doing strip in list after split() string become list
"""

"""
Problem Name   : Reverse Words in a String
Problem Url    : https://leetcode.com/problems/reverse-words-in-a-string/
Solution Video : https://youtu.be/hQFr4p1OKpk
                 

Learning:
	Brute:

		
	Better:
		Using python split(),strip(),join() method	

	Optimal: 
		Approach -> Reverse the entire string , then reverse each word in the string.

					"This is my life" -> Given I/P 
					"efil ym si ishT" -> Reversing Entire String
					"life my is This" -> Reversing each character in string		
"""	

class Solution:
	#Better Solution
    def reverseWords(self, s: str) -> str:
        return(" ".join(s.strip().split()[::-1]))
