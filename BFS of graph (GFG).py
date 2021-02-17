"""   
Key :
"""

"""
Problem Name   : BFS of graph
Problem Url    : https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
Solution Video : 

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT**
        Approach -> Implementation of BFS using Queue iterative version

""" 

from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
        visited=[False for i in range(V)]
        queue=deque([0])
        ans=[]
        while queue:
            node=queue.popleft()
            if not visited[node]:
                ans.append(node)
                queue.extend(adj[node])
                visited[node]=True

        return(ans)
        