"""   
Key : we can either use binary search by ourself or use bisect library to do the work. but note that bisect
	  and bisect_left both are different you can identify if only if you are searching for an element that
	  already exist in the array.
	  https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
	  **IMPORTANT**

"""

"""
Problem Name   : Median in a row-wise sorted Matrix
Problem Url    : https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1#
Solution Video : https://www.youtube.com/watch?v=_4rxBuhyLXw
				 **IMPORTANT** Must watch the video to get the intution **IMPORTANT**                 

Learning:
	Brute:
		Take all the element put it in new array sort it and find median
		
	Better:
		do like merge step in mergesort , merge all row into an array until we get median.

	Optimal: 
		Approach -> By using binary search.just find the min,max and no of element in the matrix. find the
					mid of min and max element and then count no of element < than mid in the array. compare
					this count with total_element_in_array//2 if both count
"""	

#Optimal solution - Using Binary Search
#User function Template for python3
import bisect
class Solution:
    def median(self, matrix, r, c):
        def countVal(mid):
            count=0
            for i in matrix:
                count+=bisect.bisect(i,mid) #this question dont use bisect_left     **IMPORTANT**
                #There is an differenet between bisect and bisect_left it can seen 
                #if the element we search is in the array
                #https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
                
            return(count)
    
        start=min([i[0] for i in matrix])  #To find the min,max value in total matrix
        end=max([i[-1] for i in matrix])#min of all will be in 1st col, and max of all will be in last col

        desiredCount=((r*c)+1)//2 #To find no of element in the matrix **IMPORTANT**
        

        while start<end:
            mid=start+(end-start)//2
            count=countVal(mid)
            

            """if count==desiredCount:
                break"""  #we break when the loop itself break no breaking condinton

            if count<desiredCount: #then median should lie on right side    **IMPORTANT**
                start=mid+1                
            else: #both >= here, if you put this in if block dont forget to include >= not just > condition
                end=mid #Dont include mid-1 here we need to look until mid then only start will contain the median element data
        return(start) #Here we output start not mid


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends
            
    
        