"""
Key : look question careffully we cant use DP here because they are asking us to count only the path that
      walks over all non obstacles, ie, if you find a path the use only 3 movable square but in question
      there are 6 movable square then the solution you found is not considered. only the solution that 
      pass through all 6 movable square is considered.
      **IMPORTANT** 
      
      Zoho Anna Idea: for previous questoin we can reach a box from only two direction either top to
      down or left to right. so we added values from (i-1,j) and (i,j-1). but for this question it
      is given that we can reach a box from all 4 direction. so we add values from all the side.
      (i-1,j) , (i,j-1) , (i+1,j) , (i,j+1). but we cant applay this approach to this question
      because its said we can reach a box only ones also start is not at (0,0) so just remember
      we can do like this.
"""

"""
Problem Name   : Unique Paths III
Problem Url    : https://leetcode.com/problems/unique-paths-iii/
Solution Video : https://youtu.be/XNKCkX_tHhM
                 #IMPORTANT** Just see last 3 minutes of video to see code walk through really easy

Learning:
	Brute: 

	Optimal: **IMPORTANT**
		Approach -> Using DFS and BackTracking , if you know how to implement DFS and BackTracking its 
                    an really easy question to solve. BackTracking is nothing just adding 2 lines in DFS

"""	


class Solution:
    #Better Approach
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        #Recursive DFS Function
        def UniquepathDFS(i,j,zeroCount):
            if i<0 or j<0 or i>=rowLen or j>=colLen: #Boundary Condition
                return(0)
            if grid[i][j]=="Visited":        #To check if the cell is already visited
                return(0)
            if grid[i][j]==-1:               #to check if its obstacle
                return(0)
            if grid[i][j]==2:
                if zeroCount==-1: #**IMPORTANT** because at position 2 also we subtracted one zero 
                    return(1)     #from total,so -1 will be there. Thik twise. **IMPORTANT**
                return(0)
            
            grid[i][j]="Visited" #Making current cell visted and reducing no of zeros for DFS **IMPORTANT**
            zeroCount-=1

            #Movement in all the 4 direction is possible
            totalPath=UniquepathDFS(i+1,j  ,zeroCount) #Moving Up,Down,Left,Right 
            + UniquepathDFS(i  , j+1, zeroCount) 
            + UniquepathDFS(i-1,j  ,zeroCount)
            + UniquepathDFS(i  ,j-1,zeroCount)

            grid[i][j]=0     #BackTracking Step, Making current cell unvisted and uncounted **IMPORTANT**
            zeroCount+=1

            return(totalPath)
            

        zeroCount=0
        startIdx=None
        endIdx=None
        rowLen=len(grid)
        colLen=len(grid[0])

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j]==0:
                    zeroCount+=1     #Counting Zero
                elif grid[i][j]==1:
                    startIdx=[i,j]   #finding Start
                elif grid[i][j]==2:
                    endIdx=[i,j]     #finding End

        return(UniquepathDFS(startIdx[0],startIdx[1],zeroCount)) #DFS Outermost function call
