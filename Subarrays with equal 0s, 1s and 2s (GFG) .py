"""
Key : you may think that this is easy question similair to equal 0s and 1s question. just convert 
      all 0 to -3 and find subarrya with sum 0. but this approach fails in some test cases. [2,2,2,-3,-3]
      this question can be solved using prefix count array similair to prefix sum array. there we had
      sum of all value until current index, here count each value until current index.
	  **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Equal 0, 1 and 2
Problem Url    : https://practice.geeksforgeeks.org/problems/equal-0-1-and-2/0
Solution Video : https://www.geeksforgeeks.org/substring-equal-number-0-1-2/
                 **IMPORTANT** look the document to understand why **IMPORTANT**

Learning:
	Brute: 
		Using 2 loops and find count of 0,1,2 in subArray each time , O(1) space, O(n^3) time

	Better:
		Approach 1 ->using 2 loop and variable to keep count track. O(1) space and O(n^2) time
		Approach 2 ->using a sliding window, create a sliding window of size 3, slide entire array
					 and check if one 0 and one 1 and 0n2 2 in any subarray, again create an sliding  
					 window of size 6 check if two 0 and two 1 and two 2 in any subarray. again create 
					 an sliding window of size 9,12,15 until you reach size>len(array). we are creating
                     sliding window of size multiple of 3 because we need to check if equal no of
                     0,1,2 exists.

	Optimal: **IMPORTANT**
		Approach -> using prefix count array, in this question we have count of 0,1,2's at each index.
                    the key to solve this question is to find (zeroCount-oneCount,zeroCount-twoCount)
                    at each index and store it on our hashTable if it already exist in hash table it 
                    means there is atleast on subarry until that index which has equal number of zero
                    and ones.

"""	

from collections import defaultdict            #**IMPORTANT** Collection's' spelling don't forget
#Optimal
for _ in range(int(input())):
    HashTable={}
    zeroCount=0
    oneCount=0
    twoCount=0
    HashTable[(0,0)]=1                          #(zeroCount-oneCount,zeroCount-twoCount)
                                                #there we store 0 in our hashTable initially here
                                                #we store (0,0) initially in our hashTable.
                                                #**IMPORTANT**
    subArrayCount=0
    inputString=input()

    for i in inputString:                      #**IMPORTANT**
        if i=="0":                             #Counting 0,1,2 at each index (Prefix Count)
            zeroCount+=1
        elif i=="1":
            oneCount+=1
        else:
            twoCount+=1
        
        tmp = (zeroCount-oneCount,zeroCount-twoCount) #finding (zc-oc,zc-tc)  **IMPORTANT**
        
        if tmp in HashTable:                #if (zc-oc,zc-tc) exist in table it means there is
                                            #atleast one subarry with same no of 0,1,2 count
            subArrayCount+=HashTable[tmp]
            HashTable[tmp]+=1

        else:
            HashTable[tmp]=1
    print(subArrayCount)