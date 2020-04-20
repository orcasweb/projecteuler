'''
Created on Apr 17, 2020

@author: orcasweb
'''
from math import factorial

'''
Lexicographic permutations
   
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

###
If n digits exists in the number, then the 0th index repeats n!/n times, 
'''
import timeit

start = timeit.default_timer()

#Your statements here

 
NList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ITHPERMUTATION = 1000000
SIZE = len(NList)

# factSize = factorial(SIZE)
# print("The max numbers that can be written is: ", factSize)
# factSizeGroups = int(factSize/SIZE)
# print("Each digit occupies: ",factSizeGroups," numbers")
# print("In a given group.....")
# for x in range(SIZE,0,-1):
#     factSizeGroups = int(factorial(x)/x)
#     quotient = divmod(ITHPERMUTATION, factSizeGroups)
#     print("The ",x," digit repeats ",factSizeGroups ,"the index is ",quotient)

    
def getNumberByGroupPosition(curlist, pos):
    curlistLen = len(curlist)
    grpSize = int(factorial(curlistLen) / curlistLen)
    quotient, remainder = divmod(pos, grpSize)
    
    if(remainder == 0):
        indx = quotient - 1
        pos = remainder
    else:
        indx = quotient
        if(indx != 0):
            pos = remainder
    
    numFound = curlist[indx]
    curlist.remove(numFound)
    return numFound,curlist, pos


finalNumber = []
for i in range(0,SIZE):
    (numFound,curlist,pos) = getNumberByGroupPosition(NList,ITHPERMUTATION)
    finalNumber.append(numFound)
    NList = curlist
    ITHPERMUTATION = pos

print("The final number is :", finalNumber)
finalNumberNew = ""
for x in finalNumber:
    finalNumberNew = finalNumberNew + str(x)
print("The final number is :", finalNumberNew)

stop = timeit.default_timer()
print('Time: ', stop - start) 
