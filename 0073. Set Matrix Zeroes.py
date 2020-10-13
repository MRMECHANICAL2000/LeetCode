"""
Key : Use same matrix to store where zero comes
"""
"""
Problem Name   : Set Matrix Zeros
Problem Url    : https://leetcode.com/problems/set-matrix-zeroes/
Solution Video : https://youtu.be/M65xBewcqcI

Learning:
	Brute: 
		for each element make entire row and coloum zero

	Better:
		if an element is zero store its row and coloum index in seperate array and finally make matrix zero

	Optimal: **IMPORTANT**
		Approach -> using matrix 1st row and coloum to store which row to make zero.here to be noted 
					that while making like this index[0][0] will either be made zero because of row or 
					coloum containing zero , so use an variable to store if coloum made index[0][0] as 0 
					or row made it. after storing data
"""	
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col= False
        R= len(matrix)   		#Row Length
        C= len(matrix[0])		#Coloum Length

        for i in range(R):			#To check and store in which index zero exists
            if matrix[i][0]== 0:	#**IMPORTANT** to check if any element in Coloum 1 is zero 
                is_col= True

            for j in range(1,C):  #***IMPORTANT* Row full , coloum from 2nd coloum so if [0,0]=0 its 
                                  #because of the 1st row only
                if matrix[i][j]==0:
                    matrix[i][0]= 0
                    matrix[0][j]= 0
        
        for i in range(1,R):
            for j in range(1,C):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        
        #1st Row to zero        
        if matrix[0][0]==0:     #**IMPORTANT** if [0,0]=0 its because of row only  
            for j in range(C):
                matrix[0][j]=0

        #1st coloum to zero
        if is_col:              #if is_col is True atleast one element is col1 is zero
            for i in range(R):
                matrix[i][0]=0
                