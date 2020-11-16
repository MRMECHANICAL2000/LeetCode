"""
Key : here each time we find  a free spot and then we check if any no from 1 to 9 can be placed in there
	  if it cant be placed we backtrack and change the last inserted value and repeat if even backtracking
	  to all value still cant fix a value means we return False since board cant be solved. else if the board
	  can be solved means we reach the i,j=None,None in the nextFree() function. Must watch the video and look 
	  the code ones to know the proper working
	  Must see the Validation part its easy to validate the row, but need to think differently to
	  validate both coloum and box. for box dont think some stupid stuff just find starting point of grid
	  add 3 to it and validate. **IMPORTANT** **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Sudoku Solver
Problem Url    : https://leetcode.com/problems/sudoku-solver/
Solution Video : https://youtu.be/tvP_FZ-D9Ng
				 **IMPORTANT** must must Watch **IMPORTANT**  

Learning:
    Brute:  **IMPORTANT**
        final all the board configuration and evaluvate the all. for finding all board it takes O(2^n) 
        for evaulvating each board it takes O(n^2), so O(n^2 * 2^n)


    Optimal: **IMPORTANT**
        Approach -> By using BackTracking, it is an NP Complete problem. this approach takes O(2^n)
        		    exponential time to complete but its 100 times faster than brute force approach
        		    **IMPORTANT**

"""	


class Solution:
    #Optimal Approach

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        def nextFree():                          #To find next location which is free on board 
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==".":
                        return(i,j)
            return(None,None)
        
        def validate(i,j,value):                 #To check if this value can be place in (i,j)
            curRow=board[i]                      #To check if curRow has this value
            if value in curRow:                  
                return(False)
            												 #**IMPORTANT**
            curCol=[board[x][j] for x in range(len(board))]  #To check if curCol has this value
            if value in curCol:
                return(False)                    #**IMPORTANT**
                                                 #To check if 3*3 grid has this value
            rowGrid=(i//3)*3                     #To find the starting of that box
            colGrid=(j//3)*3
            for a in range(rowGrid,rowGrid+3):   #since grid is always 3*3 size, from starting point add 3
                for b in range(colGrid,colGrid+3):
                    if value==board[a][b]:
                        return(False)

            return(True)  #if not returned in any of above then its an valid placement
        
        def solver():
            i,j=nextFree()                #Find the free box
            if i==None or j==None: #If None returned means we have reached the end of board **IMPORTANT**
                return(True)

            for x in range(1,10):         #Not 0 to 9 **IMPORTANT**
                if validate(i,j,str(x)):  #Check if value can be place in the free box (i,j)
                    board[i][j]=str(x)    #Placing the value
                    extendSol=solver()    #Extending the solution
                    if extendSol:
                        return(True)
                    board[i][j]="."       #Removing the value(backtracking) and find next possible value
            return(False)

        solver() #Define board as global variable so we dont need to pass it in all the function

            
        