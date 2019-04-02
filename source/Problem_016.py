'''
Created on Jan 26, 2019

@author: orcasweb
'''

def sumNumDigits(numList):
    if(len(numList) == 1):
        return int(numList[0])
    else:
        return int(numList[0]) + sumNumDigits(numList[1:])

staticNum = 1000
sumNum = sumNumDigits(list(str(2**staticNum)))
print("2 to the power of 1000 is: ",2**staticNum)
print("the sum of 2 to the power of 1000 is:", sumNum)
