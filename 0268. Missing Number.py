"""
Key : XOR property
      if you say all the 4 approach you will have absolutely no chance of rejection.
"""

"""
Problem Name   : Find the Missing and Repeating Number
Problem Url    : https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
Solution Video : https://youtu.be/5nMGY4VUoRY

Learning:
	Brute: 
		use any n^2 sorting algorithm or brute forcefully check all the combinations

	Better:
	1st approach -> using any O(n log n) sorting algorithm , but most interview wont allow modifying array
	2nd approach -> Using counting sort ,which is like Frequency Array **IMPORTANT** (dont forget the name)

	Optimal: **IMPORTANT**
	1st	Approach -> Using Summation (Some times Lead to Memory Over Flow)
    2nd Approach -> Using XOR Property (Most Optimal Approach)
"""	

class Solution:
	#Better 1nd Approach
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i,v in enumerate(nums):
            if i!=v:
                return(i)
        return(i+1)

    #Optimal 1st Approach
    def missingNumber(self, nums: List[int]) -> int:
        #**->Power ,  ^->XOR loosu mari powere ku XOR use panathae you are not using calculator 
        x2_Minus_y2=sum([i**2 for i in range(1,len(nums)+1)])-sum([i**2 for i in nums]) 
        x_Minus_y=sum([i for i in range(1,len(nums)+1)])-sum([i for i in nums])
        x_Plus_y= x2_Minus_y2//x_Minus_y  #**IMPORTANT** always during division make sure to take care of 
                                          #Zero Division Error. Put a//(b if b!=0 else 1)
        x=(x_Plus_y+x_Minus_y)//2
        y=x_Plus_y-x
        print(x2_Minus_y2,x_Minus_y,x_Plus_y,x,y)
        return("Missing No: ",x,"Repeating No: ",y)

    #Optimal 2nd Approach
    def missingNumber(self, nums: List[int]) -> int:
        #In constrains they said 1,2,....n ,if starting for 0 this medthod wont work , no set bit for 0
        #dont forget this step , direct ta eppudi panarathu nu yosikathey 1st put 0th index in x then 
        #XOR with other index
        x=nums[0]
        #**IMPORTANT**
        #dont do like this you wont get answer via list comprehension we are not summing we are XORing
        #x=[x^i for i in nums[1:]] 
        for i in nums[1:]: #only loop based approach work for XOR ,other will give wrong answer
            x^=i 

        y=1
        for i in range(2,len(nums)+1): #Make sure of edge cases in loop **IMPORTANT** here 1 to n , not 0 to n-1
            y^=i
        x_XOR_y=x^y

        binRep=bin(x_XOR_y)[2:]
        setBitNo=len(binRep)-binRep[::-1].index("1")
        
        #box splitting
        b1=0
        b2=0
        for i in nums:
            binRep=bin(i)[2:] #Note: last set bit(right most one) not the left set bit **IMPORTANT**
            if len(binRep)-binRep[::-1].index("1")==setBitNo:
                b1^=i
            else:
                b2^=i

        for i in range(1,len(nums)+1):
            binRep=bin(i)[2:]
            if len(binRep)-binRep[::-1].index("1")==setBitNo:
                b1^=i
            else:
                b2^=i
        #Remaining in this box will be missing and repeating number
        print(b1,b2)