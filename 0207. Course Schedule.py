"""   
Key : detecting cycle in directed graph.
"""

"""
Problem Name   : Course Schedule
Problem Url    : https://leetcode.com/problems/course-schedule/
Solution Video : https://youtu.be/0dJmTuMrUZM ->using DFS recursive Method
                 https://youtu.be/bGkiHe5QpO4 ->using BFS indegree Method **IMPORTANT** **IMPORTANT**
                 **IMPORTANT** Must watch the indegree Method **IMPORTANT**

Learning:
    Brute:        
        
    Better:
        
    Optimal: **IMPORTANT**
        Approach 1-> convert the given prequesties into an adjList, if you find cycle in this 
                    graph it means you cant take all the courses, else you can take all the courses
                    use DFS(recursive) method to sovle this question. go to a node put 1 if you
                    are curretnly visiting it ,recurse on all its neighour if you comple visiting
                    a node and all its neighbour put 2 in visited array. while visting if you find
                    1 in a node it means there is a cycle return False.
                    make sure to do dfs from all nodes because may be the graph coud be unconnected
                    having many islands

                    #0->not Visited
                    #1->Actively Visiting
                    #2->alredy visited and has no cycle

                    **IMPORTANT** **IMPORTANT** **IMPORTANT**
        Approach 2-> BFS this method is called indegree method. if you use plain BFS you will 
                     fail here   1->2<-3 , this graph has no cycly but if you do BFS from 1 then
                     from 3 you will visit 2 twise and bfs says its a cycle. we do indegree aproach

                     indegree means no of incomming edges for an node. here we initially count
                     the number of incomming edges of each node and store it in indegree variable
                     if there is an node with 0 indegree it means that node do not contribute
                     to any cycle , so we remove that node and all the outgoing edges of that
                     node. now we check if the graph has any node with 0 indegree... we continue
                     doing it at last we see if there were any node with indegree !=0 if such
                     a node exist there is a cycle in this graph.look video for clear understanding

""" 
class Solution:
    #Optimal Approach 1 ->bfs (Indegree)    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Using BFS
        adjListRep={}
        indegree={}
        for i in range(0,numCourses):
            adjListRep[i]=[]
            indegree[i]=0
            
        #Making an adj list repsentation of given preRequesties
        for preReq in prerequisites:
            indegree[preReq[0]]+=1
            adjListRep[preReq[1]].append(preReq[0]) #counting the indegree **IMPORTANT**
        
        queue=[i for i in indegree if indegree[i]==0] #storing node which has indegree 0 **IMPORTANT**
        while queue:
            node=queue.pop()
            for i in adjListRep[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        return(not any(indegree.values()))
        


    #Optimal Approach 1 ->dfs (Recursive)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjListRep={}
        for i in range(0,numCourses):
            adjListRep[i]=[]
            
        #Making an adj list repsentation of given preRequesties
        for preReq in prerequisites:
            adjListRep[preReq[1]].append(preReq[0])
        
        #Visited array to store wheather we have visited that node
        Visited=[False for i in range(0,numCourses)]            

        for i in range(0,numCourses):
            def dfs(node):
                if Visited[node]==1:
                    return(False)
                if Visited[node]==2:
                    return(True)
                Visited[node]=1
                for i in adjListRep[node]:
                    result=dfs(i)
                    if not result:
                        return(False)
                Visited[node]=2
                return(True)
            
            if not dfs(i):
                return(False)
                
        return(True)

