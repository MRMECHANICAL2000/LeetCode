"""
Key : know how to find how much fraction of curItem the knapsack can hold in this code and try
	  optimising the same. **IMPORTANT** 
"""

"""
Problem Name   : Fractional Knapsack
Problem Url    : https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1#
Solution Video : https://youtu.be/oTTzNMHM05I

Learning:
    Brute:  **IMPORTANT**
    	Try all the combinations and  validate the same

    Optimal: **IMPORTANT**
        Approach -> Using Greedy. find the ratio of weight and prize and sort them in decending order and 
        			include them into the bag in decending order so as to get max profit.

"""	

#Optimal Approach

def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    value=[(i.value/i.weight,i.weight) for i in Items]
    value.sort(reverse=True)
    profit=0
    for i in value:           #Heart of the code
        if W<=0: 
            break              #knapsack is full
        if W-i[1]>0:
            W-=i[1]
            profit+=i[0]*i[1]  #if weight of material is < knapsack capacity take full item **IMPORTANT**
        else:
            for j in range(0,i[1]+1):
                if W-j<=0:     #if weigh of iteam is > Knapsack capacity then find how much fraction
                    break      #of this iteam knapsack can hold then take thatmuch alone. **IMPORTANT**
            W-=j
            profit+=i[0]*j
        
    return(profit)