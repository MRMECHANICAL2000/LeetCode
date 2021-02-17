"""   
Key : this is an really really simple greedy question but you did not even had an intution that
	  you can solve it. your intution are all wrong. you taught of finding min element in array
	  give 1 chocolate to him, then expand your solution from there left and right.but this 
	  appraoch has lot of tough to handle situvation.

	  in question itself they said you need to compare only left,right side ie,neighbour then
	  suddenly 1st thing that should need to come to your mind is 2 pass approach.
	  **IMPORTANT** **IMPORTANT** **IMPORTANT**
"""
"""
Problem Name   : Candy
Problem Url    : https://leetcode.com/problems/candy/
Solution Video : https://youtu.be/h6_lIwZYHQw

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT** **IMPORTANT** **IMPORTANT**
        Approach -> using 2 pass Approach,in question its said that all child must be given
        			atleast one candy so we create an candy array of val 1 of size no of child. 
        			in 1st pass we go from Left to right, each time we see
        			if rating[i]>rating[i-1], means we need to give 1 candy for i greater than 
        			(i-1)th child so we give candy[i]=max(candy[i],candy[i-1]+1) which ever is
        			maximum we take that, because some time we may already have more candy than
        			our neightbour.

        			In 2nd pass we grom right to left, each time we see
        			if rating[i]>rating[i+1], means we need to give 1 candy for i greater than 
        			(i+1)th child so we give candy[i]=max(candy[i],candy[i+1]+1) which ever is
        			maximum we take that, because some time we may already have more candy than
        			our neightbour.

""" 
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies=[1 for i in range(len(ratings))]  #**IMPORTANT** must initilize the candy by 1
        										  #because in question its said that you need
        										  #to give atlest one candy to all child
        
        #left to right
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1

        #right to left
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i],candies[i+1]+1)
        return(sum(candies))
                