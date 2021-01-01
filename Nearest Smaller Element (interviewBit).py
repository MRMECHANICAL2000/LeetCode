"""   
Key : Note question is Nearest smaller element to left not next smaller element to right. so you cant 
	  use the same code of next grater element logic here.read question properly. but you can just reverse
	  the given input array and find next smaller element and store them in an array then reverse the array
	  you will get the required solution.

""" 

"""
Problem Name   : Nearest Smaller Element
Problem Url    : https://www.interviewbit.com/problems/nearest-smaller-element/
Solution Video : 
                 
Learning:
	Brute:
		Using 2 loops and finding next Greater each time. O(N^2) time

	Optimal: **IMPORTANT**
		Approach -> reverse the given array and find next smaller element like how we did using
					stack. store the result in array. then reverse the array and return result.
"""	

class Solution:
	#Optimal Approach
    def prevSmaller(self, A):
        HashTable={}
        stack=[]
        answer=[]
        A=A[::-1]
        for idx,val in enumerate(A):                #To cash all next Smaller element
            if not stack:
                stack.append(idx)
                continue
                
            if val>A[stack[-1]]:
                stack.append(idx)   
            else:
                while stack and val<A[stack[-1]]:           #found the next smaller element
                    HashTable[stack.pop()]=val           #cashing the result. key of question **IMPORTNAT**
                stack.append(idx)
                
        for idx,val in enumerate(A):               #To get result
            try:
                answer.append(HashTable[idx]) #if the element not in hash table it means it has no 
            except:                            #next smaller element so append -1 to answer **IMPORTNAT**
                answer.append(-1)
        return(answer[::-1])
                
        
