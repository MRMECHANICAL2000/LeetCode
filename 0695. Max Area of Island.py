"""   
Key :

"""

"""
Problem Name   : Max Area of Island
Problem Url    : https://leetcode.com/problems/max-area-of-island/
Solution Video : 

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT**
        Approach -> same as number of island question here we store the length of each island
        			and finally return the max of  all island.

""" 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        n,m=len(grid),len(grid[0])        
        visited=[[False for i in range(m)] for j in range(n)]
        
        def dfs(row,col,landSize):
            if row<0 or row>=n or col<0 or col>=m:
                return(0)           

            if  grid[row][col]==0:
                return(0)
            
            if visited[row][col]==True:
                return(0)
            
            landSize+=1
            visited[row][col]=True
            direction=[[0,-1],[-1,0],[0,1],[1,0]]
            
            for i in direction:
                nextRow=row+i[0]
                nextCol=col+i[1]
                landSize+=dfs(row+i[0],col+i[1],0)

            return(landSize)
        
        maxLandSize=0
        for row in range(n):
            for col in range(m):
                if visited[row][col]==False and grid[row][col]==1:
                    maxLandSize=max(maxLandSize,dfs(row,col,0))
        return(maxLandSize)