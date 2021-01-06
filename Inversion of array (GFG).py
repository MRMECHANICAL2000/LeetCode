"""
Key : 
"""
"""
Problem Name   : Inversion of array
Problem Url    : https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1#
Solution Video : 

Learning:
	Brute: 
		using two loops and counting inversion. O(N^2)

	Optimal: **IMPORTANT**
		Approach -> using merge sort and counting inversion. O(nlogn)
"""	


#Optimal Approach
def mergeSubroutine(l1,l2):
    inversion=0
    mergedList=[]
    l1_index=0
    l2_index=0
    while len(l1)>l1_index and len(l2)>l2_index:
        if l1[l1_index]<=l2[l2_index]:
            mergedList.append(l1[l1_index])
            l1_index+=1
        else:
            inversion+=len(l1)-l1_index
            mergedList.append(l2[l2_index])
            l2_index+=1
    if len(l1)==l1_index:
        mergedList.extend(l2[l2_index:])
    else:
        mergedList.extend(l1[l1_index:])
    
    return(mergedList,inversion)
    

def countInversions(arr):
    if len(arr)==1 or len(arr)==0:
        return(arr,0)

    j=len(arr)//2

    leftList,leftInversion=countInversions(arr[:j])
    rightList,rightInversion=countInversions(arr[j:])
    sortedList,splitInversion=mergeSubroutine(leftList,rightList)

    return(sortedList,leftInversion+rightInversion+splitInversion)
    
def inversionCount(a,n):
    return(countInversions(a)[1])
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(inversionCount(a,n))
# } Driver Code Ends