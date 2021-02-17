"""   
Key : 1st read the question carefully and see wheather they are asking undirected graph or they
	  are asking directed graph. here you code for directed code then after seeing others
	  solution only you realized that its undirected.
	  **IMORTANT**
"""

"""
Problem Name   : Clone Graph
Problem Url    : https://leetcode.com/problems/clone-graph/
Solution Video : https://youtu.be/vma9tCQUXk8

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT**
        Approach -> using hashtable and  BFS, first make a clone of all the nodes in the
        			graph, then do bfs search on original graph while doing bfs search
        			take the clone of root and make root neighbour clone point to root clone.

        			Another easy way is , instead of making clones and doing BFS while 
        			doing BFS itself you can make the clones.look the code


""" 
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        if not root:
            return(None)
        HashTable={}
        HashTable[root]=Node(root.val)
        queue=[root]

        while queue:
            node=queue.pop()
            for i in node.neighbors:
                if i not in HashTable:
                    queue.append(i)
                    HashTable[i]=Node(i.val)
                HashTable[node].neighbors.append(HashTable[i])

        return(HashTable[root])
            
        