"""   
Key : min, max in array of string wont return string with max,min length it returns strings with.
	  also look the trie approach.
	  **IMPORTANT**
"""

"""
Problem Name   : Longest Common Prefix
Problem Url    : https://leetcode.com/problems/longest-common-prefix/
Solution Video : https://www.youtube.com/watch?v=fhyIORFDD0k
				 **IMPORTANT**Must watch to know Trie Approach **IMPORTANT**
                 

Learning:
	Brute: **IMPORTANT**
		Take a string and compare it with all strings and find longest common prefix.
		O(len(bigString)*NoOfString)->O(n^2)
		
	Better: **IMPORTANT** **IMPORTANT**
		Using an Trie, store all the value in it and out put the longest common prefix
		O(sum(len(all string)))->O(n^2) to create trie it takes.

	Optimal: **IMPORTANT**
		Approach -> find min(string) and max(string) , compare these two alone. min,max string
					is found not wrt to length of string its found wrt the string itself.
					
					>>> x=['a','b','c','d']
					>>> min(x)
					'a'
					>>> max(x)
					'd'
					>>> x=['aa','ab','ac','ad']
					>>> _
					'd'
					>>> min(x)
					'aa'
					>>> max(x)
					'ad'
					>>> x=['aa','aaaa','ab','ac','ad']
					>>> min(x)
					'aa'
					>>> max(x)
					'ad'
					>>> x.sort()
					>>> x
					['aa', 'aaaa', 'ab', 'ac', 'ad']
					>>> 

					so if we take min,max in ""strs = ["flower","flow","flight"]"" it return
					>>> strs = ["flower","flow","flight"]
					>>> min(strs)
					'flight'
					>>> max(strs)
					'flower'
					>>>
					which is what we want., char wise different element will be returned. 

"""	

#Better Trie Approach
class TrieNode:
    def __init__(self):
        self.child={}
        self.endsHear=False
        self.count=0
        
class Trie:
    def __init__(self):
        self.head=TrieNode()       

    def insert(self, word: str) -> None:        
        temp=self.head
        for i in word:
            if i not in temp.child:
                temp.child[i]=TrieNode()
            temp.count+=1
            temp=temp.child[i]
        temp.endsHear=True       

    def search(self, word: str) -> bool:
        temp=self.head
        for i in word:
            if i not in temp.child:
                return(False)
            temp=temp.child[i]
        return(temp.endsHear)

    def startsWith(self, prefix: str) -> bool:
        temp=self.head
        for i in prefix:
            if i not in temp.child:
                return(False)
            temp=temp.child[i]
        return(True)
    
    def longestCommonPrefix(self):    #adding additional to trie class for this question.
        temp=self.head
        ans=""
        count=temp.count

        #if there is only one child and count of that child and prev node is same meas they
        #are common prefix . think twice to understand . **IMPORTNATNT**
        while temp.count==count and len(temp.child)==1:
            #we are checking the count also here because if one of the child is "" **IMPORTANT**
            key=[i for i in temp.child.keys()][0]
            ans+=key
            count=temp.count
            temp=temp.child[key]
        return(ans)
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        obj=Trie() #you dont need to inherit trie class to get its object
        for i in strs:
            if not i:
                return("")
            obj.insert(i) #inserting all the string into the Trie
        return(obj.longestCommonPrefix()) #creating an function inside the Trie class to find
        								  #longest common prefix.



#Optimal Solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return("") #Edge case
        s1=min(strs)
        s2=max(strs)
        print(s1,s2) #min,max wrt string not length of string **IMPORTANT**

        for idx,val in enumerate(s1):
            if val!=s2[idx]: #if one element is different then return it.
                return(s1[:idx])
        return(s1)
