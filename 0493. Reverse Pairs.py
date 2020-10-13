"""
Key : Looks simple, but we cant do similair to inversion, we need seperate loop to check them other
      than using mergining loop like we do in insetion sort. look code       **IMPORTANT**  
"""

"""
Problem Name   : Reverse Pairs
Problem Url    : https://leetcode.com/problems/reverse-pairs/
Solution Video : https://youtu.be/S6rsAlj_iB4

Learning:
	Brute: 
		Use two loop and count each element 

	Better:
		using binary search tree inside two loop to search efficiently

	Optimal: **IMPORTANT**
		Approach -> Similair to Count Inversion in merge sort but not exactly same. look the key code of 
		            program and understand it well. need seperate loop to check cant do in mergine loop itself 
		            **IMPORTANT**

"""	

class Solution:
	#Optimal Approach    
    def reversePairs(self, nums: List[int]) -> int:
        def mergeroutine(l,r):

            inversion=0                          #Reverse pair Counting Part **IMPORTANT**
            start=0
            for x in range(len(l)):
                for y in range(start,len(r)):
                    if l[x]<=r[y]*2:  #l[x] and r[y] dont put l[x] and r[x], carefull in putting loop variable
                        break
                    start+=1
                inversion+=start

                                                  #Mergesort Merge subroutine
            output=[]
            j,i=0,0
            while len(l)>i and len(r)>j:                         
                if r[j]>=l[i]:
                    output.append(l[i])
                    i+=1
                    
                elif r[j]<l[i]:
                    output.append(r[j])
                    j+=1
                
            output.extend([l[i] for i in range(i,len(l))])
            output.extend([r[j] for j in range(j,len(r))])
            return(output,inversion)
                                                      #Merge Sort Split subroutine
        def splitroutine(x):
            if len(x)==1 or len(x)==0:
                return(x,0)
            leftArray,leftInversion=splitroutine(x[:len(x)//2])
            rightArray,rightInversion=splitroutine(x[len(x)//2:])
            mergeArray,inversion=mergeroutine(leftArray,rightArray)
            return(mergeArray,inversion+leftInversion+rightInversion)

        return(splitroutine(nums)[1])