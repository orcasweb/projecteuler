'''
Created on Jan 15, 2019

@author: orcasweb
'''


def getNumForOdd(n):
    return int(((3 * n) + 1))


def getNumForEven(n):
    return int(n / 2)


def isEven(n):
    return (n % 2 == 0)


maxLimit = 1000000
chainMax = 1
    
for x in range(626331, maxLimit + 1):
    chainLength = 1
    strChain = ''
    collatzNum = x
    strChain = str(collatzNum) + '>'
    while(collatzNum != 1):
        if(isEven(collatzNum)):
            collatzNum = getNumForEven(collatzNum)
            chainLength = chainLength + 1
            strChain = strChain + str(collatzNum) + '>'
        else:
            collatzNum = getNumForOdd(collatzNum)
            chainLength = chainLength + 1
            strChain = strChain + str(collatzNum) + '>'
    if(chainMax < chainLength):
        chainMax = chainLength
        print(x, chainMax)
