"""   
Key : you did not had intution for this approach kindly learn it properly.
	  you did not craphy return type appraoch which will return the node and 
	  you messed up in make right point to parent of paretent and lot of 
	  confusion. not a good program will make this mistakes.

	  look how we did flatern BT to Singly linked List , there also we did same approach
	  of using an prev node even after doing that question you did not had the taught that
	  we can easily solve this question using prev approach. you started thinking like
	  an creepy programmer using some worst approach which do creepy stuff
	  **IMOPRTANT** **IMOPRTANT** **IMOPRTANT**
"""

"""
Problem Name   : Binary Tree to DLL
Problem Url    : https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1#
Solution Video : https://youtu.be/9ox7vRl8Ags                
				 **IMPORTANT** Must watch this 4 min video to know how prev works **IMPORTANT**


Learning:
	Brute: 
		do inorder Traversal and store all nodes in an arry, then connect all the nodes.
		but this method will take O(N) space.

	Better:
		

	Optimal: **IMPORTANT** **IMOPRTANT** **IMOPRTANT**
		Approach -> to do inorder traversal inPlace without using additional memory or  
					without using any seperate way to create DLL we need to use the 
					left,right pointer of the BST as DLL left,right. the easy way is to
					do inorder traversal with a variable called "prev" each time you
					finish a left search we see prev , if prev=None it means we are in
					left most node which is the head of DLL. if prev!=None means we make
					root.left=prev and prev.right=root. then we make prev=root. this will
					make the BST to DLL.



"""	

#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

def bToDLL(root):

    head=None
    prev=None
    def inorder(root):
        nonlocal prev   #**IMPORTANT** 
        nonlocal head   #**IMPORTANT** 

        if not root:
            return(None)
            				#**IMPORTANT**
        inorder(root.left)  #dont think creepy idea like left=inorder(root.left).... return(root)
        					#there should be no return in your code if you return someting in
        					#recursive code you gonna make lot of mistake referening, pointing...
        if not prev:		
            head=root
        else:
            root.left=prev
            prev.right=root
        prev=root    
        inorder(root.right)
    inorder(root)
    return(head)
        

#{ 
#  Driver Code Starts
from collections import deque
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

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


import sys            
def printDLL(head): #Print util function to print Linked List
    prev = None
    sys.stdout.flush()
    while(head != None):
        print(head.data, end=" ")
        prev=head
        head=head.right
    print('')
    while(prev != None):
        print(prev.data, end=" ")
        prev=prev.left
    print('')
    
if __name__=='__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        head = bToDLL(root)
        printDLL(head)
# } Driver Code Ends
