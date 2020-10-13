"""
Key : if the interviewer ask to delete the node from Memory use python del() function **IMPORTANT**
"""

"""
Problem Name   : Delete a given Node when a node is given
Problem Url    : https://leetcode.com/problems/delete-node-in-a-linked-list/
Solution Video : https://youtu.be/icnp4FJdZ_c 

Learning:
	Brute: 
		Thinking how to do it?, you can't delete a node without prev_node.

	Optimal: **IMPORTAT**
		Approach -> just swap value from next node to given node and change in pointer of given node to
					next nodes next node. it seems like we have deleted it.
"""	

class Solution:
	#Optimal
    def deleteNode(self, node):
        node.val=node.next.val
        temp=node.next
        node.next=node.next.next
        del(temp)                 #**IMPORTANT** if the interviewer asked us to delete the Node from
        						  #Computer Memory. even if he did not ask do it by saying optimal way. 