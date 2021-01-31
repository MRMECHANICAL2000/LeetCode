"""   
Key : 

"""

"""
Problem Name   : Populate Inorder Successor for all nodes
Problem Url    : https://practice.geeksforgeeks.org/problems/populate-inorder-successor-for-all-nodes/1#
Solution Video : 

Learning:
	Brute:
		using the inorder sucessor function, call the function for each node and populate
		the next right pointer. takes O(N^2) time.
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> do inorder traversal store all the element in the array, then populate
					all the element.

"""	
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        self.next=None
'''
def inorder(root):       #Find inorder Traversal
    inorTrav=[]
    if not root:
        return(inorTrav)
    if root.left:
        inorTrav.extend(inorder(root.left))

    inorTrav.append(root)
    
    if root.right:
        inorTrav.extend(inorder(root.right))
    
    return(inorTrav)
    
def populateNext(root):           #populate the node in inorder manner.
    inorTrav=inorder(root)
    
    for idx in range(len(inorTrav)-1):
        inorTrav[idx].next=inorTrav[idx+1]




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        self.next=None
        
# Tree Class
class tree:
    def __init__(self):
        self.root=None


def insert(root,p,c,dr):
    
    if not root:
        return
    
    if root.data==p:
        if dr=='L':
            root.left=Node(c)
        else:
            root.right=Node(c)
        return
    
    insert(root.left,p,c,dr)
    insert(root.right,p,c,dr)


def printd(root):
    
    if not root:
        return
    
    while root.left:
        root=root.left
    
    while root:
        print(root.data,end='->')
        if root.next:
            print(root.next.data,end=' ')
        else:
            print(-1,end=' ')
        
        root=root.next
        
 
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list
        # construct the tree according to given list
        
        t=tree()
        t.root=Node(int(a[0]))
        if a[2]=='L':
            t.root.left=Node(int(a[1]))
        else:
            t.root.right=Node(int(a[1]))
        i=3
         
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dr = a[i + 2]
            i += 3
            insert(t.root,parent, child, dr)  # Insert the nodes in tree.
        
        populateNext(t.root)
        printd(t.root)
        print()
# } Driver Code Ends