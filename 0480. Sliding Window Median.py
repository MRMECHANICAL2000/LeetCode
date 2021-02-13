"""   
Key : look at this sortedcontainer in python , but most online idea did not have it pre installed. 
	  https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/
	  watch carefully how we are taking the median of an array. 

	  read the bisect module in python carefully there is an method called bisect insort
	  in python. it insert the insert in sorted array and return the sorted array. used in 
	  this question
	  https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
	  **IMOPRTANT**
"""

"""
Problem Name   : Sliding Window Median
Problem Url    : https://leetcode.com/problems/sliding-window-median/
Solution Video :                  

Learning:
	Brute: **IMPORTANT**
		create an window of size k , sort it and return the median , find the element while
		sliding to remove it and  add new element using bisect. everything is good but finding
		and removing the element takes O(K) operation so total O(n*k) operation each time you
		may say O(n*(k+logk)) but we can eliminate the logK value. dont say it as O(n^2) or 
		O(n*k*logk) like fool does. **IMPORTANT**
		
	Better: **IMPORTANT**
		using two heaps like how we do in median of running integers question. we make the
		window into two heaps and slide it over.store median each time. takes O(n*(logk+logk))
		for adding , removing and finding median. so O(nlogk) runtime.
		
	Optimal: **IMPORTANT** **IMPORTANT** **IMPORTANT**
		Approach -> the optimal approach is by using balanced Trees, balanced trees has O(logk)
					runtime for insersion and delition. in python there is an container called
					sortedcontainers and it has one datastructure called SortedList. this data
					structure maintains the list in sorted fashion and takes O(logn) time for 
					both insersion and deletion. its implementaion is based on AVL/RB trees.

					but this library is not available always in all ides. so go with heap
					approach or implement AVL/RB trees yourself.

"""	

from sortedcontainers import SortedList
import bisect
class Solution:
    def median(self,array):
        if len(array)%2!=0:
            return(array[len(array)//2])
        else:
            return((array[len(array)//2-1]+array[len(array)//2])/2)
        #Median index in array is **IMPORTANT** **IMPORTANT** **IMPORTANT** **IMPORTANT**
        #for odd len(array)//2 not len(array)//2+1
        #for even (len(array)//2)+(len(array)//2-1) not (len(array)//2)+(len(array)//2+1)
        #think carefully , you dont even know length-1 is the indexing and you calculating
        #the median like a crap
        
    #Optimal Approach - using SortedList(AVL,RB Balanced Trees)
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        #Approach using SortedList() ie, balanced binary search tree in python **IMPORTANT**
        ans=[]
        window=SortedList(nums[:k])      #Balanced BST
        ans.append(self.median(window))
        idx=0
        for i in range(k,len(nums)):
            window.remove(nums[idx])
            window.add(nums[i])       #.add(), .remove()
            ans.append(self.median(window))
            idx+=1
        return(ans)

      #Brute -> using binarySearch O(n*k)
      def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans=[]
        window=nums[:k]
        window.sort()
        ans.append(self.median(window))
        idx=0
        for i in range(k,len(nums)):  #O(n)
            window.remove(nums[idx])   #O(k)
            bisect.insort(window,nums[i])
            ans.append(self.median(window))
            idx+=1
        return(ans)