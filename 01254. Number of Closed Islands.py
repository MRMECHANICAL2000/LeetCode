"""   
Key : initially you had no idea on how to solve this question. you know how to find number of 
	  island but you dont know how to find closed island. initially you taught find all island
	  at first dfs and in sencond dfs you taugh for each cell of island we check all 4 side 
	  and see we have water all side. your idea was pretty dump. look the question carefully.
	  only the island that are in border wont be surrended by water, all other island can be
	  surronded by water. so just go and find all islnad while finding them itself check
	  if its an corner cell , if yes dont increment the islandCount.
	  **IMPORTANT** **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Number of Closed Islands
Problem Url    : https://leetcode.com/problems/number-of-closed-islands/
Solution Video : https://youtu.be/YwL2WWxEEYQ -> using 2 DFS calls
				 https://youtu.be/MnD8KhBHgRo -> checking only (1,1) to (n-1,n-1)

Learning:
    Brute: **IMPORTANT**
        using 2 DFS calls, you just do 1st dfs and find all the island.then while finding it
        we also check if its a corner island , if yes you replace all land of that island with
        water, so now in 2nd dfs call all the island we find are closed island only.

    Better: **IMPORTANT**
    	we know that the island in corner cell wont be closed island , so we skip searching for
    	island in corner we check only island in range (1,1) to (n-1,n-1)
        
    Optimal: **IMPORTANT**
        Approach -> while doing dfs itself keep track of wheather we visit any corner cell while
        			travesing this island , we find the entire island mark as visited if there
        			is any corner cell we wont increment the islandcount.

""" 
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])        
        visited=[[False for i in range(m)] for j in range(n)]
        
        def dfs(row,col):
            if row<0 or row>=n or col<0 or col>=m:
                return("corner")     #only change from Island question **IMPORTANT**

            if  grid[row][col]==1:
                return("Not_corner")
            
            if visited[row][col]==True:
                return("Not_corner")
            
            
            visited[row][col]=True
            direction=[[0,-1],[-1,0],[0,1],[1,0]]
            
            is_corner="Not_corner"
            for i in direction:
                nextRow=row+i[0]
                nextCol=col+i[1]
                temp=dfs(row+i[0],col+i[1])
                if temp=="corner":
                    is_corner= temp                    
            return(is_corner)
        
        count=0
        for row in range(n):
            for col in range(m):
                if visited[row][col]==False and grid[row][col]==0:
                    if dfs(row,col)!="corner":
                        count+=1
        return(count)