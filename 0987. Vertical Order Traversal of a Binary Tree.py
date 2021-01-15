"""   
Key : HashTable + Horizontal Distance + Level Order Travesal -> Vertical Order Traversal
	  Main mistake here we made is that in question its said if two or more node on
	  same level have same horizontal distance we should need to store them in accending 
	  order.so at each level before inserting we should need to sort the element and insert them

"""

"""
Problem Name   : Vertical Order Traversal of a Binary Tree
Problem Url    : https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Solution Video : https://youtu.be/PQKkr036wRc  -> Generally to learn Verrtical Order Traversal
				 https://youtu.be/kqHNP6NTzME  -> for this question
Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT**
		Approach -> to do vertical order traversal we find horizontal distance(Hd) of each node
					the horizontal distance is the distance of a node from a vertical axis.

								 root
						          |
						          |
						    left  |  right
						     |    |    |
						 |   |    |    |   |
					_____|___|____|____|___|____
					....-2  -1	  0    1   2....

					we will consider the root as vertical line, the root has Hd=0, its left
					child has Hd=-1 and right child has Hd=+1, ie, left child of node has 
					rootHd-1 , right child has rootHd+1. so here while creating level order 
					traversal queue , while appending the node we calculate its Hd and also
					append its Hd as well. finally we use an HashTable in which Hd will be
					key and all node that has that horizontal distance will be its value.

					but in the question it is asked that if many node has same Hd and at same
					level we should need to store them in accending order. to over come this
					we each level we use an tempHashTable store nodes in it and at end of
					each level we sort the tempHashTable element and store them in the final
					hashTable

"""	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return([])
        queue=deque()
        queue.append((root,0))       #In addition to appending root we append its Hd **IMPORTANT**
        VerticalOrder=defaultdict(list)
        VerticalOrder[0]=[root.val]

        while queue:
            tempQue=deque()
            tempVerticalOrder=defaultdict(list)   #**IMPORTANT** we should need to use temp
            									  #hashTable then only we can just sort them
            									  #and insert into original, we if directely
            									  #insert it to original we cant sort it.
            while queue:
                popNode,horiDist=queue.popleft()
                
                if popNode.left:
                    tempQue.append((popNode.left,horiDist-1))
                    tempVerticalOrder[horiDist-1].append(popNode.left.val)
                    
                if popNode.right:
                    tempQue.append((popNode.right,horiDist+1))     
                    tempVerticalOrder[horiDist+1].append(popNode.right.val)
                    
            queue=tempQue
            for i in tempVerticalOrder:
                VerticalOrder[i].extend(sorted(tempVerticalOrder[i]))


        HorizontalDistance=list(VerticalOrder.keys())
        HorizontalDistance.sort()
        
        ans=[VerticalOrder[i] for i in HorizontalDistance]
        return(ans)
    