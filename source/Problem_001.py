'''
Created on Jan 8, 2019

@author: orcasweb
'''
from builtins import int
'''
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''
'''
loop from 1 to < 1000 and check if each number is a multiple of 3 or 5 add to a list. then sum the list
how to check if its a multiple of 3 or 5 : while looping multiple the interator with 3 or 5 and the product should be less than the 1000

'''
multList = []
limitNum = 1000
iterateLimit = int(limitNum/3) + 1
L = list(range(1,iterateLimit))
def addToMultList(n):
    print("attempting to add: ", n)
    if(len(multList)==0):
        multList.append(n)
    else:
        if(multList.__contains__(n)):
            pass
        else:
            multList.append(n)
            multList.sort()
    
for i in L:
    if(3 * i < limitNum):
        addToMultList(3*i)
    if(5 * i < limitNum):
        addToMultList(5*i)
print("The answer is :", sum(multList))
        
        
        
    