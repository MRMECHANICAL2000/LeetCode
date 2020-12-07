"""   
Key : look at how the bit approach work and keep an eye on the brackets during the bit approach
	  **IMPORTANT**

"""

"""
Problem Name   : square of a number without using *, /
Problem Url    : 
Solution Video : https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/

Learning:

	Brute: 
		5^2= 25 which means add 5 , five times. so a Simple Solution is to repeatedly add n to result. 
		O(N) linear time.

	Optimal:  **IMPORTANT** **IMPORTANT**
		Using Bit Operation. O(Log N) time.

		  square(n) = 0 if n == 0
		  if n is even 
		     square(n) = 4*square(n/2) 
		  if n is odd
		     square(n) = 4*square(floor(n/2)) + 4*floor(n/2) + 1 

		Examples
		  square(6) = 4*square(3)
		  square(3) = 4*(square(1)) + 4*1 + 1 = 9
		  square(7) = 4*square(3) + 4*3 + 1 = 4*9 + 4*3 + 1 = 49


"""	


#Brute Force Approach
def square(n):
    # handle negative input  **IMPORTANT**
    if (n < 0):
        n = -n
 
    # Initialize result
    res = n
 
    # Add n to res n-1 times
    for i in range(1, n):
        res += n
 
    return res
 
#Optimal Approach
def square(n):
 
    # Base case
    if (n == 0):
        return 0
 
    # Handle negative number
    if (n < 0):
        n = -n
 
    # Get floor(n/2) using
    # right shift
    x = n >> 1
 
    # If n is odd
    if (n & 1):
        return ((square(x) << 2) + (x << 2) + 1) #**IMPORTANT** 
        										 #Take care of bracket during bit operation , small brack
        										 #will leads to wrong answer
 
    # If n is even
    else:
        return (square(x) << 2)
 
# Driver Code
for n in range(1, 6):
    print("n =", n, end=", ")
    print("n^2 =", square(n))
 


