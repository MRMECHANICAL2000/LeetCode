"""   
Key : this is an simple topological sort question, but learnt he Kahns algorithm which uses
      indegree for topological sort. today we see some questoin asked in google currently
      called compress 2d array which uses topological sort, but you did not understand how
      they use toposort there.
      **IMOPRTANT**
"""

"""
Problem Name   : Course Schedule II
Problem Url    : https://leetcode.com/problems/course-schedule-ii/
Solution Video : https://youtu.be/qe_pQCh09yU   -> Topological sort using DFS
                 https://youtu.be/tggiFvaxjrY   -> Topological sort using Kahns Algorithm

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT** **IMPORTANT**

        Approach 1-> using DFS+stack Topological sort
                     Take a node, do dfs from that node eventually you end the dfs in a node
                     from where you wont be able to go any where else, that is the course
                     which can be taken at last. so we put it in the stack, like we for
                     all nodes ones you have exasted visiting all its neighbour you add that
                     node to the stack. finally reverese the stack, you will get the topological
                     order.


        Approach 2-> using BFS+indegree topological sort (Kahns Algorithm)
                     this medthod is based on indegree of a node, the course that we can take
                     at first will have 0 indegree(no prerequestices). so we 1st take courses
                     which have 0 preRequestices, then we remove this courses form the graph,
                     now newly some courses will be created which also have 0 prerequetices
                     we then take that course.... finally the entire graph become empty, the 
                     order in which we have taken the course is topological sort. if the graph 
                     is not empty it means there is cycle in the graph


""" 

class Solution:
    #Kahns Algorithm for topological sort, BFS+queue/indegree metod
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashTable={}
        indegreeArray=[0 for i in range(numCourses)]
        for i in range(numCourses):
            hashTable[i]=[]

        for i in prerequisites:
            hashTable[i[1]].append(i[0])    #building adjList
            indegreeArray[i[0]]+=1          #Building Indegree Array **IMPORTANT**
        
        queue=[]
        for i in range(numCourses):
            if indegreeArray[i]==0:
                queue.append(i)
        
        for node in queue:
            for i in hashTable[node]:
                indegreeArray[i]-=1       #since we complete coure node, we decrease the 
                if indegreeArray[i]==0:   #preRequestics of all other nodes, if while decreasing
                    queue.append(i)       #preRequestics we get 0 indegree for that node we add
                                          #back to the queue. **IMOPRTANT**
        return(queue if len(queue)==numCourses else [])
        
        

    #Topological Sort. DFS+stack Method
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashTable={}
        visited=[0 for i in range(numCourses)] #building Visited Array
        for i in range(numCourses):
            hashTable[i]=[]
        for i in prerequisites:
            hashTable[i[1]].append(i[0])    #building adjList
            
        stack=[]                    #this stack contains the course toposort
        def topoSort(vertex):      
            if visited[vertex]==1:
                return(False)
            if visited[vertex]==2:
                return(True)

            visited[vertex]=1
            for i in hashTable[vertex]:
                if topoSort(i)==False:
                    return(False)
            
            stack.append(vertex)  #After exast visiting all the neighbour we append it to stack
            visited[vertex]=2     #**IMPORTANT**
            return(True)
        
        for i in range(numCourses):
            if visited[i]==0:
                noCycle=topoSort(i)
                if noCycle==False:
                    return([])
        return(stack[::-1])     #reverse the stack you will get the Topological Sort Order
        