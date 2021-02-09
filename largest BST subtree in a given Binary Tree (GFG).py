"""   
Key : always in a tree question 1st think how can you solve it either by top down or bottom up
	  then if you find an appraoch top down means , its optimal approach may be of bottom up
	  manner.
	  **IMPORTANT** **IMPORTANT**

	  Also BST condition is left.val<root.val<right.val not left.val<=root.val<right.val
	  or left.val<root.val<=right.val theoritically you are correct but for not this 
	  question. 
"""

"""
Problem Name   : largest BST subtree in a given Binary Tree
Problem Url    : https://practice.geeksforgeeks.org/problems/largest-bst/1#
Solution Video : https://youtu.be/4fiDs7CCxkc

Learning:
	Brute:
		top down appraoch, at each node check wheather its an valid BST if yes store
		its size at last return the max size. takes O(N^2) time

	Better: 

	Optimal: **IMPORTANT** 
		Approach -> bottom up appraoch , wkt all leaft are BST, so from each leaf we
					'return(isBST,SizeOfBST,maxVal,minVal)' using this data both 
					subTree we see if both subTree are BST it mean our node can be 
					a root of a BST so here we check

					if leftTree_bigVal<root.val<righTree_smallVal
					
					if this condition is satisfied means its a bst, so we return 
					(True,1+leftSize+rightSize,maxRight,minLeft) to parent.
					if this condition not satisfied means we return
					(False,max(sizeOfBST_in_leftTree, sizeOfBST_in_RightTree),...,....)

					finally at the root we will get the result.




"""	

# Return the size of the largest sub-tree which is also a BST
Max=float('inf')
Min=-float('inf')

#return(isBST,SizeOfBST,maxVal,minVal)

def largestBst(root):
    def BSTfinder(root):
        if not root:
            return(True,0,Min,Max)

        leftTree=[True,0,Min,Max] #we use min,max to pass condition on line 64 for leaf Node
        rightTree=[True,0,Min,Max]

        if root.left:
            leftTree=BSTfinder(root.left)
            
        if root.right:
            rightTree=BSTfinder(root.right)
        
        overAllMax=max(rightTree[2],root.data) #**IMPORTANT** Edge Case, if we did not do it
        overAllMin=min(leftTree[3],root.data)  #then 'inf' will be passed up the recurse call

        if leftTree[0] and rightTree[0]:
            if leftTree[2]<root.data<rightTree[3]:
                return(True,1+leftTree[1]+rightTree[1],overAllMax,overAllMin)
        return(False,max(leftTree[1],rightTree[1]),overAllMax,overAllMin)

    result=BSTfinder(root)
    return(result[1])



#{ 
#  Driver Code Starts
import sys
sys.setrecursionlimit(1000000)

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root



if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()

        root = buildTree(s)

        print(largestBst(root))

# } Driver Code Ends