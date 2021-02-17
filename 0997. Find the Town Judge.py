"""   
Key : 
"""

"""
Problem Name   : Find the Town Judge
Problem Url    : https://leetcode.com/problems/find-the-town-judge/
Solution Video :                  

Learning:
	Brute:
		
		
	Better:
		
	Optimal: **IMPORTANT**
		Approach -> simple graph problem, find the vertex which has no outgoing edges but has
					incomming edges from all the nodes.

"""	

from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        hashTable=defaultdict(list)
        for i in range(1,N+1):
            hashTable[i]=[False,0]      #[False,0]->{do i trust anyone , no of people trust me}

        for i in trust:
            hashTable[i[0]][0]=True
            hashTable[i[1]][1]+=1
            
        for i in hashTable:
            if hashTable[i][0]==False and hashTable[i][1]==N-1:
                return(i)
        return(-1)