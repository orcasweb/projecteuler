'''
Created on Jan 9, 2019

@author: orcasweb
'''
from math import sqrt
'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

givenNum = 600851475143
factsList = []
primeFactsList = []
print(int(sqrt(givenNum)))
upperLimit = int(sqrt(givenNum))
L = list(range(3, upperLimit, 2))
# print(L)
for x in L:
    if(givenNum % x == 0):
        print(givenNum, "is divisible by", x)
        factsList.append(x)
    else:
        pass
# print("The list of primes are: ", factsList)
# print(factsList[::-1])
# now with each element in the factsList, loop the factsList from the right end and check if its a factor
primeFactsList = factsList.copy()
for x in factsList:
    for y in primeFactsList[::-1]:
        if((y != x) & (y % x == 0)):
            primeFactsList.remove(y)
print(primeFactsList)
print("The max prime factor is:",max(primeFactsList))
