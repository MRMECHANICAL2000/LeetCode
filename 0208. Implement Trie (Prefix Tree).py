"""   
Key : Tries are also know as prefix tree . tries are used to efficiently search for keys starting 
	  with a specific prefix. see how its implemented easly by other coders. a good coder can implement 
	  an logic in a simple way.
	  **IMPORTANT**
"""

"""
Problem Name   : Implement Trie (Prefix Tree)
Problem Url    : https://leetcode.com/problems/implement-trie-prefix-tree/
Solution Video : https://www.youtube.com/watch?v=xqsaAhQC6c8
                 

Learning:
	Brute: 
		
	Better: 

	Optimal: **IMPORTANT**
		Approach -> efficient way to implement is to use seperate class to create node. in which we
					have an hash table which has key=char and val=that char node. and any required thing
					can be inserted here like count,endshere to check no of variable having same prefix
					and to check if an word ends here. in trie class we only have pointer to head node alone.

"""	

#you need seperate node class and trie class should only contain pointer to head node.

class TrieNode:
	#def __init__(self,val=None,child={}): #No need of complex thinking, when you can do it simply
    def __init__(self):
        #self.val=val       #No need to store the val think twise to understand
        #self.child=child   #no need of using extra variable child. **IMPORTANT**
        self.child={}
        self.endsHear=False
        
class Trie:

    def __init__(self):
        self.head=TrieNode()
        #**IMPORTNAT**
        #we need to have seperate class to create node and in Trie class we only have
        #link to head node. dont think like crap and store node date also here
        

    def insert(self, word: str) -> None:   #Inserting word into trie
    	#**IMPORTANT**
    	#see if the char is in temp child, it there point the temp to that child if not there
    	#create a new node and point the temp to that place.
        temp=self.head
        for i in word:
        	#My Taught, making lot of complex stuff to create same logic
            """
            if i in temp.child:
                temp=temp.child[i]
            else:
                newNode=TrieNode(i)
                temp.child[i]=newNode
                temp=newNode
            """
            #CP Taught, same logic and simple code **IMPORTANT**
            if i not in temp.child:
                temp.child[i]=TrieNode()
            temp=temp.child[i]
        temp.endsHear=True
        

    def search(self, word: str) -> bool:          #Returns if the word is in the trie.
        temp=self.head
        for i in word:
            if i not in temp.child:
                return(False)
            temp=temp.child[i]
        
        #My code to return if word ends here   
        """
        if temp.endsHear==True:
            return(True)
        return(False)
        """
        #Cp programmer code
        return(temp.endsHear)

    def startsWith(self, prefix: str) -> bool:         #Returns if there is any word in the trie 
    												   #that starts with the given prefix.
        temp=self.head
        for i in prefix:
            if i not in temp.child:
                return(False)
            temp=temp.child[i]
        return(True)
        #same as search but instead of checking if endsHere==True we return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
