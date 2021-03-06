'''
Created on Jan 11, 2019

@author: orcasweb
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
 

primesList = []
n = 2
while(len(primesList)<10001):
    if(isPrime(n)):
        primesList.append(n)
    n = n + 1
print("n is:",n)
print("primesList length is: ",len(primesList))
print("answer is:",max(primesList))

    