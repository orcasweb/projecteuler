'''
Created on Jan 9, 2019

@author: orcasweb
'''
'''
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
maxLimit = 4000000
evenList = []
m = 1
n = 2
currFibNum = 0
#print(m)
#print(n)

evenList.append(n)
while(currFibNum < maxLimit):
    currFibNum = m + n
#    print(currFibNum)
    if(currFibNum % 2 == 0):
        evenList.append(currFibNum)
    m = n
    n = currFibNum
print(evenList)
print("sum of even fibonacci numbers below ",maxLimit, " is ",  sum(evenList))   
    
    
        
