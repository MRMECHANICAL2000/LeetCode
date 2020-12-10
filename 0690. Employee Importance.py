"""   
Key : the key is to use hashtable to find employee detail in O(1) time and either use DFS or BFS to
	  get the value of next employees
"""

"""
Problem Name   : Employee Importance
Problem Url    : https://leetcode.com/problems/employee-importance/
Solution Video :   
                 

Learning:
	Better:
		using DFS but takes more time and space than optimal approach

	Optimal: 
		Approach -> Breadth Firsts Search using Stack
					its not mentioned that employee with id 5 will be in 5th position.they can be of any 
					order.to get employee 5 details you cant look at 5th index. you need  traverse the 
					entire array find that employee positon then proceed by adding his importnace to ans
					and appending his subordinates to stack. 		
"""	


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
	#Better Solution
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        HashTable={}
        for i in employees:
            HashTable[i.id]=[i.importance,i.subordinates]
        
        def dfs(empId):     #DFS
            imp,drct=HashTable[empId]
            return(imp+sum([dfs(i) for i in drct]))
        return(dfs(id))     #Dont forget to start the dfs by calling the dfs function **IMPORTANT**
        					#dont just write dfs function forget to call it like a duplicate coder

	#Optimal Solution
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        HashTable={}
        for i in employees:
            HashTable[i.id]=[i.importance,i.subordinates]

        stack=[id]            #BFS
        ans=0
        while stack:
            imp,drct=HashTable[stack.pop()]
            ans+=imp
            stack+=drct
        return(ans)