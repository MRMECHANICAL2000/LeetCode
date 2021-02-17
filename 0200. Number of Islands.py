"""   
Key :

"""

"""
Problem Name   : Number of Islands
Problem Url    : https://leetcode.com/problems/number-of-islands/
Solution Video : https://youtu.be/__98uL6wst8

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT**
        Approach -> have an visited array , traverse through the grid , when you visit and
       				cell which has not already been visited and has value 1 in it we increment
       				the island count to +1, we do dfs in it and visit all its neighbour mark
       				them as visited. finally return the island count. 

""" 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid),len(grid[0])        
        visited=[[False for i in range(m)] for j in range(n)] #Visited Array
        
        def dfs(row,col):
            if row<0 or row>=n or col<0 or col>=m:
                return()           

            if  grid[row][col]=="0":
                return()
            
            if visited[row][col]==True:
                return()
            
            
            visited[row][col]=True
            direction=[[0,-1],[-1,0],[0,1],[1,0]]
            
            for i in direction:
                nextRow=row+i[0]
                nextCol=col+i[1]
                dfs(row+i[0],col+i[1])
                        
            return()
        
        count=0
        for row in range(n):
            for col in range(m):
                if visited[row][col]==False and grid[row][col]=="1":
                    dfs(row,col)
                    count+=1		#Each time we do a dfs call means we have find a new island
        return(count)