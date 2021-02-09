"""   
Key : kth largest element means n-k th smallest element we dont know n here so you cant use 
	  the same code of kth smallest
	  just change the traversing order, reverse inorder traversal use it.

	  Must learn the usage of nonlocal key word, instead of saying a variable is global 
	  you can use nonlocal to indicate its not an local variable.this key word is used
	  to work with nested function.
	  
	  https://www.geeksforgeeks.org/use-of-nonlocal-vs-use-of-global-keyword-in-python/
	  **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Kth largest element in BST
Problem Url    : https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1#
Solution Video : 

Learning:
	Brute:
		
	Better: 

	Optimal: **IMPORTANT** 
		Approach -> same as kth smallest element code there we do inorder traversal here
					we do reverse inorder traversal. ie, 1st visit right,root,left.

"""	

#User function Template for python3

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None
# return the Kth largest element in the given BST rooted at 'root'

def kthLargest(root, k):
    ans=None
    def inorder(root): #Reverse inorder Traversal **IMORTANT**
        if not root:
            return()

        nonlocal k    #**IMPORTANT** **IMPORTANT**  
        nonlocal ans  #Learn the use of nonlocal key word

        if k>0:
            if root.right:
                inorder(root.right)  #Right Node
            k-=1
            if k==0:
                ans=root.data        #Root Node
            if root.left:
                inorder(root.left)   #Left Node
                
    inorder(root)
    return(ans if ans!=None else -1)
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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
        k = int(input())
        print (kthLargest(root, k))
# } Driver Code Ends