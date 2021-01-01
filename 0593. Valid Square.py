"""
Key : You just need to know the property of squar to solve this question. but you dont even got this
      taught process. for square all 4 sides are equal but even an rombous has 4 sides equal how to
      differenciate them? square has other property also ie, 2 diagnoal of square is also equal of equal
      length.
      Edge case what if 2 points in same coordinte, if 2 points in same coordinate then distance between
      them is zero. use this to over come this edge case.
      **IMPORTANT**
"""

"""
Problem Name   : Valid Square
Problem Url    : https://leetcode.com/problems/valid-square/submissions/
Solution Video : https://youtu.be/x92xdjEmesY
                 **IMPORTANT** 

Learning:
    Brute: 
        
    Better:

    Optimal: **IMPORTAT**
        Approach -> find the distance for all points and store it in hashMap if the are only 2 different
                    distance (because square has only 2 differnt distance side and diagonal) and no of
                    times this 2 distance found are 4,2 (4 for sides and 2 for diagonal) then the given
                    points forms an square.
                    But there is an edge case here if the points are in same coordinate also the program
                    says it can form square? just check if any distance is 0,return false if any distance
                    between points is zero.
                    **IMPORTANT**

""" 

class Solution:
    #Better Approach
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        """
        temp=set()  #To make sure we cover This corner case [0,0] [1,1] [0,0] [1,1] 
                    #if two points are in same place then also our code return True 
        for i in [p1,p2,p3,p4]:
            temp.add(tuple(i))

        if len(temp)<4:
            return(False)  
        """
        HashTable={}
        def distance(A,B):                          #^->means XOR not Power **->only means power **IMPORTANT**
            val=(A[0]-B[0])**2 + (A[1]-B[1])**2
            return(math.sqrt(val))
        
        for i in combinations((p1,p2,p3,p4),2):
            d=distance(i[0],i[1])
            if d in HashTable:
                HashTable[d]+=1         #instead of storing the points just store no of times the **IMPORTANT** 
                                        #distance d has occured , so at last calculation will be easy
            else:
                HashTable[d]=1

        if len(HashTable)==2 and 2 in HashTable.values() and 4 in HashTable.values() 
            and 0 not in HashTable.keys():#condition to overcome points on same position.

            return(True)
        
        return(False)
