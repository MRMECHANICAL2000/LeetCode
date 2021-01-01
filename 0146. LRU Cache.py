"""   
Key : Must see the entire code, you made lot of mistke in implementing the doubley linked list and node
      creation also so observe the code properly.
      LRU is an Page replacement algoritm used in  Operating System. Must watch the full video to know
      about the paging concept in operating system. watch the entire play list.

      https://youtu.be/pJ6qrCB8pDw 
      **IMPORTANT** **IMPORTANT** **IMPORTANT**

Question Raised by ECE Topper?
why cant you use priority queue? priority queue. The list is so created so that the highest priority 
element is always at the head of the list. but it wont follow the FIFO like how normal queue do. 
Priority queue are implemented commonly as heap with highest prioority element at top. but it will take
logN time to insert and remove top element but you cant evice Least reasently used element. because we
dont know where it is. it can be any where in the leaf node.

we can repsent an binary tree in a array form. where left child in i*2'th index and right child in 
i*2+1'th index and parent of each node at floor(i/2) th index. we need to store each element in this 
index properly. if its an complete binay tree we can store element in level by level they will obey the
above index position. if its not an complete binary tree you cant sore level by level , because you 
need to insert some gap in the array . so we put element in ith index then its child in i*2 and i*2+1'th
 index. see the below video to understand.

there are two type of binary tree, a binary tree in which all possible node of all levels are fileed is
full binary tree. a binary tree in which h-1 level is a full binary tree and last h'th level nodes as 
from Left to right side is known as complete binary tree. heap can only be created with an complete 
binary tree. 
""" 

"""
Problem Name   : LRU Cache
Problem Url    : https://leetcode.com/problems/lru-cache/
Solution Video : https://youtu.be/S6IfqDXWa10 #how to solve the question Intution

                 https://youtu.be/HqPJF2L5h9U
				 **IMPORTANT** Must watch the video to know why cant we use priority Queue **IMPORTANT**
                 
Learning:
	Brute:
        just using an array, each time an element is given or searched, we check the list O(n), delete
        from its position O(n) and insert to front O(n). if memory full pop last element. O(1).
        total time complexity O(n^3) and O(N) space for array alone.


	Optimal: **IMPORTANT**
		Approach -> use an doubly linked list to store element. so now to insert in front or pop back or
                    delete from center all takes O(1) operation alone but to check if an element present
                    or not we need to traverse entire linked list, which takes O(n) time. to avoid this
                    we use an hashtable. we store the key and address of node there. so if we need to
                    search an element we just need to check in hashtable in O(1) time find its position
                    and do other opration. here all operations can be done in O(1) time. but we use
                    space for hash table and doubly linked list.
"""	

class Node: #No need to keep it as nested class **IMPORTNAT**
    def __init__(self,key=None,val=None,prev=None,nxt=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.nxt=nxt

class LRUCache:    
    def __init__(self, capacity):
        self.HashTable={}
                                #**IMPORTANT**
                                #calling the node calss dont confuse here by thinking we should need to 
                                #use self or nested node class
        self.head=Node(0,0)     #in an doubly linkedlist you should not store the data in head or tail 
        self.tail=Node(0,0)     #node, even if there is no data head and tail node will reamain, if data
                                # comes it is inserted bw them.dont think like stupid and put same node 
                                #as head and tail and add value to it. use no of values in hashtable to 
                                #check capacity not double
                                
        self.head.nxt=self.tail  #**IMPORTANT**
        self.tail.prev=self.head #1st know how to create doubly linkedlist in correct way, must not 
                                 #use head and tail node to store data ,head and tail should need to be 
                                 #pointed to each other
        self.capacity=capacity
    
    def EvictRight(self):
        temp=self.tail.prev
        key=temp.key
        #print("EvictKey",key,self.head.key,self.tail.key)
        temp.prev.nxt=self.tail
        self.tail.prev=temp.prev
        del(self.HashTable[key])
        
    def appendLeft(self,key,val):
        #print("AppendKey",key,val)
        newNode=Node(key,val)
        temp=self.head.nxt
        self.head.nxt=newNode
        newNode.prev=self.head
        newNode.nxt=temp
        temp.prev=newNode
        self.HashTable[key]=newNode
    
    def delKey(self,key):
        #print("deletekey",key)
        temp=self.HashTable[key]
        prevNode=temp.prev
        nxtNode=temp.nxt
        #if prevNode!=None: #improper implementation of doublyLL leads to unwanted checking of none
        prevNode.nxt=nxtNode
        #if nxtNode!=None:
        nxtNode.prev=prevNode
        del(self.HashTable[key])


    #only get and put function asked in question all other things we do for out advantages        
    def get(self, key):
        #print(key,self.HashTable)
        try:
            val=self.HashTable[key].val
            self.delKey(key)
            self.appendLeft(key,val)
            return(val)
        except:
            return(-1)
        

    def put(self, key, val):
        if key in self.HashTable: #To make sure no duplicate key is inserted
            self.delKey(key)
        self.appendLeft(key,val)
        if len(self.HashTable)>self.capacity:
            self.EvictRight()
            
        #print(self.capacity,self.head.key,self.tail.key)
        #print(self.HashTable)
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)