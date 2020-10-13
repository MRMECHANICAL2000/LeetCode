"""
Key : Similair to counting subarray with given sum k , **IMPORTANT**
	  XOR symbol is "^" not "|"
"""

"""
Problem Name   : Count the number of subarrays having a given XOR
Problem Url    : https://www.geeksforgeeks.org/count-number-subarrays-given-xor/
Solution Video : https://youtu.be/lO9R5CaGRPY

Learning:
	Brute: 
		Using 2 loops and find XOR of all element in each subarray compare with K and store count

	Optimal: **IMPORTANT**
		Approach -> Using HashTable , instead of "+" put "^" in  previous problem. **IMPORTANT**

"""	

from collections import defaultdict
def subarrayXor(arr, n, m): 
	HashTable=defaultdict(bool)     #Think properly you will understand .
	HashTable[0]=1                  #**IMPORTANT** Either it is XOR or +, this step is same **IMPORTANT**
	count=0                         #if this step not entire array XOR equl to m time la count aagathu
	curSum=0
	for i in arr:
	    curSum^=i
	    if HashTable[curSum^m]:
	        count+=HashTable[curSum^m]
	    HashTable[curSum]+=1
	return(count)
	    