"""   
Key : 

"""

"""
Problem Name   : Top View of Binary Tree
Problem Url    : https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#
Solution Video : 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> Do vertical order traversal , then return the 1st node in each horizontal
					distance.
"""	

from collections import defaultdict


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def topView(root):
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
            VerticalOrder[i].extend(sorted(tempVerticalOrder[i]))


    HorizontalDistance=list(VerticalOrder.keys())
    HorizontalDistance.sort()
    
    [print(VerticalOrder[i][0],end=" ") for i in HorizontalDistance]  #only change **IMPORTANT**
    return()
    # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Contributed by Sudarshan Sharma

from collections import deque
import queue 

class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def make_tree():
    n=int(input())
    l=list(map(str,input().split()))
    head=None
    q=deque()
    i=0
    while(n>0):
        a,b,c=l[i],l[i+1],l[i+2]
        if(not head):
            head=Node(int(a))
            q.append(head)
        pick=q[0]
        q.popleft()
        if(c=='L'):
            pick.left=Node(int(b))
            q.append(pick.left)
        n=n-1
        if(not n):
            break
        a,b,c=l[i+3],l[i+4],l[i+5]
        if(c=='R'):
            pick.right=Node(int(b))
            q.append(pick.right)
        i=i+6
        n=n-1
    return head
            

if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        root=make_tree()
        topView(root)
        print()

# } Driver Code Ends