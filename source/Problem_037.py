'''
Created on May 19, 2020

@author: orcasweb
'''




'''

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''

# my notes
'''
single digit primes: 2,3,5,7
first and last shall be primes - because last number when truncated should be a prime too
so first and last numbers can consist of only 3,5,7

'''

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

def truncate(n,RLflag):
    if(len(str(n))>1):
        if(RLflag == 'R'):
            trcNum = int(str(n)[0:-1])
        elif(RLflag == 'L'):
            trcNum = int(str(n)[1:])
    else:
        trcNum = n
    
    return trcNum


def isTruncatablePrime(n):
    truncatablePrime = False
    LTruncatable = False
    RTruncatable = False
    curNum = n
    if(len(str(curNum))>1):
        for i in range(len(str(n))):
            curNum = truncate(curNum, 'R')
            if(isPrime(curNum)):
                RTruncatable = True
            else:
                RTruncatable = False
                break
        
        curNum = n
        for i in range(len(str(n))):
            curNum = truncate(curNum, 'L')
            if(isPrime(curNum)):
                LTruncatable = True
            else:
                LTruncatable = False
                break
        
        if(RTruncatable == LTruncatable == True):
            truncatablePrime = True
                
    return truncatablePrime

 
primesList = []
for x in range(8,1000000):
    if(isPrime(x)):
        primesList.append(x)
print(primesList)

truncatablePrimes = []
for primex in primesList:
    if(isTruncatablePrime(primex)):
        truncatablePrimes.append(primex)
        print(primex)
print("Sum of all the truncatable primes is: ", sum(truncatablePrimes))
            
