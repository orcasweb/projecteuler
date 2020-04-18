'''
Created on Apr 12, 2020

@author: orcasweb
'''
'''
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
12 is the smallest abundant number
24 is the smallest number that can be written as the sum of 2 abundant numbers
'''

'''
The function will take in a number and return the divisors in a list
'''

LIMIT = 28123
# This list holds all the abundant numbers that are below the LIMIT.
abundantNums = []


def getDivisors(n):
    divisorsList = []
    sqrtn = int(n ** 0.5)
    
    divisorsList.append(1)
    for i in range(2, sqrtn + 1):
        if(n % i == 0):
            divisorsList.append(i)
            'do not add duplicate factors of square numbers and also do not add the number itself'
            if(i != int(n / i)):
                divisorsList.append(int(n / i))
    divisorsList.sort()
    # print(divisorsList)
    return divisorsList 


def isAbundant(n):
    if(sum(getDivisors(n)) > n):
        return True
    else:
        return False


# Loop from 1 until LIMIT + 1, to find out if the number is an abundant number and add to a list
for i in range(1, LIMIT + 1):
    if(isAbundant(i)):
        abundantNums.append(i)

print(abundantNums)
print("The number of abundant numbers below %d is %d"  % (LIMIT,len(abundantNums)))



abundantSumsDict = {}

for x in range(0, len(abundantNums)):
    for y in range(x, len(abundantNums)):
        xySum = abundantNums[x] + abundantNums[y]
        if(xySum <= LIMIT):
            abundantSumsDict[xySum] = xySum
        else:
            break


nonAbundantSum = 0  
for x in range(1, LIMIT + 1):
    if(abundantSumsDict.get(x) != x):
        nonAbundantSum = nonAbundantSum + x
    else:
        pass
  
print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is: ",nonAbundantSum)

