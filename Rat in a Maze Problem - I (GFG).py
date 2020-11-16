"""
Key : if we use backtracking it is easy to find one solution if we need to find all the solution then
	  go with DFS/recursion technique.
	  **IMPORTANT** **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Rat in a Maze Problem - I
Problem Url    : https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#
Solution Video : https://www.geeksforgeeks.org/rat-in-a-maze-problem-when-movement-in-all-possible-directions-is-allowed/

Learning:
    Brute:  **IMPORTANT**
        final all the path configuration and evaluvate the all. for finding all path confiquration
        it takes exponential time O(2^n) for evaulvating each board it takes O(n^2), so O(n^2 * 2^n)


    Optimal: **IMPORTANT**
        Approach 1 -> By using BackTracking, this approach takes O(2^n) exponential time to complete 
        			 but its 100 times faster than brute force approach. check if we can move in an 
        			 direction if possible move there else back track and check other ways.
        		     **IMPORTANT**

        Approach 2 -> Backtracking is good if we need to find only one combination, if we need to find
        			  all the possible combination then we should need to use recursion/DFS technique.
        			  just take a point check if its valid ,if yes Mark the cell as visited and check if 
        			  its last point if yes append the answer else go and recurese on all 4 direction 
        			  from there.
        			  **IMPORTANT**
"""	



#Optimal Approach 1
def findPath(arr,n):  #Using BackTracking
    totalPath=[]                       #To store all combinations
    def whatI_whatJ(i,j,direction):    #Just an Helper function to know i,j for each direction
        if direction=="U":
            return(i-1,j)
        if direction=="D":
            return(i+1,j)
        if direction=="L":
            return(i,j-1)
        if direction=="R": 
            return(i,j+1)

    def isPath(i,j):                  #Checking if we can move there
        try:
            if arr[i][j]==1:
                return(True)
        except :
			return(False)
        
    def selectPath(i,j):             #Selecting that path
        arr[i][j]=-1
    def deSelectPath(i,j):           #Deselecting that path
        arr[i][j]=1        

    def pathFinder(i,j,curSolution):
        arr[i][j]=-1
        if i==len(arr) and j==len(arr[0]):    #To check if an solution is reached
            totalPath.append(curSolution)
            return(True)
        
        for direction in ["D","L","R","U"]:
            tempI,tempJ=whatI_whatJ(i,j,direction)  #To know what is value of i,j in this direction
            if isPath(tempI,tempJ):
                i,j=tempI,tempJ
                curSolution+=direction
                extendSolution=pathFinder(i,j,curSolution) #Extending the solution
                if extendSolution:
                    return(True)
                curSolution=curSolution[:-2]        #BackTracking
                deSelectPath(i,j)                   #BackTracking
        return(False)

    pathFinder(0,0,"")
    return(totalPath)


#Optimal Approach 2
def findPath(arr, n):  #using Recursion/DFS
    totalSolution=[]
    def isValid(i,j):                       #To check if i,j is valid and we can place rat there
        if i>=0 and j>=0 and i<n and j<n:
            if arr[i][j]==1:
                return(True)
        return(False)
        
    def allPath(i,j,curSolution):           
        if isValid(i,j):                   #check if its an valid i,j position
            arr[i][j]=-1
        else:
            return(False)

        if i==n-1 and j==n-1:              #Check if we have reached an solution
            totalSolution.append(curSolution)
            return(True)
        
        downSolution=curSolution+"D"
        leftSolution=curSolution+"L"
        rightSolution=curSolution+"R"
        upSolution=curSolution+"U"
                                              #Recursing on all 4 direction
        extendDown=allPath(i+1,j,downSolution)#revering the effect of recrsion iff its an valid path
        if extendDown:
            arr[i+1][j]=1
        extendLeft=allPath(i,j-1,leftSolution)
        if extendLeft:
            arr[i][j-1]=1    
        extendRight=allPath(i,j+1,rightSolution)
        if extendRight:
            arr[i][j+1]=1
        extendUp=allPath(i-1,j,upSolution)
        if extendUp:
            arr[i-1][j]=1
        
        return(True)
    
    allPath(0,0,"")
    totalSolution.sort()
    return(totalSolution)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1

        result = findPath(matrix, n[0])
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends