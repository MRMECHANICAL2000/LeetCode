"""   
Key :  same as decode XORed array,there they have given the first element but here they
	   have not given the first element so we need to find it some how with the clue given
	   in the question
	   **IMPORTANT**
	   You failed to sove it during the contest -weekly contest 44

"""

"""
Problem Name   : Decode XORed Permutation
Problem Url    : https://leetcode.com/problems/decode-xored-permutation/
Solution Video : https://youtu.be/Gqp_osiLqeo                 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT** **IMPORTANT**
		Approach -> the key in the question is that they are given the permuatation is of
					first N positive natural number. so we find the XOR of all the n number.
					to solve the question we just need the first number in permutation.so

					a1,a2,a3,a4,a5,a6,a6,a7.......a(n-1),a(n) -> first n natural number
					
					xor all the element and store it in = TotalXOR

					(a1^a2,a2^a3,a3^a4,a4^a5,a5^a6,a6^a7.......) ->given decoded array
					   0      1    2     3     4      5   

					 Xor all element in odd index -> a2^a3^a4^a5^a6^a7 =withoutFirstEleXOR

					 now if we XOR both we will get first element,
					 firstEle=TotalXOR-withoutFirstEleXOR

"""	

class Solution:
	#Optimal Solution
    def decode(self, encoded):
        totalXOR=0
        for i in range(1,len(encoded)+2):  #clue in question is 1st N positive integer were 
        								   #used to make permutation
            totalXOR^=i
        
        
        #to find 1st value
        withoutFirstEleXOR=0
        for i in range(1,len(encoded),2):
            withoutFirstEleXOR^=encoded[i]
        

        firstEle=totalXOR^withoutFirstEleXOR
        
        ans=[firstEle]
        for i in encoded:
            ans.append(ans[-1]^i)
        
        return(ans)