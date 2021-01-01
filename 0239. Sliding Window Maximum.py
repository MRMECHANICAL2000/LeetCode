"""   
Key : Learn the optimal approach throughly, must watch the video. in optimal appraoch look all
	  points in the code. 

"""

"""
Problem Name   : Sliding Window Maximum 
Problem Url    : https://leetcode.com/problems/sliding-window-maximum/
Solution Video : https://youtu.be/TCHSXAu5pls
				 **IMPORTANT** Must watch the video to know about sliding window medthod **IMPORTATN**  
                 

Learning:
	Brute:
		for each window , find max element by linear search.
		
	Better:
		using heap, store window in heap. if window increase reomve 1 elelment and add 1 element takes
		O(logn) time for both. we will get max in constant time.
		**IMPORTANT** **IMPORTANT**
		heap are also known as priority queues so only called as heap queue ->heapq library
		by default heapq is minHeap , if you want maxheap just while putting all element put 
		-1*element so that element we get will be of max heap element. even if our array contains -ve 
		values it works. think twise to understand clearely.

	Optimal: **IMPORTANT** 
		Approach -> Using deque, at firt we store all element that are after 1st greater element in 1st
					sliding window into deque. then we loop from k element to end of list. if the deque
					is empty we append current index we last element of deque is >= curVal we append 
					curVal to end.if deque[-1]<curVal to insert element now we need to pop element from
					end until deque is empty of we find an index where deque[-1]>=curVal, then we append
					the curVal to the deque. our goal is to maintain max value at the left side of the
					deque. In all place we use Index we append Index only then only we can avoid 
					duplicate and easily know which elelmet to pop and push		
"""	



from collections import deque
class Solution:
	#Optimal Solution

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    												#**IMPORTANT**
        deq=deque()   								#We store index in this deque not value, 
        											#then only we can avoid duplicate and
        											#easily know which elelmet to pop and push
        ans=[]
        
        #storing only element after 1st greater element **IMPORTANT** watch video to understand
        for idx,val in enumerate(nums[:k]):
            if len(deq)==0: 						 
                deq.append(idx)	   					 #**IMPORTANT**
            elif nums[deq[-1]]>=val:                 #In deque no slicing but indexing is possible
                deq.append(idx)
            elif nums[deq[-1]]<val:
                while deq and nums[deq[-1]]<val:
                    deq.pop()
                deq.append(idx)
  
        popIdx=0                                    #Index of element to be poped in each slicing
        ans.append(nums[deq[0]]) 

        #Moving window
        for idx,val in enumerate(nums[k:],k):        #**IMPORTANT**
            if deq[0]==popIdx:                       #if max is element index to be poped pop it. 
                deq.popleft()

            if len(deq)==0:							 #if no element in deq append cur element
                deq.append(idx)

            elif nums[deq[-1]]>=val: 	 #if last element in deque is greater just append val to last
                deq.append(idx)          #">=" we must check >= its Very Very **IMPORTNAT***

                						 #**IMPORTANT**
            elif nums[deq[-1]]<val:      #if last element is lesser then we pop from back until we reach
            							 #an element > than val or deq empty. than append val to end.
                while deq and nums[deq[-1]]<val:
                    deq.pop()
                deq.append(idx)

            popIdx+=1
            ans.append(nums[deq[0]])    #Appending solution

        return(ans)
                
       