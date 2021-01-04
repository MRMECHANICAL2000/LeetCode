"""
Key :
      
"""

"""
Problem Name   : XOR Operation in an Array
Problem Url    : https://leetcode.com/problems/xor-operation-in-an-array/
Solution Video : 
                  

Learning:
    Brute: 
        
    Better:

    Optimal: **IMPORTAT**
        Approach -> create the array as mentioned and find xor of all of its element,return it
                    **IMPORTANT**

""" 

class Solution:
    #Optimal Approach
    def xorOperation(self, n: int, start: int) -> int:
        array=[start+2*i for i in range(n)]
        xor=0
        for i in array:
            xor^=i
        return(xor)
    
