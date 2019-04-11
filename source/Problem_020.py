'''
Created on Apr 11, 2019

@author: orcasweb
'''
from math import factorial
factNum = 100
finalResult = 0

def getFact(n):
    if(0<n<101):
        if(n==1):
            return 1
        else:
            return n*getFact(n-1)
    else:
        return 1

def getSumIntList(intList):
    global finalResult
    for item in intList:
        finalResult = finalResult + item
    return finalResult
# get the factorial of the number
factN = getFact(factNum)
print(factN)
# convert the factorial to string
# then using map function convert each char in string to int list
# pass the list to the function getSumIntList
print(getSumIntList(list(map(int,str(factN)))))

# ANOTHER WAY TO SOLVE USING THE BUILTIN FUNCTIONS
print(sum(list(map(int,str(factorial(factNum))))))
