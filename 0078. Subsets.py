"""
Key : Ditto of combination sum one question. just you need to know the logic. to know the logic go and
	  look the notes in combination sum 2 problem
      **IMPORTANT** **IMPORTANT** 
"""

"""
Problem Name   : Subsets
Problem Url    : https://leetcode.com/problems/subsets/
Solution Video :    
       			 https://leetcode.com/problems/combination-sum-ii/discuss/750378/Python3-DFS-solutionstemplates-to-6-different-classic-backtracking-problems-and-more				 
       			**IMPORTANT** Must Must Must Must look into the link**IMPORTANT**
				 
Learning:
    Brute:  **IMPORTANT**
    	using Recursive DFS Approach.just check all possible combinations. check duplicate using hashtable
    	or using an set **IMPORTANT** **IMPORTANT**

	Better: **IMPORTANT**
		same as DFS but using pro programmer tricks to skip duplicates
		**IMPORTANT** **IMPORTANT**

    Optimal: **IMPORTANT**
        Approach -> by using iterative approach **IMPORTANT** **IMPORTANT**
					look the code to understand very vey simple
        			
"""	

class Solution:
	# Better Approach - BackTracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution=[]
        nums.sort()
        def dfs(curSet,idx):
            solution.append(curSet)
            for i in range(idx,len(nums)):
                #if i>idx and nums[i]==nums[i-1]: #To generate only unique subsets alone
                #    continue
                dfs(curSet+[nums[i]],i+1)
            
        dfs([],0)
        return(solution)

    #Optimal Approach -  Iterative
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = [[]]
        nums.sort()
        for num in nums: 
            res += [ i + [num] for i in res]
        return res




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