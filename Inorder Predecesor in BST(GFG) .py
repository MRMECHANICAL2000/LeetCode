"""   
Key : similair to how we find inorder sucessor. with small changes.

"""

"""
Problem Name   : Inorder Predecesor in BST
Problem Url    : 
Solution Video : https://youtu.be/rukYFD8cYBY

Learning:
	Brute:
		do inorder traversal convert the BST to sorted array, find the element X in it and
		return the previous element/smaller element /inorder predecesor. O(N) space used
		
		
	Better:


	Optimal: **IMPORTANT**
		Approach ->  find the element x in the tree, if it has an left subTree then the 
					 largest element in the left subtree is our prev smaller element. if 
					 it does not has an left subTree then from the path we come in, the node
					 at which we too the last right looking from down to top is our smaller element
					 so while finding the node itself we store the path in which we come to 
					 trace back to parent. if there is not any node to left or no node that take
					 first right to reach our node X means it is the smallest element in the Tree.

"""	

#User function Template for python3

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''
# returns the inorder successor of the Node x in BST (rooted at 'root')
def inorderPredecesor(A, B):
    root=A
    path=[]
    									#finding the node via looping and saving the path
    									#we come from **IMPORTANT**
    while root and root.data!=B.data:
        if root.data>B.data:
            path.append(("L",root))
            root=root.left

        elif root.data<B.data:
            path.append(("R",root))
            root=root.right
            
    if not root:		#Base case if we did not find root it means there is no such element
        return(None)	#in the BST so we cant find its prev smaller element
    
    if root.data==B.data: #If the element X exist

        if root.left:				#we check if it has an left subTree if yes return the
            temp=root.left			#largest element in the left subTree. **IMPORTANT**
            while True:
                if not temp.right:
                    return(temp)
                temp=temp.right

        elif path:					#else from the path we come , return the node at which
        							#we take a right turn at last to reach node X. **IMPORTANT**
            for direction,node in path[::-1]:
                if direction=="R":
                    return(node)
            else:
                return(None)    
        else:
            return(None)


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
        ptr = inorderSuccessor(root, Node(k))
        if ptr is None:
            print(-1)
        else:
            print(ptr.data)
# } Driver Code Ends