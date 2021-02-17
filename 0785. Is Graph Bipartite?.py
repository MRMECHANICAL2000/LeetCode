"""   
Key : just knowing how to solve this question is not enough you need to why when can you make
	  bipartaite and when you cant make bipartaite, if your graph has an odd length cycle then
	  you cant make an bipartatie, if your graph has no cycle or even length cycle you can make
	  bipartaite.look the tech dose video for theory.

	  The graph has the following properties to have an bipartaite

	  There are no self-edges (graph[u] does not contain u).
	  There are no parallel edges (graph[u] does not contain duplicate values).
	  The graph may or may not be connected, meaning there may be two nodes u and v 
	  such that there is no path between them.

	  **IMPORTANT** **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : Is Graph Bipartite?
Problem Url    : https://leetcode.com/problems/is-graph-bipartite/
Solution Video : https://youtu.be/0ACfAqs8mm0

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT** **IMPORTANT** **IMPORTANT**
        Approach 1 -> using two hashTable, initially we take one edge and see node in edge is
        			present in HT_1 or HT_2, if both of them were not present we put node1,node2
        			in HT_1,HT_2. if any one node(eg:node_1) present in any one hashTble(eg:HT_1)
        			then we put node2 in HT_2, if both node are already present and they are in
        			different hashSet well and good we skip this edge, if both node are already
        			present and they are in same hashTable it means there is an odd length cycle
        			and we cant make bipartaite with it.

        Approach 2 -> its an classical graph question, Bipartaite check and it can be solve
        			  using graph colouring concept with 2 colour. we go to a node and see if
        			  its coloured is not we colour it with Red and start dfs,we check all its
        			  neighbour if the neigbour is already coloured and its not red, we return
        			  True, if neighbour is not already coloured we colour it with opposite 
        			  colour of our parent node(red/green) and we start dfs for that node.if the
        			  node is already coloured and its same colour as parent node then we return
        			  false which means we can make bipartaite/given graph has odd length cycle.

			        #-1 -> no colour yet
			        #1 -> Red colour
			        #2 -> Green Colour

""" 

class Solution:
    def isBipartite(self, graph):
        colour={}
        for idx in range(len(graph)):
            colour[idx]=-1
        
        #-1 -> no colour yet
        #1 -> Red colour
        #2 -> Green Colour
        
        def dfs(node):
            for i in graph[node]:
                if colour[i]==-1:
                    colour[i]=1 if colour[node]==2 else 2
                    canSplit=dfs(i)
                    if canSplit==False:
                        return(False)

                elif colour[i]==colour[node]:
                    return(False)

            return(True)
        
        for i in range(len(graph)):
            if colour[i]==-1:
                colour[i]=1
                canSplit=dfs(i)
                if not canSplit:
                    return(False)

        return(True)