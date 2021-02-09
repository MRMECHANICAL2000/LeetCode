"""   
Key : look the optimization in space made here thing like a cp programmer.
	  **IMPORTANT**
"""

"""
Problem Name   : Binary Search Tree Iterator
Problem Url    : https://leetcode.com/problems/binary-search-tree-iterator/
Solution Video : https://www.youtube.com/watch?v=-nx0sIvELTA&t=325s

Learning:
	Brute:
		do inorder ans store it in array, have a pointer to it , each time when required
		output the element in that pointer and increment it. takes O(N) space.
		
	Better:


	Optimal: **IMPORTANT**
		Approach -> to optimize the space instead of storing the entire tree, when we are
					at a node we just store its leftsub Tree in reverse inorder way inside
					an stack and move the root pointer to root.left. now each time we
					require the next value we pop the last element from stack and return it
					if the stack become empty we again fill it by storing the left subTree
					value in it. when both stack==[] and root is None means we have exasted
					the tree so we return False.
"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def fillLeft(self):			#Storing the leftSubTree inside our stack **IMPORTANT**
        if not self.root:
            return()
        
        def inorder(root):
            ele=[]
            if not root:
                return(ele)
            
            if root.right:
                ele.extend(inorder(root.right))

            ele.append(root.val)

            if root.left:
                ele.extend(inorder(root.left))
                            
            return(ele)
        
        self.leftTreeStack.append(self.root.val)
        self.leftTreeStack+=inorder(self.root.left)
        self.root=self.root.right 
        
    def __init__(self, root: TreeNode):  #Initilizing our DataStructure here
        self.root=root
        self.leftTreeStack=[]
        self.fillLeft()

    def next(self) -> int:      #if stack not empty return its last element if empty fill
    							#the stack and return last element if after filling also
    							#stack empty means we have exausted the tree retun None
    							#**IMPORTNAT**
        if self.leftTreeStack:
            return(self.leftTreeStack.pop())
        else:
            self.fillLeft()
            if self.leftTreeStack:
                return(self.leftTreeStack.pop())
            else:
                return(None)

    							#**IMPORTNAT**
    def hasNext(self) -> bool:  #if atlest stak or root is there , next element is conform
        if self.root or self.leftTreeStack:
            return(True)
        return(False)


#Your BSTIterator object will be instantiated and called as such:
#obj = BSTIterator(root)
#param_1 = obj.next()
#param_2 = obj.hasNext()
