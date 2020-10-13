"""
Key : Moors Voting Algorithm, checking if ans is correct and decrementing both variable count in line-45
      **IMPORTANT**  
"""

"""
Problem Name   : Majority Element (>N/3 times)
Problem Url    : https://leetcode.com/problems/majority-element-ii/
Solution Video : https://youtu.be/yDbkQd9t2ig   **IMPORTANT** Must wath video

Learning:
	Brute: 
		Use two loop and count each element , return max repeated element 

	Better:
		using hash table

	Optimal: **IMPORTANT**
		Approach -> Moores Voting Algorithm. note there can be only 2 element of >n/3 times.so use Moores
		            algorithm with two variable.In the question it is mentioned that there may or may not 
		            be such elemet so check it the element returned by algorithm comes more than n/3 times. 
		            **IMPORTANT**

"""	

class Solution:
	#Optimal Approach    
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=0
        c2=0
        e1=-1
        e2=-1
        for i in nums:
            if e1==i:            #1st checkif e1==i or e2==i , then check c1==0  pr c2==0 **IMPORTANT**
                c1+=1
            elif e2==i:
                c2+=1
            elif c1==0:
                e1=i
                c1+=1
            elif c2==0:
                e2=i
                c2+=1

            else:               #**IMPORTANT** Decrement both c1,c2 at same time **IMPORTANT**
                c2-=1           #dont decreament one which is small or big like that stuff
                c1-=1
        
        #Counting part
        checkCount1=0
        checkCount2=0
        for i in nums:
            if i==e1:
                checkCount1+=1
            elif i==e2:
                checkCount2+=1
        answer=[]
        print(e1,e2)

        #checking Part
        if checkCount1>len(nums)//3:
            answer.append(e1)
        if checkCount2>len(nums)//3:
            answer.append(e2)
        return(answer)
