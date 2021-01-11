"""    
Key : 
""" 

"""
Problem Name   : Compare Version Numbers
Problem Url    : https://leetcode.com/problems/compare-version-numbers/
Solution Video : 


Learning:
	Brute:

		
	Better:
		

	Optimal: **IMPORTANT**
	  Approach -> split both version with respect to "." then convert all of them into integer
	  			  store them into an array. if the both the array size were not equal append zero
	  			  to them to make them come to equal size.then compare both and return appropriate
	  			  values.

"""	
class Solution:
	#Optimal Approach
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=[int(i) for i in version1.split(".")]                     #Splitting wrt '.'
        v2=[int(i) for i in version2.split(".")]

        if len(v1)>len(v2):											 #Padding zeroes
            [v2.append(0) for i in range(len(v1)-len(v2))]
        elif len(v1)<len(v2):
            [v1.append(0) for i in range(len(v2)-len(v1))]

        if v1<v2:											#comparing and returning appropriate values
            return(-1)
        if v1>v2:
            return(1)

        return(0)