"""   
Key : 

"""

"""
Problem Name   : Bottom View of Binary Tree
Problem Url    : https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1#
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> Do vertical order traversal , then return the last node in each horizontal
					distance.
"""	


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import defaultdict
def bottomView(root):
    if not root:
        print([])
    queue=deque()
    queue.append((root,0))       #In addition to appending root we append its Hd **IMPORTANT**
    VerticalOrder=defaultdict(list)
    VerticalOrder[0]=[root.data]

    while queue:
        tempQue=deque()
        tempVerticalOrder=defaultdict(list)   #**IMPORTANT** we should need to use temp
        									  #hashTable then only we can just sort them
        									  #and insert into original, we if directely
        									  #insert it to original we cant sort it.
        while queue:
            popNode,horiDist=queue.popleft()
            
            if popNode.left:
                tempQue.append((popNode.left,horiDist-1))
                tempVerticalOrder[horiDist-1].append(popNode.left.data)
                
            if popNode.right:
                tempQue.append((popNode.right,horiDist+1))     
                tempVerticalOrder[horiDist+1].append(popNode.right.data)
                
        queue=tempQue
        for i in tempVerticalOrder:
            VerticalOrder[i].extend(tempVerticalOrder[i])


    HorizontalDistance=list(VerticalOrder.keys())
    HorizontalDistance.sort()
    
    return([VerticalOrder[i][-1] for i in HorizontalDistance]) #Only Change **IMPORTANT**




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = bottomView(root)
        for i in res:
            print (i, end = " ")
        print()


# } Driver Code Ends