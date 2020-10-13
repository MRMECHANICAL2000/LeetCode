"""
Key : while storing in HashTable store the index of element as well , insted of pop from front
	  directely skip to repeating_element_location+1, while checking wheather an element is repeated
	  or not we need to take care of edge case like if element is 0 and index also 0 in Approach 1
	  and in Approach 2 How to find element repeat or not since no pop in HashTable
	  See the video to learn the trick  **IMPORTANT**
"""

"""
Problem Name   : Longest substring without repeat 
Problem Url    : https://leetcode.com/problems/longest-substring-without-repeating-characters/
Solution Video : https://youtu.be/qtVh-XEpsJo           **IMPORTANT** Must Watch

Learning:
	Brute: 
		Using two loop and find all substring and check for repeat. O(n^2) time and O(1) space

	Optimal:   **IMPORTANT**
		Approach 1-> Using HashTable,use two pointer one to iterate(j) other in Index 0(i)
					 at each j store the string in Hashtable before adding a string check 
					 if it already exist ,if existed pop from front using (i) until the element
					 is removed.ones there is no repeat procede further.
		Approach 2-> Previous approach takes O(2N) times , we take O(N) for j and O(N) for i.
					 so instead of pop from start i to repeating character each time, while storing
					 char store its index so that we can directely jump to that position.
					 Must watch video to understand how Approach 2 works. **IMPORTANT**

"""	

class Solution:
	#Optimal Approach-1
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return(0)
        HashTable={}
        i=0
        j=0
        count=len(HashTable)
        
        while j<len(s):
            try:
                if HashTable[s[j]]>=0 :                  #By pop from i method
                    temp=HashTable[s[j]]+1
                    for x in range(i,HashTable[s[j]]+1):
                        HashTable.pop(s[x])
                    i=temp                        
                                      
            except Exception:
                pass
            HashTable[s[j]]=j
            j+=1
            count=max(count,len(HashTable))            

        return(count)
                

	#Optimal Approach-2
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return(0)

        HashTable={}
        i=0
        j=0
        count=len(HashTable)
        
        while j<len(s):
            try:										#By Jumping Mehod, **IMPORTANT**
                if HashTable[s[j]]>=0 and HashTable[s[j]]>=i:
                    i=HashTable[s[j]]+1                        
                                      
            except Exception:
                pass

            HashTable[s[j]]=j
            j+=1
            count=max(count,j-i)            

        return(count)
                
            