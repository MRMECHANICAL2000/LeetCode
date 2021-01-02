"""    
Key : In python , ord('char')-> gives the ASCII code of that character. ***IMPORTANT**
	  ATOI is an function in c language which is used to convert given valid string to an integer.
	  This question has lot of differnet test case so we use many if , else conditions. 	  
	  **IMPORTNAT**
""" 

"""
Problem Name   : String to Integer (atoi)
Problem Url    : https://leetcode.com/problems/string-to-integer-atoi/
Solution Video : https://youtu.be/2I9XO8jwZCA

Learning:
	Brute:
		Use HashTable and store all numbers in it, loop through given string if curChar is in hashTable
		store it in output.
		
	Better:
		check if curChar is in ASCII range of numbers ie,ASCII range of numbers is 48 to 57 for 0 to 9

	Optimal: **IMPORTANT**
		Approach -> ord('char')-ord('0') will give us value of that char if its an number,
					ord('5')-ord('0')=5, only for numbers we will get values 0 to 9 for all other
					we will get different values other than 0 to 9.
"""	


class Solution:
	#Optimal Solution
    def myAtoi(self, s: str) -> int:
        output="0"
        symbol=""
        for i in s:                       #due to lot of condition in this question we use lot of
        								  #if,else statement **IMPORTNAT**
            if (i=='-' or i=='+') and symbol=="" and output=="0":
                symbol=i
            elif 0<=ord(i)-ord('0')<=9 :
                output+=i
            elif i!=' ' or output!="0" or symbol!="":
                break
        output=symbol+output      
        
        #some times the result we get will be out of max capacity of language -10^31 to 10^31 that
        #time instead of that number we output max or min holdable capacity. **IMPORTANT**
        result = int(output)
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        if result > MAX_INT:
            return MAX_INT

        elif result < MIN_INT:
            return MIN_INT

        else:
            return result
