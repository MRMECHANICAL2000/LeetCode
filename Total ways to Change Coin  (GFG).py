"""   
Key : 1 ways to make change if sum is 0 and 0 ways to make change if coin is 0 no matter what the 
	  sum is. this is the key to fill 0th row and 0th coloum. understand it clearely
	  **IMPORTANT** Very Very important **IMPORTANT**
	  look table here to know how we filled 1 simply on row 0 while building itself.

"""

"""
Problem Name   : No fo ways to Coin Change
Problem Url    : https://practice.geeksforgeeks.org/problems/coin-change2448/1#
Solution Video : https://youtu.be/L27_JpN6Z1Q  **IMPORTANT** Must Must Watch to know the subProblems


Learning:
	Brute:
		Takes Exponential time. we can use for loop find all pair and check if it is valid or not

	Optimal: **IMOPRTANT**
		Approach -> Using DP we can solve this problem in O(N^2) time with O(N^2) Space complexity. must
					watch video to know the subproblem. try understanding it.
					if coin > val , then put value on cell above
					else val on cell above + val-coin the cell to right.
					see video to know why


"""	

class Solution:
	#Optimal Approach  -DP
    def count(self, S, m, n): 
        Table=[[1]+[0 for i in range(n) ]for j in range(m+1)]  #DP table ***IMPORTANT* filling [1] simply on col 0 
        S=[0]+S

        for i in range(1,m+1):
            for j in range(1,n+1):
                if S[i]>j:                       #Subproblems
                    Table[i][j]=Table[i-1][j]
                else:
                    Table[i][j]=Table[i][j-S[i]]+Table[i-1][j]

        return(Table[-1][-1])

#{ 
#  Driver Code Starts

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends
