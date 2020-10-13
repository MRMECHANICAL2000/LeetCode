"""
Key : Using Combination formula in math , nCr= n!/((n-r)!*r!) **IMPORTANT**
"""
"""
Problem Name   : Pascal Triangle
Problem Url    : https://leetcode.com/problems/pascals-triangle/
Solution Video : https://youtu.be/6FLvhQjZqvM   **IMPORTANT** Must wath video

Learning:
	Brute: 
		create Entire Pascal Triangle

	Optimal: **IMPORTANT**
		Approach -> Using Combination and Shortcut of combinatino to create it. (r-1) C (c-1)
"""	

class Solution:
	#Brute
    def generate(self, numRows: int) -> List[List[int]]:
        PascalTriangle=[[1],[1,1]]                  #Always 1st and last coloum are 1
        if numRows==0:
            return([])
        elif numRows==1 or numRows<0:
            return([PascalTriangle[0]])
        elif numRows==2:
            return(PascalTriangle)
        
        for i in range(3,numRows+1):
            newRow=[1 for _ in range(i)] #**IMPORTANT** Make all coloum as 1 
     
            for j in range(1,i-1): #**IMPORTANT** except 1st and last coloum change other value
                newRow[j]=PascalTriangle[i-2][j-1]+PascalTriangle[i-2][j]
       
            PascalTriangle.append(newRow)

        return(PascalTriangle)