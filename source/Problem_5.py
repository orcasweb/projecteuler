'''
Created on Jan 10, 2019

@author: orcasweb
'''

'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

primes = [2, 3, 5, 7, 11, 13, 17, 19]
cprimes = [0,0,0,0,0,0,0,0]
L = list(range(2, 21))
F = []


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
    

def isEven(n):
    if(n % 2 == 0):
        return True
    else:
        return False


def getPrimeFactors(n):
    factsList = []
    if(isPrime(n)):
        factsList.append(n)
        return factsList
    else:
        ' try divide with primes list'
        for x in primes:
            while(n%x==0):
                factsList.append(x)
                n=n/x
        return factsList
       

for x in L:
    F.append(getPrimeFactors(x))
print(F)

for x in F:
    for y in primes:
        #print(list(x).count(y))
        if(list(x).count(y)>cprimes[primes.index(y)]):
            cprimes[primes.index(y)]=list(x).count(y)
print(primes)
print(cprimes)

result = 1
for x in range(0,len(primes)):
    result = result*primes[x]**cprimes[x]

print(result)
    
            


