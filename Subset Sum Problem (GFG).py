"""
Key : This is similair to subset sum problem,instead of finding subset that accounts to an sum here we 
	  find an subset which equal to half of totalArr sum. look the code to know all the mistakes you made
	  and watch the video to get the intution
      **IMPORTANT** **IMPORTANT** 
"""

"""
Problem Name   : Partition Equal Subset Sum
Problem Url    : https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1
Solution Video : https://www.youtube.com/watch?v=kyLxTdsT8ws   #BackTracking solution
				 https://www.youtube.com/watch?v=obhWqDfzwQQ   #Watch to know why cant partition if totalSum==Odd 
				 https://www.youtube.com/watch?v=34l1kTIQCIA   #Watch to how recursive and DP intution
       			**IMPORTANT**
				 
Learning:
    Brute:  **IMPORTANT**
    	Recurse and find all subset using pro programmer trick or ordinarely. at each subset check
    	if its satisfy the condition. Leads to TLE.
    	we may use Memoization to reduct repeated computation but not implemented in my code below.
    	To know why BackTracking is not efficient look the time complexity in below link
    	https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
    	**IMPORTANT** Must Must see **IMPORTANT**


	Better: **IMPORTANT**
		using DP, it is similair to 0/1 Knapsack problem.Takes more Space O(n*w)
		this is same as subset sum probem but we just need to find subset sum=totalSum//2. we solve the
		subset sum problem by using method of 0/1 knapsack problem

		**IMPORTANT** **IMPORTANT**

    Optimal: **IMPORTANT**
        Approach -> DP with space optimization. we can do 0/1 knapsack problem with O(w) space alone.
					https://leetcode.com/problems/partition-equal-subset-sum/discuss/276278/Python-DP-and-(DFS%2BMemo)
			        **IMPORTANT** Link to know more about the space optimization **IMPORTANT**
					
        			
"""	

class Solution:
	# Brute Approach - Recursion without Memoization
    def canPartition(self, arr: List[int]) -> bool:
        subset=[]
        arr.sort()
        totalSum=sum(arr)
        				 #**IMPORTANT**
        if totalSum%2!=0:#Edge case if not implemented then Time Limit exeed error comes
            return(False)#total sum should be even then only we can divide it into two subset such that 
            			 #sum of element in each set same. if odd means we cant divide it into equal subset
            
        def dfs(curSet,curSum,idx):
            if 2*curSum==totalSum:
                return(True)
            if 2*curSum>totalSum:
                return(False)
            for i in range(idx,len(arr)):
                if i>idx and arr[i]==arr[i-1]: #Skipping duplicate to save on time  **IMPORTANT**
                    continue      #Even if we skip duplicate without memoization we will lead to TLE only
                    			  #so try DFS+Memoization **IMPORTANT**

                result=dfs(curSet+[arr[i]],curSum+arr[i],i+1)#**IMPORTANT**
                if result==True: #Make sure the program executes even after the 1st branch of tree returns
                				 #false it should contunie until all other branch were reached. 
                				 #finally if no True returned then alone we should need to return False
                    return(True)
            return(False)
        return(dfs([],0,0))

    #Better Approach - 2D DP array Method 
    def canPartition(self, arr: List[int]) -> bool:
        totalSum=sum(arr)
        #arr.sort() #No need to sort even if we dont sort also it will work  **IMPORTANT**
        if totalSum%2!=0:
            return(False)

        DP=[[True]+[False for i in range(totalSum//2)] for i in range(len(arr)+1)]       
        for i in range(1,len(arr)+1):
            for j in range(1,(totalSum//2)+1):
                """
                if arr[i-1]<=j:                  #This code outputs error because here we are checking
                    DP[i][j]=DP[i-1][j-arr[i-1]] #both the conditions seperately either. Actually
                else: 							 #we should need to put True if either of them is True
                    DP[i][j]=DP[i-1][j]
                """                            #**IMPORTANT** **IMPORTANT** **IMPORTANT**
                DP[i][j] = DP[i-1][j] or (arr[i-1]<=j and DP[i-1][j-arr[i-1]])
                			#if either of the condition is True assign True

        return(DP[-1][-1])