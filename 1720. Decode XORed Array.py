"""   
Key :  decoding an XOR is simple , do the xor again.
		a^b =k,  if we have b and k to get a -> a=k^b thats it.

"""

"""
Problem Name   : Decode XORed Array
Problem Url    : https://leetcode.com/problems/decode-xored-array/
Solution Video : https://youtu.be/sthGfBi890o
                 

Learning:
	Brute:

		
	Better:


	Optimal: 
		Approach -> first element is given , just Xor it with encoded array 1st element you 
					will get the 2nd element , Xor the 2nd element with encoded array 2nd 
					element you will get 3rd element ....continue.		
"""	

class Solution:
	#Optimal Solution
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans=[first]
        for i in encoded:
            ans.append(ans[-1]^i)
        return(ans)
