'''
Created on Apr 24, 2020

@author: orcasweb

'''


'''

n^2+an+b, where |a| < 1000 and |b| <= 1000

'''

# -1000 < a < 1000 and -1000<=b<= 1000
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

# primes list that are below 1000000
primesBelow = 10000
primesList = []
for i in range(2,primesBelow):
    if(isPrime(i)):
        primesList.append(i)

def isInPrimesList(n):
    isFound = False
    for p in primesList:
        if(p==n):
            isFound = True
            break
    return isFound


# for x in range(0,40):
#     print(x,pow(x,2)+x+41)
# 
# for y in range(0,80):
#     print(y,pow(y,2)+(-79*y)+1601)

maxLenPrimes = 0
aMax = 0
bMax = 0
pCount = 0
# a has to be odd
for a in range(-999,1000,2):
#   b has to be odd too  
    for b in range(-999,1000,2):
#       now check the function for prime output, starting with n=0
#       if the number is prime continue with next n, if not break mdkfd
        n = 0
        while(True):
            primeNumCheck = pow(n,2)+(n*a)+b
            if(isInPrimesList(primeNumCheck)):
                pCount = pCount + 1
                n = n + 1
            else:
                break
        if(maxLenPrimes < n):
            maxLenPrimes = n
            aMax = a
            bMax = b
            print(maxLenPrimes,aMax,bMax)
print("The Product of the co-efficients of a and b is: ",aMax*bMax)
        

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            