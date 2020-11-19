"""
Key : slight variation of previous combination sum 1 question and a lot of things to be learned form this
	  qusetion. look the code. and additional notes below the code.
      **IMPORTANT** **IMPORTANT** 
"""

"""
Problem Name   : Combination Sum II
Problem Url    : https://leetcode.com/problems/combination-sum-ii/
Solution Video : https://youtu.be/PFkUl_rW3_w  #Back Tracking Approach
				 **IMPORTANT**   
       			https://leetcode.com/problems/combination-sum-ii/discuss/16870/DP-solution-in-Python				 
       			**IMPORTANT** Must Must Must Must look into the link**IMPORTANT**
				 
Learning:
    Brute:  **IMPORTANT**
    	using Recursive DFS Approach.just check all possible combinations.

	Better: **IMPORTANT**
		using same Recursive DFS Approach just memoise and catch some solutions in between.
		The same approach of us can be even optimized further look into the below link **IMPORTANT**
		https://leetcode.com/problems/combination-sum/discuss/16554/Share-My-Python-Solution-beating-98.17
		**IMPORTANT** **IMPORTANT**

    Optimal: **IMPORTANT**
        Approach -> using Bottom up approach in the DP table. 
        			this problem is a variant of the knapsack problem. If you can understand the solution
        			to Coin Change or Coin Change 2, then you can easily understand this solution. 
        			One caveat here is..... Look the link to get the caviate
        			https://leetcode.com/problems/combination-sum-ii/discuss/16870/DP-solution-in-Python
        			**IMPORTANT** Must Must Must Must Must look the link**IMPORTANT**

"""	

class Solution:
	# Better Approach - BackTracking
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:    
        candidates.sort()
        #solution=set()
        solution=[]					#**IMPORTANT**
        def dfs(x,candList,curSum): #We can recurse by having curSum(adding ele by ele) or curTarget(sub
        							#ele by ele) like shown in video but curSum is clear and easy to implement
            if curSum==target:
            	"""
                candList.sort()
                solution.add(tuple(candList[:]))  #We can use set to keep track of duplicates or use
                """  							  #an HashTable to keep track like previous question
                								  #or we can use below approach like an pro coder
                								  #instead of tracking duplicate we can just skip the
                								  #code from where duplicate can start occuring
                								  #**IMPORTANT** **IMPORTANT**
                solution.append(candList)
                return(True)
            
            if curSum>target:
                return(False)
            
            for i in range(x,len(candidates)):
                if i > x and candidates[i] == candidates[i-1]:
                    continue 					#To get ride of duplicates either this method or 
                    							#use set and keep track of entries **IMPORTANT** **IMPORTANT**
                dfs(i+1,candList+[candidates[i]],curSum+candidates[i])
                								#Hey look carefully i+1 put not x+1, another thing is no 
                								#need to call two dfs with curCand and without curCand 
                								#because in this for loop each attempt we are adding new 
                								#cand and prev can is not in consideration think twise to 
                								#understand  **IMPORTANT** **IMPORTANT**
        dfs(0,[],0)
        #print(solution)
        return(solution)

#**IMPORTANT** **IMPORTANT**
#We spend 6 hours and write an DP solution for this question and read the result below
#Worst ever DP solutoin do not try this, always if you go for Dp try it if you need only one solution ,
#if all solution need try recursion/backtracking. if there were duplicates in question then also dont 
#try DP.if there were -ve element in question then do not try DP. we can do DP solution by doing some
#optimizatino for all of theses cases but you know you need to be a pro in it or try some simple solution


#Additional Notes
    
    #code to find all unique subset/combination
    for i in range(idx, len(candidates)):
        if i > idx and candidates[i] == candidates[i-1]:
            continue
        dfs(i+1, path+[candidates[i]], cur+candidates[i])

    #Code to find all subset/combination
    for i in range(idx, len(candidates)):
        dfs(i+1, path+[candidates[i]], cur+candidates[i])

    #Code to find all subject with each character infinite no of times
    for i in range(idx, len(candidates)):
        dfs(i, path+[candidates[i]], cur+candidates[i])