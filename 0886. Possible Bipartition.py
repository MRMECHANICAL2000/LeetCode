"""   
Key : same as is graph bipartite question , here we need to create the adjacency repsentation 
	  of the graph.

"""

"""
Problem Name   : Possible Bipartition
Problem Url    : https://leetcode.com/problems/possible-bipartition/
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
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        graph={}
        for i in range(1,N+1):
            graph[i]=[]
        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        colour={}
        for idx in range(1,N+1):
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
        
        for i in range(1,N+1):
            if colour[i]==-1:
                colour[i]=1
                canSplit=dfs(i)
                if not canSplit:
                    return(False)

        return(True)