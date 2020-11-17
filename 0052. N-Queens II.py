"""
Key : Everything is same as N-Queens problem just output the no of solution instead of outputting the
	  solution itself.only small change in last few lines of code. **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : N Queens
Problem Url    : https://leetcode.com/problems/n-queens/
Solution Video : https://youtu.be/kdBzkxdJ7bI -->NPTEL Lecture Video
				 **IMPORTANT** must must see our nptel class notes **IMPORTANT**  

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
    #Optimal Approach 1

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==0:
            return([[]])   #Edge Case **IMPORTAN**

        def initilize(n):
            for i in ['Queen','row','col','NWtoSE','SWtoNE']:
                board[i]=[]

            for i in range(n):
                board['Queen'].append(-1)
                board['row'].append(0)
                board['col'].append(0)

            for i in range(-(n-1),n):    #limit **IMPORTANT**
                board['NWtoSE'].append(0)
                
            for i in range(2*(n-1)+1):   #limit **IMPORTANT**
                board['SWtoNE'].append(0)
            
        def free(i,j):   #To check if a positon is free to place queen
            return(board['row'][i]==0 and board['col'][j]==0 and board['NWtoSE'][j-i]==0  and board['SWtoNE'][j+i]==0)
        
        def addQueen(i,j):         #To add an queen in positon (i,j)
            board['Queen'][i]=j
            board['row'][i]=1
            board['col'][j]=1
            board['NWtoSE'][j-i]=1
            board['SWtoNE'][j+i]=1
            
        def removeQueen(i,j):       #To remove the queen in positon (i,j)
            board['Queen'][i]=-1
            board['row'][i]=0
            board['col'][j]=0       #**IMPORTANT**
            board['NWtoSE'][j-i]=0  #Dont forget to use j-i , j+1 else board['___'] becomes int '0'
            board['SWtoNE'][j+i]=0  #ie, board['___']=0 not put like that must put board['___'][j-i]=0
            
        def placeQueen(i):
            n=len(board['Queen'])
            for j in range(n):
                if free(i,j):

                    addQueen(i,j)
                    if i==n-1:
                        Result.append(board['Queen'][:])  
                        #the appended value become pointer to original list so make sure while appending 
                        #list object we create new list and append  **IMPORTANT** **IMPORTANT** **IMPORTANT**
                         
                    else:
                        extendBoard=placeQueen(i+1)
                    removeQueen(i,j) #Add queen in one place continue then remove from that position then continue
                    				 #so that we can search through all the possible work place

                                
        global board         #Board and solution saving globally **IMPORTANT**
        global Result
        Result=[]
        board={}
        initilize(n)
        placeQueen(0)
        return(len(Result))  #Small change in N Queen code at this position alone **IMPORTANT**
