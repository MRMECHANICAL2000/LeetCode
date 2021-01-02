"""    
Key : adding all values and just subtract only the value which is next value. Read question well to 
	  understand it prpoerly.
	  **IMPORTNAT**
""" 

"""
Problem Name   : Roman to Integer
Problem Url    : https://leetcode.com/problems/roman-to-integer/
Solution Video : https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> In an hashTable store all RomanChar and their value. loop the given string if val in
					curIdx is greater than val in next index add the value to output. if its lesser then
					subtract the value to overall sum. because in roman letter, values are written from
					Left to right.
					The number 27 is written as XXVII, which is XX + V + II
					2 is written as II in Roman numeral, just two one's added together
					12 is written as XII

					Roman numerals are usually written largest to smallest from left to right. However,
					the numeral for four is not IIII. Instead, the number four is written as IV. Because
					the one is before the five we subtract it making four. The same principle applies to 
					the number nine, which is written as IX. There are six instances where 
					subtraction is used:

					I can be placed before V (5) and X (10) to make 4 and 9. 
					X can be placed before L (50) and C (100) to make 40 and 90. 
					C can be placed before D (500) and M (1000) to make 400 and 900.

"""	

class Solution:
	#Better Solution
    def romanToInt(self, s: str) -> int:
        s+="0"
        HashTable={"0":0,"I":1,"V":5,"X":10 ,"L":50,"C":100,"D":500,"M":1000}
        val=0
        for idx in range(0,len(s)-1):
            if HashTable[s[idx]]<HashTable[s[idx+1]]:
                val-=HashTable[s[idx]]
            else:
                val+=HashTable[s[idx]]
        return(val)