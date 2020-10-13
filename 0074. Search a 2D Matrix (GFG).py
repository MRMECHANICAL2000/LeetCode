"""
Key : using left and down motion inside matrix  **IMPORTANT**
"""
"""
Problem Name   : Search a 2D Matrix
Problem Url    : https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/
Solution Video : https://youtu.be/ZYpYur0znng   **IMPORTANT** Must wath video

Learning:
	Brute: 
		Linear Time search in each row and coloum 

	Better:
		Binary search in each row

	Optimal: **IMPORTANT**
		Approach -> since each row and coloum are sorted. look from 1st row last coloum , move down if
		            the number is smaller, move left if the number is bigger. using down and left move 
		            we can find easily.if either row or coloum exausted element not found. either start
		            from bottom left or top right else you would dind nothing. for matrix sum think from 
		            all 4 cornors.
"""	

class Solution:
	#Optimal
	def matSearch(self,mat, N, M, X):
	    i=0
	    j=M-1
	    while i<N and j>=0: #either moved bottom to last row or moved left to 0th coloum
	       #print(i,j,mat[i][j])
	       if mat[i][j]==X:
	            return(1)
	       elif mat[i][j]>X:
	           j-=1
	       else:
	           i+=1
	    else:
	       return(0)
	        
	        