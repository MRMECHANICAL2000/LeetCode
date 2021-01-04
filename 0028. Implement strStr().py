"""    
Key : Must Must Must watch all 5 videos from naive to most optimal pattern algorithm and comparision of 
	  them in wiki page.
	  **IMPORTNAT**

	  '''What should we return when needle is an empty string? This is a great question to ask 
	  during an interview.For the purpose of this problem, we will return 0 when needle is an 
	  empty string. This is consistent to C's strstr() and Java's indexOf().''' -> statement given in 
	  the question. 
	  In this problem we are looking how this inbuild function strStr() is implemented in C language for
	  finding the index of matched pattern in string. in python its implemented using Boyer-Moore. its
	  just small improvement over naive brute force method. most programming library uses naive brute 
	  force method (c,java)
""" 

"""
Problem Name   : Implement strStr()
Problem Url    : https://leetcode.com/problems/implement-strstr/
Solution Video : 
				 **IMPORTANT**v.v.v.v Must watch all video question**IMPORTANT**
				 https://youtu.be/nK7SLhXcqRo -> Naive Pattern Matching Algorithm
				 https://youtu.be/4Xyhb72LCX4 -> Boyer-Moore
				 https://youtu.be/qQ8vS2btsxI -> Rabin Karp
				 https://youtu.be/V5-7GzOfADQ -> KMP
				 https://youtu.be/CpZh4eF8QBw -> Z-Function/Prefix Function(Extension of KMP)
				 https://en.wikipedia.org/wiki/String-searching_algorithm -> Comparing all their speed							  

Learning:
	Brute: **IMPORTANT** **IMPORTANT**
		searching naivly , take 1st char of pattern go search entire string if same char found from
		there search for 2nd char. O(N^2)
		
	Better: **IMPORTANT** **IMPORTANT**
		using python inbuild .find() function, which uses a mix between Boyer-More
		and Horspool. The time complexity is O(N) on average, O(NM) worst case .
		Most Inbuild algorithm in web,computer are Boyer-More Algoritm only.
		The Boyer–Moore string-search algorithm has been the standard benchmark for the 
		practical string-search literature

	Optimal: **IMPORTANT** **IMPORTANT**
	  Approach 1 -> using Rabin Karp (Rolling Hash Function), Takes O(n+m) time and O(1) no extra space.
	  				1st we hash the pattern , then we take a window of size pattern and slide over
					the string, each time we hash the window and compare the hash value to pattern  
					if both are same  then we will compare the window and pattern if they are match.
					if we use some inefficient hash function then then fuction shows more window 
					value is matching with pattern and we check all of them most of then will be 
					different only, this pocess of comparing unwanted strings are known as spurious hits.

					Rabin Karp  wrote an algorithm that does this hashing efficiently.

					just take total no of strings (if we take entire letters in keyborad its 127) but for
					this question its 26(the string only has lower case numbers). the way we hash it is

					aksc =>  0*(pow(26,3)) + 10*(pow(26,2)) + 18*(pow(26,1)) + 2*(pow(26,0))
						   		thousands		hundreds 		tens			ones		

						for idx 0, [ord('a')-ord['a']]*pow(26,3) -> ..........			    
						for idx 1, [ord('k')-ord['a']]*pow(26,2) -> ...........	    
						for idx 2, [ord('s')-ord['a']]*pow(26,1) -> pow(1) to get tens term
						for idx 3, [ord('c')-ord['a']]*pow(26,0) -> pow(0) to get ones term 
						
						ie, [ord(char)-ord['a']]*pow(lenOfTotalPossibleCharacter,len(string)-idx-1)
					[ord(char)-ord['a']] -> then only we will get its position out of 26 characters

					if we use this match hashWindow and hashPattern will be same Iff they both have
					exactly same character at same position. ie,if hashCode become same we return 
					that string no need to check wheather they are same again. chances of getting furious
					hits are low here.

					Hashing the pattern is ok but in each iteration the window will change if we do hashing
					of window again and agin it will lead to N^2 solution what to do. for that also Rabin 
					karp introduced an method in his algorithm known as Rolling Hash. while moving window 
					we will be adding one elemnet at right and pop one element from left. just sub the pop
					element value from previous hash and add new element value to it to get current has 
					instead of calculating it again. but **IMPORTANT**

					'abc'defghijk              ->  a'bcd'efghijk              |sliding window ones 
					a(26**2)+b(26**1)+c(26**0) ->  b(26**2)+c(26**1)+d(26**0) |Required power's

					what we get after subtracting a(26**2) -> b(26**1)+c(26**0)
					for b pow need to be 2 for c power need to be 1 for that just multiplay with 26**1
					and add new element at end

					=>   b(26**2)+c(26**1)+d(26**0) we will get this , this pocess is known as rolling 
					hash function

					each time if you do power calculation you will end up with time limit exceed error
					so do like this,
					HashVal==HashVal*26+NewValToAdd    **IMPORTANT** Think twise and look the code
																	 you will understand this

	  Approach 2 -> Using Knuth-Morris-Pratt KMP String Matching Algorithm, Takes O(N) time & O(m) space.
	  				Aho–Corasick string matching algorithm (extension of Knuth-Morris-Pratt)
	   				linear traversal through string and m space to create patterns Longest Prefix suffix.
	  				In naive approach author found that we traverse through some distance when the pattern
	  				match if it stops matching we back track both string pointer and pattern pointer to 
	  				starting position because there may be a chance that from some other position the pattern 
	  				may match

	  				string  -> "aabaaabaaac" = "a a b a a a b a a a c "
												0 1 2 3 4 5 6 7 8 9 10

					pattern -> "aabaaac"     = "a a b a a a c"
												0 1 2 3 4 5 6

					In naive approach, strIdx =0 , patrnIdx=0 we compare both since same we increment
					we move both strIdx,patrnIdx until index 6 at six we find a mismatch so we 
					backtrack strIdx=1 ,patrnIdx=0 then start to compare becaue in betweern 0 to 6 
					there may be a chance that pattern matach start point will be there. ie. 4 to 10. so
					only naive approach takes O(N*m) time.

					The Author taught of this and realize the chances of having pattern starts inbetween
					already matched index is when there is any repeating character in pattern. ie, if there
					is any prefix in pattern that got repeated again somewhere in between the string.
					for the above example the prefix "aa" got repeated at index 3,4 and 4,5 so only the
					are chances that our string may start some where in between the already visited index
					in string. so the author give an idea that why we back track string just store at 
					which position this suffix are same and while traversing just check if it is possible to
					expand from that suffix. look video to get clear understanding. our is to not back
					track the string it is to trace back only the pattern only on required time alone.

					here we create a LPS table(LPS table size is +1 bigger than pattern size because we
					put a 0 at first additionaly). keep start=0 and curIdx=1, if both match 
					increment both idx and store start+1 in LPS because start=0 means start+1 =1 we 
					have matched 1st perfix start=1 , start+1=2 , we have matched 2nd prefix .... 
					if they do not match we check and start!=0 means there is a chance that a prefix 
					may repeat here so we trace back we trace back to LPS[start]


					0 1 2 3 4 5  6 7  -> LPS Array Indexing 
					  0 1 2 3 4  5 6  -> pattern Indexing
					  a a b a a  a c  -> pattern
					0 0 1 0 1 2 'x'   -> when we are at curIdx=5 ,start is at 2 matching 'b' and 'a'
									     here we should need to trace back we trace back to LPS[2]=1
									     which means 0,4 index is matching you need to check if 1,5 is
									     a match or not we check that and put 2 there.
									     if you dont do this step entire LPS array you created will
									     be wrong.the mistake you made is instead of doing like this 
									     you compared idx 5 and 0 since it match you put 1 in idx 5

					next when they dont match and start also 0 we store 0 in LPS array. similarely how
					we creted this LPS array we do pattern matching also we compare patrnIdx and strIdx
					and Trace bace patrnIdx using LPS array. Look code to understand even better

	  Approach 3 -> Using Prefix / Z-Function Algorithm, this is an extension of KMP Algorithm
	  				Takes O(N) time & O(m+n) space. linear time pattern matching algorithm		
					
										pattern + "$" + string

	  				In KMP at first we check if any prefix of pattern exist in pattern right? then 
	  				again we check if pattern exist in sting. in Z function we past the pattern into
	  				the beginning of the string with a special char spliter and we run only the LPS
	  				array creation here. it will check and note all the prefix that matches the suffix.
	  				then finally we check the LPS array if there is any number==len(pattern), if yes
	  				means pattern exist there. so only this method is called prefix function method.
	  				here we call the LPS array as Z Array.
"""	


