"""   
Key : Greedy Approach fails when? learn that , watch video to know subprolem solving using DP.memorist the
	  to check if change cant be made. and know how to use "infinity" in python. Always never assume the
	  given input will be sorted. if you need the input to be sorted you sort it your self or ask the interviewer
	  to conform the input will be sorted. dont assueme youself that input is sorted based on sample input.
	  **IMPORTANT** **IMPORTANT**

"""

"""
Problem Name   : Coin Change
Problem Url    : https://leetcode.com/problems/coin-change/
Solution Video : https://youtu.be/jgiZlGzXMBw  **IMPORTANT** Must Must Watch to know the subProblems


Learning:
	Brute:
		use two loop and check each pair[i:j] weather they can be used  as change
		
	Better: **IMPORTANT**
		using an GREEDY selection criteria. sort the coin in decending order make max change with each 
		coin as possible. but this method works when change is indian coin like {1,2,5,10,20,50,100} not 
		when you have change as random numbers like {3,6,9,19...}


	Optimal: **IMOPRTANT**
		Approach 1-> Using DYNAMIC PROGRAMMING, Must watch video to know subProblems. understand the probelm
					 dont memorise table. for i from 0,1,2,3 to N amount for each subproblem we find the minimum
					 no of change use them to find big subproblem. At each place check if i-Coin>=0 means              
                     on that table position DP[i]=min(DP[i],1+DP[i-Coin]) take min of curVal of 1+prev computed 
                     subproblem value. **IMPORTANT** look code and memorise the short to check if change
                     cant be made.

        Approach 2-> using BFS, Since it is to find the least coin solution (like a shortest path 
        			 from 0 to amount)using BFS gives results much faster than DP
        			 https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution
        			 #I have not implement it yet# look  this link to know how
"""	

class Solution:

	#Better Solution- Greedy
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()   #Dont assume input is sorted **IMPORTANT**
        count=0
        for i in coins[::-1]:
            if i<=amount:
                count+=amount//i
                amount=amount%i
            if amount==0:
                break            
        else:
            return(-1)
        return(count)
 

	#Optimal Approach 1 -DP
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()  #Dont assume given input will be sorted always **IMPORTANT**
        DP=[0]+[float('inf') for i in range(amount)]
        for i,Amt in enumerate(DP): #Amt is no of change i only amount dont confuse
            for j,Coin in enumerate(coins):
                
                if i-Coin>=0:              
                    DP[i]=min(DP[i],1+DP[i-Coin])  #Heat of the Table **IMPORTANT**
                else:
                    break
        #print(DP)
        return(DP[-1] if DP[-1]!='inf' else -1) #**IMPORTANT** edge case dont think like fools and do
        										#lot of unwanted code to know wheather change can be made
        										#check if last elment= 'inf' if yes then change cant be made
        										#print the table to know why **IMPORTANT**