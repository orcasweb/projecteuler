'''
Created on May 18, 2020

@author: orcasweb

'''

import itertools as itr


circularPrimes = []
def isPrime(n):

    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if ((n == 2) | (n == 3)): 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True 

def isCircularPrime(n):
    circularPrime = False
    numLen = len(str(n))
    if(numLen == 1):
        circularPrime = True
    else:
        for r in range(0,numLen):
            rtPrime = rotateOnce(n)
            if(isPrime(rtPrime)):
                n = rtPrime
                rtPrime = rotateOnce(n)
                circularPrime = True
            else:
                circularPrime = False
                break
    return circularPrime
            
        
        
    return circularPrime

def rotateOnce(n):
    nList = [int(x) for x in str(n)]
    nList.insert(len(nList), nList.pop(0))
    rtPr = [str(i) for i in nList]
    rtPr = "".join(rtPr)
        
    return rtPr



primesBelowOneMIL = []
# to get primes less than 1 million
for x in range(2,1000000):
    if(isPrime(x)==True):
        primesBelowOneMIL.append(x)
  
# print(primesBelowOneMIL)
print("No of Primes below 1 million: ",len(primesBelowOneMIL))

for p in primesBelowOneMIL:
    if(isCircularPrime(p)):
        circularPrimes.append(p)
print("No of Circular Primes below 1 million: ",len(circularPrimes))