class Solution:
	#Better Solution -> Boyer-Moore
	def strStr(self, haystack, needle):
		return haystack.find(needle)

	#Optimal Solution 1 -> Rabin Karp using built-in hash          **IMPORTANT**
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return(0)
        patternHash = hash(needle)  #Inbuild HashFunction in python is O(!)
        windowLen=len(needle)
        for i in range(len(haystack)-windowLen+1):
            if hash(haystack[i:i+windowLen])==patternHash:
                return(i)
        return(-1)

	#Optimal Solution 1-> Rabin Karp numeral base
    def strStr(self, haystack: str, needle: str) -> int:
    	#haystack-> string         needle-> pattern
        if needle=="":					#Edge Case
            return(0)
        if len(needle)>len(haystack):   #Edge Case
            return(-1)       

        def findOrder(char): 			  #find the position in our 26 char alone
            return(ord(char)-ord("a"))

        """
        #No need to compare if you are using Rabin carp Rolling has function
        def compare(str1,str2):
            if str1==str2:
                return(True)
            return(False)
        """

        d=ord('z')-ord('a')+1   #122-97   #no for element calculation 26 lower case alphabelt
        HashVal=0                         #HashValue got from pattern (remains same)
        rollHashVal=0					  #HashValue got from window  (changes each time)
        windoLen=len(needle)

        for idx in range(windoLen):       #Finding Hash value for pattern and 1st window 

            #HashVal+=findOrder(needle[idx])*(d**(windoLen-idx-1))
            #rollHashVal+=findOrder(haystack[idx])*(d**(windoLen-idx-1))

            #**IMPORTANT**
            #Both the above two line and below two line dose same thing but if you use that code you
            #will end up with TLE due to calculating power value each time
            HashVal=HashVal*d+findOrder(needle[idx])
            rollHashVal=rollHashVal*d+findOrder(haystack[idx])
        
        popIdx=0                          #Element that will be removed at each iteration from window
        if HashVal==rollHashVal:
            return(popIdx)                #if pattern is found at first index itself        

        for idx in range(windoLen,len(haystack)):  #look limit carefully
        																 #**IMPORTANT**
            rollHashVal-=(findOrder(haystack[popIdx])*(d**(windoLen-1))) #Removing 1st element 
            rollHashVal=rollHashVal*d+findOrder(haystack[idx])			 #Adding Last element
            popIdx+=1

            if HashVal==rollHashVal:
                """
                #No need to compare in Rabin Carp Method
                if compare(haystack[popIdx:(popIdx+windoLen)],needle):
                    return(popIdx)
                """
                return(popIdx)                

        return(-1)


	#Optimal Solution 2 -> KMP Pattern Matching algorithm
    def strStr(self, haystack, needle) :
        if not needle:                           #Edge Case
            return(0)

        LPS=[0]+[0 for i in range(len(needle))]  #Longest suffix that is same as prefix array
        										 #our LPS array size is +1 bigger than orignal pattern
        										 #size, to make track back ease.Look video to understand 
        idx=1
        start=0

        #Filling LPS Array , be carefull with code each line is important **IMPORTANT**
        #you cant use for loop here only while loop is possible.
        while idx<len(needle):

            if needle[start]==needle[idx]: #if both val match increment both idx and store start+1 in LPS
            							   #because start=0 means start+1 =1 we have matched 1st perfix
            							   #start=1 , start+1=2 , we have matched 2nd prefix .... 
                LPS[idx+1]=start+1
                start+=1
                idx+=1

                							#if they do not match we check and start!=0 means there is 
                							# a chance that a prefix may repeat here so we trace back

            elif start!=0:                  #**IMPORTANT**v.v.v.v Edge Case **IMPORTANT**
                start=LPS[start]			#not alone while matching the pattern to string while creating
                							#the LPS array also you should need to track back to possible 
                							#idx ,you spent 2 days to rectify this error
                
											#  0 1 2 3 4 5 6 7  -> LPS Array Indexing 
											#	"a a b a a a c" -> pattern
											#  0 0 1 0 1 2 2 0  -> Correct LPS Array idx[6]=2 not 1
											#  0 0 1 0 1 2 1 0	-> wrong LPS(our mistake)
											#think twise you will understand **IMPORTANT** **IMPORTANT**								


            else:							#if they dont match and start==0 means we increment pointer
                LPS[idx+1]=0				#and store 0 for the current idx in LPS
                idx+=1
        
        strIdx=0
        patIdx=0

        #Matching Pattern using LPS array, similair to how we create LPS we do here matching
        while strIdx<len(haystack) and patIdx<len(needle):
            if haystack[strIdx]==needle[patIdx]:	#if string,pattern match proceed
                strIdx+=1
                patIdx+=1

            elif patIdx!=0:							#if they dont match but patIdx!=0 means check
                patIdx=LPS[patIdx]					#if a prefix match that

            else:									#if not match and patIdx also zero increment strIdx 
                strIdx+=1							#and move on

        if patIdx==len(needle):      #if the whild loop got breaken due to paternLen reached means
        	return(strIdx-patIdx)	 #we have successfully matched a pattern at that index so we
        							 #return that index. **IMPORTANT**
            
        return(-1)

    #Optimal Solution 3 -> using Z function Algorithm extension of KMP
    def strStr(self, haystack, needle) :
        if not needle:
            return(0)

        Z_function=needle+"$"+haystack     #Only change from KMP Code **IMPORTANT**

        LPS=[0]+[0 for i in range(len(Z_function))]
        idx=1
        start=0

        while idx<len(Z_function):
            if Z_function[start]==Z_function[idx]: 
                LPS[idx+1]=start+1
                start+=1
                idx+=1
            elif start!=0:
                start=LPS[start]
                
            else:
                LPS[idx+1]=0
                idx+=1

        if len(needle) in LPS:            #if we have any prefix which is of len(pattern) in LPS array 
        								  # it means we found a pattern **IMPORTANT**
            return(LPS.index(len(needle))-len(needle)*2-1)
        return(-1)