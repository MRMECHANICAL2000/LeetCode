"""
Key : This question has small twist from that of merge sort inversion question.
      using HashTable to store the inversion of each element leads to wrong answere due to duplicates 
      in array and TLE since we need to update lot of range of array at same time. to avoid confusing
      with duplicates we use enumeretae() and convert all element into (idx,element) and do our work. 
      but TLE cant be avoided since you take element from 2nd array and increment one count for all 
      element in 1st array. just think different there. total inversion that element in left array can 
      make is len(rightArray)-curRightElementIdx which is smaller than leftArray currentElement.
      look the explanation you will understand it. **IMPROTANT**
      **IMPORTANT**
"""
"""
Problem Name   : Count of Smaller Numbers After Self
Problem Url    : https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Solution Video : https://youtu.be/owZhw-A0yWE

Learning:
	Brute: 
        using two loops and counting all the inversion. O(N^2)

    Better: **IMPORTANT** just remember this approach exists.
        create an temp array. iterate the given array and insert it from last. if temp array is empty
        insert it. if it has element loop from back side and insert the curElement to the place where it
        will be when the array is sorted.no of jumps we took from back for inserting it is the total
        inversion that is possible by that number.

        5,2,4,1 -> i=""  arr=[]         invCount=0
                   i=5   arr=[5]        invCount=0   #5 do not contribute for any inversion (0 jump)
                   i=2   arr=[2,5]      invCount=1   #2 can make one inversion with 5   (1 jump)
                   i=4   arr=[2,4.5]    invCount=2   #4 can make one inversion with 5   (1 jump)
                   i=1   arr=[1,2,4,5]  invCount=5   #1 can make 3 inversion with 2,4,5 (3 jump)

        this approach also takes O(N^2) time in worst case when the given array is sorted in 
        decending order.

	Optimal: **IMPORTANT**
		Approach 1 -> using Merge Sort,just counting inverion means its easy but we need to count and
                      say inversin for each element. the optimal way is in merge step when you find

                      leftArray=[5,6,7]    rightArray=[2,3,1]    
                                 i                     j       
                      when comparing this i,j usually if j<i means we say 2 can make inversion with
                      all element after 5. ie,5,3,1. this is how we usually think but to solve this 
                      question you need to think a bit different. note that if i=5 is > j=2 it means i=5
                      is greater than rest of all element in j. so i can make a total of 3 inversion.
                      usually we sort the array in accending order to make this approach work you need 
                      to sort it in decending order. just have an array/HashTable and initialize it with
                      0 for all element. each time you find inversion count increment the prevCount in
                      the array or hashTable. but the problem comes when the array has duplicates.if 
                      there were two 5 in the array our count will get wrong, to identify each element 
                      uniquely we make all element as [(0,5),(1,6),(2,5),(3,7)]-> (idx,element) using
                      python enumerate function.then do our work of merge sort by comparing each element
                      when we find inversion we increase the count of their idx. 

        Approach 2 -> using Binary Indexed Tree. O(Nlog N) time. (Have not implemented yet)
        Appraoch 3 -> using Fenwick Tree. O(N) time.  (Have not implemented yet)

"""	
class Solution:
	#Optimal
    def countSmaller(self, nums: List[int]) -> List[int]:

        def mergeSubroutine(l1,l2):  #Merge Subroutine
            inversion=0
            mergedList=[]
            l1_index=0
            l2_index=0
            while len(l1)>l1_index and len(l2)>l2_index:
                if l1[l1_index][1]<=l2[l2_index][1]:
                    mergedList.append(l2[l2_index])
                    l2_index+=1
                else:
                    inversionArray[l1[l1_index][0]]+=len(l2)-l2_index   #**IMPORTATN** counting step
                                                                    #understand throughly other than 
                                                                    #this step everything is ordinay
                                                                    #inversion question only **IMPORTANT**
                    inversion+=len(l1)-l1_index
                    mergedList.append(l1[l1_index])
                    l1_index+=1
                    
            if len(l1)==l1_index:
                mergedList.extend(l2[l2_index:])
            else:
                mergedList.extend(l1[l1_index:])
            return(mergedList,inversion)


        def countInversions(arr):         #Split Subroutine
            if len(arr)==1 or len(arr)==0:
                return(arr,0)

            j=len(arr)//2

            leftList,leftInversion=countInversions(arr[:j])
            rightList,rightInversion=countInversions(arr[j:])
            sortedList,splitInversion=mergeSubroutine(leftList,rightList)

            return(sortedList,leftInversion+rightInversion+splitInversion)


                                                     #**IMPORTANT**
        arr=list(enumerate(nums))                    #enumerating input array to avoid duplicate
        inversionArray=[0 for i in range(len(arr))]  #creating inversion array
        countInversions(arr)[1]                      #calling inversion function
        return(inversionArray)                       #returning inversion array
