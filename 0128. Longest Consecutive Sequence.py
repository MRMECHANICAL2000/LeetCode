"""
Key : if we sort the array , element order changes. Interviewer won't be happy if the we are
	  disordering the array. he will ask use to optimize **IMPORTANT**
"""

"""
Problem Name   : Longest Consecutive Sequence
Problem Url    : https://leetcode.com/problems/longest-consecutive-sequence/
Solution Video : https://youtu.be/qgizvmgeyUM           **IMPORTANT** Must Watch

Learning:
	Brute: 
		sort and traverse the array linearly to check consequetive sequence

	Optimal: 
		Approach -> Using HashTable and store all the element. linearly iterate through each element
					and check if i-1 exist if exist leave, if not exist check i+1,i+2,i+3.... and strore
					the count. look video for why we do it. if not done like it for each element we
					go n checking at worst leads to n^2 complexity. here only after knowing we are at
					starting of sequence we check for next element.   **IMPORTANT**

"""	

from collections import defaultdict            #**IMPORTANT** Collection's' spelling don't forget
class Solution:
	#Optimal
    def longestConsecutive(self, nums: List[int]) -> int:
        HashTable=defaultdict(bool)
        longSeq=0
        for i in nums:
            HashTable[i]=True

        for i in nums:
            if HashTable[i-1]==True:          #checking if this element is begining of sequence **IMPORTANT**
                continue

            else:
                curSeq=1                      #finding length of sequence
                curEle=i+1
                while True:
                    if HashTable[curEle]==True:
                        curSeq+=1
                        curEle+=1
                    else:
                        break
                if curSeq>longSeq:
                    longSeq=curSeq
                    
        return(longSeq)
