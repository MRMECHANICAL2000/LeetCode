"""
Key : Just the validation part of the sudako solver question **IMPORTANT** **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Valid Sudoku
Problem Url    : https://leetcode.com/problems/valid-sudoku/
Solution Video : https://youtu.be/tvP_FZ-D9Ng
				 **IMPORTANT** must must Watch **IMPORTANT**  

Learning:
    Brute:  **IMPORTANT**
        Validate the entire board for each cell value.


    Optimal: **IMPORTANT**
        Approach -> Validate one row , one coloum and one 3*3 grid alone for each cell.
        		    **IMPORTANT**

"""	

class Solution:
    #Optimal Approach
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        def validChecker():
            for i in range(len(board)):
                for j in range(len(board[0])):                    
                    if board[i][j]!=".":
                        value=board[i][j]
                        board[i][j]="."            #since we are check for that cell value make that cell "."
                        isValid=validate(i,j,value)#Then only we can validate row,col and grid. 
                        board[i][j]=value
                        if isValid==False:
                            return(False)
            return(True)
        
        def validate(i,j,value):
            curRow=board[i]
            if value in curRow:
                return(False)
            
            curCol=[board[x][j] for x in range(len(board))]
            if value in curCol:
                return(False)
            
            rowGrid=(i//3)*3 #To find the starting of that box
            colGrid=(j//3)*3
            for a in range(rowGrid,rowGrid+3):
                for b in range(colGrid,colGrid+3):
                    if value==board[a][b]:
                        return(False)
            return(True)
        
        return(validChecker())
