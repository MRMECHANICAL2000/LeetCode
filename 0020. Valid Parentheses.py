"""   
Key : use stack not some brute approach like how you used in google coding contests.
	  to validate the pair easliy we use HashTable
""" 

"""
Problem Name   : Valid Parentheses
Problem Url    : https://leetcode.com/problems/valid-parentheses/
Solution Video : 
                 
Learning:
	Brute:
		using 2 loops and other cheking stuff like how we did in  google coding contests
		really worst approach.

	Optimal: **IMPORTANT**
		Approach -> Using Stack. if the element is open type, then push it to stack. if the element is
					close type, pop out the last inserted element from the stack check if both are same
					if both are same go and check next element if not this is not an valid string. at 
					last if the stack has some element means also its not an valid string because
					some string has no correct pair.
"""	

class Solution:
	#Optimal Approach
    def isValid(self, s: str) -> bool:
        stack=[]
        HashTable={')':'(','}':'{',']':'['} #**IMPORTANT** to check if its correct pair in O(1) time
        for i in s:
            try:
                x=HashTable[i]
                if stack==[] or stack.pop()!=x:
                    return(False)
            except:
                stack.append(i)
        return(not stack and True)
        