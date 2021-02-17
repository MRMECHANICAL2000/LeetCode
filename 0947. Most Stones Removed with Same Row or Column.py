"""   
Key : this question looks scary a bit initially, you dont even know that it looks like a graph
	  question.always when you see points/2d planes mostly they will be graph question only.
	  ones you are given a question first draw it and see.

	  initially your idea is to take all points and do some fluffy unwanted things like
	  finiding optimal stone to remove and so on. hey creap, its an simple question you 
	  need to find island in graph from each island we can remove all stones expect one because
	  we create island by joinig stones that are either same row/col.
	  **IMPORTANT** **IMOPRTANT**
"""

"""
Problem Name   : Most Stones Removed with Same Row or Column
Problem Url    : https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
Solution Video : 

Learning:
    Brute:        
        

    Better:
        
    Optimal: **IMPORTANT**
        Approach -> take all points and store them in rowHashTable and colhashTable. do an dfs
        			and find islands at each point using visited array. finally we can say that
        			total stones-number of island=max stone can be removed. because from an
        			single island we can take all the stones other than one stones.so at each 
        			island one stone will remain, totalStone-remaining=max taken.

        			you can use dfs or union find to find island in graph.

""" 
from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rowHashTable=defaultdict(set)		#storing places where we can go from a point
        colHashTable=defaultdict(set)		#**IMPORTANT**
        visited={}

        for i in stones:
            #you cant hash a list
            rowHashTable[i[0]].add((i[0],i[1]))
            colHashTable[i[1]].add((i[0],i[1]))
            visited[(i[0],i[1])]=False
        
        def findIsland(point):                       #Findnig island using Dfs
            if visited[(point[0],point[1])]==True:
                return()
            visited[(point[0],point[1])]=True
            
            for i in rowHashTable[point[0]]:
                findIsland(i)
                
            for i in colHashTable[point[1]]:
                findIsland(i)
        
        islandCount=0
        for i in stones:
            if visited[(i[0],i[1])]==False:
                findIsland(i)
                islandCount+=1

        return(len(stones)-islandCount)