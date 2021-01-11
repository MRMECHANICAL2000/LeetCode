"""    
Key : We cant use dictionary because we only count consequent numbers 

""" 

"""
Problem Name   : Count and Say
Problem Url    : https://leetcode.com/problems/count-and-say/
Solution Video : 


Learning:
	Brute:
		
	Better:

	Optimal: **IMPORTANT**
	  Approach -> this is an simple implementation based question. just count consequative values
	  			  and store the count and value. finally return them as a string.

"""	

class Solution:
	#Optimal Approach
    def countAndSay(self, n: int) -> str:

        def CAS(x): 
            valStack=[]
            countStack=[]
            ans=""
            
            for i in x:
                if not valStack:
                    valStack.append(i)
                    countStack.append(1)

                elif valStack[-1]==i:
                    countStack[-1]+=1
                else:
                    valStack.append(i)
                    countStack.append(1)
                    
            for idx,val in enumerate(valStack):
                ans+=str(countStack[idx])+str(val)

            return(ans)
                
        sequence='1'
        if n==1:
            return(sequence)
        for i in range(n-1):        
            sequence=CAS(sequence)
        return(sequence)
                
        