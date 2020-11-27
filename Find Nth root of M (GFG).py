"""   
Key : Use correct condition to find mid value to make sure we dont over flow. also x^n can be put in 
	  the code as x**n not x*n dont do this simple mistake.
	  **IMPORTANT**

"""

"""
Problem Name   : Find Nth root of M 
Problem Url    : https://practice.geeksforgeeks.org/problems/find-nth-root-of-m/0#
Solution Video : https://www.youtube.com/watch?v=fItuKa_tIpY  
                 

Learning:
	Brute:
		using Mathematics, use **(n) to get square root
		
	Better:
		Using linear search from 1 to M, check all no i**n if any i**n==M then thats the no we are
		searching for.   O(N)	

	Optimal: 
		Approach -> Using Binary search to find the no. if i**n<M loop on left side else loop on right 
					side. O(N log N) time.
"""	

#Brute Solution
for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    root=m**(1/n)
    if root ==int(root):
        print(int(root))
    else:
        print(-1)

#Optimal solution - Using Binary Search
for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    start,end=1,m
    ans=-1
    while start<=end:
        mid=start+((end-start)//2)  #To make sure we dont over flow 

        if (mid**n)==m:   #**IMPORTANT** mid**n means mid^n dont put mid*n like a fool mistake **IMPORTANT**
            ans=mid
            break
        elif (mid**n)<m:
            start=mid+1
        else:
            end=mid-1
    print(ans)
            
            
    
        