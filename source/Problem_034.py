'''
Created on May 17, 2020

@author: orcasweb
'''

import math as ma


digitFactorials = []
def getDigitFactorialSum(n):
    digitFactorialSum = 0
    numList = [int(x) for x in str(n)]
    for i in numList:
        digitFactorialSum = digitFactorialSum + ma.factorial(i)
    return digitFactorialSum


for x in range(10,999999):
    if(x == getDigitFactorialSum(x)):
        digitFactorials.append(x)
        print(x,getDigitFactorialSum(x))
print("The final answer is: ",sum(digitFactorials))
    

