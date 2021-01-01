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

    Better:
        append 0 before and after prev row and add them you will get current row value
            1 3 3 1 0  -> Append 0 at back of row 4 
         +  0 1 3 3 1  -> Append 0 at front of row 4
         =  1 4 6 4 1  -> row 5 is got

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

    #Better Approach
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<0:
            return([[1]])
        Result=[]
        prev=[1]
        for i in range(numRows):
            cur=[0]+prev                #padding zero at front
            for i in range(len(cur)-1): #padding zero at back or loop until n-1 element **IMPORTANT**
                cur[i]=cur[i]+prev[i]
            Result.append(prev)
            prev=cur
        return(Result)
        
        
    #Optimal Approach
    def generate(self, numRows: int) -> List[List[int]]:

        """
        #If you find combination like this you will end up wiht integer overflow error even for 
        #small input value like 25. **IMPORTANT**
        def fact(val):
            fact=1
            for i in range(1,val+1):
                fact*=i
            return(fact)
        
        def nCr(n,r):
            return(ceil(fact(n)/(fact(r)*fact(n-r))))
        """

        def Optimal__nCr(n,r): #Finding nCr Optimally   **IMPORTANT**
                               #nCr=  (n to n-r)/(1 to r) 
                               #ie. (from n to 1 ,r term at top)/ (1 to r, r term at bottom)
            top=1
            bottom=1
            for i in range(n,n-r,-1):
                top*=i
            for i in range(1,r+1):
                bottom*=i            
            return(top//bottom)

        Result=[]
        if numRows<0:
            return([[1]])
        for i in range(1,numRows+1):
            temp=[]
            for j in range(1,i+1):
                found=Optimal__nCr(i-1,j-1)  #finding each element value by optimaly calculating nCr
                temp.append(found)
                
            Result.append(temp) 
        return(Result)
