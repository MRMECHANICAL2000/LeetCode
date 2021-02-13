"""   
Key : question given to test your code quality and how you think of edge cases. **IMPORTANT**
	  see the edge case in the code, you did not even taught of it.
"""

"""
Problem Name   : Flood Fill
Problem Url    : https://leetcode.com/problems/flood-fill/
Solution Video :                  

Learning:
	Brute:
		
		
	Better:
		
	Optimal: **IMPORTANT**
		Approach -> simple dfs question. at each node recurse on its left,right,top,down
					children if you find an matching colour value paint it and then check its
					neighbour. if not return back

"""	

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor==image[sr][sc] :  #**IMPORTANT** Edge case in this question
            return(image)			  #if both source and newColour are same you end up with
            						  #an infinite recursion loop. **IMPORTATN** think twise


        def fillFlood(x,y,givCol,newCol):
            if 0<=x<=len(image)-1 and 0<=y<=len(image[0])-1:
                if image[x][y]==givCol:
                    image[x][y]=newCol

		                              #[left,up,right,down]
                    direction=[(0,-1),(-1,0),(0,1),(1,0)]
                    for i in direction:
                        fillFlood(x+i[0],y+i[1],givCol,newCol)
                
        
        fillFlood(sr,sc,image[sr][sc],newColor)
        return(image)