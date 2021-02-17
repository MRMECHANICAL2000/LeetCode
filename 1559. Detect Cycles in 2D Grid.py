"""   
Key : DSU can be used to detect cycle in undirected graph only. famous algorithm use DSU is
	  kruskal Algorithm in to detect cycle in graph.

	  There are two operation in DSU, find & Union.
	  1.Find -> to find wheather given node is in a set(it is an member ship operation)
	  2.Union -> to convert two set into an single set

	  there are 3 ways to have union sets
	  1. by using linked  list(like tree structure)

	  2. using array and doing rank/weight union method.(to find union of two node we take
	  	 parent of one node and fix to another based on which node has more child counts).takes
	  	 O(1) time for union but O(n) time in worst case for find

	  3. Collapsing Find. having only one parent for entire set, if you need to union two set
	  	 take each element of set 1 and make it point to parent of set1 so that each node will
	  	 have only one level of traversal to find parent .O(1) for find, but for union we
	  	 do O(N) in worst case

	  **IMPORTANT** **IMPORTANT** **IMPORTANT** **IMPORTANT**
"""  

"""
Problem Name   : 1559. Detect Cycles in 2D Grid
Problem Url    : https://leetcode.com/problems/detect-cycles-in-2d-grid/
Solution Video : https://youtu.be/wU6udHRIkcc
				 **IMPORTANT** Must watch the video to know the 3 approach in which we 
				 can make DSU find **IMPORTANT**

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT**
        Approach 1-> using DFS and finding cycle. for each cell we go all 4 side and check
        			 if the value are matching, if yes then we see if its a cycle. similair
        			 to cycle in undirected graph with graph colouring.

                    **IMPORTANT** **IMPORTANT** **IMPORTANT**
        Approach 2-> using DSU method, initially we make entire matrix into different sets
        			 we traverse the matrix, at each cell we only check left,down cell (**IMPORTANT**)
        			 very important point you will realize why only left, down checking is
        			 enough ones you understant the DSU propely. if both newCell,curCell has
        			 different parent we make one point to other. if both are has same
        			 parent means the graph has a cycle.

""" 

#Approach 2-> using DSU        
class DSU:
    def __init__(self,n,m):
    			 #Cell:parent **IMPORTANT**
        self.set={(i,j):(i,j) for i in range(n) for j in range(m)}
    
    def find(self,node):	
        if self.set[node]==node:  #if node itself its parent return it because its root node
            return(node)		  #inintialy entire matirix is root node. **IMPORTANT**
        else:
            return(self.find(self.set[node])) #we traverse and find the root node.
        
    def union(self,node1,node2):
        node1_Parent=self.find(self.set[node1])
        node2_Parent=self.find(self.set[node2])
        if node1_Parent!=node2_Parent:				#we find parent of both and union it if possible
            self.set[node1_Parent]=self.set[node2_Parent]
            return(True)
        else:
            return(False)
        
        
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n,m=len(grid),len(grid[0])        
        DSU_set=DSU(n,m)
        
        direction=[(0,1),(1,0)] #only left and down enough **IMPORTANT**
        for row in range(n):
            for col in range(m):
                for x,y in direction:
                    newRow=row+x
                    newCol=col+y
                    #if this cell exist and has same val as our curCell
                    if 0<=newRow<n and 0<=newCol<m and grid[row][col]==grid[newRow][newCol]:
                        node1=(row,col)
                        node2=(newRow,newCol)
                        unionResult=DSU_set.union(node1,node2)
                        if unionResult==False:
                            return(True)    #Yes cycle found
        return(False)


#Approach 1-> using DFS, simialir to cycle detection in undirected graph(Graph Coloring)          
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n,m=len(grid),len(grid[0])        
        visited=[[0 for i in range(m)] for j in range(n)]
        
        def dfs(row,col,parent):  
            if row<0 or row>=n or col<0 or col>=m:
                return(True)

            if visited[row][col]==2:
                return(True)
            
            if grid[parent[0]][parent[1]]!=grid[row][col]:
                return(True)
                        
            if visited[row][col]==1:
                return(False)
            
            visited[row][col]=1
            direction=[[0,-1],[-1,0],[0,1],[1,0]]
            
            for i in direction:
                nextRow=row+i[0]
                nextCol=col+i[1]
                if parent!=[nextRow,nextCol]:
                    if dfs(row+i[0],col+i[1],[row,col])==False:
                        return(False)
                        
            
            visited[row][col]=2
            return(True)
        
        
        for row in range(n):
            for col in range(m):
                if dfs(row,col,[row,col])==False:
                    return(True)
        return(False)