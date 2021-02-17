"""   
Key :
"""

"""
Problem Name   : DFS of Graph
Problem Url    : https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1#
Solution Video : 

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT**
        Approach -> do dfs recursively, dont forget to have visited array this is undirected
        			graph so if no visited array means you will end up in infinite loop.
""" 

class Solution:
    def dfsOfGraph(self, V, adj):
        path=[]
        visited=[False for i in range(V)]
        def dfs(root,path):
            if visited[root]:
                return()
            visited[root]=True
            path.append(root)
            for i in adj[root]:
                dfs(i,path)
        dfs(0,path)
        return(path)
        
        
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
        ob = Solution()
		ans = ob.dfsOfGraph(V, adj)
		for i in range(len(ans)):
			print(ans[i], end = " ")
		print()
        

# } Driver Code Ends