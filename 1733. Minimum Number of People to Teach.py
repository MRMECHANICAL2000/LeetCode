"""   
Key :  You did not solve it in the challenge. it may seem like a tree problem at first but if
	   you look into the constrains it is said it has only 500 friends, languages and atmost 500
	   connections. so its not a tree/graph problem.
	   **IMPORTANT**
	   
"""

"""
Problem Name   : Minimum Number of People to Teach
Problem Url    : https://leetcode.com/problems/minimum-number-of-people-to-teach/
Solution Video : https://youtu.be/JKtjz1rurTE   **IMPORTANT** Must Watch

Learning:
	Brute:

		
	Better:


	Optimal: **IMPORTANT** **IMPORTANT**
		Approach -> at first keep the people ans lang they know in a hash table. then for each
					set of friends we check if there exist atleast one lang in common if not
					we need to teach any lang so that they can communicate. for all the friends
					who need a lang to communicate we create a lang hashTable and increment the
					language count there so the we can find the most famous lang there. so now
					we subtract the totalPeole we need to make contact with famous lang count
					so we will get the min people to teach the famous lang so that all people
					can communicate. watch video for clear understanding.


					Key: the key in
					question is you taugh you need to make all peole to speak to each other
					but in question they asked they need to make only the friends to speak 
					with each other

"""	

from collections import defaultdict
class Solution:
    def minimumTeachings(self, n, languages, friendships):
        HashTable={}
        for idx,val in enumerate(languages,1):
            HashTable[idx]=set(val)
        
        #friends to who we need to make communication
        frndsToConnect=set()
        for i in friendships:
            frnd1=i[0]
            frnd2=i[1]
            if HashTable[frnd1].intersection(HashTable[frnd2]):
                continue
            else:
                frndsToConnect.add(frnd1)
                frndsToConnect.add(frnd2)
                
        #Famous lang known by peole to be communicate
        langCount=defaultdict(int)
        for i in frndsToConnect:
            for j in HashTable[i]:
                langCount[j]+=1

        
        
        famousLang=max(*langCount.values(),0,0)
        ans=abs(len(frndsToConnect)-famousLang)
        return(ans)