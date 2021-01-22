"""   
Key : Iterative code is more easier than the recursive code. have a look into iteratvie code
	  BFS+queue.
	  **IMPORTANT**
"""

"""
Problem Name   : Path Sum II
Problem Url    : https://leetcode.com/problems/path-sum-ii/submissions/
Solution Video : 
				 **IMPORTANT** 

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> same as how we did pathSum I, here we also cache the path we travelled.
					we will have a global variable if an path is found we append it to global
					answer list.



"""	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
	#Recursive Approach
    def pathSum(self, root: TreeNode, givenSum: int) -> List[List[int]]:        
        self.ans=[]
        def helper(root,givenSum,result):
            if root is None:
                return(False)


            if root.left==None and root.right==None and givenSum==root.val:
                result.append(root.val)
                self.ans.append(result)
                return(True)


            givenSum-=root.val
            result.append(root.val)
            leftTree=helper(root.left,givenSum,result[:])
            rightTree=helper(root.right,givenSum,result[:])        


            return(leftTree or rightTree)
        
        helper(root,givenSum,[])
        return(self.ans)


    #Iterative Approach
    def pathSum(self, root: TreeNode, givenSum: int) -> List[List[int]]:        

        if root is None:
            return([])
        self.ans=[]
        queue=deque()
        			 
        			 #[curNode, curNodeVal , [path we came from]] **IMPORTANT**
        queue.append([root,root.val,[root.val]])
        
        while queue:
            curNode,curNodeVal,result=queue.popleft()
            
            if curNode.left==None and curNode.right==None and sum(result)==givenSum:
                self.ans.append(result)
                
            if curNode.left:
                queue.append([curNode.left,curNode.left.val,result+[curNode.left.val]])

            if curNode.right:
                queue.append([curNode.right,curNode.right.val,result+[curNode.right.val]])
                
        return(self.ans)
            