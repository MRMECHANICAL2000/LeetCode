"""   
Key : You dont need two heap for it, kth largest element only required always you just need the 
      heap to store right side , no need of left side heap which we use for median
    
      in question they are asking us to find the kth largest element so it should be min heap 
      which are using we need to to have only k element in our min heap and each time they ask 
      we return the min element which will be kth largest element.this is simple question but 
      you complicated it beecause you did not even clearely know correct understanding of kth 
      largest and kth element

	  **IMOPRTANT** **IMOPRTANT** **IMOPRTANT**
"""

"""
Problem Name   : Kth Largest Element in a Stream
Problem Url    : https://leetcode.com/problems/kth-largest-element-in-a-stream/
Solution Video :                  

Learning:
	Brute: 
		
	Better:
		
	Optimal: **IMPORTANT**
		Approach -> simple min heap question but you need more knowledge to identify that
					its an min heap questoin. you are putting two heaps and maintaing one
					heap with size k other with remaining .... very bad thinking process.

"""	

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.minHeap=nums
        heapq.heapify(self.minHeap)

    def balance(self):
        while len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
           
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        self.balance()
        return(self.minHeap[0])


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)