"""    
Key : similair to coin change problem. here make sure to keep 900,400,90,40,9,4 also as change
	  think twise you will understand
	  **IMPORTNAT**
""" 

"""
Problem Name   : Integer to Roman
Problem Url    : https://leetcode.com/problems/integer-to-roman/
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as rome to interger but we do it like how we did coin change problem. In addition
					to that we will be adding 900,400,90,40,9,4 rupee coins for change, because in roman
					these symbol are written differentely from R t L (subtraction happens), other symbol L
					to R addition of symbol
"""	


class Solution:
	#Optimal Solution
    def intToRoman(self, num: int) -> str:
        output=""
        HashTable={0:"0",1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL" ,50:"L" ,90:"XC" ,100:"C", 400:"CD", 500:"D",900:"CM" ,1000:"M"}
        value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]  #**IMPORTANT** keeping 900,400,90,40,9,4 as change

        for i in value:
        	#Approach 2                    #Both approach does same things **IMPORTANT**
            output+=(num//i)*HashTable[i]
            num=num%i
            """
            #Approach 1
            while i<=num:
                num=num-i
                output+=HashTable[i]
            """     
        return(output)
            
