"""   
Key : 
	  **IMOPRTANT**
"""

"""
Problem Name   : Find Median from Data Stream
Problem Url    : https://leetcode.com/problems/find-median-from-data-stream/
Solution Video :                  

Learning:
	Brute: **IMPORTANT**
		have an sorted array each time , insert the element using binary search, inserting
		in array takes O(N) time in array.even if you use bisect.insort() it gonna use
		same time only. so it takes O(N*m) for inserting m numbers. ie, O(N^2)
		
	Better: **IMPORTANT**

		
	Optimal: **IMPORTANT** **IMPORTANT** **IMPORTANT**
		Approach -> using two heaps one to store 0 to n//2 element and other to store
					n//2 to n element. here leftHeap is maxHeap returns  the max element
					in the left array and right heap in minHeap returns the min element in
					the right array. the median is either maxelment in leftheap or minele
					in rightHeap. or their average. we should need to main the heap 
					structure always such a way the number of element such a way that
					abs(leftLen-rightLen)<=1 to get the median in constant time.

"""	

import heapq
class MedianFinder:
    #You should need to update length each time , when you push, pop, 
    #while balancing ,after balencing  **IMPORTANT** **IMPORTANT**
    def __init__(self):
        self.leftHeap=[]
        self.leftLength=0
        self.rightHeap=[]
        self.rightLength=0
        #leftHeap -> max heap always return the max element
        #rightHeap -> min heap always return the min element

    def updateLen(self):
        self.leftLength=len(self.leftHeap)
        self.rightLength=len(self.rightHeap)
        
    def balance(self):
        self.updateLen()
        while abs(self.leftLength-self.rightLength)>1:
            if self.leftLength>self.rightLength:
                pop=-heapq.heappop(self.leftHeap)
                heapq.heappush(self.rightHeap,pop)
            else:
                pop=-heapq.heappop(self.rightHeap)
                heapq.heappush(self.leftHeap,pop)
            self.updateLen()
        self.updateLen()
        
    def addNum(self, num: int) -> None:
        if self.leftLength==0:
            heapq.heappush(self.leftHeap,-num)
        else:
            if -self.leftHeap[0]>=num:
                heapq.heappush(self.leftHeap,-num)
            else:
                heapq.heappush(self.rightHeap,num)
        self.balance()

    def findMedian(self) -> float:
        if self.leftLength==self.rightLength:
            return((-self.leftHeap[0]+self.rightHeap[0])/2)
        elif self.leftLength<self.rightLength:
            return(self.rightHeap[0])
        else:
            return(-self.leftHeap[0])




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()