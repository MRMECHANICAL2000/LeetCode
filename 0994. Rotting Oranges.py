"""   
Key : look all important points in code. solutino easy but you made lot mistake in implementation. 

"""

"""
Problem Name   : Rotting Oranges
Problem Url    : https://leetcode.com/problems/rotting-oranges/
Solution Video : https://youtu.be/CxrnOTUlNJE
                 

Learning:
	Brute:


		
	Better:


	Optimal: 
		Approach -> Using BFS, 1st save rotten oranges index. then from that do BFS and save newlely
					rotten oranges index.continue until all oranges get rotten or no more neighbours
					to rotten. 	
"""	

from collections import deque #for implementing queue we import it
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def bfs(x,y):
            global freshOrangeCount  # must define this variable as global out side function and inside 
            						 #the function where we use also use this. you may ask for list and 
            						 #all we are not declaring it as global but still we use it in and 
            						 #outside function because tuple,int,string are immutable so they are
            						 #created newely each time in each function. so we need to say dont 
            						 #create newly in current function use previously created variable
            						 #which is declared as global. for mutable object like list, the name
            						 #we give is an reference so we can use it in any place. **IMPORTANT**
            
            grid[x][y]=-1            #Making surrent index rotten
            newelyRottenIdx=[]
            direction=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)] #Good coder trick **IMPORTANT**

            #Good coder used one code inside loop and given direction as input            
            for dx,dy in direction:
	            if  0<=dx<row and 0<=dy<col and grid[dx][dy]==1: #**IMPORTANT** look condition**IMPORTANT**
	                grid[dx][dy]=-1                 #Rotting neibour index
	                newelyRottenIdx.append((dx,dy)) #appending it to rotten list
	                freshOrangeCount-=1             #reducing the fresh orange count

            """
            #My code using 4 times same code to calculate 4 direction, if we do like this we will get 
            #lot of duplicate insersion as well in our code
            #for UP
            if up!=None and grid[up[0]][up[1]]==1:
                grid[up[0]][up[1]]=-1
                newelyRottenIdx.append(up)
                freshOrangeCount-=1
            #for Down
            if down!=None and grid[down[0]][down[1]]==1:
                grid[down[0]][down[1]]=-1
                newelyRottenIdx.append(down)
                freshOrangeCount-=1

            #for Left
            if left!=None and grid[left[0]][left[1]]==1:
                grid[left[0]][left[1]]=-1
                newelyRottenIdx.append(left)                
                freshOrangeCount-=1

            #for Right
            if right!=None and grid[right[0]][right[1]]==1:
                grid[right[0]][right[1]]=-1
                newelyRottenIdx.append(right)                
                freshOrangeCount-=1
            """
            return(newelyRottenIdx)


        row=len(grid)
        col=len(grid[0])

        rottenIdx=deque()
        global freshOrangeCount # must define this variable as global out side function and 
        						#inside the function **IMPORTANT**
        freshOrangeCount=0

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:           #Storing rotten index
                    rottenIdx.append((i,j))                     
                elif grid[i][j]==1:
                    freshOrangeCount+=1

        timeElapsed=0
        while freshOrangeCount: #Break when all freash oranges were rotten
            queue=deque()

            while rottenIdx:
                i,j=rottenIdx.popleft() #Rotting Neighbours and storing in queue
                [queue.append(i) for i in bfs(i,j)]
                
            rottenIdx=queue
            timeElapsed+=1

            if not rottenIdx: #Break if no more oranges to look around
                break

        if freshOrangeCount==0: #if all oranges rotten return time else return -1
            return(timeElapsed)
        return(-1)