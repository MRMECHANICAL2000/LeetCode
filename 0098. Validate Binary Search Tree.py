"""   
Key : your initial intution will be, for each node check if left<root<right, thats engough? but
	  think twise, the condition will be true in below tree but its not an valid binary search
	  Tree because , 2 which is in right side of root 5, is less than 5. every element to left
	  of root must be < than root and every element to the right of root must be > than root.
		   5
		 /   \
		1     3
			/   \
		   2     4
"""

"""
Problem Name   : Validate Binary Search Tree
Problem Url    : https://leetcode.com/problems/validate-binary-search-tree/
Solution Video : https://youtu.be/TKvbwPIOGCM                 

Learning:
	Brute:
		
		
	Better:
		for every node go to left subTree and find the biggest value there it should be
		lesser than the root value and go to right subTree and find the smallest value there
		it should be greater than root val. recursively applay this to each node.(ie, for
		every node push the minVal,maxVal in that tree to its parent)

	Optimal: **IMPORTANT**
		Approach ->  the better approach work but its hard to implement it, the shortcut to 
					 solve this question is, it is said that the node will lie in range
					 -2^31 to 2^31, so we go to root and check if root.val(x) lies between
					 the limit,if yes we recurse on its child for left child we check if
					 it lies between (-2^31 to x) and we check if right child lies between
					 the range (x to 2^31). we recursively do this for all the child and return
					 true or false to the parent.
"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        minVal=-pow(2,31)-1  #**IMPORTANT** This values were given in Question constrains
        maxVal=pow(2,31)+1  #or else you may chose any bigger value. but make sure to chose
        					#one number greater than limits given in question in both +ve and
        					#-ve limits , else some test case will fail think twise look the
        					#condition in line 57
        
        def ValidBSTChecker(root,minVal,maxVal):
            if not root:
                return(True)
               							 #**IMPORTANT** 
            if minVal<root.val<maxVal:   #Its BST so <=/>= wont come(atleast for this question)
                leftTree=ValidBSTChecker(root.left,minVal,root.val)
                rightTree=ValidBSTChecker(root.right,root.val,maxVal)
                
                if leftTree and rightTree:
                    return(True)
            return(False)
        return(ValidBSTChecker(root,minVal,maxVal))