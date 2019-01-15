'''
Created on Jan 14, 2019

@author: orcasweb
'''
from math import ceil

reqDivCount = 500


def getPrimeFacts(n):
    primeFactsList = []
    if(n < 2):
        return None
    else:
        if(n == 2 | n == 3):
            primeFactsList.append(n)
            return primeFactsList
        else:
            nSqrt = int(abs(ceil(n ** 0.5)))
            for x in range(2, nSqrt + 2):
                while(n % x == 0):
                    primeFactsList.append(x)
                    n = n / x
                
            if(len(primeFactsList) == 0):
                        primeFactsList.append(n)
                
            return primeFactsList                    
    
    
def getDivCount(n):
    divCount = 1
    primeFactsList = getPrimeFacts(n)
    uniqPrimes = set(primeFactsList)
    uniqPrimes = list(uniqPrimes)
    for x in uniqPrimes:
        divCount = (primeFactsList.count(x)+1) * divCount
    return divCount



def getTriangularNum(n):
    return int(((n * (n - 1)) / 2) + n)  # n + n*(n-1)/2


triangularNum = 1
n = 1
divCount = 1
# print(n, triangularNum, divCount)
while(divCount < reqDivCount):
    n = n + 1
    triangularNum = triangularNum + n
    divCount = getDivCount(triangularNum)
print(n, triangularNum, divCount)

