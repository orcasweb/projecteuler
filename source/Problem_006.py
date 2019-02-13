'''
Created on Jan 11, 2019

@author: orcasweb
'''
'''
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
N = 100
sumSquares = 0
sumSumSquares = 0

def getSquare(n):
    return n**2

def getSumSquares(n):
    result = getSquare(n)
    while(n>0):
        result = result + getSquare(n-1)
        n = n - 1
    return result
def getSquareofSum(n):
    return int(((n*(n+1))/2)**2)
    

print("Sum of squares of n =",N,"is",getSumSquares(N))
print("Square of squares of n =",N,"is",getSquareofSum(N))
print("difference between the sum of the squares of the first one hundred natural numbers and the square of the sum: ", getSquareofSum(N)-getSumSquares(N))
