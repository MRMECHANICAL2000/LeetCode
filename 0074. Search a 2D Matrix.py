"""
Key : finding row,col index using //,% operator (doing binary search in Matrix)  **IMPORTANT**
"""
"""
Problem Name   : Search a 2D Matrix
Problem Url    : https://leetcode.com/problems/search-a-2d-matrix/
Solution Video : https://youtu.be/ZYpYur0znng   **IMPORTANT** Must wath video

Learning:
	Brute: 
		Linear Time search in each row and coloum 

	Optimal: **IMPORTANT**
		Approach -> since the matrix looks like sorted array split into multiple sub array and kept
		            at each row. if it is an single array we can use binary search. since its like 
		            row in matrix to do binary search we need its row,col value , that we find using
		            row_index=mid//row_length and col_index=mid%row_length. think twise you can 
		            understand it . **IMPORTANT**
"""	

class Solution:
	#Optimal
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix)==0:     #Don't forget this corner case in interview **IMPORTANT**
            return(False)      #can the input be an empty array

        r = len(matrix)
        c = len(matrix[0])

        #Binary search in Matrix
        
        left = 0
        right = r*c-1
        mid = left + (right - left)//2

        while left <= right:

            mid = left + (right - left)//2  #Dont forget this formula. **IMPORTANT**

            r_index = mid//c
            c_index = mid%c

            if matrix[r_index][c_index] == target:
                return(True)
            
            elif matrix[r_index][c_index] < target: #dont put left in right place and right in left place?
                left = mid+1
                
            else:
                right = mid-1
                
        else:
            return(False)
                
