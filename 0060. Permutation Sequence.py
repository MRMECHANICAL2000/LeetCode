"""
Key : brute method you can do but mathemitical method you need to watch the video to understand 
	  Know the use of divmode() and math.factorial() function. **IMPORTANT** **IMOPORTANT**
	  https://www.w3schools.com/python/ref_func_divmod.asp
	  **IMPORTANT**
"""   

"""
Problem Name   : Permutation Sequence
Problem Url    : https://leetcode.com/problems/permutation-sequence/
Solution Video : https://youtu.be/W9SIlE2jhBQ
				 **IMPORTANT**Must Must Must watch to know the mathemitical shortcuts **IMPORTANT**

Learning:
	Brute: 
		just take the next permutation code. call it k times to get kth permutaion 

	Optimal: **IMPORTANT**
		Approach -> Mathemitical method see the video to understand it. but this method works if the
					1st permutatino is in correct accending order.if an permutation in middle is given 
					and ask us to find kth permutation from there this method wont works
"""	

class Solution:
	#Brute Approach
    def getPermutation(self, n: int, k: int) -> str:
        def nextPermutation(sequence):                      #Find Next permutation code
            for i in range(len(sequence)-1,0,-1):
                if sequence[i]>sequence[i-1]:
                    for j in range(len(sequence)-1,i-1,-1):
                        if sequence[i-1]<sequence[j]:
                            sequence[i-1],sequence[j]=sequence[j],sequence[i-1]
                            break
                    sequence[i:]=sequence[i:][::-1]
                    break
            return(sequence)

        sequence=[i for i in range(1,n+1)]                  #Calling next permutation N times
        for i in range(1,k):
            sequence=nextPermutation(sequence)
        return("".join([str(i) for i in sequence]))


    #Optimal Mathemitical approach
	import math
    def getPermutation(self, n, k):
        sequence=[i for i in range(1,n+1)]
        permute=""
        k-=1
        import math
        while n>0:
            n-=1 # updating n,k each time. find index of a correct number append to result 
            	 # remove form sequence. repeat it . **IMPORTNAT**         
            index,k=divmod(k,math.factorial(n))

            permute+=str(sequence[index])
            sequence.pop(index)
        return(permute)

