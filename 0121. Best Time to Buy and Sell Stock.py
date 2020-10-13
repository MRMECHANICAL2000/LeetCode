"""
Key : Loop from front to back, store overall minStock price and overll maxProfit
"""
"""
Problem Name   : Best Time to Buy and Sell Stock
Problem Url    : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Solution Video : https://youtu.be/eMSfBgbiEjk

Learning:
	Brute: 
		Using 2 Loop Method

	Optimal: **IMPORTANT**
		Approach -> loop from index 0 to n-1 , store minVal overall, at each index find 
					current index value - minVal. store that val in overall maxVal if it is bigger
					than previous overall maxVal. 
"""	

class Solution:
	#Optimal
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=0:
            return(0)
        small=prices[0]  #Overall Small
        profit=0		 #Overall profit

        for i in prices:
            if i<small:
                small=i

            if i-small>profit:
                profit=i-small
        return(profit)
        