"""
Key : Using Combination formula in math , nCr= n!/((n-r)!*r!) **IMPORTANT**
      same as pascal triangle I just need to output only last row
"""
"""
Problem Name   : Pascal Triangle II
Problem Url    : https://leetcode.com/problems/pascals-triangle-ii/
Solution Video : https://youtu.be/6FLvhQjZqvM  

Learning:
	Brute: 
		create Entire Pascal Triangle

    Better:
        append 0 before and after prev row and add them you will get current row value
            1 3 3 1 0  -> Append 0 at back of row 4 
         +  0 1 3 3 1  -> Append 0 at front of row 4
         =  1 4 6 4 1  -> row 5 is got

	Optimal: **IMPORTANT**
		Approach -> Using Combination and Shortcut of combinatino to create it. (r-1) C (c-1)
"""	

class Solution:
    #Brute Force Method
    def getRow(self, rowIndex: int) -> List[int]:
        numRows=rowIndex+1
        PascalTriangle=[[1],[1,1]]
        if numRows==0:
            return([])
        elif numRows==1 or numRows<0:
            return([1])
        elif numRows==2:
            return([1,1])
        
        for i in range(3,numRows+1):
            newRow=[1 for _ in range(i)]        
            for j in range(1,i-1):
                newRow[j]=PascalTriangle[i-2][j-1]+PascalTriangle[i-2][j]
            
            PascalTriangle.append(newRow)
        return(PascalTriangle[rowIndex])
        
    #Better Approach
    def getRow(self, rowIndex: int) -> List[int]:
        prev=[1]
        for i in range(rowIndex):           
            cur=[0]+prev
            for i in range(len(cur)-1):
                cur[i]=cur[i]+prev[i]
            prev=cur
        return(prev)