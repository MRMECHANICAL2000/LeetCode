"""
Key : Best way to optimise is not to find which position is free each time but to keep track of 
	  the current vertex that we have finished. this question has more optimization than the sudako
	  problem. look the code
	  **IMPORTANT** **IMPORTANT** **IMPORTANT**
"""

"""
Problem Name   : M-Coloring Problem
Problem Url    : https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#
Solution Video : https://youtu.be/052VkKhIaQ4
				 https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/
				 **IMPORTANT** must must Watch to know use case of problem**IMPORTANT**  

Learning:
    Brute:  **IMPORTANT**
        final all the colour configuration and evaluvate the all. for finding all colour it takes exponential 
        time O(2^n) for evaulvating each board it takes O(n^2), so O(n^2 * 2^n)


    Optimal: **IMPORTANT**
        Approach -> By using BackTracking, this approach takes O(2^n) exponential time to complete 
        			but its 100 times faster than brute force approach.The idea is to assign colors 
        			one by one to different vertices, starting from the vertex 0. Before assigning a 
        			color, check for safety by considering already assigned colors to the adjacent vertices
        		    **IMPORTANT**

"""	



#Optimal Approach

from collections import defaultdict
def graphColoring(graph, k, V):
    '''
    :param graph: grid of size V*V in specified format(0 based indexing i.e. vertex 1 is index 0)
    :param k: number of colors allowed
    :param V: number of vertices 
    :return: True or False
    '''
    
    def nextFree():                    #Time consuming approach , finiding which vertex is free each time
        for i in colourGraph.keys():   #**IMPORTANT** similair to how we did in sudako.
            if colourGraph[i]==0:      #The optimization we have done in this question can be used in 
                    return(i)          #sudako problem as well
        return(None)
    
    def isValid(i,colour):
        if colour not in graph[i]:    # To check if the colour is in any of neighbour in graph
            return(True)
        return(False)
        
    def addColour(i,colour):          #to add that colour on vertex and mark on graph as well
        colourGraph[i]=colour
        neighbour=[j for j,v in enumerate(graph[i]) if v!=0]
        for j in neighbour:
            graph[j][i]=colour
    
    def removeColour(i):             #to remove that colour and mark on graph as well
        colourGraph[i]=0
        neighbour=[j for j,v in enumerate(graph[i]) if v!=0]
        for j in neighbour:
            graph[j][i]=1    #**IMPORTANT** [j][i] not [i][j] think carefully **IMPORTANT**
    
    def ColoringGraph(curVertex):
        i=curVertex
        if i==len(graph): #To Make sure we have reached last vertex and coloured graph successfully 
            return(True)
        
        for colour in range(-k,0):    #-ve indicate colour **IMPORTANT**
            if isValid(i,colour):
                addColour(i,colour)   #Adding colour and extending solution from there
                extendSolution=ColoringGraph(i+1)
                if extendSolution:
                    return(True)
                removeColour(i)       #BackTracking part
        return(False)
                
    colourGraph=defaultdict(int)  #Creating dicrtionary to keep track of colour assigned to vertex
    for i in range(V):
        colourGraph[i]=0          #0-> indicate no colour assigned **IMPORTANT**
    return(ColoringGraph(0))      #1-> indicate there is an edge between two vertex 
    							  #-ve value -> indicate colour assigned to that vertex


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends
