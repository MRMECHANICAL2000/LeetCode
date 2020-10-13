"""
Key : using Matrix transpose 
"""
"""
Problem Name   : Rotate Image
Problem Url    : https://leetcode.com/problems/rotate-image/
Solution Video : https://youtu.be/Y72QeX0Efxw                **IMPORTANT**
				 https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
				 https://www.geeksforgeeks.org/transpose-matrix-single-line-python/  **IMPORTANT**
Learning:
	Brute: 
		Using antother matrix, take row and put it in last coloum

	Optimal: **IMPORTANT**
		1st Approach -> Take Transpose and reverse each row in the Matrix
				Taking Transpose: 
				**IMPORTANT** Zip(*Martrix)-> outputs coloum of an matrix **IMPORTANT**
				zip Takes unzips element from each row and returns
		2nd Approach -> Inverse entire matrix at first then take transpose
"""	

class Solution:
	#Optimal 1st
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:]=[i[::-1] for i in list(zip(*matrix))]
        #**IMPORTANT** Best way to take transpose

	#Optimal 2nd
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:]=list(zip(*matrix[::-1]))


       