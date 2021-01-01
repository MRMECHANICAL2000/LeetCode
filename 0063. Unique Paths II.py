"""
Key : Cant use combination like unique path 1 because obstacle given, still we can calucalete total root
      and no of root via obstacle seperately and subtract both to get solution but it get tedious when
      the no of obstacle is high.
      **IMPORTANT** 
"""

"""
Problem Name   : Unique Paths II
Problem Url    : https://leetcode.com/problems/unique-paths-ii/
Solution Video : see the notes created from NPTEL lecture, easy to solve this sum. **IMPORTANT**
                 https://youtu.be/z6kelCB0ww4   

Learning:
	Brute: 
		use recursion, at each cell two recursion one down other right find all path and count the 
        unique paths.if obstacle dont recurse on that path.

	Optimal: **IMPORTANT**
		Approach -> using Dynamic Programming, create a matrix and find solution. same as Unique path 1
                    there we add value in top and left box. here also we do same but if our box has
                    obstacle we simply put 0 and move because on path can be formed there. **IMPORTANT**
                    like previous question we wont initilize 1st row and col to 1 initially, here we
                    initially check which box has obstacle then we put -1 on those box.then check if
                    [0,0] is free, then we put 1 there and start filling DP table from there Left to Right.
                    if it has obstacle we put 0 there and start filling DP table. obviously we end up with 
                    0 paths in this case.

"""	

class Solution:
	#Better Approach
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=-1  #Noting where obstacle comes **IMPORTANT**

        obstacleGrid[0][0]=1 if obstacleGrid[0][0]!=-1 else 0 #Checking [0,0]th cell if no obstacle
                                                              #initilize it with 1 else 0
        
        for i in range(m):                     #Filling the DP Table. **IMPORTANT**
            for j in range(n):
                if i==0 and j==0:              #Already we filled [0,0]th cell
                    continue

                if obstacleGrid[i][j]==-1:     #if there is an obstacle
                    obstacleGrid[i][j]=0

                elif i==0 and j<n:             #filling 1st Row
                    obstacleGrid[i][j]=obstacleGrid[i][j-1]

                elif j==0 and i<m:             #Filling 1st Col
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]

                else:                          #filling all other cell
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]

        return(obstacleGrid[-1][-1])
        
