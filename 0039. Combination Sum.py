"""
Key : in recursion while appending final solution make sure to append with [:] else it become pointer
	  to that solution and changes made will reflect there as well.
      watch the video to know the intution on how to approach the problem
      **IMPORTANT** **IMPORTANT** 
"""

"""
Problem Name   : Combination Sum
Problem Url    : https://leetcode.com/problems/combination-sum/
Solution Video : https://youtu.be/yFfv03AE_vA  #Back Tracking Approach
				 **IMPORTANT**   
				 https://youtu.be/AUIfTelAGVc  #DP Approach
				 **IMPORTANT** Must Must Must Must Must watch DP approach**IMPORTANT** 
				 
Learning:
    Brute:  **IMPORTANT**
    	using Recursive DFS Approach.just check all possible combinations.

	Better: **IMPORTANT**
		using same Recursive DFS Approach just memoise and catch some solutions in between.
		The same approach of us can be even optimized further look into the below link **IMPORTANT**
		https://leetcode.com/problems/combination-sum/discuss/16554/Share-My-Python-Solution-beating-98.17
		**IMPORTANT** **IMPORTANT**

		The solution i have written is very poor plese look the below link to get good solution and 
		real intution behind the backTracking problem 
		**IMPORTANT** Must Must Must Must Must See **IMPORTANT**
		https://leetcode.com/problems/combination-sum-ii/discuss/750378/Python3-DFS-solutionstemplates-to-6-different-classic-backtracking-problems-and-more

    Optimal: **IMPORTANT**
        Approach -> using Bottom up approach in the DP table. must watch the video to get intution.
        			**IMPORTANT** **IMPORTANT**

"""	

class Solution:
	# Better Approach - BackTracking
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solution=[]  #Final solution
        HashTable={} #For Memoization
        def allCombo(curCandList,curSum,addCand):
            if addCand!=0:                                #to Make sure we are not comming 1st time
                if curSum+addCand==target:                #If target achieved we check if its in Table
                    temp=curCandList[:]
                    temp.append(addCand)
                    temp.sort()                         #list cant be appended so we convert it into tuple
                    temp=tuple(temp)                    #to keep order fine we sort it **IMPORTANT**
                    try:
                        HashTable[temp]
                    except:
                        curCandList.append(addCand)     #if new cand list found append it to the table
                        solution.append(curCandList[:]) #Make sure to append with[:] else it becomes an 
                        HashTable[temp]=1               #pointer to existing part **IMPORTANT**
                        return(True)

                if curSum+addCand>target:
                    return(False)                #if val>target kill it with the bounding conditions 

                curCandList.append(addCand)      #if val<target add that cand and recurse with other possiblity
                curSum+=addCand

            for i in candidates:                            #Recursion Step
                allCombo(curCandList[:],curSum,i)

        allCombo([],0,0)
        return(solution)

