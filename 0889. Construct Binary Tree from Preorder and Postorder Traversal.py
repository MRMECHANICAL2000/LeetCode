"""   
Key : we can create many BT that satisfies the given pre and post order but we can create only
	  one unique Full Binary tree with it.
	  **IMPORTANT**
"""

"""
Problem Name   : Construct Binary Tree from Preorder and Postorder Traversal
Problem Url    : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
Solution Video : https://youtu.be/5lWJpTEnyow
				 **IMPORTANT** Must watch to understand the Logic

Learning:
	Brute:

	Better:

	Optimal: **IMPORTANT**
		Approach -> there can be only one unique binary tree that can be formed from the pre and
					post order traversal. here we take 1st element of pre/last element of post
					will be our root node. we need to split the given array into left,right
					pre & post to recuse on them. for that the clue is, find the 2nd element 
					of pre in post order, post[: pre 2nd element] is left and post[pre 2nd ele:]
					will be our right array. from that take the lenght and splt the pre array 
					as well. **IMPORTANT**
"""	


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre)==0:
            return(None)
        newNode=TreeNode(pre[0])

        if len(pre)==1:
            return(newNode)

        leftPost=post[:post.index(pre[1])+1]
        leftPre=pre[1:len(leftPost)+1]
        
        rightPre=pre[len(leftPre)+1:]
        rightPost=post[len(leftPost):-1]

        newNode.left=self.constructFromPrePost(leftPre,leftPost)
        newNode.right=self.constructFromPrePost(rightPre,rightPost)
        
        return(newNode)
        
