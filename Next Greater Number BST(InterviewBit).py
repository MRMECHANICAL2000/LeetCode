"""   
Key : 

"""

"""
Problem Name   : Next Greater Number BST
Problem Url    : https://www.interviewbit.com/problems/next-greater-number-bst/
Solution Video : 

Learning:
	Brute:
		
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as inorder sucessor question

"""	

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	#using Iterative Approach
    def getSuccessor(self, A, B):
        
        root=A
        path=[]
        while root and root.val!=B:
            if root.val>B:
                path.append(("L",root))
                root=root.left

            elif root.val<B:
                path.append(("R",root))
                root=root.right
                
        if not root:
            return(None)
        
        if root.val==B:
            if root.right:
                temp=root.right
                while True:
                    if not temp.left:
                        return(temp)
                    temp=temp.left

            elif path:
                for direction,node in path[::-1]:
                    if direction=="L":
                        return(node)
                else:
                    return(None)    
            else:
                return(None)        


class Solution:
        #using Recursion
        def searchSucessor(root,key,path):
            if not root:
                return(None)
            
            if root.val==key:
                
                if root.right:
                    temp=root.right
                    while True:
                        if not temp.left:
                            return(temp)
                        temp=temp.left

                else:
                    for direction,node in path[::-1]:
                        if direction=="L":
                            return(node)
                    else:
                        return(None)
                        
            elif root.val>key:
                
                return(searchSucessor(root.left,key,path[:]+[("L",root)]))

            elif root.val<key:
                return(searchSucessor(root.right,key,path[:]+[("R",root)]))
        
        return(searchSucessor(A,B,[]))
                
                
                
