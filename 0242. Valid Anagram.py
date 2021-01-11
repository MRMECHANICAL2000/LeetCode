"""    
Key : 
""" 

"""
Problem Name   : Valid Anagram
Problem Url    : https://leetcode.com/problems/valid-anagram/
Solution Video : 


Learning:
	Brute:
		sort both the string and compare.
		
	Better:
		store the frequency of each of both string two hashTable and compare both hashTable.


	Optimal: **IMPORTANT**
	  Approach -> store the frequency of one string in one hashTable and loop through another
	  			  string and reduce the frequency of this string from that hashTable.finally
	  			  if all value in hashTable are 0 both are anagram else not anagrams.

"""	
class Solution:
	#Optimal Approach
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable={}
        for i in s:
            if i not in hashTable:
                hashTable[i]=1
            else:
                hashTable[i]+=1
                
        for i in t:
            if i not in hashTable:
                return(False)
            else:
                hashTable[i]-=1

        for i in hashTable.values():
            if i!=0:
                return(False)
        return(True)
                
        