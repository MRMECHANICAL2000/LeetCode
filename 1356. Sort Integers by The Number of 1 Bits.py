"""
Key :
      
"""

"""
Problem Name   : Sort Integers by The Number of 1 Bits
Problem Url    : https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
Solution Video : 
                  

Learning:
    Brute: 
        
    Better:

    Optimal: **IMPORTAT**
        Approach -> find no of set bit in each array element store both (val,setBit Count) in an array
        			sort the array wrt setBit Count,val then return the values alone
                    **IMPORTANT**

""" 

class Solution:
    #Optimal Approach
    def sortByBits(self, arr: List[int]) -> List[int]:
        for idx,val in enumerate(arr):
            arr[idx]=(val,str(bin(val)).count('1'))
        arr.sort(key=lambda x:(x[1],x[0]))
        for idx,val in enumerate(arr):
            arr[idx]=val[0]
        return(arr)